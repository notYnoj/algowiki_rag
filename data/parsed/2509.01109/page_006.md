<tbc>During decoding, we first render the GPSTokens **z** into a 2D feature map using Eq. 3, then decode them into the reconstructed image. Following VQGAN \[11\], we use a combination of reconstruction loss _L_rec, perceptual loss _L_perc, and adversarial loss _L_adv during training.

### 3.3 GPSToken-driven Two-stage Image Generation

The shape-texture decomposition property of GPSToken naturally offers a two-stage image generation pipeline, which first synthesizes the image layout using the shape information and then generates the image details using the texture features. This two-stage scheme simplifies the image generation process and improves the generation quality.

**Layout Synthesis.** As illustrated in Fig. 3 (a), in the first stage, we focus on generating the overall structure of the image, which can be represented by the Gaussian parameters.Note that we use the initial Gaussian parameters **g**_<sup>init</sup>_, instead of the final parameters **g**, for layout synthesis. This is because the initial Gaussian parameters are more decorrelated with the local textures and are easier to predict, while they are good enough to represent the image rough layout. Specifically, we first generate the **g**_<sup>init</sup>_ using a simple generative model and then calibrate it to correct potential inaccuracies (see Fig. 3 (c)). The calibration procedure consists of two steps: calibrate the means \(\{\mu_x,\mu_y\}\) of each Gaussian to its nearest valid values and recompute \(\{\sigma_x,\sigma_y,\rho\}\), obtaining the calibrated Gaussian parameters \(\mathbf{g}_{cal}^{init}\). The detailed calibration can be found in Algorithm 2 in the **Appendix**.

**Texture Generation.** After synthesizing the overall structure of the image, we enrich the generated layout with detailed textures (see Fig. 3 (b)) using diffusion models such as SiT \[23\]. Specifically, we first convert \(\mathbf{g}_{cal}^{init}\) into embedding vectors and incorporate them as additional inputs in each timestep. This ensures that the newly generated texture features accurately reflect the constraints of the original layout while preserving structural consistency and rich details in the final image. In practice, the model predicts a Gaussian parameter residual \(\Delta\mathbf{g}\) and texture features **f**. The Gaussian parameters are updated by \(\mathbf{g}=\mathbf{g}_{cal}^{init}+\Delta\mathbf{g}\), while **f** captures the specific texture characteristics of each token. The results can be rendered and reconstructed into natural images using our GPSToken decoder.

The two-stage generation pipeline significantly reduces the complexity of image generation by decoupling geometric modeling from texture synthesis. The \(\mathbf{g}_{cal}^{init}\) acts as a structural constraint, simplifying the texture generation task while ensuring spatial consistency. It aligns with the human perception process (from structure to detail). Additionally, since layout synthesis is much easier than texture generation, we employ a simple network or cached database to produce results in the first stage, introducing minimal additional computation compared to existing methods.

## 4 Experiments

### 4.1 Experimental Settings

**Training Data and Settings.** We train all models on the ImageNet dataset \[30\], which contains 1.28M training images and 50K validation images. During preprocessing, images are resized to \(256\times 256\) and center-cropped without additional augmentation beyond horizontal flipping. We implement three variants of GPSToken: GPSToken-S64 (64 tokens), GPSToken-M128 (standard setting, used<tbc>

Noises
Guassian parameters g
Decoder
Rendering
Textual features f
i. means calibration
ii. sigmas reinitization
Diffusions
ginit
x
Simple Net
Layout condition
Calibrate
+
ginit
init
g cal
z = {g, f}
init
g
(a) Layout Synthesis
(b) Conditional Texture Generation
(c) Visual Results

Figure 3: The overview of two-stage generation pipeline based on GPSToken.

