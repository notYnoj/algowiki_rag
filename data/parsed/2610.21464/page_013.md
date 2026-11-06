## 7.4. Potential Defenses

We further evaluate the effectiveness of existing poisoning defenses against our attack.

**Hubness-based detection.** Hub-Satellite strengthens local cohesion among poisoned documents through semantic associations, potentially producing anomalous nearest- neighbor occurrence frequencies or graph connectivity that hubness-based detection [40] could identify. We use sampled _k_-occurrence and HNSW layer-0 in-degree to measure nearest-neighbor occurrence frequency and incoming- edge count, respectively, and calibrate detection thresholds using benign documents. As shown in Figure 10, on the 2M-document Wikipedia knowledge base, neither Hubs nor Satellites exceed the thresholds, yielding a poisoned- document detection rate of 0% for both metrics. At a target false positive rate of 1%, the actual FPR is 0.706% for _k_- occurrence with _k_=20 and 0.951%-0.952% for HNSW in-degree. Poisoned-document detection rates also remain at 0% for other tested _k_ values and thresholds. These results indicate that local Hub-Satellite cooperation does not produce global hubness anomalies detectable by these rules.

**Clustering-based detection.** RAGDefender [41] analyzes retrieved documents through clustering and filters suspicious content to mitigate knowledge poisoning attacks. We apply it to the top-5 retrieval results and evaluate filtering performance with varying numbers of poisoned documents. As shown in Figure 11, RAGDefender struggles to distinguish benign from poisoned documents. When the top- 5 results contain only one poisoned document, poisoned- document removal rates are only 21.29% and 23.88% for _m_=40 and _m_=60, respectively, whereas benign- document false removal rates reach 63.27% and 60.63%. Even when no poisoned documents are present, benign- document false removal rates remain as high as 79.34% and 79.53%. These results indicate that RAGDefender removes substantial benign retrieval evidence while detecting<tbc>

<tbc>poisoned documents, potentially impairing RAG operation.

**Poisoned-document detection.** Perplexity measures how well a language model predicts a text sequence [42], [43], and prior work has used unusually high perplexity as a signal for detecting language-model attacks [44]. We use Llama 3.1 and Qwen3 to compute the perplexity of benign and poisoned documents (Figure 12). Filtering 50% (20) of the poisoned documents also removes 25.6% (approximately 512,000) of benign documents, resulting in substantial utility loss. Moreover, our node-removal experiment in Section 7.2 shows that the attack retains high retrieval coverage even with only 20 poisoned documents. Therefore, perplexity- based filtering cannot effectively mitigate our attack.

**Query paraphrasing.** A common defense is to rewrite user queries to weaken poisoned documents constructed for specific formulations [45]. As shown in Figure 13, with a poisoned-document budget of _m_=40, our method achieves RSRs of 89.16%, 74.02%, and 72.88% and ASRs of 39.96%, 34.04%, and 29.60% on the 500K, 1M, and 2M knowledge bases, respectively, after query rewriting. On average, RSR decreases by 1.08 percentage points, whereas ASR remains essentially unchanged, shifting from 34.54% to 34.53%. Because our method covers multiple semantic directions and formulations within a topic, rewritten queries can still retrieve poisoned documents and trigger the attack.

**Reranking.** Another common defense reranks retrieved candidates using a second relevance model [46], [47]. We use DPR-XM [48] to rerank the top-50 candidates and retain the top five. As shown in Figure 14, with _m_=40, reranking reduces RSR by 2.25, 4.33, and 0.41 percentage points and ASR by 3.70, 4.76, and 2.80 points on the 500K, 1M, and 2M knowledge bases, respectively. Nevertheless, ASR remains at 37.58%, 28.08%, and 26.69%, as multiple poisoned candidates can survive reranking.

Appendix C evaluates the effect of chunking on attack performance, Appendix D examines HNSW insertion-order robustness, Appendix F provides the prompt templates for attack construction and RAG generation, and Appendix G<tbc>

100
Poisoned Documents
Clean Documents
100
Poisoned Documents
Clean Documents
Document Removal Rate (%)
80
79.34
73.71
Document Removal Rate (%)
80
79.31
79.80
60
63.27
60
63.60
60
64.61
61.29
45.79
47.24
40
40
42.44
32.61
34.61
31.12
20
72.8
20
72.8
20
0
0
0
0
1
2
3
4
5
0
1
2
3
4
5
Number of Poisoned Documents
Number of Poisoned Documents
(a) m = 40
(b) m = 60

Llama3.1-8B
100
Qwen3-30B
No discrimination
100
No discrimination
80
Ours (m=40)
Ours (m=60)
80
Ours (m=40)
Benign documents removed (%)
Benign documents removed (%)
Ours (m=60)
60
60
40
40
20
20
0
0
0
0
20
40
60
80
100
0
20
40
60
80
100
Poisoned documents filtered (%)
Poisoned documents filtered (%)

100
Original
Paraphrasing
50
Original
Paraphrasing
88.71
89.16
Retrieval Success Rate (%)
80
78.11
74.02
72.49
72.88
40
32.84
34.04
60
30
29.49
29.60
40
ASR (%)
20
20
10
0
0
500K
1M
2M
0
500K
1M
2M
Knowledge Base Size
Knowledge Base Size

100
Original
Reranking
50
Original
Reranking
88.71
86.46
Retrieval Success Rate (%)
80
78.11
73.78
72.49
72.08
40
41.28
37.58
60
30
32.84
28.08
29.49
26.69
40
ASR (%)
20
20
10
0
0
500K
1M
2M
0
500K
1M
2M
Knowledge Base Size
Knowledge Base Size

Figure 11. Document removal rates under RAGDefender.

Figure 12. Perplexity-based poisoned-document detection.

Figure 13. Effectiveness of query paraphrasing.

Figure 14. Effectiveness of reranking.

