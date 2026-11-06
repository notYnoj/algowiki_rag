The algorithm proceeds as follows to update \(\sigma^\mathrm{in}\) to a new assignment \(\sigma^\mathrm{out}\in[q]^V\):

\(\bullet\) Set the truncation threshold:<tbc>

<tbc>\(M=1+\mathrm{log}\frac{4}{\varepsilon}.\)<tbc>

<tbc>Construct the LP on the _M_-truncated coupling tree \(\mathcal{T}=\mathcal{T}_M(\Phi,c_0)\), as described in Definition 5.6.<tbc>

\(\bullet\) Use binary search to find an interval \[_r_<sub>-</sub>_,r_<sub>+</sub>\] such that \(r_-\ge\frac{4+\varepsilon}{4+2\varepsilon}r_+\) and the LP remains feasible for parameters _r_<sub>-</sub> and _r_<sub>+</sub>. Let \(\left\{\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^X,\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^Y\right\}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in V(\mathcal{T})}\) be the corresponding LP feasible solution.<tbc>

\(\bullet\) Simulate the random process from Definition 5.12 using the feasible solution obtained above, replacing the random assignment \(\mathfrak{X}^\mathrm{lp}\) (used as the random seed for the process) with \(\sigma^\mathrm{in}\). Let \((\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in\mathcal{L}\) be the random leaf reached by this process.<tbc>

\(\bullet\) If the leaf node \((\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\notin\mathcal{L}_\mathrm{coup}\), then set \(\sigma^\mathrm{out}\in[q]^V\) to be an arbitrary satisfying assignment of \(\Phi\). Otherwise, update \(\sigma^\mathrm{in}\) by modifying the assigned variables according to \(\tau\), i.e., set \(\sigma^\mathrm{out}\leftarrow\tau\wedge\sigma_{V\backslash\Lambda(\tau)}^\mathrm{in}\).

We will prove the following lemma, which shows that the new sample produced by the dynamic sampler approximates the target distribution \(\mu_\mathcal{C}\).

**Lemma 5.16.** _Assume Condition 3.1 and that_ \(\sigma^\mathrm{in}\sim\mu_{\mathcal{C}\backslash\{c_0\}}\)_. Then, the assignment_ \(\sigma^\mathrm{out}\) _produced by the dynamic sampler in Definition 5.15 follows a distribution_ \(\mu^\mathrm{out}\) _that satisfies_

\(d_\mathrm{TV}(\mu^\mathrm{out},\mu_\mathcal{C})\le\varepsilon.\)

With Lemma 5.16, we can complete the proof of Theorem 3.2.

_Proof of the sampling part of Theorem 3.2._ Let C={_c_<sub>1</sub>_,c_<sub>2</sub>_,...,c<sub>m</sub>_}. Note that \(km=n\alpha\). For each \(0\le i\le m\), define C_<sub>i</sub>_={_c_<sub>1</sub>_,c_<sub>2</sub>_,...,c<sub>i</sub>_}, \(\Phi_i=(V,[q],\mathcal{C}_i)\) and let \(\mu_{\Phi_i}\) denote the uniform distribution over satisfying assignments of \(\Phi_i\). Let \(\sigma_0,\sigma_1,\dots,\sigma_m\in[q]^V\) be constricted as follows:

\(\bullet\) Sample \(\sigma_0\sim\mathcal{P}\), the uniform product distribution.<tbc>

\(\bullet\) For each \(1\le i\le m\), use the dynamic sampler from Definition 5.15 to generate \(\sigma_i\) from \(\sigma_{i-1}\), with the input formula \(\Phi_i=(V,[q],\mathcal{C}_i)\), input constraint _c<sub>i</sub>_, error bound \(\frac{\varepsilon}{m}\), and current sample \(\sigma_{i-1}\). If \(\sigma_i\) is not a solution to \(\Phi_i\) at any step \(0\le i\le m\), output an arbitrary final assignment instead.

By applying induction along with Lemma 5.16, we can verify that for each \(0\le i\le m\), the distribution \(\mu_i\) of \(\sigma_i\) satisfies

\(d_\mathrm{TV}(\mu_i,\mu_{\mathcal{C}_i})\le\frac{i}{m}\cdot\varepsilon.\)

The total running time is bounded by \(O\left(\left(\frac{n}{\varepsilon}\right)^{\mathrm{poly}(k,\mathrm{log}q.\alpha)}\right)\) according to Proposition 5.8, which accounts for the overhead of building and solving the linear program. Thus, the theorem is proved. □

We then finish this section by proving Lemma 5.16.

_Proof of Lemma 5.16._ According to Definition 5.15 and Lemma 5.13, for each \(y\in\Omega^\mathcal{C}\), we have

\(\mathbf{Pr}\left[\sigma^\mathrm{out}=y\right]=\sum_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in\mathcal{L}_\mathrm{coup}\text{with}\mathcal{F}\wedge\tau\text{satisfied by}y}\mu_{\mathcal{C}\backslash\{c_0\}}(\mathcal{E}\wedge\sigma)\cdot\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^X\cdot\frac{1}{|\Omega^{\mathcal{E}\wedge\sigma}|}\)<br>
\(\ge r_-\cdot\sum_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in\mathcal{L}_\mathrm{coup}\text{with}\mathcal{F}\wedge\tau\text{satisfied by}y}\mu_{\mathcal{C}\backslash\{c_0\}}(\mathcal{E}\wedge\sigma)\cdot\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^Y\cdot\frac{1}{|\Omega^{\mathcal{E}\wedge\sigma}|}\)<br>
\(=r_-\cdot\frac{1}{|\Omega^{\mathcal{C}\backslash\{c_0\}}|}\cdot\sum_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in\mathcal{L}_\mathrm{coup}\text{with}\mathcal{F}\wedge\tau\text{satisfied by}y}\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^Y.\)

