## Appendix A: Mathematical description

The mathematical description of the checks in `cottax` is given here; starting from the definition of a place, moving to the definition of nodes, the graph and its validity checks, a runnable partition, and finally the executable graph.

These mathematical constructs are repeated almost verbatim in the Python package, and furthermore allow for a comparison with the existing graph-based theory in [26, 28, 56].

### 1. Places

A place \(p=(\rho_0,\rho_1,\dots)\in P\) is an ordered sequence of segments \(\rho_j\) (e.g. indexes in a nested hierarchical structure). The following operation is defined for \(a,b\in P\) (both places):

\(\text{\textbf{Incomparable:}}a,b\in P:a\|b:\Leftrightarrow a\unknown\text{\textit{b}}\text{and}b\unknown\text{\textit{a}}\) (A1)

Intuitively, comparable means that _a_ is either containing (a prefix of) _b_ in the hierarchical structure or vice versa (e.g. _c.d_ and _c_ are comparable): i.e. \(a\sqsubseteq b\) iff _a_ is a prefix of _b_. Two places being comparable is the generalisation of two places being equal in a flat namespace: two nodes with one owning _a.b_ and the other owning _a_ would equally be a conflict.

### 2. Nodes

A node _n_ in the dependency graph is a set of inputs _I<sub>n</sub>_={_p<sub>j</sub>_} and outputs _O<sub>n</sub>_={_p<sub>k</sub>_}, which are all simply a place:

\(n=(I_n,O_n)\)

The following validity checks are enforced for every node \(n\in N\):

(A.1) **No node owns something twice**:<tbc>

\(o\|m\forall o,m\in O_n,o\neq m\)

(A.2) **No node reads what it writes**:<tbc>

\(o\|i\forall o\in O_n,i\in I_n\)

### 3. Graph

A graph _G_=(_N_) is constructed of valid nodes _N_={_n<sub>i</sub>_} (it does not need to know about conditional or functional nodes to SCC) with edges _E_ directly implied by the nodes sharing inputs or outputs:

\(E=\{(n_i,n_j):\exists o\in O_i,p\in I_j\text{with}o=p\}.\) (A2)

This has to satisfy the graph-validity checks:

(A.3) **One producer per place**: owned places are incomparable.<tbc>

\(o\|m\forall n_i\neq n_j,o\in O_i,m\in O_j\)

(A.4) **Exact reads**: a read is exactly an owned place; no partial reads.

\(o\|p\text{or}o=p\forall n_i,n_j,o\in O_i,p\in I_j\)

The latter check is not entirely required: _a.b_ could be read if _a_ is owned, but for simplicity this is not implemented yet: simply pass the full _a_ instead (or make a projection-type node which extracts it).

Two nodes are _p∼<sub>G</sub>q_ iff they are reachable from each other through edges of the graph _G_ in both directions (\(p\rightarrow q\) and \(q\rightarrow p\) are paths in _G_, with path length \(\ge 0\)). A _strongly connected component_ is then the equivalence class (grouping all nodes which are ∼<sub>_G_</sub>):

\([n]_G=\{k\in N:k\sim_Gn\}\)

