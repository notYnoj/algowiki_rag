<tbc>autoencoder and a diffusion model. The synthesis if thus performed in the abundance space, which enables to obtain realistic objects’ distribution in abundance maps. However, this method focuses on the spectral profiles consistency rather than on the texture representativity of the different natural background components, such as forest, sky, grassland... Another publication \[18\] emphasizes the use of a diffusion model for the synthesis of hyperspectral images, but with a conditional RGB image as input. They introduce a conditional vector quantized generative adversarial network (VQGAN) to map hyperspectral data into a low-dimensional latent space, in which the diffusion model is easier to train. They pay particular attention to the diversity of the generated hyperspectral images, by proposing two new metrics focusing on spectral content diversity. The syntheses are evaluated using both pixel-wise metrics such as RMSE, spectral angle mapper (SAM), and PSNR, and the structure similarity index metric SSIM for evaluating the quality of spatial information. Additionally, foundation models--trained on vast unlabelled datasets and fine-tuned for specific tasks using limited annotated data--have seen increased use in satellite imagery over the past two years. FG-MAE \[35\] and SatMAE \[6\] have been developed for multispectral Sentinel-2 images, and DOFA \[36\] has been very recently proposed to adaptively integrate various data modalities into a single framework, leveraging the concept of neural plasticity in brain science. These foundation models will undoubtedly contribute to strengthen multispectral image analysis capabilities.<br>
These models have only been applied on satellite data, and mostly on data taken over cities, not on textured natural backgrounds.

### c) Neural texture synthesis:

The work from Gatys et al. \[8\] was a major breakthrough for exemplar-based texture synthesis. The main idea of this work, that we will detail in Section III-A, is to constrain some statistics on deep image features extracted by classical classification networks that have been trained on large image datasets (such as the VGG19 network trained on ImageNet). More precisely, second order statistics between deep features are computed on an exemplar image through Gram matrices and images are then synthesized by optimizing the pixel responses to match these matrices. This results in very realistic synthesized texture images, although at the price of a relatively heavy optimization procedure for each synthesis. Many works have followed, all exploiting the central idea of measuring distance between texture images through the squared difference between their Gram matrices, distances that in this paper we will call _style distances_. A particular interest was devoted to develop feed-forward architecture to speed-up the synthesis \[33\], use the style distances in the GAN framework \[12\] or to develop auto-encoder texture synthesizers \[2\]. To the best of our knowledge, none of these state-of-the-art texture synthesis approaches have been adapted to the multispectral or hyperspectral framework, which is the purpose of the present paper.

## III. METHODS

### A. Neural statistics for texture synthesis

As recalled in the previous section, the method from Gatys et al. \[8\] rely on the use of statistics of deep features. These features are classically obtained from the VGG19 network. It consists of a succession of convolutional layers. Each layer _l_ is made of _N<sub>l</sub>_ convolutional filters and provides a feature map \(F^l\in\mathbb{R}^{N_l\times M_l}\) (where _M<sub>l</sub>_ is the number of pixels of the feature map). The Gram matrices were chosen by the authors to form a summary statistic that is blind to spatial information:

\(\forall l\in\{1,\dots,L\},G^l=F^l\left(F^l\right)^T.\) (1)

The set \(G=\left\{G^1,\dots,G^L\right\}\) of Gram matrices computed from the network in response to an image constitutes a stationary multi-scale description of the texture. It can further be used to define a style distance between two images _I_ and \(\hat{I}\) with Gram matrices _G_ and \(\hat{G}\):

\(\mathcal{L}_{style}\left(I,\hat{I}\right)=\sum_lw_l\left(G^l-\hat{G}^l\right)^2,\) (2)

where the _w<sub>l</sub>_ are chosen weighting factors.

This style distance was used in \[8\] to achieve a clear breakthrough for texture synthesis. It was also later used to train other neural networks as a loss function \[33\] \[16\] \[2\]. In this work, we follow the exemplar synthesis process presented by \[8\]: given an exemplar image _I_, a synthetic image \(\hat{I}\) is initialized with a Gaussian white noise and then gradient descent is used to minimize the style distance between the two images _I_ and \(\hat{I}\). The result of this optimization is expected to match the Gram matrices of the exemplar. In the following, we chose to initialize the synthetic image following a Gaussian noise with the mean and covariance of the original image as it showed better performances.

This style distance makes use of the Gram matrices to describe the feature maps distributions, but other statistics as covariance matrices (i.e. Gram matrices of the centered feature maps) have also shown good performances for texture synthesis.

We chose to use the latter in our work.

The main obstacle to the extension of CNN based texture synthesis processes to multispectral imaging is the design and the training of a multispectral CNN from which to extract feature maps statistics. To address this, we introduce a stochastic style distance in section III-B and a style distance that makes use of projection in section III-C. In section III-D, we add a color operation to the projection to align the color distributions with those of the images the network has been trained on. These distances enables one to use the VGG19 network, pre-trained on ImageNet, that has become standard for 3-channels images.

### B. Stochastic style distance

The difficulty to extend the approach recalled in the previous paragraph to multispectral images is to constrain the statistics of an image of dimension _N_ with an optimization procedure

