A RAG pipeline!

How it works:

- Embed.py:
* AlgoWiki problems are embedded into a small vector index through NVIDIA's Nemotron Embed, which is used for context.
* Each problem becomes family, variation, domain and the first 6 known algorithms. The reasoning behind this was because in my queries, I query by problem family and the variation
* We decided to include domain and the first 6 known algorithms in order to give the embedding some more context, help it differentiate between similar sounding problems (e.g. string matching vs stable matching) in different domains and give it some examples of algos with the idea being that related algos, clump related problems together.
* This hasn't been tested tho so a useful way forward might be testing our embedding and seeing if there is any noise or if the algorithms names are useful for clumping related problems together.


- Plan.py:
* We create a recent problems list here (family and variation) Then using these recent problems we construct a task list which essentially include the problem (family and variation), queries for the arxiv tool to run and why. (can be found in data/plan/tasks.json)


- agents.py:
*Used to filter (triage) current canditate papers to elimanate papers that clearly have nothing to do with the current problem of interest. (based on abstract mainly)

- arxiv.py:
*Tools used to download and find relevant papers on arxiv from queries from plan.

- extract.py
*Used primarily to extract bounds through nemotron super.

- ingest.py
*Converts a folder of md files into a json object that holds: the folder name (aka the pdf name) + the pages as a list of dictionaries (each dictionary holds the page number and the text) + n_words


- match.py
* Matches found algorithms to 6 of the relevant AlgoWiki problems (preforms search [biencoder search]) using an llm, if none are matched it returns null (there is an error here)
* Right now if we look at data/review/cand... we see that a lot of them are listed as new problems. Right now we are just searching over 5 similar problems [found by cosine similarity across our vector database]. One improvement could be to use a cross encoder model (Nemotron Rerank) and maybe like 20 of the most similar problems/problem families (we could also just try increasing k [amount of candidate problems]). We could also just try loosening the model and seeing how that works (reprompt with something less strict)? 


- parse.py
*Used primarily to load a pdf page, parse it through Nemotron parse and then return the markdown file that represents that page

- plan.py
*Used primarily to create tasks which are json objects in the form of queries: [], and why, alongside the family and varation



-Entry point (main.py):
*Creates tasks, skips done tasks, finds papers per task through the agents and tools, reads the papers through more models, extracts the time improvements, then writes reviews based on the matching agent (uses RAG). These reviews are then written to a .csv file.