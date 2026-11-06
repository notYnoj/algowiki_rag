A simplified proof of polynomial improvements for 3SUM and APSP

**Abstract**

We give a simplified proof of the polynomial improvements for integer 3SUM and all-pairs shortest paths (APSP) established by Alman and Vassilevska Williams, with weaker exponents. The central ingredient is selected-entry matrix multiplication: computing a prescribed set of entries of a product of dense rectangular matrices. Starting from Schönhage’s inner/outer- product identity, we construct a multiplication rule that shares intermediate products among many outputs. We apply this rule recursively and bound the work by counting the requested entries at each level.

Applied to incidence matrices, the algorithm solves Offline Set Disjointness over a small universe. Known deterministic reductions then yield truly subquadratic integer 3SUM and truly subcubic APSP for polynomially bounded integer inputs.

## 1 Introduction

Alman and Vassilevska Williams [1] established the first truly subquadratic algorithms for integer 3SUM and truly subcubic algorithms for all-pairs shortest paths with polynomially bounded integer inputs. Their main innovation is a matrix multiplication algorithm that exploits sparsity in the set of requested outputs, even when the input matrices are dense. We give a simplified proof of these qualitative improvements, with weaker exponents.

We focus on the matrix multiplication argument. To obtain the 3SUM and APSP consequences, we first apply it to Offline Set Disjointness, where matrix entries directly encode intersection sizes. We then use existing deterministic reductions from 3SUM and APSP to this problem as black boxes.

Selected-entry matrix multiplication. Let _X_ be an \(n\times d\) matrix and _Y_ a \(d\times m\) matrix. Each entry of _XY_ is a dot product of a row of _X_ and a column of _Y_ . We call the task of computing _w_ specified entries of _XY selected-entry matrix multiplication_. Computing these entries as separate dot products uses _wd_ multiplications, while writing down the full product takes \(\Omega(nm)\) time. When the middle dimension _d_ and the number of requested entries _w_ are small enough, sharing intermediate computations gives the following bound.

**Theorem 1.1** (Selected-entry matrix multiplication)**.** _For every fixed_ \(\tau\in(0,1]\)_, there is an integer_ \(\kappa=\kappa(\tau)=O(\tau^{-2})\) _with the following property. Let_ \(d^\kappa\le min\{n,m\}\)_. Given integer matrices_ \(X\in\mathbb{Z}^{n\times d}\) _and_ \(Y\in\mathbb{Z}^{d\times m}\)_, with entries of polynomial magnitude in n+m, and_ \(w\ge 1\) _distinct specified positions in XY, those entries can be computed deterministically in time_

\(\widetilde{O}((n+m)d^\kappa+d^\tau\sqrt{nmw}).\) (1)

<sup>∗</sup>Supported by Simons Investigator Award #929894 and NSF award CCF-2425349.

Sankeerth Rao Karingula Agentin AI <u>sankeerthrao@agentin.ai</u>

Shachar Lovett<sup>∗</sup> University of California, San Diego <u>slovett@ucsd.edu</u>

October 14, 2026

arXiv:2610.15663v1 [cs.CC] 11 Oct 2026

