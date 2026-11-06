For notational convenience, we identify the vertices with their topological indices; henceforth, we assume _V_={1_,...,T_} and \(\tau(v)=v\), so an edge (_u,v_) implies _u\<v_. All references to cuts, frontiers, and frontier width are with respect to this fixed topological order. We are free to choose \(\tau\) when formulating the DP; in particular, in applications where the underlying graph has bounded pathwidth, we will later choose \(\tau\) derived from a path decomposition.

Standard dynamic programming formulations typically involve recurrences with a constant number of terms. We formalize this via a bounded in-degree assumption.

**Assumption 1** (Locality)**.** _There exists a universal constant_ \(\Delta_\mathrm{max}\in\mathbb{N}\) _such that for all_ \(v\in V\) _, the in-degree is bounded:_

\(\mathrm{deg}^-(v)=|\{u:(u,v)\in E\}|\le\Delta_\mathrm{max}.\)

This assumption implies that the evaluation of a single state, given the values of its predecessors, requires _O_(1) primitive semiring operations.

## 2.2 Time order and frontier width

The space complexity of evaluating a DP is governed not by the total size of the state space, but by the maximum number of values that must be persisted across any cut in the topological order. We formalize this memory footprint as the _frontier width_. The following definition is specific to the fixed topological order \(\tau\); changing \(\tau\) may change the frontier width.

**Definition 2** (Frontier and frontier width)**.** _For any time step_ \(\ell\in\{0,\dots,T\}\)_, the_ frontier at time \(\ell\)_, denoted_ \(\mathrm{Front}(\ell)\)_, is the set of vertices processed at or before time_ \(\ell\) _that have outgoing edges to vertices processed strictly after_ \(\ell\):<tbc>

\(\mathrm{Front}(\ell):=\big\{v\in V:v\le\ell\text{\textit{and}}\exists w>\ell\text{\textit{such that}}(v,w)\in E\big\}.\)

<tbc>_The_ frontier width _of G with respect to_ \(\tau\)_, denoted_ \(\omega(G,\tau)\)_, is the maximum frontier size:_

\(\omega(G,\tau):=\mathrm{max}_{0\le\ell\le T}|\mathrm{Front}(\ell)|,\)

_and we write_ \(\omega\) _when G and_ \(\tau\) _are clear from context._

The frontier \(\mathrm{Front}(\ell)\) captures precisely the set of DP state values that a forward-pass evaluation algorithm must retain in memory after step \(\ell\) in order to continue computing all future states \(w>\ell\). In geometric settings such as the standard Needleman-Wunsch algorithm on an \(m\times n\) grid (with \(m\le n\)), a natural topological order proceeds column-by-column or row-by-row; the frontier then corresponds to a single column or row, and \(\omega(G,\tau)=\Theta(\mathrm{min}\{m,n\})\) for that choice of \(\tau\).

## 2.3 Semiring and witness structure

We restrict our attention to optimization problems over ordered structures where one seeks not just the optimal value, but a canonical certificate (witness) of that optimality.

**Assumption 2** (Max-type semiring with deterministic witnesses)**.** _We consider computations over a structure_ \((\mathcal{S},\oplus,\otimes,\unknown)\) _satisfying:_

1. \((\mathcal{S},\unknown)\) _is a totally ordered set._<tbc>

_2._ _The "addition" operator_ \(\oplus\) _is the supremum with respect to_ \(\unknown\) _over finite subsets of_ S_, and in particular for any_ \(a,b\in\mathcal{S}\) _we have_ \(a\oplus b=\mathrm{max}_\unknown\{a,b\}\)_. There is a distinguished bottom element_ \(\mathbf{0}\in\mathcal{S}\) _such that_ \(\mathbf{0}\oplus a=a\) _for all a._<tbc>

_3._ _The "multiplication" operator_ \(\otimes\) _is associative and distributes over_ \(\oplus\).<tbc>

_4._ \(\otimes\) _is monotone with respect to_ \(\unknown\)_: if_ \(a\unknown b\)_, then_ \(a\otimes c\unknown b\otimes c\) _and_ \(c\otimes a\unknown c\otimes b\) _for all_ \(c\in\mathcal{S}\).

_For each vertex_ \(v\in V\) _, we associate a value_ \(x_v\in\mathcal{S}\) _defined by the recurrence_<tbc>

\(x_v=\left\{\begin{array}{ c c }
a_v & \text{\textit{if}}v\in S_\mathrm{src}, \\
\oplus_{(u,v)\in E}\big(x_u\otimes w_{u,v}\big) & \text{\textit{otherwise}},
\end{array}\right.\)

