## 1 Introduction

Dynamic programming (DP) is a central paradigm for discrete optimization and combinatorial problems. Given a DP formulation on a directed acyclic graph (DAG), we typically distinguish two tasks:

• _Value computation_: compute the optimal value _x<sub>t</sub>_ at a designated sink _t_;<tbc>

• _Witness reconstruction_: reconstruct a specific optimal witness: e.g., a path from a source to _t_, an alignment, a labeling, or other structured solution.

For many DP formulations--on grids, banded lattices, and pathwidth- or treewidth-based decompositions-- the value _x<sub>t</sub>_ can be computed in space proportional to a structural width parameter, such as a frontier width \(\omega\) or a pathwidth pw(_G_), by storing only a single frontier of DP states at a time. In contrast, witness reconstruction is usually implemented by storing the entire DP table or a large fraction of it, requiring \(\Theta(T)\) space where _T_ is the number of states. This raises a question:

_For width-bounded DPs where the decision problem can be solved in_ \(O(\omega)\) _space, how much additional space is actually needed to recover a single optimal witness?_

### Hirschberg as a motivating example.

A classical exception to the \(\Theta(T)\) traceback pattern is Hirschberg’s algorithm for LCS/edit distance \[1\]. On an \(m\times n\) grid DP (\(T=\Theta(mn)\), frontier width \(\omega=min\{m,n\}\) under a natural row- or column-major topological order), naive traceback requires _O(mn_) space. Hirschberg’s divide-and-conquer algorithm recursively bisects along the longer dimension, uses forward and backward DPs to identify a midpoint on some optimal alignment, and recurses on the two subproblems. This reconstructs an optimal alignment in _O(m+n_) space. The standard presentation is tightly coupled to the 2D grid geometry and the fact that the reverse DP has the same frontier width as the forward DP.

### This work: a structural "Universal Hirschberg" theorem.

We generalize Hirschberg’s idea from grids to arbitrary _time-ordered_ DP DAGs with bounded frontier width, in an offline model with random access to the instance and inexpensive recomputation. Informally:

**Theorem 1** (Informal main result)**.** _Let G be a DP DAG on T vertices equipped with a fixed topological order_ \(\tau\)_, frontier width_ \(\omega=\omega(G,\tau)\)_, bounded in-degree, and a max-type semiring recurrence with deterministic tie-breaking, so that each vertex has a unique witness predecessor. In the standard random-access multitape Turing-machine (or RAM) model, there is a deterministic algorithm that, given an encoding of G and a designated sink t,_

• _computes x<sub>t</sub> and outputs the canonical optimal source-to-t witness path (as determined by the fixed tie-breaking rule),_<tbc>

• _runs in time_ poly(_T), and_<tbc>

• _uses work-tape space_<tbc>

<tbc>\(\mathsf{SPACE}_\mathsf{traceback}=O\big(\omega logT+\mathsf{polylog}T\big)\)<tbc>

<tbc>_measured in tape cells over a fixed finite alphabet. Equivalently, the algorithm stores the values of_ \(O(\omega)\) _DP states (each encoded in O_(log_T_) _bits) plus an additional O_(polylog_T_) _words of recursion metadata._

Thus, up to polylogarithmic factors, traceback can be done in essentially the _same_ space as value computation for any DP DAG whose frontier width is bounded under some topological order. No geometric symmetry, band structure, or small-width backward DP is required; the only structural parameter that enters the space bound is the frontier width \(\omega\).

### Techniques and scope.

Our algorithm organizes the fixed topological order into a balanced binary recursion tree over intervals of "time". Each node induces a subproblem whose internal vertices lie in a time window _I_, with small interfaces to the rest of the DAG. At each level, we:

• identify a _middle frontier_ \(F_I^\mathsf{mid}\) across which every optimal path relevant to the subproblem must pass;<tbc>

