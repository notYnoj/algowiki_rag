# Whether quantum advantage? New classical lower bounds for Max-Cut on large-girth 3-regular graphs

Every 3-regular graph of girth at least _g_ has a cut containing at least a fraction _Mg_ of its edges, and the best rigorous bounds at large girth are \(0.912\le lim_{g\rightarrow\infty} Mg\le 0.92386\). Lower bounds on _Mg_ follow from the performance of local algorithms: on a graph of girth \(g\ge 2p+2\) a depth-_p_ local algorithm sees the same tree around every edge, so its expected cut fraction on that tree bounds _Mg_ from below. We apply this strategy to the Variational Iterative Rotation Algorithm (VIRAL), a classical local algorithm, and evaluate it on the depth-_p_ tree for every even depth up to _p_=32. The resulting bounds exceed those recently obtained from the Quantum Approximate Optimization Algorithm (QAOA) for every \(p\ge 4\), by 0.005 to 0.011, and they extend the range of girths covered from _g_=36 to _g_=66. Notably, at _g_=66 we obtain \(M_{66}\ge 0.9127\) at 99.99999% confidence level, which raises the asymptotic lower bound from 0.912 to 0.9127.

_Introduction_ - The maximum cut of a graph _G_=(_V,E_) is the largest number of edges connecting the two sides of a bipartition of _V_ . Finding this cut is NP-hard even for 3-regular graphs [1]. The girth _g_ of a graph is the length of its shortest cycle. In a 3-regular graph of girth _g_, the ball of radius _d_ around any vertex contains no cycles whenever \(g\ge 2d+2\), and is then the same finite tree for every vertex, so all such graphs look alike locally and differ only globally, as illustrated in Fig. 1 for \(g\ge 6\). The question we address is what fraction of the edges an algorithm can guarantee to cut on these graphs. This motivates the following definition:

\(M_g=inf_{G\text{3-regular girth}(G)\ge g}\frac{\text{MaxCut}(G)}{|E(G)|}.\) (1)

The quantity _Mg_ is non-decreasing in _g_ and \(lim_{g\rightarrow\infty} Mg\) exists, but its value is not known. The best lower bound, \(lim_{g\rightarrow\infty} Mg\ge 0.912\), follows by combining the results of Refs. [2] and [3], as noted in [4]. The best upper bound comes from random 3-regular graphs, whose maximum cut fraction is asymptotically at most 0.92410 by the 1RSB bound conjectured in [5] and proven in [6], and at most 0.92386 by the tighter 2RSB bound of Ref. [7]. Thus

\(0.912\le lim_{g\rightarrow\infty} M_g\le 0.92386,\) (2)

and any progress on the lower bound must be made inside a window of width \(\Delta M\approx 0.012\).

All lower bounds on _Mg_ to date come from local algorithms, which assign a vertex to a side of the cut using only information up to distance _p_ from that vertex. On a graph of girth \(g\ge 2p+2\) the radius-_p_ neighborhood of every edge, defined below, is the same finite tree, as shown in Fig. 1 for \(g\ge 6\) and _p_=2. Therefore, the expected cut fraction of a local algorithm of depth _p_ is a single number that can be computed on the tree and bounds _Mg_ from below for all \(g\ge 2p+2\) [4]. The Quantum<tbc>

Approximate Optimization Algorithm (QAOA) [9] is an algorithm of this type and the depth-_p_ QAOA circuit is a local algorithm of radius _p_. A series of works evaluated the QAOA on large-girth regular graphs at increasing depth [10, 11], culminating in \(Mg\ge 0.8971\) for \(g\ge 36\) from _p_=17 [4]. Classical local algorithms have been compared with the QAOA. At depth one [12] and two [13] simple classical rules outperform the QAOA for every degree, and numerical experiments on small random 3- regular graphs suggest the same at larger depth [14]. On large-girth graphs, however, the picture is different: at degree three the explicit vector algorithm of Thompson, Parekh, and Marwaha [8], whose guarantees are known at every depth, falls behind the QAOA for \(p\ge 7\) [4] (see  I). We recently introduced the Variational Iterative Rotation Algorithm (VIRAL) [15], a classical local algorithm in which every vertex carries a unit vector that is rotated _p_ times by angles set by its neighbors. On ran-<tbc>

3-regular graph of girth g 2 6
a11
b11
a1
b1
a12
u
v
b12
edge (u, v)
a21
b21
a2
b2
a22
b22

Flaviano Morone,<sup>1</sup> Shivang Rawat,<sup>1</sup> and Dries Sels<sup>2,3</sup>

<sup>1</sup>_Center for Quantum Phenomena, Department of Physics, New York University, New York, NY 10003 USA_ <sup>2</sup>_Department of Physics, Boston University, 590 Commonwealth Ave., Boston, Massachusetts 02215, USA_ <sup>3</sup>_Center for Computational Quantum Physics, Flatiron Institute, New York, NY, USA_

FIG. 1. **Section of a 3-regular graph of girth** \(g\ge 6\). The radius-2 neighborhood of an edge (_u,v_), consisting of the 14 vertices within distance 2 of _u_ or _v_, and the 13 edges incident to _u_, _v_ and their neighbors. The girth forces this tree structure. Any further edge among these vertices must join two leaves (since every other vertex already has degree 3) and it is allowed only if the two leaves lie on opposite sides of (_u,v_), where it closes a cycle of length 6 (dashed edge).

arXiv:2610.17236v1 [quant-ph] 12 Oct 2026

