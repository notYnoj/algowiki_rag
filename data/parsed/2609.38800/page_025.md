## D.3 Bounding the Mean Squared Error

**Lemma 10** (Variance and Bias Decomposition)**.** The mean squared error of the CRVG estimator satisfies:

\(\mathbb{E}[\|v_t-\nabla f(\theta_t)\|^2]\le 2\mathbb{E}[\|v_t-\bar{g}(\theta_t)\|^2]+\frac{L_g^2\nu^2}{2}.\) (56)

_Proof._ Using \(v_t-\nabla f(\theta_t)=(v_t-\bar{g}(\theta_t))+(\bar{g}(\theta_t)-\nabla f(\theta_t))\) and the inequality \(\|a+b\|^2\le 2\|a\|^2+2\|b\|^2\):

\(\mathbb{E}[\|v_t-\nabla f(\theta_t)\|^2]\le 2\mathbb{E}[\|v_t-\bar{g}(\theta_t)\|^2]+2\mathbb{E}[\|\bar{g}(\theta_t)-\nabla f(\theta_t)\|^2].\)

The analytical bias is bounded by \(\|\bar{g}(\theta_t)-\nabla f(\theta_t)\|\le\frac{\nu L_g}{2}\) . Substituting this into the second term bounds it by \(2\left(\frac{\nu L_g}{2}\right)^2=\frac{L_g^2\nu^2}{2}\) .

## D.4 Unrolling the Recursive Variance Bound

**Lemma 11** (Cumulative Variance Control)**.** The tracking error summed over one epoch satisfies:

\(\sum_{t=1}^m\mathbb{E}[\|v_t-\bar{g}(\theta_t)\|^2]\le m\mathbb{E}[\|v_0-\bar{g}(\theta_0)\|^2]+L_g^2\eta^2m\sum_{t=1}^m\mathbb{E}[\|v_{t-1}\|^2].\) (57)

_Proof._ By Lemma 8, unrolling the recursion from step _t_ back to step 0:

\(\mathbb{E}[\|v_t-\bar{g}(\theta_t)\|^2]\le\mathbb{E}[\|v_0-\bar{g}(\theta_0)\|^2]+L_g^2\eta^2\sum_{j=1}^t\mathbb{E}[\|v_{j-1}\|^2],\)

where we used \(\|\theta_j-\theta_{j-1}\|^2=\eta^2\|v_{j-1}\|^2\). Summing over _t_=1_,...,m_:

\(\sum_{t=1}^m\mathbb{E}[\|v_t-\bar{g}(\theta_t)\|^2]\le m\mathbb{E}[\|v_0-\bar{g}(\theta_0)\|^2]+L_g^2\eta^2\sum_{t=1}^m\sum_{j=1}^t\mathbb{E}[\|v_{j-1}\|^2].\)

Using \(\sum_{t=1}^m\sum_{j=1}^ta_{j-1}=\sum_{j=0}^{m-1}(m-j)a_j\le m\sum_{j=0}^{m-1}a_j\) yields the result.

## D.5 Proof of Theorem 3

_Proof._ **Step 1: Apply the Descent Lemma.** Taking the expectation of Lemma 9:

\(\mathbb{E}[f(\theta_{t+1})]\le\mathbb{E}[f(\theta_t)]-\frac{\eta}{2}\mathbb{E}[\|\nabla f(\theta_t)\|^2]-\frac{\eta}{2}(1-L\eta)\mathbb{E}[\|v_t\|^2]+\frac{\eta}{2}\mathbb{E}[\|v_t-\nabla f(\theta_t)\|^2].\) (58)

**Step 2: Substitute the MSE bound.** By Lemma 10, substituting the decomposed tracking error and bias:

\(\mathbb{E}[f(\theta_{t+1})]\le\mathbb{E}[f(\theta_t)]-\frac{\eta}{2}\mathbb{E}[\|\nabla f(\theta_t)\|^2]-\frac{\eta}{2}(1-L\eta)\mathbb{E}[\|v_t\|^2]+\eta\mathbb{E}[\|v_t-\bar{g}(\theta_t)\|^2]+\frac{\eta}{4}L_g^2\nu^2.\) (59)

**Step 3: Telescope over one epoch.** Summing (59) from _t_=1 to _t=m_ within epoch _s_:

\(\frac{\eta}{2}\sum_{t=1}^m\mathbb{E}\left[\left\|\nabla f(\theta_t^{(s)})\right\|^2\right]\le\mathbb{E}[f(\theta_1^{(s)})]-\mathbb{E}[f(\theta_{m+1}^{(s)})]-\frac{\eta}{2}(1-L\eta)\sum_{t=1}^m\mathbb{E}[\|v_t\|^2]\)<br>
\(+\eta\sum_{t=1}^m\mathbb{E}[\|v_t-\bar{g}(\theta_t)\|^2]+\frac{m\eta}{4}L_g^2\nu^2.\) (60)

**Step 4: Substitute the cumulative variance bound.** By Lemma 11:

\(\eta\sum_{t=1}^m\mathbb{E}[\|v_t-\bar{g}(\theta_t)\|^2]\le\eta m\mathbb{E}\left[\left\|v_0^{(s)}-\bar{g}(\theta_0^{(s)})\right\|^2\right]+L_g^2\eta^3m\sum_{t=1}^m\mathbb{E}[\|v_{t-1}\|^2].\)

