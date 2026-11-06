# Faster Algorithms for Finding Small Induced Patterns in Sparse Host Graphs

**Abstract.** We study algorithms to detect induced _G_-subgraphs, for fixed patterns _G_, given host graphs with _n_ vertices and _m_ edges as input. We show that:

- There are at least five 5-vertex connected graphs _G_ (out of 21) that can be detected in \(\widetilde{O}(nm)\)-time.

- There are at least sixty-five 6-vertex connected graphs _G_ (out of 112) that can be detected in \(\widetilde{O}(m^2)\)-time.

- The graphs _P_<sub>7</sub> and _C_<sub>7</sub> can be detected in \(\widetilde{O}(nm^2)\)-time.

Our main technical tool is a generalized notion of width of tree decompositions that we call (_p,q_)-width tree decompositions. We use (_p,q_)-width tree decompositions to derive algorithms with running-time \(\widetilde{O}(n^pmq)\) for detecting induced subgraphs. Our upper-bounds are never worse than existing upper-bounds and are faster when _m=o(n_<sup>2</sup>). Moreover, for some patterns, such as _C_<sub>7</sub>, our algorithms are optimal under standard complexity theoretic assumptions.

The new technique we use to obtain fast algorithms for fixed pattern graphs is not scalable to families of pattern graphs. We further refine this idea by constructing pattern-based polynomials that exploit the structure of the tree decomposition, and not just its width, to obtain algorithms for larger classes of graphs. We show:

- An \(\widetilde{O}(m^{k-1})\)-time algorithm for detecting induced _P_<sub>2_k_</sub> in bipartite graphs.

- An \(\widetilde{O}(nm^{k-1})\)-time algorithm for detecting induced _C_<sub>2_k_</sub> in bipartite graphs.

These algorithms improve the best known upper-bounds for general graphs.

**Keywords: Combinatorial Graph Algorithms** \(\cdot\) Induced Subgraph Detection \(\cdot\) Graph Pattern Polynomials.

### 1 Introduction

We consider the computational problem of finding induced copies of fixed _k_- vertex pattern graphs _G_ in a host graph _G_ with _n_ vertices and _m_ edges given as input. The straight-forward search algorithm for this problem takes _O(n<sup>k</sup>_)- time, which is polynomial-time since we regard _k_ as a constant. Williams [11] showed that even minor improvements to this trivial upper-bound can be used<tbc>

Priyanshi Agrawal and Balagopal Komarath

Indian Institute of Technology, Gandhinagar, India <u>agrawalpriyanshi15@gmail.com</u> <u>bkomarath@rbgo.in</u>

