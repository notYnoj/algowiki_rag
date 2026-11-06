_orbits of exact ADMM and exact sGS-ADMM converge to an endpoint of_ Z_<sub>⋆</sub>. The distance contracts eventually Q-linearly in the_ \(\mathsf{G}_\tau\) _metric, and the shadow and the raw primal-dual iterates converge R-linearly (Appendix F.3)._

**Corollary 5.2** (PDHG)**.** _Under the same hypotheses with_ \(\sigma=\eta_x\) _and_ \(\eta_x\eta_y\|\mathcal{A}\|_\mathrm{op}^2<1\)_, every PDHG orbit converges to a KKT pair; the distance to_ W_<sub>⋆</sub> contracts eventually Q-linearly in the preconditioned metric, and the iterates and the slack_ \(S^k=C-\mathcal{A}^*\lambda^k\) _converge R-linearly._

The convergence is _eventual_: it begins after an entrance time that we do not bound (Appendix F.1).

## 6 Generic Benign Degeneracy

It remains to show that the two hypotheses of Theorem 4.3 occur broadly: outside one lower- dimensional semialgebraic set of objectives, they hold _simultaneously at every uniquely rank-one exact order_ (proofs in Appendix G).

### Full order: exactness and strict complementarity for free.

Let \(\mathcal{P}_n:=\mathrm{span}\{x^T:T\subseteq[n]\}\) be the 2_<sup>n</sup>_-dimensional space of square-free objectives, and \(\mathcal{P}_{\le 2d}\) its subspace of degree at most 2_d_.

**Proposition 6.1** (Full-order structure)**.** _At d=n the moment body_ X_<sub>n</sub> is the affine image, with unique coefficients, of the probability simplex on_ \(\{\pm 1\}^n\): \(X=\sum_{a\in\{\pm 1\}^n}\pi_ab_n(a)b_n(a)^\top\) _with_ \(\pi_a\ge 0\), \(\sum_a\pi_a=1\)_. Consequently every uniquely minimized f is uniquely rank-one exact at d=n, so_ \(d_\star(f)\le n\)_; and unique rank-one exactness persists upward from any order at which it holds. Moreover, for every uniquely minimized f the full-order relaxation admits a strictly complementary optimal certificate of rank_ 2_<sup>n</sup>_-1 _(Appendix G.1)._

### Fixed-order cells and one Gram construction.

Fix a candidate optimizer \(a\in\{\pm 1\}^n\) and an order _d_, and let _u=b<sub>d</sub>(a_). Inside the normalized coefficient space \(\mathcal{Q}(a,d):=\{g\in\mathcal{P}_{\le 2d}:g(a)=0\}\), the _exact cell_ E(_a,d_) collects the _g_ for which (P_<sub>d</sub>_) has the unique optimizer \(uu^\top\). The _strictly complementary cell_ \(\mathcal{E}_\mathrm{sc}(a,d)\subseteq\mathcal{E}(a,d)\) collects the _g_ represented by some PSD Gram matrix _S_ with ker(_S_)=span{_u_}. For each nonempty \(\Gamma\in\mathcal{I}_{2d}\), split \(\Gamma=P_\Gamma\dot{\cup}Q_\Gamma\) into parts of size at most _d_ (with \(P_\Gamma=\Gamma\), \(Q_\Gamma=\emptyset\) when \(|\Gamma|\le d\)) and set

\(w_\Gamma:=e_{P_\Gamma}-a^\Gamma e_{Q_\Gamma},S_\mathrm{int}:=\sum_{\emptyset\neq A\in\mathcal{I}_d}w_Aw_A^\top.\) (6.1)

Each \(w_\Gamma\) is orthogonal to _u_ and its Gram matrix represents \(2(1-a^\Gamma x^\Gamma)\); under this splitting convention, the _N_-1 vectors \(w_A=e_A-a^Ae_\emptyset\) (\(\emptyset\neq A\in\mathcal{I}_d\)) form a basis of \(u^\perp\), so \(S_\mathrm{int}\unknown 0\) is an _interior certificate_ with kernel exactly span{_u_}.

**Theorem 6.2** (Fixed-order SC genericity)**.** E<sub>sc</sub>(_a,d_) _is open in_ Q(_a,d_) _and dense relative to_ E(_a,d); both cells are semialgebraic; and_ \(\mathrm{dim}\big(\mathcal{E}(a,d)\backslash\mathcal{E}_\mathrm{sc}(a,d)\big)<\mathrm{dim}\mathcal{E}(a,d)\).

The proof (Appendix G.2) gets openness from the Gram construction (6.1), density from \(S+\varepsilon S_\mathrm{int}\), and the rest from Tarski-Seidenberg and the frontier theorem \[BCR98\].

