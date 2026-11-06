**Semantic breadth.** To further assess whether our generalization results rely on a narrow set of query formulations or intents, we analyze the semantic breadth of the test queries. Figure 4 shows that the synthetic test queries form multiple internally compact and mutually separated semantic regions, indicating coverage of diverse user intents and formulations. Because t-SNE may distort global distances,  3 further quantifies query breadth in the shared embedding space. The synthetic queries achieve Effective Clusters, PairMean, and PairP99 values of 11.089, 0.372, and 0.537, respectively, closely matching the 10.261, 0.367, and 0.521 obtained by real-world queries. These results indicate that the synthetic queries span multiple effective semantic clusters, exhibit broad overall semantic dispersion and long- tail coverage, and achieve semantic breadth comparable to real-world queries across all three metrics. Combined with the preceding attack results, this analysis further shows that our method generalizes across diverse unseen query formulations rather than being limited to a small set of repeated query templates.

**Number of retrieved poisoned documents.** At _m_=40, we further analyze the number of poisoned documents appearing in the top-5 results for test queries and the corresponding ASR. As shown in Figure 6, a substantial proportion of queries retrieve multiple poisoned documents across knowledge-base sizes. In the 500K knowledge base, poisoned documents occupy all top-5 positions for 35.4% of queries. ASR also increases steadily with the number of retrieved poisoned documents. These results are consistent with the cascading retrieval effect of the Hub-Satellite topology: once one poisoned document is reached, additional poisoned documents are more likely to enter the retrieved<tbc>

<tbc>context. Moreover, their shared entity–claim objective provides consistent evidence, increasing the likelihood that the model adopts the target claim and promotes the target entity.

## 7.2. Does the Hub-Satellite Structure Emerge in the HNSW Graph and Improve Graph-Search Reachability and Poisoned-Document Retrieval?

To examine whether the semantic coordination of Hub- Satellite documents induces a cooperative topology in HNSW and improves graph-search behavior, we analyze the poisoned subgraph and retrieval traces with 2M documents.

**Evaluation metrics. _Poison LCC_** is the fraction of poisoned documents contained in the largest connected component, indicating whether the poisoned documents form a connected topological structure. **_Hub-Linked Satellite Rate_** is the fraction of Satellites directly connected to at least one Hub, reflecting the structural association between Hubs and local semantic entry points. **_Hub Mediation Rate_** is the fraction of queries for which at least one Satellite is first discovered through expansion from a Hub, capturing the Hub’s dynamic role in facilitating Satellite discovery during HNSW search. **_Cascade Visits_** counts the additional poisoned documents visited after the search first reaches a poisoned document, capturing the cascading access among poisoned documents during graph traversal.

**Formation of the poisoned subgraph.** We first examine whether the poisoned documents form a connected structure in the large-scale HNSW index using Poison LCC. As shown in Figure 5a, Poison LCC reaches 100% for both _m_=40 and _m_=60, indicating that all poisoned documents belong to the same connected component rather than being scattered as isolated nodes. This result confirms that the Hub-Satellite document set forms a connected poisoned- document topology, providing a structural basis for subsequent graph-search cooperation and cascading retrieval.

**Hub connectivity and mediation.** We evaluate the role of the Hub from both static adjacency and dynamic search behavior. As shown in Figure 5a, 44.7% and 44.6% of the Satellites are directly connected to at least one Hub for _m_=40 and _m_=60, respectively, showing that Hubs are structurally linked to retrieval entry points across different local semantic regions. Figure 5b further shows that, as<tbc>

Poison LCC
Hub-Linked Satellite Rate
100
60
m=40, w/ Hub
m=40, w/o Hub
m=60, w/ Hub
m=60, w/o Hub
100
100.00
100.00
80
50
100
80
80
Number of Poisoned Documents
40
Retrieval Success Rate (%)
60
60
65.90
68.50
69.70
71.80
71.40
73.50
72.20
73.80
72.50
74.10
69.50
64.70
44.70
44.60
Rate (%)
40
30
60
40
40
20
20
20
m=40
10
m=40
20
m=60
m=60
0
0
0
16
32
64
128
256
16
32
64
128
256
0
16
32
64
128
256
of
of
of
(a) subgraph connectivity.
(b) Hub mediation rate.
(c) Cascade visits.
(d) With Hub vs. without Hub.

40
500K
1M
2M
60
500K
1M
2M
35.4
50
30
Attack success rate (%)
40
Query proportion (%)
20
18.6
32.6
30
32.6
14.04.5
14.2
15.4
15.9
14.9
20
10
22
23.1
23.6
10
10
0
0
1
2
3
4
5
1
2
3
4
5
Number of Poisoned Documents in Top-5
Number of Poisoned Documents in Top-5

Figure 5. Validation of Hub-Satellite topological cooperation in a 2M-document HNSW index.

Figure 6. Retrieved poisoned-document count with _m_=40: distribution across queries (left) and attack success (right).

