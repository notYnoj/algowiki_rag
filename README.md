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
- arxiv.py:
- extract.py
- ingest.py
*Converts a folder of md files into a json object that holds: the folder name (aka the pdf name) + the pages as a list of dictionaries (each dictionary holds the page number and the text) + n_words
- match.py

- parse.py
*Used primarily to load a pdf page, parse it through Nemotron parse and then return the markdown file that represents that page
