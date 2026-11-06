<tbc>The dampening history of the residuals is documented in Figure 7, where we observe a smooth convergence. Moreover, M<sub>CrossDoF</sub> has better numerical performance in avoiding stagnation under extreme cases.

This customized matrix \(\varepsilon_1\), in general, does not satisfy Assumption 3.2 or 3.3, which further shows the robustness of our scheme.

## 5. Conclusions

In this paper, we have presented a robust, GPU-accelerated framework for solving 3D Maxwell eigenproblems in photonic crystals with anisotropic media. Our key innovations include a novel, provably positive definite discretization for the anisotropic permittivity tensor and a rigorous theoretical completion of the kernel compensation method, which now includes a precise characterization of the null space H, an explicit rule for selecting the penalty coefficient \(\gamma\), an<tbc>

\begin{tabular}{ccccc}
**Eigenvalue** & \multicolumn{2}{c}{**Absolute Difference**} & \(|\omega_h^2-\omega_{2h}^2|\) & **Average** \\
**Index** & _h_=1/32 & _h_=1/64 & _h_=1/128 & **Order** \\
1 & 4.87e-09 & 5.36e-12 & 6.22e-15 & 9.79 \\
2 & 4.87e-09 & 5.36e-12 & 7.41e-15 & 9.66 \\
3 & 1.97e-08 & 2.23e-11 & 2.53e-14 & 9.79 \\
4 & 1.97e-08 & 2.23e-11 & 3.14e-14 & 9.63 \\
5 & 1.97e-08 & 2.23e-11 & 3.31e-14 & 9.59 \\
6 & 3.60e-08 & 4.13e-11 & 3.51e-14 & 9.98 \\
7 & 3.60e-08 & 4.13e-11 & 4.14e-14 & 9.87 \\
8 & 3.60e-08 & 4.14e-11 & 3.31e-14 & 10.03 \\
\end{tabular}

\begin{tabular}{ccccc}
 & SC-CURV & FCC & BCC-SG & BCC-DG \\
Isotropic & 32.8 (4.0) & 42.2 (6.9) & 55.0 (6.9) & 58.0 (6.6) \\
Anisotropic \(\mathcal{M}_\varepsilon=\mathcal{M}_\text{Trivial}\) & 52.3 (5.1) & 54.0 (7.4) & 68.7 (8.7) & 76.5 (8.5) \\
Anisotropic \(\mathcal{M}_\varepsilon=\mathcal{M}_\text{CrossDoF}\) & 45.3 (4.2) & 51.3 (7.9) & 65.8 (8.8) & 74.7 (8.1) \\
\end{tabular}

\begin{tabular}{ccccccccc}
\multirow{2}{*}{DoFs} & \multicolumn{4}{c}{**Isotropic SC-CURV**} & \multicolumn{4}{c}{**Anisotropic SC-CURV**} \\
 & Steps & GPU time & CPU time & Speed up & Steps & GPU time & CPU time & Speed up \\
\(3\times 100^3\) & 31 & 10.79 & 432.71 & 40.10 & 50 & 16.67 & 666.39 & 39.98 \\
\(3\times 120^3\) & 34 & 19.85 & 835.91 & 42.11 & 49 & 28.67 & 1297.50 & 45.26 \\
\multirow{2}{*}{DoFs} & \multicolumn{4}{c}{**Isotropic FCC**} & \multicolumn{4}{c}{**Anisotropic FCC**} \\
 & Steps & GPU time & CPU time & Speed up & Steps & GPU time & CPU time & Speed up \\
\(3\times 100^3\) & 45 & 16.00 & 623.77 & 39.01 & 56 & 19.59 & 852.17 & 43.50 \\
\(3\times 120^3\) & 45 & 27.71 & 1197.90 & 43.23 & 55 & 34.15 & 1506.35 & 44.11 \\
\multirow{2}{*}{DoFs} & \multicolumn{4}{c}{**Isotropic BCC-SG**} & \multicolumn{4}{c}{**Anisotropic BCC-SG**} \\
 & Steps & GPU time & CPU time & Speed up & Steps & GPU time & CPU time & Speed up \\
\(3\times 100^3\) & 57 & 19.85 & 835.33 & 42.08 & 68 & 24.14 & 1020.15 & 42.26 \\
\(3\times 120^3\) & 47 & 27.96 & 1295.39 & 46.33 & 65 & 41.08 & 1816.56 & 44.22 \\
\multirow{2}{*}{DoFs} & \multicolumn{4}{c}{**Isotropic BCC-DG**} & \multicolumn{4}{c}{**Anisotropic BCC-DG**} \\
 & Steps & GPU time & CPU time & Speed up & Steps & GPU time & CPU time & Speed up \\
\(3\times 100^3\) & 89 & 26.83 & 1056.57 & 39.98 & 77 & 25.25 & 1038.00 & 41.11 \\
\(3\times 120^3\) & 86 & 44.61 & 1903.39 & 43.20 & 76 & 43.55 & 1971.94 & 45.28 \\
\end{tabular}

** 5**<br>
SC lattice where dielectric coefficient \(\varepsilon=\varepsilon(x)\) is smooth (4.7), wave number vector \(\mathbf{k}=(\pi,\pi,\pi)\), convergence analysis of the first 8 eigenvalues.

** 6**<br>
Average iterations (and standard deviation) for computing complete band structure. Grid division _N_=120, first 10 eigenpairs are computed with tolerance 10<sup>-5</sup>.

** 7**<br>
CPU and GPU runtime (seconds) for the first 10 eigenvalues of SC-CURV, FCC, BCC-SG, BCC-DG at wave number vector \(\mathbf{k}=(\pi,\pi,\pi)\), grid division _N_=100,120.

