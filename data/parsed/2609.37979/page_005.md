graph _H_ with its own length and cost functions, and must either return the constrained shortest path distance _OPT(H_) or report that _H_ is not isomorphic to any _G<sub>i</sub>_.<sup>4</sup><tbc>

<tbc>Note that an algorithm may still correctly return the optimal value _OPT(H_) even if no _G<sub>i</sub>_ is isomorphic to _H_; indeed, the algorithms in this paper exhibit this behavior.

### Can we Avoid Computing _OPT(H_) from Scratch when _H_ is Isomorphic to some _G<sub>i</sub>_?

Ideally, if _H_ is isomorphic to one of the prior graphs _G_<sub>1</sub>_,...,G<sub>k</sub>_, the algorithm should compute _OPT(H_) significantly faster than traditional worst-case bounds guarantee. Conversely, if _H_ is not isomorphic to any prior graph, the algorithm should quickly report this so that a heavy-duty fallback computation can be invoked from scratch. For instance, if a weighted query graph _H_ is isomorphic to a prior graph _G<sub>i</sub>_ (i.e., identical up to a renaming of vertices), can we determine whether _H_ contains a negative triangle in truly subcubic time \(O(n^{3-\epsilon})\)? Similarly, for CSP, can we achieve polynomial preprocessing and query times in our model?

Trivially, every problem in our model can be solved via Graph Isomorphism (GI); however, the best known algorithm for GI requires quasipolynomial time \[Bab16\] and is efficient only on restricted graph classes \[HW74, Luk82, Bod90\]. This is prohibitively slow for a query phase even for NP-hard problems like CSP, and is inferior to the classical worst-case time for problems in P like Negative Triangle. _Is this new model capable of bypassing worst-case barriers without invoking computationally expensive graph isomorphism algorithms?_

## 1.1 Our Results

### Algorithmic Results.

We show that our model has the power to bypass worst-case time complexity barriers for various classes of computational problems.

The first class of problems we consider encompasses NP-hard graph optimization. Besides the aforementioned Constrained Shortest Path (CSP) problem, \(\ell_p\)-Shortest Path (\(\ell_p\)-SP) stands as another classic multi-objective challenge \[PY00, YY98, BLM<sup>+</sup>08, CMM26, MOT24, LXZ24\]. Started by Papadimitriou and Yannakakis \[PY00\] and the subject of recent progress characterizing its exact approximation landscape \[CMM26, MOT24, LXZ24\], this problem requires finding an _s-t_ path in a graph with _d_-dimensional edge weights such that the \(\ell_p\)-norm of the path’s total aggregated weight vector is minimized. Closely related are Constrained Spanning Tree (CST) and \(\ell_p\)-Spanning Tree (\(\ell_p\)-_ST)_ \[HCP04, Xue00, RG96, MRS<sup>+</sup>98, Sho83, AAN82, GJ79\], where the optimization goal shifts from finding an _s-t_ path to computing a spanning tree.

All these problems are NP-hard. In contrast, in our model, we only require near-linear preprocessing and query times to solve the problems for paths and subcubic time for trees.

**Theorem 1.1** (Algorithms for NP-hard Problems)**.** _There exist deterministic isomorphic-priors algorithms that solve_ Constrained Shortest Path _and_ \(\ell_p\)-Shortest Path _using_ \(\widetilde{O}(km)\) _preprocessing time and_ \(\widetilde{O}(m)\) _query time._<sup>5</sup> _For_ Constrained Spanning Tree _and_ \(\ell_p\)-Spanning Tree_, there exist randomized_<sup>6</sup> _algorithms requiring_ \(\widetilde{O}(kn^\omega)\) _preprocessing time and_ \(\widetilde{O}(n^\omega)\) _query time, where_ \(\omega<2.37134\) _is the matrix multiplication exponent._

<sup>4</sup>Following the definition in  2, an isomorphism between _G<sub>i</sub>_ and _H_ must strictly preserve the source and target nodes, mapping _s_ to _s_ and _t_ to _t_. <sup>5</sup>\(\widetilde{O}\) hides polylogarithmic factors. <sup>6</sup> The algorithms are correct with high probability. We say an event occurs _with high probability_ (w.h.p.) if it holds with probability at least 1-1_/N<sup>c</sup>_ for any arbitrarily large constant \(c\ge 1\), where _N_ denotes the input size. Furthermore, our algorithms are analyzed under the standard _oblivious adversary_ model; that is, we assume the sequence of queries is generated independently of the algorithm’s internal random choices (see, e.g., \[NY15\] and \[KL14, Definition 3.4\]).

