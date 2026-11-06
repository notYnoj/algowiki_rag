<tbc>image _I<sub>P</sub>_ with color statistics \((\mu_P,\Sigma_P)\) to an image matching the color statistics \((\mu_C,\Sigma_C)\) of a palette image _I<sub>C</sub>_. We denote \(T_{P\rightarrow C}\) such a transformation and, for an image _I_, we have:

\(T_{P\rightarrow C}(I)=\mu_C+L_CL_P^{-1}\left(I-\mu_P\right)\) (6)

where the _L<sub>P</sub>_ and _L<sub>C</sub>_ matrices are obtained using Cholesky decomposition of covariances matrices:

\(\Sigma_P=L_PL_P^T\) (7)

\(\Sigma_C=L_CL_C^T\) (8)

As it is possible to define the converse transformation \(T_{C\rightarrow P}\), such a transformation happens to be reversible so that it conserves the spatial information of the images and only act on the color of the pixels to match the first and second order statistics.

The corresponding style distance is therefore (see Figure 2 for illustration):

\(\mathcal{L}_{style}^{P+C}\left(I,\hat{I}\right)=\mathcal{L}_{style}\left(T_{P\rightarrow C}(P(I)),T_{P\rightarrow C}(P(\hat{I}))\right)\) (9)

\(=\mathcal{L}_{style}\left(P_C(I),P_C(\hat{I})\right)\) (10)

with \(T_{P\rightarrow C}\) being the color transformation introduced earlier, that maps the color statistics of the projection of the exemplar texture _P(I_)=_I<sub>P</sub>_ into the color statistics of the palette color image _I<sub>C</sub>_, and \(P_C=T_C\circ P\) being the new projection operator.

### E. Multispectral texture synthesis with deep features statistics

To perform multispectral texture synthesis, we initialize a synthetic multispectral image of _N_ channels with a Gaussian noise of mean and covariance of the exemplar image as it showed better results than a white noise initialization. Then, we use L-BFGS \[17\] to update the synthetic multispectral image in order to minimize a style distance. At each iteration of the algorithm, the gradients of one of the aforementioned style distances are used to update the pixels of the _N_ channels synthetic image. The style distance uses a CNN trained on RGB images to extract deep features statistics, covariance matrices here.

## IV. EXPERIMENTS

In this section, we give a brief description of the dataset we consider, the experimental settings and the metrics used to compare the texture syntheses. Comprehensive comparisons of syntheses using the different style distances that we formerly introduced as objective functions are then presented and discussed.

### A. Dataset

We consider a dataset composed of 130 512\(\times\)512 Sentinel- 2 images of cloud fields. The Sentinel-2 mission is an Earth observation mission from the Copernicus Program that acquires optical imagery at a spatial resolution ranging from 10 m to 60 m over land and coastal waters. It captures images in 12 spectral channels in the visible/near infrared (VNIR) and short wave infrared spectral range (SWIR), including 9 proper observation bands and 3 atmospheric correction bands (near 442, 945 and 1375 nm), for which the atmospheric absorption is high. The last band at 1375 nm present particularly high absorption percentage and is not exploitable. As a consequence, only 11 spectral bands are available.

### B. Experimental settings

We use the different style distances that we introduced in this paper as objective functions to perform texture synthesis on the 11-band images. Additional results over the 9 observation bands are also available in Appendix A.

Experimental choices and hyperparameters for each objective are as follows:

\(\bullet\) **Stochastic** : we use a batch size of 10 triplets at each iterations. We show further experiments varying the batch size in Appendix B.<tbc>

\(\bullet\) **PCA** : we use Principal Component Analysis to encode the spectral information contained in 11 bands into 3 dimensions. In our case, these 3 first components are sufficient to explain 99% of the variance (see Figure 3 for eigenvalues and eigenvectors).



P
TC
G
VGG19
G
P
TC

Fig. 1: Examples of unusual color distributions induced by the PCA projection of Sentinel-2 cloud field images.

Fig. 2: Scheme of the proposed use of color transfer for multispectral texture synthesis. A projection _P_ is used to obtain 3-channels images from the exemplar and synthetic multispectral images. Then, a color transfer operator _T<sub>C</sub>_ is applied to both images to match their color statistics to the one of a reference palette image. Finally, statistics of deep features are extracted from the so-obtained images to perform texture synthesis.

