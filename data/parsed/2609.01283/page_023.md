<tbc>requires \(O(|Q|^2(kr)^{\omega-2}+(kr)^\omega)=O(\sigma^2(kr)^{\omega-2}+(kr)^\omega)\) time and \(O(|Q|^2)=O(\sigma^2)\) space. An update toggles at most _f_ entries in _E<sub>Q</sub>_ and at most _f_ entries in _R<sub>switch</sub>_, modifying a total of \(\le 2f\) diagonal entries. Querying the determinant thus takes \(O((2f)^\omega)=O(f^\omega)\) time. □

**Remark 3.12** (Comparison of Oracle Models for Covering)**.** _Similar to the packing problem, the matroid covering problem has following space and query-time trade-offs:_

## 4 Max-Flows, Min-Cuts, _s_-Min-Cuts, Global Min-Cut

### 4.1 Sensitivity Oracles for All-Pairs _k_-Bounded Flow

We first establish the matroid formulation for all-pairs bounded flows. Let _k_ be a positive integer. Let _H_=(_V<sub>H</sub>,E<sub>H</sub>_) be a directed multigraph on _N_ vertices with a designated source _s_<sup>∗</sup> and a designated sink _t_<sup>∗</sup> such that the out-degree of _s_<sup>∗</sup> and the in-degree of _t_<sup>∗</sup> are both equal to \(\lambda\le k\). We add to each vertex \(v\in V_H\backslash\{s^*,t^*\}\) a set of exactly _k_ zero-cost self-loops, and to vertices _s_<sup>∗</sup> and _t_<sup>∗</sup> we add \(k-\lambda\) zero-cost self-loops. Let _M_ denote the number of edges in the resulting graph _H_. We define two partition matroids on the edge set of _H_:

• _M_<sub>out</sub>: A subset \(S\subseteq E_H\) is independent if every vertex \(v\in V_H\backslash\{t^*\}\) has at most one outgoing edge in _S_. This is represented by a matrix \(A_\mathrm{out}\in\{0,1\}^{(N-1)\times M}\), where rows are indexed by _V<sub>H</sub>_\\{_t_<sup>∗</sup>}. The column for an edge _e_=(_u,v_) has a 1 at row _u_ (if \(u\neq t^*\)) and 0 elsewhere.<tbc>

• _M_<sub>in</sub>: A subset \(S\subseteq E_H\) is independent if every vertex \(v\in V_H\backslash\{s^*\}\) has at most one incoming edge in _S_. This is represented by a matrix \(A_\mathrm{in}\in\{0,1\}^{(N-1)\times M}\), where rows are indexed by _V<sub>H</sub>_\\{_s_<sup>∗</sup>}. The column for an edge _e_=(_u,v_) has a 1 at row _v_ (if \(v\neq s^*\)) and 0 elsewhere.

Both matroids have rank _N_-1. The following lemma establishes the equivalence between a _k_- packing of common bases in these matroids and the existence of edge-disjoint (_s_<sup>∗</sup>_,t_<sup>∗</sup>)-paths.

**Lemma 4.1.** _The directed multigraph H contains_ \(\lambda\) _edge-disjoint_ (_s_<sup>∗</sup>_,t_<sup>∗</sup>)_-paths if and only if there exists a set_ \(S\subseteq E_H\) _of size k(N_-1) _that can be partitioned into k bases of M_<sub>out</sub> _as well as M_<sub>in</sub> _(the partitionings may differ)._

_Proof._ For the forward direction, suppose _H_ contains \(\lambda\) edge-disjoint (_s_<sup>∗</sup>_,t_<sup>∗</sup>)-paths \(P_1,\dots,P_\lambda\). Using the _k_ self-loops at each \(v\in V_H\backslash\{s^*,t^*\}\), we extend these paths to a family of \(\lambda\) edge-disjoint sets \((B_1,\dots,B_\lambda)\) by adding self-loops so that for each \(i\in[\lambda]\): (i) \(E(P_i)\subseteq B_i\), and (ii) every \(v\in V_H\backslash\{s^*,t^*\}\) has exactly one incoming and one outgoing edge from _B<sub>i</sub>_, while _s_<sup>∗</sup> has exactly one outgoing edge in _B<sub>i</sub>_ and _t_<sup>∗</sup> has exactly one incoming edge in _B<sub>i</sub>_. For the remaining \(k-\lambda\) indices, we use only self-loops to obtain edge sets satisfying the same in-/out-degree constraints. Let (_B_<sub>1</sub>_,...,B<sub>k</sub>_) denote the resulting family. Each _B<sub>i</sub>_ has size _N_-1 and is independent in both _M_<sub>out</sub> and _M_<sub>in</sub>, hence a basis of both. Thus \(S:=\unknown_{i=1}^kB_i\) has size _k(N_-1) and partitions into _k_ bases of each matroid.

For the converse, suppose \(S\subseteq E_H\) has size _k(N_-1) and partitions into _k_ bases of _M_<sub>out</sub> as well as _M_<sub>in</sub>. Since both matroids are strongly base-orderable, Theorem 2.13 implies _S_ can be partitioned into _k_ common independent sets \(S=C_1\unknown\cdots\unknown C_k\). Fix \(i\in[k]\). Independence in _M_<sub>out</sub> forces every<tbc>

\begin{tabular}{ccc}
 & **_General Sensitivity_** & **_Subset Sensitivity_** \\
 & _(Theorem 3.10)_ & _(Theorem 3.11)_ \\
_Space_ & _O_((_kr_)<sup>2</sup>log_r_) & \(O(\sigma^2)\) \\
_Query Time_ & \(O((\delta k)^\omega)\) & \(O(f^\omega)\) \\
\end{tabular}

