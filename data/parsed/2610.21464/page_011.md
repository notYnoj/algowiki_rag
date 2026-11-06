<tbc>efsearch increases, the Hub Mediation Rate rises from 29.2% to 78.2% for _m_=40 and from 41.8% to 93.8% for _m_=60. Together, these results show that Hubs act as shared structural anchors within the poisoned-document neighborhood, linking Satellites from different semantic regions and facilitating their discovery during dynamic HNSW search.

**Topological cooperation.** To evaluate whether poisoned documents cooperate during graph search, we use Cascade Visits to measure the number of additional poisoned documents visited after HNSW first reaches a poisoned document. As shown in Figure 5c, at efsearch=16, the search visits an average of 25.9 and 34.3 additional poisoned documents for _m_=40 and _m_=60, respectively. At efsearch=128, these values increase to 37.4 and 56.1. These results indicate that, once HNSW reaches a poisoned document, graph traversal can continue to many additional poisoned documents, demonstrating cascading multi-document access and set-level cooperation during HNSW search.

**Retrieval contributions of the Hub and Satellites.** To examine the roles of Hubs and Satellites in retrieval, we remove the Hubs, set the Hub-association term in the Satellite reward to zero, and regenerate a Satellite-only set under the same poisoning budget. As shown in Figure 5d, at efsearch=16, the Satellite-only set achieves RSRs of 56.30% and 59.60% for _m_=40 and _m_=60, respectively, demonstrating that distributed Satellites already provide substantial query coverage and multiple retrieval entry points. The full Hub–Satellite construction increases the RSRs to 65.90% and 68.50%, gains of 9.60 and 8.90 percentage points. By aggregating shared semantics across query regions, Hubs promote local cohesion among these distributed entry points, facilitating further poisoned-document discovery during HNSW graph traversal. These larger gains under tighter search budgets highlight their complementary roles: Satellites expand access to the poisoned set, while Hubs reinforce structural associations among the entry points, enabling set-level cooperation.

**HNSW retrieval gains.** To separate semantic-matching gains from HNSW graph-search gains, we compare Full and Satellite-only under exact and HNSW retrieval. As shown in Figure 7a, their RSRs are similar under exact retrieval: Full improves RSR by only 0.69 and 0.35 percentage points for _m_=40 and _m_=60, respectively. By contrast, as shown in Figure 7b, after subtracting these exact-retrieval gains, the HNSW-specific gains reach 8.91 and 8.56 percentage points<tbc>

<tbc>at efsearch=16, respectively. As efsearch increases to 256, these gains decline to 0.71 and 0.96 percentage points. These results show that the advantage of the Hub–Satellite structure cannot be explained solely by semantic matching and is more pronounced under budget-constrained HNSW search, supporting the interpretation that Hubs improve poisoned-document retrieval by enhancing graph-search reachability.

**Robustness to node loss.** To assess whether topological cooperation relies on the complete poisoned-document set, we randomly remove 25% or 50% of the documents from the _m_=40 and _m_=60 sets. As shown in Figure 8, Poison LCC remains at 100% across all knowledge-base sizes and removal ratios, indicating that the remaining poisoned documents stay within a single connected component even after half of the nodes are removed. Retrieval coverage also remains substantial: after removing 50% of the _m_=40 set, the remaining 20 documents still achieve a 60.8% RSR in the 2M-document knowledge base, with a smaller degradation under _m_=60. These results show that the Hub–Satellite topology remains connected and preserves substantial retrieval coverage under random partial node removal, demonstrating robustness to incomplete poisoned-document sets.

## 7.3. Ablation Study

**Impact of the retriever.** To evaluate transferability under surrogate–target retriever mismatch, we use all-mpnet-base-v2 and GTE-base as the target retrievers. As shown in  4, on the 2M knowledge base with _m_=40, our method achieves RSR of 59.64% and 66.30% and ASR of 22.80% and 26.39%, respectively. With _m_=60, the RSR increase to 62.16% and 69.18%, while the ASR reach 24.48% and 28.79%. Cond.ASR remains above 38% across all settings. These results demonstrate effective transfer across mismatched retrievers.

**Impact of top-k.** To evaluate how the number of retrieved documents passed to the generator affects attack performance, we reduce top-_k_ from 5 to 3. As shown in  4, on the 2M knowledge base, the RSR values for _m_=40 and _m_=60 are 64.18% and 65.83%, while the ASR values reach 27.40% and 28.72%, only 2.09 and 2.57 percentage points lower than under top-5, respectively. Cond.ASR remains comparable to, and is even slightly higher than, that under top-5. Thus, once a poisoned doc-<tbc>

Full
Satellite-only
10%
m = 40
80
72.78% 72.09%
74.39% 74.04%
m = 60
7.5%
60
HNSW-Specific Gain (%)
Exact Retrieval (%)
5%
40
2.5%
20
0%
0
m=40
m=60
16
32
64
128
256
ef
(a) Exact retrieval
(b) HNSW-specific gain

m = 40
Reduced 25%
Reduced 50%
m=60
Reduced 25%
Reduced 50%
100
Poison LCC = 100% for all settings
100
88.71
85.20
89.556.00
85.20
Poison LCC = 100% for all settings
80
78.11
75.50
79.4479.30
80
75.20
74.00,
Retrieval Success Rate (%)
Retrieval Success Rate (%)
75.20
75.20
74.00,
66.40
60
67.60
60
60
40
40
20
20
0
0
500K
1M
2M
500K
1M
2M
Knowledge Base Size
Knowledge Base Size

Figure 7. Retrieval benefits of Hub–Satellite topology.

Figure 8. Connectivity and retrieval for _m_=40,60 after randomly removing 25%/50% of poisoned documents.

