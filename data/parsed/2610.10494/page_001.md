# Rectangular matrix multiplication from polynomial products

**Abstract**

In this note, we extend the matrix-multiplication analysis in [9] to rectangular products and prove

In particular, \(\omega(1,\frac{1}{2},1)=2\) and the dual exponent satisfies \(\alpha\ge\frac{1}{2}\). The proof uses explicit degenerations of convolution tensors, multinomial counting, and Strassen’s spectral theorem. An angular constraint on three dot-product parameters gives both the rectangular curve and a bound for \(\omega(a,b,c)\), with exact exponent _a+b_ whenever \(a\ge b\ge c\ge 0\) and \(c\le\frac{ab}{a+b}\). As an application, Zwick’s algorithm [15] for all-pairs shortest paths in directed unweighted graphs runs in _O(n_<sup>2.5</sup>) time. Combining the rectangular bound with the (min,+)-product improvement of Alman and Vassilevska Williams [1] further gives _O(n_<sup>2.4999</sup>) running time.

### 1. Introduction

Disclaimer. This note, its proofs, analysis and writeup were obtained fully through OpenAI x (GPT-6.1). The author has read and analyzed this note in full and takes full responsibility for its contents, and takes no credit for this work.

The initial motivation for this note was to explore whether the methods of the ground- breaking matrix-multiplication result in [9] could be pushed to analyze rectangular matrix products. We also aim to gather useful bounds and their algorithmic consequences in one place. Rephrasing the proofs in a form accessible to the theoretical computer science community has value in its own right.

### Complexity convention.

Throughout this note, all complexity bounds suppress a +_o_(1) term in the exponent: _O(nc_) denotes _nc+o_(1). All shape parameters are fixed.

Rectangular matrix multiplication is a basic ingredient in algorithms for all-pairs problems, including shortest paths, lowest common ancestors, and Hamming distance. Its exponents depend on the shape of the product; an improvement for square matrices need not give a comparable improvement for every rectangular shape. The analysis in [9] establishes the square bound \(\omega\le 2.25\) using a shared-leg entropy inequality and degenerations of convolution tensors. We extend that analysis to rectangular products by retaining the orientation information lost under full leg symmetrization.

We work over C. The resulting exponent bounds hold over every field of characteristic zero by invariance of asymptotic tensor rank under field extension [10, Theorem 3.10].

Przemysław Uznański

Pathway

`przemek@pathway.com`

October 9, 2026

arXiv:2610.10494v2 [cs.DS] 11 Oct 2026

