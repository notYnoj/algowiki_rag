the admissible assignments for the remaining variables. The family C is just the collection of these derived local constraints, so any assignment to the parity coordinates satisfies the CSP instance precisely when it extends _m_ to a full codeword in _C_.

**Definition 3.2.** For a systematic LTC _C_, we define an optimization problem MaxCSP(_C_) as follows. The input is a message \(m\in\Sigma^k\), and the goal is to compute an assignment in \(\Sigma^V\) that maximizes the number of satisfied constraints in I_<sub>C</sub>(m_).

Notice that all constraints in I_<sub>C</sub>(m_) can be satisfied by assigning the code bits of _f(m_) to the variables.

Throughout this section we reuse the convention from the introduction: for any approximate algorithm A for MaxCSP(_C_) we define the randomized map

\(\tilde{\mathcal{A}}(\mathcal{I}_C(m)):=(m,\mathcal{A}(\mathcal{I}_C(m)))\)

which simply pairs the input message with the assignment returned by A.

## 3.2 Nearest-Message Decoder

We collect here the decoder and stability statements that connect near-optimal assignments to nearby codewords.

**Definition 3.3.** Let \(\sigma:\Sigma^n\rightarrow\Sigma^k\) be the _nearest-message decoder_ for (_C,f_), that is, for every \(w\in\Sigma^n\) the value \(\sigma(w)\) belongs to

\(argmin_{m^\prime\in\Sigma^k}\delta_\mathrm{H}\left(f(m'),w\right).\)

We break ties arbitrarily.

**Lemma 3.4.** _Let C be a systematic LTC with rate r=k/n and let_ A _be an_ \((1-\varepsilon)\)_-approximation randomized algorithm for_ MaxCSP(_C). Then for every_ \(m\in\Sigma^k\),<tbc>

\(\mathbb{E}\big[\delta_\mathrm{H}(\sigma(\tilde{\mathcal{A}}(\mathcal{I}_C(m))),m)\big]\le\frac{\varepsilon}{\kappa}.\)

<tbc>_Proof._ Because A achieves approximation ratio \(1-\varepsilon\), the expected fraction of satisfied constraints on the instance I_<sub>C</sub>(m_) is at least \(1-\varepsilon\), whence<tbc>

\(\mathbb{E}\left[\frac{\#\text{of unsatisfied constraints in}\mathcal{I}_C(m)}{|\mathcal{C}|}\right]\le\varepsilon.\)

<tbc>For every word \(w\in\Sigma^n\), Definition 2.3 guarantees that the rejection probability is at least \(\kappa\cdot\delta_\mathrm{H}(w,C)\). Applying this to the random output \(\tilde{\mathcal{A}}(\mathcal{I}_C(m))\) gives

\(\frac{\#\text{of unsatisfied constraints in}\mathcal{I}_C(m)}{|\mathcal{C}|}\ge\kappa\cdot\delta_\mathrm{H}(\tilde{\mathcal{A}}(\mathcal{I}_C(m)),C).\)

Taking expectations yields \(\mathbb{E}[\delta_\mathrm{H}(\tilde{\mathcal{A}}(\mathcal{I}_C(m)),C)]\le\varepsilon/\kappa\).

Let \(w:=\tilde{\mathcal{A}}(\mathcal{I}_C(m))\) and let \(c^\star:=f(\sigma(w))\) be the codeword selected by the nearest-message decoder. By definition, \(\delta_\mathrm{H}(w,C)=\delta_\mathrm{H}(w,c^\star)\). Because _f_ is systematic, the first _k_ entries of _w_ coincide with the message _m_, while the first _k_ entries of _c<sup>⋆</sup>_ coincide with \(\sigma(w)\). Consequently every coordinate where \(\sigma(w)\) and _m_ differ must also be a coordinate where _w_ and _c<sup>⋆</sup>_ differ. We therefore have

\(\delta_\mathrm{H}(\sigma(w),m)\le\delta_\mathrm{H}(w,c^\star)=\delta_\mathrm{H}(w,C).\)

Taking expectations over the randomness of \(\tilde{\mathcal{A}}\) completes the proof.

