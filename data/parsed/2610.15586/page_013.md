Krylov circuit therefore consists of one _R<sub>Y</sub>_ rotation that prepares \(s_1|0\rangle+s_2|1\rangle\) on the first qubit, one CNOT gate to the second register, and two _m_-qubit unitaries

\(W_\mu=\mathrm{DCT}_4e^{-iA_\mu T}U_u,W_\nu=\mathrm{DCT}_2e^{-iA_\nu T}U_v,\) (28)

where _U<sub>u</sub>_ and _U<sub>v</sub>_ map \(|0\rangle,|1\rangle\) to the Schmidt vectors of the source. The circuit is exact, and its depth does not depend on _T_. This makes the elliptic duct a structured calibration benchmark. On the other hand, generic synthesis of \(W_\mu\) and _W<sub>v</sub>_ has a cost exponential in the register size, so separability alone does not supply an efficient asymptotic quantum algorithm, and the problem is classically easy.

### 4.8.3 Lens-shaped duct

Bipolar coordinates are \(x=\ell_g\mathrm{sinh}\tau/(\mathrm{cosh}\tau-\mathrm{cos}\sigma),y=\ell_g\mathrm{sin}\sigma/(\mathrm{cosh}\tau-\mathrm{cos}\sigma)\), with \(h=\ell_g/(\mathrm{cosh}\tau-\mathrm{cos}\sigma)\). A curve of constant \(\sigma\) is a circular arc through the foci \((\pm\ell_g,0)\). The lens is the region \(\sigma_0\le\sigma\le 2\pi-\sigma_0\), whose corners at the foci have the interior angle \(W_c=2\pi-2\sigma_0\). For \(\sigma_0=\pi/2\) the lens is a disk of radius \(\ell_g\). We use \(\sigma_0=2\pi/3\), which gives corners of \(120^\circ\). The strip \(-\infty<\tau<\infty\) is truncated to \(|\tau|\le\tau_\mathrm{max}\) with _w_=0 at \(\tau=\pm\tau_\mathrm{max}\). It can be shown that the homogeneous solutions decay as \(e^{-\pi|\tau|/W_c}\) toward the corners, so the truncation error is exponentially small. We use \(\tau_\mathrm{max}=6\). With Dirichlet conditions on all sides and _N_ interior points, the basis is \(F=\mathrm{DST}-\mathrm{I}\otimes\mathrm{DST}-\mathrm{I}\).

The lens and the source are symmetric about \(\sigma=\pi\) and \(\tau=0\). Therefore only modes with odd indices in both directions are excited. This symmetry sector has dimension _N_<sup>2</sup>/4. Symmetry alone does not make every coefficient in the sector nonzero. This is the selection rule of Proposition 13 for the two reflections of the lens. In the quantum register this sector corresponds to the least significant qubit of each register being 0, and a measured bitstring that violates this rule can be discarded. This parity filter plays the role of particle-number postselection in SQD \[5\].

The lens operator is not separable. We use the split Trotter step

\(e^{-i\Lambda\Delta t/r}\approx F_q^\dagger D_\Lambda F_qD_h,D_\Lambda=e^{-i\Lambda_0\Delta t/r},D_h=e^{-i\Gamma\mathrm{diag}(h^2)\Delta t/r},\) (29)

where \(\Lambda_0\) contains the eigenvalues of the constant-coefficient Laplacian. Both factors are diagonal in some basis, so no Pauli decomposition of _A_ is needed, and \(D_\Lambda\) is separable between the registers. The splitting is a Class II approximation. On hardware the grid and the transform must be chosen together. With _N_=2_<sup>m</sup>_ interior points the DST-I has the denominator _N_+1, so a power-of-two QFT does not implement it exactly without padding. A cell-centered Dirichlet grid leads to a DST-II with a power-of- two denominator, but it changes the discrete operator and the source. We leave it as a future option. For small registers the DST-I can be synthesized exactly as a generic register unitary, and we use this in the hardware pilot. All numerical results below use the DST-I grid.

### 4.8.4 General and curved cross sections

For a patient-specific cross section, Step 1 is a numerical conformal map onto a rectangle or a disk \[17, 18\]. The analytic _h_<sup>2</sup> of the examples above is then replaced by a computed metric factor, and the map error is a Class I approximation bounded by Proposition 15. If no map is available, a Brinkman penalization on a bounding box \[25\] gives an operator of the same form with a discontinuous coefficient. For a curved vessel, Step 2 uses the coefficients (20). The curvature breaks the symmetry \(\tau\rightarrow-\tau\) of the lens, so that the parity filter acts only in \(\sigma\).

## 5 Numerical results for duct flows

### 5.1 Setup

All results in this section use exact time evolution of the discrete operator and multinomial sampling from the exact outcome laws, without hardware noise unless stated otherwise. We use _d_=12 Krylov states<tbc>

