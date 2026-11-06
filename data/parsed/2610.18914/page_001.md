Polynomial Separation of a Shared Tensor Leg and Matrix Multiplication in Arbitrary Characteristic

Houxi Lü

October 9, 2026

**Abstract**

We improve the shared-leg separation construction in Proposition 3.1 of OpenAI, _An Upper Bound of_ 9/4 _for the Matrix Multiplication Exponent_ (October 2, 2026). If _M_ tensor blocks have a common first space and independent matched sectors on their other two spaces, then _M+n_-1 copies of their matched sum degenerate to the full direct sum of the blocks, each tensored with an _n_-dimensional dot product. For _n=M_, this reduces the number of source copies from 5_M_ to 2_M_-1. The construction uses polynomial interpolation and truncated local substitution, with no roots of unity or factorial denominators. It works over every field containing enough distinct elements. We verify that the remaining spectral and discrete-growth arguments of the cited preprint are independent of characteristic. Over an algebraic closure, the replacement therefore gives \(\omega\le 9/4\) in every characteristic.

## 1 The replacement and its setting

The separation problem is to make each block read its own copy of a shared input. In Proposition 3.1 of OpenAI [1], this is done by Fourier projection followed by a weight degeneration. We use evaluation of polynomials instead. Evaluation at _M_ distinct points gives _M_ independent input coordinates; a local substitution allows us to approach this evaluation map through restrictions of ordinary polynomial multiplication.

We follow the notation of the cited paper: \(A=\sum_hA_h\) denotes a matched sum, \(A\ge B\) means that _B_ is a restriction of _A_, \(\otimes\) denotes tensor product, and \(A^{\oplus r}\) denotes a full direct sum of _r_ copies. An integer _r_ also denotes the direct sum of _r_ scalar tensors, so \(A\otimes r\cong A^{\oplus r}\). All spaces are finite-dimensional over a algebraically closed field _F_. Tensors are viewed as trilinear forms, and a restriction pulls a form back along a linear map on each of its three spaces.

We use \(\unknown\) for an algebraic degeneration: the three pullback maps may have entries in \(F[\varepsilon,\varepsilon^{-1}]\), provided that the resulting form is polynomial in \(\varepsilon\); its value at \(\varepsilon=0\) is the target tensor. This extends the fixed-substitution, monomial-weight convention of Section 2.2 of the cited paper. Its interpolation argument still applies. Indeed, if the resulting polynomial family has degree _L_ and constant term _B_, interpolation of its _j_th tensor power at _jL_+1 distinct nonzero points gives

\((jL+1)\lambda(A)^j\ge\lambda(B)^j.\)

Over an infinite field, taking _j_th roots proves degeneration monotonicity for every tensor character \(\lambda\).

arXiv:2610.18914v1 [cs.CC] 12 Oct 2026

