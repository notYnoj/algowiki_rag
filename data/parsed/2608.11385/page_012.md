## 2.3 Hardness of exponentially precise additive approximation

Recalling the setting of Theorem 1.2 let

\(F_G(\phi):=\langle\psi_p(\phi)|C_G|\psi_p(\phi)\rangle,\) (34)

where \(|\psi_p(\phi)\rangle\) is the single-parameter depth-_p_ QAOA state with \(\gamma_1=\gamma_2=\phi,\beta_1=\mathrm{arctan}(1/2),\beta_2=\pi/4\), and all other angles fixed \(\gamma_j=\beta_j=0\). We show that exponentially small evaluation errors still allow exact recovery of the number of optimal cuts.

**Corollary 2.8** (Exponentially precise additive evaluation)**.** _Fix_ \(p\ge 2\) _and the mixer angle choices of Theorem 1.2. There exists a constant_ \(\alpha>0\) _such that the following problem is #P-hard under deterministic polynomial-time Turing reductions: given an N-vertex MaxCut instance from the family constructed in the proof and a tied phase angle specified by the exact algebraic input_ \(z=e^{\mathrm{i}\phi}\)_, return a rational number_ \(\widetilde{F}_G(\phi)\) _satisfying_

\(\left|\widetilde{F}_G(\phi)-F_G(\phi)\right|\le 2^{-\alpha N}.\)

_The same statement holds for the designated correlator_ \(\langle Z_rZ_s\rangle\).

_Proof._ Write

\(F_G(z)=\sum_{k=-D}^Da_kz^k,z=e^{\mathrm{i}\phi}.\)

Evaluate the approximation oracle at _M\>_2_D_ distinct _M_-th roots of unity and apply the normalized inverse discrete Fourier transform. If every oracle value has additive error at most \(\varepsilon\), then every recovered Laurent coefficient has additive error at most \(\varepsilon\). Indeed, each coefficient error is an average of the oracle errors multiplied by phase factors of unit magnitude. Its magnitude is therefore at most \(M^{-1}\sum_{j=0}^{M-1}|\delta_j|\le\varepsilon\) by the triangle inequality, where \(\delta_j\) is the error in the _j_th oracle value. For the mixer angle choice \(\mathrm{tan}\beta=1/2\), write \(c_\beta=\mathrm{cos}\beta=\frac{2}{\sqrt{5}}\) and \(s_\beta=\mathrm{sin}\beta=\frac{1}{\sqrt{5}}\), and define

\(\kappa_N:=-2^{1-N}c_\beta^{N/2}(\mathrm{i}s_\beta)^{N/2}\left[c_\beta^N+(-\mathrm{i}s_\beta)^N\right].\)

This is the factor multiplying |#MC(_G_)| in (27).

By Eq. (30) and Theorem 2.4, for the coefficient of _z_<sup>_D<sub>⋆</sub>_</sup> in _F<sub>G</sub>(z_) we may write

\(a_{D_\star}=-\frac{1}{2}\kappa_N|\#\mathrm{MC}(G)|=-\kappa_N|\#\mathrm{MC}(H)|.\)

Then \(|\kappa_N|\) is bounded from below (cf. Eq. (27)) by

\(2^{1-N}(c_\beta s_\beta)^{N/2}\left|c_\beta^N+(-is_\beta)^N\right|\ge 2^{1-N}\left(\frac{2}{5}\right)^{N/2}\left(c_\beta^N-s_\beta^N\right)\)<br>
\(=2^{1-N}\left(\frac{2}{5}\right)^{N/2}\frac{2^N-1}{5^{N/2}}\)<br>
\(\ge\left(\frac{\sqrt{2}}{5}\right)^N=2^{-N\mathrm{log}_2(5/\sqrt{2})}.\) (35)

Here we used the triangle inequality and \(2^N-1\ge 2^{N-1}\). Hence \(|\kappa_N|\ge 2^{-\alpha_0N}\) for \(\alpha_0:=\mathrm{log}_2(5/\sqrt{2})\).

Set \(b_N:=\left\lceil\alpha_0N\right\rceil+2\). Any oracle request with precision \(b\ge b_N\) has absolute error at most<tbc>

\(\varepsilon\le 2^{-b}\le 2^{-b_N}\le\frac{1}{4}2^{-\alpha_0N}\le|\kappa_N|/4.\)

