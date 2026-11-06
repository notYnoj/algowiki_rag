It multiplies two polynomials represented by their coefficient vectors. Its rank is _r+s_-1: evaluation at _r+s_-1 points and interpolation give the upper bound, and the independent output coefficients give the matching matrix-rank lower bound. Decreasing either input length is a restriction. Also

\(C_{ij}(1,s)\cong B_i(s),C_{ij}(r,1)\cong B_j(r).\) (4)

Blocks _T<sub>h</sub>_ are _matched sectors sharing leg i_ when \(T=\sum_hT_h\) and the blocks may share variables on leg _i_, but use pairwise disjoint variables on each other leg. The following constructions hold for every permutation of the legs.

**Lemma 2.1** (Finite separation and polynomial splittings)**.**

1. _If T has M matched sectors sharing leg i, then_<tbc>

\((2M)T\unknown\oplus_{h=1}^M(T_h\otimes B_i(M)).\) \(\text{(5)}\)

_The sectors on the right are independent on all three legs._<tbc>

_2._ _For_ \(r\ge 1\) _and_ \(s\ge 2\), \(C_{ij}(r,s)\otimes B_i(2)\) _degenerates to two matched sectors sharing leg i, namely C<sub>ij</sub>(r,s_+1) _and C<sub>ij</sub>(r,s_-1).<tbc>

_3._ _For_ \(r,s\ge 1\), _C<sub>ij</sub>(r,_3_s+r_-1) _degenerates to three matched sectors sharing leg i: two copies of C<sub>ij</sub>(r,s_) _and one copy of C<sub>ik</sub>(r,s)._

Appendices A and B give the polynomial splittings in coefficient coordinates. Appendix C proves (5) using a finite geometric sum and a nonnegative square. The next construction splits a convolution into repeated independent copies of a smaller convolution.

**Lemma 2.2** (Replicating a convolution)**.** _For all positive integers m,r,s,_

\(C_{ij}(mr,ms)\unknown mC_{ij}(r,s).\) (6)

The construction combines polynomial division with the standard evaluation description of cyclic convolution \[5, Theorem 5 and Section 5.1\]. We give the full proof in Appendix E.

## 3. Tensor characters and counting

To use the preceding constructions, we assign numerical values to tensors using tensor characters. The splittings and separation give concavity and tripling inequalities for their convolution values, which we rescale in the next section. We also identify the three parameters that determine their matrix-multiplication values and state Strassen’s theorem: bounding every character value will give an asymptotic rank bound in Section 6.

A _tensor character_ is a function \(\lambda\) from tensors to nonnegative real numbers satisfying

\(\begin{array}{ c c c }
\lambda(S\oplus T) & = & \lambda(S)+\lambda(T), \\
 &  & S\ge T \Longrightarrow & \lambda(S)\ge\lambda(T).
\end{array}\) (7)

These rules express addition of independent computations, multiplication of tensor factors, and monotonicity under linear substitutions. Matrix rank after grouping one leg against the other two is an example. Keeping one nonzero term and using \(\text{rank}(T)xyz\ge T\) gives \(1\le\lambda(T)\le\text{rank}(T)\) for every nonzero _T_.

