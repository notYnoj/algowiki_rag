<tbc>At the end, we perform a nearest neighbour projection on the largest scale: each patch in the generated _x_ is matched to its nearest patch in the target _u_. Then, each pixel is reconstructed by averaging the corresponding patches. In Fig. 30 we observe an example of this process for a single scale. For this simple example, even the lighter mono-scale model produces satisfactory results.

## A.9.7 Image Generation

As a proof of concept, we train a Generative Adversarial Network (GAN) \[Goo+14; ACB17; DZS18\] using the Mixture-Wasserstein distance as a regularisation. The idea is to encourage the generator to produce images which have similar features to real images: while this does not suffice to produce realistic images, it can guide the training optimisation out of spurious local minima induced by the notoriously unstable GAN training (\[ACB17\]). Given a batch size _b_ and a latent dimension \(\ell\), we independently sample \(x_1,\cdots,x_b\sim\mathcal{N}(0_\ell,I_\ell)\), and we draw \(y_1,\cdots,y_b\) from our dataset of real images. The aim of our _generator_ \(\mathsf{G}:\mathbb{R}^\ell\longrightarrow\mathbb{R}^{C\times H\times W}\) is to map these Gaussian samples to real images of height _H_, width _W_ and _C_ channels. We also introduce a _feature extractor_ \(\mathsf{F}:\mathbb{R}^{C\times H\times W}\longrightarrow\mathbb{R}^f\) which learns to map images to relevant features of dimension _f_, and a _discriminator_ \(\mathsf{D}:\mathbb{R}^f\longrightarrow\mathbb{R}\) whose goal is to discriminate real and fake images by producing different vectors of features. The full adversarial objective on a noise batch _X_ and a real image batch _Y_ is then defined as follows:

\(min_\mathsf{G}\left[\mathrm{MW}_2^2\left(F^T(\theta_0,\mathsf{F}\circ\mathsf{G}(X)),F^T(\theta'_0,\mathsf{F}(Y))\right)+\mathrm{max}_{\mathsf{F},\mathsf{D}}\left(\sum_{i=1}^b\mathrm{log}\mathsf{D}\circ\mathsf{F}\left(y_i\right)+\mathrm{log}\left(1-\mathsf{D}\circ\mathsf{F}\circ\mathsf{G}(x_i)\right)\right)\right],\) (82)

where \(\theta_0\) and \(\theta'_0\) are chosen using _k-means_ initialisation. Note that the feature extractor F appears in the \(\mathrm{MW}_2^2\) term, but gradients from this term are not used to update F. We optimise these losses using Stochastic Gradient Descent and _Full Automatic Differentiation_ (see Section 2.3). For every sampled batch, we alternate one step on F and D, then one step on G. The generator is encouraged to produce images with similar features to the real ones, and aims to fool the discriminator. The feature extractor F attempts to extract features such that D is able to discriminate real from fake images. The full network architecture is described in Appendix A.9.7. Note that as in other GANs \[Goo+14; ACB17; DZS18\], we do not optimise over the full dataset and rather optimise by sampling mini-batches at each step, incurring a seldom-discussed bias \[Fat+20; Fat+21b; Fat+21a; Ton+24\] for computational efficiency.





(a)

(b)

Figure 30: (a) Texture synthesis with \(12\times 12\) patches, _K_=4, mono-scale, (b) reference.

