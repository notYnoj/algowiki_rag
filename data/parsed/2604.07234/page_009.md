<tbc>The heart of the proof is the corresponding inverse problem for the null model. Here _Y_ is independent of \(X'\), and we must rule out the possibility that an adversary can produce an induced near-equipartition of _Y_ so as to mimic the macroscopic block structure of \(X'\). This is difficult because it can be shown that

(1) many natural block statistics can be driven above 1/2 by a favorable induced near-equipartition, so one needs a score that is robust under adversarial choices;<tbc>

(2) there are exponentially many induced near-equipartitions of _Y_ , and this family is large enough that standard metric entropy arguments over the collection of all such induced near-equipartitions do not provide appropriate guarantees.

The notions of alignment introduced above are so that we may overcome the first obstacle. Our main device for overcoming the second obstacle is the _standardization algorithm_. This algorithm defines a map<tbc>

\(\varphi_Y:\mathcal{N}\mathcal{E}_\text{ind}(Y)\rightarrow\mathcal{N}\mathcal{E}_\text{std}(Y),\)

<tbc>sending induced near-equipartitions of _Y_ to a much smaller class of _standardized near-equipartitions_ in which almost all block lengths are some fixed length. We construct the standardization algorithm in such a way that the typical "extremal increase" in the value of the average local alignment is modest, so we may think of the standardization algorithm as an approximation algorithm. More precisely, Section 3.3 shows that with probability \(1-e^{-\Omega(N)}\), every induced near-equipartition is mapped to a standardized one whose score is larger by at most \(\beta^\star(\alpha)/2\). The proof reduces the worst-case effect of standardization to fluctuation bounds for contiguous substrings of _Y_ : large gains can only come from _biased stretches_, and a uniform random string contains too few such stretches for them to matter on the exponential scale. Once this reduction is established, a union bound over the much smaller family NE<sub>std</sub>(_Y_), together with concentration for each fixed partition, bounds the _standardized total alignment_ via

\(T_\text{std}(X',Y)<\frac{1+\beta^\star(\alpha)}{2}\)

with overwhelming probability. Hence, \(Y\notin\mathcal{G}(X')\).

Section 3.4 converts this structural separation into free-energy separation. Under the null model, the event \(Y\notin\mathcal{G}(X')\) implies that only an exponentially sparse subcollection of the \(\genfrac(){pt}{2}{N}{M}\) candidate embeddings contributes. Together with the regular alignment property for typical _x_, this yields the quantitative result

(1.10) \(\mathbb{P}\left(Z_{X^\prime,Y}<e^{N\left(f_\text{null}^\text{ann}(\alpha)-\Omega(1)\right)}\right)\ge 1-e^{-\Omega(N)}.\)

This implies that \(f_\text{null}(\alpha)<f_\text{null}^\text{ann}(\alpha)\). Under the planted model, (1.10) together with the size-bias relation between planted and null embeddings forces _Z<sub>X,Y</sub>_ above the null annealed scale by a fixed exponential margin, giving \(f_\text{null}^\text{ann}(\alpha)<f_\text{pl}(\alpha)\). This proves Theorem 1.1. Corollary 1.2 then follows by substituting the resulting gap into the mutual information identity (1.3).

## 1.3.2. _Proof overview of Theorem 1.3._

The starting point of the proof is to rewrite the planted annealed partition function in a way that exposes the geometry of _pairs_ of embeddings rather than individual embeddings. Indeed, a simple argument leads to the formula<tbc>

\(\mathbb{E}\left[Z_{X,Y}\right]=\frac{1}{\genfrac(){pt}{2}{N}{M}2^M}\sum_{\sigma,\tau\in\Sigma} 2^{\langle\sigma,\tau\rangle},\)

<tbc>where \(\langle\sigma,\tau\rangle\) denotes the _overlap_

\(\sum_{j=1}^M\unknown\{\sigma(j)=\tau(j)\}.\)

Hence, the goal of the rest of the proof is to understand the moment generating function of the overlap of a random pair of configurations. The key structural property used to understand this is a certain Markov

