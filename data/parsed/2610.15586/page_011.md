## 4.7 Approximation hierarchy

A realization on hardware requires approximations. We divide them into two classes.

### Class I: approximations of the operator.

These replace _A_ by a nearby matrix \(\tilde{A}\). Examples are the error of a numerical conformal map, the truncation of an infinite coordinate strip, the neglect of higher orders in the curvature, and the penalization of a domain on a bounding box. They change the solution that the algorithm computes.

**Proposition 15** (Metric perturbation)**.** _Let_ \(\tilde{A}=A+\delta A\) _with_ \(|\langle v,\delta Av\rangle|\le\epsilon\langle v,Av\rangle\) _for all v and some_ \(\epsilon<1\)_, and let_ \(\tilde{b}=b+\delta b\) _and_ \(\tilde{x}=\tilde{A}^{-1}\tilde{b}\)_. Then_

\(\frac{\|\tilde{x}-x^*\|_A}{\|x^*\|_A}\le\frac{\epsilon+\|\delta b\|_{A^{-1}}/\|x^*\|_A}{1-\epsilon}.\) (22)

_In particular, a relative error_ \(|\delta\big(\sqrt{g}\big)|\le\epsilon\sqrt{g}\) _of the metric factor in C, or_ \(|\delta\rho|\le\epsilon\rho\) _in K, satisfies the assumption on_ \(\delta A\).

_Proof._ Let \(\mathscr{E}=A^{-1/2}\delta AA^{-1/2}\), so that \(\|\mathscr{E}\|\le\epsilon\). Since \(\tilde{x}-x^*=-\tilde{A}^{-1}\delta Ax^*+\tilde{A}^{-1}\delta b\), we obtain \(A^{1/2}(\tilde{x}-x^*)=-(I+\mathscr{E})^{-1}\mathscr{E}A^{1/2}x^*+(I+\mathscr{E})^{-1}A^{-1/2}\delta b\). Hence \(\|\tilde{x}-x^*\|_A\le(1-\epsilon)^{-1}(\epsilon\|x^*\|_A+\|\delta b\|_{A^{-1}})\). The second statement follows because \(0\unknown C\unknown A\) and \(0\unknown K\unknown A\).

Geometric uncertainty, such as an error in the segmented wall of a vessel, is a Class I approximation of a particular kind. We describe it by a vector field _V_ that deforms the cross section. Its flow \(\psi_s\) maps the reference cross section to the deformed one. By pulling the problem back to the reference coordinates, we keep the grid and the basis _F_ and change only the metric, \(g\rightarrow\psi_s^*g=g+s\mathscr{L}_Vg+O(s^2)\).

**Proposition 16** (First-order shape perturbation)**.** _In two dimensions, let_ \(\mu_1\ge\mu_2\) _be the eigenvalues of g_<sup>-1</sup>L_<sub>V</sub>g at each point. To first order in s, the deformation changes the coefficients of Eq._ (19) _by_

\(\delta\big(\sqrt{g}g^{ij}\big)=-s\sqrt{g}\big(\mathscr{L}_Vg\big)_\circ^{ij},\delta\sqrt{g}=s\sqrt{g}\mathrm{div}_gV,\) (23)

_where_ \((\mathscr{L}_Vg)_\circ=\mathscr{L}_Vg-(\mathrm{div}_gV)g\) _is the trace-free part and indices are raised with g. Hence Proposition 15 applies, to first order, with_

\(\epsilon=|s|\mathrm{max}\big\{\mathrm{sup}_\Omega\frac{1}{2}(\mu_1-\mu_2),\mathrm{sup}_\Omega\frac{1}{2}|\mu_1+\mu_2|\big\},\) (24)

_and with_ \(\delta b=s\mathrm{diag}(\mathrm{div}_gV)b\)_, when_ \(\rho\), \(\gamma\)_, and f are transported with the deformation. A conformal deformation,_ \(\mathscr{L}_Vg=2\sigma g\)_, leaves K unchanged and changes only C and b._

_Proof._ We use \(\delta g^{ij}=-g^{ik}\delta g_{kl}g^{lj}\) and \(\delta\sqrt{g}=\frac{1}{2}\sqrt{g}g^{kl}\delta g_{kl}\) with \(\delta g=s\mathscr{L}_Vg\). Since \((\mathscr{L}_Vg)_{ij}=\nabla_iV_j+\nabla_jV_i\), we have \(\frac{1}{2}g^{kl}(\mathscr{L}_Vg)_{kl}=\mathrm{div}_gV\) . By substituting these expressions into \(\delta(\sqrt{g}g^{ij})=\delta\sqrt{g}g^{ij}+\sqrt{g}\delta g^{ij}\), we obtain Eq. (23). Relative to _g_, the trace-free part has the eigenvalues \(\pm\frac{1}{2}(\mu_1-\mu_2)\), and \(\mathrm{div}_gV=\frac{1}{2}(\mu_1+\mu_2)\). The relative changes of the blocks of _W_ and of the entries of _C_ are therefore bounded by the two terms of Eq. (24), and the bound on \(\langle v,\delta Av\rangle\) follows as in the proof of Proposition 15. For \(\mathscr{L}_Vg=2\sigma g\) the trace-free part vanishes.

The stiffness matrix thus responds only to the shear part of the deformation, and the reaction term and the load respond only to the change of area. This is the infinitesimal form of Proposition 12.

A pointwise relative metric bound does not imply the same relative bound on a signed or cancelling load, so the load term must be estimated separately. A Class I approximation that is itself derived from a weak form of the type (18), with \(\rho>0\) and \(\gamma\ge 0\), preserves positive definiteness and therefore Lemma 1. This is analogous to the conserving approximations of many-body theory, which are derived from a functional and therefore preserve the conservation laws \[22\].

