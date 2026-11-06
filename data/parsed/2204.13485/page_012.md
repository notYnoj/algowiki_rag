**Theorem 13.** \(\ell_1\)-min-pm _can be solved in polynomial time in bipartite graphs._

_Proof._ We reduce \(\ell_1\)-min-pm to a minimum weight vertex cover problem in a bipartite graph with a polynomial-time computable bipartite-submodular cost function. Recall that, by Theorem 1, the latter problem is solvable in polynomial time.

Let _G_=(_A,B;E_) be the bipartite graph and _M_ be a fixed _q_-matching. We first start with a series of preprocessing steps. If the _q_-matching _M_ is not maximal, then the problem is infeasible and we stop. Otherwise, we iterate through all edges and check whether they are already dominated. If an edge is already dominated, then we delete it. This can be done as there always exists an optimal solution that does not decrease the values on _M_ and does not increase the values on _E_\\_M_. Therefore, we may assume that the _q_-matching _M_ is maximal and all edges outside _M_ are blocking edges.

We construct an an auxiliary bipartite graph _H_=(_U,W;F_) as follows. For each vertex _v_, we add \(\ell_v\) copies \(v_1,\dots,v_{\ell_v}\) of _v_, where \(\ell_v\) is the number of edges in _E(v_)\\_M(v_). These vertices are added to _U_ if \(v\in A\) and to _W_ if \(v\in B\). For each vertex _v_, consider an arbitrary ordering \(e_1^v,\dots,e_{\ell_v}^v\) of the non-matching edges incident to _v_. Then we define the edges of _H_ as follows: \(u_iv_j\in F\) if and only if \(uv\in E\backslash M\), \(uv=e_i^u\), and \(uv=e_j^v\).

Now we define an LP for each vertex _v_ saturated by _M_ and each subset \(\{e_{j_1}^v,\dots,e_{j_k}^v\}\) of \(\{e_1^v,\dots,e_{\ell_v}^v\}\):

\(\text{min}\sum_{e\in E(v)}|x(e)-p_v(e)|\)<br>
\((LP_v(v_{j_1},\dots,v_{j_k}))\text{s.t.}0\le x(e_{ji}^v)\le min_{e\in M(v)}x(e)\text{for}1\le i\le k\)

Though the above formulation is not an LP, both the objective function and the constraints can be linearized using standard techniques. It is not difficult to see that the optimum value of the LP is exactly the minimum cost of dominating all of {_e_<sub>_j_<sub>1</sub></sub>_,...,e<sub>j<sub>k</sub></sub>_} at _v_ by changing the values of the edges. We denote the optimum value by OPT_<sub>v</sub>(v_<sub>_j_<sub>1</sub></sub>_,...,v<sub>j<sub>k</sub></sub>_). If _v_ is not saturated by _M_, then OPT_<sub>v</sub>(v_<sub>_j_<sub>1</sub></sub>_,...,v<sub>j<sub>k</sub></sub>_) is defined to be \(+\infty\), since then no edge can be dominated at _v_. By the maximality of _M_, at least one endpoint of each blocking edge is saturated, so we know that there exists a solution.

For each vertex \(v\in A\cup B\), we define a function _f<sub>v</sub>_. Let \(X\subseteq U\cup W\). If \(X\cap\{v_1,\dots,v_{\ell_v}\}=\emptyset\), then define _f<sub>v</sub>(X_):=0. Otherwise, if \(X\cap\{v_1,\dots,v_{\ell_v}\}=\{v_{j_1},\dots,v_{j_k}\}\), then define _f<sub>v</sub>(X_)=_f<sub>v</sub>_({_v_<sub>_j_<sub>1</sub></sub>_,...,v<sub>j<sub>k</sub></sub>_}):=_OPT<sub>v</sub>(v_<sub>_j_<sub>1</sub></sub>_,...,v<sub>j<sub>k</sub></sub>_).

**Claim 14.** _For each_ \(v\in A\cup B\)_, f<sub>v</sub> is submodular._

C
e
a
d
b

C''
0
0
1
1
0
0
1
1
1
1
1
1
0
0
1
1
0
a'
1
d'
0
1
0
b'
0
d''
b''

(a) An instance of vertex-cover. Note that {_a,c_} is a vertex cover of minimum size.

(b) The corresponding \(\ell_1\)-min-pm instance. If the values of \(p_{a^\prime}(a'a'')\) and \(p_{c^\prime}(c'c'')\) are increased to 1, then thick edges form a weakly stable matching.

Figure 2: An illustration of Theorem 12. Higher values correspond to higher preferences.

