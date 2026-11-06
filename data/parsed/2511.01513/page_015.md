## S6 Additional high-resolution results

Our method lends itself to high-resolution generation and editing. In Figures 20, 21, we add results generated at high-resolution, presenting various painted features. Fig. 22 includes additional high- resolution editing results.

## S7 Comparison Addition

We include in Fig. 23 a representative failure case of Diffusion Texture Painting [Hu et al. 2024], as referenced in the main paper.

## S8 Comparison of different thresholding functions

In Section 3.1, we introduce our thresholding function, together with the theoretical justification for combining a local and global threshold. In Fig. 24 we present some representative results for alternative thresholding schemes that we considered. That is, we compare our approach to using local (per-image) quantiles, dataset- level quantiles, and Otsu’s method.

## S9 Timings

As presented in the main paper, our pipeline is trained in 3 stages: anomaly detection, feature clustering, and diffusion-based synthesis. The first stage resembles the detection part of BlindLCA [Ardelean and Weyrich 2024b], which takes about 5 minutes. The second stage performs the binarization, mines the positive and negative pairs of connected components, and performs the contrastive learning; the time is dominated by the last step, taking around 15 minutes. The third stage is by far the most time-consuming: training the diffusion model to convergence takes between 6 and 12 hours on an A5000 NVIDIA GPU. This time, however, could be greatly reduced by using a more fitting pre-training, with more textures compared to the DTD dataset used in our experiments.

The training time is a drawback of our approach compared to single-exemplar texture synthesis methods (_e.g._, Image Analogies [Hertzmann et al. 2001], Guided Correspondence [Zhou et al. 2023]); however, after training, our method can generate new images quickly, enabling interactive texture authoring. During inference we perform 18 steps with the Heun solver, taking around 1 second for a<tbc>

<tbc>512\(\times\)512 image, as shown in  3. This , however, shows the timing for generating a new texture with a given mask. Editing an existing image requires an additional inversion step. Since we use an Euler solver with 4 fixed-point iterations, the number of diffusion model calls (NFE) is significantly larger. In the experiments performed in the main paper we use 250 steps (1000 NFE), taking about 15.5 seconds per image. After inversion, our noise-mixing editing does another 250 NFE, taking around 4.5 seconds. The time spent on encoding and decoding using the Stable Diffusion VAE is negligible, which means the total time for editing is 20 seconds. That being said, our interactive editing framework benefits from the ability to dynamically choose the numbers of steps performed by the diffusion model. Namely, the user can use a small number of steps at the beginning of the editing sessions and only use the full number of steps to synthesize the final result. Importantly, our noise-inversion on real images performs well even with significantly fewer steps, as seen in Fig. 25. Note that after 40 steps the returns in quality are minimal and the inverted image converges to the VAE representation. The mean absolute error (MAE) is dominated by the loss of information during encoding-decoding. For the interactive editing (as presented in the supplementary video) we only use 42 steps.

## S10 Detailed numerical results

We include in  4 the detailed quantitative results of our method, and compare them with the metrics obtained using BlindLCA [Ardelean and Weyrich 2024b]. We use macro averaging for the F1-score to emphasize the importance of detecting all feature types. Note that<tbc>

\begin{tabular}{cc}
Method & Time (s) \(\downarrow\) \\
Image Analogies [Hertzmann et al. 2001] & 1200 \\
Guided Correspondence [Zhou et al. 2023] & 224 \\
Neural Style Transfer [Gatys et al. 2016] & 75 \\
Texture Reformer [Wang et al. 2022b] & 0.34 \\
Ours & 0.98 \\
\end{tabular}



Fig. 14. Overview of our 9 textures, captured using a handheld phone camera.

3. Comparison of inference time.

