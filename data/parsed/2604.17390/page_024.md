<tbc>approaches such as Deep Image Prior (DIP), which require neither training nor dedicated datasets, as shown in both the figure and the table.

10 and Figure 15 show the Peak Signal-to-Noise Ratio (PSNR) values achieved by the different methods. PSNR measures pixel-wise similarity between a reconstructed image and a reference (ground-truth) image, which

\begin{tabular}{ccccc}
**Method** & **Dataset A** & **Dataset B** & **Dataset C** & **Averages** \\
DIP-DENOISE TF & 29.6638 & 29.9005 & 29.7345 & 29.7663 \\
DIP-INPAINTING TF & 31.2086 & 31.1740 & 31.3163 & 31.2330 \\
DNCNN TN & 38.4847 & 36.8845 & 31.3225 & 35.5639 \\
DNCNN TS & 38.3920 & 36.8139 & 36.0718 & 37.0926 \\
DRUNET TN & 30.8336 & 32.4036 & 36.2790 & 33.1720 \\
DRUNET TS & 31.0895 & 33.4126 & 35.7140 & 33.4054 \\
ESRGAN TN & 39.3524 & 37.5612 & 36.0042 & 37.6393 \\
ESRGAN TS & 39.1888 & 36.8152 & 36.6121 & 37.5387 \\
MESA TF & 28.9296 & 30.9083 & 31.2342 & 30.3574 \\
\end{tabular}

Dataset A Averages SSIM
MESA TF
ESRGAN TS
ESRGAN TN
DRUNET TS
DRUNET TN
DNCNN TS
DNCNN TN
DIP-INPAITFING TF
DIP-DENOISE TF
0,7
0,75
0,8
0,85
0,9
0,95
1

Dataset B Averages SSIM
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
0,2
0,4
0,6
0,8
1

Dataset C Averages SSIM
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
0,2
0,4
0,6
0,8
1

All Datasets Averages SSIM
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
0,2
0,4
0,6
0,8
1

(a) Dataset A

(b) Dataset B

(c) Dataset C

(d) All Datasets’ Averages

Fig. 14. SSIM evaluation

10. PSNR per method across datasets and their averages.

