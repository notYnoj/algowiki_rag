### 3) Comparison between methods :

We now use all metrics introduced above to compare the three methods that we have introduced to perform neural multispectral texture synthesis: by using the stochastic style distance, by using the projected distance, and finally by using the projected style distance together with color transfer. Of course, each of these methods perform best when using the metric that has been optimized by the method, and we therefore focus on the remaining metrics to reach some conclusions. Results are gathered in  II.

First, we observe that the stochastic style distance enforces greater respect of the Fourier spectra and of the gradients in the generated textures, two features that are related to the spatial structure of the images. We can see in Figure 6 that this is the case across all spectral bands.

For the multispectral distribution, two methods, namely _Stochastic_ and _PCA + Pebbles_, stand out, showing competitive SWD L_<sub>hist</sub>_. However, these results find different explanations if we look at the different statistics. The projected style distance ensures a better respect of the mean \(\mathcal{L}_\mu\) while its stochastic counterpart seems to allow a better respect of the higher order statistics, as seen for the covariance \(\mathcal{L}_\Sigma\). Then, we also observe different dynamics across the spectral bands with the _Stochastic_ method outperforming _PCA + Pebbles_ for 4 out of 11 spectral bands.

Finally, the band wise analysis clearly reveals that all methods under-perform on the 2 correction bands, at 442nm and 945nm (see Figure 6). This was expected as they present more variability than other bands. However, the two most effective methods are less sensitive to this high variability, showing greater ability to take multispectral information into account.

## V. CONCLUSION

In this paper, we have introduced several strategies to generalize state-of-the-art RGB texture synthesis methods to multispectral images. The main difficulty to do so is to generalize style distances obtained from CNN pre-trained on 3-channels images to a larger number of bands.

The new introduced style distances were used to perform exemplar-based texture synthesis on single multispectral images of cloud fields from the Sentinel-2 mission. They show satisfactory results, both visually and numerically.

The stochastic style distance ensures the best visual reconstruction and globally shows the best numerical results among the tested methods, but comes at a higher computational cost. The use of a projection is faster but less efficient. However, color transfer upstream of the projection happens to largely enhance the quality of the reconstruction.

Finally, all of the proposed methods do not require any additional training, since they leverage an RGB CNN that has proven itself to perform well for texture synthesis and style transfer. The solutions we propose are not specific to texture modeling and can be applied to a wide range of style- like distances that take advantage of the capabilities of pre- trained neural networks. The most direct perspective we can highlight is style transfer. A second perspective is the use of the proposed style distances for feed-forward approaches, to texture synthesis or to more general restoration or editing tasks. Eventually, common distances based on neural networks such as the widely used FID \[11\] or LPIPS \[38\] can also be extended to multi/hyperspectral imaging with the strategies proposed in this paper, opening interesting avenues for multispectral image quality evaluation. Another perspective lies in the use of the texture models presented here to train new networks to perform multi-texture synthesis.

\begin{tabular}{ccccccccc}
Method & \(\mathcal{L}_{style}^{MS}\downarrow\) & \(\mathcal{L}_{style}^{PCA}\downarrow\) & \(\mathcal{L}_{sp}^{mean}\downarrow\) & \(\mathcal{L}_{grad}(\cdot 10^{-3})\downarrow\) & \(\mathcal{L}_{hist}(\cdot 10^{-3})\downarrow\) & \(\mathcal{L}_\mu(\cdot 10^{-3})\downarrow\) & \(\mathcal{L}_\Sigma(\cdot 10^{-3})\downarrow\) & \(\mathcal{L}_{RX}(\cdot 10^{-3})\downarrow\) \\
Stochastic & **0.17** & 676.84 & **1.96** & **13.52** & 12.63 & 17.36 & **14.02** & 18.62 \\
PCA & 115.38 & **0.59** & 2.33 & 26.52 & 15.02 & 12.20 & 21.45 & 15.68 \\
PCA + Wall & 98.38 & 2158.46 & 2.35 & 21.92 & 14.39 & 9.24 & 21.63 & 12.65 \\
PCA + Pebbles & 68.00 & 4872.01 & 2.21 & 18.94 & **11.70** & **4.58** & 21.01 & **7.87** \\
PCA + Fabrics & 102.09 & 11008.26 & 2.33 & 29.78 & 15.32 & 12.80 & 22.16 & 16.83 \\
\end{tabular}

Azimuthal spectral distance
Gradients Sliced Wasserstein Distance
Sliced Wasserstein Distance
Method
Method
0.035
Method
Stochastic
Stochastic
4.0
PCA
0.06
PCA
Stochastic
PCA
PCA
PCA + Wall
PCA + Wall
PCA + Pebbles
PCA + Pebbles
PCA + Pebbles
PCA + Fabrics
PCA + Fabrics
3.5
3.0
0.04
Lsp
Lsp
Lrap
0.020
2.5
0.03
0.015
2.0
0.02
0.01
1.5
0.01
0.010
0
2
4
6
8
10
0
2
4
6
8
10
0
2
4
6
8
10
Band index
Band index
Band index

TABLE II: Evaluation of multispectral texture synthesis through CNN trained on RGB images. Metrics were computed and averaged over 130 multispectral images.

Fig. 6: Band wise comparison of the proposed methods.

