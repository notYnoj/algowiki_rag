Then, after _S_ epochs of length _m_ each, the 3-Circuit Recursive CRVG algorithm (Algorithm 2) satisfies:

\(\frac{1}{Sm}\sum_{s=0}^{S-1}\sum_{t=1}^m\mathbb{E}\left[\|\nabla f(\theta_t^{(s)})\|^2\right]\le\frac{2\left[f(\theta_0)-f^*\right]}{\eta mS}+2\bar{\sigma}_0^2+\frac{L_g^2}{2}\nu^2\) (16)

where \(\bar{\sigma}_0^2:=\frac{1}{S}\sum_{s=0}^{S-1}\mathbb{E}\left[\|v_0^{(s)}-\bar{g}(\theta_0^{(s)})\|^2\right]\) is the average initial anchor error.

**Proof**. Deferred to Appendix D.

## 4.5 Complexity Analysis

To determine the theoretical sample complexity of both CRVG variants to achieve a strict \(\epsilon^2\)-stationary point (where \(\mathbb{E}[\|\nabla f(\theta)\|^2]\le\epsilon^2\)), we evaluate the initial anchor gradient \(v_0^{(s)}\) using a stochastic mini-batch of _B_ independent 1-sided estimators:

\(v_0^{(s)}=\frac{1}{B}\sum_{i=1}^Bg(\theta_0^{(s)},\Delta_i)\) (17)

where \(g(\theta,\Delta)=\frac{f(\theta+\nu\Delta)-f(\theta)}{\nu}\Delta\) and \(\nu>0\) is the finite-difference shift.

Following standard conventions in stochastic non-convex optimization, we absorb the problem-specific landscape constants, namely the objective smoothness _L_, the stochastic Lipschitz constant _L<sub>g</sub>_, and the Hamiltonian norm bound _G_, into the asymptotic \(\mathcal{O}(\cdot)\) notation. This isolates the structural sample complexity scaling strictly with respect to the parameter dimension _p_ and the target accuracy \(\epsilon\).

**Step 1: Universal Anchor Variance and Bias Mismatch**<br>
From the convergence theorems, the deterministic bias floor evaluates to \(\mathcal{O}(\nu^2)\). To strictly satisfy the \(\mathcal{O}(\epsilon^2)\) convergence criterion without introducing dimension dependence, we set the finite-difference shift to \(\nu=\mathcal{O}(\epsilon)\). This perfectly bounds the bias term to \(\mathcal{O}(\epsilon^2)\).

Because simultaneous perturbation injects a spatial variance of O(_p_) into each 1-sided estimator, the variance of the mini-batch anchor is \(\bar{\sigma}_0^2=\mathcal{O}(p/B)\). To ensure the anchor variance matches the \(\mathcal{O}(\epsilon^2)\) target threshold, we need a batch size of \(B=\mathcal{O}(p/\epsilon^2)\).

**Step 2: Circuit Complexity of the Non-Recursive Variant**<br>
For the Non-Recursive CRVG, bounding the optimization term \(\frac{1}{\eta mS}\) under the restrictive step size \(\eta=\mathcal{O}\left(\frac{1}{m^{2/3}}\right)\) requires that the epoch count scales as:

\(\frac{m^{2/3}}{mS}=\mathcal{O}(\epsilon^2)\Longrightarrow S=\mathcal{O}\left(\frac{1}{m^{1/3}\epsilon^2}\right)\) (18)

The total execution cost C_<sub>non</sub>_ sums the \(\mathcal{O}(p/\epsilon^2)\) anchor evaluations and the 3_m_ inner-loop steps across the _S_ epochs:

\(\mathcal{C}_{non}=S(B+3m)=\mathcal{O}\left(\frac{1}{m^{1/3}\epsilon^2}\right)\left[\mathcal{O}\left(\frac{p}{\epsilon^2}\right)+3m\right]=\mathcal{O}\left(\frac{p}{m^{1/3}\epsilon^4}+\frac{m^{2/3}}{\epsilon^2}\right)\) (19)

Minimizing C_<sub>non</sub>_ with respect to the epoch length by balancing the two terms yields the optimal length \(m=\mathcal{O}(p/\epsilon^2)\). Substituting this back isolates the exact sample complexity:

\(\mathcal{C}_{non}=\mathcal{O}\left(\frac{(p/\epsilon^2)^{2/3}}{\epsilon^2}\right)=\mathcal{O}\left(\frac{p^{2/3}}{\epsilon^{10/3}}\right)\) (20)

**Step 3: Circuit Complexity of the Recursive Variant**<br>
For the Recursive CRVG, the history-dependent update permits a more aggressive step size of \(\eta=\mathcal{O}\left(\frac{1}{\sqrt{m}}\right)\). Enforcing the \(\mathcal{O}(\epsilon^2)\) optimization bound dictates the total number of epochs:

\(\frac{\sqrt{m}}{mS}=\mathcal{O}(\epsilon^2)\Longrightarrow S=\mathcal{O}\left(\frac{1}{\sqrt{m}\epsilon^2}\right)\) (21)

Calculating the total executions C_<sub>rec</sub>_ utilizing the mini-batch anchor configurations and 3_m_ inner-loop executions:

\(\mathcal{C}_{rec}=S(B+3m)=\mathcal{O}\left(\frac{1}{\sqrt{m}\epsilon^2}\right)\left[\mathcal{O}\left(\frac{p}{\epsilon^2}\right)+3m\right]=\mathcal{O}\left(\frac{p}{\sqrt{m}\epsilon^4}+\frac{\sqrt{m}}{\epsilon^2}\right)\) (22)

