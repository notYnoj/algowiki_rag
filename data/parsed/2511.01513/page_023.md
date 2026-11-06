## S12 Implementation Details

Several implementation details have been omitted for brevity in the main text. We expand here the explanation of various steps and the hyperparameters used.

### S12.1 Anomaly detection

In the first stage of the pipeline, we apply FCA to the residuals of the VAE reconstruction. We use a similar preprocessing to Ardelean and Weyrich \[2024b\]: resize the images to 512\(\times\)512, use a Wide ResNet-50 \[Zagoruyko and Komodakis 2016\], and train the VAE for 10k iterations. After subtracting the original features from the reconstruction we use FCA with a patch size of 7\(\times\)7, \(\sigma_p=3\), and \(\sigma_s=1\).

### S12.2 Semantic feature segmentation

In order to enable an efficient training of the segmentation network through contrastive learning, we first build a database of positive and negative pairs. As described in section 3.1, we first binarize the<tbc>

<tbc>anomaly maps from the previous step using an adaptive threshold. Afterward, we form groups of prominent features by finding the connected components. To reduce some of the noise that arises from binarization, we perform a small erosion (2\(\times\)2) and then eliminate objects smaller than 12 pixels. For each region, we then compute a neural descriptor by averaging the ResNet features from the pixels inside the mask. We employ a weighted average using the softmax of the scores predicted by FCA, similarly to Sohn et al. \[2023\]. The<tbc>





16
Inversion Time Edit Time
14
12
10
Time (s)
8
6
4
2
0
10
30
50
100
150
200
250
Number of Steps

Inversion error VAE reconstruction error
0.075
0.065
MAE
0.055
0.045
10
30
50
100
150
200
250
Number of Steps

A1
A2
A3
A4
A5
Normal
A1
A2
A3
A4
A5
Normal
A1
A2
A3
A4
A5

Fig. 23. Failure case for Diffusion Texture Painting \[Hu et al. 2024\]. The results are generated with a progressively dilated mask. Only at the largest size (dilated by 77 pixels), the feature is actually painted.

Image Ano. scores Local 95% Dataset 95% Otsu Our Eq. (1)

Fig. 24. Comparing the binarization of anomaly scores using different thresholding functions.

Fig. 25. Timing and errors for diffusion inversion.

Fig. 26. Histograms of sampled negatives from each anomaly class, used for contrastive learning: uniformly sampled (_left_) and using our stratified sampling (_right_). A disproportionate number of normal samples hinders the proper separation of the anomaly classes.

