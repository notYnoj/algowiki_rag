# Example-based feature painting on textures

SUPPLEMENTARY MATERIAL

ANDREI-TIMOTEI ARDELEAN, Friedrich-Alexander-Universität Erlangen-Nürnberg, Germany

TIM WEYRICH, Friedrich-Alexander-Universität Erlangen-Nürnberg, Germany

### S1 Dataset examples

It is difficult to gauge the quality of the generated textures and the painted features without having a fair understanding of how the training data looks like. Therefore, we include in Fig. 13 and Fig. 14 a set of images from each texture class, presenting all existing features.  2 describes how many images and anomalies, or prominent feature types, are contained in each dataset.

### S2 Additional experiment on latent noise unionization

While our noise-uniformization technique is designed for textures, the concept readily extends to more generic image types, such as panoramas. We demonstrate this by incorporating our improvements in MultiDiffusion [Bar-Tal et al. 2023] to generate large-scale images that are more realistic in terms of internal consistency. The results of this experiment are presented in Fig. 15, comparing our results with a vanilla MultiDiffusion based on Stable Diffusion 2.0. To highlight the benefits of the introduced improvements, we use a stride of 32 for the sliding window. It can be easily seen that our results are more spatially consistent while still exhibiting a realistic amount of variation. This has the added advantage that seams are less noticeable, despite using a large stride. The seams are almost completely eliminated when we additionally use our randomized sliding windows scheme. That is, instead of using a fixed stride, we offset each window by a random amount both horizontally and

vertically. We limit the offset to be less than half of the stride to ensure full coverage of the latent map. The seams seen in the first row of each group could also be resolved by running MultiDiffusion with a stride of 1; however, this would incur a significantly longer running time (18 minutes per image). Moreover, as seen in Fig. 16, the high-level inconsistencies remain even in this case.

We want to stress that our latent noise unionization is complementary to the strategy used to generate large textures. For example, a competitive approach to the noise averaging employed by MultiDiffusion is the noise rolling algorithm introduced in ControlMat [Vecchio et al. 2024]. In Fig. 16, we combine our noise unionization with the noise rolling method for generating arbitrarily large images and show that the results are significantly improved. Our uniformization technique is most useful when there is a high diversity of different images that would fit a given prompt, as it makes it difficult to reconcile adjacent patches (e.g. beach landscape, Fig 16). The noise rolling algorithm has the advantage that each pixel is used just once for each timestep in the diffusion process (equivalent to using a stride of 64). The algorithm is thus significantly faster compared to the full MultiDiffusion (shown in the first row of each group in Fig. 16), with virtually no loss in quality. Wang et al. [2024] also proposed a similar way to improve upon MultiDiffusion in regards to the sampling of patches to be denoised. We, however, do not combine our noise unionization with this method as their mechanism for sampling the random patches is not described with sufficient detail.

### S3 Additional details on the tileable texture synthesis of arbitrary size.

Section 3.5 of the main paper presents our approach to generating textures of arbitrary size using constant GPU memory. Crucially, our noise-uniformization preprocessing ensures that the generated textures are stationary. To avoid seams caused by the patch-based denoising, we set the pixel overlap range to 32 (_i.e._, half the window size). This means the number of evaluations of the diffusion model is 4 times larger compared to an independent generation of the same number of pixels. This constant factor aside, the complexity of texture synthesis is linear with respect to the images resolution, meaning that generating large textures in this manner is time consuming (_e.g._, 170 seconds for a 4096\(\times\)4096 image). We approach this issue by making our textures tileable; this is done by wrapping around the sliding windows circularly during denoising. This strategy directly ensures tileability in the latent space in which the diffusion model operates. In order to obtain tileable texture in RGB space, we first circularly pad the output of the multi-diffusion. Then, the enlarged map is decoded using the Stable Diffusion VAE [Rombach et al. 2022], followed by a crop to the original (unpadded size). The decoded output can then be easily tiled. This allows trading quality

\begin{tabular}{ccccc}
Texture name & K & Normal images & Feature images & Total \\ Tile & 5 & 33 & 84 & 117 \\ Grid & 5 & 21 & 57 & 78 \\ Carpet & 5 & 28 & 89 & 117 \\ Wood & 5 & 19 & 60 & 79 \\ Leather & 5 & 32 & 92 & 124 \\ Pavement & 2 & 0 & 9 & 9 \\ Taboret & 2 & 0 & 1 & 1 \\ Shirt & 1 & 0 & 1 & 1 \\ Puzzle & 1 & 0 & 1 & 1 \\ Wall & 2 & 0 & 5 & 5 \\ Grass & 2 & 0 & 15 & 20 \\ Chair & 1 & 0 & 3 & 3 \\ Blueberries & 2 & 3 & 12 & 15 \\ Dots & 3 & 1 & 6 & 7 \\ SVBRDF & 2 & 0 & 1 & 1 \\ \end{tabular}

2. Overview of each texture category used in our experiments. It includes the number of anomaly/feature types (K), the number of images without anomalies (Normal images), the number of images that contain prominent features, and the total. The first 5 textures are from MVTecAD, the other 10 are acquired by us.

