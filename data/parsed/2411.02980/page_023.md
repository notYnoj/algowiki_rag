## 5.3.1. _Performance of the LP._

First, we show that the feasibility of the LP can be checked efficiently.

**Proposition 5.8.** _Assume Condition 3.1. For any_ \(0\le r_-\le r_+\)_, the feasibility of the linear program in Definition 5.6 can be determined within_ \(\mathrm{exp}(M\cdot\mathrm{poly}(k,\mathrm{log}q,\alpha))\) _time._

This result follows directly from Proposition 5.5, as the size of the linear program is bounded by the size of the _M_-truncated coupling tree \(\mathcal{T}=\mathcal{T}_M(\Phi,c_0)\), which is at most \(\mathrm{exp}(M\cdot\mathrm{poly}(k,\mathrm{log}q,\alpha))\) according to the bound on maximum degree (Property 3.4) in Condition 3.1.

Next, we prove the soundness of this linear program by showing that the true values of the marginal probabilities satisfy all the linear constraints.

**Lemma 5.9.** _Assume_ \(\Phi\) _is satisfiable. The linear program in Definition 5.6 is feasible for_<tbc>

\(r_-=r_+=\frac{|\Omega^{\mathcal{C}\backslash\{c_0\}}|}{|\Omega^\mathcal{C}|}.\)

<tbc>_Proof._ For each \((\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in V(\mathcal{T})\), we define the following quantities:

(10) \(\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^X=\mu_\mathcal{C}(\mathcal{F}\wedge\tau),\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^Y=\mu_{\mathcal{C}\backslash\{c_0\}}(\mathcal{E}\wedge\sigma).\)

We will show that they form a feasible solution to the LP described in Definition 5.6 with the parameters \(r_-=r_+=\frac{|\Omega^{\mathcal{C}\backslash\{c_0\}}|}{|\Omega^\mathcal{C}|}\) . By Proposition 5.2, these quantities in (10) are consistent with the actual values of \(p_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^X,p_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^Y\) as defined in Definition 5.1, also extending these marginal probabilities to all nodes in _V_(T) rather than just V<sup>cp</sup>. Note that compared to V<sup>cp</sup>, which contains only those \((\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\) corresponding to the final outcomes of the _M_-truncated coupling procedure, the set _V_(T) also contains all \((\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\) corresponding to the intermediate steps of the coupling.

We then verify that (10) satisfies all linear constraints of the LP in Definition 5.1:

\(\bullet\) _Range and Non-leaf constraints_: These constraints hold by Items 1 and 2 of Proposition 5.3.<tbc>

\(\bullet\) _Leaf constraints_: Item III.b is a direct consequence of (10). To verify Item III.a, note that for \((\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in\mathcal{L}_\mathrm{coup}\), we have \(\mathcal{E}^\sigma=\mathcal{F}^\tau\), which implies that \(|\Omega^{\mathcal{E}\wedge\sigma}|=|\Omega^{\mathcal{F}\wedge\tau}|\). Thus:<tbc>

- If \(|\Omega^{\mathcal{E}\wedge\sigma}|=|\Omega^{\mathcal{F}\wedge\tau}|>0\), then Item III.a follows directly from Item 3 of Proposition 5.3.<tbc>

**-** If \(|\Omega^{\mathcal{E}\wedge\sigma}|=|\Omega^{\mathcal{F}\wedge\tau}|=0\), then \(\mu_\mathcal{C}(\mathcal{F}\wedge\tau)=\mu_{\mathcal{C}\backslash\{c_0\}}(\mathcal{E}\wedge\sigma)=0\) and Item III.a holds.<tbc>

\(\bullet\) _Truncation constraints_: The constraints in Item IV. hold by Item 3 of Proposition 5.3. □

At last, we show that the feasibility of the linear program implies that _r_<sub>-</sub> and _r_<sub>+</sub> provide respective lower and upper bounds for \(\frac{|\Omega^{\mathcal{C}\backslash\{c_0\}}|}{|\Omega^\mathcal{C}|}\) with bounded multiplicative error. With this, we can apply a binary search to approximate the true value of \(\frac{|\Omega^{\mathcal{C}\backslash\{c_0\}}|}{|\Omega^\mathcal{C}|}\) .

**Lemma 5.10.** _Assume Condition 3.1. If the LP in Definition 5.6 is feasible for parameters_ \(0\le r_-\le r_+\)_, then it holds that_

\(\left(1-2\cdot 2^{-M}\right)r_-\le\frac{|\Omega^{\mathcal{C}\backslash\{c_0\}}|}{|\Omega^\mathcal{C}|}\le\left(1+2\cdot 2^{-M}\right)r_+.\)

The proof of Lemma 5.10 relies on the following claim, which provides an upper bound on the estimated average marginal probabilities for truncated nodes of the coupling tree.

**Claim 5.11.** _Assume Condition 3.1. The following hold for the solution of the LP in Definition 5.6:_

\(\frac{1}{|\Omega^{\mathcal{C}\backslash\{c_0\}}|}\sum_{x\in\Omega^{\mathcal{C}\backslash\{c_0\}}}\sum_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in\mathcal{L}_\mathrm{run}\text{\textit{with}}\mathcal{E}\wedge\sigma\text{\textit{satisfied by}}x}\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^X\le 2^{-M},\)<br>
\(\frac{1}{|\Omega^\mathcal{C}|}\sum_{y\in\Omega^\mathcal{C}}\sum_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in\mathcal{L}_\mathrm{run}\text{\textit{with}}\mathcal{F}\wedge\tau\text{\textit{satisfied by}}y}\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^Y\le 2^{-M}.\)

Assuming this claim holds, Lemma 5.10 can be proved using the same argument as in the proof of \[WY24, Lemma 4.11\]. For completeness, we provide the proof here.

