## Filtering Posterior Sampling.

Dou and Song (2023) precisely leverage the linear measurement process and the corresponding optimal proposal. As the likelihood in eq. (12) and the reverse diffusion kernel are both Gaussian, the optimal proposal \(q_t^*\) is analytically available and is given by

\(q_t^*(\mathbf{x}_t|\mathbf{x}_{t+1},\mathbf{y}_t)=\mathcal{N}(\mathbf{x}_t;\mu^*(\mathbf{x}_{t+1},\mathbf{y}_t,t+1),\Sigma^*(t+1)),\) (13)

\(\Sigma^*(t)=\left(\Sigma_\theta(t)^{-1}+\frac{1}{\sigma_v^2\bar{\alpha}_{t-1}}\mathbf{A}^\top\mathbf{A}\right)^{-1},\)<br>
\(\mu^*(\mathbf{x}_t,\mathbf{y}_{t-1},t)=\Sigma^*(t)\left(\Sigma_\theta(t)^{-1}\mu_\theta(\mathbf{x}_t,t)+\frac{1}{\sigma_v^2\bar{\alpha}_{t-1}}\mathbf{A}^\top\mathbf{y}_{t-1}\right).\)

With the optimal proposal, the new weight update is simply<tbc>

\(\tilde{w}_t=\boxed{\frac{p_\theta(\mathbf{x}_t|\mathbf{x}_{t+1})g_t(\mathbf{y}_t|\mathbf{x}_t)}{q_t^*(\mathbf{x}_t|\mathbf{x}_{t+1},\mathbf{y}_t)}}.\)

<tbc>However, instead of forward-noising **y**<sub>0</sub>, they find improved performance through a noise-sharing technique by setting **y**_<sub>T</sub>_=**A**x_<sub>T</sub>_ and building the sequence backwards with

\(\nu_{FPS}(\mathbf{y}_{t-1}|\mathbf{y}_t,\mathbf{y}_0)=\mathcal{N}\left(\mathbf{y}_{t-1};\sqrt{\bar{\alpha}_{t-1}}\mathbf{y}_0+\sqrt{\frac{(1-c)(1-\bar{\alpha}_{t-1})}{1-\bar{\alpha}_t}}(\mathbf{y}_t-\sqrt{\bar{\alpha}_t}\mathbf{y}_0),c(1-\bar{\alpha}_{t-1})\mathbf{A}^\top\mathbf{A}\right)\)

for some tunable parameter \(c\in[0,1]\). We choose \(c=\beta_t/(1-\bar{\alpha}_{t-1})\) to match our DDPM variance \(\Sigma_\theta(t)=\beta_t\mathbf{I}\).

## Monte Carlo Guided Diffusion.

Cardoso et al. (2023) use the same optimal proposal \(q_t^*\) in eq. (13) (for sequential measurements) but adopt a terminal measurement model. To improve efficiency, they tilt the targets with the twist function \(\psi_t=g_t(\mathbf{y}_t|\mathbf{x}_t)\). Because of their algorithm’s construction, where the final samples are not reweighted (i.e. \(\tilde{w}_0=1\)), the weight updates are shifted one time step in advance. For _t\>_1,

