<tbc>MS MARCO v1 collection in 47 minutes, compared to 5.5 hours for HNSW with an efc of 2000. As with term-seeded entry point selection, where we borrow ideas from inverted indexes to initialize graph-based search, and approximate routing, where we take inspiration from the concentration of importance property used in the Seismic inverted index system, our sparse PiPNN algorithm utilizes inverted indexes as part of the index build stage to reduce graph construction time by an order of magnitude. In each of our core optimizations behind GRIP, we see a common narrative pattern of infusing the strengths of inverted index designs to make graph-based search for LSR more performant.

As shown in Figure 3, a graph built with our Sparse PiPNN approach (without any of the other GRIP-specific optimizations) performs slightly below standard HNSW search with an efc construction setting of 2000 while building in 47 minutes as opposed to 5.5 hours. Thus, Sparse PiPNN trades off a small loss in search quality for major gains in construction build time, which becomes particularly important at larger collection sizes. Furthermore, we also note in Figure 3 that GRIP, which adds entry point seeding and approximate routing on top of Sparse PiPNN, outperforms Sparse PiPNN and HNSW, which underscores the value of our other aforementioned optimizations.

## 4 Experiments

We implemented GRIP in Rust, building off the ANN search primitives developed within the kannolo library \[13\]. We conduct our experimental evaluation using two standard sparse retrieval benchmarks, MS MARCO v1, which consists of 8.8M passages and MS MARCO v2, which contains 138M passages in the collection. We embed both sets of passages using two different sparse embedding models: SPLADE-CoCondenser \[17\] and the recently released SPARSEUP model \[15\] which achieves state-of-the-art performance on several retrieval benchmarks. We conducted all experiments on a single cloud instance with an Intel Xeon Platinum 8358 @ 2.60 GHz processor, 30 vCPUs, and 222 GB of RAM. We use all 30 available threads for index construction and a single thread at query time.

We compare GRIP against two representative baselines. The first is HNSW without any sparsity-specific optimizations to provide a reference point for GRIP’s specific improvements tailored to LSR. We use the kannolo Rust implementation of HNSW. Second, we also compare with the latest version of Seismic \[5\], using the official Rust implementation, which represents, to the best of our knowledge, the current state-of-the-art index for LSR in terms of recall-latency tradeoffs. We do not explicitly benchmark other LSR indexes such as SINDI \[22\], GrassRMA, and PyANNS since recent work has shown that an optimized implementation of Seismic outperforms these other methods by substantial margins \[29\].

We report our primary experimental findings in Figures 4 and 1, which benchmark on MS MARCO v1 and MS MARCO v2, respectively. In Figure 4 we observe that GRIP dominates HNSW on both SPLADE-CoCondenser and SPARSEUP, running 2.8-3.2\(\times\) and 2.0- 2.1\(\times\) faster at recall@10 targets between 95% and 98% (though the gap narrows in the high-recall regime, falling to 1.5\(\times\) at 99% on SPARSEUP). These results validate our sparsity-specific optimizations. Furthermore, we see that GRIP achieves a 1.4-1.7\(\times\) speedup<tbc>

<tbc>over Seismic on SPLADE-CoCondenser across recall@10 targets from 90% to 99%. On SPARSEUP, GRIP is 1.2\(\times\) faster than Seismic at 92-95% recall@10 and roughly on par at 97%, while Seismic is faster in the extremely high-recall regime of 98% and above. In Figure 1, the gap over Seismic widens at scale: on the 138M passages of MS MARCO v2, GRIP is 2.2-3.4\(\times\) faster than Seismic at recall@10 targets between 90% and 98%. This observation on the improvement of graph search over inverted indexes at larger scale is also consistent with the prior findings of Bruch et al. \[7\], who found that graphs exhibited better asymptotic scalability. However, at the time, the concrete efficiency of graph-based search still lagged behind inverted indexes like Seismic, so the point at which the scalability of graphs provided an advantage occurred at impractically large collection sizes. Our evaluation of GRIP shows that we can bend this scaling curve considerably by bringing ideas from inverted indexes into graph search.

In  1, we report the index construction time of the index types we consider in our experiments. For the graph-based methods, GRIP and HNSW, we build a single index and generate the corresponding recall-latency tradeoff curve by varying search time<tbc>

\begin{tabular}{cccc}
 & \multicolumn{2}{c}{MS MARCO v1 (8.8M)} & MS MARCO v2 (138M) \\
Method & CoCondenser & SPARSEUP & CoCondenser \\
HNSW (efc 200) & 19 min & 31 min & - \\
HNSW (efc 2000) & 5.5 h & 7.4 h & - \\
Seismic & 2 min & 3 min & 47 min \\
GRIP & 47 min & 54 min & 7.3 h \\
\end{tabular}

GRIP (ours)
Seismic
HNSW
SPLADE-CoCondenser
SparseUp
100
100
98
98
96
96
Recall@10 (%)
Recall@10 (%)
94
94
92
92
90
90
100
200
500
1k
2k
5k
10k
20k
200
500
1k
2k
5k
10k
20k
Latency per query (us, log scale)
Latency per query (us, log scale)

** 1: Index construction time (30 threads). For Seismic, we report the build time for the index that gives its best latency at 95% recall@10. We observe that Seismic has an order-of- magnitude faster build time than GRIP, underscoring that the inverted indexes still maintain a decisive advantage over graph-based indexes in terms of build time.**

**Figure 4: On the MS MARCO v1 dataset, we observe that GRIP is** \(1.4-1.7\times\) **faster than Seismic across all recall@10 targets plotted with SPLADE-CoCondenser embeddings. With SPARSEUP embeddings, GRIP is** \(1.2\times\) **faster than Seismic at 92-95% recall@10 and roughly on par at 97%, while Seismic remains faster in the extremely high-recall regime of 98% and above.**

