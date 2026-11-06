VERTEX-COVER

**Input:** A graph _G_=(_V,E_).

**Goal:** Find a vertex cover of minimum size.

## Submodular and bipartite-submodular set functions.

A set function \(f:2^V\rightarrow R\) is called _submodular_ if \(f(X)+f(Y)\ge f(X\cup Y)+f(X\cap Y)\) holds for every \(X,Y\subseteq V\) . It is known that this is equivalent to \(f(X+a)+f(X+b)\ge f(X+a+b)+f(X)\) for every \(X\subseteq V\) and distinct \(a,b\in V\backslash X\). A function _f_ defined on the vertex set of a bipartite graph _G_=(_A,B;E_) is _bipartite-submodular_ if there exist two submodular functions _f<sub>A</sub>_ and _f<sub>B</sub>_ defined on _A_ and _B_, respectively, such that \(f(X)=f_A(X\cap A)+f_B(X\cap B)\) for every \(X\subseteq A\cup B\). The following result appeared in \[16\].

**Theorem 1** (Hochbaum)**.** _Given a bipartite graph G_=(_A,B;E_) _and a polynomial-time computable submodular cost function_ \(c:2^{A\cup B}\rightarrow E\)_, the minimum cost vertex cover problem can be 2-approximated in polynomial time. Furthermore, if c is also bipartite-submodular, then a minimum cost vertex cover can be found in polynomial time._

## Stable matchings.

Let _G_=(_V,E_) be an undirected simple graph, and let _\<<sub>u</sub>_ be a linear order on _N(u_) for each \(u\in V\) . The pair (_G,\>_) is called a _stable roommates instance_. If _G_ is bipartite, then (_G,\>_) is a _stable marriage instance_. If ties are allowed, i.e., _\<<sub>u</sub>_ are weak orders, then (_G,\>_) is a _stable roommates instance with ties_. For a stable roommates instance (_G_=(_V,E),\>_) and a matching \(M\subseteq E\), an edge \(uv\in E\backslash M\) is _blocking_ if _u_ prefers _v_ to its partner in _M_ (or has no partner in _M_) and _v_ prefers _u_ to its partner in _M_ (or has no partner in _M_). If no blocking edge exists, then _M_ is a _stable matching_.

Let (_G,\>_) be a stable roommates instance. A _stable partition of_ (_G,\>_) is a permutation \(\pi:V\rightarrow V\) such that for each \(u\in V\) , (i) if \(\pi(u)\neq\pi^{-1}(u)\), then \(u\pi(u),u\pi^{-1}(u)\in E\) and \(\pi(u)>_u\pi^{-1}(u)\), and (ii) for each _v_ adjacent to _u_, if \(\pi(u)=u\) or \(v>_u\pi^{-1}(u)\), then \(\pi^{-1}(v)>_vu\). The cycles of the permutation \(\pi\) partition the agents into _odd_ and _even cycles_ depending on the parity of their lengths. We call an agent _u_ a _singleton in_ \(\pi\) if \(\pi(u)=u\). The following fundamental result is due to Tan \[28\].

**Theorem 2** (Tan)**.** _Any stable roommates instance_ (_G,\>_) _admits a stable partition_ \(\pi\)_, and such a partition can be found in_ O(|_V_|<sup>2</sup>) _time. Furthermore, each stable partition has the same set of singleton agents and the same set of odd cycles. There exists a stable matching if and only if there exist a stable partition without odd cycles of length_ \(\ge 3\).

We will also need the notion of weak stability. Let (_G_=(_V,E),\>_) be a stable roommates instance with ties, and let \(M\subseteq E\) be a matching. An edge \(uv\in E\backslash M\) _strongly blocks M_ if _u_ strictly prefers _v_ to its partner in _M_ (or has no partner in _M_) and _v_ strictly prefers _u_ to its partner in _M_ (or has no partner in _M_). If no strongly blocking edge exists, then _M_ is a _weakly stable matching_.

We also consider cases where the vertices of _G_ have nonnegative integer capacities _q(v_). In such an instance, we call \(M\subseteq E\) a _q-matching_ if \(|M(v)|\le q(v)\) for each \(v\in V\) . A vertex is _unsaturated_ in _M_ if |_M(v_)|_\<q(v_). We say that an edge \(uv\in E\backslash M\) _blocks M_ if both _u_ and _v_ are either unsaturated by _M_ or strictly prefer the other to some of their partners in _M_. The _q_-matching _M_ is called a _stable q-matching_ if it is not blocked by any edge. We also say that an edge \(uv\in E\backslash M\) is _dominated_ at _u_ if |_M(u_)|=_q(u_) and for all \(xu\in M(u)\), we have _x\><sub>u</sub>v_. Clearly a _q_-matching _M_ is stable if and only if each \(uv\in E\backslash M\) is dominated at either _u_ or _v_.

The hardness of the following problem, proved by Manlove et al. \[23\], is a useful tool for proving NP-completeness of various stable matching problems.

