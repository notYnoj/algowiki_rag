## 3 Preliminaries

Let \[_n_\]={1_,...,n_}. Let log denote the base-2 logarithm, unless stated otherwise. For any set _S_, let |_S_| denote the size of the set. For an empty set, we use the conventions \(\mathrm{min}(\emptyset)=\infty\) and \(\mathrm{max}(\emptyset)=-\infty\). In our algorithms, we use \(x\leftarrow^\pm y\) to denote \(x\leftarrow x+y\) and \(x\leftarrow^\mathrm{min}y\) to denote \(x\leftarrow\mathrm{min}(x,y)\). For sets, we use \(A\leftarrow^\cup B\) to denote \(A\leftarrow A\cup B\).

For a graph _G_=(_V,E_), we typically use _n_=|_V_| and _m_=|_E_| to denote the number of vertices and edges respectively. We use _G_=(_V,E,_wt) to denote a weighted graph with weight function \(\mathrm{wt}:E\mapsto\mathbb{Z}\). For any \(S\subseteq V\) , _E(S_) denotes all edges incident to some vertex in _S_. Unless otherwise stated, all graphs are undirected. Furthermore, we assume (without loss of generality) that all graphs are connected.

For any two vertices \(s,t\in V\) , let dist_<sub>G</sub>(s,t_) denote the length of the shortest path from _s_ to _t_. When the context is clear, we omit _G_ and write dist(_s,t_). For any path \(\pi\subseteq G\) (not necessarily shortest), let \(|\pi|\) denote the length, or number of edges, of \(\pi\). For a subset of vertices \(S\subseteq V\) and a vertex \(v\in V\) , let \(\mathrm{dist}(S,v):=\mathrm{min}_{s\in S}\mathrm{dist}_G(s,v)\). For any vertex \(s\in V\) , let \(N(s,r):=\{v\text{s.t.}\mathrm{dist}(s,v)\le r\}\) and for a subset of vertices \(S\subset V\) , let \(N(S,r):=\{v\text{s.t.}\mathrm{dist}(S,v)\le r\}\). Let _N(v_):=_N(v,_1) and _N(S_):=_N(S,_1). Let \(\mathrm{diam}_G(S):=\mathrm{max}_{s,t\in S}\mathrm{dist}_G(s,t)\) denote the diameter of a subset _S_. For a given vertex \(s\in V\) and distance _r_, let _L(s,r_):={_v_ s.t. dist(_s,v_)=_r_}.

Given a matrix _A_, we let _A_\[_i,j_\] denote the entry of _A_ in the _i_-th row and _j_-th column. Let \(0_{a\times b}\) denote an \(a\times b\) matrix of 0s. Let T<sub>MUL</sub>(_n_<sub>1</sub>_,n_<sub>2</sub>_,n_<sub>3</sub>) denote the time required to compute a \(n_1\times n_2\times n_3\) dimensional matrix product i.e. the product of an \(n_1\times n_2\) matrix and an \(n_2\times n_3\) matrix. Given matrices _A,B_, we let _AB_ denote the standard matrix product (either Boolean or integer), and _A⋆B_ the (min,+) (or Min-Plus) matrix product, where (_A⋆B_)\[_i,j_\]=min_<sub>k</sub>{A_\[_i,k_\]+_B_\[_k,j_\]}. Let T<sub>BMM</sub>(_n_<sub>1</sub>_,n_<sub>2</sub>_,n_<sub>3</sub>) denote the time required to compute a \(n_1\times n_2\times n_3\) dimensional boolean matrix product, and T<sub>MPP</sub>(_n_<sub>1</sub>_,n_<sub>2</sub>_,n_<sub>3</sub>|_B_<sub>1</sub>_,B_<sub>2</sub>) the time required to compute the (min,+) product of a \(n_1\times n_2\) matrix with entries in \([B_1]\cup\{\infty\}\) and a \(n_2\times n_3\) matrix with entries in \([B_2]\cup\{\infty\}\). Let T<sub>MPP</sub>(_n_<sub>1</sub>_,n_<sub>2</sub>_,n_<sub>3</sub>|_B_):=T<sub>MPP</sub>(_n_<sub>1</sub>_,n_<sub>2</sub>_,n_<sub>3</sub>|_B,B_). In some cases, we write T<sub>BMM</sub>(_A,B,C_):=T<sub>BMM</sub>(|_A|,|B_|,|_C_|) where _A,B,C_ are sets. We also allow combinations of sets and integers, e.g. for set _A_ and integers _n_<sub>2</sub>_,n_<sub>3</sub>, T<sub>BMM</sub>(_A,n_<sub>2</sub>_,n_<sub>3</sub>):=T<sub>BMM</sub>(|_A|,n_<sub>2</sub>_,n_<sub>3</sub>).

## 4 Low Diameter Small Neighborhood Decomposition

In this section, we present an efficient algorithm for computing a low diameter small neighborhood decomposition. We begin by defining the desired properties.

**Definition 4.1.** _A partition of V into subsets V_<sub>1</sub>_,...,V<sub>k</sub> is a_ \((d,\phi)\)_-low diameter small neighborhood decomposition_ (LDSND_) of G_=(_V,E_) _if:_

1. _(Low Diameter)_ \(\mathrm{diam}_G(V_i)\le d\) _for all_ \(i\in[k]\).<tbc>

_2._ _(Total Neighborhood Size)_ \(\sum_{i=1}^k|N(V_i)|\le\phi n\).

We now give an efficient algorithm for computing a low diameter small neighborhood decomposition.

**Theorem 4.2.** _For any_ \(\psi>1\)_, there is a randomized_ \(O\left(n^2\psi^4\mathrm{log}n\mathrm{log}_\psi n\right)\) _time algorithm that given an n-vertex m-edge undirected, unweighted graph G computes a_ \((d,\phi)\)-LDSND _where_ \(d=6\cdot 3^{\mathrm{log}_\psi n}\) _and_ \(\phi=O\left(\psi\mathrm{log}n\mathrm{log}_\psi n\right)\) _Furthermore, this algorithm computes N(V<sub>i</sub>_) _for all subsets V<sub>i</sub> in the decomposition._

_Proof._ We give an algorithm that computes a collection of subsets _V_<sub>1</sub>_,...,V<sub>k</sub>_ such that \((1)V=V_1\cup\cdots\cup V_k\), \((2)\mathrm{diam}_G(V_i)\le d\) for all _i_, and \((3)\sum_i|N(V_i)|\le\phi n\). From here, it is easy to observe that by removing duplicate vertices, we obtain a partition that is a \((d,\phi)\)-LDSND, as removing vertices can only reduce the diameter and the total neighborhood size.

First, we show that any vertex _v_ has a small-diameter neighborhood that does not expand.

**Claim 4.3.** _For every_ \(v\in V\)_, there exists_ \(0\le k<\lceil\mathrm{log}_\psi n\rceil\) _such that_ \(|N(v,3^{k+1})|\le\psi^{k+1}\) _and_ \(|N(v,3^k)|>\psi^k\).

