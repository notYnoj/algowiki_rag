<tbc>10<sup>7</sup>, which is 37%-45% smaller than CubeGraph on Sift-Geo-1M, Yfcc-Clip (2.28 GiB), and SpaceV-Geo-10M (26.08 GiB; CubeGraph is 1.07 GiB on Overture-1M), while FAISS stores the 4_nD_-byte vectors (1.68-2.26 GiB).

**Exp-3: Direct Connectivity Verification (Figure 7(a)).** Over 1,000 queries on Yfcc-Clip at \(\bar{\sigma}=10^{-3}\), \(\mathcal{H}_\infty(c)\) achieves LSCC=100% on 98.4% of queries (_\>_99% on the rest; Theorem 3.7): active fibers are strongly connected for 99.998% of co-located objects and the quotient has 100% median LSCC. Cut rank \(\ell_\mathrm{SC}(c)\) (Theorem 3.3) has median 48 and p95 123 (LSCC reaches 100% at \(\ell=64\) median, 128 p10).

**Exp-4: Recovery Budget** \(\ell\) **and Query Work.** With _L_=16 on Overture-1M (\(\bar{\sigma}=10^{-1}\); Appendix B.3), Recall@10 rises from 0.3730 at \(\ell=8\) (16,864 QPS) to 0.8576 at \(\ell=64\) (3,243 QPS) and 0.8691 at \(\ell=96\) (2,257 QPS, 1,330 evaluations), nearly matching \(\ell=\infty\) (0.8738, 4,157 evaluations, 797 QPS): from \(\ell=8\) to \(\infty\), vector evaluations grow by \(37\times\) vs. \(11\times\) for scans. Across _all_ 20 _filtered cells_, the max-recall gap between \(\ell=64\) and \(\infty\) is \(\le 0.0032\) (\(\le 0.0008\) for \(\bar{\sigma}\le 10^{-3}\)), and the active fraction scored for 0.99 recall drops from 1.0 at 10<sup>-5</sup> to 0.004-0.02 at \(\bar{\sigma}=1\).

**Exp-5-Exp-8: Ablations, Sensitivity, Scale, and Fibers.** _Exp- 5 (Figure 7(b)-(d)):_ On Yfcc-Clip (\(\bar{\sigma}=10^{-2},\ell=32\)), removing<tbc>

<tbc>geographic (_B<sub>g</sub>_=0) or vector edges (_B<sub>v</sub>_=0) caps recall at 0.8811 or 0.9285 vs. 0.9981 for both; grid seeding matches graph descent while reducing seed time by \(18\times\) (1.2 vs. \(21.7\mu\)s). _Exp-6 (Figure 8(a),(b),(d)): B_=384 matches _B_=512 at lower scan cost; _B<sub>v</sub>/B<sub>g</sub>_=128/256 balances scans (2,611 vs. 3,524 for 192/192 at _L_=16) and recall (0.9590 vs. 0.9513 for 64/320 at _L_=64); and \(k\in[5,100]\) exceed 0.997 recall. _Exp-7_ (\(10^6\rightarrow 10^7\)): From Sift-Geo-1M to SpaceV-Geo-10M, size scales by \(10.0\times\) (1.44 \(\rightarrow\) 14.34 GiB) and build time by \(17.1\times\) (\(117\rightarrow 2,007\) s, vs. \(43.8\times\) for CubeGraph). _Exp-8 (Figure 8(c)):_ On Yfcc-Clip (fibers up to 5,726), fiber \(\alpha\)-pruning beats ID truncation (0.9928 vs. 0.9860 recall at _L_=256; 0.9981 at _L_=1024).

## 6 Related Work

**Filtered and Hybrid ANN Search.** Proximity graphs searched with beam search (HNSW \[25\], NSG \[13\], DiskANN \[17\]) lead unfiltered ANN \[2, 3, 27, 41\]. For attribute filters \[8\], Filtered- DiskANN \[15\], UNG \[6\], and JAG \[42\] embed discrete labels into edges; CGIF \[24\] pairs HNSW with inverted files; SIEVE \[21\] builds workload-tuned sub-indexes; VBASE \[46\] uses relaxed monotonicity; NHQ \[40\] and DEG \[45\] define composite attribute-vector metrics; and ACORN \[28\] filters two-hop neighborhoods. However, 2D disks cannot be indexed by finite inverted lists and act as hard boundaries (\(\Delta(s_v,g_q)\le r_q\)). Range graphs (SeRF \[48\], uRNG \[23\], RNSG \[47\], WinFilter \[12\], iRangeGraph \[43\], UNIFY \[22\], DSG \[29\], DIGRA \[19\]) rely on a 1D attribute order absent for 2D disks.

**Spatial-Vector and Fiber-Navigable Retrieval.** Spatial \[14, 16, 34\] and geo-textual indexes \[7\] prune 2D space before secondary filtering (_Spatial-First, Geo-Partition_); REACH uses a flat grid only for \(\tau\) entry seeds. Mesh \[37\] tunes cell graphs for a known workload and switches between spatial scan and cell-graph search by selectivity, whereas CubeGraph \[44\] builds graphs across tree levels. Unlike FNS \[10\], which calls any predicate-induced subgraph a "fiber," our _coordinate fibers F(z_) are co-located object classes admitted in full or not at all by any disk (Lemma 3.4), which connects intra-fiber \(\alpha\)-pruning with RGG theory \[4, 9, 30-32\].

## 7 Conclusion

We proposed REACH for GFANN search via _Ranked Active-Graph Recovery_: (1) filtering a vector-sorted row preserves survivor order, recovering \(\mathcal{H}_\ell(c)\) governed by cut rank \(\ell_\mathrm{SC}(c)\); and (2) coordinate fibers pass or fail any disk filter as a unit, yielding polylogarithmic- degree connectivity and \(2.49\times\) higher selective QPS.

(a) Connectivity
(b) Graph components
(c) Entry method
(d) Entry latency
100
8k
21.7
8k
20
95
2k
LSCC (%)
2k
Time (μs)
10
90
QPS
0.5k
REACH No geo.
No vector No a
0.5k
Cell directory Graph descent
1.2
85
0
8
16
32
64
128
8
.4
.7
1.0
.90
.95
1.0
Cell dir.
Graph descent
Recovery budget l
Recall@10
Recall@10

(a) Row width
(b) Quota split
8k
4k
2k
1k
B
Bv/Bg
64/320
0.5k
128
384
128/256
256
512
192/192
(c) Duplicate handling
(d) Result count
QPS (single thread)
8k
4k
2k
1k
k
Selection
5
50
0.5k
Fiber-aware Naive
10
100
20
.85
.92
1.0.85
.92
1.0
Recall@10
Recall@k

**Figure 7: Structural connectivity check (_a_, \(\bar{\sigma}=10^{-3}\)) and source/seeding ablations (_b-d_, \(\bar{\sigma}=10^{-2},\ell=32\)) on Yfcc-Clip.**

**Figure 8: Sensitivity and robustness on Yfcc-Clip (**\(\bar{\sigma}=10^{-2},\ell=32\)**): row width** _B_**, quota split** _B<sub>v</sub>/B<sub>g</sub>_**, fiber-aware** \(\alpha\)**- pruning vs. naive truncation, and result count** \(k\in[5,100]\)**.**

