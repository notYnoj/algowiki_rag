the burden on downstream tasks. Second, the Gaussian function provides a smooth, continuous weight distribution over pixels, naturally capturing uncertainty and modeling soft or ambiguous boundaries in natural images. Third, GPSToken is fully differentiable, enabling end-to-end training and seamless integration into existing gradient-based learning frameworks. In contrast, bounding boxes are restricted to rigid, axis-aligned shapes and exhibit hard, non-differentiable boundaries. Segmentation maps, while precise, are high-dimensional, discrete, and inherently incompatible with differentiable optimization.

## 3.2 Spatially-adaptive GPSToken Learning

Image tokenizers typically use an encoder-decoder framework, where the encoder maps the image **x** to a latent representation **z**=Enc(**x**), and the decoder reconstructs it as \(\hat{\mathbf{x}}=\text{Dec}(\mathbf{z})\). Our GPSToken also follows this framework. As shown in Fig. 2 (a), we first apply an iterative algorithm to partition the image into regions of varying sizes based on texture complexity. Each region’s position and size initialize the Gaussian parameters of the corresponding GPS-tokens, providing a coarse spatially- adaptive representation. Next, a transformer-based encoder refines GPS-tokens for fine-grained adaptation, adjusting the position, shape, and orientation according to regional textures. Finally, the GPSTokens are converted back to 2D feature maps and passed through a decoder to reconstruct \(\hat{\mathbf{x}}\).

**Spatially-adaptive Token Initialization.** As shown in Fig. 2 (b), we use an iterative algorithm to initialize Gaussian parameters aligned with local regions. Specifically, we maintain a dynamic list of region candidates and iteratively split the most complex regions into simpler sub-regions until the target number is reached. We measure region complexity using gradient entropy. We compute the gradient magnitude map _E_ via the Sobel operator \[32\], then calculate the information entropy _H_ from the histogram of _E_. The overall metric is defined as:

\(m=hw\times H^\lambda=hw\times\left(-\sum_{i=1}^{512}q_ilog(q_i)\right)^\lambda,\) (4)

where _h_ and _w_ are the spatial size of regions, _q<sub>i</sub>_ is the probability of gradients in the _i_-th histogram bin, and \(\lambda\) balances size and complexity. By integrating region size into the metric, we promote division of larger regions. A higher _m_ value indicates a larger and more complex region.

Once regions are determined, we associate the _i_-th GPSToken **z**_<sub>i</sub>_ with the _i_-th region and initialize its Gaussian parameters as \(\mathbf{g}_i^{init}=\{\sigma_x^{(i)},\sigma_y^{(i)},\rho^{(i)},\mu_x^{(i)},\mu_y^{(i)}\}=\{\frac{w_i}{6},\frac{h_i}{6},0,x_i,y_i\}\), where _h<sub>i</sub>_, _w<sub>i</sub>_ are the height and width of regions, and (_x<sub>i</sub>,y<sub>i</sub>_) is its center. Setting \(\sigma_x^{(i)}\) and \(\sigma_y^{(i)}\) to \(\frac{1}{6}\) of _w<sub>i</sub>_ and _h<sub>i</sub>_ ensures full coverage during rendering. Please see Algorithm 1 in the **Appendix** for more details.

**Spatially-adaptive Token Refinement.** After obtaining the initialized Gaussian parameters, we employ a transformer-based encoder to refine these parameters to achieve fine-grained spatial adaptation, while simultaneously extracting the corresponding texture features **f** for each region.

As shown in Fig. 2(c), the encoder first projects the initial Gaussian parameters **g**_<sup>init</sup>_ into query embeddings, which are then processed by attention blocks. To focus each embedding on its corresponding region, we include region-specific features as conditions. Specifically, we extract image features via residual blocks and use RoIAlign \[12\] to obtain fixed-size features for each region. These are added to the query embeddings before each attention block. This ensures that each query interacts with its local image features, improving alignment with regional textures.

Additionally, self-attention blocks enable query embeddings to interact with each other, considering the global image layout during training. The encoder outputs residuals \(\Delta\mathbf{g}\) for refining Gaussian parameters and textual features **f** for each token. The final GPS-tokens are:

\(\mathbf{z}=\{\mathbf{g}^{init}+\Delta\mathbf{g},\mathbf{f}\}.\) (5)

The refined Gaussian parameters **g** define the spatial layout and overall structure of the image, while **f** encode the textual patterns of Gaussians. They work synergistically to represent the whole image.

To illustrate the spatial adaptation of GPSTokens, we visualize **g**_<sup>init</sup>_ and **g** as Gaussian maps in Fig. 2. As shown in Fig. 2(a), the initial map **g**_<sup>init</sup>_ aligns with the region partitions. Complex regions have denser Gaussians, while simpler ones use fewer, larger Gaussians. After encoder refinement, the parameters better match local textures. While **g**_<sup>init</sup>_ contains only axis-aligned Gaussians, the refined **g** includes rotated ones that align better with local structures, such as the dog’s ear edges.

