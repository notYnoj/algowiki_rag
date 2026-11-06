### 5.4 Proof of the Coding Advantage

Lemma 5.2 supplies the coding computation, and Lemma 5.3 supplies the matrix labels that bound routing. We now combine them to prove Theorem 3.2 from the main results.

_Proof of Theorem 3.2._ Give each edge _uw_ length \(\ell_{uw}=\mathrm{rank}_\mathbb{Q}(M_w-M_u)\). These lengths are used only in the proof; a zero-length edge still has unit capacity. Along any undirected path \(s_i=u_0,\dots,u_p=t_{\sigma(i)}\), the matrix differences sum to the session endpoint difference, which has rank _m_, so<tbc>

\(m=\mathrm{rank}_\mathbb{Q}\left(\sum_{j=1}^p(M_{u_j}-M_{u_{j-1}})\right)\le\sum_{j=1}^p\ell_{u_{j-1}u_j}.\)

<tbc>Traversing an edge in reverse only negates its matrix difference and does not change its rank. For a common routing rate _r_, let _f<sub>i,P</sub>_ be the flow of session _i_ on path _P_. The unit edge-capacity constraints imply<tbc>

\(rWm\le\sum_{i,P}f_{i,P}\sum_{e\in P}\ell_e=\sum_e\ell_e\sum_{i,P:e\in P}f_{i,P}\le\sum_e\ell_e=S.\)

<tbc>Therefore,

\(R_\mathrm{route}\le\rho:=\frac{S}{Wm}=1-\eta<1.\) (12)

Coding, in contrast, approaches common rate one by pipelining. Schedule one execution of the circuit in gate order. Suppose it takes _D_ rounds, with each edge _e_ sending one bit only in round _t<sub>e</sub>_. Give each source _k_ independent bits and delay the execution of batch _j_ by _j_ rounds, for _j_=0_,...,k_-1. Each edge then sends once in each of _k_ consecutive rounds, respecting capacity and the causal order within every batch. All messages arrive within at most _k+D_ rounds, giving common rate at least _k/(k+D_). Choosing

\(k>\frac{D\rho}{1-\rho}\) (13)

gives a finite-round binary linear protocol with rate strictly above the routing bound \(\rho\). Letting \(k\rightarrow\infty\) yields \(R_\mathrm{code}\ge 1\), while the unit-capacity cut at any source leaf gives \(R_\mathrm{code}\le 1\).

If the graph has parallel edges, insert a private vertex _x<sub>e</sub>_ into every edge _uw_ and set _M<sub>x<sub>e</sub></sub>=M<sub>u</sub>_. Both new edges have capacity one, and their lengths sum to the original length. The new vertex only forwards information, so coding still has a constant startup delay and the routing bound is unchanged. Thus the network can be chosen to be simple. Substituting \(\eta=33/338432\) from Corollary 5.4 proves the stated gap.

The next section uses the same total-rank saving to accelerate address interchange. The inequality \(S/W<m^{1-\varepsilon}\) in Corollary 5.4 will determine the recursion exponent.

## 6 Address-Field Interchange

Sorting repeatedly moves data to the positions needed for subsequent comparisons. We use coding to accelerate one fixed permutation: interchanging two fields of an array address. The sorting algorithms below require only this operation, sequential scans, and sorting in memory.

