\(\sum_{T^\prime\in\mathbb{T}_M^{c_0}}\sum_{\varsigma^\prime\in[q]^{\text{vbl}(T^\prime)}}\sum_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in P^\text{lp}}\sum_{x\in\Omega^{\mathcal{E}\wedge\sigma} T=T^\prime\wedge\varsigma=\varsigma^\prime}\mathbf{Pr}\left[\mathfrak{X}^\text{lp}=x\right]\cdot\hat{p}_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^X\)<br>
\((\star)\le\sum_{T^\prime\in\mathbb{T}_M^{c_0}}\sum_{\varsigma^\prime\in[q]^{\text{vbl}(T^\prime)}}\mathbf{Pr}\left[\mathfrak{X}_{\text{vbl}(T^\prime)}^\text{lp}=\sigma(T',\varsigma')\right]\cdot\hat{p}_{N(T^\prime,\sigma^\prime)}^X\)<br>
\((\blacktriangle)\le\sum_{T^\prime\in\mathbb{T}_M^{c_0}}\sum_{\varsigma^\prime\in[q]^{\text{vbl}(T^\prime)}}\mathbf{Pr}\left[\mathfrak{X}_{\text{vbl}(T^\prime)}^\text{lp}=\sigma(T',\varsigma')\right]\cdot q^{-|\text{vbl}(T^\prime)\cap V_\text{good}|}\cdot\left(1-\mathrm{e}q^{-(1-\varepsilon_1)}k\right)^{-|\text{vbl}(T^\prime)|p_1\alpha}\)<br>
\((\blacksquare)\le\sum_{T^\prime\in\mathbb{T}_M^{c_0}}\sum_{\varsigma^\prime\in[q]^{\text{vbl}(T^\prime)}}q^{-2|\text{vbl}(T^\prime)\cap V_\text{good}|}\cdot\left(1-\mathrm{e}q^{-(1-\varepsilon_1)}k\right)^{-2|\text{vbl}(T^\prime)|p_1\alpha}\)<br>
\((\text{15})\le\sum_{T^\prime\in\mathbb{T}_M^{c_0}}q^{|\text{vbl}(T^\prime)|}\cdot q^{-2|\text{vbl}(T^\prime)\cap V_\text{good}|}\cdot\left(1-\mathrm{e}q^{-(1-\varepsilon_1)}k\right)^{-2|\text{vbl}(T^\prime)|p_1\alpha}\)<br>
\((\triangle)\le 2^{-M}.\)

The (⋆) inequality is derived using the argument above. The (\(\blacktriangle\)) inequality follows from Item IV. of Definition 5.6. The (\(\blacksquare\)) inequality follows from Lemma 4.11. Finally, the \((\triangle)\) inequality holds for the chosen parameters in Condition 3.1 and was already established in the proof of Theorem 4.1; in particular, (15) is exactly (7) and hence the same proof applies. □

## 5.4. Sampling and counting via linear programming.

In this subsection, we apply the linear program in Definition 5.6 to derive sampling and counting algorithms and prove Theorem 3.2. The proofs essentially follow those in \[WY24, Section 5\], and we include for completeness.

We begin with the counting algorithm, which directly follows from the analysis of the linear program presented in the previous subsection.

_Proof of the counting part of Theorem 3.2._ Let C={_c_<sub>1</sub>_,c_<sub>2</sub>_,...,c<sub>m</sub>_}. Note that \(km=n\alpha\). For each \(0\le i\le m\), define C_<sub>i</sub>_={_c_<sub>1</sub>_,c_<sub>2</sub>_,...,c<sub>i</sub>_}, \(\Phi_i=(V,[q],\mathcal{C}_i)\). In particular, \(\Phi_m=\Phi\). By applying a _constraint-wise self-reduction_, we decompose \(Z(\Phi_m)\) into the following telescopic product:

(16) \(Z(\Phi_m)=Z(\Phi_0)\cdot\frac{Z(\Phi_m)}{Z(\Phi_0)}=Z(\Phi_0)\cdot\prod_{i=1}^m\frac{Z(\Phi_i)}{Z(\Phi_{i-1})}.\)

Note that \(\Phi_0\) is a trivial CSP formula, so \(Z_{\Phi_0}=q^{|V|}\). Moreover, and crucially, observe that each \(\Phi_i\) satisfies Condition 3.1 for \(0\le i\le m\), assuming the original CSP formula \(\Phi\) satisfies Condition 3.1. Setting:

\(M=1+\mathrm{log}\frac{4m}{\varepsilon},\)

we use the LP in Definition 5.6 with binary search to approximate each ratio \(\frac{Z(\Phi_i)}{Z(\Phi_{i-1})}=\frac{|\Omega^{\mathcal{C}_i}|}{|\Omega^{\mathcal{C}_{i-1}}|}\) within a multiplicative error of \(\frac{\varepsilon}{4m}\). According to Proposition 5.8 and lemmas 5.9 and 5.10, this can be done in time \(O\left(\left(\frac{n}{\varepsilon}\right)^{\text{poly}(k,\mathrm{log}q.\alpha)}\right)\). Therefore, we obtain an estimate of \(Z(\Phi)=Z(\Phi_m)\) within a total multiplicative error of \(\varepsilon\) in time \(O\left(\left(\frac{n}{\varepsilon}\right)^{\text{poly}(k,\mathrm{log}q.\alpha)}\right)\), as required. □

For the sampling part, we establish a constraint-wise self-reduction for sampling by constructing a _dynamic sampler_. Given an atomic CSP formula \(\Phi=(V,[q],\mathcal{C})\) and a constraint \(c\in\mathcal{C}\backslash\{c_0\}\), it dynamically updates a current sample \(\sigma^\text{in}\sim\mu_{\mathcal{C}\backslash\{c_0\}}\) to a new sample \(\sigma^\text{out}\sim\mu_\mathcal{C}\). This dynamic sampler is derived from the random process in Definition 5.12, which was initially introduced to analyze the linear program.

**Definition 5.15** (dynamic sampler)**.** The algorithm takes as input a CSP \(\Phi=(V,[q],\mathcal{C})\), a constraint \(c_0\in\mathcal{C}\), and an error bound \(\varepsilon\in(0,1)\). Additionally, the algorithm is also given access to an assignment \(\sigma^\text{in}\in[q]^V\) that satisfies \(\Phi^{c_0}=(V,[q],\mathcal{C}\backslash\{c_0\})\).

