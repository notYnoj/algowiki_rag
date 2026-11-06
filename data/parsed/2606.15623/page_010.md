<tbc>and Random Elo is essentially tied with SGS on KonIQ. This pattern suggests that SGS helps most when the VLM gives a coarse but directionally useful ordering and the human budget has not already saturated the ranking.

SGS adds 345-535 automatically resolved edges on five datasets, corresponding to a 38-47% edge multiplier. These edges should not be interpreted as equivalent to human labels; their accuracy is measured separately in the controlled simulation ( 5). TID2013 produces zero inferred edges because the calibration gate disables the MergeSort backbone, yielding warm-started Active Elo rather than forcing inference from an unreliable VLM prior. The image/text split follows the same logic: perceptual IQA cues support a useful \(\pi_0\), whereas compositional semantic similarity weakens pointwise VLM scoring and makes graph-based exploration more competitive.

\begin{tabular}{ccccccccc}
 & & & & & & & & \multicolumn{2}{c}{SGS Budget} \\
Dataset & **Ours** & Active & Random & Active & RAIR-Lap. & PairS-MS & \multicolumn{2}{c}{\multirow{2}{*}{Human Inferred}} \\
 & **(SGS)** & Elo & Elo & (same) & \[12\] & \[10\] & \multicolumn{2}{c}{} \\
\multicolumn{9}{c}{_Image Quality Assessment_} \\
KonIQ \[6\] & **65.8** & 59.8 & <u>65.5</u> & 58.3 & 65.3 & 33.8 & 600 & 535 \\
LIVE-C \[5\] & **74.1** & 61.6 & 67.9 & 62.9 & <u>68.5</u> & 38.0 & 596 & 526 \\
TID2013 \[19\] & <u>65.5</u> & 59.3 & 62.3 & **64.8** & 63.4 & 42.8 & 600 & 0 \\
\multicolumn{9}{c}{_Text Similarity_} \\
BIOSSES \[23\] & <u>81.4</u> & 77.2 & 76.2 & 74.8 & **83.0** & 53.8 & 550 & 345 \\
SICKR \[13\] & 63.5 & 62.5 & <u>63.9</u> & 62.3 & **66.0** & 38.2 & 600 & 535 \\
STS-B \[3\] & **76.5** & 64.4 & 65.1 & 63.5 & <u>62.5</u> & 17.9 & 600 & 535 \\
**Average** & **71.1** & 64.1 & 66.8 & 64.4 & <u>68.1</u> & 37.4 & - & - \\
\end{tabular}

\begin{tabular}{cccc}
Dataset & Human & Inferred & Ratio \\
KonIQ-10k \[6\] & 600 & 535 & 47.1% \\
LIVE-C \[5\] & 596 & 526 & 46.9% \\
TID2013 \[19\] & 600 & 0 & 0.0% \\
BIOSSES \[23\] & 550 & 345 & 38.5% \\
SICKR-STS \[13\] & 600 & 535 & 47.1% \\
STS-B \[3\] & 600 & 535 & 47.1% \\
\end{tabular}

** 2.** Main results on 3 image (top) and 3 text (bottom) datasets. Metric: Kendall’s \(\tau\times 100\) (higher is better). "Human" and "Inferred" denote the number of human and automatically resolved comparisons used by SGS. All baselines use their full budget as human comparisons. Best in **bold**; second best <u>underlined</u>.

** 3.** Inferred comparison statistics. "Ratio" is the fraction of total (human + inferred) comparisons resolved by transitivity. TID2013 triggers the adaptive fallback (zero inferred).

