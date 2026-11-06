Additionally, Fig. 3 and Fig. 4 show a qualitative comparison between our method and the others, demonstrating reconstruction performance at different scales. Whether in- scale or out-of-scale, our method consistently surpasses others in recovering text and graphical details, highlighting its clear advantages in detail preservation and visual quality.

## 4.3 . Comparisons for Homography Warping

We compare our STEN model with SRWarp\[33\] and LTEW\[19\] on the generated benchmark datasets (SCI1KW,<tbc>

<tbc>SCIDW, and SIQADW) with homography warping transformation, including in-distribution and out-of-distribution scenarios. In the in-scale scenario, we consider the scale factors present in the training dataset, while in the out-of- scale scenario, the scale factors were not included in the training dataset. To ensure a fair comparison, all methods use RDN\[44\] as the encoder for feature extraction and are trained on the SCI1K dataset. Additionally, we include results from bilinear interpolation and the RDN model. For RDN, we upsample the input images and use the Warp- Perspective function\[5\] with a bicubic kernel to synthesize the warped images. For SRWarp and LTEW, we implement them using their publicly available source code.

2 presents the average mPSNR results of our method compared to other methods on benchmark datasets under both in-scale and out-of-scale conditions. It can be observed that our method outperforms LTEW\[19\] in both cases. Additionally, we validate the effectiveness of the transformation self-estimation model, where STEN(est) is the result obtained using the estimated transformation matrix _M<sub>i</sub>_. From  2, it is evident that although the performance metrics of STEN(est) are lower, it can still effectively predict the transformation matrix. Furthermore, Fig. 5 and Fig. 6 provide qualitative comparisons of in-scale and out-of-scale methods, showing that our approach generates text and texture details more clearly. In summary,<tbc>

\begin{tabular}{ccccccc}
\multirow{2}{*}{Method} & SCI1KW & \multicolumn{2}{c}{SCIDW} & \multicolumn{3}{c}{SIQADW} \\
 & isc & osc & isc & osc & isc & osc \\
Bicubic & 24.93 & 23.04 & 22.43 & 21.02 & 20.36 & 19.21 \\
RDN\[44\] & 33.81 & 25.08 & 28.54 & 22.39 & 27.24 & 21.04 \\
SRWarp-RDN\[33\] & 35.93 & 27.65 & 31.65 & 24.38 & 31.24 & 21.89 \\
LTEW-RDN\[19\] & <u>36.18</u> & <u>28.55</u> & <u>32.17</u> & <u>25.91</u> & <u>31.67</u> & <u>22.31</u> \\
STEN-RDN(est) & 25.84 & 22.78 & 22.94 & 20.68 & 20.43 & 18.62 \\
STEN-RDN(Ours) & **36.97** & **29.29** & **32.49** & **26.17** & **32.15** & **22.59** \\
\end{tabular}

