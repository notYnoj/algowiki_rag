<tbc>be described as:

\(M^*=argmin_M\left(E(S,M,I)+\alpha|M|\right),\) (16)

where _E_ represents the transformation error estimator, _S_ is our proposed unwarping model (STEN), |_M_| denotes the size of the matrix _M_, and \(\alpha\ge 0\) is a tunable parameter. The description of the transformation self-estimation algorithm is detailed in Algorithm 1.

## 4 . Experiments

### 4.1 . Implementation Details

**Dataset** We use the existing SCI1K, SCID, and SCIAQ dataset \[42\] to construct our warped dataset - SCI1KW, SCIDW, and SCIAQW to train and test our STEN model. Specifically, we first randomly generate a warping matrix, which includes transformations such as random scaling, cropping, rotation, and projection. Then, we distort each image in SCI1K with the warping matrix to obtain a distorted version and finally form the SCI1KW datasets. During training processing, we crop the maximum effective region of the warped result as the input image according to the<tbc>

<tbc>transformation effect. In the testing phase, we centre-crop the \(384\times 384\) size patch from each test image in the test set and assign a transformation on the patch. This method allows us to effectively evaluate the model’s performance under different warping conditions. **Settings** For optimization, we employ L1 loss \[25\] and the Adam optimizer \[18\] with \(\beta_1=0.9\) and \(\beta_2=0.999\). Our STEN model is trained for 1000 epochs with a batch size of 16, starting with a learning rate of \(1\times 10^{-4}\), halving it every 200 epochs. In the transformation self-estimation algorithm, we set the adjustable parameter _alpha_=0.05. All the compared methods used in this work adopt the same settings as our STEN model.

### 4.2 . Comparisons for Arbitrary Scale Super-Resolution

We compare our proposed STEN model with BTC\[27\], LTE\[20\], LIIF\[7\], and MetaSR\[17\] for arbitrary-scale image super-resolution in both in-scale and out-of-scale scenarios. To ensure a fair comparison, all methods use RDN\[44\] as the encoder for feature extraction and are trained on the SCI1K dataset. As shown in  **??**, our method outperforms existing arbitrary-scale super- resolution techniques across most scale factors and datasets.<tbc>

\begin{tabular}{ccccccccc}
\multicolumn{2}{c}{Train set: SCI1K (n=800)} & \multicolumn{3}{c}{In-training-scale} & \multicolumn{4}{c}{Out-of-training-scale} \\
Test set & Method & \(\times 2\) & \(\times 3\) & \(\times 4\) & \(\times 5\) & \(\times 6\) & \(\times 7\) & \(\times 8\) \\
\multirow{8}{*}{SCI1K

(n = 200)} & Bicubic & 28.81 & 25.15 & 23.18 & 22.02 & 21.23 & 20.72 & 20.26 \\
 & RDN \[44\] & 38.45 & 33.59 & 29.81 & - & - & - & - \\
 & MetaSR \[17\] & 38.57 & 33.67 & 30.12 & 27.52 & 26.13 & 23.91 & 23.19 \\
 & LIIF \[7\] & 38.65 & 33.97 & 30.55 & 27.77 & 26.07 & 23.99 & 23.24 \\
 & LTE \[20\] & 39.14 & 34.50 & 30.93 & 28.22 & 26.19 & 24.28 & 23.17 \\
 & BTC\[27\] & <u>39.17</u> & <u>34.58</u> & <u>31.10</u> & <u>28.33</u> & <u>26.31</u> & **24.47** & <u>23.38</u> \\
 & STEN(Ours) & **39.22** & **34.87** & **31.33** & **28.34** & **26.38** & <u>24.37</u> & **23.40** \\
\multirow{8}{*}{SCID

(n = 40)} & Bicubic & 25.22 & 22.78 & 21.60 & 20.90 & 20.42 & 20.04 & 19.77 \\
 & RDN \[44\] & 34.00 & 28.34 & 25.74 & - & - & - & - \\
 & MetaSR \[17\] & 33.84 & 29.08 & 25.76 & 23.62 & 22.38 & 21.59 & 21.07 \\
 & LIIF \[7\] & 34.24 & 29.10 & 25.89 & 23.77 & 22.53 & 21.73 & 21.21 \\
 & LTE \[20\] & <u>34.49</u> & <u>29.60</u> & <u>26.34</u> & 24.06 & <u>22.67</u> & 21.81 & 21.28 \\
 & BTC\[27\] & 34.48 & 29.56 & 26.30 & <u>24.09</u> & **22.69** & <u>21.84</u> & **21.29** \\
 & STEN(Ours) & **34.59** & **29.81** & **26.60** & **24.15** & 22.65 & **21.85** & <u>21.28</u> \\
\multirow{8}{*}{SCIAQ

(n = 22)} & Bicubic & 22.89 & 20.66 & 19.70 & 19.18 & 18.79 & 18.46 & 18.20 \\
 & RDN \[44\] & 33.53 & 26.89 & 23.38 & - & - & - & - \\
 & MetaSR \[17\] & 34.12 & 28.40 & 23.55 & 21.18 & 20.18 & 19.63 & 19.25 \\
 & LIIF \[7\] & 34.31 & 28.27 & 23.44 & 21.16 & 20.25 & 19.70 & 19.36 \\
 & LTE \[20\] & <u>35.07</u> & 29.33 & 24.21 & 21.52 & 20.39 & 19.78 & 19.43 \\
 & BTC \[27\] & 34.91 & <u>29.36</u> & <u>24.25</u> & <u>21.57</u> & **20.43** & <u>19.82</u> & <u>19.45</u> \\
 & STEN(Ours) & **35.20** & **29.71** & **24.60** & **21.63** & <u>20.40</u> & **19.85** & **19.48** \\
\end{tabular}

1: Quantitative comparison of arbitrary scale super-resolution methods on SCI1K, SCID, and SIQAD datasets within in-scale (PSNR (dB)). The best results are highlighted in bold, while the second-best results are indicated with an underline.

