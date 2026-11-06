• compute prefix values from the left boundary to each \(v\in F_I^\mathrm{mid}\) by a single forward DP on _I_;<tbc>

• compute suffix values from each \(v\in F_I^\mathrm{mid}\) to the sink _t_ via forward-only recomputation on subintervals (no backward DP on the reversed graph);<tbc>

• select a canonical midpoint vertex _v<sup>⋆</sup>_ using the max-type semiring and deterministic tie-breaking; and<tbc>

• recurse on the left and right subintervals, carrying only boundary values and a small amount of recursion metadata.

The working frontier buffer always stores at most \(\omega\) DP values at any time, and the recursion tree has depth _O_(log_T_); recursion metadata fits in _O_(polylog_T_) space. We work throughout with finite DAGs of bounded in-degree, max-type semirings with deterministic witnesses, and deterministic algorithms in a random-access model with running time polynomial in _T_.

### Applications and limitations.

Instantiating the framework yields:

• for asymmetric sequence alignment on an \(m\times n\) grid with \(m\le n\), traceback in space _O(m_log(_mn_)+polylog(_mn_));<tbc>

• for one-dimensional recurrences with constant in-degree, traceback in space _O_(polylog_T_);<tbc>

• for banded alignment with bandwidth _B_, traceback in space _O(B_log(_BN_)+polylog(_BN_)); and<tbc>

• for DPs on DAGs of pathwidth pw(_G_), traceback in space \(O\big(\)pw(_G_)log|_V_|+polylog|_V_|\(\big)\).

We also show that an \(\Omega(\omega)\) term (in bits) is unavoidable in any forward, single-pass model where the input is streamed once in topological order, and we discuss conjectured \(\sqrt{T}\)-type barriers in genuinely streaming settings, in contrast to the offline random-access model we analyze.

The rest of the paper develops the formal model and assumptions (Section 2), recasts Hirschberg’s algorithm in structural terms (Section 3), presents the height-compressed recursion and universal traceback algorithm (Sections 4-5), derives applications (Section 6), discusses lower bounds and model variants (Section 7), and concludes with related work and open problems (Sections 8-9).

## 2 Model and Assumptions

We now formalize the setting of dynamic programming as a graph-theoretic problem on a structured directed acyclic graph. We define the parameters governing the space complexity of evaluation and the specific class of optimization problems--max-type recurrences with unique witnesses--to which our results apply.

### 2.1 Dynamic programming as a local DAG

We abstract the dependency structure of a dynamic program into a directed acyclic graph where vertices represent states and edges represent dependencies in the recurrence.

**Definition 1** (Computational DP DAG)**.** _A_ computational DP DAG _is a tuple_

\(G=(V,E,S_\mathrm{src},T_\mathrm{sink},\tau)\)

_where:_

• _V is a finite set of T_=|_V_| _vertices, which we refer to as_ states,<tbc>

• \(E\subseteq V\times V\) _is a set of directed edges representing computational dependencies,_<tbc>

• \(S_\mathrm{src}\subseteq V\) _is a non-empty set of_ source vertices _(states with in-degree_ 0_),_<tbc>

• \(T_\mathrm{sink}\subseteq V\) _is a non-empty set of_ sink vertices,<tbc>

• \(\tau:V\rightarrow\{1,\dots,T\}\) _is a bijection defining a_ topological order_: for every edge_ \((u,v)\in E\)_, we have_ \(\tau(u)<\tau(v)\).

