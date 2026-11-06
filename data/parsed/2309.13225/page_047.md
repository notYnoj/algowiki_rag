### Case 2: deg(_P<sub>w,x</sub>)\>s_<sub>_k_<sub>0</sub></sub>

We now arrive at the key case depending on Phase 1. Let _y_ denote the vertex in _P<sub>w,x</sub>_ closest to _x_ with degree \(\mathrm{deg}(y)\ge s_{k_0+2}\) and _z_ be a vertex of maximum degree on _P<sub>w,x</sub>_. Then, let _i_<sup>∗</sup> be the integer \(1\le i\le l\) such that \(\frac{n}{2^{i^*}}\le\mathrm{deg}(z)<\frac{n}{2^{i^*-1}}\). Let \(y^*=r(y,D_{k_0+2})\) and _z_<sup>∗</sup>=_r(z,C_<sub>_i_<sup>∗</sup></sub>).

Since \(P\subset F_{i^*}\), in the _i_<sup>∗</sup> iteration of Phase \(1X_{i^*}(z^*,w^*)\le\delta(z,w)+2\le C+2\) and \(X_{i^*}(z^*,y^*)\le\delta(z,y)+2\le C+2\). Since the entries are finite, we use `BoundedMinPlus`(_A_<sub>_i_<sup>∗</sup></sub>_,B_<sub>_i_<sup>∗</sup></sub>) to compute,<tbc>

\(\hat{\delta}_{i^*}(w^*,y^*)\le X_{i^*}(w^*,z^*)+X_{i^*}(z^*,y^*)\le\delta(w,z)+\delta(z,y)+4=\delta(w,y)+4\)

<tbc>Now, in the (_k_<sub>0</sub>+3)-th iteration in Phase 2, when we execute Dijkstra from _w_<sup>∗</sup>, we have an edge to _y_<sup>∗</sup> with weight at most \(\delta(w,y)+4\). If deg(_x)\>s_<sub>_k_<sub>0</sub>+2</sub>, and therefore _y=x_, we take an extra edge \((x^*,x)\in E^*\) to find a path of length at most \(\delta(w,y)+4+1=\delta(w,x)+5\). Otherwise, after using the edge \((y^*,y)\in E^*\), the remaining edges of _P<sub>w,x</sub>_ are in _E_<sub>_k_<sub>0</sub>+3</sub> and we can conclude,

\(\hat{\delta}_{k_0+3}(w^*,x)\le\hat{\delta}_{i^*}(w^*,y^*)+1+\delta(y,x)\le\delta(w,y)+\delta(y,x)+5=\delta(w,x)+5\)

## 6 Weighted Approximation via Approximate (min,+) Product

In this section, we generalize our results to graphs with arbitrary non-negative weights. Let wt(_e_) denote the weight of an edge \(e\in E\). For any subset of edges \(S\subset E\), let \(\mathsf{wt}(S)=\sum_{e\in S}\mathsf{wt}(e)\) denote the total weight of edges in _S_. Throughout, we assume all weights are non-negative.

### Preliminaries

We first require some preliminary results analogous to unweighted graphs for computing dominating sets, and degree decompositions. Note that this decomposition is slightly different than what is used in previous sections.

**Lemma 6.1.** _Let G be a weighted, undirected graph on n vertices. For a given edge e incident to vertex v, let_ rank_<sub>v</sub>(e_) _be the order of e among all edges incident to v when ranked in increasing order of weight. For example, if e is the lightest edge incident to v,_ rank_<sub>v</sub>(e_)=1_. For a neighbor_ \(w\in N(v)\)_, we also denote_ rank_<sub>v</sub>(w_)=rank_<sub>v</sub>(v,w_) _to be the rank of the edge_ (_v,w)._

_Given thresholds s_<sub>1</sub>_\>s_<sub>2</sub>_\>...\>s_<sub>_k_-1</sub>_, there is an algorithm `WeightedDecompose` that outputs edge sets_ \(\{E_i\}_{i=1}^k\)_, edge set E_<sup>∗</sup>_, and vertex sets_ \(\{D_i\}_{i=1}^k\) _satisfying,_

1. \(E_i=\{(u,v)\in E\text{\textit{s.t.}}\mathrm{min}(\mathrm{rank}_u(u,v),\mathrm{rank}_v(u,v))<s_{i-1}\}\).<tbc>

_2._ _D<sub>i</sub> dominates_ \(V_{s_i}=\{v\in V\text{\textit{s.t.}}\mathrm{deg}(v)\ge s_i\}\) _and_ \(|D_i|=\tilde{O}\left(\frac{n}{s_i}\right)\)<tbc>

_3._ \(E^*=\bigcup_{i=1}^kE_i^*\) _where each_ \(E_i^*\subset E\) _has for every_ \(v\in V_{s_i}\) _at least one edge_ \((v,w)\in E_i^*\) _where_ \(w\in D_i\) _and_ rank_<sub>v</sub>(v,w)\<s<sub>i</sub>._

_Furthermore, `WeightedDecompose` runs in_ \(\tilde{O}(kn^2)\)_-time._

_We define the level of a vertex and edge analogously as in the unweighted case. For a given vertex_ \(v\in V\) _, define the_ **level of** _v, denoted_ \(\ell(v)\)_, as the integer i such that_ \(s_i\le\mathrm{deg}(v)<s_{i-1}\)_. For a given edge_ \(e\in E\)_, define the_ **level of** _e, denoted_ \(\ell(e)\)_, as the integer i such that_ \(e\in E_i\backslash E_{i+1}\).

### 6.1 \((1+\varepsilon,2w)\) Approximation

For a given path _P_, let _h(P_) denote the weight of the heaviest edge in _P_. For a pair of vertices _u,v_, let _w<sub>u,v</sub>_ denote the minimum _h(P_) over all shortest paths _P_ between _u,v_.

