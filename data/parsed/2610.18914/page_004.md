## 3 The spectral comparison

Let _F_ now be infinite, and let \(\lambda\) be a tensor character in the sense of Section 2 of the cited paper: it is normalized, restriction-monotone, additive on full direct sums, and multiplicative on tensor products. Write \(\lambda(B_X(n))=n^{p_X}\), with \(p_X\in[0,1]\), as in its Section 2.1. Proposition 2.1 and interpolation monotonicity give

\((M+n-1)\lambda(A)\ge n^{p_X}\sum_h\lambda(A_h).\) (3.1)

Taking _n=M_ yields

\((2M-1)\lambda(A)\ge M^{p_X}\sum_h\lambda(A_h).\) (3.2)

This replaces the factor 5_M_ in Proposition 3.1 of the cited paper.

The proof of its Corollary 3.2 now goes through with this new factor. To see precisely what changes, let \(T=\sum_iT_i\) be a matched sum and let _q_ be a rational probability vector. In \(T^{\otimes N}\) retain only sector words containing _Nq<sub>i</sub>_ copies of label _i_. There are<tbc>

\(M_N=\frac{N!}{\prod_i(Nq_i)!}\)

<tbc>blocks, each of character value \(\prod_i\lambda(T_i)^{Nq_i}\). Equation (3.2) gives<tbc>

\(\lambda(T)\ge\left(\frac{M_N}{2M_N-1}\right)^{1/N}M_N^{p_X/N}\prod_i\lambda(T_i)^{q_i}.\)

<tbc>The first factor tends to 1, while log_M<sub>N</sub>/N_ tends to the entropy \(H(q)=-\sum_iq_ilogq_i\). By continuity in _q_, we recover exactly the original shared-leg inequality

\(\lambda(T)\ge e^{p_XH(q)}\prod_i\lambda(T_i)^{q_i}.\) (3.3)

The factorials here count words as integers; they are not inverted in _F_. The improved finite copy count therefore preserves the entropy exponent. By itself it does not give a strict improvement below 9/4.

## 4 The consequence in positive characteristic

The new separation argument works over every infinite field. To apply the remainder of the cited paper in positive characteristic, we need to check its other field-dependent steps. We record these checks rather than repeat its proofs.

First, the rank bound for polynomial multiplication follows from interpolation at distinct points, which is valid over any infinite field. Second, the determinant filtration in its Lemma 4.1 uses

\(0\longrightarrow(uw-vs)V_{e-1}\longrightarrow V_e\otimes span(s,w)\longrightarrow V_{e+1}\longrightarrow 0.\)

Here _V<sub>e</sub>_ is the space of homogeneous degree-_e_ forms in _u,v_, and the last map substitutes (_s,w_)=(_u,v_). It is surjective on monomials. Multiplication by _uw-vs_ is injective, and its image has the dimension of the kernel. These facts hold in every characteristic, including 2. Multiplication by a first input preserves this kernel, so the block degeneration in that lemma also holds without a characteristic assumption.

