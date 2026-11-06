<tbc>assignments in \(\Omega^{\mathcal{E}\wedge\sigma}\). Thus, we have

\(\mathbf{Pr}\left[(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in P^\mathrm{lp}\wedge\mathfrak{X}^\mathrm{lp}=x\right]=\mathbf{Pr}\left[(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in P^\mathrm{lp}\right]\cdot\frac{1}{|\Omega^{\mathcal{E}\wedge\sigma}|}\)<br>
\(=\frac{|\Omega^{\mathcal{E}\wedge\sigma}|}{|\Omega^{\mathcal{C}\backslash\{c_0\}}|}\cdot\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^X\cdot\frac{1}{|\Omega^{\mathcal{E}\wedge\sigma}|}\)<br>
\(=\frac{1}{|\Omega^{\mathcal{C}\backslash\{c_0\}}|}\cdot\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^X,\)

combining this with (13) completes the proof of the corollary. □

We are now ready to prove Claim 5.11.

_Proof of Claim 5.11._ We will prove the first inequality; the second inequality can be proved by following a similar approach.

First, we verify the following identity:

\(\frac{1}{|\Omega^{\mathcal{C}\backslash\{c_0\}}|}\sum_{x\in\Omega^{\mathcal{C}\backslash\{c_0\}}}\sum_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in\mathcal{L}_\mathrm{trunc}\text{with}\mathcal{E}\wedge\sigma\text{satisfied by}x}\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^X\)<br>
\(=\sum_{x\in\Omega^{\mathcal{C}\backslash\{c_0\}}}\sum_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in\mathcal{L}_\mathrm{trunc}\text{with}\mathcal{E}\wedge\sigma\text{satisfied by}x}\frac{\mathbf{Pr}\left[(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in P^\mathrm{lp}\right]}{|\Omega^{\mathcal{E}\wedge\sigma}|}\)<br>
\(=\sum_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in\mathcal{L}_\mathrm{trunc}}\mathbf{Pr}\left[(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in P^\mathrm{lp}\right],\)

where the first equality follows from Lemma 5.13 and the fact that for each \((\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in V(\mathcal{T})\), any assignment **_x_** that satisfies \(\mathcal{E}\wedge\sigma\) must also satisfy C\\{_c_<sub>0</sub>}. The second equality follows from this same fact and the exchange of the order of summation.

Combining these results, we have the following:

\(\sum_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in\mathcal{L}_\mathrm{trunc}}\mathbf{Pr}\left[(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in P^\mathrm{lp}\right]\)<br>
\(\le\sum_{T^\prime\in\mathbb{T}_M^{c_0}}\sum_{\varsigma^\prime\in[q]^\mathrm{vbl}(T^\prime)}\sum_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in P^\mathrm{lp}T=T^\prime\wedge\varsigma=\varsigma^\prime}\mathbf{Pr}\left[(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in P^\mathrm{lp}\right]\)<br>
\(\le\sum_{T^\prime\in\mathbb{T}_M^{c_0}}\sum_{\varsigma^\prime\in[q]^\mathrm{vbl}(T^\prime)}\sum_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in P^\mathrm{lp}T=T^\prime\wedge\varsigma=\varsigma^\prime}\sum_{x\in\Omega^{\mathcal{E}\wedge\sigma}}\mathbf{Pr}\left[\mathfrak{X}^\mathrm{lp}=x\right]\cdot\mathbf{Pr}\left[(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in P^\mathrm{lp}|\mathfrak{X}^\mathrm{lp}=x\right]\)<br>
\(=\sum_{T^\prime\in\mathbb{T}_M^{c_0}}\sum_{\varsigma^\prime\in[q]^\mathrm{vbl}(T^\prime)}\sum_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in P^\mathrm{lp}T=T^\prime\wedge\varsigma=\varsigma^\prime}\sum_{x\in\Omega^{\mathcal{E}\wedge\sigma}}\mathbf{Pr}\left[\mathfrak{X}^\mathrm{lp}=x\right]\cdot\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^X.\)

Here, the last equality follows directly from Corollary 5.14.

Note that by Lemma 4.7, fixing the witness tree _T_ and the witness assignment \(\varsigma\) uniquely identifies a node \((\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in P^\mathrm{lp}\) satisfying \(T=T'\wedge\varsigma=\varsigma'\). We then denote this unique node as \(N(T',\sigma')\), and the partial assignment \(\sigma\) in this unique node as \(\sigma(T',\varsigma')\). Therefore, we further have

