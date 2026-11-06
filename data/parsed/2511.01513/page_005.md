<tbc>anomalous it will inevitably yield false positives on textures that are completely stationary. To overcome this issue, we compute a global threshold and segment each anomaly map based on the maximum between the local and global thresholds:

\(\mathcal{T}(A_i):=\mathrm{max}(\text{0tsu}(\{\hat{\mathcal{T}}(A_j)\}_{j=1}^N),\hat{\mathcal{T}}(A_i)).\) (1)

We empirically validate our thresholding function in the supplementary material (Sec S8).

To enhance the authoring control of the final generative model, we are interested in grouping the prominent features of the same type into clusters. Based on the binary detection of anomalous regions, we identify the various types of features through contrastive learning (CL) and clustering. As opposed to prior work \[Ardelean and Weyrich 2024b\], we are interested in pixel-level rather than image-level clustering. Moreover, we do not assume there is only one possible anomaly type per image, making the method more flexible and applicable in practical scenarios. To this end, we divide each image into regions by computing the connected components in the binary masks _B<sub>i</sub>_. For simplicity, it is reasonable to assume that each such region either belongs to the normal class or contains a single type of feature. We then compute region-level descriptors by averaging the pixel-level features extracted by a pretrained WideResnet-50 network, and use the descriptors to find positive pairs as nearest neighbors. Importantly, we observe that naively creating negative pairs for contrastive learning by sampling regions that are far away in feature space yields poor results. As shown in Fig. 26, this is due to the oversampling of the normal class, which limits the effectiveness of contrastive learning to separate the various anomaly types. We alleviate this problem by sampling negative pairs in a stratified manner, _i.e._, the regions are preclustered using _k_-means based on the computed feature descriptors, and negative pairs are<tbc>

<tbc>sampled equally across these clusters. The number of classes used for preclustering is a free hyperparameter of our method; that being said, we observed that using the same number of classes as for the final clustering is a robust choice.

The positive and negative pairs are used to train a 3-layer CNN, with a receptive field of 5\(\times\)5, optimizing for the InfoNCE \[Oord et al. 2018\] contrastive objective. After training, the CL-features produced by the neural net are easily separable into clusters: to obtain pixel-level segmentations, we pool the CL-features for all pixels in all input images and cluster them using _k_-means.

## 3.3 Guided texture generation

The output of the clustering stage consists of _N_ label maps \(\{L\}_{i=1}^N\) with values from 0 (normal class) to _K_, the number of feature types in the dataset. We leverage the label maps as conditioning for a diffusion model \[Ho et al. 2020\] (DM) trained to generate the same set of images \(\{I_i\}_{i=1}^N\).

Diffusion models are a class of generative models that synthesize outputs through progressive denoising. We include here a brief explanation of the concept of diffusion models, and refer the reader to a more extensive analysis of these models \[Ho et al. 2020; Karras et al. 2022; Song et al. 2021a,b\]. Let _p_<sub>data</sub>(**_x_**) be the distribution of the data to be modeled; in our case, natural textures. The forward diffusion process pushes samples away from the true data distribution by adding i.i.d. (independent identically distributed) Gaussian noise with standard deviation \(\sigma(t)\). The noise is increasing with the timestep _t_, so that for a large enough _t<sub>N</sub>_ the resulting distribution \(p(x;\sigma(t_N))\) is virtually identical to the normal distribution \(\mathcal{N}(0,\sigma(t_N)^2I)\). Sampling from _p_<sub>data</sub>(**_x_**) can be achieved by reversing the diffusion process. In practice, this is implemented by a progressively applied, learned denoising function, starting from pure noise<tbc>

Input
Ours
BlindLCA
STEGO

Fig. 4. Results of our pixel-level anomaly segmentation. We seek to have the background pixels mapped to a single class and the different features to distinct labels. The figure compares the results of our approach, BlindLCA \[Ardelean and Weyrich 2024b\], and STEGO \[Hamilton et al. 2022\].

