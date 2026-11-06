uses _U<sub>h</sub>_. The choice \(\Psi^\sharp=\Psi_H\) costs one extra linear solve on the coarse mesh, but the nonlinear coarse problem is then assembled entirely on T_<sub>H</sub>_. With \(\Psi^\sharp=\Psi_h\) no coarse linear solve is needed, but the integrals \((\rho_\tau(U_h+\Phi_H),v)_{D_s}\) have to be evaluated by quadrature on the fine mesh, since _U<sub>h</sub>_ is piecewise linear on T_<sub>h</sub>_; this costs _O(N<sub>h</sub>_) operations per coarse Newton iteration, but no fine-mesh solve. In both cases the fine-mesh work consists of two linear solves, whereas the scheme of \[34\] needs one fine linear solve for \(\Psi_h\) and one per Newton iteration.

### 5.3 The symmetric 1:1 electrolyte

For a symmetric 1:1 ionic solution, \(\rho(\xi)=\kappa^2\mathrm{sinh}\xi\) with \(\kappa^2=2\beta I_s\), and \(\rho_\tau=\kappa^2\mathrm{sinh}_\tau\), \(\rho'_\tau=\kappa^2\mathrm{cosh}_\tau\) with \(\mathrm{sinh}_\tau,\mathrm{cosh}_\tau\) defined in (22). Here _Z_<sub>max</sub>=1 and \(\tau_0=2M_U\). The coarse and fine problems of Algorithm 1 read: find \(\Phi_H\in V_H^0\) with<tbc>

\(a(\Phi_H,v)+\kappa^2\big(\mathrm{sinh}_\tau(U^\sharp+\Phi_H),v\big)_{D_s}=0\forall v\in V_H^0,\)

<tbc>and find \(\Phi_h^\mathrm{tg}\in V_h^0\) with

\(a(\Phi_h^\mathrm{tg},v)+\kappa^2\big(\mathrm{cosh}_\tau(U_h+\Phi_H)\Phi_h^\mathrm{tg},v\big)_{D_s}\)<br>
\(=\kappa^2\big(\mathrm{cosh}_\tau(U_h+\Phi_H)\Phi_H-\mathrm{sinh}_\tau(U_h+\Phi_H),v\big)_{D_s}\forall v\in V_h^0.\)

Apart from the use of _C_<sup>2</sup> instead of _C_<sup>0</sup> truncations (\(\mathrm{sinh}_\tau,\mathrm{cosh}_\tau\) instead of \(\widetilde{\mathrm{sinh},\mathrm{cosh}}\) in \[34, Eq. (49)\]), the coarse problem is the nonlinear problem solved by the PBE finite element package of \[34\], and the fine problem is one step of its modified Newton scheme \[34, Eq. (40)\] with unit step length, taken on the fine mesh from the coarse solution.

**Corollary 5.6.** _Let n_=2_, Z_<sub>1</sub>=-_Z_<sub>2</sub>=1, \(\bar{c}_1=\bar{c}_2=I_s>0\)_, let Assumptions 2.1 and 4.1 hold with_ \(\hat{g}\) _smooth, and let_ \(\tau\ge 2M_U\)_. Then the conclusions of Theorem 5.2 and Corollary 5.3 hold for the two-grid scheme above. Moreover, the solution_ \(\widehat{\Phi}\) _of_ (15) _satisfies_ \(|\widehat{\Phi}|\le M_U\) _a.e. in_ \(\Omega\)_, so that the dimensionless potential satisfies_ \(\|u\|_{0,\infty,D_s}=\big\|U+\widehat{\Phi}\big\|_{0,\infty,D_s}\le 2M_U\).

_Remark_ 5.7 (a linear initial guess is not needed). Two initial guesses for the Newton minimization are suggested in \[34\]: \(\widehat{\Phi}^{(0)}=0\), or the solution of the linearized problem \(-\epsilon_s\Delta\widehat{\Phi}+\kappa^2\widehat{\Phi}=-\kappa^2U\) in _D<sub>s</sub>_. In the two-grid scheme Newton’s method runs only on the coarse mesh, where iterations are cheap, so the initial guess matters much less; on the fine mesh the starting point is the coarse solution, and by Theorem 5.2 one step is enough. If the nonlinear fine-mesh solution itself is wanted, further Newton steps can be taken on the fine mesh starting from \(\Phi_h^\mathrm{tg}\), cf. the experiments in \[19, 41\].

_Remark_ 5.8 (on the constants). The constants in Theorems 4.6-5.2 depend exponentially on the truncation level through the factor \(e^\tau\) in _C_<sub>0</sub>_,C_<sub>1</sub>_,C_<sub>2</sub> of (21), and on _M<sub>U</sub>_ through (28). Since _M<sub>U</sub>_ is an essential supremum of the potential of the solute in water over the solvent region, including points close to the molecular surface, \(e^{\tau_0}\) may be large for highly charged solutes; this exponential dependence reflects the size of the ionic densities _e_<sup>-_Z<sub>i</sub>u_</sup> near the surface and also appears in \[9, 19\]. The level \(\tau=85\) used in \[34\] to prevent overflow is allowed by the theory but gives larger constants; the convergence rates, in particular the exponents in (65), do not depend on the choice of \(\tau\ge\tau_0\).

## 6 Numerical verification

We test the convergence rates of Sections 4 and 5, the quadratic dependence of the two-grid correction on the coarse error (Lemma 5.1), the choice _H∼h_<sup>2/5</sup>, and Theorem 3.6 on a problem with a<tbc>

