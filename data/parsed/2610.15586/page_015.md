<tbc> 3 shows the scaling with the grid for \(\Gamma=100\). For the lens, the number of modes selected by \(|\hat{b}|\) for 1% error grows from 14 to 60 while the number of unknowns grows from 64 to 4096. For the ellipse the oracle ordering requires between 19 and 45 modes. In the computational basis, an oracle ordering still requires 85-95% of all grid points for the lens and all grid points for the ellipse. The selection by \(|\hat{b}|\) is smaller than the oracle ordering in some lens rows, which illustrates that the oracle ordering is not an optimal Galerkin subspace.

## 5.4 Verification of the energy-norm theory

### Support completeness.

4 tests Eq. (15) without a support threshold in the bound itself. The ratio \(q^\infty(z)\text{tr}A^{-2}/|\hat{x}_z|^2\) must be at least 1 for every mode, and it is. We compute \(q^\infty\) with degenerate eigenvalues grouped into spectral projectors (tolerance \(10^{-6}\lambda_\text{max}\)). Without this grouping, exactly degenerate pairs from different symmetry sectors are split and produce spurious weight outside the sector. The same ratio formed with the single-state law \(|\hat{b}_z|^2\) vanishes for the ellipse. The source \(h^2=\ell_g^2(\text{sinh}^2\mu+\text{sin}^2\nu)\) excites exactly 32 or 64 modes, whereas the solution has weight above 10<sup>-12</sup> in 93 to 139 modes. For the lens, both \(\hat{b}\) and \(\hat{x}\) lie in the odd-odd sector of dimension _N_<sup>2</sup>/4. The solution coefficients decay rapidly, so the number of modes counted as nonzero depends on the threshold;  4 gives two thresholds. The minimum ratios do not change between them.  3 shows the consequence of the ellipse mismatch: a selection by \(|\hat{b}|\) matches the oracle for the lens and fails for the ellipse.

\begin{tabular}{ccccc}
Geometry & \(\Gamma\) & Fourier, _d_=12 & Fourier, _d_=1 & Computational, _d_=12 \\
Lens & 0 & \(26/1.0\times 10^{-2}\) & \(24/1.8\times 10^{-2}\) & \(139/1.8\times 10^{-1}\) \\
Lens & 100 & \(41/1.0\times 10^{-2}\) & \(21/2.3\times 10^{-2}\) & \(136/2.5\times 10^{-1}\) \\
Lens & 1000 & \(54/3.3\times 10^{-4}\) & \(23/2.4\times 10^{-2}\) & \(93/3.0\times 10^{-1}\) \\
Ellipse & 0 & \(28/4.4\times 10^{-3}\) & \(25/6.4\times 10^{-3}\) & \(192/5.3\times 10^{-1}\) \\
Ellipse & 100 & \(28/2.1\times 10^{-2}\) & \(25/4.1\times 10^{-2}\) & \(195/4.9\times 10^{-1}\) \\
Ellipse & 1000 & \(60/8.3\times 10^{-3}\) & \(28/2.3\times 10^{-2}\) & \(193/3.6\times 10^{-1}\) \\
\end{tabular}

(c)
1.0
100
(b)
0
(a)
0.8
15
10-2
0.5
mode index in v
-2
0.6
10
relative A-norm error
10-4
0.0
0.4
W Wmax
-3
log10 |W| max
0.5
5
-4
10-6
-1
0
1
0.2
-5
x / c
5
10
15
10-8
0.0
mode index in μ
-6
101
102
|S|
classical top-[f]
Krylov, At = n/v(λminmax)
Krylov, At = n/||A|
classical residual-greedy

**Figure 2:** Elliptic duct (_B<sub>e</sub>/A<sub>e</sub>_=0.5, \(32\times 32\) quarter grid, \(\Gamma=100\)). (a) Axial velocity after the first implicit step from rest, mirrored to the full ellipse; dots mark the foci. (b) Magnitude of the coefficients in the DCT-IV\(\otimes\)DCT-II basis; the solution is concentrated near two lines of modes. (c) Error versus subspace size for classical selection by \(|\hat{b}|\), Krylov sampling with two uniform steps (\(\pi/\lambda_\text{max}\) and \(\pi/\sqrt{\lambda_\text{min}\lambda_\text{max}}\); up to 19200 shots), and classical residual-greedy selection.

** 2:** Sampled subspaces on the \(16\times 16\) grids (8 qubits), _M_=1200, \(T_k=k\pi/\lambda_\text{max}\). Entries are |S| / relative energy-norm error.

