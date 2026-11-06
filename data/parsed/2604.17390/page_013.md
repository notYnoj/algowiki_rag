\(\text{LogLevSimilarity}(LD)=\frac{1}{1+log_{10}(1+LD)}.\) (6)

This score maps the raw edit distance to the interval (0,1], with 1 indicating a perfect match and values tending toward 0 as the dissimilarity between the texts increases.

3 compares Log-scaled Levenshtein Similarity (LLS) with raw Levenshtein Distance (LD) . LLS compresses small edit distances via a logarithmic scale transformation producing values bounded in (0,1]. On the other side, LD simply counts minor substitutions from the original text without considering proportional significance or text length. Moreover, LLS provides a more interpretable measure of text recovery quality across texts of different lengths penalizing extra or missing content proportionally.

### 4.2 Results & Experiments

Our method has been implemented in Python using TensorFlow [1], and all experiments were conducted on an NVIDIA GeForce RTX 2080 Ti GPU with 11,GB GDDR6 RAM and a 1350,MHz base clock. We use L-BFGS [15] as the optimization algorithm and set the maximum number of epochs to 5000 (as dictated by the behavior of the L-BFGS optimizer).

\begin{tabular}{ccccc}
**Original Text** & **Estimated Text** & **LD** & **LLS** & **Error Analysis** \\
INTERNATIONALIZATION & INTERNAT1ONALIZAT1ON & 2 & 0.676 & LD = 2 / 20 characters (≈ 10% error); minor substitutions penalized disproportionately in long text; LLD reflects relative error more appropriately. \\
CAT & CUT & 1 & 0.768 & LD = 1 / 3 characters (≈ 33% error); short word appears "better" under raw LD; LLD accounts for proportional significance. \\
HELLO WORLD & HELLO & 6 & 0.765 & LD = 6 / 11 characters (≈ 55% error); recovered text is shorter, raw LD underestimates proportional error; LLD heavily penalizes missing content. \\
HELLO & HELLO ABCDEF & 6 & 0.765 & LD = 6 / 5 characters (≈ 120% error); recovered text is longer, raw LD underestimates proportional error; LLD penalizes extra content as an important factor. \\
\end{tabular}

3. Comparison of Raw Levenshtein Distance (LD) and Log-scaled Levenshtein Similarity (LLS).

