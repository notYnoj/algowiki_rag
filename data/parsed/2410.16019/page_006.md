\(\bullet\) **PCA + Color** : We use 3 different color exemplar images to perform color transfer upstream of the PCA projection : _Wall_, _Pebbles_ and _Fabrics_. The images are available in Figure 4.

For style distances, we use a VGG19 network initialized with the pre-trained weights from \[8\]. As the authors of the latter, we extract the feature maps of the first convolutionnal filters at each spatial resolution (i.e. Conv layers with indices 1,3,5,8,11) and use quadratic decaying loss weights \(w_l=\frac{1}{N_l^2}\) where _N<sub>l</sub>_ is the number of feature maps of the layer _l_. As mentioned in section III-A, we use the covariance matrices as deep features statistics instead of the Gram matrices and we initialize the synthetic image with a Gaussian noise with the mean and covariance of the exemplar image. We use L-BFGS for 500 iterations to perform optimization.

## C. Metrics

Unlike traditional pixel-by-pixel reconstruction, we want to generate a new texture image that conserves the statistics, the properties and the general visual aspect of the original image while allowing another spatial distribution. Therefore, traditional pixel-wise metrics such as the PSNR are not adapted. In the following, we introduce different metrics used to evaluate the performance of our methods.

### 1) Style:

We measure different style distances between original and synthetic images :

\(\bullet\) the stochastic style distance denoted as \(\mathcal{L}_{style}^{MS}\). It is computed by averaging over every possible triplets. This is precisely the metric corresponding to the stochastic style distance.<tbc>

\(\bullet\) the projected style distance using a PCA, denoted as \(\mathcal{L}_{style}^{PCA}\), corresponding to the second style distance introduced in this paper.<tbc>

\(\bullet\) the style distance for the bands 2,3 and 4 which are the closest to RGB wavelengths. It is denoted as \(\mathcal{L}_{style}^{RGB}\)

### 2) Multispectral distribution:

In the context of RGB images, color distribution is a central feature in texture description. For multispectral images, we similarly want to synthesize images having a distribution of pixel values as close as possible to the exemplar image. An efficient way to compare multidimensional distribution is the Wasserstein distance. Because it is very costly to compute such distances as soon as we are in dimension greater than two, we either rely on the sliced Wasserstein distance \[24\] or to band-wise distances:

\(\bullet\) sliced Wasserstein distance L_<sub>hist</sub>_:<tbc>

\(\mathcal{L}_{hist}(I,\hat{I})^2=SW_2(I,\hat{I})^2\)<br>
\(=\mathbb{E}_{v\sim\mathcal{U}(\mathbb{S}^{N-1})}\left[W_2(I\cdot v,\hat{I}\cdot v)^2\right]\)<br>
\(=\mathbb{E}_{v\sim\mathcal{U}(\mathbb{S}^{N-1})}\left[\left\|\text{sort}(I\cdot v)-\text{sort}(\hat{I}\cdot v)\right\|_2^2\right],\)

where S<sup>_N_-1</sup> is the unit sphere in dimension _N_, _SW_<sub>2</sub> the 2-sliced Wasserstein distance, _W_<sub>2</sub> the 2-Wasserstein distance, \(I\cdot v\) the scalar product between _I_ and _v_, and sort the sorting operator.<tbc>

\(\bullet\) band-wise Wasserstein distance \(\mathcal{L}_{hist}^\lambda\) for a band \(\lambda\):<tbc>

\(\mathcal{L}_{hist}^\lambda(I,\hat{I})=W_2(I_\lambda,\hat{I}_\lambda)\)<br>
\(=\left\|\text{sort}(I_\lambda)-\text{sort}(\hat{I}_\lambda)\right\|_2\)

Eigen values
Eigen vectors
100
98.7
100
95.7
99.6
0.4
u1
84.9
U2
80
80
0.2
Cumulated variance (%)
0.0
60
60
-0.2
Variance (%)
40
40
-0.4
20
20
-0.6
-0.8
0
0
1
2
3
4
5
6
7
8
9
10
11
0
1
2
3
4
5
6
7
8
9
10
Principal component order
Band index







Fig. 3: (Left) Eigenvalues of the used PCA over 11-band Sentinel-2 images. The first component encompasses 95% of the variance, the 3 first 99%. (Right) 3 first eigenvectors of the used PCA over 11-band Sentinel-2 images (denoted as _u<sub>i</sub>_).

(a) Wall

(b) Pebbles

(c) Fabrics

Fig. 4: Exemples of palette images used for the proposed color transfer.

