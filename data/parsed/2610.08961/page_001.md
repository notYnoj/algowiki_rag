Analysis of the two-for-one swap heuristic for approximating the maximum independent set in a _k_-polymatroid<sup>∗</sup>

**Abstract**

Let \(f:2^N\rightarrow\mathbb{Z}_{\ge 0}\) be a polymatroid (an integer-valued non-decreasing submodular set function with \(f(\emptyset)=0\)). A _k_-polymatroid satisfies that \(f(e)\le k\) for all \(e\in N\). We call \(S\subseteq N\) _independent_ if \(f(S)=\sum_{e\in S}f(e)\) and _f(e)\>_0 for all \(e\in S\). Such a set was also called a _matching_. Finding a maximum-size independent set in a 2-polymatroid has been studied and polynomial-time algorithms are known for linearly represented polymatroids. For \(k\ge 3\), the problem is NP-hard, and a \(((2/k)-\epsilon)\)-approximation is known and is obtained by swapping as long as possible a subset of up to \((1/\epsilon)^{log_{k-1}(2k+1)}\) elements from the current solution by a set with one more element.

Here we give a simple analysis of the more particular two-for-one repeated swapping heuristic, obtaining a tight (weaker) (2/(_k_+1))-approximation.

**Keywords:** Approximation Algorithm; Matroid; Local Optimization. **2000 MSC:** 05B35; 05B40; 68W05; 68W25; 68W40; 68R05; 90C27.

## 1 Introduction

A polymatroid \(f:2^N\rightarrow\mathbb{Z}_{\ge 0}\) on a ground set _N_ is a non-decreasing (monotone) integer-valued submodular function with \(f(\emptyset)=0\). A function _f_ is monotone iff \(f(A)\le f(B)\) for all \(A\subseteq B\). A function _f_ is submodular iff \(f(A)+f(B)\ge f(A\cup B)+f(A\cap B)\) for all _A_, \(B\subseteq N\).<sup>1</sup> Polymatroids generalize matroids which have the additional condition that \(f(\{i\})\le 1\) for all \(i\in N\).

<sup>∗</sup>Minor corrections from the version published in Operations Research Letters <sup>†</sup>The Research Institute of the University of Bucharest. Work performed while at Illinois Institute of Technology. Email: gcali9999@gmail.com <sup>‡</sup>Work performed while at University of Illinois. Email: adriancyay@gmail.com <sup>1</sup>Equivalently, a monotone function _f_ is submodular if for any \(S\subseteq T\subseteq N\), we have \(\sum_{i\in T\backslash S}(f(S\cup\{i\})-f(S))\ge f(T)-f(S)\). [35, Proposition 7]

arXiv:2610.08961v1 [cs.DS] 6 Oct 2026

Gruia Călinescu<sup>†</sup>

Adrian Calinescu<sup>‡</sup>

