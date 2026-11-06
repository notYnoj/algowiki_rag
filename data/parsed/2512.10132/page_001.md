# Universal Hirschberg for Width Bounded Dynamic Programs

Logan Nye, MD

Carnegie Mellon University School of Computer Science

5000 Forbes Ave Pittsburgh, PA 15213 USA

`lnye@andrew.cmu.edu`

ORCID: 0009-0002-9136-045X

**Abstract**

Hirschberg’s algorithm (1975) reduces space complexity for the Longest Common Subsequence problem from _O(N_<sup>2</sup>) to _O(N_) via recursive midpoint bisection on a grid DP. We show that the underlying idea generalizes to a broad class of dynamic programs with local dependencies on directed acyclic graphs (DP DAGs). Modeling a DP as deterministic time-evolution over a topologically ordered DAG with frontier width \(\omega\) and bounded in-degree, and assuming a max-type semiring with deterministic tie- breaking, we prove that in a standard offline random-access model any such DP admits deterministic traceback in space \(O(\omega logT+polylogT)\) cells over a fixed finite alphabet, where _T_ is the number of states. Our construction replaces backward DPs by forward-only recomputation and organizes the time order into a height-compressed recursion tree whose nodes expose small "middle frontiers" across which every optimal path must pass. The framework yields near-optimal traceback bounds for asymmetric and banded sequence alignment, one-dimensional recurrences, and DP formulations on graphs of bounded pathwidth. We also show that an \(\Omega(\omega)\) space term (in bits) is unavoidable in forward single-pass models and discuss conjectured \(\sqrt{T}\)-type barriers in streaming settings, supporting the view that space-efficient traceback is a structural property of width-bounded DP DAGs rather than a peculiarity of grid-based algorithms.

arXiv:2512.10132v1 [cs.DS] 10 Dec 2025

