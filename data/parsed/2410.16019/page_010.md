## APPENDIX A 9 BANDS DATASET

In addition to the results presented for the 11-band Sentinel- 2 images, we present in this section the results of texture synthesis for 9-band images. These images correspond to the same images keeping only the proper observation bands and excluding the 2 spectral bands that are usually used for atmospheric correction (see IV-A). We chose to test this new dataset only on the 2 best performing methods, namely _Stochastic_ and _PCA + Pebbles_. Figure 7 presents the eigenvectors and eigenvalues of PCA used for the 9-band dataset.

Numerical results are shown in  III. These results are in line with the previous results on the 11-band images with regard to the hierarchy of the two methods in the various metrics. Moreover, as the two bands that presented the more variability are removed, the synthesis task becomes easier. Indeed, those bands shown themselves to be harder to synthesize for the 11-band images and the results on the 9-band images show a quantitative improvement for both of<tbc>

<tbc>the tested methods. The same goes when we compare the synthesis on the 3 RGB bands with the benchmark (consisting of optimizing the images only on these 3 bands) and the 11- band dataset: a fewer number of bands to consider enhance the quality of the reconstruction for both tested methods.

## APPENDIX SHASTIC STYLE DISTANCE BATCH SIZE

In this section we study the influence of the batch size (i.e. the number of triplets drawn at each iteration) on the synthesis results when using the stochastic style distance as a minimization objective. We performed exemplar synthesis on the same 130 images from the Sentinel-2 mission and vary the batch size.

The numerical results of our experiment are given in  V and illustrated in Figure 8. We also provide visual examples in Figure 9. They show that the higher the batch size is, the better are the results for all the tested metric. We observe a great interest in increasing the batch size up to at least 5<tbc>

\begin{tabular}{cccccccc}
Method & \(\mathcal{L}_{style}^{MS}\downarrow\) & \(\mathcal{L}_{style}^{PCA}\downarrow\) & \(\mathcal{L}_{sp}^{mean}\downarrow\) & \(\mathcal{L}_{grad}(\cdot 10^{-3})\) & \(\mathcal{L}_{hist}(\cdot 10^{-3})\downarrow\) & \(\mathcal{L}_\mu(\cdot 10^{-3})\downarrow\) & \(\mathcal{L}_\Sigma(\cdot 10^{-3})\downarrow\) & \(\mathcal{L}_{RX}(\cdot 10^{-3})\downarrow\) \\
Stochastic & **0.09** & **161.51** & **1.72** & **12.46** & 9.19 & 14.69 & **4.93** & 15.27 \\
PCA + Pebbles & 27.92 & 745.75 & 1.88 & 16.30 & **7.66** & **3.10** & 7.08 & 4.04 \\
\end{tabular}

\begin{tabular}{cccccc}
Number

of bands & Method & \(\mathcal{L}_{style}^{RGB}\downarrow\) & \(\mathcal{L}_{sp}^{mean}\downarrow\) & \(\mathcal{L}_{grad}(\cdot 10^{-3})\downarrow\) & \(\mathcal{L}_{hist}(\cdot 10^{-3})\downarrow\) \\
3 & RGB & **0.019** & 2.03 & 3.09 & 1.56 \\
\multirow{2}{*}{9} & Stochastic & 0.059 & **1.58** & **9.32** & 9.75 \\
 & PCA + Pebbles & 31.15 & 1.68 & 11.63 & **8.25** \\
\multirow{2}{*}{11} & Stochastic & 0.099 & 1.68 & 9.33 & 12.41 \\
 & PCA + Pebbles & 44.71 & 1.87 & 13.46 & 9.32 \\
\end{tabular}

\begin{tabular}{ccccccc}
Batch size & \(\mathcal{L}_{style}^{MS}\downarrow\) & \(\mathcal{L}_{style}^{PCA}\downarrow\) & \(\mathcal{L}_{sp}^{mean}\downarrow\) & \(\mathcal{L}_{grad}(\cdot 10^{-3})\downarrow\) & \(\mathcal{L}_{hist}(\cdot 10^{-3})\downarrow\) \\
1 & 18.32 & 4254.55 & 2.09 & 22.98 & 68.11 \\
3 & 3.00 & 2435.40 & 2.05 & 13.74 & 60.51 \\
5 & 0.68 & 1228.71 & 2.01 & 13.65 & 27.59 \\
7 & 0.27 & 726.56 & 1.98 & 13.62 & 15.60 \\
10 & **0.17** & **676.84** & **1.96** & **13.52** & **12.63** \\
\end{tabular}

Eigen values
Eigen vectors
100
94.7
99.4
99.7
100
u1
98.2
0.6
u2
U3
80
80
0.4
Cumulated variance (%)
60
60
0.2
Variance (%)
40
40
0.0
-0.2
20
20
-0.4
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
0
1
2
3
4
5
6
7
8
Principal component order
Band index

Fig. 7: (Left) Eigenvalues of the used PCA over 9-band Sentinel-2 images. The first component encompasses 95% of the variance, the 3 first 99%. (Right) 3 first eigenvectors of the used PCA over 9-band Sentinel-2 images (denoted as _u<sub>i</sub>_).

TABLE III: Mean principal metrics results for multispectral texture synthesis on 9-band Sentinel-2 images. Sliced distances \(\mathcal{L}_{sp}^{mean}\) and L_<sub>hist</sub>_ were computed using 1000 random directions.

TABLE IV: Mean principal metrics results computed on RGB bands. The line RGB refers to the benchmark where the 3 bands images were optimized to match deep features statistics

TABLE V: Mean principal metrics results for multispectral texture synthesis on 11-band Sentinel-2 images when varying the the number of triplets drawn at each iteration

