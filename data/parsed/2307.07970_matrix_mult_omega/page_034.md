the same bucket _b_ as _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_ is \(\frac{1}{M}\) by Claim 5.5. Thus, by the union bound, the probability that any of them is mapped to the same bucket as _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_ is upper bounded by \(\frac{N_\alpha}{N_\mathrm{BZ}}\cdot p_\mathrm{comp}\cdot\frac{1}{M}\le\frac{N_\alpha\cdot p_\mathrm{comp}}{N_\mathrm{BZ}\cdot M_0}\). Furthermore, if none of them are mapped to the same bucket as _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_, then \(Z_\hat{K}\) is compatible with a unique triple _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_ in T<sub>comp</sub>, so the claim follows.

Recall that we require _M_<sub>0</sub> to be at least \(8\cdot\mathrm{max}\big\{\frac{N_{\alpha_X,\alpha_Y,\alpha_Z}}{N_\mathrm{BX}},\frac{N_{\alpha_X,\alpha_Y,\alpha_Z}}{N_\mathrm{BY}}\big\}\). Now, we add another (and final) constraint: \(M_0\ge\frac{N_\alpha\cdot p_\mathrm{comp}}{N_\mathrm{BZ}}\cdot 80N\). That is, we will set _M_<sub>0</sub> to be

\(\mathrm{max}\big\{\frac{8N_{\alpha_X,\alpha_Y,\alpha_Z}}{N_\mathrm{BX}},\frac{8N_{\alpha_X,\alpha_Y,\alpha_Z}}{N_\mathrm{BY}},\frac{N_\alpha\cdot p_\mathrm{comp}}{N_\mathrm{BZ}}\cdot 80N\big\}\)<br>
\(=2^{\mathrm{max}\{H(\alpha)-P_\alpha-H(\alpha_X),H(\alpha)-P_\alpha-H(\alpha_Y),H(\alpha)+\lambda_Z-H(\overline{\beta_{Z,*,*,*}})\}\cdot A_1\cdot n\pm o(n)}.\)

Now, for every \(b\in B\) and every level-\(\ell\) block triple _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_ that is consistent with \(\alpha\) with _h<sub>X</sub>(I_)=_h<sub>Y</sub>(J_)=_h<sub>Z</sub>(K_)=_b_,

1. by Claim 5.6, it remains in T<sub>hash</sub> with probability \(\ge\frac{3}{4}\);<tbc>

2. by Claim 5.16, linearity of expectation and Markov’s inequality, among \(Z_\hat{K}\in Z_K\) that is useful for _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_ (this implies that \(Z_\hat{K}\) is typical, so we could apply Claim 5.16), the fraction of \(Z_\hat{K}\) that becomes a hole in T<sub>useful</sub> is at most \(10/80N=\frac{1}{8N}\) with probability at least 9/10.

Therefore, by the union bound, with constant probability, the subtensor of T<sub>useful</sub> over _X<sub>I</sub>,Y<sub>J</sub>,Z<sub>K</sub>_ is a copy of T<sup>∗</sup> whose fraction of holes does not exceed 1/8_N_. The expected number of _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_ with _h<sub>X</sub>(I_)=_h<sub>Y</sub>(J_)=_h<sub>Z</sub>(K_)=_b_ over all \(b\in B\) is \(N_\alpha\cdot M^{-1-o(1)}\), so overall, T<sub>useful</sub> contains \(N_\alpha\cdot M^{-1-o(1)}\) copies of T<sup>∗</sup> whose fraction of holes is 1/8_N_.

By Corollary 4.2, we can degenerate them into \(N_\alpha\cdot M^{-1-o(1)}\) unbroken copies of T<sup>∗</sup>.

## 5.7 Summary

So far, we have degenerated \(\left(\mathrm{CW}_q^{\otimes 2^{\ell-1}}\right)^{\otimes A_1\cdot n}\) into \(\ge N_\alpha\cdot M_0^{-1-o(1)}\) copies of a level-\(\ell\) interface tensor T<sup>∗</sup> with parameter list<tbc>

\(\big\{\left(n\cdot A_1\cdot\alpha^{(1)}(i,j,k),i,j,k,\beta_{X,i,j,k}^{(1)},\beta_{Y,i,j,k}^{(1)},\beta_{Z,i,j,k}^{(1)}\right)\big\}_{i+j+k=2^\ell}.\)

<tbc>By plugging in the bounds of \(N_\alpha\) and _M_<sub>0</sub>, we see that the number of copies we obtained (in the first region) is

\(2^{A_1n\cdot\mathrm{min}\big\{H(\alpha_X^{(1)})-P_\alpha^{(1)},H(\alpha_Y^{(1)})-P_\alpha^{(1)},H(\overline{\beta_{Z,*,*,*}^{(1)}})-\lambda_Z^{(1)}\big\}-o(n)}.\)

By symmetry, we can apply the same method to the second and third region, where for the second region we perform asymmetric hashing that shares _Y_ -variable blocks, and for the third region we perform asymmetric hashing that shares _X_-blocks. Taking the tensor product of these results returned by our method on the three regions concludes the proof.

