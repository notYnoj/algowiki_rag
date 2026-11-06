**Corollary 3** (Sample complexity)**.** _Let_ \(\epsilon>0\)_, and let_ \(\mathscr{E}_\epsilon\) _be a set of indices with_<tbc>

\(\lambda_\mathrm{max}\sum_{z\notin\mathscr{E}_\epsilon}|\hat{x}_z|^2\le\frac{\epsilon^2}{2}\|x^*\|_A^2.\)

<tbc>_Define_ \(q_\mathrm{min}(\mathscr{E}_\epsilon)=\mathrm{min}_{z\in\mathscr{E}_\epsilon} q(z)\)_. If_

\(M\ge\frac{\mathrm{ln}(2\kappa/\epsilon^2)}{q_\mathrm{min}(\mathscr{E}_\epsilon)},\) (11)

_then_ \(\mathbb{E}[\|x_\mathscr{S}-x^*\|_A^2]\le\epsilon^2\|x^*\|_A^2\)_, where_ \(\kappa=\lambda_\mathrm{max}/\lambda_\mathrm{min}\).

_Proof._ We split the sum in Eq. (8) into \(z\notin\mathscr{E}_\epsilon\) and \(z\in\mathscr{E}_\epsilon\). The first part is at most \((\epsilon^2/2)\|x^*\|_A^2\) by definition. The second part is at most \(\lambda_\mathrm{max}\|x^*\|^2e^{-Mq_\mathrm{min}}\). Since \(\|x^*\|_A^2\ge\lambda_\mathrm{min}\|x^*\|^2\), it is at most \(\kappa e^{-Mq_\mathrm{min}}\|x^*\|_A^2\). Equation (11) makes it at most \((\epsilon^2/2)\|x^*\|_A^2\).

**Corollary 4** (High-probability Galerkin reconstruction)**.** _Let_ \(\epsilon\), \(\mathscr{E}_\epsilon\)_, and_ \(q_\mathrm{min}(\mathscr{E}_\epsilon)\) _be as in Corollary 3, but with the stronger tail condition_ \(\lambda_\mathrm{max}\sum_{z\notin\mathscr{E}_\epsilon}|\hat{x}_z|^2\le\epsilon^2\|x^*\|_A^2\)_. For_ \(0<\delta<1\)_, if_

\(M\ge\frac{\mathrm{ln}(|\mathscr{E}_\epsilon|/\delta)}{q_\mathrm{min}(\mathscr{E}_\epsilon)},\) (12)

_then with probability at least_ \(1-\delta\) _every index of_ \(\mathscr{E}_\epsilon\) _is observed and_ \(\|x_\mathscr{S}-x^*\|_A\le\epsilon\|x^*\|_A\).

_Proof._ By Eq. (10), \(\mathrm{Pr}(z\notin\mathscr{S})\le e^{-Mq(z)}\le\delta/|\mathscr{E}_\epsilon|\) for every \(z\in\mathscr{E}_\epsilon\). The union bound gives \(\mathrm{Pr}(\mathscr{E}_\epsilon\unknown\subseteq\mathscr{S})\le\delta\). If \(\mathscr{E}_\epsilon\subseteq\mathscr{S}\), Eq. (9) and the tail condition give the error bound.

Compared with Corollary 3, the high-probability budget replaces \(\mathrm{ln}(2\kappa/\epsilon^2)\) by \(\mathrm{ln}(|\mathscr{E}_\epsilon|/\delta)\). The essential set of Eq. (12) is defined in the energy norm, so it can contain modes of very small normalized weight. Complete discovery of \(\mathscr{E}_\epsilon\) is a sufficient condition and can be pessimistic, because a missed mode of small weight costs little error. Any filter must preserve the solution support, and pruning after sampling must be controlled separately.

**Proposition 5** (Lower bound and sampling efficiency)**.** _Let_ \(K_\epsilon\) _be the smallest_ |S| _for which the Galerkin error is at most_ \(\epsilon\|x^*\|_A\)_. Any sampling protocol needs_ \(M\ge K_\epsilon\) _shots, because each shot adds at most one index. Since_ \(q_\mathrm{min}(\mathscr{E}_\epsilon)\le 1/|\mathscr{E}_\epsilon|\)_, the right-hand side of Eq._ (11) _is at least_ \(|\mathscr{E}_\epsilon|\mathrm{ln}(2\kappa/\epsilon^2)\).

We therefore define the sampling efficiency

\(\eta_\mathrm{s}=|\mathscr{E}_\epsilon|q_\mathrm{min}(\mathscr{E}_\epsilon)\le 1.\) (13)

A small value of \(\eta_\mathrm{s}\) identifies an essential index with a low sampling probability. Inefficiency can arise from repeated samples of already observed indices or from probability mass outside \(\mathscr{E}_\epsilon\). This is a coupon- collector problem with a nonuniform distribution \[16\]. The relevant property of _q_ is its flatness on \(\mathscr{E}_\epsilon\), not its resemblance to \(|\hat{x}|^2\). The two bounds of Proposition 5 need not match when \(\eta_\mathrm{s}\) is small.

**Corollary 6** (Replacement noise)**.** _Suppose that each shot is independently replaced, with probability p\<_1_, by an index drawn from an arbitrary distribution. Then the outcome law satisfies_ \(q'(z)\ge(1-p)q(z)\)_, and the sufficient budget of Corollary 3 increases at most by the factor_ 1/(1-_p)._

By Lemma 1, adding corrupted indices to a retained set cannot increase its error. At a fixed total number of shots, however, replacement can remove useful ideal samples and increase the error relative to an uncontaminated run. The shot bound assumes independent replacement. Arbitrary gate and readout channels need not satisfy the pointwise dominance \(q'\ge(1-p)q\). For them we use a weaker statement. If the actual law \(q'\) lies within total-variation distance \(\eta\) of _q_, then \(|q'(z)-q(z)|\le\eta\) for every _z_, and Corollaries 3 and 4 hold with _q_<sub>min</sub> replaced by \(q_\mathrm{min}-\eta\) whenever this is positive.

