<tbc>worst-case update and query time \(\tilde{O}(\sqrt{n}logW/\epsilon^2)\) time where _W_ is the aspect ratio of _G_. Karczmarz \[22\] achieved similar time bounds for the \((1+\epsilon)\)-approximate APSP problem for a larger family of graphs (so-called \(O(\sqrt{n})\)-separable graphs), however, the algorithm only works for _decremental graphs_. Further, the exact dynamic single-source shortest paths problem has been studied \[8\]. In very recent work by Filtser et al. \[17\], a deterministic algorithm achieving subpolynomial amortized update and query time \(n^{o(1)}/\text{poly}(\epsilon)\) was given.

### Dynamic All-Pairs Shortest Paths in General Graphs.

The dynamic exact APSP problem has received extensive attention over the past years, also in incremental and decremental settings \[4, 24, 11, 5, 12, 32, 3, 31, 15\]. However, conditional lower bounds \[1, 19\] are quite strong and, in particular, stipulate that exact APSP requires either \(\tilde{\Omega}(m)\) update or query time. This motivates the more restricted but powerful planar setting.

### Dynamic Offline Algorithms.

The purpose of studying dynamic algorithms in an offline setting is twofold. First it captures some of the inherent difficulties of the online setting, thus making any progress for the first provides significant insight towards designing an online dynamic algorithm. Secondly most of the lower bound results for standard dynamic setting also hold for offline setting. Thus, giving an efficient algorithm for the offline dynamic setting shows that no such conditional lower bound exists. Following this, substantial effort has been taken to design dynamic algorithms in offline setting. In \[9\] authors provide a fully dynamic offline algorithm that computes _O_(log<sup>4_t_</sup>_n_) approximation of all pair max flow/min cut in average \(\tilde{O}(m^{1/t+1})\) update and query time . They also propose a fully dynamic offline algorithm for all pair shortest path that computes (2_r_-1)_<sup>t</sup>_ approximation in average \(\tilde{O}(m^{1/t+1}n^{2/r})\) update and query time for \(t,r\ge 1\). \[30\] presents a fully dynamic offline algorithm computing 3 edge and vertex connectivity in an undirected graph in time _O_(log_n_) per update. \[27, 23\] studies the dynamic connectivity and reachability in graph timelines in a semi offline setting. Here the updates are given upfront while the queries can arrive online. For the connectivity problem \[23\] provides a data structure with _O(m+t_log_n_) preprocessing time and _O_(log_n_) query time. For rechability in undirected graph \[27\] gives a randomized algorithm that has _O(t_log_t_loglog_t_log_n+m_) preprocessing time and can answer all queries in _O_(log_n_loglog_t_) time.

### Static Planar Graphs.

Finally, we point out that there has been extensive work on \((1+\epsilon)\)- approximate and exact static distance oracles culminating recently in a data structure that can be constructed in _n_<sup>1+_o_(1)</sup> space and answer distance queries exactly in subpolynomial worst-case query time \[7, 28\].

## 4 Preliminaries

In this article, we assume that every graph _H_ is planar, directed and weighted with positive weights, is already embedded in the plane, is triangulated and undergoing edge weight updates given by an efficient encoding of the weight update sequence. We call a dynamic graph _H_, _incremental/ decremental_ if the weight update sequence monotonically decreases/ increases edge weights in _H_ over time. In the offline setting, we assume that the update sequence is given with the input, in<tbc>

