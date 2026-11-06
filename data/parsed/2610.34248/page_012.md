<tbc>with the cluster-probe count _n<sub>probe</sub>_. We further ablate the graph degree \(M\in\{16,32,64,128,256\}\) across all 10 datasets in the extended version \[49\]; the WAN advantage holds throughout the _M_ sweep.

**End-to-end RAG Quality.** We evaluate end-to-end RAG on 200 multi-hop queries sampled from HotpotQA \[46\] with retrieval over the 1M-document MS MARCO passage corpus. Queries and documents are embedded with `inffloat/e5-large-v2` \[41\], we retrieve the top-10 passages, and `Qwen2.5-7B-Instruct` \[33\] generates answers, with Exact Match and token-level F1 as metrics. We sweep _C_ in  4 to characterize RAG quality as _C_ varies. It shows that HNSecW matches the standard HNSW at _C_=7 and larger _C_ gives negligible improvement, so our termination strategy in Section 4.1 achieves similar RAG quality to standard HNSW.

### 7.3 Efficiency of HNSecW

We next compare HNSecW’s efficiency and scaling for single, multiple, and batch queries.

#### 7.3.1 Single-Query Scenario.

We first examine single-query cost on the four datasets, shown in Figure 9. In 2PC, HNSecW is 4-22\(\times\) faster than PANTHER on WAN and reduces communication by 7-46\(\times\) (excluding BIGANN-1B, where existing DORAM cannot fit a PANTHER cluster; see Figure 9 caption). The gap widens against SORT in 3PC, reaching 111\(\times\) to 1.6k\(\times\) on WAN and 185\(\times\) to 617\(\times\) in communication. The ablation in the bottom row of Figure 9 decomposes WAN time and Communication into Secure distance, Visited check, and Oblivious sort. WAN is round-dominated, since Visited check and Oblivious sort account for 60% to 90%. The Secure distance share rises with _d_, from about 10% at DEEP-100M (_d_=96) to about 30% at GIST-1M (_d_=960) under 2PC. This share is smaller in 3PC because replicated sharing reduces distance-computation overhead. For Communication, distance bytes dominate at high _d_, reaching about 78% on GIST-1M 2PC, while Visited check and Oblivious sort take larger shares at low _d_.

We further check whether HNSecW keeps its WAN advantage across the _ef_<sup>(0)</sup> ablation in Figure 8, which plots WAN 2PC latency against top-10 recall. At the same recall, HNSecW’s 2PC WAN curve sits below PANTHER’s _n<sub>probe</sub>_ sweep on every dataset where PANTHER runs across the full \(ef^{(0)}\in\{k+1,\dots,k+50\}\) sweep, so the WAN advantage is robust to the choice of _ef_<sup>(0)</sup>.

#### 7.3.2 Multiple- and Batch-Query Scenarios.

We sweep _U_ under WAN and report per-query amortized latency and communication in Figure 10, combining online search with offline reshuffle divided by _U_. At small _U_ the reshuffle dominates; as _U_ grows its share falls linearly while the online share grows slowly, so the amortized total drops toward the online floor. HNSecW crosses below PANTHER once _U_ amortizes the offline cost. The batch variant starts below<tbc>

<tbc>the multi-query curve at small _U_ by sharing one parallel reshuffle. The crossover _U_ varies with _N_ and _d_, but all four datasets follow the same trend.

## 8 RELATED WORK

**Approximate Nearest Neighbor (ANN).** ANN enables scalable similarity search in high-dimensional embedding spaces where exact _k_NN is often too expensive \[29, 30, 43\]. Classical methods include tree-based partitioning \[5\], locality-sensitive hashing \[22\], and vector quantization \[23\]. Graph-based indexes, such as HNSW \[32\] and NSG \[17\], dominate in practice, building proximity graphs for greedy query traversal. Recent systems extend graph-based ANN with improved indexing and retrieval strategies \[24, 42, 52\], while vector databases deploy these methods at scale \[10, 20, 40\].

**Secure ANN.** Prior work considers secure ANN under several threat models. When the database is public but the query is private, Tiptoe \[21\] searches a small candidate subset selected via clustering, trading accuracy for sublinear bandwidth and latency. Wally \[2\] further improves this pipeline’s throughput by batching queries, while Preco \[35\] reduces communication using two non-colluding servers. Pacmann \[50\] goes beyond clustering-based ANN methods by building a graph-index under query privacy. When both the database and query are private under a single owner (encrypted outsourcing), Compass \[51\] directly uses ORAM only to hide the server-side data access pattern, while executing the search logic in plaintext on the client. Instead, HERS \[15\] scans the encrypted database with FHE at high computational cost. SANNS \[11\] and PANTHER \[28\] use secure two-party computation between a server owning the database and a client owning the query. SANNS proposes a clustering-based secure ANN with optimized distance computation and top-_k_ selection, while PANTHER further improves end-to-end performance. In contrast, HNSecW secret-shares the query, database, and index among computation servers and achieves the same logarithmic complexity as the non-private setting. Notably, both SANNS \[11\] and PANTHER \[28\] can be adapted to secret-shared inputs. How ever, both approaches have \(O(\sqrt{N})\) complexity. Moreover, several early works \[34, 36, 38, 53\] studied secure _k_NN protocols, but they either target smaller-scale settings or apply only to the specialized secure settings discussed above.

## 9 CONCLUSION

We present HNSecW, an MPC ANN protocol with _O_(log_N_) online time and symmetric privacy for the query and database. It supports single-query, sequential multi-query, and batch-query settings. Future work includes more efficient secure index construction and dynamic graph updates. Currently, the database owner builds the index locally before queries arrive. For secure offloading, MPC servers can insert the _N_ vectors into the graph one by one and reuse our oblivious search to find neighbors. This requires _N_ graph searches, _O(N_log_N_) time, and _O(NM_) space for degree bound _M_ \[32\].

## ACKNOWLEDGMENTS

This research is supported by the Singapore Ministry of Education Tier 1 Grant (RG19/25) and the NTU-NAP Startup Grant (024584- 00001). We also thank the anonymous reviewers who have made valuable suggestions on improving the presentation of the paper.

\begin{tabular}{ccccccccc}
 & No retrieval & HNSW & \multicolumn{6}{c}{HNSecW} \\
 & & & _C_=1 & _C_=3 & _C_=5 & _C_=7 & _C_=9 & _C_=11 \\
EM (%) & 22.4 & 66.2 & 56.8 & 63.5 & 65.2 & **66.0** & 66.1 & 66.2 \\
F1 (%) & 31.5 & 81.5 & 70.2 & 78.5 & 80.6 & **81.3** & 81.4 & 81.5 \\
\end{tabular}

** 4: End-to-end RAG quality on HotpotQA queries. At our setting:** _C_=7, **HNSecW matches the HNSW baseline.**

