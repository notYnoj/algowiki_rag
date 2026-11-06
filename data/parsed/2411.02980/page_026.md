_Proof._ We prove the lemma by structural induction in the top-down manner. The induction basis is the root node \((\mathcal{C}\backslash\{c_0\},\mathcal{C},\varnothing,\varnothing,\emptyset,\varnothing)\), where the lemma follows easily from Definition 5.12.

For the induction step, we only consider the case when \(\mathcal{F}^\tau\unknown\in\mathcal{E}^\sigma\), as the complementary case with \(\mathcal{F}^\tau\subseteq\mathcal{E}^\sigma\) is straightforward. Let _c_ be the smallest constraint in \(\mathcal{F}^\tau\backslash\mathcal{E}^\sigma\). We have the following cases:

\(\bullet\) **Case 1**: _c_ is satisfied by Xlp. The process transitions to \((\mathcal{E}\cup\{c\},\mathcal{F},\sigma,\tau,T,\varsigma)\). By the induction hypothesis, we know that \(\mathfrak{X}^\mathrm{lp}\sim\mu_\mathcal{E}^\sigma\). Therefore, the event that _c_ is satisfied by Xlp occurs with probability \(\mu_\mathcal{E}^\sigma(c)\). Consequently, we have<tbc>

\(\text{\textbf{Pr}}\left[(\mathcal{E}\cup\{c\},\mathcal{F},\sigma,\tau,T,\varsigma)\in P^\mathrm{lp}\right]\)<br>
\(\text{(by Definition 5.12)}=\text{\textbf{Pr}}\left[(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in P^\mathrm{lp}\right]\cdot\mu_\mathcal{E}^\sigma(c)\)<br>
\(\text{(by I.H.)}=\mu_{\mathcal{C}\backslash\{c_0\}}(\mathcal{E}\wedge\sigma)\cdot\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^X\cdot\mu_\mathcal{E}^\sigma(c)\)<br>
\(\text{(by the chain rule)}=\mu_{\mathcal{C}\backslash\{c_0\}}((\mathcal{E}\cup\{c\})\wedge\sigma)\cdot\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^X.\)

Additionally, conditioning on moving to \((\mathcal{E}\cup\{c\},\mathcal{F},\sigma,\tau,T,\varsigma)\), it follows that<tbc>

<tbc>\(\mathfrak{X}^\mathrm{lp}\sim\mu_{\mathcal{E}\cup\{c\}}^\sigma,\)<tbc>

<tbc>thus completing the proof of this case.<tbc>

\(\bullet\) **Case 2**: _c_ is violated by Xlp. Let \(\pi=\mathfrak{X}_{\mathrm{vbl}(c)}^\mathrm{lp}\), then we have \(\pi=\mathtt{False}(c)\). By the induction hypothesis, we know that \(\mathfrak{X}^\mathrm{lp}\sim\mu_\mathcal{E}^\sigma\). Therefore, the event that _c_ is violated by Xlp occurs with probability<tbc>

<tbc>\(\mu_\mathcal{E}^\sigma(\neg c)=\mu_\mathcal{E}^\sigma(\pi).\)<tbc>

<tbc>In this case, for each \(\rho\in[q]^{\mathrm{vbl}(c)}\), the process transitions to \((\mathcal{E},\mathcal{F},\sigma\wedge\pi,\tau\wedge\rho,T\oplus c^O,\varsigma\wedge\rho)\) with probability \(\frac{\hat{p}_{(\mathcal{E},\mathcal{F},\sigma\wedge\pi,\tau\wedge\rho,T\oplus c^O,\varsigma\wedge\rho)}^X}{\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^X}\). Therefore, for each \(\rho\in[q]^{\mathrm{vbl}(c)}\), we have<tbc>

\(\text{\textbf{Pr}}\left[(\mathcal{E},\mathcal{F},\sigma\wedge\pi,\tau\wedge\rho,T\oplus c^O,\varsigma\wedge\rho)\in P^\mathrm{lp}\right]\)<br>
\(\text{(by Definition 5.12)}=\text{\textbf{Pr}}\left[(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in P^\mathrm{lp}\right]\cdot\mu_\mathcal{E}^\sigma(\pi)\cdot\frac{\hat{p}_{(\mathcal{E},\mathcal{F},\sigma\wedge\pi,\tau\wedge\rho,T\oplus c^O,\varsigma\wedge\rho)}^X}{\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^X}\)<br>
\(\text{(by I.H.)}=\mu_{\mathcal{C}\backslash\{c_0\}}(\mathcal{E}\wedge\sigma)\cdot\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^X\cdot\mu_\mathcal{E}^\sigma(\pi)\cdot\frac{\hat{p}_{(\mathcal{E},\mathcal{F},\sigma\wedge\pi,\tau\wedge\rho,T\oplus c^O,\varsigma\wedge\rho)}^X}{\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^X}\)<br>
\(\text{(by the chain rule)}=\mu_{\mathcal{C}\backslash\{c_0\}}(\mathcal{E}\wedge\sigma\wedge\pi)\cdot\hat{p}_{(\mathcal{E},\mathcal{F},\sigma\wedge\pi,\tau\wedge\rho,T\oplus c^O,\varsigma\wedge\rho)}^X.\)

This concludes the proof for the case when \(\mathcal{F}^\tau\unknown\in\mathcal{E}^\sigma\). As we discussed earlier, it proves the lemma. □

The following corollary follows from Lemma 5.13 by the definition of conditional probability.

**Corollary 5.14.** _Assume_ \(\Phi\) _is satisfiable. For each_ \(x\in\Omega^{\mathcal{C}\backslash\{c_0\}}\) _and each_ \((\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in V(\mathcal{T})\),<tbc>

\(\text{\textbf{Pr}}\left[(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in P^\mathrm{lp}|\mathfrak{X}^\mathrm{lp}=x\right]=\left\{\begin{array}{ c c }
0 & \text{\textit{if}}x\notin\Omega^{\mathcal{E}\wedge\sigma}, \\
\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^X & \text{\textit{if}}x\in\Omega^{\mathcal{E}\wedge\sigma}.
\end{array}\right.\)

<tbc>_Proof._ For each \(x\in\Omega\) and each \((\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in V(\mathcal{T})\), we have

\(\text{\textbf{Pr}}\left[(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in P^\mathrm{lp}|\mathfrak{X}^\mathrm{lp}=x\right]=\frac{\text{\textbf{Pr}}\left[(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in P^\mathrm{lp}\wedge\mathfrak{X}^\mathrm{lp}=x\right]}{\text{\textbf{Pr}}\left[\mathfrak{X}^\mathrm{lp}=x\right]}\) (13)

\(\text{(by Definition 5.12)}=|\Omega^{\mathcal{C}\backslash\{c_0\}}|\cdot\text{\textbf{Pr}}\left[(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in P^\mathrm{lp}\wedge\mathfrak{X}^\mathrm{lp}=x\right].\)

If \(x\notin\Omega^{\mathcal{E}\wedge\sigma}\), then by Lemma 5.13, the above expression equals 0. Therefore, we assume \(x\in\Omega^{\mathcal{E}\wedge\sigma}\). By Lemma 5.13, conditioning on the event \((\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\), the distribution of \(\sigma\) is uniform over all<tbc>

