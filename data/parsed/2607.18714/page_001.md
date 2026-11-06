<tbc>ÖOptimal Algorithm for 2-Approximate All Pair Shortest Paths -- almost

**Abstract**

Given an undirected, unweighted graph G, we aim to compute a 2-approximation of all-pairs shortest paths (APSP). This problem admits a natural lower bound of \(\Omega(n^2)\) since the output size is \(\Theta(n^2)\). A central goal in this area is to achieve a running time of O(n<sup>2</sup>).

Dor, Halperin, and Zwick (FOCS 1996, SICOMP 2001) designed an algorithm with a running time<sup>1</sup> of \(\tilde{\mathrm{O}}(n^2)\) that guarantees a 2-approximation only for pairs at a distance of at least O(logn). Recently, Gupta (FOCS 2025) improved this bound, handling all pairs at a distance of at least O(loglogn).

We nearly resolve this problem. We design a randomized algorithm that runs in \(\tilde{\mathrm{O}}(n^2)\) time and, with high probability<sup>2</sup>, guarantees a 2-approximation for all pairs at distance at least c, where \(c\ge 0\) is a constant. Unlike the above two results, which were purely combinatorial, our algorithm combines combinatorial techniques with fast matrix multiplication (FMM).

## 1 Introduction

Let G=(V,E) be an unweighted, undirected graph with n vertices and m edges. Let st denote a shortest path between vertices s and t in G, and let |st| denote its length. Computing all pairs shortest paths in a graph G is a fundamental problem in graph algorithms. For unweighted graphs, a simple combinatorial algorithm computes all pairs shortest paths in O(mn) time. Seidel [Sei95] designed an algorithm that uses fast matrix multiplication (FMM) and solved the problem in \(\tilde{\mathrm{O}}(n^\omega)\) time, where \(n^\omega\) denotes the time required to multiply two \(n\times n\) matrices. Even with the advancements in fast matrix multiplication in [AW24, Gal14, Sto10, Wil12, DWZ23, WXXZ24], this running time remains superquadratic. To achieve near quadratic running time, we must allow approximate solutions.

Let est(s,t) denote the estimate of the shortest path between s and t returned by an algorithm. We say that the algorithm is \((\alpha,\beta)\) approximate, for \(\alpha\ge 1\) and \(\beta\ge 0\), if

\(|\mathrm{st}|\le\mathrm{est}(\mathrm{s},\mathrm{t})\le\alpha|\mathrm{st}|+\beta,\text{for all}\mathrm{s},\mathrm{t}\text{pairs in}\mathrm{G}\)

If \(\beta=0\), we obtain a purely multiplicative approximation and call the algorithm an \(\alpha\) approximate all pairs shortest paths algorithm, or \(\alpha\)-APSP algorithm in short. If \(\alpha=1\), we obtain a purely additive approximation and call the algorithm a +\(\beta\)-APSP algorithm. In this paper, we focus on purely multiplicative, or \(\alpha\)-APSP.

<sup>∗</sup>Research supported by the Anusandhan National Research Foundation (ANRF) through MATRICS grant ANRF/ARGM/2025/001853/MTR. <sup>†</sup>Now at Google, India <sup>1</sup>\(\tilde{\mathrm{O}}\) hides polylogn factors. <sup>2</sup>With probability \(\ge 1-1/n^k\) for a constant k.

Manoj Gupta<sup>∗</sup><br>
IIT Gandhinagar<br>
India<br>
gmanoj@iitgn.ac.in

Mrigankashekhar Shandilya<sup>†</sup><br>
IIT Gandhinagar<br>
India<br>
mrigankashekhar.shandilya@alumni.iitgn.ac.in

arXiv:2607.18714v1 [cs.DS] 21 Jul 2026

