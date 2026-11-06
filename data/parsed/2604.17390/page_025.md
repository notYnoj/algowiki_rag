<tbc>is not the primary objective of our approach, as we focus on inscription text recovery rather than exact pixel reconstruction. Nonetheless, we report PSNR for completeness, since it is one of the most widely used metrics in image processing and computer vision.

Regenerate Copy Good response Bad response

## 5 Discussion, Conclusions & Future Work

In this work, we introduced _MESA_, a training-free, multi-exemplar, style-aware method for the restoration of degraded inscriptions. Unlike conventional supervised approaches such as DRUNET, DnCNN, and ESRGAN, our method does not require paired ruined/clean datasets or extensive pretraining. Instead, it leverages clean exemplars from the same or similar inscription styles to guide the reconstruction process, making it particularly suitable for cultural heritage scenarios where annotated data are scarce or prohibitively expensive to obtain. It also offers a competitive alternative to training-free baselines such as Deep Image Prior (DIP), while providing superior performance both visually and according to multiple quantitative metrics.

A key characteristic and potential limitation of MESA, despite its material independence, lies in its reliance on the availability of well-preserved and stylistically relevant exemplar inscriptions. The core mechanism of our approach, which leverages Gram matrices and minimizes Mean-Squared Displacement (MSD) for feature matching, is designed to capture and transfer texture, style, and stroke structure from these exemplars to the damaged input. This exemplar-driven approach is a strength in specific cultural heritage contexts, especially<tbc>

Dataset A Averages - PSNR MESA TF ESRGAN TS ESRGAN TN DRUNET TS DRUNET TN DNCNN TS DNCNN TN DIP-INPAITFING TF DIP-DENOISE TF 0
5 10 15 20 25 30 35 40

Dataset B Averages - PSNR MESA TF ESRGAN TS ESRGAN TN DRUNET TS DRUNET TN DNCNN TS DNCNN TN DIP-INPAITFING TF DIP-DENOISE TF 0
5 10 15 20 25 30 35 40

Dataset C Averages - PSNR MESA TF ESRGAN TS ESRGAN TN DRUNET TS DRUNET TN DNCNN TS DNCNN TN DIP-INPAITFING TF DIP-DENOISE TF 0
5 10 15 20 25 30 35 40

All Datasets Averages - PSNR MESA TF ESRGAN TS ESRGAN TN DRUNET TS DRUNET TN DNCNN TS DNCNN TN DIP-INPAITFING TF DIP-DENOISE TF 0
5 10 15 20 25 30 35 40

(a) Dataset A

(b) Dataset B

(c) Dataset C

(d) All Datasets’ Averages

Fig. 15. PSNR evaluation

