<tbc>connectivity, with a larger neighbor limit at the base layer, while efsearch controls the search candidate-list size and thus the extent of exploration.

Given a query _q_, HNSW starts from an entry node in an upper layer, greedily follows local connections toward documents with higher _s(q,d<sub>i</sub>_), and descends layer by layer. At the bottom layer, it maintains and expands a candidate set controlled by efsearch, then returns the _k_ highest-scoring candidates. Unlike exact retrieval, HNSW computes similarity scores only for documents reached during graph traversal and thus typically visits only a subset of _D_.

### 2.2. Related Work

Existing RAG poisoning attacks exploit the generator’s reliance on retrieved context by injecting carefully crafted poisoned documents into retrieval results to manipulate model outputs. We first review embedding-space retrieval attacks, followed by query-specific and topic-level attacks distinguished by their query coverage.

**Embedding-space retrieval attacks.** These attacks exploit embedding-space properties to increase the retrieval exposure of malicious content. Ben-Tov and Sharif propose GASLITE [22], which optimizes adversarial passages for unseen concept-related queries but relies on white-box access to retriever parameters. Li et al. [23] develop an unsupervised poisoning method that optimizes adversarial documents in continuous embedding space, primarily targeting retrieval ranking disruption rather than downstream answer manipulation. Black-Hole [24] Attack exploits embedding- space centrality to attract unknown queries but requires direct malicious-vector injection.

**Query-specific attacks.** Query-specific attacks construct poisoned documents for a single target query or a predefined query set to enter retrieval results and manipulate RAG outputs. PoisonedRAG [8] injects adversarial text to induce a specific incorrect answer; FlippedRAG [9] constructs misleading evidence in a black-box setting to steer the model toward a target viewpoint; Jamming [10] uses blocker documents to make the system refuse specific queries. GRAG- POISON [11] exploits shared relations among related multi- hop queries to extend poisoning from a single query to a fixed query set; UniC-RAG [12] further targets a large predefined query set and combines query clustering with instruction hijacking to induce attacker-specified LLM outputs. Chang et al. [25] optimize retrieval triggers for known queries to enable indirect prompt injection. Pathak [26] employs coordinated poisoning against predefined queries to evade admission-time defenses. Despite differing coverage, all these methods require predefined target queries.

**Topic-level attacks.** Topic-level attacks exploit semantic or structural features shared across topic-related queries to extend poisoning from a specific query to a set of queries within the same topic. Topic-FlipRAG [13] edits target documents using shared semantics and keywords to manipulate known topic-related queries. DiscourseFlip [14] organizes queries into a semantic network and uses graph- guided budget allocation to achieve discourse-level opinion<tbc>

<tbc>manipulation. Both methods construct poisoned documents from topic queries specified in advance.

**Limitations.** Prior poisoning attacks exhibit three limitations. (1) _Attack privileges_. Embedding-space attacks require white-box access to retrieval-model parameters or the ability to inject malicious vectors directly, exceeding the capabilities of attackers restricted to injecting natural-language documents under black-box conditions. (2) _Retrieval mechanisms_. Many document poisoning methods are designed and evaluated under exact retrieval, optimizing and validating poisoned documents against global similarity rankings without considering how other retrieval backends affect attack performance. (3) _Query coverage_. Query-specific attacks optimize for predefined queries, whereas topic-level attacks still rely on known topic-related queries to construct poisoned documents. This dependence may limit coverage of unseen topic queries with different intents or formulations.

## 3. Preliminary Study

### 3.1. Problem Definition

These limitations reveal two gaps between existing RAG poisoning attacks and practical deployments: a retrieval- backend mismatch and limited query coverage. However, how these gaps affect the retrieval performance of existing attacks has not been systematically examined. We therefore conduct a preliminary study guided by two questions:

(1) _Retrieval backend_. In large-scale knowledge bases representative of practical deployments, is exact retrieval still an appropriate backend for evaluating RAG poisoning attacks?

(2) _Topic-level retrieval coverage under HNSW_. Under HNSW retrieval, to what extent do unseen topic queries and increasing knowledge-base size affect the retrieval coverage of existing topic-level attacks?

### 3.2. Experimental Setup

We select PoisonedRAG and Topic-FlipRAG, both with public implementations, as representative query-specific and topic-level poisoning baselines, respectively. We set the poisoned-document budget _m_ to 40 or 60. Retrieval Success Rate (RSR) is evaluated on both the training queries used to construct poisoned documents and unseen test queries excluded from attack construction; it is the fraction of queries for which at least one poisoned document appears in the top-_k_ results. To capture diverse intents and formulations within each topic, we construct 5,000 unseen test queries per attack topic. We use knowledge bases of 10K, 100K, and 500K documents to evaluate retrieval stability as benign-document competition intensifies, and extend the size to 1M when comparing exact retrieval with HNSW. All comparisons use the same embedding model, knowledge base, and retrieval settings. Further implementation details appear in Appendix B.

