### 2.5.4. Generative Adversarial Networks

Generative adversarial networks (GANs) formulate generative modeling as a two-player game between a generator _G_ and a discriminator _D_ \[GPM\*14\]. The classical minimax objective

\(\mathcal{L}_\text{GAN}=min_Gmax_D\left[\mathbb{E}_{\mathbf{x}\sim p_\text{data}}[logD(\mathbf{x})]+\mathbb{E}_{\mathbf{z}\sim p(\mathbf{z})}[log(1-D(G(\mathbf{z})))]\right]\)

trains _D_ to distinguish real samples **x** from synthesized ones _G_(**z**), while _G_ learns to fool _D_ (Fig. 10). Under an optimal discriminator, this objective can be shown to correspond to minimizing the Jensen–Shannon divergence between the data and model distributions, which motivated later variants based on alternative divergence measures.

In fact, numerous extensions have strengthened the original GAN formulation, improving training stability, sample fidelity, and controllability. For instance, Wasserstein GANs \[ACB17,GAA\*17\] reformulate adversarial training using the Wasserstein-1 (EarthMover) distance, yielding smoother gradients and more stable optimization. Complementarily, PatchGAN discriminators classify local image patches rather than entire images, enabling sharper detail in conditional settings such as image-to-image translation \[IZZE17\].

However, common challenges in training GANs include instability (_e.g._, oscillations or failure to converge), mode collapse (loss of diversity), and sensitivity to the choice of objective and regularization. While Wasserstein objectives and gradient penalties help mitigate these issues, they do not eliminate them entirely \[ACB17, GAA\*17\]. Nonetheless, GANs remain attractive for high-fidelity, sharp synthesis and for learning class- or image- conditional mappings with controllable outputs.

### 2.5.5. Diffusion Models

Diffusion models learn to reverse a process that gradually perturbs data into Gaussian noise \[SWMG15, HJA20\]. The forward process is defined by a variance schedule \(\{\beta_\text{\textit{\textbf{r}}}\}_{\text{\textit{\textbf{t}}}=1}^T\):

\(q(\mathbf{x}_\text{\textit{\textbf{t}}}|\mathbf{x}_{\text{\textit{\textbf{t}}}-1})=\mathcal{N}\big(\sqrt{1-\beta_\text{\textit{\textbf{r}}}}\mathbf{x}_{\text{\textit{\textbf{t}}}-1},\beta_\text{\textit{\textbf{t}}}\mathbf{I}\big),\)<br>
\(\bar{\alpha}_\text{\textit{\textbf{t}}}=\prod_{\text{\textit{\textbf{s}}}=1}^\text{\textit{\textbf{t}}}(1-\beta_\text{\textit{\textbf{s}}}),\mathbf{x}_\text{\textit{\textbf{t}}}=\sqrt{\bar{\alpha}_\text{\textit{\textbf{t}}}}\mathbf{x}_\text{\textit{\textbf{0}}}+\sqrt{1-\bar{\alpha}_\text{\textit{\textbf{t}}}}\epsilon,\epsilon\sim\mathcal{N}(\mathbf{0},\mathbf{I}).\)

A neural network \(\epsilon_\text{\textit{\textbf{0}}}\) is then trained to predict the injected noise from (**x**_<sub>t</sub>,t_) \[HJA20\]. In the commonly used simplified objective, this becomes

\(\mathcal{L}_\text{DDPM}=\mathbb{E}_{\mathbf{x}_\text{\textit{\textbf{0}}},\text{\textit{\textbf{t}}},\epsilon}\left[\left\|\epsilon-\epsilon_\text{\textit{\textbf{0}}}(\mathbf{x}_\text{\textit{\textbf{t}}},\text{\textit{\textbf{t}}},\mathbf{c})\right\|_2^2\right].\)

Conditioning variables **c** (_e.g._, text features) can be incorporated in several ways, including guidance at sampling time and conditioning mechanisms within the denoiser such as cross-attention.

Direct diffusion in pixel space is computationally expensive. Latent diffusion models mitigate this by learning an autoencoder (E,D) and performing the diffusion process in a lower-dimensional latent space **z**=E(**x**), with conditioning (_e.g._, text) injected via cross-attention inside the denoiser \[RBL\*22\] (Fig. 11). Beyond text prompts, additional conditioning modules have been introduced to provide finer control without retraining the full backbone. ControlNet \[ZRA23\] adds condition-specific, zero-initialized branches to incorporate structural signals such as edges, depth, or human pose while preserving the pretrained model. IP-Adapter \[YZL\*23\] introduces a lightweight image-prompt pathway through decoupled cross-attention, enabling style and identity control alongside text conditioning.

Diffusion has been applied to a wide range of modalities, including images \[RBL\*22\], video \[HSG\*22\], audio \[LCY\*23\], and 3D content \[LGT\*23, CCJJ23\], as well as mesh-based textures, as discussed in subsequent sections. Collectively, the core formulation, latent variants, and conditioning mechanisms have evolved into a flexible toolkit that has broadened the practicality of diffusion- based generation.

## 3. Guidance for 3D Mesh Texturing

This section discusses the types of _guidance_ used in neural 3D mesh texturing. Here, guidance refers to the signals or conditions that specify aspects of the desired texture and steer the generative model toward a target result. Broadly, we group guidance into two categories: _structural_ guidance, which constrains the spatial layout or geometric placement of texture on the 3D surface, and _stylistic_ guidance, which specifies the desired appearance of the texture.

High Dimensional Sample Space
Real Images
Real
Discriminative Network D
Low Dimensional Latent Space
Generative Network G
Generated Fake Images
Fake

