9 and Figure14 report the Structural Similarity Index (SSIM) scores. Although SSIM emphasizes local structural fidelity and is sensitive to pixel-level luminance and contrast, our method is not explicitly designed to optimize these low-level characteristics. This explains why, on average, it exhibits slightly lower SSIM performance compared to some training-based methods (ESRGAN, DnCNN, DRUNET), while still outperforming low-cost

\begin{tabular}{ccccc}
**Method** & **Dataset A** & **Dataset B** & **Dataset C** & **Average** \\
DIP-DENOISE TF & 0.8269 & 0.7059 & 0.6922 & 0.7416 \\
DIP-INPAINTING TF & 0.8834 & 0.7548 & 0.8212 & 0.8198 \\
DNCNN TN & 0.9590 & 0.9066 & 0.6169 & 0.8275 \\
DNCNN TS & 0.9458 & 0.8855 & 0.9094 & 0.9136 \\
DRUNET TN & 0.8393 & 0.8579 & 0.9182 & 0.8718 \\
DRUNET TS & 0.8174 & 0.8703 & 0.9040 & 0.8639 \\
ESRGAN TN & 0.9607 & 0.9133 & 0.9203 & 0.9314 \\
ESRGAN TS & 0.9482 & 0.8938 & 0.9071 & 0.9164 \\
MESA TF & 0.9046 & 0.8393 & 0.8571 & 0.8670 \\
\end{tabular}

Test Dataset A Averages LPIPS VGGNet
Test Dataset B Averages LPIPS VGGNet
MESA TF
ESRGAN TS
ESRGAN TN
DRUNET TS
DRUNET TN
DNCNN TS
DNCNN TN
DIP-INPAITFING TF
DIP-DENOISE TF
0
0,05
0,1
0,15
0,2
0,25

Test Dataset B Averages LPIPS VGGNet
MESA TF
ESRGAN TS
ESRGAN TN
DRUNET TS
DRUNET TN
DNCNN TS
DNCNN TN
DIP-INPAITFING TF
DIP-DENOISE TF
0
0,05
0,1
0,15
0,2
0,25
0,3
0,35
0,4

Test Dataset C Averages LPIPS VGGNet
Test Dataset C Averages LPIPS VGGNet
MESA TF
ESRGAN TS
ESRGAN TN
DRUNET TS
DRUNET TN
DNCNN TS
DNCNN TN
DIP-INPAITFING TF
DIP-DENOISE TF
0
0,05
0,1
0,15
0,2
0,25
0,3
0,35

All Datasets Averages LPIPS VGGNet
MESA TF
ESRGAN TS
ESRGAN TN
DRUNET TS
DRUNET TN
DNCNN TS
DNCNN TN
DIP-INPAITFING TF
DIP-DENOISE TF
0
0,05
0,1
0,15
0,2
0,25
0,3
0,35

(a) Dataset A

(b) Dataset B

(c) Dataset C

(d) All Datasets’ Averages

Fig. 13. LPIPS evaluation with VGG network usage

9. SSIM per method across datasets and their averages.

