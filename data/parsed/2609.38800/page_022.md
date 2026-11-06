**Step 2: Universal Spatial Variance of a Single Estimator**<br>
The spatial variance of a single 1-sided estimator is \(\text{Var}(g)=\mathbb{E}_\Delta[\|g(\theta,\Delta)-\bar{g}(\theta)\|^2]\). As formally established in quantum zeroth-order literature (e.g., \[Sweke et al., 2020\]), projecting this structurally bounded landscape onto a _p_-dimensional random perturbation vector \(\Delta\in\{-1,+1\}^p\) injects a spatial variance that scales linearly with the dimension of the parameter space. Because the gradient magnitude cannot diverge, the global upper bound for the variance of a single estimator is rigorously constrained to:

\(\text{Var}(g(\theta,\Delta))=\mathcal{O}(p)\) (49)

**Step 3: Variance of the Empirical Mini-Batch**<br>
The anchor gradient _v_<sub>0</sub> is constructed as the empirical mean of _B_ independent and identically distributed (i.i.d.) 1-sided estimators. By the fundamental statistical properties of i.i.d. random variables, the variance of the sample mean scales inversely with the batch size:

\(\bar{\sigma}_0^2=\text{Var}\left(\frac{1}{B}\sum_{i=1}^Bg(\theta,\Delta_i)\right)=\frac{\text{Var}(g(\theta,\Delta))}{B}=\mathcal{O}\left(\frac{p}{B}\right)\) (50)

**Step 4: Enforcing the Convergence Threshold**<br>
To satisfy the bounds of the convergence theorems, the tracking error introduced by the anchor must not exceed the target stationarity threshold \(\mathcal{O}(\epsilon^2)\). Equating our worst-case variance bound to this threshold yields:

\(\mathcal{O}\left(\frac{p}{B}\right)\le\mathcal{O}(\epsilon^2)\) (51)

Solving for the batch size rigorously dictates the structural requirement \(B=\mathcal{O}\left(\frac{p}{\epsilon^2}\right)\). This completes the proof, demonstrating that the anchor batch size must scale with the parameter dimension to successfully suppress the inherent spatial variance of the hardware.

## C Technical Proof of Theorem 2

Before proving Theorem 2, we introduce the following supporting lemmas to bound the tracking error and construct the Lyapunov sequence.

### C.1 Refined Descent Lemma

**Lemma 5** (Descent Lemma for Non-Recursive CRVG)**.** For the parameter update \(\theta_{t+1}^{(s)}=\theta_t^{(s)}-\eta v_t\), under the _L_-smoothness guarantee, the expected objective function value satisfies:

\(\mathbb{E}[f(\theta_{t+1}^{(s)})]\le\mathbb{E}[f(\theta_t^{(s)})]-\frac{\eta}{2}\mathbb{E}[\|\nabla f(\theta_t^{(s)})\|^2]-\frac{\eta}{2}(1-L\eta)\mathbb{E}[\|\bar{g}(\theta_t^{(s)})\|^2]\)<br>
\(+\frac{L\eta^2}{2}\mathbb{E}[\|v_t-\bar{g}(\theta_t^{(s)})\|^2]+\frac{\eta L_g^2}{8}\nu^2.\) (52)

_Proof._ Applying the standard smoothness inequality to the parameter update \(\theta_{t+1}^{(s)}=\theta_t^{(s)}-\eta v_t\) gives:<tbc>

\(f(\theta_{t+1}^{(s)})\le f(\theta_t^{(s)})-\eta\langle\nabla f(\theta_t^{(s)}),v_t\rangle+\frac{L\eta^2}{2}\|v_t\|^2.\)

<tbc>Taking the expectation conditioned on the history up to step _t_, we note \(\mathbb{E}[v_t]=\bar{g}(\theta_t^{(s)})\). Using the algebraic identity \(-\eta\langle\nabla f,\bar{g}\rangle=\frac{\eta}{2}\|\bar{g}-\nabla f\|^2-\frac{\eta}{2}\|\nabla f\|^2-\frac{\eta}{2}\|\bar{g}\|^2\), and separating the variance as \(\mathbb{E}\|v_t\|^2=\mathbb{E}\|v_t-\bar{g}(\theta_t^{(s)})\|^2+\|\bar{g}(\theta_t^{(s)})\|^2\), we obtain:

\(\mathbb{E}[f(\theta_{t+1}^{(s)})]\le\mathbb{E}[f(\theta_t^{(s)})]-\frac{\eta}{2}\mathbb{E}[\|\nabla f(\theta_t^{(s)})\|^2]-\frac{\eta}{2}(1-L\eta)\mathbb{E}[\|\bar{g}(\theta_t^{(s)})\|^2]\)<br>
\(+\frac{L\eta^2}{2}\mathbb{E}[\|v_t-\bar{g}(\theta_t^{(s)})\|^2]+\frac{\eta}{2}\mathbb{E}[\|\bar{g}(\theta_t^{(s)})-\nabla f(\theta_t^{(s)})\|^2].\)

By the analytical bias bound established in Theorem 1, the final term is bounded by \(\frac{\eta}{2}\left(\frac{L_g\nu}{2}\right)^2=\frac{\eta L_g^2}{8}\nu^2\). Substituting this yields the desired result.

