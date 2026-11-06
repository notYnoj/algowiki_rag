approximates. This is a real concern for our scheme: the freezing of the coefficients (Section 3) makes the equations linear, but it could have cost us the energy law. The discrete energy might then decrease only approximately, with an error that grows with \(\Delta t\), or it might decrease only for sufficiently small \(\Delta t\).

The scheme (S1)-(S4) satisfies an exact discrete analogue of Proposition 2.1, with no approximation and no restriction on \(\Delta t\). Specifically, we construct a discrete energy E_<sup>n</sup>_ and a discrete dissipation \(\widetilde{\mathcal{D}}^{n+1}\), which have the same completed-square structure as the continuous dissipation D. They satisfy

\(\mathcal{E}^{n+1}-\mathcal{E}^n=-\Delta t\widetilde{\mathcal{D}}^{n+1}-R^{n+1},\)

where \(R^{n+1}\ge 0\) is an explicit non-negative remainder. This holds exactly, for every \(\Delta t>0\). We call a scheme unconditionally energy stable in this sense: the modified energy decreases at every step, by construction, for any step size, and not only once \(\Delta t\) is sufficiently small.

Since BDF2 is a two-step method, the discrete energy E_<sup>n</sup>_ depends on two consecutive time levels, through the quadratic form \(\Phi\) (Section 3.1). The result relies on the coefficient freezing of Section 3. Because all coefficients in (S1)-(S4) are evaluated at the same extrapolated state, the discrete calculation parallels the continuous proof of Proposition 2.1 step by step, and no additional error terms need to be controlled.

**Theorem 4.1** (Discrete energy-dissipation identity)**.** _Assume d_<sub>0</sub>_\>_0 _constant,_ \(\varepsilon_q\ge 0\), \(\kappa_\star\ge 0\) _pointwise (i.e. at every point_ \(x\in\Omega\)_, not merely on average), Assumption 1, and a spatial discretisation with exact discrete integration by parts under which_ \(\nabla D_2=D_2\nabla\) _(differentiating in space and then applying the BDF2 time-difference operator gives the same result as doing these two steps in the opposite order) and the frozen-coefficient products entering_ (4) _are evaluated and integrated exactly at each degree of freedom, that is, computing a product such as_ \(b_\star|\nabla\mu^{n+1}|^2\) _pointwise at the grid points (or retained Fourier modes) and then summing it discretely gives exactly the same number the continuous integral would, with no quadrature or aliasing error. This holds for the periodic Fourier-Galerkin discretisation without dealiasing used below. With_ \(\Phi(u,v):=\|u\|^2+\|2u-v\|^2\),

\(\mathcal{E}^n:=\frac{1}{4}\big[\gamma\Phi(\nabla\phi^n,\nabla\phi^{n-1})+\Phi(q^n,q^{n-1})+2\Phi(r^n,r^{n-1})\big]-C_0,\) (10)

\(\widetilde{\mathcal{D}}^{n+1}:=\int_\Omega\big(b_\star-\frac{c_\star^2}{d_0}\big)|\nabla\mu^{n+1}|^2+\frac{1}{d_0}\int_\Omega\big|c_\star\nabla\mu^{n+1}-d_0\nabla(A_\star q^{n+1})\big|^2\)<br>
\(+\big(\kappa_\star q^{n+1},q^{n+1}\big)+\varepsilon_q\|\nabla q^{n+1}\|^2(\ge 0),\) (11)

_solutions of (S1)-(S4) satisfy, for_ every \(\Delta t>0\),

\(\mathcal{E}^{n+1}-\mathcal{E}^n+\frac{1}{4}\big[\gamma\|\nabla D^2\phi^{n+1}\|^2+\|D^2q^{n+1}\|^2+2\left(D^2r^{n+1}\right)^2\big]+\Delta t\widetilde{\mathcal{D}}^{n+1}=0.\) (12)

_Proof._ Testing (S2) with \(D_2\phi^{n+1}\) and (S1) with \(\mu^{n+1}\) gives two expressions for the same pairing \(\big(\mu^{n+1}\), \(D_2\phi^{n+1}\big)\); equating them, and using (S4) to replace \(r^{n+1}\big(G_\star\), \(D_2\phi^{n+1}\big)\) by 2_r_<sup>_n_+1</sup>_D_<sub>2</sub>_r_<sup>_n_+1</sup>, isolates the frozen-coefficient terms on one side. Adding the result of testing (S3) with _q_<sup>_n_+1</sup>, the two cross terms combine (add, as in Proposition 2.1’s proof, because \(b_\star,c_\star,A_\star,\kappa_\star\) are all evaluated at the same \(\phi_b^\star\)), and (4) converts them into exactly \(-\widetilde{\mathcal{D}}^{n+1}\), with no \(\|\phi^{n+1}-\phi^\star\|\) remainder, since the frozen coefficients carry no \(\phi^{n+1}\)-dependence. The G-stability concept is due to Dahlquist \[22\]; the specific multiplier identity used here, for BDF2, is due to Nevanlinna and Odeh \[23\]:

\(\big(3a^{n+1}-4a^n+a^{n-1},a^{n+1}\big)=\frac{1}{2}\big[\Phi(a^{n+1},a^n)-\Phi(a^n,a^{n-1})\big]+\frac{1}{2}\|a^{n+1}-2a^n+a^{n-1}\|^2,\) (13)

applied to \(a=\nabla\phi,q,r\), then turns the left-hand side into the telescoping difference E<sup>_n_+1</sup>-E_<sup>n</sup>_ plus the stated non-negative remainder, giving (12). Non-negativity of \(\widetilde{\mathcal{D}}^{n+1}\) follows from Assumption 1, \(\kappa_\star\ge 0\), \(\varepsilon_q\ge 0\). Full proof in Appendix A.

