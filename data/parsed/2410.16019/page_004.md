<tbc>that relies on a RGB CNN. To do so, we decide to constrain the statistics of all possible 3-channels images obtained from the channels of the multispectral image.

We consider an exemplar multispectral image _I_ with _N_ spectral bands and \(\hat{I}\) its synthetic counterpart. We propose to randomly draw a triplet _J_ of integers in {1_,...,N_} at each iteration of the optimization. Then, to evaluate the style distance \(\mathcal{L}_{style}\left(I_J,\hat{I}_J\right)\) between the images _I<sub>J</sub>_ and \(\hat{I}_J\) made of the spectral bands indexed by the integers of _J_. Finally, the gradient of this quantity is used to take an optimization step on \(\hat{I}\).

During the optimization, one can average the style distance over batches of uniformly drawn triplets in a way that is reminiscent with stochastic gradient descent algorithms. It ensures to take into account more spectral bands and correlations at each iterations. Moreover, it regularizes the objective function.

The global minimization objective of our algorithm is the expectation of the style distance between 3-channels images corresponding to the spectral bands indexed by a triplet _J_ that follows the uniform law. This amounts to averaging the style distance over all possible triplets :

\(\mathcal{L}_{style}^{MS}\left(I,\hat{I}\right)=\mathbb{E}_{J\sim\mathcal{U}(\mathcal{J}_N)}\left[\mathcal{L}_{style}\left(I_J,\hat{I}_J\right)\right]\) (3)

\(=\frac{1}{N_J}\sum_{J\in\mathcal{J}_N}\mathcal{L}_{style}\left(I_J,\hat{I}_J\right)\) (4)

Where :

• J_<sub>N</sub>_ is the set of triplets of integers in {1_,...,N_} of cardinal _N<sub>J</sub>_,<tbc>

• U(J_<sub>N</sub>_) is the uniform distribution on J_<sub>N</sub>_,<tbc>

• E<sub>_J_∼U(J_<sub>N</sub>_)</sub> is the mathematical expectation under the condition that _J_ follows a uniform distribution,<tbc>

• if _J_ is a triplet, _I<sub>J</sub>_ is the 3-channels image made of the 3 spectral bands of _I_ indexed by _J_,<tbc>

• L_<sub>style</sub>_ is the classical style loss for RGB images using a VGG19 pre-trained network described by \[8\], recalled in Equation (2).

The proposed synthesis algorithm is detailed in Algorithm 1 for _n_ iterations of the gradient descent algorithm and _B_ triplets drawn at every iteration. The mean and covariance of _I_ are denoted as \(\mu_I\) and \(\Sigma_I\).

**Algorithm 1** Texture synthesis with stochastic style loss

\(\hat{I}\sim\mathcal{N}\left(\mu_I,\Sigma_I\right)\triangleright\) Gaussian noise initialization<br>
for \(i\in\left\{1,\dots,n\right\}\) do<br>
   \(\mathcal{L}\leftarrow 0\)<br>
   for \(j\in\left\{1,\dots,B\right\}\) do<br>
   \(J\sim\mathcal{U}(\mathcal{J}_N)\triangleright\) Uniformly drawn triplet<br>
   \(\mathcal{L}\leftarrow\mathcal{L}+\mathcal{L}_{style}\left(I_J,\hat{I}_J\right)\)<br>
   end for<br>
   Take a gradient step on \(\hat{I}\) with gradient \(\nabla\mathcal{L}\)<br>
end for<br>
return \(\hat{I}\)

Our method ensures to browse every spectral bands and consider the correlations between each of them in the course<tbc>

<tbc>of the optimization. However, a drawback of this method is that it may need a relatively large number of triplets to reach a good overall control over multi-spectral statistics, resulting in a high computational cost. In the next section, we introduce a more simple and faster alternative approach.

## C. Projected style distance

The second style distance that we propose aims to take advantage of the redundancy of the spectral information. Indeed, the spectral information that is contained in _N_ dimensions often can be reduced in a lower number of dimensions. Therefore, we consider a projector \(P:\mathbb{R}^N\rightarrow\mathbb{R}^3\) that maps multispectral images with _N_ spectral bands into RGB-like images with 3-channels. The proposed style distance consists then in the classical style distance computed on projected images :

\(\mathcal{L}_{style}^P\left(I,\hat{I}\right)=\mathcal{L}_{style}\left(P(I),P(\hat{I})\right)\) (5)

The use of the projected style distance for exemplar-based texture synthesis is detailed in algorithm 2.

**Algorithm 2** Texture synthesis with projected style loss

\(\hat{I}\sim\mathcal{N}\left(\mu_I,\Sigma_I\right)\triangleright\) Gaussian noise initialization<br>
for \(i\in\left\{1,\dots,n\right\}\) do<br>
   \(I_P\leftarrow P(I)\)<br>
   \(\hat{I}_P\leftarrow P(\hat{I})\)<br>
   \(\mathcal{L}\leftarrow\mathcal{L}_{style}\left(I_P,\hat{I}_P\right)\)<br>
   Take a gradient step on \(\hat{I}\) with gradient \(\nabla\mathcal{L}\)<br>
end for<br>
return \(\hat{I}\)

## D. Color transfer for neural statistics extraction

We observe that the use of a projection can lead to unusual color distributions that can have an influence on the quality of the description provided by the feature maps as the network may not have been trained on such distributions. This domain shift can affect the quality of the description provided by the CNN. Examples of the color that are induced by a PCA projection for cloud field images taken from Sentinel- 2 mission are available in Figure 1.

To circumvent this, we propose to perform a color transfer operation after the projection and before the use of the VGG- 19 network. The target distribution of this transfer operation is simply the color distribution of a natural image, that therefore acts as a color palette. The idea here is to send back the considered 3-channels image in regions of the color space that are likely to be closer to the regions that have been explored during the training of the network.

To define such a color transfer operation, we chose to describe the color distributions of the images by the first and second order statistics, assuming that it gives a first satisfactory and sufficient approximation for our application. Hence, we consider an affine transformation that maps the projected<tbc>

