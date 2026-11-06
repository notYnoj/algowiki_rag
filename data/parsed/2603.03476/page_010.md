• **Tree branches**: Number of internal nodes, i.e., non-leaf nodes, denoted by _N_<sub>branches</sub>. This counts the subdivisions within the hierarchical structure, indicating the degree of recursive decomposition.<tbc>

• **Tree balance**: Normalized measure of left/right subtree balance, quantifying symmetry. Computed as<tbc>

<tbc>\(B=1-\frac{|N_L-N_R|}{N_L+N_R},\)<tbc>

<tbc>where _N<sub>L</sub>_ and _N<sub>R</sub>_ are the numbers of nodes in left and right subtrees of the root, respectively. Perfect balance yields _B_=1.

For example, in Figure 1, both trees have 5 nodes in total, and are of max depth 3. Additionally, both have 3 leaves and 2 internal nodes, i.e., branches. Moreover, \(B=1-\frac{|1-3|}{1+3}=0.5\).

Together, the CTM-derived features provide a comprehensive characterization of EEG waveform structure that is invariant to amplitude scaling. **Tree structural features** capture the hierarchical organization of extrema, revealing the complexity and symmetry of oscillatory patterns. While **gradient features** quantify the dynamics of temporal change. This combination enables robust comparison of waveform morphology across different recording conditions and subject groups.

### 4.2 Motif Features Statistical Analysis

To evaluate group-specific differences in EEG motif features between ADHD and control groups, we conducted a comprehensive comparison across all non-initial features and EEG channels. This analysis was performed separately for both OPM-derived and CTM-derived feature sets.

For each group, median feature values were computed to represent central tendencies while mitigating the impact of outliers, which are common in EEG data due to artifacts and biological variability. Group differences were assessed using the Mann- Whitney U test (also known as the Wilcoxon rank-sum test), a non-parametric approach that makes no assumptions about the underlying distribution of the data. This test is particularly appropriate for EEG features, which often exhibit skewed or non-Gaussian distributions.

To control for multiple comparisons across the large number of features and channels tested, we applied False Discovery Rate (FDR) correction to all _p_-values using the Benjamini-Hochberg procedure with a significance threshold of _q\<_0.05. This procedure controls the expected proportion of false positives among all rejected hypotheses, providing a balance between statistical power and Type I error control. Only features that remained significant after FDR correction were considered statistically reliable and included in the final interpretation. The detailed results are presented in the following section.

## 5 Results

The results are presented in the same feature order as defined in the previous section, and separately, for OPM and CTM motifs. We analyzed motifs with support \(\ge 0.9\) for both OPM and CTM approaches, ensuring that only highly recurrent patterns were considered. The discovered OPM motifs are of length 6 and 7 (only one motif of length 8 in the ADHD group in channel 1 was discovered), while the discovered<tbc>

