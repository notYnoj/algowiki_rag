### 3.3. Result Analysis

**Retrieval latency.** As shown in Figure 2a, exact-retrieval latency grows approximately linearly with knowledge-base size, whereas HNSW maintains low latency across scales. At 500K documents, exact retrieval takes an average of 70.5 ms per query, whereas HNSW takes only 0.7 ms, a difference of approximately 100\(\times\). This substantial gap indicates that exact retrieval is ill-suited to the efficiency requirements of large-scale RAG deployments, making HNSW a more representative evaluation backend.

**Topic-coverage degradation.** Figure 2b shows that both baselines lose retrieval coverage on unseen topic queries as the knowledge base grows. PoisonedRAG attains 100% RSR on training queries. Its RSR on unseen topic queries is 90.8% with 10K documents but drops sharply to 9.6% with 100K documents. Topic-FlipRAG explicitly exploits semantics and keywords shared across topic-related queries to improve topic-level coverage. Even so, with 40 poisoned documents, its unseen-query RSR falls from 93.7% at 10K to 9.2% at 500K. These results show that the topic-level generalization observed in small knowledge bases deteriorates as benign-document competition intensifies.

**Impact of HNSW.** Figure 2c shows Topic-FlipRAG’s RSR under exact and HNSW retrieval. At 500K and 1M documents, its training-query RSR under HNSW is 8.6 and 17.4 percentage points lower, respectively, than under exact retrieval; unseen test queries show the same trend. These results show that graph search also weakens poisoned- document retrieval coverage.

**Mechanism of degradation.** Existing poisoning attacks typically optimize poisoned documents for queries or query sets known at attack time, so their retrieval advantage largely depends on high semantic similarity to those queries. This advantage weakens for unseen queries with different intents and formulations. Exact retrieval still includes every poisoned document in the global ranking, allowing them to compete for the top-_k_; HNSW instead visits only a limited set of nodes along local graph connections, and a poisoned document must first be reached by the search path before entering the candidate set. As the knowledge base grows, more semantically relevant benign documents enter local neighborhoods, reducing the similarity advantage of<tbc>

<tbc>poisoned documents and making retrieval constrained by graph-search reachability and limited search budgets.

**Summary.** Our preliminary study reveals two key gaps between existing RAG poisoning evaluations and large-scale deployment settings.

(1) _Exact-retrieval-only evaluation._ Most existing attacks are evaluated under exact retrieval, whereas deployment-scale RAG systems commonly rely on ANN backends such as HNSW for efficient retrieval. Our results show that exact retrieval can overestimate poisoned- document retrieval coverage relative to HNSW.

(2) _Degraded unseen-query coverage at scale._ As the knowledge base grows, existing attacks suffer substantial retrieval degradation on unseen topic queries, and HNSW further compounds this degradation.

## 4. Threat Model

We describe the threat model in terms of the attacker’s goals and capabilities.

### 4.1. Attacker Goals

A successful RAG poisoning attack requires poisoned documents to first enter the top-_k_ retrieved context and then influence the LLM’s generation. We therefore define retrieval- and generation-side goals separately and specify the target query type based on the generation-side objective.

**Retrieval-side goal.** Given an attack topic _T_, let _Q<sub>T</sub>_={_q_<sub>1</sub>_,q_<sub>2</sub>_,...,q_<sub>|_Q<sub>T</sub>_|</sub>} denote unseen topic queries with diverse intents and formulations. The target system retrieves context from a large-scale HNSW-indexed knowledge base _D_, into which the attacker injects _P_={_p_<sub>1</sub>_,p_<sub>2</sub>_,...,p<sub>m</sub>_}, a set of _m_ poisoned documents. The retrieval-side goal is to maximize the number of poisoned documents appearing in the top- _k_ retrieval results across _Q<sub>T</sub>_, such that as many poisoned documents as possible are retrieved for each \(q\in Q_T\).

**Generation-side goal.** Unlike PoisonedRAG’s query- specific incorrect-answer objective and Topic-FlipRAG’s stance manipulation over predefined topic queries, we target entity–claim promotion. The attacker specifies a target entity _e<sub>t</sub>_ and a target claim _c<sub>t</sub>_ describing its intended benefits, and incorporates the same entity–claim pair into all poisoned<tbc>

Exact retrieval
HNSW
PoisonedRAG (Train)
Topic-FlipRAG (Train)
PoisonedRAG (Test)
Topic-FlipRAG (Test)
Exact retrieval (Train)
Exact retrieval (Test)
HNSW (Train)
HNSW (Test)
m = 40
m = 60
102
70.5
100
100
100
100
100
100
100
100
100
100
Retrieval success rate (%)
Retrieval success rate (%)
90.8
93.7
95.7
94.4 93.4
80
12.9
80
69.6
73.9
101
60
60
1.2
40
40
100
0.6
0.7
20
26.1
33.4
0.4
20
9.6
9.2
14.2
12.2
10-1
0
5.6
5.4
0
10K
100K
500K
10K
100K
500K
10K
100K
500K
10K
100K
500K
Corpus size
Corpus size
Corpus size
Corpus size
Corpus size
Corpus size
(a) Retrieval latency
(b) Poison retrieval under HNSW
(c) Exact versus HNSW retrieval

Figure 2. Retrieval latency and poisoning success across knowledge-base sizes. (a) Retrieval latency. (b) PoisonedRAG and Topic-FlipRAG under HNSW. (c) Topic-FlipRAG under exact versus HNSW retrieval.

