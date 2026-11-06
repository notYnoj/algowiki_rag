The proof relies on some basic properties of the Lagrangian and strong concavity and is deferred to the appendix.

**Lemma 5.** _The coordination mechanism_ ReC _instantiated with regularization parameter_ \(\eta\) _and target accuracy parameter_ \(\varepsilon\) _will coordinate the players to play a solution_ \(\widehat{x}\) _that satisfies_ \(\|\widehat{x}-x^\bullet\|\le\varepsilon\)_, and has a coordination complexity of_ \(O(klog(nk/\eta\varepsilon))\).

_Proof._ Note that \(\alpha=\frac{\eta\varepsilon^2}{4\sqrt{nk}}\), and the mechanism rounds each coordinate of the optimal dual solution \(\lambda^\bullet\) to a multiple of \(\alpha/\sqrt{k}\), so the approximate dual vector \(\widehat{\lambda}\) can be specified with \(O(klog(\sqrt{k}/\alpha))\) bits.

Since for each coordinate _j_, \(|\lambda_j^\bullet-\widehat{\lambda}_j|\le\alpha/\sqrt{k}\), we also have that that \(\|\lambda^\bullet-\widehat{\lambda}\|\le\alpha\). By Lemma 4, we know that \(\|\widehat{x}-x^\bullet\|\le\varepsilon\).

## 4.2 Approximate Feasibility and Optimality

Now we carry out the second step to show that if we choose the regularization parameter \(\eta\) carefully, the solution resulting from the coordination mechanism above is both approximately feasible and optimal. Let _x_<sup>∗</sup> denote the optimal solution of the original convex program, \(x^\bullet\) denote the optimal solution of the regularized convex program, and \(\widehat{x}(\eta)\) denote the solution resulting from the coordination mechanism when we use parameter \(\eta\).

As an intermediate step, we will first bound the objective difference between \(x^\bullet\) and _x_<sup>∗</sup>.

**Lemma 6.** _For any choice of_ \(\eta\), \(v(x^*)-v(x^\bullet)\le\frac{\eta m}{2}\) .

_Proof._ Since both _x_<sup>∗</sup> and \(x^\bullet\) are in the feasible region of the regularized convex program, we know that

\(v(x^\bullet)-\frac{\eta}{2}\|x^\bullet\|^2\ge v(x^*)-\frac{\eta}{2}\|x^*\|^2.\)

Since for each _i_, \((x^\bullet)^{(i)},(x^*)^{(i)}\) has \(\ell_2\) norm bounded by 1, then \(\|x^\bullet\|^2-\|x^*\|^2\le n\). Therefore, we must have \(v(x^\bullet)\ge v(x^*)-\frac{\eta m}{2}\)

Next we bound the objective difference between \(\widehat{x}\) and \(x^\bullet\) using Lipschitzness.

**Lemma 7.** _Suppose that_ \(\|\widehat{x}-x^\bullet\|\le\varepsilon\)_, then_

\(v(x^\bullet)-v(\widehat{x})\le n\varepsilon.\)

_Proof._ The proof follows easily from the fact that each _v_<sup>(_i_)</sup> is 1-Lipschitz and the function _v_ is _n_-Lipschitz in the aggregate vector _x_.

**Theorem 3.** _The coordination mechanism_ \(\text{ReC}(\eta,\varepsilon)\) _coordinates the players to play a joint solution_ \(\widehat{x}\) _that satisfies_

\(v(\widehat{x})\ge\text{OPT}-n(\varepsilon+\eta)\text{\textit{and}}min_{x\in\mathcal{F}}\|x-\widehat{x}\|\le\varepsilon\)

_and has coordination complexity of_ \(O(klog(nk/\eta\varepsilon))\).

_Proof._ Follows easily from the previous lemmas.

