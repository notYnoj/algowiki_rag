## 4.2 Elliptic problems on a Riemannian cross section

Let \(\Omega\) have local coordinates (_u_<sup>1</sup>_,u_<sup>2</sup>) and metric _g<sub>ij</sub>_, and let \(\sqrt{g}=\sqrt{\mathrm{det}g_{ij}}\). We consider the weak problem: find _w_ with _w_=0 on the wall such that

\(\int_R\big(\rho g^{ij}\partial_iw\partial_jv+\gamma wv\big)\sqrt{g}du^1du^2=\int_Rfv\sqrt{g}du^1du^2\) (18)

for all admissible _v_. Here \(\rho>0\) and \(\gamma\ge 0\) are coefficient fields. Equation (18) is the weak form of \(-\nabla_g\cdot(\rho\nabla_gw)+\gamma w=f\), where \(\nabla_g\) denotes the Levi-Civita gradient and divergence \[10\]. A conservative discretization on a coordinate grid gives

\(A=K+C,K=\nabla_h^TW\nabla_h,W=\mathrm{blockdiag}\big(\rho\sqrt{g}[g^{ij}]\big),C=\mathrm{diag}(\gamma\sqrt{g}),b=\mathrm{diag}(\sqrt{g})f.\) (19)

where \(\nabla_h\) is the discrete gradient. For an orthogonal coordinate system \[_g<sup>ij</sup>_\] is diagonal and _K_ is a symmetric five-point stencil.

**Proposition 11** (Structure)**.** _The matrix A of Eq._ (19) _is real symmetric positive definite whenever_ \(\rho>0\), \(\gamma\ge 0\)_, and the wall carries a Dirichlet condition. Therefore the results of Sec. 3 apply to every problem of the form_ (18)_, for any metric and any orthogonal measurement basis._

The implicit Euler step of the unsteady Stokes equation, Eq. (25) below, is the case \(\rho=1\), \(\gamma=\Gamma\), and \(f=\Gamma w^n+G^{n+1}\).

## 4.3 Conformal reduction in two dimensions

**Proposition 12** (Conformal reduction)**.** _If the coordinates are conformal,_ \(g_{ij}=h^2\delta_{ij}\)_, then_ \(\sqrt{g}g^{ij}=\delta^{ij}\)_. As a result, K is the flat stiffness matrix with coefficient_ \(\rho\)_, independent of the metric, and the geometry enters only through_ \(C=\mathrm{diag}(\gamma h^2)\) _and b_=diag(_h_<sup>2</sup>)_f._

_Proof._ In two dimensions \(\sqrt{g}=h^2\) and \(g^{ij}=h^{-2}\delta^{ij}\), so their product is \(\delta^{ij}\).

Proposition 12 is the discrete form of the conformal invariance of the Dirichlet energy in two dimensions. When the coordinate domain is a rectangle and \(\rho=1\), a sine or cosine basis diagonalizes _K_ exactly, and all mode coupling comes from the metric factor _h_<sup>2</sup> through _C_. A proper simply connected planar domain admits a conformal map to the disk. Mapping a physical boundary to a rectangle or a strip requires appropriate boundary treatment, and corners, narrow features, and mapping singularities can affect numerical conditioning. Patient-specific cross sections segmented from images can be treated by a numerical conformal map \[17, 18\], which replaces the analytic _h_<sup>2</sup> of the examples below by a computed one.

## 4.4 Symmetries and the Lie derivative

Step 4 of the geometric method applies a filter that removes indices at which the solution vanishes. The Lie derivative gives a systematic way to find such indices. A vector field _X_ on \(\Omega\) is a Killing field if L_<sub>X</sub>g_=0, where L_<sub>X</sub>_ denotes the Lie derivative (Appendix A). Its flow is then a one-parameter group of isometries. A reflection that maps \(\Omega\) onto itself and preserves _g_ is a discrete isometry.

**Proposition 13** (Symmetry selection rule)**.** _(i) Let X be a Killing field that is tangent to the wall and has a complete flow on_ \(\Omega\)_, and assume_ \(\mathcal{L}_X\rho=\mathcal{L}_X\gamma=0\)_. Then_ L_<sub>X</sub> commutes with the solution operator of Eq._ (18)_. In particular, if_ L_<sub>X</sub>f_=0_, then_ L_<sub>X</sub>w_=0_, and if_ -_i_L_<sub>X</sub>f=mf, then_ -_i_L_<sub>X</sub>w=mw._

_(ii) Let P be a unitary matrix with PA=AP and_ \(Pb=\chi b\)_. Then every Krylov state e_<sup>-_iAT_</sup>_b and the solution x_<sup>∗</sup> _are eigenvectors of P with eigenvalue_ \(\chi\)_. If the measurement basis F diagonalizes P, with_ \(FPF^\dagger=\mathrm{diag}(\chi_z)\)_, then q(z_)=0 _and_ \(\hat{x}_z=0\) _for every index with_ \(\chi_z\neq\chi\).

