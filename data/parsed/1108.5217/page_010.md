### 3.5 ABS Results

ABS gives us an option to choose the number of sequences, length of sequences, the Motif to be planted along with the probability to plant the motif as an input. We generated datasets of 50 sequences with length 500 each and planted 1 motif with probability 1. Since, ABS plants the motif exactly in about 50% of the sequences, we generate the list M of PMS motifs by finding all motifs which occur exactly in 20 out of 50 sequences.  9 presents a summary of the comparison.

## 4 Conclusions

In this paper we have compared PMSprune, one of the best known exact algorithms based on the (_l,d_) motif model, with 14 other algorithms. In particular, we have employed the 13 algorithms<tbc>

\begin{tabular}{cccccccc}
**Scoring Technique** & **nSn** & **nSp** & **sSn** & **nPPV** & **sPPV** & **nPC** & **nCC** \\
PMSSumMin & 0.1464 & 0.8304 & 0.2254 & 0.3799 & 1.0000 & 0.1168 & 0.1463 \\
PMSSumMinD & 0.1575 & 0.8148 & 0.2322 & 0.3603 & 1.0000 & 0.1058 & 0.1143 \\
PMSSumMin500 & 0.1441 & 0.8351 & 0.2253 & 0.3883 & 1.0000 & 0.1169 & 0.0762 \\
PMSSumMinD500 & 0.1181 & 0.8944 & 0.1848 & 0.4314 & 1.0000 & 0.1003 & 0.0277 \\
PMSSumMin10 & 0.1667 & 0.8342 & 0.2481 & 0.4181 & 1.0000 & 0.1364 & 0.112 \\
PMSSumMinD10 & 0.1278 & 0.8928 & 0.1890 & 0.4328 & 1.0000 & 0.1089 & 0.1275 \\
DMESumMin & 0.1416 & 0.8717 & 0.2025 & 0.4118 & 1.0000 & 0.1193 & 0.0422 \\
DMESumMinD & 0.1485 & 0.8741 & 0.2079 & 0.4300 & 1.0000 & 0.1265 & 0.0608 \\
DMESumMin500 & 0.1282 & 0.8833 & 0.1918 & 0.4232 & 0.9997 & 0.1077 & -0.02588 \\
DMESumMin10 & 0.1546 & 0.8855 & 0.2138 & 0.4553 & 1.0000 & 0.1339 & 0.0475 \\
\end{tabular}

\begin{tabular}{cccccccc}
**Scoring Technique** & **nSn** & **nSp** & **sSn** & **nPPV** & **sPPV** & **nPC** & **nCC** \\
PMSSumMin & 0.1554 & 0.8613 & 0.2458 & 0.2086 & 0.9999 & 0.0977 & 0.1554 \\
PMSSumMinD & 0.1339 & 0.8923 & 0.2142 & 0.2195 & .9999 & 0.08176 & 0.1793 \\
PMSSumMinD500 & 0.1135 & 0.9061 & 0.1555 & 0.1896 & 0.9998 & 0.0639 & 0.0935 \\
PMSSumMin500 & 0.1284 & 0.8802 & 0.2068 & 0.1879 & 0.9999 & 0.0776 & 0.1184 \\
DMESumMin & 0.1128 & 0.9121 & 0.1687 & 0.1365 & 0.9989 & 0.0453 & 0.1769 \\
DMESumMinD & 0.1043 & 0.8796 & 0.0618 & 0.1170 & 0.9999 & 0.0326 & 0.0429 \\
DMESumMin500 & 0.1189 & 0.9361 & 0.1963 & 0.1376 & 0.9998 & 0.0960 & 0.0891 \\
\end{tabular}

\begin{tabular}{cccccccc}
**Scoring Technique** & **nSn** & **nSp** & **sSn** & **nPPV** & **sPPV** & **nPC** & **nCC** \\
PMS & 0.1934 & 0.9104 & 0.2298 & 0.5275 & 1.0000 & 0.1783 & 0.2168 \\
DME & 0.1485 & 0.9148 & 0.1650 & 0.3187 & 1.0000 & 0.1256 & 0.1797 \\
\end{tabular}

7: Average Results for ChIP-Chip database

8: Average Results for ChIP-Seq database

9: Average Results for ABS database

