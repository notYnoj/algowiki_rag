# Approximating the Longest Common Subsequence problem within a sub-polynomial factor in linear time

Negev Shekel Nosatzki <br>
Columbia University <br>
`ns3049@columbia.edu`

**Abstract**

The Longest Common Subsequence (LCS) of two strings is a fundamental string similarity measure with a classical dynamic programming solution taking quadratic time. Despite significant efforts, little progress was made in improving the runtime. Even in the realm of approximation, not much was known for linear time algorithms beyond the trivial \(\sqrt{n}\)-approximation. Recent breakthrough result provided a \(n^{0.497}\)-factor approximation algorithm [HSSS19], which was more recently improved to a \(n^{0.4}\)-factor one[BCD21]. The latter paper also showed a \(n^{2-2.5\alpha}\) time algorithm which outputs a \(n^\alpha\) approximation to the LCS, but so far no sub-polynomial approximation is known in truly subquadratic time.

In this work, we show an algorithm which runs in _O(n_) time, and outputs a \(n^{o(1)}\)-factor approxi- mation to LCS(_x,y_), with high probability, for any pair of length _n_ input strings.

Our entire algorithm is merely an efficient black-box reduction to the Block-LIS problem, introduced very recently in [ANSS21], and solving the Block-LIS problem directly.

