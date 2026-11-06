\(=\mathrm{min}_{P\in\mathbb{C}^{n\times n_c}}\mathrm{min}_{R\in\mathbb{C}^{n\times n_c}}\mathrm{sup}_{x\in Mx\neq 0M=\mathcal{N}(R^HA)}\frac{x^H\mathcal{A}^{\nu_2}x}{x^H\mathcal{C}^{\nu_1}x}\)<br>
\(=\mathrm{min}_{P\in\mathbb{C}^{n\times n_c}}\mathrm{min}_{M\subseteq\mathbb{C}^n\mathrm{dim}(M)=n-n_c}\mathrm{sup}_{x\in Mx\neq 0}\frac{x^H\mathcal{A}^{\nu_2}x}{x^H\mathcal{C}^{\nu_1}x}\)<br>
\(=\mathrm{min}_{P\in\mathbb{C}^{n\times n_c}}(1-\mu_{n_c+1})^{\nu_1+\nu_2}=(1-\mu_{n_c+1})^{\nu_1+\nu_2}.\)

Due to Theorem 4.1 we know that this bound is attained for the pairs \((\hat{P},\hat{R})\), \((P_*,\hat{R})\) and \((\hat{P},R_*)\). □

For \((\nu_1,\nu_2)=(1,0)\) this result was already proven in \[2, Theorem 4.5, 4.6\].

_Remark_ 4.5. \((\hat{P},\hat{R})\), \((P_*,\hat{R})\) and \((\hat{P},R_*)\) are not the only combinations of interpolation and restriction that minimize the _B_-norm of \(E_+^{\nu_1,\nu_2}\). In fact, any pair (_P,R_) with \(\mathcal{R}(P)=\mathcal{R}(\hat{P})\) and \(\mathcal{R}(R)=\mathcal{R}(\hat{R})\) minimizes the _B_-norm of the operator \(E_+^{\nu_1,\nu_2}\). This means that the optimal compatible transfer operators are unique up to a change of basis.

The operator \(E_+^{\nu_1,\nu_2}\) for \((\nu_1,\nu_2)\in\{(0,1),(1,0),(1,1)\}\) provides a natural generalization of the HPD error operator \(E_\mathrm{HPD}^{\nu_1,\nu_2}\) and gives a convergent two-grid methods under fairly easy assumptions. However, from an application-oriented point of view, computing the post-smoother (_M_<sup>-1</sup>_A_)<sup>+</sup>=_B_<sup>-1</sup>_A<sup>H</sup>M_<sup>-_H_</sup>_B_ seems infeasible due to the inverse of _B_. But for special cases of _B_, the post-smoother can still be computed. For more details about the computation of _P_<sub>∗</sub> in these cases, see \[2\].

In the following we list some special choices for _B_. For the classic HPD case, that is _B=A_ HPD, it holds

\((M^{-1}A)^+=A^{-1}A^HM^{-HA}=M^{-HA}\)

which yields the error propagation operator \(E_\mathrm{HPD}^{\nu_1,\nu_2}(P,P)\) when choosing _R=P_. In this case, Theorem 4.4 reduces to the known result \[38, Theorem 5.7\].

For _B=I<sub>n</sub>_ we get

\((M^{-1}A)^+=(M^{-1}A)^H=A^HM^{-H}\)

which can be computed easily. Moreover, we have

\(\widehat{M^{-1}}=M^{-1}A+A^HM^{-H}-M^{-1}AA^HM^{-H}.\)

For _B=A<sup>H</sup>A_ we get

\((M^{-1}A)^+=A^{-1}A^{-HA}^HM^{-HA}A=A^{-1}M^{-HA}^HA=A^{-1}M^{-HB}\)

but this smoother contains _A_<sup>-1</sup> which is also infeasible. However, if we choose additionally _M_<sup>-1</sup>=_AA<sup>H</sup>_ we obtain

\((M^{-1}A)^+=A^HB\)

The operator _R_<sub>∗</sub> that produces a _B_-orthogonal coarse-grid correction can be easily determined as _R_<sub>∗</sub>=_A_<sup>-_H_</sup>_BP=AP_ given some interpolation operator _P_.

The case _B=M_ HPD was also investigated in \[39\]. Here, we have

\((M^{-1}A)^+=M^{-1}A^HM^{-HM}=M^{-1}A^H\)

