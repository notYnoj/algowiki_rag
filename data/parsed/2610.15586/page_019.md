<tbc>active. They contain 78, 194, and 315 logical two-qubit gates for six qubits and 332, 862, and 1395 for eight qubits. With a single step, the circuit laws for _k_=1 and 2 differ from the exact evolution by total-variation distances between 0.05 and 0.08. We therefore compare the measured laws with the laws of the circuits as submitted.

We use the register convention of Appendix D: the integer outcome of the measured bits equals the row-major mode index _k_<sub>1</sub>_N+k_<sub>2</sub>. Every circuit was checked against its ideal law by an exact statevector calculation before submission. Each circuit was run with 500 shots. The IonQ circuits were run on 11 October 2026 without debiasing or symmetry verification. The provider returned the outcome frequencies; all of them are integer multiples of 1/500, so the integer counts are recovered exactly. The IBM circuits were run on 14 October 2026 with dynamical decoupling and twirling disabled, and the raw counts were recorded. The IBM processor uses CZ as its native two-qubit gate. On the qubits used, the calibrated median CZ error was \(1.5\times 10^{-3}\) and the median readout error was \(3.5\times 10^{-3}\). Routing to the heavy-hex connectivity increased the native two-qubit count by a factor of 1.6 to 2.1 relative to the logical count.

\begin{tabular}{ccccccccc}
Cross section & \(\kappa_e\ell_g\) & nonzero & \(|\mathcal{E}_e|\) & \(\eta_\mathrm{s}\) & \(|\mathcal{S}|\) & Krylov & top-\(|\hat{b}|\) & residual-greedy \\
Disk & 0 & 256 & 70 & \(6.0\times 10^{-3}\) & 236 & \(2.0\times 10^{-3}\) & \(6.4\times 10^{-7}\) & \(3.5\times 10^{-7}\) \\
Disk & 0.1 & 512 & 107 & \(5.6\times 10^{-3}\) & 401 & \(4.3\times 10^{-3}\) & \(3.4\times 10^{-3}\) & \(2.0\times 10^{-6}\) \\
Disk & 0.3 & 512 & 132 & \(5.8\times 10^{-3}\) & 413 & \(4.0\times 10^{-3}\) & \(1.0\times 10^{-2}\) & \(3.3\times 10^{-6}\) \\
Lens \(120^\circ\) & 0 & 256 & 58 & \(6.7\times 10^{-3}\) & 190 & \(1.5\times 10^{-3}\) & \(2.5\times 10^{-6}\) & \(9.3\times 10^{-7}\) \\
Lens \(120^\circ\) & 0.1 & 512 & 84 & \(4.4\times 10^{-3}\) & 338 & \(2.9\times 10^{-3}\) & \(7.6\times 10^{-3}\) & \(2.5\times 10^{-6}\) \\
Lens \(120^\circ\) & 0.3 & 511 & 102 & \(2.0\times 10^{-3}\) & 338 & \(4.5\times 10^{-3}\) & \(2.3\times 10^{-2}\) & \(4.2\times 10^{-6}\) \\
\end{tabular}

\begin{tabular}{ccccccccc}
Platform & Circuit & 2Q & TV & TV (sampling) & _p_ & Residual & Acceptance / 1-3_p/_4 \\
IonQ, 6 qubits & Ellipse, _k_=0 & 38 & 0.296 & 0.046 & 0.38 & 0.215 (0.110) & - \\
 & Ellipse, _k_=1 & 39 & 0.274 & 0.062 & 0.28 & 0.191 (0.110) & - \\
 & Ellipse, _k_=2 & 39 & 0.226 & 0.074 & 0.23 & 0.139 (0.109) & - \\
 & Lens, _k_=0 & 78 & 0.327 & 0.043 & 0.42 & 0.233 (0.114) & 0.726 / 0.689 \\
 & Lens, _k_=1 & 194 & 0.539 & 0.055 & 0.64 & 0.167 (0.130) & 0.510 / 0.520 \\
 & Lens, _k_=2 & 315 & 0.748 & 0.042 & 0.88 & 0.209 (0.139) & 0.310 / 0.338 \\
IBM, 6 qubits & Ellipse, _k_=0 & 38 / 67 & 0.441 & 0.046 & 0.51 & 0.296 (0.120) & - \\
 & Ellipse, _k_=1 & 39 / 68 & 0.268 & 0.062 & 0.29 & 0.178 (0.111) & - \\
 & Ellipse, _k_=2 & 39 / 68 & 0.258 & 0.073 & 0.14 & 0.214 (0.099) & - \\
 & Lens, _k_=0 & 78 / 143 & 0.686 & 0.043 & 0.76 & 0.273 (0.134) & 0.462 / 0.431 \\
 & Lens, _k_=1 & 194 / 317 & 0.779 & 0.055 & 0.98 & 0.186 (0.142) & 0.262 / 0.266 \\
 & Lens, _k_=2 & 315 / 527 & 0.856 & 0.043 & 0.97 & 0.149 (0.143) & 0.266 / 0.270 \\
IBM, 8 qubits & Ellipse, _k_=0 & 191 / 340 & 0.677 & 0.055 & 0.78 & 0.447 (0.272) & - \\
 & Ellipse, _k_=1 & 191 / 340 & 0.660 & 0.064 & 0.78 & 0.425 (0.273) & - \\
 & Ellipse, _k_=2 & 191 / 340 & 0.663 & 0.074 & 0.71 & 0.436 (0.266) & - \\
 & Lens, _k_=0 & 332 / 711 & 0.911 & 0.057 & 1.00 & 0.298 (0.276) & 0.296 / 0.250 \\
 & Lens, _k_=1 & 862 / 1813 & 0.900 & 0.088 & 1.00 & 0.276 (0.276) & 0.216 / 0.251 \\
 & Lens, _k_=2 & 1395 / 2975 & 0.890 & 0.090 & 1.00 & 0.295 (0.277) & 0.260 / 0.251 \\
\end{tabular}

** 9:** Curved vessels, reduced model (20) (\(32\times 32\), \(\Gamma=100\), multiscale heuristic, _M_=19200). Errors are relative energy-norm errors at the |S| reached by the Krylov sampling.

** 10:** Hardware results (500 shots per circuit). 2Q: logical / native two-qubit gates. TV: total-variation distance between the measured law and the circuit law; the sampling column is its expected value for 500 ideal shots. _p_: fitted replacement probability of the model (1-_p)q+p/_2_<sup>n</sup>_. Residual: distance after the fit, with its sampling value in parentheses. Acceptance: fraction of lens shots in the odd-odd sector, followed by the value 1-3_p/_4 predicted by the fitted model.

