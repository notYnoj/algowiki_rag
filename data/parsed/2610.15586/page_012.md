### Class II: approximations of the sampler.

These change only the states that are measured. Examples are qDRIFT compilation \[13\], the Trotter splitting of Eq. (29), truncated Walsh series of diagonal phases, approximate state preparation, gate errors, and readout errors. They do not change _A_ or _b_.

**Corollary 17** (Sampler approximations)**.** _Class II approximations leave the Galerkin solution on a given set unchanged. They affect the outcome law, and Theorem 2 and Corollaries 3 and 4 hold with the law that the approximate sampler actually produces._

Circuit approximations can nevertheless destroy essential support. If an essential mode has zero probability, no finite shot budget recovers it without a separate classical expansion. At a fixed budget, both the achieved accuracy and the classical subspace cost can worsen. The hierarchy gives a simple design rule. The accuracy budget is spent on Class I, where Proposition 15 applies. Class II approximations cost shots and coverage, and their effect enters only through the outcome law.

## 4.8 Examples: elliptic, lens-shaped, and curved ducts

We now apply the geometric method to three cases. The first two are exact conformal instances. The third uses the curvature terms of Sec. 4.5 and is treated numerically in Sec. 5.7.

### 4.8.1 The implicit step in conformal coordinates

We consider fully developed axial flow _w(x,y,t_) in a straight duct driven by a pressure gradient _G(t_). Let (_u,v_) be conformal coordinates of the cross section with scale factor _h(u,v_), so that \(\nabla^2=h^{-2}(\partial_{uu}+\partial_{vv})\). We nondimensionalize lengths by a geometric length \(\ell_g\), the velocity by \(G\ell_g^2/\mu\), and time by \(\ell_g^2/v\). The implicit Euler step of the unsteady Stokes equation then reads

\(-(\partial_{uu}+\partial_{vv})w^{n+1}+\Gamma h^2w^{n+1}=h^2\big(\Gamma w^n+G^{n+1}\big),\Gamma=\frac{\ell_g^2}{v\Delta t}.\) (25)

The operator is symmetric positive definite, and its variable coefficient _h_<sup>2</sup> is supplied by the geometry. For \(\Gamma=0\), Eq. (25) reduces to steady Poiseuille flow with a constant-coefficient operator, to which Corollary 8 applies. For a coronary artery with \(\ell_g\approx 1.3-1.5\) mm, \(v=3.3\times 10^{-6}\) m<sup>2</sup>/s, and one hundred steps per cardiac cycle (\(\Delta t=8\) ms), we obtain \(\Gamma\approx 64-85\). We therefore study \(\Gamma=0\), 100, and 1000.

### 4.8.2 Elliptic duct

Elliptic coordinates are \(x=\ell_g\mathrm{cosh}\mu\mathrm{cos}v\), \(y=\ell_g\mathrm{sinh}\mu\mathrm{sin}v\), with \(h^2=\ell_g^2(\mathrm{sinh}^2\mu+\mathrm{sin}^2v)\), where \(\ell_g\) is half the distance between the foci. The wall is \(\mu=\mu_0\), with semi-axes \(A_e=\ell_g\mathrm{cosh}\mu_0\) and \(B_e=\ell_g\mathrm{sinh}\mu_0\). We use _B<sub>e</sub>/A<sub>e</sub>_=0.5. In order to avoid the branch line at the focal segment, we solve on the quarter domain \(0\le\mu\le\mu_0\), \(0\le v\le\pi/2\). The focal segment and the two axes are symmetry lines with zero normal derivative, and the wall carries _w_=0. On a cell-centered grid with _N_=2_<sup>m</sup>_ points per direction, the one-dimensional Laplacians are diagonalized exactly by the DCT-IV in \(\mu\) and the DCT-II in _v_. The measurement basis is \(F=\mathrm{DCT}-\mathrm{IV}\otimes\mathrm{DCT}-\mathrm{II}\) on 2_m_ qubits. The steady solution is known in closed form \[23\],<tbc>

\(w=\frac{A_e^2B_e^2}{2(A_e^2+B_e^2)}\big(1-\frac{x^2}{A_e^2}-\frac{y^2}{B_e^2}\big),Q=\frac{\pi A_e^3B_e^3}{4(A_e^2+B_e^2)}.\) (26)

<tbc>Since _h_<sup>2</sup> is a sum of a function of \(\mu\) and a function of _v_, the operator of Eq. (25) is separable,

\(A=A_\mu\otimes I+I\otimes A_v,A_\mu=-\partial_{\mu\mu}+\Gamma\mathrm{sinh}^2\mu,A_v=-\partial_{vv}+\Gamma\mathrm{sin}^2v.\) (27)

The continuous counterparts of \(A_\mu\) and _A<sub>v</sub>_ are the modified and ordinary Mathieu operators \[24\]. Separability has three consequences. First, the system is solved classically by two \(N\times N\) eigenvalue problems. Second, \(e^{-iAT}=e^{-iA_\mu T}\otimes e^{-iA_vT}\), so no entangling gate between the registers is needed for the time evolution. Third, the source _h_<sup>2</sup> has Schmidt rank 2, and the product evolution preserves this rank. Each<tbc>

