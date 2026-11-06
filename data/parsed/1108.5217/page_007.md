sTP, sTN, sFP, sFN. Use these values to compute the 7 Statistical measures nSn, nSp, sSn, nPPV, sPPV, nPC, and nCC.

## 3 Results and Discussions

### 3.1 Result for Tompa’s dataset

We tested PMSprune and DME on ChIP-Chip, ChIP-Seq, ABS and Tompa’s datasets \[TLB<sup>+</sup>\].  2 shows the results for 13 algorithms that were initially evaluated in \[TLB<sup>+</sup>\]. The data for the table was obtained from `http://bio.cs.washington.edu/assessment/assessment\_result.html`. The table shows the average values over all the datasets for all four species. It is observed that ANN-Spec shows the best result based on Sensitivity which is 0.087 followed by Weeder with Sensitivity as 0.086. Both PMSprune and DME perform better than these 13 algorithms on sensitivity and other measures. However, when it comes to specificity, many of the 13 algorithms perform better.

\begin{tabular}{cc}
**Length(s)** & **Hamming Distance** \\
5,6 & 1 \\
6, 8 & 2 \\
9, 10, 11 & 3 \\
12, 13, 14 & 4 \\
15 & 5 \\
\end{tabular}

\begin{tabular}{cccccccc}
**Algorithm** & **nSn** & **nSp** & **sSn** & **nPPV** & **sPPV** & **nPC** & **nCC** \\
AlignACE & 0.0551 & 0.9914 & 0.0881 & 0.1118 & 0.1226 & 0.0383 & 0.0650 \\
ANN-Spec & 0.0870 & 0.9822 & 0.1551 & 0.0881 & 0.0848 & 0.0458 & nan \\
Consensus & 0.0205 & 0.9968 & 0.0402 & 0.1132 & 0.1329 & 0.0176 & 0.0404 \\
GLAM & 0.0257 & 0.9872 & 0.0459 & 0.0381 & 0.0482 & 0.0156 & nan \\
The Improbizer & 0.0685 & 0.9819 & 0.1226 & 0.0695 & 0.0836 & 0.0357 & nan \\
MEME & 0.0670 & 0.9890 & 0.1111 & 0.1071 & 0.1394 & 0.0430 & 0.0706 \\
MEME3 & 0.0776 & 0.9847 & 0.1245 & 0.0909 & 0.1348 & 0.0437 & nan \\
MITRA & 0.0313 & 0.9906 & 0.0498 & 0.0623 & 0.0623 & 0.0213 & 0.0309 \\
MotifSampler & 0.0600 & 0.9901 & 0.0977 & 0.1069 & 0.1013 & 0.0399 & 0.0666 \\
Oligo/dyad-analysis & 0.0398 & 0.9957 & 0.0727 & 0.1542 & 0.1214 & 0.0326 & 0.0694 \\
QuickScore & 0.0174 & 0.9889 & 0.0325 & 0.0301 & 0.0185 & 0.0111 & 0.0083 \\
SeSiMCMC & 0.0611 & 0.9685 & 0.0804 & 0.0369 & 0.0751 & 0.0235 & 0.0493 \\
Weeder & 0.0863 & 0.9960 & 0.1609 & 0.2996 & 0.2886 & 0.0718 & 0.1523 \\
YMF & 0.0639 & 0.9920 & 0.1206 & 0.1369 & 0.1200 & 0.0455 & 0.0815 \\
\end{tabular}

1: The (_l,d_) pairs used for testing

2: Results for 13 algorithms evaluated in Tompa _et. al._ \[12\]

