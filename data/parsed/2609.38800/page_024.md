Let _W<sub>max</sub>_ be the upper bound of _W<sub>t</sub>_. Telescoping this inequality over the _m_ updates collapses the Lyapunov terms. Recognizing \(R_1^{(s)}-R_{m+1}^{(s)}\le\mathbb{E}[f(\theta_0^{(s)})]-\mathbb{E}[f(\theta_m^{(s)})]\), we sum across all _S_ epochs:<tbc>

\(\frac{\eta}{2}\sum_{s=0}^{S-1}\sum_{t=1}^m\mathbb{E}[\|\nabla f(\theta_t^{(s)})\|^2]\le[f(\theta_0)-f^*]+mW_{max}\sum_{s=0}^{S-1}\mathbb{E}[\|v_0^{(s)}-\bar{g}(\theta_0^{(s)})\|^2]+\frac{Sm\eta L_g^2}{8}\nu^2.\)

<tbc>Dividing both sides by \(\frac{\eta Sm}{2}\) and substituting the definition \(\bar{\sigma}_0^2:=\frac{1}{S}\sum_{s=0}^{S-1}\mathbb{E}[\|v_0^{(s)}-\bar{g}(\theta_0^{(s)})\|^2]\) yields the final result:

\(\frac{1}{Sm}\sum_{s=0}^{S-1}\sum_{t=1}^m\mathbb{E}\left[\|\nabla f(\theta_t^{(s)})\|^2\right]\le\frac{2[f(\theta_0)-f^*]}{\eta mS}+\frac{2W_{max}}{\eta}\bar{\sigma}_0^2+\frac{L_g^2}{4}\nu^2.\)

Because \(W_{max}\le\frac{L\eta^2}{2}+2\tau L_gm^{2/3}\eta^2\), dividing by \(\eta\) scales the bounded constant \(C_\sigma=\frac{W_{max}}{\eta}\le\frac{L\eta}{2}+2\tau\mu\), completing the proof.

## D Technical Proof of Theorem 3

Before proving Theorem 3, we introduce the following lemmas. Throughout this section, we utilize the landscape smoothness constant \(L\le pG\) and the stochastic Lipschitz constant \(L_g\le p^2G\).

### D.1 Recursive Variance

**Lemma 8** (Recursive Variance Identity)**.** Under the stochastic Lipschitz condition, the tracking error \(\|v_t-\bar{g}(\theta_t)\|^2\) satisfies:<tbc>

\(\mathbb{E}[\|v_t-\bar{g}(\theta_t)\|^2]\le\mathbb{E}[\|v_{t-1}-\bar{g}(\theta_{t-1})\|^2]+L_g^2\|\theta_t-\theta_{t-1}\|^2.\) (54)

<tbc>_Proof._ Define \(e_t:=v_t-\bar{g}(\theta_t)\). By the recursive update:<tbc>

\(e_t=[g(\theta_t,\Delta_t)-g(\theta_{t-1},\Delta_t)+v_{t-1}]-\bar{g}(\theta_t)\)<br>
\(=[v_{t-1}-\bar{g}(\theta_{t-1})]+[g(\theta_t,\Delta_t)-g(\theta_{t-1},\Delta_t)-(\bar{g}(\theta_t)-\bar{g}(\theta_{t-1}))]\)<br>
\(=e_{t-1}+\xi_t,\)

<tbc>where \(\xi_t:=g(\theta_t,\Delta_t)-g(\theta_{t-1},\Delta_t)-(\bar{g}(\theta_t)-\bar{g}(\theta_{t-1}))\).

Since \(\mathbb{E}_{\Delta_t}[\xi_t|\mathcal{F}_t]=0\) and _e_<sub>_t_-1</sub> is F_<sub>t</sub>_-measurable:<tbc>

\(\mathbb{E}[\|e_t\|^2]=\mathbb{E}[\|e_{t-1}\|^2]+\mathbb{E}[\|\xi_t\|^2],\)

<tbc>where the cross-term vanishes. Now, \(\|\xi_t\|^2\le\|g(\theta_t,\Delta_t)-g(\theta_{t-1},\Delta_t)\|^2\) (since variance \(\le\) second moment). By the stochastic Lipschitz property of the estimator, we have

\(\mathbb{E}[\|\xi_t\|^2]\le\mathbb{E}[\|g(\theta_t,\Delta_t)-g(\theta_{t-1},\Delta_t)\|^2]\le L_g^2\|\theta_t-\theta_{t-1}\|^2.\)

This completes the proof.

### D.2 Descent Lemma

**Lemma 9** (Descent Lemma for Recursive CRVG)**.** For the parameter update \(\theta_{t+1}=\theta_t-\eta v_t\), under the _L_-smoothness guarantee, it holds that:<tbc>

\(f(\theta_{t+1})\le f(\theta_t)-\frac{\eta}{2}\|\nabla f(\theta_t)\|^2-\frac{\eta}{2}(1-L\eta)\|v_t\|^2+\frac{\eta}{2}\|v_t-\nabla f(\theta_t)\|^2.\) (55)

<tbc>_Proof._ By the smoothness descent inequality with \(y=\theta_{t+1}=\theta_t-\eta v_t\):<tbc>

\(f(\theta_{t+1})\le f(\theta_t)-\eta\langle\nabla f(\theta_t),v_t\rangle+\frac{L\eta^2}{2}\|v_t\|^2.\)

<tbc>Using the algebraic identity \(-\langle a,b\rangle=\frac{1}{2}\|a-b\|^2-\frac{1}{2}\|a\|^2-\frac{1}{2}\|b\|^2\) with \(a=\nabla f(\theta_t)\) and _b=v<sub>t</sub>_:

\(f(\theta_{t+1})\le f(\theta_t)-\frac{\eta}{2}\|\nabla f(\theta_t)\|^2-\frac{\eta}{2}\|v_t\|^2+\frac{\eta}{2}\|v_t-\nabla f(\theta_t)\|^2+\frac{L\eta^2}{2}\|v_t\|^2\)<br>
\(=f(\theta_t)-\frac{\eta}{2}\|\nabla f(\theta_t)\|^2-\frac{\eta}{2}(1-L\eta)\|v_t\|^2+\frac{\eta}{2}\|v_t-\nabla f(\theta_t)\|^2.\)

This completes the proof.

