## C Proofs for Section 3 (1-bit BAI algorithm and upper bound)

### C.1 Fixed clipping: proof of Theorem 8

This subsection proves the sample complexity upper bound of the fixed-clipping algorithm. We first establish a high-probability event on which all fixed-clipping confidence intervals are valid uniformly over time (Lemma 19). On this event, the interval stopping rule can only return an \(\varepsilon\)-optimal arm (Lemma 20). It remains to control the number of samples. The key structural step is Lemma 22: whenever the algorithm samples arm _k_, its stochastic radius must still be larger than a constant fraction of the effective gap. Solving this inequality gives an arm-wise pull bound, and summing these bounds over arms yields the stated sample complexity (Lemma 23).

Throughout this subsection, fix<tbc>

\(L_\varepsilon=\frac{2\sigma^2}{\varepsilon},\alpha_\varepsilon=1+log\frac{2\sigma}{\varepsilon},\gamma=\frac{\delta}{K}.\)

<tbc>For the fixed-clipping algorithm, write

\(\beta_\varepsilon(n,\gamma)=\frac{\varepsilon}{4}+2\sqrt{\frac{3\alpha_\varepsilon\sigma^2x_n(\gamma)}{n}}+\frac{2\alpha_\varepsilon\sigma^2x_n(\gamma)}{n\varepsilon},r_\varepsilon(n,\gamma):=\beta_\varepsilon(n,\gamma)-\frac{\varepsilon}{4}.\)

Let _Z_<sub>_k,_1</sub>_,Z_<sub>_k,_2</sub>_,..._ be i.i.d. copies of the estimator, each built from an independent reward sample and independent internal randomization of arm _k_.

At a generic round, let _N<sub>k</sub>_ denote the number of 1-bit queries already made to arm _k_, and let

\(\widehat{\mu}_k=c_k+\frac{1}{N_k}\sum_{i=1}^{N_k}Z_{k,i},\mathrm{LCB}_k=\widehat{\mu}_k-\beta_\varepsilon(N_k,\gamma),\mathrm{UCB}_k=\widehat{\mu}_k+\beta_\varepsilon(N_k,\gamma).\)

**Lemma 19** (Fixed-clipping good event)**.** _With probability at least_ \(1-\delta\),

\(\mathcal{E}_\mathrm{fix}:=\cap_{k=1}^K\cap_{n\ge 1}\{|\widehat{\mu}_k(n)-\mu_k|\le\beta_\varepsilon(n,\delta/K)\}\)

_holds throughout_ FIXEDCLIP-1BITBAI.

_Proof._ For a fixed arm _k_, the samples used by its tail-integral estimator are i.i.d. when indexed by the local count _n_, regardless of the adaptive times at which arm _k_ is selected. Applying Theorem 5 with clipping level \(L_\varepsilon\) and failure probability \(\delta/K\) gives

\(\mathrm{Pr}\left(\forall n\ge 1,|\widehat{\mu}_k(n)-\mu_k|\le\beta_\varepsilon(n,\delta/K)\right)\ge 1-\frac{\delta}{K}.\)

Taking a union bound over \(k\in[K]\) yields

\(\mathrm{Pr}(\mathcal{E}_\mathrm{fix})\ge 1-\sum_{k=1}^K\frac{\delta}{K}=1-\delta.\)

The time-uniformity over _n_ is what makes the event valid under the adaptive sampling rule.

**Lemma 20** (Fixed-clipping stopping correctness)**.** _On_ E<sub>fix</sub>_, if_ FIXEDCLIP-1BITBAI _stops and returns_ \(\widehat{k}\)_, then_<tbc>

\(\mu_\widehat{k}\ge\mu^\star-\varepsilon.\)

<tbc>_Proof._ Let _h_ be the arm returned by the algorithm. The stopping rule gives<tbc>

\(B_h=\mathrm{max}_{\ell\neq h}\mathrm{UCB}_\ell-\mathrm{LCB}_h\le\varepsilon.\)

<tbc>Equivalently, for every \(\ell\neq h\),<tbc>

\(\mathrm{UCB}_\ell-\mathrm{LCB}_h\le\varepsilon.\)

