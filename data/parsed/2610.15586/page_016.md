### Error bound.

5 compares the observed errors with Theorem 2. The bound holds in all cases. It exceeds the observed root-mean-square error by a factor of 1.2 to 18, and by less than 4 in ten of the twelve entries.

### Uniform steps and the multiscale heuristic.

6 lists \(q_\mathrm{min}(\mathscr{E}_\varepsilon)\) for two uniform steps and for Algorithm 2. The short step \(\pi/\lambda_\mathrm{max}\) fails on the finer elliptic grids, where _q_<sub>min</sub> drops to 10<sup>-15</sup>-10<sup>-20</sup>, in agreement with Lemma 9. The geometric-mean step is better but loses a factor of 37 on the \(64\times 64\) ellipse. The multiscale heuristic is within a factor of 2 of the better uniform step in all twelve cases and is the best choice in six. This is an empirical observation; Lemma 10 does not apply to Algorithm 2.

### Efficiency and initial state.

With the multiscale heuristic, the efficiency of Eq. (13) lies between \(2\times 10^{-3}\) and \(6\times 10^{-2}\). The sampler is therefore 16 to 480 times less efficient than a uniform law on \(\mathscr{E}_\varepsilon\). It seems natural to start the evolution from an approximate solution, such as \(|\Lambda_0^{-1}b\rangle\), so that the sampling resembles \(|\hat{x}|^2\). This was harmful for the tested initial states. In the four cases tested, \(q_\mathrm{min}(\mathscr{E}_\varepsilon)\) drops by four to six orders of magnitude and the error at _M_=19200 increases to about 10%. Proposition 5 explains the failure: a law close to \(|\hat{x}|^2\) is strongly concentrated, while efficient coverage requires a flat law on \(\mathscr{E}_\varepsilon\).

## 5.5 Noise and the parity filter

We model hardware errors by replacing each shot, with probability _p_, by a uniformly random index.  7 shows the result for the lens on the \(32\times 32\) grid. The parity filter removes about three quarters of the spurious indices without changing the error. In these runs the error decreases as the contamination increases, because random indices fill the small symmetric sector. This is an empirical outcome for this law. It is not a consequence that holds at a fixed shot budget for arbitrary replacement noise (Corollary 6), and it shows that a low error alone is not evidence of a useful quantum sampler.

\begin{tabular}{ccccccc}
 & & \multicolumn{3}{c}{Lens} & \multicolumn{2}{c}{Ellipse} \\
_N_ & qubits & oracle & top-\(|\hat{b}|\) & grid points (oracle) & oracle & top-\(|\hat{b}|\) \\
8 & 6 & 14 & 14 & 61 & 19 & 27 \\
16 & 8 & 27 & 27 & 217 & 32 & 115 \\
32 & 10 & 46 & 43 & 897 & 45 & 143 \\
64 & 12 & 63 & 60 & 3649 & 40 & 249 \\
\end{tabular}

\begin{tabular}{cccccc}
Case & dephased ratio & single-state ratio & \(\#\hat{x}(10^{-12})\) & \(\#\hat{x}(10^{-24})\) & \(|\mathrm{supp}\hat{b}|\) \\
Ellipse 16<sup>2</sup>, \(\Gamma=1000\) & 10.7 & 0 & 93 & 236 & 32 \\
Ellipse 32<sup>2</sup>, \(\Gamma=100\) & 4.0 & 0 & 94 & 266 & 64 \\
Ellipse 32<sup>2</sup>, \(\Gamma=1000\) & 9.4 & 0 & 139 & 416 & 64 \\
Lens 16<sup>2</sup>, \(\Gamma=1000\) & 791 & \(3.8\times 10^3\) & 64 & 64 & 64 \\
Lens 32<sup>2</sup>, \(\Gamma=100\) & 11.9 & 3.4 & 150 & 256 & 256 \\
Lens 32<sup>2</sup>, \(\Gamma=1000\) & 435 & 3.2 & 167 & 256 & 256 \\
\end{tabular}

** 3:** Scaling with the grid (\(\Gamma=100\)). Number of basis states required for 1% relative energy-norm error. The lens grid is the full domain; the ellipse grid is the quarter domain.

** 4:** Support completeness, Eq. (15). Minimum over modes with \(|\hat{x}_z|^2\ge 10^{-24}\|\hat{x}\|^2\) of the dephased ratio \(q^\infty(z)\mathrm{tr}A^{-2}/|\hat{x}_z|^2\) (bound: \(\ge 1\)) and of the single-state ratio \(|\hat{b}_z|^2\mathrm{tr}A^{-2}/|\hat{x}_z|^2\). The last three columns count solution modes with relative weight above 10<sup>-12</sup> and 10<sup>-24</sup>, and the exact support of \(\hat{b}\).

