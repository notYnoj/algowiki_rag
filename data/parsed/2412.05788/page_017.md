## A Additional Background

### A.1 Diffusion Models and Protein Structure

#### Denoising Diffusion Probabilistic Models (DDPMs).

Recall that diffusion models learn to reverse a diffusion process applied to a target distribution _q_(**x**<sub>0</sub>). Here, we outline them in more detail under the framework of denoising diffusion probabilistic models (DDPMs) (Ho et al., 2020). In general, their dynamics are governed by a _forward (diffusion)_ process and a _reverse (denoising)_ process--both of which are Markovian. Adopting the terminology of Ho et al. (2020), we start with the forward process with a transition kernel<tbc>

\(q(\mathbf{x}_t|\mathbf{x}_{t-1}):=\mathcal{N}\left(\mathbf{x}_t;\sqrt{1-\beta_t}\mathbf{x}_{t-1},\beta_t\mathbf{I}\right),\) (8)

<tbc>for some decreasing variance schedule \(\beta_1,\dots,\beta_T\in(0,1)\). Equivalently, denoting \(\alpha_t:=1-\beta_t\) and \(\bar{\alpha}_t:=\prod_{s=1}^t\alpha_s\), the noising process can be done in a single step via<tbc>

\(q(\mathbf{x}_t|\mathbf{x}_0)=\mathcal{N}\left(\mathbf{x}_t;\sqrt{\bar{\alpha}_t}\mathbf{x}_0,(1-\bar{\alpha}_t)\mathbf{I}\right).\) (9)

<tbc>For large enough _T_, we have _q_(**x**_<sub>T</sub>_|**x**<sub>0</sub>)≈N(**x**_<sub>T</sub>_; **0**, **I**). As a result, the forward process constructs a bridge from the data distribution _q_(**x**<sub>0</sub>) to the Gaussian distribution N(**0**,**I**). Naturally, the _time reversal_ of this process maps Gaussian samples back to the data distribution. DDPMs do this by learning to measure the total noise accumulated from the forward process. Manipulating eq. (9) above, we can write<tbc>

\(\mathbf{x}_0=\frac{1}{\sqrt{\bar{\alpha}_t}}\left(\mathbf{x}_t-\sqrt{1-\bar{\alpha}_t}\epsilon_t\right),\text{where}\epsilon_t\sim\mathcal{N}(\mathbf{0},\mathbf{I}),\) (10)

<tbc>which enables reconstructing the clean sample upon predicting the total noise. The reverse process, however, is done gradually rather than in a single step through the transition kernel<tbc>

\(p_\theta(\mathbf{x}_{t-1}|\mathbf{x}_t):=\mathcal{N}\left(\mathbf{x}_{t-1};\mu_\theta(\mathbf{x}_t,t),\Sigma_\theta(t)\right),\)

<tbc>parameterised by

\(\mu_\theta(\mathbf{x}_t,t):=\frac{\sqrt{\bar{\alpha}_t}(1-\bar{\alpha}_{t-1})}{1-\bar{\alpha}_t}\mathbf{x}_t+\frac{\sqrt{\bar{\alpha}_{t-1}}\beta_t}{1-\bar{\alpha}_t}\hat{\mathbf{x}}_0(\mathbf{x}_t,t)\Sigma_\theta(t):=\beta_t\mathbf{I},\)<br>
\(=\frac{1}{\sqrt{\bar{\alpha}_t}}\left(\mathbf{x}_t-\frac{1-\alpha_t}{\sqrt{1-\bar{\alpha}_t}}\epsilon_\theta(\mathbf{x}_t,t)\right),\)

where \(\epsilon_\theta(\mathbf{x}_t,t)\) is the total noise as predicted by a denoising network and \(\hat{\mathbf{x}}_0(\mathbf{x}_t,t)\) is the predicted clean sample found by substituting \(\epsilon_\theta(\mathbf{x}_t,t)\) into eq. (10). The procedure to generate samples \(\mathbf{x}_0\sim q(\cdot)\) then involves the reverse process

\(p_\theta(\mathbf{x}_{0:T})=p(\mathbf{x}_T)\prod_{t=1}^Tp_\theta(\mathbf{x}_{t-1}|\mathbf{x}_t),\)

first sampling from **x**_<sub>T</sub>_∼N(**0**,**I**) then gradually denoising the samples for _T_ steps.

A key connection can be made with score-based generative models (SBGMs) (Song and Ermon, 2019) in their learning objectives. SBGMs predict the _score function_ \(s(\mathbf{x})=\nabla_\mathbf{x}logq(\mathbf{x})\), a vector that points in the direction of areas with high density in the data distribution. Taking the gradient of the log density of eq. (9), we precisely have

\(s_\theta(\mathbf{x}_t,t)=-\frac{\epsilon_\theta(\mathbf{x}_t,t)}{\sqrt{1-\bar{\alpha}_t}}.\)

When working with denoising networks, we use this relationship to compute the score.

