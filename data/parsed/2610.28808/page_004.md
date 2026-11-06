<tbc>definition. Assume now that (2.4)-(2.7) hold at iteration \(\ell<n-k\) and CG has not terminated. The CG update for the linear system (2.3) gives

\(\widetilde{y}_{\ell+1}=\widetilde{y}_\ell+\frac{\widetilde{r}_\ell^\top\widetilde{r}_\ell}{\widetilde{p}_\ell^\top\overline{\Delta_k}\widetilde{p}_\ell}\widetilde{p}_\ell=\overline{Q_k^\top} z_\ell+\frac{\widehat{r}_\ell^\top\overline{Q_k}\overline{Q_k^\top}\widehat{r}_\ell}{\widehat{p}_\ell^\top\overline{Q_k}\overline{\Delta_k}\overline{Q_k^\top}\widehat{p}_\ell}\overline{Q_k^\top}\widehat{p}_\ell.\)

Since \(\widehat{r}_\ell\in\mathcal{R}(\overline{Q_k})\), then \(\overline{Q_k}\overline{Q_k^\top}\widehat{r}_\ell=\widehat{r}_\ell\). We get \(\widetilde{y}_{\ell+1}=\overline{Q_k^\top}\left(z_\ell+\frac{\widehat{r}_\ell^\top\widehat{r}_\ell}{\widehat{p}_\ell^\top\widehat{A}\widehat{p}_\ell}\widehat{p}_\ell\right)=\overline{Q_k^\top} z_{\ell+1}\). Using this identity, the reduced residual satisfies

\(\widetilde{r}_{\ell+1}=\overline{Q_k^\top\widehat{b}}-\overline{\Delta_k}\widetilde{y}_{\ell+1}=\overline{Q_k^\top}\left(\widehat{b}-\overline{Q_k}\overline{\Delta_k}\overline{Q_k^\top} z_{\ell+1}\right)=\overline{Q_k^\top}\left(\widehat{b}-\widehat{A}z_{\ell+1}\right)=\overline{Q_k^\top}\widehat{r}_{\ell+1},\)

where \(\widehat{r}_{\ell+1}\in\mathcal{R}(\widehat{A})\). For the search direction, from the CG recurrence, we get

\(\widetilde{p}_{\ell+1}=\widetilde{r}_{\ell+1}+\frac{\widetilde{r}_{\ell+1}^\top\widetilde{r}_{\ell+1}}{\widetilde{r}_\ell^\top\widetilde{r}_\ell}\widetilde{p}_\ell=\overline{Q_k^\top}\widehat{r}_{\ell+1}+\frac{\widehat{r}_{\ell+1}^\top\overline{Q_k}\overline{Q_k^\top}\widehat{r}_{\ell+1}}{\widehat{r}_\ell^\top\overline{Q_k}\overline{Q_k^\top}\widehat{r}_\ell}\overline{Q_k^\top}\widehat{p}_\ell\)<br>
\(=\overline{Q_k^\top}\left(\widehat{r}_{\ell+1}+\frac{\widehat{r}_{\ell+1}^\top\widehat{r}_{\ell+1}}{\widehat{r}_\ell^\top\widehat{r}_\ell}\widehat{p}_\ell\right)=\overline{Q_k^\top}\widehat{p}_{\ell+1}.\)

Since \(\widehat{p}_{\ell+1}\) is a linear combination of \(\widehat{p}_\ell\) and \(\widehat{r}_{\ell+1}\), it also belongs to \(\mathcal{R}(\widehat{A})\). Finally, \(Q_kQ_k^\top\widehat{p}_\ell=0\), so the null-space component of \(z_{\ell+1}\) remains equal to that of _z_<sub>0</sub>. This proves (2.7) and completes the induction. □

In exact arithmetic, CG finds the exact solution \(\widehat{y}^*\) of (2.3) in at most _n-k_ iterations. From (2.6) and (2.7), the corresponding final iterate for (2.2) is

(2.8) \(z^*=Q_kQ_k^\top z_0+\overline{Q_k}\overline{\Delta_k^{-1}}\overline{Q_k^\top\widehat{b}}.\)

The first term in (2.8) is the component of the initial vector _z_<sub>0</sub> in the null space of \(\widehat{A}\). By (2.7), in exact arithmetic, CG leaves it unchanged. The second term is the uniquely determined component in \(\mathcal{R}(\widehat{A})\) that solves the projected system (2.2). For completeness, we now express the energy norm of the deflated CG error.

Proposition 2.2. _Let_ \(1\le\ell\le n-k\)_. Assuming that the_ \(\ell\)_-th deflated CG iterate_ \(x_\ell^D\) _exists, the corresponding error satisfies_

\(\left\|x^*-x_\ell^D\right\|_A^2=min_{p\in\mathbb{P}_\ell(0)}\|p(\overline{\Delta_k})\left(\widetilde{y}^*-\widetilde{y}_0\right)\|_{\overline{\Delta_k}}^2=min_{p\in\mathbb{P}_\ell(0)}\|p(\overline{\Delta_k})\overline{Q_k^\top}\left(z^*-z_0\right)\|_{\overline{\Delta_k}}^2,\)

_where x_<sup>∗</sup> _represents the exact solution of Ax=b and_ \(\widetilde{y}_0=\overline{Q_k^\top} z_0\).

_Proof._ Applying (2.1) to both \(x_\ell^\mathrm{D}\) and the exact solution _x_<sup>∗</sup> (with \(z_\ell\) replaced by _z_<sup>∗</sup>), and using \(PAP^\top=PA=\overline{Q_k}\overline{\Delta_k}\overline{Q_k^\top}\) (see \[9\]) gives

\(\left\|x^*-x_\ell^\mathrm{D}\right\|_A^2=\left\|P^\top\left(z^*-z_\ell\right)\right\|_A^2=\left(z^*-z_\ell\right)^\top PAP^\top\left(z^*-z_\ell\right)\)<br>
\(=\left(z^*-z_\ell\right)^\top PA\left(z^*-z_\ell\right)\)<br>
\(=\left(z^*-z_\ell\right)^\top\overline{Q_k}\overline{\Delta_k}\overline{Q_k^\top}\left(z^*-z_\ell\right)\)<br>
\(=\left\|\overline{Q_k^\top}(z^*-z_\ell)\right\|_{\overline{\Delta_k}}^2=\left\|\widetilde{y}^*-\widetilde{y}_\ell\right\|_{\overline{\Delta_k}}^2.\)

