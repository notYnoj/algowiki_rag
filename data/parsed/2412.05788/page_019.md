## A.2 SMC-Aided Diffusion Posterior Samplers

With SMC, we reiterate that two main design choices are available: the proposals _q<sub>t</sub>_ and the intermediate targets \(\gamma_t\). In this section, we detail the specific choices made by the SMC samplers considered in our experiments. We first outline how a linear structure to the inverse problem can define a noisy measurement process. This is utilised by two existing samplers, FPS-SMC and MCGDiff, that operate on linear problems. Then, we discuss how each sampler fits the recipe in Alg. 1. Seeing as the weight updates can be a source of confusion, we show their derivations. Where there are distributions that we are free to design, we time-index them.

### Linear Measurement Process.

We follow the construction by Dou and Song (2023) for producing a measurement process under a linear inverse problem<tbc>

\(\mathbf{y}_0=\mathbf{Ax}_0+\sigma_v\mathbf{z}_0,\)

<tbc>where \(\mathbf{y}_0\in\mathbb{R}^d\), \(\mathbf{x}_0\in\mathbb{R}^D\), \(\mathbf{A}\in\mathbb{R}^{d\times D}\), and **z**<sub>0</sub>∼N(**0**,**I**). Recall that the DDPM’s forward process (8) can be written as<tbc>

\(\mathbf{x}_t=\sqrt{1-\beta_t}\mathbf{x}_{t-1}+\sqrt{\beta_t}\mathbf{z}_{t-1},\)

<tbc>for **z**<sub>_t_-1</sub>∼N(**0**,**I**). Applying the matrix **A** to this recursion, we can define an analogous measurement process<tbc>

\(\mathbf{y}_t=\sqrt{1-\beta_t}\mathbf{y}_{t-1}+\sqrt{\beta_t}\mathbf{A}\mathbf{z}_{t-1},\)

<tbc>where **z**<sub>_t_-1</sub> is randomly sampled or chosen to be equal to the noise applied in the latent forward process. The intermediate noisy measurements can then be constructed by

\(\nu(\mathbf{y}_{1:T}|\mathbf{y}_0)=\prod_{t=1}^T\nu(\mathbf{y}_t|\mathbf{y}_{t-1}),\) (11)

where \(\nu(\mathbf{y}_t|\mathbf{y}_{t-1})=\mathcal{N}(\mathbf{y}_t;\sqrt{1-\beta_t}\mathbf{y}_{t-1},\beta_t\mathbf{A}\mathbf{A}^\top).\)

Using the above recursions and the inverse problem statement, the likelihood has the form

\(g(\mathbf{y}_t|\mathbf{x}_t)=\mathcal{N}(\mathbf{y}_t;\mathbf{A}\mathbf{x}_t,\sigma_v^2\bar{\alpha}_t\mathbf{I}),\) (12)

and its logarithm’s gradient is precisely the guidance term for replacement methods. From here, we can develop a simple particle filter by considering BPF, the baseline sampler for SSMs.

**Bootstrap Particle Filter.** For now, let us assume a (filtering) model with sequential measurements and the likelihood in eq. (12). In BPF, the proposal _q<sub>t</sub>_ matches the DDPM’s reverse kernel \(p_\theta\) and the target \(\gamma_t\) is the joint distribution between the latent and measurement variables. Under this choice, the weight update becomes

\(\tilde{w}_t=\frac{p_\theta(\mathbf{x}_t|\mathbf{x}_{t+1})g_t(\mathbf{y}_t|\mathbf{x}_t)}{p_\theta(\mathbf{x}_t|\mathbf{x}_{t+1})}=\boxed{g_t(\mathbf{y}_t|\mathbf{x}_t)},\)

and the likelihood values essentially become the fitness criteria for filtering samples.

To improve the efficiency of BPF, we can choose _q<sub>t</sub>_ to be the locally _optimal proposal_ \(q_t^*\), better estimating the target with fewer particles. This notion is formalised by minimising the KL-divergence between \(\gamma_{t+1}(\mathbf{x}_{t+1:T})q_t(\mathbf{x}_t|\mathbf{x}_{t+1})\) and \(\gamma_t(\mathbf{x}_{t:T})\). For SSMs, this is a known result with<tbc>

\(q_t^*(\mathbf{x}_t|\mathbf{x}_{t+1},\mathbf{y}_t)\propto\underbrace{\frac{\gamma_t(\mathbf{x}_{t:T})}{\gamma_{t+1}(\mathbf{x}_{t+1:T})}}_{\tilde{f}_t(\mathbf{x}_t|\mathbf{x}_{t+1})}=p_\theta(\mathbf{x}_t|\mathbf{x}_{t+1})g_t(\mathbf{y}_t|\mathbf{x}_t),\)

<tbc>where \(\tilde{f}_t\) is what we refer to as the transition between targets. Note that this can be different for a terminal measurement model, where we do not need to explain each intermediate measurement, only the last one.

