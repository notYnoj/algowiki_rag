## 5.6 Comparison with classical mode selection

Because _b_ and _A_ are known classically, the sampler must be compared with classical selections of the same Galerkin subspace. We consider three. The first selects the modes with the largest \(|\hat{b}_z|\). The second selects the largest \(|\hat{b}_z/\Lambda_{0,z}|\). The third is the residual-greedy method, which starts from the ten largest \(|\hat{b}_z|\) and repeatedly adds the modes with the largest residual, i.e., Phase 2 of Algorithm 1 used alone. Its cost includes residual formation and repeated solves; the efficiency \(\eta_\mathrm{s}\) is not a performance measure for this deterministic method.

8 shows the result for the ellipse at matched |S|. With a suitable uniform step, the Krylov sampling outperforms the first two selections by one to four orders of magnitude. This is the effect of Theorem 7. The residual-greedy method, however, is better than the Krylov sampling in every case, often by several orders of magnitude. For the lens it is at least as good. For an off-center localized source in the lens, the selection by \(|\hat{b}|\) was also better than the Krylov sampling, by a factor of 1.3 to 2.4 in error. These results are consistent with the efficiency analysis and with the remark in Sec. 7 that favorable concentration alone is not evidence of quantum advantage.

## 5.7 Geometric extensions

### Curvature.

9 applies Eq. (20) to the disk and the \(120^\circ\) lens on the \(32\times 32\) grid with \(\Gamma=100\), the multiscale heuristic, and _M_=19200. The curvature breaks the symmetry \(\tau\rightarrow-\tau\), and the number of nonzero modes doubles from 256 to 512. The essential set grows by a factor of 1.5 to 1.9 at \(\kappa_c\ell_g=0.3\), while \(\eta_\mathrm{s}\) stays of order 10<sup>-3</sup>. The source _h_<sup>2</sup> remains symmetric while the solution does not, which is the support mismatch of Theorem 7. As a result, at \(\kappa_c\ell_g=0.3\) the Krylov sampling is 2.5 to 5 times more<tbc>

\begin{tabular}{cccc}
Case & times & _M_=4800 & _M_=19200 \\
Ellipse 16<sup>2</sup>, \(\Gamma=1000\) & \(k\pi/\lambda_\mathrm{max}\) & \(2.7\times 10^{-4}/2.8\times 10^{-3}\) & \(1.1\times 10^{-4}/2.6\times 10^{-4}\) \\
Ellipse 32<sup>2</sup>, \(\Gamma=100\) & \(k\pi/\sqrt{\lambda_\mathrm{min}\lambda_\mathrm{max}}\) & \(4.6\times 10^{-3}/7.2\times 10^{-3}\) & \(3.7\times 10^{-5}/6.5\times 10^{-4}\) \\
Ellipse 32<sup>2</sup>, \(\Gamma=1000\) & \(k\pi/\lambda_\mathrm{max}\) & \(1.1\times 10^{-2}/2.1\times 10^{-2}\) & \(2.7\times 10^{-3}/1.0\times 10^{-2}\) \\
Lens 16<sup>2</sup>, \(\Gamma=1000\) & \(k\pi/\lambda_\mathrm{max}\) & \(3.6\times 10^{-5}/1.4\times 10^{-4}\) & \(8.7\times 10^{-6}/1.3\times 10^{-5}\) \\
Lens 32<sup>2</sup>, \(\Gamma=100\) & \(k\pi/\lambda_\mathrm{max}\) & \(8.7\times 10^{-3}/1.3\times 10^{-2}\) & \(3.2\times 10^{-3}/4.8\times 10^{-3}\) \\
Lens 32<sup>2</sup>, \(\Gamma=1000\) & \(k\pi/\lambda_\mathrm{max}\) & \(1.2\times 10^{-2}/1.8\times 10^{-2}\) & \(4.8\times 10^{-3}/5.7\times 10^{-3}\) \\
\end{tabular}

\begin{tabular}{cccccc}
Case & \(|\mathcal{E}_\varepsilon|\) & \(k\pi/\lambda_\mathrm{max}\) & \(k\pi/\sqrt{\lambda_\mathrm{min}\lambda_\mathrm{max}}\) & multiscale & ratio \\
Ellipse 16<sup>2</sup>, \(\Gamma=100\) & 37 & \(1.2\times 10^{-7}\) & \(6.7\times 10^{-4}\) & \(6.5\times 10^{-4}\) & 0.97 \\
Ellipse 16<sup>2</sup>, \(\Gamma=1000\) & 41 & \(1.3\times 10^{-3}\) & \(2.6\times 10^{-4}\) & \(7.2\times 10^{-4}\) & 0.55 \\
Ellipse 32<sup>2</sup>, \(\Gamma=100\) & 56 & \(5.3\times 10^{-15}\) & \(2.9\times 10^{-4}\) & \(3.0\times 10^{-4}\) & 1.03 \\
Ellipse 32<sup>2</sup>, \(\Gamma=1000\) & 75 & \(2.8\times 10^{-6}\) & \(9.3\times 10^{-5}\) & \(1.5\times 10^{-4}\) & 1.6 \\
Ellipse 64<sup>2</sup>, \(\Gamma=100\) & 67 & \(8.4\times 10^{-20}\) & \(4.1\times 10^{-6}\) & \(1.5\times 10^{-4}\) & 37 \\
Ellipse 64<sup>2</sup>, \(\Gamma=1000\) & 118 & \(5.0\times 10^{-15}\) & \(3.8\times 10^{-5}\) & \(7.5\times 10^{-5}\) & 2.0 \\
Lens 16<sup>2</sup>, \(\Gamma=100\) & 35 & \(2.1\times 10^{-4}\) & \(1.2\times 10^{-4}\) & \(1.6\times 10^{-4}\) & 0.76 \\
Lens 16<sup>2</sup>, \(\Gamma=1000\) & 31 & \(2.0\times 10^{-3}\) & \(2.1\times 10^{-3}\) & \(2.0\times 10^{-3}\) & 0.95 \\
Lens 32<sup>2</sup>, \(\Gamma=100\) & 58 & \(5.0\times 10^{-5}\) & \(5.4\times 10^{-5}\) & \(1.2\times 10^{-4}\) & 2.2 \\
Lens 32<sup>2</sup>, \(\Gamma=1000\) & 59 & \(4.4\times 10^{-5}\) & \(3.9\times 10^{-5}\) & \(4.3\times 10^{-5}\) & 0.98 \\
Lens 64<sup>2</sup>, \(\Gamma=100\) & 90 & \(5.7\times 10^{-6}\) & \(7.3\times 10^{-5}\) & \(8.8\times 10^{-5}\) & 1.2 \\
Lens 64<sup>2</sup>, \(\Gamma=1000\) & 107 & \(3.8\times 10^{-5}\) & \(8.8\times 10^{-6}\) & \(2.0\times 10^{-5}\) & 0.53 \\
\end{tabular}

** 5:** Relative energy-norm error: observed root-mean-square value over four sampling runs / square root of the bound of Theorem 2.

** 6:** Smallest sampling probability \(q_\mathrm{min}(\mathcal{E}_\varepsilon)\) on the essential set (\(\varepsilon=1\%\)) for three sets of _d_=12 times. The last column is the ratio of the multiscale value to the better of the two uniform steps.

