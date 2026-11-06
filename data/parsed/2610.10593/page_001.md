# A faster matrix multiplication algorithm through structured optimization

**Abstract**

We present a new asymptotic matrix multiplication construction yielding \(\omega<2.37115924\), and therefore an algorithm that multiplies two \(n\times n\) matrices in _O(n_<sup>2.37115924</sup>) arithmetic operations over the rationals, reals, or complex numbers. The construction improves the bound 2.371177 of Dupont et al. within the combination-loss framework for the Coppersmith–Winograd tensor. Our approach combines a shared recursive parameter family with a conditioned optimization procedure that addresses two obstacles: weak gradients at low-mass constituents and competing bottlenecks in the retained exponent. A mass- and probability-dependent rescaling supports quasi-Newton optimization in 212820 coordinates, while a six-control correction balances the three extraction roles at each relevant stage. Positive rational entropy-dual factors and an independent ordinary-string verifier turn the resulting construction into an exact certificate. The verified upper-bound expression lies in [2.3711592385931075066123, 2.3711592385931075066124]. The complete witness and an offline verifier using only the Python standard library accompany the paper.

### 1 Introduction

We give a new asymptotic algorithm for matrix multiplication, reducing the exponent bound to 2.37115924. The improvement arises from a specific recursive tensor construction discovered by an optimization procedure tailored to the geometry and bottlenecks of combination-loss analysis. The resulting rational construction is accompanied by an independently implemented exact verifier.

The matrix multiplication exponent \(\omega_\mathbb{Q}\) is the infimum of the real numbers _a_ such that two \(n\times n\) matrices over Q can be multiplied using \(O(n^{a+\varepsilon})\) arithmetic operations for every \(\varepsilon>0\). We write \(\omega=\omega_\mathbb{Q}\) throughout. Since Strassen’s subcubic algorithm [15], successive improvements have relied on algebraic constructions that reduce many matrix products to tensor decompositions. The Coppersmith–Winograd tensor [7], together with the asymptotic sum inequality [13], provides the starting point for the construction studied here.

Combination-loss analysis refines the laser method by retaining additional combinations of tensor constituents. Its recent developments include asymmetric hashing [8], refined bounds for square and rectangular multiplication [18], and the asymmetric framework of Alman et al. [2]. These theorems reduce an upper-bound calculation to a constrained optimization problem involving probability distributions, entropy penalties, and recursively derived matrix dimensions. A feasible parameter choice is sufficient; global optimality is unnecessary.

Dupont et al. [9] formulate this optimization at recursion level four and obtain \(\omega<2.371177\). The central question addressed here is how to obtain a better algorithmic construction from that

Reza Zadeh Matroid, Inc. `reza@matroid.com`

October 6, 2026

arXiv:2610.10593v1 [cs.DS] 6 Oct 2026

