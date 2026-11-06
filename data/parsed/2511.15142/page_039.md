In contrast, many connected weighted graphs cannot be recovered using just comparison queries. This is not surprising: we cannot distinguish between a graph with weights _w<sub>e</sub>_, and those with weight \(\alpha w_e\) for all \(\alpha>0\). But there are other kinds of barriers apart from a simple scaling of weights--here is an example. Given any graph _G_=(_V,E_) with unit weight edges, add another spanning tree _T_=(_V,F_) on the same vertices, and give the _i<sup>th</sup>_ edge \(e_i\in F\) a weight of \(w_T(e_i)=n^2\cdot 2^i\). This weight function ensures that the _F_-weights of all cuts are distinct. Moreover, for a set \(S\subseteq V\), \(w(\partial S)=|\partial_GS|+w_T(\partial_TS)\). Since the _w<sub>T</sub>_ weights are scaled by _n_<sup>2</sup> (and hence much larger than the contribution due to the unit-weight edges), we know that

\(w(\partial S)>w(\partial S')\Longleftrightarrow w_T(\partial_TS)>w_T(\partial_TS)\)

and hence we cannot infer the structure of the unit-weight edges.

### D.4.3 Finding Heaviest Edge Incident to a Vertex

We can show that comparison queries do not allow us to identify, for a vertex _v_, the heaviest edge adjacent to it. Finding this edge would be useful, e.g., in the min-cut algorithm of \[SW94\]. Indeed, consider the 4-vertex graph {_a,b,c,d_} and the 6 edge weight variables. Here are two universes:

In both scenarios, _w<sub>ad</sub>_=10 is much less than _w<sub>ab</sub>_ and _w<sub>ac</sub>_ (which are both ∼1000). However, a calculation shows that the order of the cuts is **identical** in both universes:

\(f(\{a,d\})>f(\{a\})>f(\{a,b\})>f(\{b\})>f(\{a,c\})>f(\{c\})>f(\{d\}).\)

Hence, given this specific ordering of cuts, we cannot distinguish between Case 1 (where (_a,b_) is the max-weight edge adjacent to _a_) or Case 2 (where (_a,c_) is).

## E Matroids, Matchings, and Paths

In this section, we give efficient comparison-based algorithms to optimize over matroids, matroid intersections, and shortest paths.

### E.1 Matroid Bases

We now give our algorithm to compute a minimum-weight basis of a matroid M=(_U,_I) with |_U_|=_n_ elements, where we are only allowed to compare matroid bases.

Our main result for matroid bases is the following:

**Theorem E.1** (Matroid Bases)**.** _There is an algorithm outputs the minimum-weight basis of a matroid on n elements using O(n_log_n_) _comparison queries in_ \(\widetilde{O}(n^2)\) _time._

_Proof._ First, let us consider graphical matroids, where the bases are spanning trees of a graph. Given any graph with edge set _E_, we can first partition the graph into its 2-vertex-connected<tbc>

\begin{tabular}{ccc}
**Edge Weight** & **Universe 1 (_w<sub>ab</sub>\>w<sub>ac</sub>_)** & **Universe 2 (_w<sub>ab</sub>\<w<sub>ac</sub>_)** \\
_w<sub>ab</sub>_ & **1000.01** & **999.99** \\
_w<sub>ac</sub>_ & **999.99** & **1000.01** \\
_w<sub>ad</sub>_ & **10** & **10** \\
_w<sub>bc</sub>_ & 100 & 100 \\
_w<sub>bd</sub>_ & 50 & 50 \\
_w<sub>cd</sub>_ & 1 & 1 \\
\end{tabular}

