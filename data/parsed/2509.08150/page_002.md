In addition to hardware limitations and long context issues, LLM reasoning usually does not follow a formally specified algorithm. Even if it does, the algorithm may be unsound, incomplete, and lack formal guarantees on time/space/optimality. Even if we discount these issues, autoregressive LLMs fundamentally operate sequentially. One could parallelize token generations (e.g., beam search or MCTS), but such task-agnostic parallelization lacks sophisticated coordinations in dedicated parallel algorithms that exploit task characteristics.

Traditional disciplines of computer science instead approach computational tasks with _task decomposition_. For example, a merge sort decomposes a sorting task into smaller sorting tasks and combines the results, where, at the limit, there is an elementary binary comparison over individual pairs. These traditional algorithms, given an accurate oracle, guarantee the correctness of their outputs and the average/worst-case runtime/memory. The opaqueness of LLM’s reasoning prevents such an analysis.

In this work, we propose an abstract framework called "verbalized algorithms". Given an informal representation of a formal task, a verbalized algorithm replaces some atomic operations in a classical algorithm with LLM-driven text-based oracles while _retaining the high-level control flow_, thereby largely retaining the theoretical guarantees. Our work is heavily influenced by _Algorithm with Predictions_ \[Mitzenmacher and Vassilvitskii, 2022, ALPS\] literature, which achieved significant progress in augmenting algorithms with data-driven oracles. There are certainly other work that replaces part of algorithms with LLM oracles, including successor function and goal condition in planning \[Katz et al., 2024\] and collision checking in STRPR \[Djuhera et al., 2025\], yet we believe ours is the first general proposal for the reductionist approach toward LLM reasoning.

We perform four case studies with increasing difficulty and non-triviality: Maximum, sorting, clustering, and submodular maximization. Our implementations are built on top of the offline asynchronous engine of SGLang \[Zheng et al., 2024\], and all experiments are repeated 5 times with different seeds.

**Contributions.** VAs have several key advantages: (1) It is more accurate than classical non-LLM methods or more recent embedding-based or other LLM-based methods, and is also scalable with data parallelism. (2) The reasoning trace of VAs is interpretable, as we have a full understanding of<tbc>

Free-Form Reasoning
Formalization-based Reasoning
Translation Barrier:
Task
Task
Weak models fail at precise translation
Weak models tend to return nonsensical answers
Language Expressivity:
The target language may not be expressive enough for the task
ba-bu, wah !
ba-bu, wah !
translate
Delegate reasoning to symbolic solvers
Even a strong model can't guarantee the correct answer
Lack of Integration: LLM is excluded from reasoning
PDDL
SMT
ASP
Prover9
FAST DOWNWARD
Potasso
Answer:
but it doesn't sound right!
Answer
translate
LLM-modulo-theory
Verbalized Algorithms
Task
Give me more booze!
Task
Known Algorithm
Answer
def fn {...}
constrained decoding
yes/no
Invalid answer! What an idiot...
Route to known algorithms
fn{ left } # recurse fn{ right } # recurse
Predictable correctness
FAST DOWNWARD
Potasso
Symbolic Verifiers
yes/no
runtime
Task requirement
if |y-x|>|zx|:
yes/no
Eventually returns a correct answer but
Weak / strong models can answer simple questions
Language expressivity
How long does it take? {X runtime}
LLM is integrated in algorithmic reasoning
How good is the answer? {X optimality}

Figure 1: Conceptual comparison of various reasoning approaches

