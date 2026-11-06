_where_ \(a_v\in\mathcal{S}\) _is an initialization value for sources and_ \(w_{u,v}\in\mathcal{S}\) _is the weight of edge_ (_u,v)._

_We assume that every semiring element (weight or DP value) admits a representation using O_(log_T_) _tape cells over a fixed finite alphabet. We refer to this unit of storage (O_(log_T_) _bits) as a_ machine word. _We assume that the primitive operations (comparison,_ \(\oplus\), \(\otimes\)_) as well as index arithmetic on_ {1_,...,T_} _can be performed in time and space polynomial in_ log_T._

_Crucially, we assume a fixed, deterministic tie-breaking rule on edges. Fix once and for all a total order_ \(\prec\) _on the edge set E. For any vertex_ \(v\notin S_\text{src}\)_, let_ \(P(v)=\{u:(u,v)\in E\}\) _be the set of predecessors. We define the unique_ witness predecessor pred(_v_) _as follows:_

\(\mathsf{pred}(v)=u^\star\text{\textit{where}}u^\star\in P(v),x_{u^\star}\otimes w_{u^\star,v}=x_v,\)

_and_ (_u<sup>⋆</sup>,v_) _is_ \(\prec\)_-minimal among all edges_ (_u,v_) _with_ \(u\in P(v)\) _satisfying_ \(x_u\otimes w_{u,v}=x_v\)_. For_ \(v\in S_\text{src}\)_, we set_ \(\mathsf{pred}(v)=\perp\).

The tie-breaking rule ensures that, once the DP values \(\{x_v\}_{v\in V}\) are fixed, the predecessor map \(\mathsf{pred}:V\rightarrow V\cup\{\perp\}\) is uniquely determined.

**Lemma 1** (Consistency of local re-evaluation)**.** _Let_ \(U\subseteq V\) _be any subset of vertices, and let_ \(B\subseteq V\backslash U\) _be a boundary set such that:_

• _for every edge_ \((u,v)\in E\) _with_ \(v\in U\) _and_ \(u\notin U\)_, we have_ \(u\in B\)_, and_<tbc>

• _the subgraph induced by_ \(U\cup B\) _is acyclic and respects the restriction of the topological order_ \(\tau\).

_Suppose we are given the true global DP values_ \(\{x_u\}_{u\in B}\) _on B. If we recompute the DP on the induced subgraph on_ \(U\cup B\) _using these boundary values and the same recurrence and tie-breaking rule, then for every_ \(v\in U\) _the recomputed value_ \(x'_v\) _and predecessor_ \(\mathsf{pred}'(v)\) _coincide with the global value x<sub>v</sub> and predecessor_ pred(_v)._

_Proof._ Order the vertices of \(U\cup B\) according to the restriction of \(\tau\). We prove the claim by induction on this order, restricted to _U_.

_Base case:_ Let _v_ be the first vertex in _U_ according to \(\tau\). If \(v\in S_\text{src}\), its value depends only on initialization _a<sub>v</sub>_, so \(x'_v=x_v\) trivially. If \(v\notin S_\text{src}\), all its predecessors _u_ lie in _B_ (since any predecessor in _U_ would precede _v_ in \(\tau\), contradicting that _v_ is first). The values _x<sub>u</sub>_ for \(u\in B\) are equal to the global values by assumption. Thus, \(x'_v\) is computed from the same multiset \(\{x_u\otimes w_{u,v}\}\) as the global value, and tie-breaking uses the same \(\prec\), so \(x'_v=x_v\) and \(\mathsf{pred}'(v)=\mathsf{pred}(v)\).

_Inductive step:_ For a general \(v\in U\), predecessors lie either in _B_ or in _U_ (earlier in the order). By the induction hypothesis, predecessors in _U_ have correct values \(x'_u=x_u\). Predecessors in _B_ have correct values by assumption. The calculation for _v_ is therefore identical to the global calculation.

This determinism and consistency are essential: they guarantee that for any optimal sink value _x<sub>t</sub>_, there exists a unique canonical trajectory through the DAG obtained by iteratively following \(\mathsf{pred}(\cdot)\), and that re-evaluating the recurrence in any local window with correct boundary values consistently yields the same predecessor choices. This enables space-efficient reconstruction without storing the global pointer graph.

**Definition 3** (Traceback problem)**.** _Given a computational DP DAG G and a target sink_ \(t\in T_\text{sink}\)_, the_ traceback problem _asks to construct the unique sequence of vertices P_=(_v_<sub>0</sub>_,v_<sub>1</sub>_,...,v<sub>k</sub>_) _such that:_

1. _v<sub>k</sub>=t,_<tbc>

2. \(v_0\in S_\text{src}\)_, and_<tbc>

_3._ _for all_ \(1\le i\le k\), _v_<sub>_i_-1</sub>=pred(_v<sub>i</sub>)._

_We refer to P as the canonical optimal witness path from a source to t._

## 2.4 Machine model and space measure

We analyze space complexity in the standard deterministic multitape Turing machine model, which is polynomially equivalent (for space) to the Random Access Machine (RAM) model.

• **Input:** The graph _G_ (adjacency lists, edge weights) is provided on a read-only input tape. The input is _random-access_ in the sense that the machine can move its input head to any vertex or edge description in time polynomial in log_T_.<tbc>

