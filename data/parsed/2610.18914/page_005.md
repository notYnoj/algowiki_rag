Third, the three-sector construction in its Lemma 4.2 only uses coordinate restrictions, basis permutations, and integer weights of a degeneration parameter. It does not divide by 3: the uniform probability vector and its entropy are real numbers used to compare character values. Finally, the detecting-character proof in its Appendix A uses the ordered tensor semiring, flattening ranks, finite-dimensional real separation, compactness, and a fixed-point theorem. Every nonzero tensor still restricts to a scalar tensor over an arbitrary field, and all semiring and rank comparisons used there remain valid. The separation and fixed-point arguments concern real-valued states, not the characteristic of the tensor field.

These observations justify using Sections 4 and 5 and Appendix A of the cited paper over an algebraically closed field _F_ of any characteristic, with Proposition 2.1 in place of its Proposition 3.1. For clarity, the resulting chain of inequalities is as follows. Put<tbc>

\(t=(p_X+p_Y+p_Z)/3>0,C(a,b)=\sum_{i=0}^{a-1}\sum_{j=0}^{b-1}x_iy_jz_{i+j},\)

<tbc>and use the original symmetrized profile<tbc>

\(P(a,b)=\left(\prod_{\pi\in S_3}\lambda_\pi(C(a,b))\right)^{1/(6t)}.\)

<tbc>Its concavity and shifted tripling follow from the two constructions just checked and (3.3). The real argument of Lemma 5.1 then gives

\(a^{4/3}\le P(a,a)\le(2a-1)^{1/t}.\)

Consequently \(t\le 3/4\), and every character satisfies \(\lambda(T_d)\le d^{9/4}\) for the matrix multiplication tensor \(T_d=\sum_{i,j,k=1}^dx_{ij}y_{jk}z_{ki}\).

Write \(\nu=inf_{d\ge 2}log_dR(T_d)\), again as in the cited paper. Its detecting-character lemma, applied with \(k=\lceil d^\nu\rceil-1\), yields

\(d^\nu\le d^{9/4}+1.\)

Letting \(d\rightarrow\infty\) gives \(\nu\le 9/4\). The recursive bilinear-algorithm argument in its proof of Theorem 1.1 therefore gives \(\omega_F\le 9/4\).

**Corollary 4.1.** _For every algebraically closed field K, the matrix multiplication exponent satisfies_ \(\omega_K\le 9/4\)_. In particular, the bound holds in all but finitely many characteristics; in fact no characteristic needs to be excluded._

## Acknowledgements

I would like to thank GPT 6.1 Sol (OpenAI) and Deepseek V4.1 Flash (Deepseek) for completing a gap in an earlier proof, checking the validity of my proof and generating the format of this paper.

## References

