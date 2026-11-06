As a first step towards the proof of Corollary 4.9 we define the problem of Boolean min-plus product and prove that it has equivalent running time to \(\alpha\)-navigability testing up to polylogarithmic factors.

**Definition 4.4.** _Let M be an_ \(n\times n\) _matrix over_ \(\mathbb{R}_{\ge 0}\)_, and let N be an_ \(n\times n\) _Boolean matrix. Their_ Boolean min-plus product _is the matrix M⋆N defined by_

\([M\star N]_{i,j}=min\{M_{i,k}:N_{k,j}=1\},\)

_with the convention that the minimum over the empty set is_ \(+\infty\).

Equivalently, one may regard _N_ as a matrix over \(\{0,\infty\}\), replacing each 1 by 0 and each 0 by \(\infty\), and then take the usual min-plus product.

This is a problem that has been used as a subroutine to compute node-weighted APSP in previous works by Chan, Yuster, and Abboud et al most recently (see "All-Pairs Shortest Paths with Few Weights per Node " for more details). It’s hardness was studied in the recent "Universe Reduction for APSP: Equivalence of Three Fine-Grained Hypotheses", which demonstrated APSP-hardness.

**Lemma 4.5.** _\[Lemma 6.3 from Universe Reduction for APSP: Equivalence of Three Fine-Grained Hypotheses\] For every_ \(\varepsilon>0\)_, there does not exist an_ \(O(n^{2.5-\varepsilon})\) _algorithm for Boolean min-plus product on_ \(n\times n\) _matrices, unless the APSP conjecture is falsified._

For the purpose of proving \(\alpha\)-navigability testing is equivalent to Boolean min-plus product computation, we define an intermediate problem.

**Definition 4.6.** _Let_ \(A\in\{0,1\}^{n\times n}\) _and let_ \(B,C\in\mathbb{R}_{\ge 0}^{n\times n}\)_. The_ Boolean min-plus threshold testing problem _asks to report all pairs_ \((i,j)\in[n]\times[n]\) _such that_

\(min\{B_{k,j}:A_{i,k}=1\}\le C_{i,j},\)

_again with the convention that the minimum over the empty set is_ \(+\infty\).

**Lemma 4.7.** _Boolean min-plus product and Boolean min-plus threshold testing are equivalent up to polylogarithmic overhead. More precisely, if one of the two problems on_ \(n\times n\) _matrices can be solved in time T(n), then the other can be solved in time_ \(\widetilde{O}(T(n)+n^2)\).

_Proof._ We first reduce Boolean min-plus product to threshold testing.

Let \(M\in\mathbb{R}_{\ge 0}^{n\times n}\) and \(N\in\{0,1\}^{n\times n}\), our goal is to compute _M⋆N_. For each row _i_, replace the entries of _M_ by their ranks within that row. Formally, define \(R\in[n]^{n\times n}\) by

\(R_{i,k}=\big|\{k'\in[n]:M_{i,k^\prime}\le M_{i,k}\}\big|.\)

Then, for every _i,j_, the value \[_R⋆N_\]_<sub>i,j</sub>_ is exactly the rank, within row _i_, of the minimum entry among the columns _k_ with _N<sub>k,j</sub>_=1, which makes recovering _M⋆N_ from _R⋆N_ straight forward in \(\widetilde{O}(n^2)\) time.

It therefore suffices to compute _R⋆N_, and this can be done using _O_(log_n_) calls to the threshold- testing oracle by parallel binary search on all entries simultaneously. More precisely, a threshold matrix _C_ is formed, and a search space for each coordinate is maintained (initialized to \[_n_\]). At each step, we query threshold testing on (_N<sup>T</sup>,R<sup>T</sup>,C<sup>T</sup>_). Following this call, for each pair _i,j_ we learn whether:<tbc>

\(min\{[R^T]_{k,i}=R_{i,k}:[N^T]_{j,k}=N_{k,j}=1\}\le[C^T]_{j,i}\Longleftrightarrow[R\star N]_{i,j}\le C_{i,j}\)

