<tbc>The best result by Han and Takaoka \[73\] achieve _O(loglogn_)<sup>2</sup> reduction factor when compared to the result of \[28\]. Their approach focuses on the distance product computation. First, an _nxn_ matrix js divided into _m_ sub-matrices, each having _nxn/m_ dimensions, where m is determined based on a specific criterion. Then, the algorithm proceeds in a series of matrix manipulations, index building, encoding, and partitioning steps until it reaches the proposed bound.

The best _non-negative edge weight_ complexity is _O(n_<sup>2</sup>_logn_) \[98\]. First, the algorithm sorts all adjacency lists in an increasing weight fashion. Then, it performs an SSSP computation _n_ times and proceeds in iterations. In the first phase, it uses the notion of _potential_ over the edges of vertices and selects and labels the edge with the minimum potential. _Potential_ derived from the _potential-model_ is defined as a probability distribution on complete directed graphs with arbitrary edge lengths that contain no negative cycles. The algorithm runs in two main phases, each with a specific invariant and has an _O(n_<sup>2</sup>_logn_) complexity.

The best _positive integer edge weight_ complexity is \(O(n^\omega+c)\) \[110\], where \(\omega<2.575\) is the exponent being proposed by Coppersmith and Winograd \[33\]. Their proposed algorithm provides a transition between the fastest exact and approximate shortest-paths algorithms with a linear error rate. The algorithm focuses on directed graphs with small positive integer weights in order to obtain additive approximations. The approximations are polynomial given the actual distance between pairs of vertices.

## 5.3 Distance Oracles

_Definition:_ Given a graph _G_=(_V,E_), a distance oracle encompasses a (1) data structure or index that undergoes preprocessing, and a (2) query algorithm.

The term _distance oracle_ has been proposed by Thorup and Zwick \[132\]. It proposes a faster alternative to the SSSP and APSP algorithms. This can be achieved by preprocessing the graph and creating an auxiliary data structure to answer queries. Distance oracle operates in two phases, namely, a preprocessing phase and a query phase. In the preprocessing phase, information such as data structures or indexes are computed. In contrast, the query processing phase processes queries efficiently using the outcome from the preprocessing phase. Distance oracles may return exact or approximate distances. A distance oracle provides an efficient trade-off between space (in terms of data structure or index storage) and query time.

### 5.3.1 Exact Distances

Fakcharoenphol and Rao \[51\] propose an algorithm for planar graphs that balances the trade-off between preprocessing and query time. The preprocessing complexity for both space and time is \(\tilde{O}(n)\), and the run-time complexity is \(\tilde{O}(\sqrt{n})\). Their proposed approach creates a non-planar graph given a subset of vertices followed by the computation of the shortest-path tree. First, the graph is divided into a set

\begin{tabular}{cc}
Time Complexity & Author \\
_n_<sup>3</sup> & \[52, 134\] \\
_n_<sup>3</sup>(_loglogn)/logn_<sup>1/3</sup> & \[55\] \\
_n_<sup>3</sup>(_loglogn/logn_)<sup>1/2</sup> & \[126\] \\
_n_<sup>3</sup>/(_logn_)<sup>1/2</sup> & \[45\] \\
_n_<sup>3</sup>(_loglogn/logn_)<sup>5/7</sup> & \[71\] \\
_n_<sup>3</sup>_loglogn/logn_ & \[127\] \\
_n_<sup>3</sup>(_loglogn_)<sup>1/2</sup>_/logn_ & \[141\] \\
_n_<sup>3</sup>_/logn_) & \[27\] \\
_n_<sup>3</sup>(_loglogn/logn_)<sup>5/4</sup> & \[72\] \\
_n_<sup>3</sup>(_loglogn_)<sup>3</sup>/(_logn_)<sup>2</sup> & \[28\] \\
_n_<sup>3</sup>(_loglogn)/(logn_)<sup>2</sup> & \[73\] \\
\end{tabular}