\(\tilde{w}_t=\frac{p_\theta(\mathbf{x}_{t-1}|\mathbf{x}_t)}{q_t^*(\mathbf{x}_{t-1}|\mathbf{x}_t,\mathbf{y}_{t-1})}\frac{g_{t-1}(\mathbf{y}_{t-1}|\mathbf{x}_{t-1})}{g_t(\mathbf{y}_t|\mathbf{x}_t)}=\frac{p_\theta(\mathbf{x}_{t-1}|\mathbf{x}_t)}{\frac{p_\theta(\mathbf{x}_{t-1}|\mathbf{x}_t)g_{t-1}(\mathbf{y}_{t-1}|\mathbf{x}_{t-1})}{\int p_\theta(\mathbf{x}_{t-1}|\mathbf{x}_t)g_{t-1}(\mathbf{y}_{t-1}|\mathbf{x}_{t-1})d\mathbf{x}_{t-1}}}\frac{g_{t-1}(\mathbf{y}_{t-1}|\mathbf{x}_{t-1})}{g_t(\mathbf{y}_t|\mathbf{x}_t)},\)<br>
\(=\frac{\int p_\theta(\mathbf{x}_{t-1}|\mathbf{x}_t)g_{t-1}(\mathbf{y}_{t-1}|\mathbf{x}_{t-1})d\mathbf{x}_{t-1}}{g_t(\mathbf{y}_t|\mathbf{x}_t)}\approx\boxed{\frac{g_{t-1}(\mathbf{y}_{t-1}|\hat{\mathbf{x}}_{t-1})}{g_t(\mathbf{y}_t|\mathbf{x}_t)}},\) (14)

where we used \(\hat{\mathbf{x}}_{t-1}=\mathbb{E}[\mathbf{x}_{t-1}|\mathbf{x}_t]\) as a single-sample approximation of the integral. Note that, at _t_=1, we get the same weight computation, as \(\psi_0=1\) but the target transition contains an extra term _g_<sub>0</sub>(**y**<sub>0</sub>|**x**<sub>0</sub>) to explain the terminal measurement. To maintain the correct targets in the midst of the shifted weight computations, the first weight is set to be \(\tilde{w}_T=g_{T-1}(\mathbf{y}_{T-1}|\hat{\mathbf{x}}_{T-1})\), where \(\hat{\mathbf{x}}_{T-1}=\mathbb{E}[\mathbf{x}_{T-1}|\mathbf{x}_T]\).

Furthermore, instead of noising **y**<sub>0</sub>, they set \(\mathbf{y}_t=\sqrt{\bar{\alpha}_t}\mathbf{y}_0\), the conditional expectation of the measurement process given the terminal measurement. For experiments, we use the noiseless inpainting version of MCGDiff (i.e. \(\sigma_v=0\) and **A** is a masking matrix), which involves a similar proposal, but we omit the details here.

## Twisted Diffusion Sampler.

Wu et al. (2023) similarly adopt a terminal measurement model, with the twist function \(\psi_t=g_t(\mathbf{y}_0|\hat{\mathbf{x}}_0(\mathbf{x}_t,t))\) and proposal \(q_t^{TDS}\) relying on the likelihood approximation in eq. (4). Their proposal is given by<tbc>

\(q_t^{TDS}(\mathbf{x}_t|\mathbf{x}_{t+1},\mathbf{y}_0)=\mathcal{N}\left(\mathbf{x}_t;\frac{1}{\sqrt{\bar{\alpha}_t}}\left(\mathbf{x}_{t+1}+(1-\alpha_t)s_{t+1}(\mathbf{x}_{t+1},\mathbf{y}_0,t+1)\right),\Sigma_\theta(t)\right),\) (15)

<tbc>where we have the conditional score approximation<tbc>

\(s_t(\mathbf{x}_t,\mathbf{y}_0,t)=s_\theta(\mathbf{x}_t,t)+\nabla_{\mathbf{x}_t}logg(\mathbf{y}_0|\hat{\mathbf{x}}_0(\mathbf{x}_t,t)).\)

<tbc>For _t\>_0, this leads to the weight update

\(\tilde{w}_t=\boxed{\frac{p_\theta(\mathbf{x}_t|\mathbf{x}_{t+1})}{q_t^{TDS}(\mathbf{x}_t|\mathbf{x}_{t+1},\mathbf{y}_0)}\frac{g_t(\mathbf{y}_0|\hat{\mathbf{x}}_0(\mathbf{x}_t,t))}{g_{t+1}(\mathbf{y}_0|\hat{\mathbf{x}}_0(\mathbf{x}_{t+1},t+1))}},\)

which also coincides with the update for _t_=0, as \(\psi_0=1\) and the terminal measurement has to be explained.

