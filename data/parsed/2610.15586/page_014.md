<tbc>with equal shots per state. Unless stated otherwise, the sampling times are \(T_k=k\pi/\lambda_\mathrm{max}\), the reference short step of Sec. 3.1. The error is the relative energy-norm error \(\|x_\mathscr{S}-x^*\|_A/\|x^*\|_A\) of the Galerkin solution of Eq. (5) with respect to the solution of the discrete system. We also use an oracle ordering, which selects modes by the magnitude of the exact coefficients \(|\hat{x}_z|\). It is a reference ordering and need not minimize the Galerkin energy error. The essential set \(\mathscr{E}_\varepsilon\) is the smallest set of the form required in Corollary 3, with \(\varepsilon=1\%\), built in the oracle ordering. No hardware data are included.

## 5.2 Validation of the discretizations

1 validates both discretizations against exact steady solutions. The elliptic duct shows second- order convergence of the velocity and the flow rate. For the lens we use the disk (\(\sigma_0=\pi/2\)). Its flow rate converges to 0.03% on the \(128\times 128\) grid, while the pointwise error is limited at about 1% by the truncation at \(\tau_\mathrm{max}=6\).

## 5.3 Fourier basis versus computational basis

Figures 1 and 2 show the solutions and their Fourier coefficients.  2 compares the subspaces sampled on the \(16\times 16\) grids (8 qubits) with a total budget of _M_=1200 shots. In both geometries the Fourier basis gives an error that is one to three orders of magnitude smaller than the computational basis, with a subspace that is 1.7 to 7 times smaller. For \(\Gamma=1000\) the time evolution helps clearly. With twelve states the error is \(3.3\times 10^{-4}\) (lens) and \(8.3\times 10^{-3}\) (ellipse), while the single state \(|b\rangle\) with the same number of shots gives \(2.4\times 10^{-2}\) and \(2.3\times 10^{-2}\).

\begin{tabular}{ccccc}
 & \multicolumn{2}{c}{Ellipse} & \multicolumn{2}{c}{Disk (lens discretization)} \\
_N_ & max. velocity error & flow-rate error & max. velocity error & flow-rate error \\
16 & \(1.5\times 10^{-3}\) & \(+2.8\times 10^{-3}\) & \(8.1\times 10^{-3}\) & \(-1.1\times 10^{-2}\) \\
32 & \(3.7\times 10^{-4}\) & \(+6.9\times 10^{-4}\) & \(6.9\times 10^{-3}\) & \(-3.0\times 10^{-3}\) \\
64 & \(9.2\times 10^{-5}\) & \(+1.7\times 10^{-4}\) & \(8.2\times 10^{-3}\) & \(-8.6\times 10^{-4}\) \\
128 & \(2.3\times 10^{-5}\) & \(+4.3\times 10^{-5}\) & \(9.0\times 10^{-3}\) & \(-2.9\times 10^{-4}\) \\
\end{tabular}

(c)
1.0
(b)
0
grid points
(a)
0.8
15
1
0.5
mode index in T
103
0.6
10
-2
log10 |W| max
y a
0.0
w Wmax
-3
0.4
5
-4
102
-0.5
0.2
1
0
1
-5
DST modes
x a
0.0
5
10
15
-6
mode index in σ
102
103
104
number of unknowns N2

** 1:** Validation against exact steady solutions. Ellipse: _B<sub>e</sub>/A<sub>e</sub>_=0.5, quarter domain. Disk: lens discretization with \(\sigma_0=\pi/2\), \(\tau_\mathrm{max}=6\). Errors are relative to the maximum velocity and to the exact flow rate.

**Figure 1:** Lens-shaped duct (\(\sigma_0=2\pi/3\), \(32\times 32\) grid). (a) Steady axial velocity. (b) Magnitude of the DST-I coefficients of the solution; only odd-odd modes are nonzero. (c) Number of basis states required for 1% error (\(\Gamma=100\)) versus the number of unknowns: DST modes selected by \(|\hat{b}|\), grid points selected by an oracle ordering, and the total number of unknowns (dashed).

