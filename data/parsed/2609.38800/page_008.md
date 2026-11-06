**Proof**. Deferred to Appendix B.1.

This formally proves that VQE and QAOA objective functions satisfy the smoothness assumption required for the CRVG convergence analysis without relying on arbitrary constants.

## 4.2 1-Sided Estimator Bias Bound

Let \(g(\theta,\Delta)=\frac{f(\theta+\nu\Delta)-f(\theta)}{\nu}\Delta\) be the 1-sided gradient estimator with shift \(\nu>0\) and \(\Delta\in\{-1,+1\}^p\) drawn uniformly. Define the _expected estimator_:<tbc>

\(\bar{g}(\theta):=\mathbb{E}_\Delta[g(\theta,\Delta)].\)

<tbc>**Theorem 1.** The 1-sided estimator satisfies:

\(\|\bar{g}(\theta)-\nabla f(\theta)\|\le\frac{\nu p^2\|H\|}{2}.\) (11)

**Proof**. Deferred to Appendix B.2.

**Lemma 2** (Lipschitz Property of the Stochastic Estimator)**.** For any fixed perturbation \(\Delta\), the 1-sided estimator inherently satisfies a stochastic Lipschitz condition with constant _L<sub>g</sub>_. Specifically, bounded by the parameter dimension and the Hamiltonian norm, it holds that:

\(\mathbb{E}_\Delta\|g(x,\Delta)-g(y,\Delta)\|^2\le L_g^2\|x-y\|^2\le p^4\|H\|^2\|x-y\|^2\forall x,y\in\mathbb{R}^p.\) (12)

**Proof**. Deferred to Appendix B.3.

**Lemma 3** (Spatial Variance of the Mini-Batch Anchor)**.** Let \(v_0=\frac{1}{B}\sum_{i=1}^Bg(\theta,\Delta_i)\) be the anchor gradient computed using a mini-batch of _B_ independent 1-sided estimators, where \(\Delta_i\in\{-1,+1\}^p\) are uniformly drawn Rademacher random vectors. Because the trigonometric structure of the quantum landscape strictly bounds the gradient magnitude, the variance of this mini-batch anchor scales as:

\(\bar{\sigma}_0^2=\text{Var}(v_0)=\mathcal{O}\left(\frac{p}{B}\right).\) (13)

To guarantee the initial anchor variance globally satisfies the target threshold \(\mathcal{O}(\epsilon^2)\) across all epochs, the required mini-batch size is \(B=\mathcal{O}\left(\frac{p}{\epsilon^2}\right)\).

**Proof**. Deferred to Appendix B.4.

## 4.3 Convergence Results for Non-Recursive CRVG

**Theorem 2** (Convergence Rate of 3-Circuit Non-Recursive CRVG)**.** Suppose Assumptions 1 and 2 hold. Let _L_ denote the landscape smoothness constant and _L<sub>g</sub>_ denote the stochastic Lipschitz constant of the expected 1-sided estimator. There exist universal constants \(\mu>0\) and \(\tau>0\) such that by choosing the learning rate \(\eta=\frac{\mu}{L_gm^{2/3}}\), the 3-Circuit Non-Recursive algorithm satisfies:

\(\frac{1}{Sm}\sum_{s=0}^{S-1}\sum_{t=1}^m\mathbb{E}\left[\|\nabla f(\theta_t^{(s)})\|^2\right]\le\frac{2[f(\theta_0)-f^*]}{\eta mS}+2C_\sigma\bar{\sigma}_0^2+\frac{L_g^2}{4}\nu^2\) (14)

where \(\bar{\sigma}_0^2:=\frac{1}{S}\sum_{s=0}^{S-1}\mathbb{E}\left[\|v_0^{(s)}-\bar{g}(\theta_0^{(s)})\|^2\right]\) is the average initial anchor error, and \(C_\sigma=\frac{L\eta}{2}+2\tau\mu\) is a bounded constant.

**Proof**. Deferred to Appendix C.

## 4.4 Convergence Results for Recursive CRVG

**Theorem 3** (Convergence Rate of 3-Circuit Recursive CRVG)**.** Suppose Assumptions 1 and 2 hold. Let _L_ denote the landscape smoothness constant and _L<sub>g</sub>_ denote the stochastic Lipschitz constant of the expected 1-sided estimator. Choose the learning rate \(\eta\) such that it satisfies the bounds:

\(\eta\le\frac{1}{2L}\text{and}\eta\le\frac{1}{2L_g\sqrt{m}}\) (15)

