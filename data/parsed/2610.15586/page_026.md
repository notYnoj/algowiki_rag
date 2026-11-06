## B.2 Spectral geometry and sampling efficiency

The efficiency \(\eta_\mathrm{s}\) of Eq. (13) depends on how the eigenvectors of _A_ are spread over the measurement basis, since \(q^\infty(z)=\sum_\lambda|a_\lambda(z)|^2\). In spectral geometry, eigenfunctions of domains with integrable geodesic flow, such as the disk and the ellipse, are structured, while those of chaotic domains, such as the stadium, become equidistributed at high energy \[29-32\]. This suggests a hypothesis: a chaotic cross section might give a flatter _q_, a larger \(\eta_\mathrm{s}\), and an essential set that is harder to find classically. We tested this hypothesis in Sec. 5.7 and found no support for it. A theoretical reason is that quantum ergodicity is a statement about high-lying eigenfunctions, while the solution of an elliptic problem with smooth data is carried by the lowest modes.

### Numerical test.

We tested the hypothesis of Sec. B.2 in two ways. First, we used smooth non-separable conformal deformations of a square, \(h^2=\mathrm{exp}(2\Re\phi)\) with \(\phi\) a random cubic polynomial of amplitude between 0.3 and 1.5. Compared with a separable metric factor on the same square, the efficiency did not increase (\(\eta_\mathrm{s}=3\times 10^{-4}\) to \(3\times 10^{-3}\) versus \(8\times 10^{-4}\)), and the residual-greedy selection remained 2 to 13 times more accurate than the Krylov sampling. Second, we compared cross sections of equal area with integrable and chaotic geodesic flow by Brinkman penalization on a bounding box ( 12). Penalization is a Class I approximation that avoids a conformal map. The sharp interface spreads the solution in the Fourier basis, so the subspaces are larger and the errors higher than with conformal coordinates. The chaotic stadium does not give a higher efficiency than the disk, the ellipse, or the square. In all four cases the residual-greedy selection is about twice as accurate as the Krylov sampling.

## B.3 Metric perturbation

We perturbed the metric factor of the lens and the disk by \(\delta(h^2)=\epsilon h^2\mathrm{sin}(k_1\sigma+k_2\tau+\phi)\) with random \(k_1,k_2,\phi\), which models the error of a numerical conformal map, with the load held fixed.  13 shows the largest relative energy-norm change of the solution over five samples. The bound of Proposition 15 holds and is within a factor of 1.7 of the observed change.

## B.4 Circuit resources and source preparation

Resource accounting must include preparation, evolution, and the final basis transform. In the ellipse, the separable source has exact Schmidt rank two and the evolution factors into two register unitaries. Generic<tbc>

\begin{tabular}{cccccccc}
Cross section & \(|\mathcal{E}_e|\) & \(\eta_\mathrm{s}\) & IPR & |S| & Krylov & top-\(|\hat{b}|\) & residual-greedy \\
Disk (integr.) & 249 & \(4.6\times 10^{-4}\) & 0.094 & 198 & \(1.2\times 10^{-1}\) & \(1.2\times 10^{-1}\) & \(5.4\times 10^{-2}\) \\
Ellipse _B<sub>e</sub>/A<sub>e</sub>_=0.6 (integr.) & 247 & \(4.5\times 10^{-4}\) & 0.165 & 186 & \(1.3\times 10^{-1}\) & \(1.8\times 10^{-1}\) & \(5.6\times 10^{-2}\) \\
Square (integr.) & 225 & \(5.9\times 10^{-5}\) & 0.147 & 117 & \(9.3\times 10^{-2}\) & \(8.5\times 10^{-2}\) & \(3.7\times 10^{-2}\) \\
Stadium (chaotic) & 240 & \(1.3\times 10^{-4}\) & 0.173 & 188 & \(1.1\times 10^{-1}\) & \(9.2\times 10^{-2}\) & \(5.4\times 10^{-2}\) \\
\end{tabular}

\begin{tabular}{cccc}
\(\epsilon\) & Lens \(120^\circ\) & Disk & Bound \\
10<sup>-3</sup> & \(6.8\times 10^{-4}\) & \(6.0\times 10^{-4}\) & \(1.0\times 10^{-3}\) \\
10<sup>-2</sup> & \(5.5\times 10^{-3}\) & \(6.4\times 10^{-3}\) & \(1.0\times 10^{-2}\) \\
\(5\times 10^{-2}\) & \(3.3\times 10^{-2}\) & \(3.0\times 10^{-2}\) & \(5.3\times 10^{-2}\) \\
\end{tabular}

** 12:** Cross sections of equal area by Brinkman penalization (\(32\times 32\) bounding box, \(\Gamma=100\), penalty 10<sup>4</sup>, multiscale heuristic, _M_=19200). IPR is the mean inverse participation ratio of the 40 lowest eigenvectors in the Fourier basis.

** 13:** Class I approximation: effect of a relative metric error \(\epsilon\) (\(32\times 32\), \(\Gamma=100\), fixed load). Largest observed relative energy-norm change over five samples versus the bound \(\epsilon/(1-\epsilon)\).

