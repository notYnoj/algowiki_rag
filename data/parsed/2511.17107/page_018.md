where \(\omega_{h,j}^{(1)}(\mathbf{k}),\omega_{h,j}^{(2)}(\mathbf{k})\) denote the _j_-th frequency at the wave number vector **k** and grid size _h_. The superscripts (1), (2) correspond to permittivity matrix M<sub>Trivial</sub> and M<sub>CrossDoF</sub>, respectively. As is shown in  2, the difference is rather minor.

## 4.2. Precision Tests

s 3 and 4 present the first 8 smallest non-zero frequencies of the BCC-SG lattice in anisotropic media, computed with mesh resolutions _N_=16,32,64,128 and a 10th-order finite difference stencil. We choose both M=M<sub>Trivial</sub> and M=M<sub>CrossDoF</sub> to evaluate the relative errors and the corresponding average convergence rates. For certain cases, both discretization methods achieve approximately second-order convergence, with M=M<sub>CrossDoF</sub> yielding slightly higher accuracy than M=M<sub>Trivial</sub>. However, for specific eigenvalues (the 3rd and 4th eigenvalues

\begin{tabular}{ccccc}
Lattice type & SC-CURV & FCC & BCC-SG & BCC-DG \\
\(\Delta\omega_\mathrm{max}\) & \(2.93\times 10^{-3}\) & \(2.76\times 10^{-3}\) & \(4.71\times 10^{-3}\) & \(4.72\times 10^{-3}\) \\
\(\Delta\omega_\mathrm{mean}\) & \(9.88\times 10^{-4}\) & \(1.08\times 10^{-3}\) & \(1.47\times 10^{-3}\) & \(1.08\times 10^{-3}\) \\
\end{tabular}

Isotropic media, BCC-SG, bandgap ratio 0.315.
Anisotropic media, BCC-SG, bandgap ratio 0.193.
0.8
0.8
0.7
0.7
0.6
0.6
Normalized frequencies w/2π
Normalized frequencies w/2π
0.5
0.5
0.4
0.4
0.3
0.3
0.2
0.2
0.1
0.1
0
0
H'
r
P
H'
N
r
H
P
N
H'
r
P
H'
N
r
H
P
N
Wave number vector k
Wave number vector k

Isotropic media, BCC-DG, bandgap doesn't exist.
Anisotropic media, BCC-DG, bandgap doesn't exist.
0.7
0.7
0.6
0.6
Normalized frequencies w/2π
Normalized frequencies w/2π
0.5
0.5
0.4
0.4
0.3
0.3
0.2
0.2
0.1
0.1
0
0
H'
r
P
H'
N
r
H
P
N
H'
r
P
H'
N
r
H
P
N
Wave number vector k
Wave number vector k

**Figure 5:** Band structures of BCC lattice with single gyroid surfaces. Left: isotropic system; Right: anisotropic system. Grid division _N_=120.

**Figure 6:** Band structures of BCC lattice with double gyroid surfaces. Left: isotropic system; Right: anisotropic system. Grid division _N_=120.

** 2**<br>
Maximum and mean relative difference of frequencies computed with two types of \(\mathcal{M}_\varepsilon\) in Subsection 4.1 over the complete band.

