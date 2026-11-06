<tbc>Figure 11 and  6 illustrate that our method surpasses the other methods in text recovery as measured by the Log Levenshtein Distance metric which is a newly proposed metric as presented in 4.1. This metric makes clear that our approach is better than no training needed counterparts (Deep Image Prior), but also from well-known networks utilized for restoring ruined inscription parts, which networks need training as is mentioned above. The higher the value the better the restoration quality.

\begin{tabular}{ccccc}
**Method** & **Dataset A** & **Dataset B** & **Dataset C** & **Average** \\
DIP-DENOISE TF & 0.3507 & 0.3885 & 0.3971 & 0.3788 \\
DIP-INPAINTING TF & 0.3508 & 0.3973 & 0.3964 & 0.3815 \\
DNCNN TN & 0.3566 & 0.3679 & 0.4015 & 0.3753 \\
DNCNN TS & 0.3524 & 0.3688 & 0.3936 & 0.3716 \\
DRUNET TN & 0.3527 & 0.3768 & 0.3877 & 0.3724 \\
DRUNET TS & 0.3401 & 0.3768 & 0.3991 & 0.3720 \\
ESRGAN TN & 0.3550 & 0.3634 & 0.4043 & 0.3743 \\
ESRGAN TS & 0.3567 & 0.3725 & 0.3938 & 0.3743 \\
MESA TF & 0.3527 & 0.3897 & 0.4104 & 0.3843 \\
\end{tabular}

Test Dataset A Averages Log Levenshtein Similarity
OURS NT
ESRGAN TS
ESRGAN TN
DRUNET TS
DRUNET TN
DNCNN TS
DNCNN TN
DIP-INPAINTING NT
DIP-DENOISE NT
0.33
0.335
0.34
0.345
0.35
0.355
0.36

Test Dataset B Averages Log Levenshtein Similarity
OURS NT
ESRGAN TS
ESRGAN TN
DRUNET TS
DRUNET TN
DNCNN TS
DNCNN TN
DIP-INPAINTING NT
DIP-DENOISE NT
0.34
0.35
0.36
0.37
0.38
0.39
0.4

Test Dataset C Averages Log Levenshtein Similarity
OURS NT
ESRGAN TS
ESRGAN TN
DRUNET TS
DRUNET TN
DNCNN TS
DNCNN TN
DIP-INPAINTING NT
DIP-DENOISE NT
0.375
0.38
0.385
0.39
0.395
0.4
0.405
0.41
0.415

All Datasets Averages Log Levenshtein Similarity
OURS NT
ESRGAN TS
ESRGAN TN
DRUNET TS
DRUNET TN
DNCNN TS
DNCNN TN
DIP-INPAINTING NT
DIP-DENOISE NT
0.365
0.37
0.375
0.38
0.385

6. Log-scaled Levenshtein Similarity per method across datasets and their averages.

(a) Dataset A

(b) Dataset B

(c) Dataset C

(d) All Datasets’ Averages

Fig. 11. Log-scaled Levenshtein Similarity evaluation as described in 4.1

