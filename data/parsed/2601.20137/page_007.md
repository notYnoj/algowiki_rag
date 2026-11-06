preserves connected components of _F<sub>j</sub>_ (Lemma 3), every such edge still creates a cycle. The displaced edge also has both endpoints in the same component of _F<sub>j</sub>_, so it would induce a cycle if re-added. Therefore _F<sub>j</sub>_ remains maximal.

Let _e<sub>old</sub>_={_u,w_} be the edge discarded from _F<sub>k</sub>_. Since _w_=parent(_u_), the vertices _u_ and _w_ were in the same connected component of _F<sub>k</sub>_ before the swap, and they remain so afterward by Lemma 3. By Lemma 4, _u_ and _w_ are connected in every _F<sub>j</sub>_ for \(1\le j\le k\). Each forest _F<sub>j</sub>_ therefore contains a path _P<sub>j</sub>_ from _u_ to _w_ using edges from _E<sub>j</sub>_. Since _E_<sub>1</sub>_,E_<sub>2</sub>_,...,E<sub>k</sub>_ are pairwise disjoint, the paths _P_<sub>1</sub>_,P_<sub>2</sub>_,...,P<sub>k</sub>_ are edge-disjoint. Hence \(\lambda(u,w;G')\ge k\).

### 4.3 Complexity analysis of sparse certificate maintenance algorithm

Initialization consists of two steps: computing the forest decomposition _F_<sub>1</sub>_,F_<sub>2</sub>_,...,F<sub>k</sub>_ via Algorithm 1 in _O(m_) time, and building the _k_ Link-Cut structures _LC_<sub>1</sub>_,LC_<sub>2</sub>_,...,LC<sub>k</sub>_. The latter requires _O(kn_) MakeTree and link operations, each costing _O_(log_n_) amortized time, for a total initialization cost of \(O(m+k\cdot n\mathrm{log}n)\).

For each edge addition, HandleAddition calls TryAdd on at most _k_ forests. Each TryAdd call performs _O_(1) Link-Cut tree operations (FindRoot, cut, link), so the amortized cost per edge addition is _O(k_log_n_).

## 5 Restoration after Edge Removal

### 5.1 Edge-connectivity restoration algorithm

This section addresses restoring _k_-edge-connectivity after an edge deletion. Let _e_={_u,v_} be the deleted edge and let \(G'=G\backslash\{e\}\). If \(\lambda(G')\ge k\), no action is needed. Otherwise, the algorithm must compute a set of augmenting edges _E<sub>aug</sub>_ such that \(\lambda(G'\cup E_{aug})\ge k\). We compute a maximum _u-v_ flow in \(G'\) using Dinic’s algorithm \[4\], whose complexity on unit- capacity networks is \(O(\mathrm{min}(n^{2/3},m^{1/2})\cdot m)\) by Even and Tarjan \[5\], and use the resulting residual graph to identify _E<sub>aug</sub>_.

We model each undirected edge \(\{u,v\}\in E\) as a pair of directed arcs (_u,v_) and (_v,u_), each with unit capacity; for background on flow networks and residual graphs we refer to \[1\]. In the resulting residual graph _G<sub>f</sub>_, a saturated arc (_u,v_) with _f(u,v_)=1 is replaced by a backward arc (_v,u_) with residual capacity 2, while an unsaturated arc retains both directions with residual capacity 1.

The procedure HandleDeletion (Algorithm 4) works as follows. Given the deleted edge _e_={_u,v_}, it computes a maximum _u-v_ flow on \(G'=G\backslash\{e\}\). If the flow value is still at least _k_, the edge was redundant and no action is needed. Otherwise, let _G<sub>f</sub>_ denote the residual graph. The algorithm computes _S_, the set of vertices reachable from _u_ in _G<sub>f</sub>_, and _T_, the set of vertices from which _v_ is reachable in _G<sub>f</sub>_; both sets are obtained by BFS or DFS algorithm on _G<sub>f</sub>_.

The algorithm distinguishes two cases. If \(|S|\ge 2\) or \(|T|\ge 2\), there exists a pair \(u'\in S\), \(v'\in T\) with \(\{u',v'\}\neq\{u,v\}\); the algorithm adds \(\{u',v'\}\) to \(G'\) (Algorithm 4, lines 15-17). If _S_={_u_} and _T_={_v_}, the only edge from _S_ to _T_ is the deleted edge {_u,v_}, so instead the algorithm selects an arbitrary vertex \(w\in V\backslash\{u,v\}\) and adds the two edges {_u,w_} and {_w,v_} (Algorithm 4, lines 12-13).

### 5.2 Correctness and complexity of edge-connectivity restoration algorithm

We show that edges added by HandleDeletion increases the maximum _u-v_ flow by one (Lemma 6), and that the full procedure restores \(\lambda(G')\ge k\) (Theorem 7).

**Lemma 6.** _Let f be a maximum u-v flow in_ \(G'=G\backslash\{e\}\) _(e_={_u,v}), let G<sub>f</sub> be the residual graph, and define_ \(S=\{w\in V:w\text{\textit{is reachable from}}u\text{\textit{in}}G_f\}\) _and_ \(T=\{w\in V:v\text{\textit{is reachable from}}w\text{\textit{in}}G_f\}\)_. Then:_

1. \(S\cap T=\emptyset\).<tbc>

