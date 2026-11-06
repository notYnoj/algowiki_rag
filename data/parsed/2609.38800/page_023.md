## C.2 Lyapunov Sequence Expansion

**Lemma 6** (Lyapunov Sequence Expansion)**.** Define the Lyapunov function for a single epoch as \(R_t^{(s)}=\mathbb{E}[f(\theta_t^{(s)})+c_t\|\theta_t^{(s)}-\theta_0^{(s)}\|^2]\), where _c<sub>m</sub>_=0. By defining the recursive control sequence as \(c_t=c_{t+1}(1+\beta)+\left(\frac{L\eta^2}{2}+c_{t+1}(1+\beta^{-1})\eta^2\right)L_g^2\), the single-step Lyapunov difference satisfies:

\(R_{t+1}^{(s)}-R_t^{(s)}\le-\frac{\eta}{2}\mathbb{E}[\|\nabla f(\theta_t^{(s)})\|^2]-\left[\frac{\eta}{2}(1-L\eta)-c_{t+1}(1+\beta^{-1})\eta^2\right]\mathbb{E}[\|\bar{g}(\theta_t^{(s)})\|^2]\)<br>
\(+W_t\mathbb{E}[\|v_0^{(s)}-\bar{g}(\theta_0^{(s)})\|^2]+\frac{\eta L_g^2}{8}\nu^2,\) (53)

where \(W_t=\frac{L\eta^2}{2}+c_{t+1}(1+\beta^{-1})\eta^2\).

_Proof._ Applying Young’s Inequality establishes \(\|\theta_{t+1}^{(s)}-\theta_0^{(s)}\|^2\le(1+\beta)\|\theta_t^{(s)}-\theta_0^{(s)}\|^2+(1+\beta^{-1})\eta^2\|v_t\|^2\) for some \(\beta>0\). Substituting this alongside Lemma 5 into \(R_{t+1}^{(s)}-R_t^{(s)}\), and expanding \(\mathbb{E}\|v_t\|^2\) again, we get:

\(R_{t+1}^{(s)}-R_t^{(s)}\le-\frac{\eta}{2}\mathbb{E}[\|\nabla f(\theta_t^{(s)})\|^2]-\left[\frac{\eta}{2}(1-L\eta)-c_{t+1}(1+\beta^{-1})\eta^2\right]\mathbb{E}[\|\bar{g}(\theta_t^{(s)})\|^2]\)<br>
\(+\left[\frac{L\eta^2}{2}+c_{t+1}(1+\beta^{-1})\eta^2\right]\mathbb{E}[\|v_t-\bar{g}(\theta_t^{(s)})\|^2]+\frac{\eta L_g^2}{8}\nu^2\)<br>
\(+[c_{t+1}(1+\beta)-c_t]\mathbb{E}[\|\theta_t^{(s)}-\theta_0^{(s)}\|^2].\)

Letting \(W_t=\frac{L\eta^2}{2}+c_{t+1}(1+\beta^{-1})\eta^2\), we substitute the non-recursive SVRG tracking error bound, \(\mathbb{E}[\|v_t-\bar{g}(\theta_t^{(s)})\|^2]\le\mathbb{E}[\|v_0^{(s)}-\bar{g}(\theta_0^{(s)})\|^2]+L_g^2\mathbb{E}[\|\theta_t^{(s)}-\theta_0^{(s)}\|^2]\), into the inequality to group the terms:

\(R_{t+1}^{(s)}-R_t^{(s)}\le-\frac{\eta}{2}\mathbb{E}[\|\nabla f(\theta_t^{(s)})\|^2]-\left[\frac{\eta}{2}(1-L\eta)-c_{t+1}(1+\beta^{-1})\eta^2\right]\mathbb{E}[\|\bar{g}(\theta_t^{(s)})\|^2]\)<br>
\(+W_t\mathbb{E}[\|v_0^{(s)}-\bar{g}(\theta_0^{(s)})\|^2]+\frac{\eta L_g^2}{8}\nu^2+\left[c_{t+1}(1+\beta)+W_tL_g^2-c_t\right]\mathbb{E}[\|\theta_t^{(s)}-\theta_0^{(s)}\|^2].\)

To entirely eliminate the path dependency, we force the coefficient of \(\|\theta_t^{(s)}-\theta_0^{(s)}\|^2\) to zero by defining \(c_t=c_{t+1}(1+\beta)+W_tL_g^2\), which strictly yields the final bound.

## C.3 Bounding Constants and Non-Negativity

**Lemma 7** (Non-Negativity Condition)**.** By setting the decay rate \(\beta=m^{-1/3}\) and the learning rate \(\eta=\frac{\mu}{L_gm^{2/3}}\) for a sufficiently small universal constant \(\mu>0\), the coefficient of \(\|\bar{g}(\theta_t^{(s)})\|^2\) in Lemma 6 is strictly non-negative.

_Proof._ Following standard non-convex variance reduction techniques, we set \(\beta=m^{-1/3}\). By mathematical induction, the recursive sequence defined in Lemma 6 is bounded by \(c_t\le\tau L_gm^{1/3}\) for a universal constant \(\tau>0\).

To safely drop the \(\|\bar{g}(\theta_t^{(s)})\|^2\) term from the Lyapunov difference, its coefficient must be non-negative:

\(\frac{\eta}{2}(1-L\eta)\ge c_{t+1}(1+m^{1/3})\eta^2.\)

Given \(c_{t+1}\le\tau L_gm^{1/3}\), the right-hand side is bounded by \(2\tau L_gm^{2/3}\eta^2\). Substituting \(\eta=\frac{\mu}{L_gm^{2/3}}\), this condition resolves to \(\frac{\mu}{2}\ge 2\tau\mu^2\), which strictly holds for \(\mu\le\frac{1}{4\tau}\).

## C.4 Proof of Theorem 2

_Proof._ By applying Lemma 7 to the result of Lemma 6, the non-positive \(\|\bar{g}(\theta_t^{(s)})\|^2\) term is safely dropped:

\(R_{t+1}^{(s)}-R_t^{(s)}\le-\frac{\eta}{2}\mathbb{E}[\|\nabla f(\theta_t^{(s)})\|^2]+W_t\mathbb{E}[\|v_0^{(s)}-\bar{g}(\theta_0^{(s)})\|^2]+\frac{\eta L_g^2}{8}\nu^2.\)

