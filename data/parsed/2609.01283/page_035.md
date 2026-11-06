1. **_Decision Oracle:_** _Decides if a parity basis exists. This oracle requires_ \(O(c^2m+r^\omega)\) _preprocessing time, O(r_<sup>2</sup>log(_r_)) _space, and answers queries in_ \(O((c^2f)^\omega)\) _time._<tbc>

_2._ **_Weighted Oracle:_** _Returns the exact minimum weight of a parity basis. This oracle requires_ \(\widetilde{O}(c^2m+Wr^3)\) _preprocessing time, O(Wr_<sup>3</sup>log_r_) _space, and answers queries in_ \(\widetilde{O}(W\cdot r\cdot(c^2f)^\omega)\) _time._

_Proof._ The proof is similar to that of Theorem 3.5 and hence, we discuss it in brief. We first apply the preprocessing algorithm from Theorem A.2 to the \(r\times r\) Parity Laplacian.

For the unweighted decision oracle, we evaluate the matrix at _Y_=1 (maximum degree _d_=0). The preprocessing requires \(O(c^2m+r^\omega)\) time and _O(r_<sup>2</sup>log_r_) space. For the weighted oracle, the matrix entries are polynomials of maximum degree _d=O(W_), requiring \(\widetilde{O}(c^2m+Wr^3)\) preprocessing time and _O(Wr_<sup>3</sup>log_r_) space.

When a query containing _f_ pair updates arrives, since the matroid is _c_-sparse, the modifications translate to an additive update matrix containing at most 2_c_<sup>2</sup>_f_ non-zero entries. By Theorem A.2, re-evaluating the determinant takes \(O((2c^2f)^\omega)=O((c^2f)^\omega)\) time for the scalar case, and \(\widetilde{O}(Wr(2c^2f)^\omega)=\widetilde{O}(Wr\cdot(c^2f)^\omega)\) time for the polynomial case. □

## 7 \(\alpha\)-Factors and Matchings

Let _G_=(_V,E,c_) be an undirected graph with _n_ vertices and _m_ edges, where edge costs are integers in the range \[-_W,W_\]. Let \(\alpha:V\rightarrow\mathbb{Z}^+\) be a function assigning a degree bound to each vertex in _V_ . Following the terminology of \[GS21b\], we define a (perfect) \(\alpha\)**-factor** as a subgraph _H_ of _G_ such that every vertex \(v\in V\) has degree exactly \(\alpha(v)\) in _H_. <sup>3</sup>

For convenience, we only consider the (perfect) \(\alpha\)-factor and refer to it throughout as just \(\alpha\)-factor. The _minimum-cost_ \(\alpha\)-factor is the \(\alpha\)-factor with minimum total edge cost, if it exists. Throughout this section, we refer to the set of edges incident to a vertex _v_ in graph _G_ as \(\delta_G(v)\). We omit the subscript _G_ if the graph _G_ is clear from the context.

### 7.1 \(\alpha\)-Factors as Linear Matroid Parity

In this subsection, we study the _k-bounded_ \(\alpha\)_-factor problem_, where we assume that the maximum degree constraint is bounded by a parameter _k_, i.e., \(max_{v\in V}\alpha(v)\le k\). The _k-bounded_ \(\alpha\)_-factor problem_ can be formulated as a linear matroid parity problem over a _k_-sparse linear matroid _M_ having _m_ disjoint pairs of elements. Let \(N=\sum_{v\in V}\alpha(v)\) denote the sum of all degree constraints. We assume that \(N\le 2m\) and is even, otherwise an \(\alpha\)-factor does not exist.

Furthermore, we assume that the vertex set _V_ has some fixed total ordering, i.e., for any two vertices \(a,b\in V\) , either _a\<b_ or _a\>b_. Since the graph is undirected, we assume that every edge is written as an ordered pair according to the total ordering over _V_ , i.e., an edge _e_ in _G_ is written as (_a,b_), where _a\<b_, and (_b,a_) otherwise.

Define V as a set where each vertex \(v\in V\) has \(\alpha(v)\) distinct copies, and \(v_j(j\in[\alpha(v)])\) refers to the _j<sup>th</sup>_ copy of vertex _v_.

Now, consider the following matrix representation matrix _A_ for a matroid _M_: _A_ is a \(N\times 2m\) polynomial matrix over the variables \(\{x_{u_k,e}\}_{u_k\in\mathcal{V},e\in\delta(u)}\) whose rows are indexed by V and the column<tbc>

<sup>3</sup>Note that our results carry over to (maximum) \(\alpha\)-factor as well. The (maximum) \(\alpha\)-factor considers \(\alpha(v)\) as an upper bound on the desired degree of _v_ and the objective is to maximise the number of edges picked. We provide its details in the appendix.

