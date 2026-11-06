# Approximation Algorithms for LCS and LIS with Truly Improved Running Times<sup>∗</sup>

Aviad Rubinstein<sup>†</sup><tbc>

<tbc>Saeed Seddighin<sup>‡</sup><tbc>

<tbc>Zhao Song<sup>§</sup><tbc>

<tbc>Xiaorui Sun<sup>¶</sup>

November 23, 2021

**Abstract**

Longest common subsequence (LCS) is a classic and central problem in combinatorial optimization. While LCS admits a quadratic time solution, recent evidence suggests that solving the problem may be impossible in truly subquadratic time. A special case of LCS wherein each character appears at most once in every string is equivalent to the longest increasing subsequence problem (LIS) which can be solved in quasilinear time. In this work, we present novel algorithms for approximating LCS in truly subquadratic time and LIS in truly sublinear time. Our approximation factors depend on the ratio of the optimal solution size over the input size. We denote this ratio by \(\lambda\) and obtain the following results for LCS and LIS without any prior knowledge of \(\lambda\).

• A truly subquadratic time algorithm for LCS with approximation factor \(\Omega(\lambda^3)\).

• A truly sublinear time algorithm for LIS with approximation factor \(\Omega(\lambda^3)\).

Triangle inequality was recently used by Boroujeni, Ehsani, Ghodsi, HajiAghayi and Seddighin [BEG<sup>+</sup>18] and Charkraborty, Das, Goldenberg, Koucky and Saks [CDG<sup>+</sup>18] to present new approximation algorithms for edit distance. Our techniques for LCS extend the notion of triangle inequality to non-metric settings.

<sup>∗</sup>A preliminary version of this work is appeared in FOCS’19. <sup>†</sup>Stanford University. aviad@stanford.edu <sup>‡</sup>Toyota Technological Institute at Chicago. saeedreza.seddighin@gmail.com <sup>§</sup>Adobe Research. zsong@adobe.com <sup>¶</sup>University of Illinois. xiaorui@uic.edu

