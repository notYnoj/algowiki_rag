<tbc>where _LD(o,r_) is the Levenshtein distance [13] between the original text _o_ and the recovered text _r_, and _S_ is a fixed positive integer that specifies the maximum number of edit operations considered. In our experiments, we set _S=_100, which is a reasonable choice in many cases, clamping all larger distances to 100. A perfect match yields 0, while any distance \(\ge\) 100 is effectively treated as 100. The resulting values are bounded in [0,1].

To illustrate the advantage of TRS over the raw Levenshtein Distance, consider the example shown in  2. _Inthe firstcase, alongtextualsentencecontainsamoderatenumberofOCR-inducedsubstitutionerrors, resultinginaneditdistanceof_18 While the raw Levenshtein Distance grows unbounded and disproportionately penalizes such catastrophic failures, TRS assigns a moderate score to the partially recovered text and clamps the completely corrupted output to a score of 0. This behavior ensures that realistic variations in OCR quality are preserved, while preventing extreme outliers from dominating aggregated evaluation results.

Each row in  2 illustrates a different type of text error-minor substitutions, complete corruption, missing content or extra content and shows how raw Levenshtein Distance (LD) and the Text Recovery Score (TRS) evaluate these cases. TRS normalizes and clamps the edit distance producing a bounded score between 0 and 1 and proportionally penalizes missing or extra content providing a more interpretable measure than raw LD. This metric is consistent with previous work on normalized text similarity metrics which are bounded to [0,1].

The second metric is a log-scaled Levenshtein-based similarity which applies a logarithmic transformation to the raw edit distance. This emphasizes small differences while compressing the penalty for large errors. The score lies strictly in (0,1], with 1 corresponding to a perfect match and values approaching 0 for highly divergent texts:<tbc>

\begin{tabular}{ccccc}
**Original Text** & **Recovered Text** & **LD** & **TRS** & **Error Analysis** \\
THE HISTORY OF ANCIENT & THE H1STORY OF ANC1ENT & 7 & 0.93 & LD = 7 / 62 characters (≈ 11% error); minor substitutions, raw LD appears large; TRS penalizes incorrect content proportionally. \\
CIVILIZATIONS IS COMPLEX AND MULTIFACETED & CIVIL1ZATI0NS IS C0MPLEX AND MULT1FACETED & & & \\
THE HISTORY OF ANCIENT & xQ9@!#%\\ \(^\unknown\)()? \> \<{} & 101 & 0.00 & LD = 101 / 62 characters (≈ 163% error); complete corruption, raw LD grows unbounded; TRS heavily penalizes missing or incorrect content. \\
CIVILIZATIONS IS COMPLEX AND MULTIFACETED & abcd1234567890 & & & \\
HELLO WORLD & HELLO & 6 & 0.94 & LD = 6 / 11 characters (≈ 55% error); recovered text is shorter; TRS penalizes missing content. \\
HELLO & HELLO ABCDEF & 6 & 0.94 & LD = 6 / 5 characters (≈ 120% error); recovered text is longer; TRS penalizes extra content appropriately. \\
\end{tabular}

2. Comparison between Levenshtein Distance (LD) and the proposed Text Recovery Score (TRS) with fixed normalization (_S=_100).

