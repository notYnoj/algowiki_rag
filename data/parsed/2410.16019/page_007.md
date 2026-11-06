### 3) Gaussian hypothesis:

Anomaly detection is one of the most common analyses performed on multispectral images. The historical multispectral anomaly detection criterion, the RX \[25\], makes a Gaussian assumption for the whole image, or at least for limited windows, in order to define a statistical test. Hence, we also measure the difference in the first and second order spectral statistics, using :<tbc>

• the _L_<sub>2</sub> norm between the means and covariances, respectively \(\mathcal{L}_\mu\) and \(\mathcal{L}_\Sigma\) :<tbc>

\(\mathcal{L}_\mu(I,\hat{I})=\left\|\mu-\hat{\mu}\right\|_2\)<br>
\(\mathcal{L}_\Sigma(I,\hat{I})=\left\|\Sigma-\hat{\Sigma}\right\|_2\)

• the Wasserstein distance between the two gaussian distributions given by the means and covariances which, for the sake of simplicity, we label _RX_ even though it is not equivalent to the _RX_ criterion (we do not compute a Mahalanobis distance):<tbc>

\(\mathcal{L}_{RX}(I,\hat{I})=\sqrt{(\mu-\hat{\mu})^2+\mathrm{Tr}\left(\Sigma+\hat{\Sigma}-2\Sigma^\frac{1}{2}\hat{\Sigma}\Sigma^\frac{1}{2}\right)}\) \(\text{(11)}\)

where _I_ and \(\hat{I}\) have respectively \((\mu,\Sigma)\) and \((\hat{\mu},\hat{\Sigma})\) as statistics.

### 4) Spectrum:

Cloud fields images exhibit fractal behaviors, which can be analyzed through the decay of the azimuthal modulus of the Fourier’s transform of the image. which is defined as follows :<tbc>

\(\mathcal{F}_{rad}(I)(r)=\frac{1}{N_r}\int_0^{2\pi}\|\mathcal{F}(I)(r\mathrm{cos}\theta,r\mathrm{sin}\theta)\|d\theta\) (12)

<tbc>where _I_ is a single channel image and F the Fourier’s transform operator. As one expects a power-law decay \(\mathcal{F}_{rad}(r)\sim\frac{1}{r^p}\), the differences in fractal behaviours is quantified by the _l_<sub>2</sub> distance between the two logarithm of the azimuthal spectra :<tbc>

\(\mathcal{L}_{sp}(I,\hat{I})=\left\|\mathrm{log}\left(\mathcal{F}_{rad}(I)\right)-\mathrm{log}\left(\mathcal{F}_{rad}(\hat{I})\right)\right\|_2\) (13)

<tbc>We compute this distance on the band-wise image \(I_\lambda\) for each spectral band \(\lambda\) and on the grey-scale image _I<sub>mean</sub>_ :

\(\mathcal{L}_{sp}^\lambda(I,\hat{I})=\mathcal{L}_{sp}(I_\lambda,\hat{I}_\lambda)\) (14)

\(\mathcal{L}_{sp}^{mean}(I,\hat{I})=\mathcal{L}_{sp}(I_{mean},\hat{I}_{mean})\) (15)

### 5) Gradients:

The final features we consider are image gradients, which are key to several cloud image applications \[32\] \[21\] \[9\]. Gradient calculation in the two spatial directions (horizontal and vertical) on an image _I_, leads to two multispectral images \(\nabla_xI\) and \(\nabla_yI\) that can be used together to obtain the magnitude resulting in another multispectral image \(|\nabla I|\). A proper reconstruction should exhibit a distribution of gradients as close as possible to the original one. Hence, we use the sliced Wasserstein distance to evaluate the deviation between the two distributions :<tbc>

\(\mathcal{L}_{grad}(I,\hat{I})=SW_2\left(|\nabla I|,|\nabla\hat{I}|\right)\) (16)

<tbc>We further compute the Wasserstein distance over the spectral bands in a similar way :

\(\mathcal{L}_{grad}^\lambda(I,\hat{I})=W_2(\nabla I_\lambda,\nabla\hat{I}_\lambda)\) (17)

A total of 1000 random directions is used to compute the sliced Wasserstein distances, L_<sub>grad</sub>_ and L_<sub>hist</sub>_.

## D. Results

We show qualitative results with reconstruction examples in Figure 5 and quantitative results in  II. In addition, we show band-wise comparison for distribution, gradients and spectral metrics in Figure 6.

### 1) Visual quality :

Our methods enable faithful texture reconstruction for cloud field multispectral images. However, results differ depending on the method used. Indeed, we observe more frequently grid-like artifacts on the images synthesized using a projected style distance (either PCA or PCA + Color), while the ones synthesized using the stochastic style distance do not exhibit this kind of artifacts. The PCA method is the one showing the coarsest artifacts and the use of color transfer significantly enhances the visual aspect of the synthetic images.

### 2) Comparison with RGB texture synthesis:

As a sanity check, we compare our method with the result of applying the original method from \[8\] to the three multispectral bands that are closer to the RGB spectral content. For this, we consider bands 2, 3 and 4. We perform texture synthesis only using these 3 bands. Then, we compare the obtained 3-channels images with the images obtained by keeping only the same 3 bands after optimizing the multispectral images using the aforementioned multispectral style distances. The quantitative comparison on the 3 RGB bands is given in  I. The considered metrics are computed only on the RGB bands.

Without surprise, the \(\mathcal{L}_{style}^{RGB}\) loss is smaller when optimizing the RGB image. Also, the stochastic style distance performs much better than the projected ones for this metric. Next, one observes that all proposed style distances yield a better or similar preservation of the gradient, the histogram and the spectrum. This may be due to a better account of inter-band dependency when optimizing over all bands.

\begin{tabular}{ccccc}
Method & \(\mathcal{L}_{style}^{RGB}\downarrow\) & \(\mathcal{L}_{sp}^{mean}\downarrow\) & \(\mathcal{L}_{grad}(\cdot 10^{-3})\downarrow\) & \(\mathcal{L}_{hist}(\cdot 10^{-3})\downarrow\) \\
RGB & **0.019** & 2.03 & 28.53 & 14.09 \\
Stochastic & 0.099 & **1.68** & **9.33** & 12.41 \\
PCA & 85.15 & 2.09 & 20.55 & 13.02 \\
PCA + Wall & 55.65 & 1.90 & 15.27 & 11.75 \\
PCA + Pebbles & 44.71 & 1.87 & 13.46 & **9.32** \\
PCA + Fabrics & 95.68 & 2.29 & 27.73 & 12.35 \\
\end{tabular}

TABLE I: Evaluation of our methods on RGB bands. The line RGB refers to a baseline where images are obtained by optimizing only on the 3 RGB bands to match deep features statistics. All metrics are computed on the RGB bands.

