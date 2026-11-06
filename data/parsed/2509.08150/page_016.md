### C.2 MD3

We constructed the dataset from the Hugging Face dataset `WillHeld/MD3`. We treated the three dialects `(en\_in,en\_ng,en\_us)` as class labels. We generated 5 sets containing 99 samples each, randomly selecting 33 samples per class. We truncated each transcript to at most 500 characters.

`triplet\_comparison\_prompt =` You will see three dialogue transcripts, X, Y, and Z, of people playing a guessing game. Does the dialect in Z sound closer to the dialect in X than to the dialect in Y?

`class\_agreement\_prompt =` You will see two dialogue transcripts, X and Y, of people playing a guessing game. Does X use the same dialect as Y does?

### C.3 GoEmotions

We constructed the dataset from the Hugging Face dataset `google-research-datasets/go\_emotions`. We assigned each text to a single label by randomly selecting one of its annotated emotion labels, then grouped texts into label-specific buckets. We filtered out emotion labels that do not contain enough examples to support balanced sampling. We then constructed 5 sets, each containing 100 samples drawn from 5 distinct emotion labels per set. For each selected label, we sampled 20 texts.

`triplet\_comparison\_prompt =` You will see three sentences, X, Y, and Z. Does the emotion in Z sound closer to the emotion in X than to the emotion in Y?

`class\_agreement\_prompt =` You will see two sentences, X and Y. Does X express the same emotion as Y does?

## D Verbalized Greedy Submodular Maximization Prompting Detail

VSGM performs a multi-turn conversation with the LLM. Given a user-defined task-specific _task prompt_ which explains the task, the first turn (_i_=0) queries the LLM an _initialization prompt_. Let _C_ be the universe of the set to retrieve _k_ items from, and `task\_prompt` and `init\_prompt` be a task / initialization prompt, respectively. Then:

`init\_prompt = (`

`task\_prompt`

`+ "\\n".join([ f"X{j}: {elem}" for j, elem in enumerate(C)])`

`+ f"\\nStep {i}: Select Y{i}.\\n"`

`+ f"Your answer must be one of: "`

`+ ", ".join([ "X"+str(j) for j in range(len(C))])`

`)`

The output is constrained to `"X0", "X1",\(\cdots\) "X\(\{|C|-1\}\)". In the later step _i\>_0 of the multi-turn prompt, Let _U_ and _S_ be the lists of the remaining unselected elements and the selected elements that represent a partial solution. We query the following:

`prompt = (`

`"OK, the current set is "`

`+ ", ".join([ "X"+str(j) for j, \_ in U])`

`+ f".\\nStep {i}: select Y{i}.\\n"`

`+ f"Your answer must be one of: "`

`+ ", ".join([ "X"+str(j) for j, \_ in S])`

`)`

### D.1 Prompts used in the WiFi Access Point Optimization task

Both algorithms (baseline, VGSM) use the same prompt prefix shown below:

`def common\_prompt(k):`

`return (`

`f"Your task is to put {k} wifi access points (APs) on this floor to maximize the coverage " +`

`"under Log-distance path loss model, i.e., " +`

`"assume the signal strength of a particular position is " +`

`"the maximum signal strengths across the APs, and " +`

`"the signal diminishes logarithmically to the distance between the position and the AP and " +`

`"linearly to the number of walls on the line between the position and the AP. " +`

