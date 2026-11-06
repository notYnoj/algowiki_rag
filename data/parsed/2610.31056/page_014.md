### 3.2 Hardness Hypothesis

For any parameter \(\kappa\ge 1\), the currently best algorithms for \(n^\kappa\)-approximate SVP run in \(2^{\mathcal{O}(n/\kappa)}\) time \[Sch87, SE94, GN08, ALNSD20\]. More precisely, when \(\kappa\ge 1\), \(n^\kappa\)-approximation to SVP can be computed in \(\mathcal{O}^\star(2^{0.802n/(\kappa+1)})\) time \[ALNSD20\]. Motivated by the apparent hardness, Vafa and Vaikuntanathan \[VV25\] implicitly stated the following hypothesis <sup>11</sup>:

**Hypothesis 2.** _For any_ \(\varepsilon>0\) _and parameter_ \(\ell\in[1,n]\)_, there is no_ \(2^{\mathcal{O}(n/\ell)^{1-\varepsilon}}\)_-time algorithm that given a lattice_ L _of dimension n returns n non-zero independent vectors_ \(\mathbf{v}_i\in\mathcal{L}\) _such that_ \(\|\mathbf{v}_i\|_2\le 2^{\mathcal{O}(\ell)}\cdot\lambda_n(\mathcal{L})\).

However, notice that since the work of Schnorr \[Sch87\], there is no 2<sup>_o(n_)</sup> time algorithm that solves _n<sup>c</sup>_-approximate SVP for any constant \(c\ge 0\). Motivated by this, we state an even stronger hypothesis than Hypothesis 2.

**Hypothesis 1.** _For any constant_ \(c\ge 1\)_, there exists_ \(\varepsilon>0\) _such that there is no_ \(\mathcal{O}(2^{\varepsilon n})\) _time algorithm that given an n-dimensional lattice_ L _with high probability returns a non-zero vector_ \(\mathbf{v}\in\mathcal{L}\) _such that_ \(\|\mathbf{v}\|_2\le\mathcal{O}(n^c)\cdot\lambda_n(\mathcal{L})\).

To the best of our knowledge, this hypothesis was not explicitly stated. However, if the hypothesis turns out to be false, it would mean a significant breakthrough on the approximate Shortest Vector Problem. In section Section B.1, we show that these problems are tightly connected.

### 3.3 Declaration on the Use of AI Tools.

**No** AI tools were used for the version submitted to the FOCS 2026 conference. A generative AI tool, Claude (Opus), was used solely for proofreading, language editing, and identifying potential inconsistencies for this arXiv version. All technical contributions are original to the authors, who independently verified relevant AI-generated suggestions and take full responsibility for the manuscript.

## 4 Subexponential algorithm: Proof of Theorem 1.1

In this section, we present our subexponential algorithm for weak PESS.

**Theorem 1.1.** _There exists a deterministic algorithm that, given an integer n and a set_ \(S\subseteq\{1,\dots,M\}\) _of size n such that nM\<_2_<sup>n</sup>_-1_, runs in time_ \(\mathrm{poly}(n)\cdot M^{\mathcal{O}(1/\mathrm{log}\delta)}\) _and returns two distinct subsets of S with the same sum, where_ \(\delta=\delta(n,M):=n/\mathrm{log}M\) _is the density of the instance._

_As a corollary, when M_=2<sup>_o(n_)</sup>_, the algorithm runs in time_ \(\mathrm{poly}(n)\cdot M^{o(1)}\).

Let _k_ be the largest power of 2 such that \(n\cdot M\le 2^{\lfloor n/k\rfloor\mathrm{log}k}\) (if such a _k_ does not exist, then \(\delta=\Omega(1)\) and the brute-force algorithm solves the problem in the desired time). Let \(W:=2^{\lfloor n/k\rfloor}\).

If \(k=\Omega(n)\), then _M_=poly(_n_) and we can run dynamic programming of \[Vas22\] in \(\widetilde{\mathcal{O}}(nM)=\mathrm{poly}(n)\) time. Hence, we may assume _k=o(n_). We will present an algorithm running in \(\mathrm{poly}(n)\cdot W^2\) time. This will conclude the proof of Theorem 1.1 by setting \(\delta=\Theta(k/\mathrm{log}k)\).

First, arbitrarily partition the input set \(S=S_1\unknown\dots\unknown S_k\unknown S_{k+1}\) such that \(|S_i|=\lfloor n/k\rfloor\) for every \(i\in[k]\). We will ignore the set _S_<sub>_k_+1</sub>. In the base case, for every \(i\in[k]\), compute the sets:<tbc>

\(\mathcal{A}_i^{(0)}:=\{\Sigma(X)|X\subseteq S_i\}.\)

<sup>11</sup>To be precise, \[VV25\] needed only to assume \(\ell=\Theta(\sqrt{n})\) and assumed hardness of SVP rather than SIVP. In their setting, these problems are equivalent \[MR07\].

