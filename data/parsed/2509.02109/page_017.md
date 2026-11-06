<tbc>Mixture Loss defined in Section 3.4: by relaxing the constraints on marginals, it can ignore outliers in the input distributions. Specifically, in Fig. 8, we consider an illustration with a corrupted target image where a patch of red has been added, and observe that the unbalanced approach is more robust to this aberration, showing no propagation of the red artifact.

## 5.3 Neural Style Transfer

We apply our distance within Gatys et al.’s neural style transfer framework \[GEB16\]. The goal is to generate an image that combines the content of one image _X_<sub>0</sub> with the artistic style of another image _Y_ . We rely on a pre-trained VGG-19 network \[SZ15\] (see Fig. 9a) to encode our image and extract relevant features from three specific layers \(\ell\). Given an image _X_ in \(\mathbb{R}^{3\times H\times W}\), we denote these features VGG\(_{1\dots\ell}(X)\). Starting with the content image as _X_<sub>0</sub>, we optimise _X_ such that its features progressively match those of the style image _Y_ . The target mixtures \(\overline{\mu_\ell^\text{style}}\) are fitted at the beginning of the procedure on style features VGG\(_{1\dots\ell}(Y)\). Notably, the target style is encoded as a low-dimensional GMM, and the reference image is not needed during training, unlike in \[GEB16\]. Our objective is a weighted sum of Mixture Losses between the optimised features VGG\(_{1\dots\ell}(X)\) and the target \(\overline{\mu_\ell^\text{style}}\), for each layer \(\ell\) in {1,2,3}: we solve

\(min_{X\in\mathbb{R}^{3\times H\times W}}\sum_{l=1}^3\lambda_\ell\text{MW}_2^2\left(F(\theta_\text{init},\text{VGG}_{1\dots\ell}(X)),\overline{\mu_\ell^\text{style}}\right).\) (23)

The weights \(\lambda_\ell\) follow Gatys et al.’s scheme (\[GEB15\]) of \(1/d_\ell^2\) where \(d_\ell\) is the dimension of features in layer \(\ell\). We fit _K_=3 Gaussian components at each layer. The chosen procedure for fitting Gaussian mixtures is still _Warm-Start EM_. We optimise using 100 iterations of Adam with learning rate 0.01, which takes approximately 20 seconds using CUDA on an RTX 4000. The example results shown in Fig. 9 illustrate the ability of GMM to encode (and store) an image style which, to the best of our knowledge, has never been shown. The experimental setup is further detailed in Appendix A.9.5, along with additional examples.

## 5.4 Texture Synthesis

We perform texture synthesis using a novel method inspired by \[GLR18; LDD23; Hou+23\]. We initialise the synthesised texture using a stationary Gaussian field of the same mean and covariance<tbc>

Source
Result
Target
Balanced result
Unbalanced result
Corrupted target

Figure 8: Colour transfer experiments. Top row: \(\text{EM}-\text{MW}_2^2\) from source to target. Bottom row: unbalanced colour transfer with regularisations \(\lambda_1=10\) (source) and \(\lambda_2=0.1\) (target).

