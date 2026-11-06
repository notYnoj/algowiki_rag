<tbc>parameters. For Seismic, we build many indexes to generate different latency-recall operating points, so we report the build time of the index that gives the best latency at 95% recall@10. From  1, we see that GRIP’s Sparse PiPNN approach considerably reduces build time compared to HNSW with high efc, as previously noted. We also observe that Seismic maintains an order-of-magnitude faster build time than GRIP demonstrating that inverted indexes still maintain a considerable advantage over graph indexes in construction time. Nevertheless, the 7.3h construction time for GRIP at the 138M scale of MS MARCO v2 is still within practical constraints of search systems that require rebuilding indexes on a daily cadence. We do not report the build time of HNSW on MS MARCO v2 because an efc value of 200 would produce uncompetitive search quality and an efc of 2000 would require days to build.

In  2, we report the index size for each of the methods we evaluate. On MS MARCO v1, we observe that the GRIP index consumes more space than Seismic with CoCondenser embeddings but less memory with SPARSEUP. We hypothesize that the lower space footprint on SPARSEUP stems from the fact that SPARSEUP embeddings are denser (more nonzero components) and have a larger vocabulary, leading Seismic’s posting lists to grow faster than the graph. We leave further investigation of the impact of these parameters for future work. On MS MARCO v2 with CoCondenser, we note that GRIP uses almost double the space of Seismic primarily due to the fact that GRIP stores an additional copy of each vector in _R_-sketched form. Improving the space efficiency of GRIP is another promising direction for future work, following similar work on optimizing the space footprint of Seismic \[3, 29\].

Finally, in  3, we conduct an ablation study to isolate the speedup of term-based entry point seeding and approximate routing via sketching. We observe that term-based seeding provides larger gains than routing, but the two optimizations are complementary and, when combined, produce a larger speedup than either technique alone.

## 5 Conclusion

Our core insight behind the design of GRIP is that we can infuse the strengths of inverted indexes into graph-based search. To that end, we introduced three optimizations that accelerate query processing and index construction, namely term-based entry point seeding, approximate routing via sparse sketching, and Sparse PiPNN, each of which is inspired by, or directly uses, inverted indexes. Together, these allow GRIP to outperform Seismic, a state-of-the-art inverted index, by 2.2-3.4\(\times\) on the 138M-passage MS MARCO v2 collection with SPLADE-CoCondenser embeddings. These results challenge<tbc>

<tbc>the recent consensus in the vector search community that inverted indexes are the better choice for learned sparse retrieval at realistic collection sizes. These gains do come at a cost: GRIP’s index is larger than Seismic’s and takes longer to build. Closing this gap, for instance through graph and vector compression, is an important direction for future work. Nevertheless, within LSR specifically, our results call into question the default choice of inverted indexes for deploying sparse retrieval, and may open the door to applying sparse embeddings in new, ambitious applications that demand more scalability. More broadly, we believe that our insights on combining the strengths of inverted indexes and graph-based indexes may have implications beyond learned sparse retrieval. Graph- based search for LSR was not inherently uncompetitive; it simply had not yet borrowed what made inverted indexes successful. We suspect the same is true in other data structures problems where one technique has been set aside in favor of another, and where the better answer may be to combine the strengths of both. Exploring the generality of our insights to other problems may also be a promising direction of future work.

## References

\begin{tabular}{cccc}
 & \multicolumn{2}{c}{MS MARCO v1 (8.8M)} & MS MARCO v2 (138M) \\
Method & CoCondenser & SPARSEUP & CoCondenser \\
HNSW (efc 200) & 5.5 & 7.8 & - \\
HNSW (efc 2000) & 6.3 & 8.5 & - \\
Seismic & 6.5 & 16.1 & 73.0 \\
GRIP & 8.8 & 12.3 & 140 \\
\end{tabular}

\begin{tabular}{cccccc}
 & & \multicolumn{4}{c}{Recall@10} \\
Model & Search & 95% & 97% & 98% & 99% \\
\multirow{3}{*}{CoCondenser} & Seeding only & 2.39\(\times\) & 2.59\(\times\) & 2.55\(\times\) & 2.34\(\times\) \\
 & Routing only & 1.37\(\times\) & 1.38\(\times\) & 1.34\(\times\) & 1.22\(\times\) \\
 & Seeding + routing & 2.97\(\times\) & 3.36\(\times\) & 3.32\(\times\) & 3.07\(\times\) \\
\multirow{3}{*}{SparseUp} & Seeding only & 1.99\(\times\) & 1.95\(\times\) & 1.96\(\times\) & 1.95\(\times\) \\
 & Routing only & 1.16\(\times\) & 1.10\(\times\) & 1.12\(\times\) & 1.16\(\times\) \\
 & Seeding + routing & 2.15\(\times\) & 2.08\(\times\) & 2.04\(\times\) & 2.17\(\times\) \\
\end{tabular}

** 2: Index size in GB. For Seismic, we report the size of the index that gives its best latency at 95% recall@10.**

** 3: Ablation of GRIP’s search on MS MARCO v1 (8.8M). We report the speedup over standard beam search on the same Sparse PiPNN graph at matched recall@10 (single thread). Seeding uses** _T_=2 **(CoCondenser) and** _T_=4 **(SparseUp) with** _L_=64**. Routing uses** _R_=80 **and** _R_=128**. We observe that term-based seeding provides the majority of the efficiency gains, but the two optimizations are complementary and combine to produce a larger speedup than either technique alone.**

