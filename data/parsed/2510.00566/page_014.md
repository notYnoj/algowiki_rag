<tbc>where \(p^{(0,m)}(\mathbf{q},\mathbf{x})=\sum_{j=1}^MT(\mathbf{q})_jT(\mathbf{x})_j\). The \(\varepsilon\)-relaxed bound re places the second factor by \(2\varepsilon\sqrt{R_{T(\mathbf{q})}^{(m,d)}R_{T(\mathbf{x})}^{(m,d)}}\), with \(\varepsilon=1\) recov ering (5).

Panorama maintains a running threshold \(\tau\), the squared distance of the _k_th nearest neighbour found so far (written _d<sub>k</sub>_ in the main paper). A candidate **x** is pruned at level _m_ if \(\mathrm{LB}^m(\mathbf{q},\mathbf{x})>\tau\), equivalently if the gap

\(\|\mathbf{q}-\mathbf{x}\|^2-\mathrm{LB}^m(\mathbf{q},\mathbf{x})\le\Delta:=\|\mathbf{q}-\mathbf{x}\|^2-\tau.\)

We call \(\Delta\) the _pruning margin_. In strict mode (\(\varepsilon=1\)), true _k_-nearest neighbours satisfy \(\Delta\le 0\) and are never pruned by a valid lower bound; the analysis below shows that for non-near-neighbours \(\Delta\) is positive with high probability and the gap shrinks fast enough to prune at \(m\checkmark d\).

_Asymptotic notation._ We use \(f(n)\lesssim g(n)\) for model upper-bound scaling after constants are explicit, and _f(n_)∼_cg(n_) for asymptotic equivalence with constant _c\>_0.

_Assumptions._ The proofs rest on the following assumptions, reproduced here for self-containment.

**Assumption A1** (Exponential PCA tail energy)**.** We take _T_ to be the PCA basis of the dataset. On real embeddings its tail energy decays exponentially,

\(R_{T(\mathbf{x})}^{(m,d)}\approx\|\mathbf{x}\|^2e^{-\alpha m/d},\)

where \(\alpha>0\) is the per-dataset decay rate read directly off the PCA spectrum. This exponential profile is an empirical property of the PCA basis, which we verify directly: the mean absolute fit error of the model is below 0.04 on every dataset (main paper, energy-compaction figure). The ≈ records exactly this finite-sample modelling claim.

**Assumption A2** (Bounded norms)**.** There is a constant _R_ such that \(\|T(\mathbf{x})\|\le R\) for every **x** in the dataset and every query **q**. We write _C_<sub>0</sub>:=4_R_<sup>2</sup>.

**Assumption A3** (Gaussian distance model)**.** For a fixed query **q**, the squared distances \(\|\mathbf{q}-\mathbf{x}\|^2\) in the candidate stream are modelled as i.i.d. draws from a Gaussian with mean \(\mu\) and standard deviation \(\sigma\). The exact distribution is chi-square-like and the candidate stream produced by an ANN index is not literally i.i.d.; the Gaussian order- statistic calculation is the tractable cost model whose constants are checked empirically.

**Assumption A4** (One dimension per level)**.** The proof reasons at the finest pruning granularity, _L=d_, \(m_\ell=\ell\).

A fifth assumption (residual isotropy, A5) is introduced and used only in Section A.5.

## A.2 PCA minimises expected tail energy

**Lemma A.1** (Ky Fan)**.** _Let_ \(\Sigma\in\mathbb{R}^{d\times d}\) _be symmetric positive semidefinite with eigenvalues_ \(\lambda_1\ge\cdots\ge\lambda_d\ge 0\)_. For every_ \(m\in\{1,\dots,d\}\),

\(\mathrm{max}_{T\in\mathrm{O}(d)}\sum_{j=1}^m(T\Sigma T^\top)_{jj}=\sum_{j=1}^m\lambda_j,\)

_with the maximum attained when the first m rows of T span the eigenspace associated with the top-m eigenvalues of_ \(\Sigma\).

Proof (sketch). The diagonal of \(T\Sigma T^\top\) is majorised by the eigenvalues of \(\Sigma\) (Schur–Horn theorem). For any _m_, the partial sum of the _m_ largest diagonal entries is at most the partial sum of the _m_ largest eigenvalues of \(\Sigma\). Equality is attained by the orthogonal transform whose first _m_ rows span the corresponding eigenspace. See Horn and Johnson \[21\], Section 4.3 for the full proof. \(\square\)

**Proposition** (PCA energy-optimality; cf. main paper Sections 4.1 and 5.1)**.** _Let_ \(X\in\mathbb{R}^d\) _be a centred random vector_ (E\[_X_\]=**0**_) with covariance_ \(\Sigma=\mathbb{E}[XX^\top]\) _having eigenvalues_ \(\lambda_1\ge\cdots\ge\lambda_d\ge 0\)_. For any orthogonal_ \(T\in\mathrm{O}(d)\) _and any_ \(m\in\{1,\dots,d-1\}\),

\(\mathbb{E}\big[R_{T(X)}^{(m,d)}\big]\ge\sum_{j=m+1}^d\lambda_j,\)

_with equality when the rows of T are eigenvectors of_ \(\Sigma\) _ordered by decreasing eigenvalue._

Proof. For any orthogonal _T_,

\(\mathbb{E}\big[(TX)_j^2\big]=\mathbb{E}\big[(TX)(TX)^\top\big]_{jj}=\big(T\mathbb{E}[XX^\top]T^\top\big)_{jj}=(T\Sigma T^\top)_{jj}.\)

Summing over _j\>m_,

\(\mathbb{E}\big[R_{T(X)}^{(m,d)}\big]=\sum_{j=m+1}^d(T\Sigma T^\top)_{jj}.\)

Orthogonal conjugation preserves the trace, so

\(\sum_{j=1}^d(T\Sigma T^\top)_{jj}=\mathrm{Tr}(T\Sigma T^\top)=\mathrm{Tr}(\Sigma)=\sum_{j=1}^d\lambda_j.\)

Therefore

\(\mathbb{E}\big[R_{T(X)}^{(m,d)}\big]=\sum_{j=1}^d\lambda_j-\sum_{j=1}^m(T\Sigma T^\top)_{jj}.\)

By Lemma A.1,

\(\sum_{j=1}^m(T\Sigma T^\top)_{jj}\le\sum_{j=1}^m\lambda_j,\)

with equality when the first _m_ rows of _T_ span the top-_m_ eigenspace of \(\Sigma\). Substituting,

\(\mathbb{E}\big[R_{T(X)}^{(m,d)}\big]\ge\sum_{j=1}^d\lambda_j-\sum_{j=1}^m\lambda_j=\sum_{j=m+1}^d\lambda_j,\)

with equality precisely when _T_ is the PCA basis. \(\square\)

## A.3 Proposition 5.1: Expected refinement cost

This section derives the expected refinement cost of Panorama under the Gaussian candidate-stream model. The argument has three ingredients: a high-probability model for the running _k_th threshold, a Cauchy–Schwarz pruning-depth bound, and an averaged finite-sample margin constant.

Panorama maintains a pruning threshold \(\tau\), the squared distance of the _k_th nearest neighbour found so far. For analytical tractability we model \(\tau_i\) as the _k_th order statistic among _i_ i.i.d. draws from the distance distribution, acknowledging that the algorithm’s threshold actually arises from a mixture of exact and pruned candidates.

