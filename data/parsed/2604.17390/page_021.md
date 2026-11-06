Figure 12 and  7 highlight the effectiveness of our method with respect to a metric that more closely reflects human perception. LPIPS is a perceptual measure that leverages features from pre-trained CNNs to quantify the similarity between the feature representations of two images. Our method performs on par with ESRGAN on average (where we use only the generator component), while outperforming all other baselines.

\begin{tabular}{ccccc}
**Method** & **Dataset A** & **Dataset B** & **Dataset C** & **Average**\\
DIP-DENOISE TF & 0.1652 & 0.2253 & 0.2426 & 0.2111\\
DIP-INPAINTING TF & 0.0729 & 0.1751 & 0.1020 & 0.1166\\
DNCNN TN & 0.0435 & 0.0927 & 0.1621 & 0.0994\\
DNCNN TS & 0.0893 & 0.1606 & 0.1373 & 0.1291\\
DRUNET TN & 0.1247 & 0.1196 & 0.0879 & 0.1108\\
DRUNET TS & 0.2192 & 0.1334 & 0.1542 & 0.1690\\
ESRGAN TN & 0.0495 & 0.0928 & 0.0871 & 0.0764\\
ESRGAN TS & 0.0894 & 0.1187 & 0.1614 & 0.1231\\
MESA TF & 0.0552 & 0.0993 & 0.0839 & 0.0795\\
\end{tabular}

Test Dataset A Averages LPIPS AlexNet
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

Test Dataset B Averages LPIPS AlexNet
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

Test Dataset C Averages LPIPS AlexNet
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

All Datasets Averages LPIPS AlexNet
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

7. LPIPS Alex Network used per method across datasets and their averages.

(a) Dataset A

(b) Dataset B

(c) Dataset C

(d) All Datasets’ Averages

Fig. 12. LPIPS evaluation with Alex network usage

