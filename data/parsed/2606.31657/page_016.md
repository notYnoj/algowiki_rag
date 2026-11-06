<tbc>has marginals \(\nu_m\) and \(\nu_{m^\prime}\)). Under \(\Pi\) we have \((\sigma(x),\sigma(y))=(a,b)\) almost surely. For any outputs \(x,y\in\Sigma^n\) of \(\tilde{\mathcal{A}}\), the triangle inequality gives<tbc>

\(\delta_\mathrm{H}(x,y)\ge\delta_\mathrm{H}(f\circ\sigma(x),f\circ\sigma(y))-\delta_\mathrm{H}(x,f\circ\sigma(x))-\delta_\mathrm{H}(y,f\circ\sigma(y)).\)

<tbc>Whenever \(d_c(\sigma(x),\sigma(y))=1\), the first term is at least \(\delta\), so averaging over \(\Pi\) yields<tbc>

\(\mathbb{E}_{(x,y)\sim\Pi}\left[\delta_\mathrm{H}(x,y)\right]\ge\delta\mathbb{E}_{(a,b)\sim\pi_k}\left[d_c(a,b)\right]-\mathbb{E}_{x\sim\mu_m}\left[\delta_\mathrm{H}(x,f\circ\sigma(x))\right]-\mathbb{E}_{y\sim\mu_{m^\prime}}\left[\delta_\mathrm{H}(y,f\circ\sigma(y))\right].\)

<tbc>Lemma 3.4 bounds each error term by \(\varepsilon/\kappa\), giving

\(\mathsf{EMD}_{\delta_\mathrm{H}}\big(\tilde{\mathcal{A}}(\mathcal{I}_C(m)),\tilde{\mathcal{A}}(\mathcal{I}_C(m'))\big)\ge\delta\cdot\mathsf{TV}\left(\tilde{\mathcal{A}}(\mathcal{I}_C(m)),\tilde{\mathcal{A}}(\mathcal{I}_C(m'))\right)-\frac{2\varepsilon}{\kappa}.\)

By the definition of \(\tilde{\mathcal{A}}\), the first _k_ coordinates of the outputs are fixed to _m_ and \(m'\) respectively, so we have

\(\mathsf{EMD}_{\delta_\mathrm{H}}\big(\mathcal{A}(\mathcal{I}_C(m)),\mathcal{A}(\mathcal{I}_C(m'))\big)=\mathsf{EMD}_{\delta_\mathrm{H}}\big(\tilde{\mathcal{A}}(\mathcal{I}_C(m)),\tilde{\mathcal{A}}(\mathcal{I}_C(m'))\big)-\frac{1}{n}\)<br>
\(\ge\delta\cdot\mathsf{TV}\left(\tilde{\mathcal{A}}(\mathcal{I}_C(m)),\tilde{\mathcal{A}}(\mathcal{I}_C(m'))\right)-\frac{2\varepsilon}{\kappa}-\frac{1}{n}.\)

Averaging over _m_ and \(m'\) completes the proof.

## 3.4 Worst-Case Sensitivity Bound

We now convert the total-variation gap into an earth-mover lower bound for neighboring messages.

**Theorem 3.8** (Worst-case sensitivity via LTC)**.** _Let_ (_C,f,_S,V) _be a systematic LTC over_ \(\Sigma\) _with rate r, distance_ \(\delta\)_, variable degree_ \(\theta\)_, and detection probability_ \(\kappa\)_. Suppose_ A _is a_ \((1-\varepsilon)\)_- approximation algorithm for_ MaxCSP(_C). Then there exist messages_ \(m,m'\in\Sigma^k\) _with_ \(m\sim m'\) _such that_

\(\mathsf{EMD}_{\delta_\mathrm{H}}\big(\mathcal{A}(\mathcal{I}_C(m)),\mathcal{A}(\mathcal{I}_C(m'))\big)\ge\delta\left(1-\frac{|\Sigma|}{|\Sigma|-1}\cdot\frac{\varepsilon}{r\kappa}\right)-\frac{2\varepsilon}{\kappa}-\frac{1}{n}.\)

_Proof._ The claim follows directly from Lemma 3.7 since the expectation over _m_ and \(m'\sim m\) implies the existence of some pair \(m,m'\) achieving at least the expected value.

_Proof of Theorem 1.1._ Let \(C\subseteq\mathbb{F}_p^n\) be a linear LTC with rate _r_, distance \(\delta\), and detection probability \(\kappa\), and let A be a \((1-\varepsilon)\)-approximation algorithm for MaxCSP(_C_). By Lemma 2.5, after a fixed permutation of coordinates we may regard _C_ as a systematic LTC; we henceforth work in this permuted coordinate system and write _f_ for the associated systematic encoder. Consequently every instance I_<sub>C</sub>(m_) is satisfiable, witnessed by the codeword _f(m_). Applying Theorem 3.8 yields adjacent messages \(m\sim m'\) satisfying<tbc>

\(\mathsf{EMD}_{\delta_\mathrm{H}}\big(\mathcal{A}(\mathcal{I}_C(m)),\mathcal{A}(\mathcal{I}_C(m'))\big)\ge\delta\left(1-\frac{p}{p-1}\frac{\varepsilon}{r\kappa}\right)-\frac{2\varepsilon}{\kappa}-\frac{1}{n}.\)

<tbc>The two instances differ only on the tester constraints that query the unique message coordinate where _m_ and \(m'\) disagree; by Definition 2.3 their number is at most \(\theta\). Enumerate these constraints in I_<sub>C</sub>(m_) as _c_<sub>1</sub>_,...,c<sub>t</sub>_ with \(t\le\theta\), and let \(c'_j\) denote the corresponding constraint in \(\mathcal{I}_C(m')\) for each _j_. For _j_=0_,...,t_ define the chains of satisfiable instances<tbc>

\(\mathcal{I}^{(0)}:=\mathcal{I}_C(m),\mathcal{I}^{(j)}:=\mathcal{I}^{(j-1)}-c_j,\)

