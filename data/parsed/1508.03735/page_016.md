<tbc>**Definition 6** (The Exponential Mechanism \[MT07\])**.** _The_ exponential mechanism \(\mathcal{M}_E(D,q,\mathcal{R},\varepsilon)\) _selects and outputs an element_ \(r\in\mathcal{R}\) _with probability proportional to_<tbc>

\(\mathrm{exp}\left(\frac{\varepsilon q(D,r)}{2\Delta(q)}\right),\)

<tbc>_where_

\(\Delta(q)\equiv\mathrm{max}_{D,D^\prime\in\mathcal{X}^n,D\sim D^\prime}|q(D)-q(D')|.\)

McSherry and Talwar showed that the exponential mechanism is private and with high probability selects an outcome with high quality.

**Theorem 5** (\[MT07\])**.** _The exponential mechanism_ \(\mathcal{M}_E(\cdot,q,\mathcal{R},\varepsilon)\)_satisfies_ \((\varepsilon,0)\)_-differential privacy, and for any_ \(D\in\mathcal{X}^n\) _it outputs an outcome_ \(r\in\mathcal{R}\) _that satisfies_

\(q(D,r)\ge\mathrm{max}_{r^\prime} q(D,r')-\frac{2\Delta(q)(\mathrm{log}(|\mathcal{R}|/\beta))}{\varepsilon}\)

_with probability at least_ \(1-\beta\).

Using the exponential mechanism, we can take any coordination protocol \((\sigma,\pi)\), and construct a jointly differentially private coordination protocol \((\sigma',\pi)\) with the same coordination complexity, and almost the same approximation factor. The idea is to construct a differentially private encoding function \(\sigma'\) that selects from the message space of \(\sigma\) using the exponential mechanism. Without loss of generality, we assume that the social objective function _S_ has low-sensitivity:

\(\mathrm{max}_{i\in[n]}\mathrm{max}_{a\in\mathcal{A}^n,D\in\mathcal{X}^n}\mathrm{max}_{a_i^\prime\in\mathcal{A}_i,D_i^\prime\in\mathcal{X}}|S(D,a)-S((D'_i,D_{-i}),(a'_i,a_{-i}))|\le 1.\)<sup>4</sup>

Now we present the private protocol as follows:

**Algorithm 2** Jointly private algorithm \(\mathrm{PriCoor}((\sigma,\pi),q,\varepsilon,D)\)

**Input:** A coordination protocol \((\sigma,\pi)\), objective function _f_, and input instance _D_<br>
Let \(\mathcal{R}=\{\sigma(D')|D'\in\mathcal{X}^n\}\) be the space of all possible messages in the range of \(\sigma\)<br>
Let quality function _q_ be defined as \(q(D,r)=\mathbb{E}_\pi[S(D,(\pi(r,D^{(i)}))_{i\in[n]})]\forall D\in\mathcal{X}^n,r\in\mathcal{R}\)<br>
Let \(\sigma'(D)=\mathcal{M}_E(D,q,\mathcal{R})\) be the message selected by the exponential mechanism<br>
**Output** \(a=(\pi(\sigma'(D),D^{(i)}))_{i=1}^n\)

**Lemma 12.** _Suppose that_ \((\sigma,\pi)\) _has coordination complexity_ \(\ell\) _and approximation ratio_ \(\rho\) _for the objective f. Then the algorithm_ \(\mathrm{PriCoor}((\sigma,\pi),f,\varepsilon,D)\) _satisfies_ \((\varepsilon,0)\)_-joint differential privacy, and with probability at least_ \(1-\beta\)_, the resulting action profile a satisfies_

\(\mathbb{E}\left[S(D,a)\right]\ge\frac{\mathrm{OPT}(D)}{\rho}-\frac{2(\ell+\mathrm{log}(1/\beta))}{\varepsilon},\)

_where the expectation is taken over the internal randomness of the encoding function_ \(\sigma'\) _and decoding function_ \(\pi\).

<sup>4</sup>We can always obtain this condition by scaling. It is already satisfied in the matching problem.

