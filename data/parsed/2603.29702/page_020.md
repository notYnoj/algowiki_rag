Now we have

\(\sigma_k=\sum_{s\in[S]}\sum_{(l,r]\in s}\unknown[(l,r]\in I]]\cdot\mathrm{SD}_M(A(l,r],B(l,r])\)<br>
\(=\sum_{s\in[S]}\sum_{(l,r]\in s}\unknown[(l,r]\in I]]\cdot\mathrm{SD}_M(C(l,r],D(l,r])\text{due to (7)}\)<br>
\(=O\left(\sum_{s\in[S]}\sum_{(l,r]\in s}\unknown[(l,r]\in I]]\cdot\frac{1}{2^k}\cdot\mathrm{TD}_M(C(l,r])\right)\text{due to (8)}\)<br>
\(\le O\left(\sum_{s\in[S]}\sum_{(l,r]\in s}\frac{1}{2^k}\cdot\mathrm{TD}_M(C(l,r])\right)\)<br>
\(=O\left(\frac{1}{2^k}\cdot\unknown\mathrm{TD}_{M,S}(C)\right)\text{by definition}\)<br>
\(=O\left(\frac{1}{2^k}\cdot\left(\left(\sum_xc_x\right)S^{0.51}+\mathrm{max}_{x^\prime}\left(c_{x^\prime}\right)\cdot\left(n/2^{\mathrm{log}_M^{0.015}(n)}\right)\right)\right)\text{from Lemma 4.1}\)<br>
\(=O\left(\frac{1}{2^k}\cdot\left(\sum_xc_x\right)S^{0.51}+\frac{1}{2^k}\cdot\mathrm{max}_{x^\prime}\left(c_{x^\prime}\right)\cdot\left(n/2^{\mathrm{log}_M^{0.015}(n)}\right)\right)\)<br>
\(=O\left(\frac{1}{2^k}\cdot\left(\sum_xc_x\right)S^{0.51}+\mathrm{max}_{x^\prime}\left(c_{x^\prime}\right)\cdot\left(n/2^{\mathrm{log}_M^{0.015}(n)}\right)\right)\text{since}\frac{1}{2^k}\le 1\)<br>
\(=O\left(\left(\sum_xd_x\right)S^{0.51}+\mathrm{max}_{x^\prime}\left(c_{x^\prime}\right)\cdot\left(n/2^{\mathrm{log}_M^{0.015}(n)}\right)\right)\text{due to (9)}\)<br>
\(=O\left(\left(\sum_xb_x\right)S^{0.51}+\mathrm{max}_{x^\prime}\left(c_{x^\prime}\right)\cdot\left(n/2^{\mathrm{log}_M^{0.015}(n)}\right)\right)\text{since}b_x\le d_x\)<br>
\(=O\left(\left(\sum_xb_x\right)S^{0.51}+\mathrm{max}_{x^\prime}\left(a_{x^\prime}\right)\cdot\left(n/2^{\mathrm{log}_M^{0.015}(n)}\right)\right).\text{since}c_{x^\prime}\le a_{x^\prime}\)

In an earlier manuscript, we mistakenly thought the lemma would hold without the requirement on the _W_-to-_A_ ratio (without the \(\left(1+\mathrm{log}\left(\frac{1}{\alpha}\right)\right)\) term in the bound). As an anonymous reviewer kindly pointed out, the requirements on the _W_-to-_A_ ratio are necessary, see Section C for further discussion.

## 5 Shortest Path Problems on Grids

### 5.1 Introduction

#### 5.1.1 Grid Graph for LCS and Edit Distance

Given two strings _X,Y_ of length _n<sub>X</sub>_ and _n<sub>Y</sub>_, we define an edge-weighted graph, corresponding to the cost of moving between states in the standard quadratic-time DP algorithm for ED (closely related to the _alignment graph_ defined in e.g., \[CKW23\]):

