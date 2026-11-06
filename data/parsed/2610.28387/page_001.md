Exact Covariance Structure and Efficient Computation for L-Comments

**Abstract**

L-moments are useful summary statistics and so have been widely employed in statistical analysis. L-comoments provide a multivariate generalization of L-moments. Joint finite- sample covariance structure, which represents the sampling uncertainty, of L-comoments is less well understood than that of univariate L-moments. We thus derive exact finite-sample covariance formulas for sample L-comoments using explicit conditional U-statistic kernels. We further construct an asymptotic projection estimator and an unbiased estimator of the finite-sample covariance matrix and develop positive-definite corrections. An efficient rank-prefix algorithm evaluates the full unbiased covariance estimator in _O(n_<sup>2</sup>) time without enumerating disjoint subsets. Numerical experiments demonstrate substantial computational savings. The results provide a basis for first-order covariance approximations for L-comoment ratios and for subsequent multivariate L-moment estimation.

**Keywords:** Concomitant; U-statistic; covariance estimation; Gini covariance; exact unbiased estimation; L-moments; rank-prefix algorithm.

**MSC 2020:** 62G05, 62H20, 62G30.

## 1 Introduction

L-moments summarize distributional location, scale, and shape through linear combinations of order statistics and require only first moments for their existence (Hosking, 1990). Methods based on L-moments have been widely used for distributional analysis and parameter estimation, notably through the method of L-moments estimation. Compared with conventional moments,<tbc>

arXiv:2610.28387v1 [stat.ME] 20 Oct 2026

Palakorn Seenoi<sup>_a_</sup>

Jeong-Soo Park<sup>_b,_∗</sup>

<sup>_a_</sup>Department of Statistics, Faculty of Science, Khon Kaen University

Khon Kaen 40002, Thailand

<sup>_b_</sup>Department of Statistics, Chonnam National University

Gwangju 61186, South Korea

<sup>∗</sup>Corresponding author: jsparkstat@gmail.com

October 21, 2026

