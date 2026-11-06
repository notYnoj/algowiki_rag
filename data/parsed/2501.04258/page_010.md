<tbc>ette score and homogeneity score, indicating poor clustering performance on these two datasets. Similarly, while GMM has the highest sensitivities on Datasets V4&5 and V6, its silhouette and homogeneity scores are the lowest among the clustering methods evaluated. This suggests that relying solely on sensitivity to choose the suitable clustering methods for identifying top RNA-like graphs may not be sufficient. Therefore, a more comprehensive approach, considering multiple evaluation metrics and clustering algorithms are necessary to assess their performance and hence prediction regarding most likely RNA-like graphs.

### 3.1.3 Comparison of different feature performance of _k_-means clustering

For the _k_-means clustering method, we also evaluate in  3 the _s_ and _e_ features as used before \[10\] compared to the topological and geometric features by PSG introduced in this work. We see that the sensitivity (the percentage of existing graph topologies in 2021 dataset correctly clustered into the RNA-like cluster) has been improved by PSG features from 88.288% to 97.297% on Dataset All.

## 3.2 Top central structures within clusters among six clustering methods.

Now it is interesting to explore the most RNA-like and unlikely RNA-like predicted hypothetical graphs. For each dataset (V4&5, V6, V7, V8, V9, and All), we selected the top 15 RNA-like hypothetical graphs closest to the center of the RNA-like cluster and the top 15 non-RNA-like hypothetical graphs closest to the center of the non-RNA-like cluster using each of the six clustering methods. We then collect graphs that commonly appeared in the top 15 lists of three, four, and five clustering algorithms, for both RNA-like and non-RNA-like structures. These motifs are considered to be the most likely RNA-like 2D structures.

\begin{tabular}{cccccccc}
 & & \multicolumn{6}{c}{**Datasets**} \\
 & & **V4\&5** & **V6** & **V7** & **V8** & **V9** & **All** \\
_k_-means & Sensitivity(%) & **72.973** & **86.364** & 85.714 & **92.857** & **94.118** & **97.297** \\
 & RNA-like(%) & 59.712 & 55.118 & 49.079 & 48.712 & 46.241 & 46.017 \\
Mini-batch _k_-means & Sensitivity(%) & 56.757 & **86.364** & **95.238** & **92.857** & **94.118** & **97.297** \\
 & RNA-like(%) & 42.446 & 56.496 & 59.153 & 48.541 & 42.683 & 46.795 \\
GMM & Sensitivity(%) & 86.486 & 90.909 & 90.476 & 78.571 & 94.118 & 90.090 \\
 & RNA-like(%) & 76.259 & 72.638 & 72.677 & 72.904 & 73.517 & 73.412 \\
Hierarchical (ward) & Sensitivity(%) & 67.568 & 86.364 & 71.429 & 100.000 & NA & NA \\
 & RNA-like(%) & 61.151 & 60.236 & 33.242 & 69.659 & NA & NA \\
Spectral & Sensitivity(%) & 70.270 & 86.364 & 90.476 & 78.571 & 100.000 & 100.000 \\
 & RNA-like(%) & 58.993 & 60.630 & 90.396 & 99.843 & 98.189 & 99.990 \\
Birch & Sensitivity(%) & 83.784 & 86.364 & 57.143 & 85.714 & 94.118 & 76.577 \\
 & RNA-like(%) & 85.612 & 68.504 & 29.008 & 48.480 & 62.461 & 32.505 \\
\end{tabular}

\begin{tabular}{cccccccc}
 & & \multicolumn{6}{c}{**Datasets**} \\
 & & **V4\&5** & **V6** & **V7** & **V8** & **V9** & **All** \\
_k_-means _s_ and _e_ & Sensitivity(%) & 70.270 & 72.727 & 57.143 & 64.286 & 64.706 & 88.288 \\
 & RNA-like(%) & 70.504 & 67.913 & 71.815 & 69.843 & 71.749 & 72.169 \\
_k_-means PSG & Sensitivity(%) & **72.973** & **86.364** & **85.714** & **92.857** & **94.118** & **97.297** \\
 & RNA-like(%) & 59.712 & 55.118 & 49.079 & 48.712 & 46.241 & 46.017 \\
\end{tabular}

2: Comparison of sensitivity and percentage of RNA-like graphs under six clustering methods. The red values denote predictions by the _k_-mean and mini-batch _k_-mean methods of the RNA-like group size.

3: Comparison of sensitivity and percentage of RNA-like graphs using different features for _k_-means clustering.

