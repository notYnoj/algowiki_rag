<tbc>proposed modules not only effectively enhance the overall performance of the model but also better preserve details and improve visual quality when handling complex images. Meanwhile, to validate the effectiveness of B-splines, we conducted another ablation experiment, where we used the Fourier representation in addition to B-splines. The results show that using the Fourier representation leads to a significant decline in all performance metrics, which validates that B-splines are more effective than the Fourier representation for handling screen content images.

### 4.5 . Comparisons for Natural Images

To further validate the performance of our model on real-world natural images, we retrain it on the widely used DIV2K dataset\[2\]. In these experiments, we evaluate STEN on several benchmark datasets, including DIV2KW, Set5W, Set14W, B100W, and Urban100W\[33\]. The results are presented in Sec. 4.3, demonstrating that STEN performs well on natural image benchmarks, despite a slight decline in performance in certain cases. These results further highlight the robustness of STEN across a wide range of datasets, including more diverse natural images, making it applicable to practical scenarios.

### 4.6 . Comparisons for the Real-world Images

We conducted experiments on real-world images to validate the effectiveness of our proposed error estimation model. In the distorted images captured using a camera, the transformation matrix parameters were unknown at the time of capture. Subsequently, we applied the trained error estimation model to estimate these unknown parameters. Due to the lack of ground truth images (GT), we were unable to perform quantitative analysis; therefore, we opted for a qualitative comparison between STEN and SRWarp\[33\] as well as LTEW\[19\]. As shown in Fig. 7, we made predictions for both screen content images and natural images. The results indicate that our error estimation model can effectively predict the parameters of the transformation matrix, thereby validating the effectiveness of the proposed method.

## 5 . Conclusion

In this work, we propose an innovative structure-texture enhancement dual-branch model, named STEN, to achieve arbitrary scale super-resolution (SR) and homography unwarping. Our STEN model includes a structure estimation branch and a texture estimation branch. The texture estimation branch uses the implicit B-spline neural representation of transformed images to handle coordinate transformation and improve the synthesized texture details. At the same time, the structure estimation branch enhances structural features by using global transformation blocks and local transformation blocks, facilitating effective global modeling and thereby better representing the overall shape and structure of the image. Additionally, our STEN model also introduces the transformation self-estimation module to process unknown transformation cases in real-world scenarios. Experiments demonstrate that our proposed STEN method significantly outperforms existing techniques in homography unwarping tasks across three publicly available SCI datasets, five natural image datasets, and the real-world images.<tbc>

\begin{tabular}{cccccccccccc}
\multirow{2}{*}{Method} & \multicolumn{2}{c}{DIV2K} & \multicolumn{2}{c}{Set5W} & \multicolumn{2}{c}{Set14W} & \multicolumn{2}{c}{B100W} & \multicolumn{2}{c}{Urban100W} \\
 & isc & osc & isc & osc & isc & osc & isc & osc & isc & osc & isc & osc \\
Bicubic & 27.85 & 25.03 & 35.00 & 28.75 & 28.79 & 24.57 & 28.67 & 25.02 & 24.84 & 21.89 \\
RRDB\[40\] & 30.76 & 26.84 & 37.40 & 30.34 & 31.56 & 25.95 & 30.29 & 26.32 & 28.83 & 23.94 \\
SRWarp-RRDB\[33\] & 31.04 & 26.75 & 37.93 & 29.90 & 32.11 & 25.35 & 30.48 & 26.10 & 29.45 & 24.04 \\
LTEW-RRDB\[19\] & 31.10 & 26.92 & <u>38.20</u> & 31.07 & 32.15 & 26.02 & 30.56 & 26.41 & 29.50 & 24.25 \\
MFR-RRDB\[41\] & <u>31.18</u> & <u>27.12</u> & **38.23** & **31.19** & <u>32.26</u> & <u>26.26</u> & <u>30.62</u> & **26.53** & **29.68** & **24.51** \\
STEN-RRDB(Ours) & **31.96** & **27.75** & 38.12 & <u>31.10</u> & **32.30** & **26.27** & **30.88** & <u>26.45</u> & <u>29.50</u> & <u>24.26</u> \\
\end{tabular}

