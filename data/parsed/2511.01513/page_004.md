## 3 Method

Our pipeline consists of three stages (Fig. 3). The first stage is our approach for automatically identifying regions with prominent features by posing that task as a fully-unsupervised anomaly localization problem. This framing is feasible since regions with irregular features break the stationarity assumption of textures, making these regions deviate from the overall statistics. After identifying such regions, the second stage addresses the separation of prominent features in different groups. Leveraging the anomaly maps, we devise an approach for sampling positive and negative pairs of pixels, which are used to optimize a contrastive learning objective. This produces a disentangled feature space that we cluster using _k_-means to obtain pixel-level semantic maps where the labels indicate the feature type or the absence of a prominent feature accordingly. The result of the second stage enables us to train a generative model that follows the desired spatial and semantic conditions. Our diffusion model can generate new textures interactively (1 sec for a 512\(\times\)512 image). Moreover, we demonstrate synthesis of arbitrary size using constant GPU memory, and design a way to avoid distribution drift across the generated texture. Finally, we advance a noise-mixing technique to support texture editing while remaining faithful to the original input. Our editing method even supports transferring blemishes from one texture class to an image of another class.

### 3.1 Prominent feature scoring

The input of our pipeline consists of a handful of photographs of textures that are largely stationary, yet contain prominent features<tbc>

<tbc>that we want to disentangle. These irregularities can be considered anomalies in the context of the global textures, which can be detected using unsupervised anomaly localization.

The initial stage of our pipeline leverages an unsupervised anomaly detection approach, as a first step towards removing the need for manual user annotations, required by previous methods \[Du and Song 2023; Iizuka et al. 2016\]. We employ FCA, the zero-shot anomaly detection method of Ardelean and Weyrich \[2024a\], and apply it to the residual obtained from a VAE-based reconstruction, similarly to Blind LCA \[Ardelean and Weyrich 2024b\]. The output of this step is a set of anomaly-score maps \(\{A_i\}_{i=1}^N\), one for each input image \(\{I_i\}_{i=1}^N\), as shown in the first section of Fig. 3. These methods, however, do not provide a way to threshold the anomaly scores, which have an arbitrary range.

### 3.2 Feature type clustering

Our pixel-level semantic segmentation procedure requires well- defined (binary) anomaly regions. Therefore, we propose an adaptive thresholding function to obtain a binary segmentation _B<sub>i</sub>_ of the areas of interest. Let \(B_i^{xy}:=\left\{\begin{array}{ c c }
1 & A_i^{xy}>\mathcal{T}(A_i) \\
0 & \text{otherwise}
\end{array}\right.\), where T is a function that adaptively computes the threshold based on the anomaly scores. We observed that global thresholding and simple quantiles do not generalize well across different datasets. Otsu’s method \[Otsu et al. 1975\] yields reasonable results, yet it tends to produce segmentations that are too permissive. To reduce the number of false positives, we skew the distribution using an exponential factor: \(\hat{\mathcal{T}}(A_i)=\text{Otsu}(A_i^\beta)^{1/\beta}\), where \(\beta=1.5\) in our experiments.

This function is able to find adequate thresholds across different datasets; however, since it always segments a part of the image as<tbc>

3.1 Prominent feature scoring
VAE
Wide Resnet-50
VAE
FCA
3.2 Feature type clustering
CL features
K-means clustering
Thresholding Equation (1)
LCL
Stratified pair sampling Section 3.2
3.3 Guided texture generation
SD Decoder
Diffusion model
SD Encoder
Noise
+
Frozen weights
LCM
Training

Fig. 3. Our 3-stage pipeline for obtaining a generative model for textures with prominent features.

