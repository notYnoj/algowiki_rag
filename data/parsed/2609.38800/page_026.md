Substituting this back into (60):

\(\frac{\eta}{2}\sum_{t=1}^m\mathbb{E}\left[\left\|\nabla f(\theta_t^{(s)})\right\|^2\right]\le[f(\theta_0^{(s)})-f^*]+\eta m\mathbb{E}\left[\left\|v_0^{(s)}-\bar{g}(\theta_0^{(s)})\right\|^2\right]+\frac{m\eta}{4}L_g^2\nu^2\)<br>
\(-\left[\frac{\eta}{2}(1-L\eta)-L_g^2\eta^3m\right]\sum_{t=1}^m\mathbb{E}[\|v_t\|^2].\) (61)

**Step 5: Choose step size to ensure non-negativity.** Under the conditions \(\eta\le\frac{1}{2L}\) (ensuring \(1-L\eta\ge\frac{1}{2}\)) and \(\eta\le\frac{1}{2L_g\sqrt{m}}\), the composite coefficient satisfies \(\left[\frac{\eta}{2}(1-L\eta)-L_g^2\eta^3m\right]\ge\frac{\eta}{4}-\frac{\eta}{4}=0\). This allows us to drop the non-positive \(\|v_t\|^2\) sum:

\(\frac{\eta}{2}\sum_{t=1}^m\mathbb{E}\left[\left\|\nabla f(\theta_t^{(s)})\right\|^2\right]\le[f(\theta_0^{(s)})-f^*]+\eta m\mathbb{E}\left[\left\|v_0^{(s)}-\bar{g}(\theta_0^{(s)})\right\|^2\right]+\frac{m\eta}{4}L_g^2\nu^2.\) (62)

**Step 6: Sum over epochs and divide.** Summing (62) over _s_=0,1_,...,S_-1 and using the telescoping property \(\sum_{s=0}^{S-1}[f(\theta_0^{(s)})-\mathbb{E}f(\theta_{m+1}^{(s)})]\le f(\theta_0)-f^*\):

\(\frac{\eta}{2}\sum_{s=0}^{S-1}\sum_{t=1}^m\mathbb{E}\left[\left\|\nabla f(\theta_t^{(s)})\right\|^2\right]\le[f(\theta_0)-f^*]+\eta mS\bar{\sigma}_0^2+\frac{Sm\eta}{4}L_g^2\nu^2.\)

Dividing both sides by \(\frac{\eta Sm}{2}\) yields the following upper bound:

\(\frac{1}{Sm}\sum_{s=0}^{S-1}\sum_{t=1}^m\mathbb{E}\left[\left\|\nabla f(\theta_t^{(s)})\right\|^2\right]\le\frac{2[f(\theta_0)-f^*]}{\eta mS}+2\bar{\sigma}_0^2+\frac{L_g^2}{2}\nu^2.\)

This completes the proof.

