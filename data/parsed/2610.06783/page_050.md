## 5 Further reductions

This section presents the remaining algorithmic results of the introduction: directed unweighted APSP (Section 5.1), the real-valued versions of 3SUM, APSP, and Exact Triangle (Section 5.2), the weighted _k_-Clique problems (Section 5.3), and the refutation of the rectangular hinted OMv conjectures of van den Brand, Nanongkai, and Saranurak \[vdBNS19\] (Section 5.4). Each result but the last composes a known reduction with the algorithms of Sections 3 and 4; the last applies the data structure of Section 4 directly. We cite the reduction we use in each case and modify it only where our parameter regime requires it, saying what changes.

### What we use.

We recall the three results of Sections 3 and 4 that the reductions plug into.

• _Exact Triangle_ (Section 3.2) asks whether a complete tripartite graph with parts _A,B,C_ of _n_ vertices and integer edge weights of absolute value at most \(n^\nu\) has a triangle of weight zero. Theorem 19 solves it deterministically in \(O(n^{3-\varepsilon^\prime} logn)\le O(n^{3-\varepsilon_T})\) time, where \(\varepsilon'=0.00175\) and \(\varepsilon_T=0.0017\), and Theorem 22 derives from this a deterministic \(\tilde{O}(n^{3-\varepsilon^\prime/3})\)-time algorithm for the (min,+)-product of two \(n\times n\) matrices with integer entries of absolute value _n_<sup>_O_(1)</sup>.<tbc>

• Lop-AE-SparseTri(_n,D_) and #Lop-AE-SparseTri(_n,D_) (Definitions 13 and 14) are given a tripartite graph with parts _A_ and _B_ of _n_ vertices and a middle part of at most _D_ vertices, together with a set _W_ of _query pairs_ \((a,b)\in A\times B\), and ask for every query pair in _W_ whether _a_ and _b_ have a common neighbor in the middle part, or for the counting version, how many they have. Corollary 16 solves both deterministically in _O_(|_W|D_<sup>0.437</sup>+_n_<sup>2</sup>_/D_<sup>0.063</sup>) time when \(n\ge D^{18}\). Theorem 17 reduces Exact Triangle to Lop-AE-SparseTri deterministically by hashing the weights modulo a prime.<tbc>

• Corollary 26 is the data structure behind Corollary 16. Given \(X\in\mathbb{Z}^{N\times D}\) and \(Y\in\mathbb{Z}^{D\times N}\) with \(N\ge D^{18}\) and entries of absolute value _N_<sup>_O_(1)</sup>, it preprocesses them deterministically in _O(N_<sup>2</sup>_/D_<sup>0.063</sup>) time, after which it computes any entry of _XY_ in _O(D_<sup>0.437</sup>) time. Section 5.2 applies it to matrices whose entries are not 0/1, and Section 5.4 uses its queries online.

The algorithms of Sections 5.1, 5.3, and 5.4 are deterministic. Those of Section 5.2 are randomized (Las Vegas), because the reductions of \[CVX22\] that they use as black boxes are randomized.

### 5.1 Directed APSP with small integer weights

Let \(\omega(1,r,1)\) denote the exponent of multiplying an \(n\times n^r\) matrix by an \(n^r\times n\) matrix, and let \(\mu\) be the solution of \(\omega(1,\mu,1)=1+2\mu\). Then \(\mu\ge\frac{1}{2}\), since \(\omega(1,\mu,1)\ge 2\), and \(\mu<0.5275\) by the bounds of \[ADV<sup>+</sup>25\]. Zwick’s algorithm \[Zwi02\] solves APSP in directed unweighted graphs in \(\tilde{O}(n^{2+\mu})\) time, and the Directed Unweighted APSP hypothesis \[CVX21, CVX23, Fis26\] asserts that no algorithm is polynomially faster. We refute this in Theorem 34.

We revisit Theorem 3.1 of Chan, Vassilevska Williams, and Xu \[CVX21\], which is just a presentation of Zwick’s algorithm \[Zwi02\] as a reduction. Zwick’s algorithm is typically used in its randomized form because the proof is simple, so the reduction in \[CVX21\] was stated in its randomized form. However, following an argument by Yuster and Zwick \[YZ05a, Section 8\], the reduction has a deterministic version as well:

