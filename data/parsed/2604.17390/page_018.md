<tbc>In Figure 9 and  4, we present the Levenshtein distance results, from which we observe that our method, on average, outperforms the baselines by requiring fewer operations to transform the recovered output into the ground-truth text. A lower distance indicates a better restoration quality. Both the ground-truth and recovered texts are obtained using Tesseract [19], and the same procedure is applied to all results presented in these figures.

\begin{tabular}{ccccc}
**Method** & **Dataset A** & **Dataset B** & **Dataset C** & **Average** \\
DIP-DENOISE TF & 70.3333 & 37.0000 & 32.0000 & 46.4444 \\
DIP-INPAINTING TF & 70.2222 & 32.5556 & 32.6667 & 45.1481 \\
DNCNN TN & 63.3333 & 51.3333 & 30.3333 & 48.3333 \\
DNCNN TS & 68.6667 & 54.0000 & 34.0000 & 52.2222 \\
DRUNET TN & 67.6667 & 48.3333 & 37.3333 & 51.1111 \\
DRUNET TS & 86.3333 & 47.0000 & 31.3333 & 54.8889 \\
ESRGAN TN & 65.0000 & 55.6667 & 29.0000 & 49.8889 \\
ESRGAN TS & 65.0000 & 64.0000 & 34.0000 & 54.3333 \\
MESA TF & 68.3333 & 36.0000 & 26.6667 & 43.6667 \\
\end{tabular}

Test Dataset A Averages Levenshtein Distance
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
10
20
30
40
50
60
70
80
90

Test Dataset B Averages Levenshtein Distance
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
10
20
30
40
50
60
70

Test Dataset C Averages Levenshtein Distance
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
5
10
15
20
25
30
35
40

All Datasets Averages Levenshtein Distance
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
10
20
30
40
50
60

4. Levenshtein Distance per method across datasets and their averages.

(a) Dataset A

(b) Dataset B

(c) Dataset C

(d) All Datasets’ Averages

Fig. 9. Levenshtein Distance evaluation

