**Algorithm 1** 3-Circuit Non-Recursive CRVG with Center-Point Caching

Require: Initial parameters \(\theta_0\), learning rate \(\eta>0\), shift \(\nu>0\), epoch length _m_, number of epochs _S_.<br>
for s=0,1,...,S_-1 do<br>
   Compute anchor gradient: \(v_0^{(s)}=\hat{g}(\theta_0^{(s)})\) (O(1) zeroth-order estimate or mini-batch)<br>
   Update: \(\theta_1^{(s)}=\theta_0^{(s)}-\eta v_0^{(s)}\)<br>
   Evaluate and cache: \(C_\text{anchor}=f(\theta_0^{(s)})\) // Cached for entire epoch<br>
   Set \(\theta_t=\theta_1^{(s)}\)<br>
   Evaluate and cache: \(C_\text{curr}=f(\theta_t)\) // Circuit 1<br>
   for t=1,...,m-1 do<br>
   Sample \(\Delta_t\in\{-1,+1\}^p\) uniformly at random // Circuit 2<br>
   Evaluate: \(C_\text{curr}=f(\theta_t+\nu\Delta_t)\)<br>
   Evaluate: \(C_\text{anc+}=f(\theta_0^{(s)}+\nu\Delta_t)\) // Circuit 3<br>
   \(g_\text{curr}=\frac{1}{\nu}(C_\text{curr+}-C_\text{curr})\Delta_t\)<br>
   \(g_\text{anchor}=\frac{1}{\nu}(C_\text{anc+}-C_\text{anchor})\Delta_t\)<br>
   Anchored update: \(v_t=g_\text{curr}-g_\text{anchor}+v_0^{(s)}\)<br>
   Parameter update: \(\theta_{t+1}=\theta_t-\eta v_t\)<br>
   Evaluate: \(C_\text{curr}=f(\theta_{t+1})\) // Circuit 1 (for next step)<br>
   end for<br>
   Set \(\theta_0^{(s+1)}=\theta_m^{(s)}\)<br>
end for

## 3.3 Variant 2: 3-Circuit Recursive CRVG

The Recursive CRVG variant takes caching a step further by employing a SARAH-type update rule \[Nguyen et al., 2017\]. Instead of anchoring to a static epoch snapshot, it draws on the immediate history of the optimization trajectory to bound the spatial variance. The recursive tracking estimator _v<sub>t</sub>_ is defined as:

\(v_t=g(\theta_t,\Delta_t)-g(\theta_{t-1},\Delta_t)+v_{t-1}.\) (6)

Because the identical perturbation vector \(\Delta_t\) is utilized for both shifted evaluations, the spatial variance is tightly correlated and mathematically cancels out across sequential steps. The center-point caching mechanism operates as a continuous rolling window.

**Algorithm 2** 3-Circuit Recursive CRVG with Center-Point Caching

Require: Initial parameters \(\theta_0\), learning rate \(\eta>0\), shift \(\nu>0\), epoch length _m_, number of epochs _S_.<br>
for s=0,1,...,S_-1 do<br>
   Compute anchor gradient: \(v_0^{(s)}=\hat{g}(\theta_0^{(s)})\) (O(1) zeroth-order estimate or mini-batch)<br>
   Update: \(\theta_1^{(s)}=\theta_0^{(s)}-\eta v_0^{(s)}\)<br>
   Evaluate and cache: \(C_\text{prev}=f(\theta_0^{(s)})\), \(\theta_\text{prev}=\theta_0^{(s)}\)<br>
   Set \(\theta_t=\theta_1^{(s)}\)<br>
   Evaluate and cache: \(C_\text{curr}=f(\theta_t)\) // Circuit 1<br>
   for t=1,...,m-1 do<br>
   Sample \(\Delta_t\in\{-1,+1\}^p\) uniformly at random<br>
   Evaluate: \(C_\text{curr+}=f(\theta_t+\nu\Delta_t)\) // Circuit 2<br>
   Evaluate: \(C_\text{prev+}=f(\theta_\text{prev}+\nu\Delta_t)\) // Circuit 3<br>
   \(g_\text{curr}=\frac{1}{\nu}(C_\text{curr+}-C_\text{curr})\Delta_t\)<br>
   \(g_\text{prev}=\frac{1}{\nu}(C_\text{prev+}-C_\text{prev})\Delta_t\)<br>
   Recursive update: \(v_t=g_\text{curr}-g_\text{prev}+v_{t-1}\)<br>
   \(\theta_\text{prev}=\theta_t\), \(C_\text{prev}=C_\text{curr}\) // Rolling cache transfer<br>
   Parameter update: \(\theta_{t+1}=\theta_t-\eta v_t\)<br>
   Evaluate: \(C_\text{curr}=f(\theta_{t+1})\) // Circuit 1 (for next step)<br>
   end for<br>
   Set \(\theta_0^{(s+1)}=\theta_m^{(s)}\)<br>
end for

