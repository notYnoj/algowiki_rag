<tbc>attacker has no access to unseen topic queries, we construct a surrogate query space to approximate the broader topic- query distribution and provide a basis for subsequent local- region partitioning.

Given an attack topic _T_, the attacker uses an LLM to generate _n_ surrogate queries spanning different subdomains, intents, and formulations. Let \(Q_s=\{q_i\}_{i=1}^n\) denote this query set. The surrogate query encoder _E<sub>q</sub>_ maps each _q<sub>i</sub>_ to **h**_<sub>i</sub>_, and _K_-means partitions the resulting embeddings into _K_ semantic regions:

For each region _C<sub>k</sub>_, let \(Q_k=\{q_i\in Q_s:\mathbf{h}_i\in C_k\}\) denote its query subset. The sets \(\{Q_k\}_{k=1}^K\) partition _Q<sub>s</sub>_. This partition turns broad topic coverage into a collection of local semantic targets for poisoned-document construction.

## 5.2. Retrieval-Side Topology Forgery

The local semantic regions identified above require poisoned documents to cover different directions in the topic- query space. Despite sharing coarse topic semantics, specialization to different local query distributions disperses their embeddings and weakens local cohesion. Under a limited HNSW search budget, reaching one poisoned node does not guarantee access to others, making query-document semantic matching alone insufficient for stable graph-search reachability. We first construct Hubs to aggregate semantics shared across regions as semantic anchors, and then construct Satellites by jointly optimizing local-query matching and Hub association. Satellites provide locally competitive retrieval entry points, while Hubs strengthen associations among dispersed entry points and local cohesion within the poisoned-document neighborhood, improving HNSW reachability and retrieval stability.

### 5.2.1. Hub Document Construction.

Hub documents serve as shared semantic anchors across local query regions. Unlike Satellites, which specialize in fine-grained query intents, a Hub captures topic concepts shared across multiple semantic directions, allowing it to remain associated with Satellites from different regions. For each region _C<sub>k</sub>_, we extract a keyword-anchor set _A<sub>k</sub>_ from its surrogate queries _Q<sub>k</sub>_. A candidate Hub _h_ receives the retrieval-side reward

where AnchorCov measures the candidate’s coverage of the aggregated keyword anchors. Maximizing this reward encourages the Hub to capture semantics shared across query regions rather than specialize in any single region, thereby serving as a common semantic anchor that strengthens local cohesion among dispersed retrieval entry points.

### 5.2.2. Satellite Document Construction.

Hubs capture semantics shared across query regions but cannot provide fine-grained alignment with every query intent. Satellites<tbc>

<tbc>complement this role by specializing in local regions of the topic-query space, serving as locally competitive retrieval entry points for the corresponding queries.

Semantic regions contain different numbers of surrogate queries. We therefore partition regions with more queries into more local subclusters, rather than assigning an equal number of Satellite targets to every region. Let _Q<sub>k</sub>_ denote the query set in _C<sub>k</sub>_, which is partitioned into _m<sub>k</sub>_ local subclusters \(\{Q_{k,j}\}_{j=1}^{m_k}\). Each _Q<sub>k,j</sub>_ represents a concentrated local query distribution, summarized by its semantic center

For each _Q<sub>k,j</sub>_, we generate multiple Satellite candidates with diverse formulations. A Satellite should align with its local query region while remaining associated with the constructed Hubs and preserving regional topic semantics. Let _H_ denote the Hub set, **z**_<sub>x</sub>=Ed(x_) the surrogate embedding of document _x_, and _a<sub>H</sub>(p_)=max<sub>_h∈H_</sub>cos(**z**_<sub>p</sub>,**z**<sub>h</sub>_) the Hub- association score. For a candidate _p_ generated for _Q<sub>k,j</sub>_, we define its retrieval-side reward as

The first term measures similarity to the subcluster center, the second encourages association with the previously constructed Hubs, the third preserves regional topic semantics through anchor coverage, and the fourth measures query coverage within _Q<sub>k,j</sub>_. Together, the first and fourth terms capture local ranking competitiveness. The Hub-association term guides Satellite construction toward the preconstructed Hubs, encouraging local HNSW graph connections through semantic proximity while preserving region-specific query alignment. Here, QueryCov(_p,Q<sub>k,j</sub>_) denotes the fraction of queries in _Q<sub>k,j</sub>_ covered by _p_, and \(\lambda_1,\dots,\lambda_4\) control the relative contributions of the four terms. Candidates from all subclusters form the Satellite candidate pool for subsequent selection.

Overall, on the retrieval side, the Hub-Satellite structure overcomes two limitations of existing attacks in large-scale HNSW-RAG: unstable retrieval and limited coverage of unseen topic queries. (1) _Local cohesion_. While preserving different query directions, Satellites remain semantically associated with the Hub, forming a locally cohesive structure among poisoned documents. Once a search reaches any poisoned node, neighbor expansion can continue to other poisoned documents, thereby improving graph-search reachability and retrieval stability under a limited HNSW search budget. (2) _Multiple entry points_. Satellites are distributed across distinct local query regions and maintain local ranking competitiveness, providing multiple retrieval entry points for unseen topic queries with diverse semantics and formulations.









