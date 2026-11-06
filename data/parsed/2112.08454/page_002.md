## 1 Introduction

The Longest Common Subsequence problem (LCS) is a classical string alignment problem. Formally, given two strings _x,y_ of length _n_ over alphabet \(\Sigma\), the longest common subsequence between _x_ and _y_ is the largest string which appears as a subsequence in both _x_ and _y_. The (length of the) LCS has a classical dynamic programming solution in quadratic time \[WF74\].

LCS is also a fundamental string similarity measure of key importance both in theory and practice, and therefore has been extensively studied during the course of the past 50 years \[UAH76, Hir77, HS77, AG87, EGGI92, SW07, RSSS19, RS20\], with the main goal of improving the run-time from polynomial towards close(r) to linear.

Despite significant attention, little progress was made, and the runtime has improved by logarithmic factors only \[MP80\]. More recently, fine-grained hardness results helped explaining the lack of progress, showing that any truly subquadratic solution for LCS would refute the Strong Exponential Time Hypothesis (SETH)\[ABW15, BK15\]. Moreover, for the LCS problem in particular, it was later shown that even a high polylogarithmic speedup would be surprising \[AHWW16, AB18\].

Even before the above hardness results, researchers started considering faster algorithms that approximate the LCS, but there as well the progress has been slow. The trivial \(\sqrt{n}\)-factor approximation was only recently improved to ≈_n_<sup>0.497</sup> \[HSSS19\] and even more recently to _n_<sup>0.4</sup> \[BCD21\]. In parallel, a parametrized version was developed which gives a subquadratic solution with improved approximation when the longest common subsequence is promised to be above a certain threshold \[RSSS19\].

In contrast, the progress for the corresponding Edit Distance problem has been more "rosy", with a series of advances \[BJKK04, BES06, AKO10, CDG<sup>+</sup>18\], recently culminating in a near-linear time, constant factor approximation algorithm \[AN20\].

### 1.1 Main result

Our main result is a sub-polynomial factor approximation algorithm for LCS, which runs in linear time.

**Theorem 1.** LCS_<sub>n</sub> can be approximated up to n_<sup>_o_(1)</sup>_-factor, with high probability, and in O(n_) _time._

While we do not track the exact approximation factor in our analysis, we note it is \(exp\left(\frac{log(n)}{log^clog(n)}\right)\) for some absolute constant _c_. Interesting enough, we could not find a way to significantly improve the bound above, obtainable in linear time, even if one can afford _n_<sup>1.99</sup> runtime. This relates to the issue of balancing of dense and sparse cases described in \[ANSS21\], which is the core component of our algorithm.

To improve the bound, one would need to find a more efficient way to solve the Block-LIS algorithm from \[ANSS21\].

One of the implications of this paper is that an affirmative resolution to the open question posed in \[ANSS21\] would yield surprising results, and in particular, a near-linear time, \((1+\epsilon)\) approximation to LCS, which also provides near-linear \(\epsilon n\) additive approximation to the edit distance.

## 2 Preliminaries

### 2.1 Definitions

**Sequences.** Fix alphabet \(\Sigma\). We denote \(x\in\Sigma^n\) as a length _n_ sequence.

For a sequence _x_, we denote by \(\psi(x):\Sigma\rightarrow\unknown\), the count vector of letters in _x_, i.e., \(\psi(x)_c\unknown|x^{-1}(c)|\) for any \(c\in\Sigma\).

We also define integer block sequence \(z\in\unknown^{n\times k}\), and denote |_z_| as the count of all integers in all the blocks (with repetitions).

