By Theorem 7.7, a query on _G+U_ is equivalent, with matching cost, to a \(\beta\)-factor query on _H+U<sub>H</sub>_, where _H_ has 4_n_ vertices, degree bounds \(\beta\le 2f\), dimension _N<sub>H</sub>=O(nf_), and |_U<sub>H</sub>_|=_O(f_). The susceptible edges _E<sub>Q</sub>_ of _G_ correspond to a susceptible set \(E_Q^H\) of _H_ with \(|E_Q^H|=O(\sigma)\). We instantiate Theorem 8.12 on _H_ with capacity parameter _k_:=2_f_, susceptible-set size \(O(\sigma)\), and update size _O(f_). Substituting _k=O(f_) and matrix dimension _N<sub>H</sub>=O(nf_) into the bounds of Theorem 8.12 yields the stated preprocessing, space, and query complexities. \(\square\)

## 9 Lower Bounds

In this section, we present our lower bound results.

We first show that any (_s,t_)-Bounded Max-Flow sensitivity oracle requires \(\Omega(min\{\sigma^2,n^2\})\) space, irrespective of the query time, assuming at least two edge updates. This holds even for the case when flow value is bounded by 1, and imply that our oracles of Theorem 4.2, 4.5 have almost optimal space for a constant number of edge updates.

**Theorem 9.1** (Flows and Cuts)**.** _For any positive integers n and_ \(\sigma\) _satisfying_ \(4\le\sigma\le n(n-1)\)_, there exists an n-vertex directed unit-capacity graph G_=(_V,E_) _and a susceptible edge set E<sub>Q</sub> disjoint from E, with_ \(|E_Q|=O(\sigma)\)_, such that any subset sensitivity oracle supporting at most f_=2 _updates requires_ \(\Omega(min\{\sigma^2,n^2\})\) _bits of space for each of the following problems:_

(_a)_ _k-bounded_ (_s,t_) _maximum flow and_ (_s,t_) _minimum cut, for k_=1;<tbc>

(_b)_ _Global directed minimum cut;_<tbc>

_(c)_ _s-min-cut and s-rooted spanning arborescences (fixed source s)._

_Proof._ Let \(p=min(\lfloor\sigma/4\rfloor,\lfloor n/4\rfloor)\) and let \(M\in\{0,1\}^{p\times p}\) be an arbitrary binary matrix. Define a graph _G_ with vertex-set \(V(G)=X\cup Y\cup\{s,t\}\cup Z\), where _X_={_x_<sub>1</sub>_,...,x<sub>p</sub>_}, _Y_={_y_<sub>1</sub>_,...,y<sub>p</sub>_}, and _Z_ consists of _n_-2_p_-2 isolated dummy vertices, and the edge set

\(E(G)=\{(x_a,y_b):M[a,b]=1\}\cup\{(v,s),(t,v):v\in V(G)\backslash\{s,t\}\}.\)

Also, define the susceptible edge set \(E_Q=\{(s,x_a),(y_b,t):a,b\in[p]\}\), so \(E_Q\cap E(G)=\emptyset\) and \(|E_Q|=2p\le\sigma\).

Consider an update \(U=\{(s,x_i),(y_j,t)\}\subseteq E_Q\). In _G+U_, every simple (_s,t_)-path must use the inserted edges (_s,x<sub>i</sub>_) and (_y<sub>j</sub>,t_), since the edges (_v,s_) and (_t,v_) cannot lie on a simple (_s,t_)-path. Hence (_s,x<sub>i</sub>,y<sub>j</sub>,t_) is the unique candidate (_s,t_)-path, which exists if and only if \((x_i,y_j)\in E(G)\), that is, _M_\[_i,j_\]=1. We now show that each of the listed problems distinguishes whether _M_\[_i,j_\]=1.

(a) Since there is at most one (_s,t_)-path, the value of the 1-bounded (_s,t_)-maximum flow (equivalently, the (_s,t_)-minimum cut) value in _G+U_ is 1 if _M_\[_i,j_\]=1 and 0 otherwise.<tbc>

(b) Observe that any cut having _s_ on the sink side or _t_ on the source side will have a capacity of 1, because of the fixed edges of form (_v,s_) and (_t,v_). As discussed previously, (_s,t_)-min-cut in _G+U_ is 1 if and only if _M_\[_i,j_\]=1. Hence the value of global directed minimum cut in _G+U_ equals _M_\[_i,j_\].<tbc>

(c) From the above discussions, _s_-min-cut in _G+U_ has value exactly _M_\[_i,j_\]. Moreover, an _s_-rooted spanning arborescence exists if and only if every vertex is reachable from _s_, which holds exactly when the edge (_x<sub>i</sub>,y<sub>j</sub>_) is present, that is, when _M_\[_i,j_\]=1.<tbc>

