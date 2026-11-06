# MOMENTI: Scalable Motif Mining in Multidimensional Time Series

### ABSTRACT

Time series play a fundamental role in many domains, capturing a plethora of information about the underlying data-generating processes. When a process generates multiple _synchronized_ signals we are faced with _multidimensional_ time series. In this context a fundamental problem is that of _motif mining_, where we seek patterns repeating twice with minor variations, spanning some of the dimensions. State of the art exact solutions for this problem run in time quadratic in the length of the input time series.

We provide a scalable method to find the top-_k_ motifs in multidimensional time series with probabilistic guarantees on the quality of the results. Our algorithm runs in subquadratic time in the length of the input, and returns the exact solution with probability at least \(1-\delta\), where \(\delta\) is a user-defined parameter. The algorithm is designed to be _adaptive_ to the input distribution, self-tuning its parameters while respecting user-defined limits on the memory to use.

Our theoretical analysis is complemented by an extensive experimental evaluation, showing that our algorithm is orders of magnitude faster than the state of the art.

**PVLDB Reference Format:**<br> Matteo Ceccarello, Francesco Pio Monaco, and Francesco Silvestri.<br> MOMENTI: Scalable Motif Mining in Multidimensional Time Series.<br> PVLDB, 18(10): XXX-XXX, 2025.<br> doi:XX.XX/XXX.XX

**PVLDB Artifact Availability:**<br> The source code, data, and/or other artifacts have been made available at https://github.com/aidaLabDEI/MOMENTI-motifs.

### 1 INTRODUCTION

Time series play a central role in modeling the evolution of data- generating processes in many domains. To capture the multifaceted nature of processes generating data, time series are oftentimes _multidimensional_: collections of co-evolving signals whose measurements are synchronized, collectively describing the evolution of the process. Extracting information from such multidimensional time series is thus fundamental.

In particular, _top-k motifs_ mining is a crucial and challenging problem: intuitively, the goal is to find patterns that occur twice with minor modifications, spanning many, but not all, the signals

of the time series. More formally, given a time series **T** with _D\>_1 dimensions and _n_ points, the problem consists in finding _k_ pairs of **T**’s subsequences with the smallest distance, where the distance captures the similarity between subsequences. Indeed, similar patterns might imply a particular behavior, making motif discovery a crucial step for higher-level analysis. Applications include forecasts for volcanic eruptions [10], healthcare management [26], and machine management in industry [33]. In particular, multidimensional motif discovery is key in pollution control [27], in quality control in industrial settings [4], in activity discovery [7, 38], and in healthcare [6, 26].

A common approach to motif discovery is to extend the approach for motif mining in 1-dimension time series to the multidimensional case: that is, we look for pairs of subsequences of the time series where all the _D_ dimensions are similar. However, this approach might not reveal interesting patterns: for instance, some dimensions might be noisy or uncorrelated with respect to the others, and they might hide similar patterns involving only a subset of the dimensions that are in general unknown beforehand. We aim to discover patterns that involve only a subset of the _D_ dimensions which is unknown and needs to be retrieved as well. This formulation overcomes the limitation of several previous approximate approaches that assumed all dimensions as equally informative.

Multidimensional motifs can then be discovered with the following naive approach: for each of the 2_<sup>D</sup>_ subset of dimensions, we compare the _O(n_<sup>2</sup>) subsequences of **T** on the selected dimensions and we return the _k_ closest ones. This solution forces _O_(2_<sup>D</sup>n_<sup>2</sup>) comparisons, which, for large sets of data, are clearly prohibitive.

In this paper, we propose a scalable and efficient solution that aims at minimizing the number of distance computations to perform. We leverage Locality Sensitive Hashing (LSH), a common technique in similarity search that groups together similar elements. At a high level, we build an index of the time series where each multidimensional subsequence is mapped to a set of LSH hash values: by the properties of LSH this ensures that similar subsequences are more likely to hash to the same values across the dimensions spanned by the motif. Thanks to this index we are able to prune a hefty amount of candidates from the search space. We focus on comparisons based on the _z-normalized Euclidean Distance_, however our approach can be generalized to other similarity measures.

One of the challenges of employing LSH is setting its parameters to ensure that good quality results are retrieved efficiently, since the precise setting of the parameters is data-dependent. To overcome this challenge we design an index that automatically tunes its parameters depending on the data at hand while respecting user-specified limits on the memory to be used.

Our contributions are the following:

<sup>∗</sup>Corresponding author. This work is licensed under the Creative Commons BY-NC-ND 4.0 International License. Visit https://creativecommons.org/licenses/by-nc-nd/4.0/ to view a copy of this license. For any use beyond those covered by this license, obtain permission by emailing info@vldb.org. Copyright is held by the owner/author(s). Publication rights licensed to the VLDB Endowment. Proceedings of the VLDB Endowment, Vol. 18, No. 10 ISSN 2150-8097. doi:XX.XX/XXX.XX

Matteo Ceccarello<sup>∗</sup><br> University of Padova<br> Padova, Italy<br> matteo.ceccarello@unipd.it

Francesco Pio Monaco<br> University of Padova<br> Padova, Italy<br> monacofran@dei.unipd.it

Francesco Silvestri<br> University of Padova<br> Padova, Italy<br> francesco.silvestri@unipd.it

