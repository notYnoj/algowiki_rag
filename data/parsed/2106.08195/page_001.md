# A Linear-Time _n_<sup>0.4</sup>-Approximation for Longest Common Subsequence

Karl Bringmann<sup>∗</sup>

Vincent Cohen-Addad<sup>†</sup>

Debarati Das<sup>‡</sup>

**Abstract**

We consider the classic problem of computing the Longest Common Subsequence (LCS) of two strings of length _n_. While a simple quadratic algorithm has been known for the problem for more than 40 years, no faster algorithm has been found despite an extensive effort. The lack of progress on the problem has recently been explained by Abboud, Backurs, and Vassilevska Williams [FOCS’15] and Bringmann and Künnemann [FOCS’15] who proved that there is no subquadratic algorithm unless the Strong Exponential Time Hypothesis fails. This major roadblock for getting faster exact algorithms has led the community to look for subquadratic _approximation_ algorithms for the problem.

Yet, unlike the edit distance problem for which a constant-factor approximation in almost-linear time is known, very little progress has been made on LCS, making it a notoriously difficult problem also in the realm of approximation. For the general setting (where we make no assumption on the length of the optimum solution or the alphabet size), only a naive \(O(n^{\varepsilon/2})\)-approximation algorithm with running time \(\widetilde{O}(n^{2-\varepsilon})\) has been known, for any constant \(0<\varepsilon\le 1\). Recently, a breakthrough result by Hajiaghayi, Seddighin, Seddighin, and Sun [SODA’19] provided a linear-time algorithm that yields a _O(n_<sup>0.497956</sup>)- approximation in expectation; improving upon the naive \(O(\sqrt{n})\)-approximation for the first time.

In this paper, we provide an algorithm that in time \(O(n^{2-\varepsilon})\) computes an \(\widetilde{O}(n^{2\varepsilon/5})\)-approximation with high probability, for any \(0<\varepsilon\le 1\). Our result (1) gives an \(\widetilde{O}(n^{0.4})\)-approximation in linear time, improving upon the bound of Hajiaghayi, Seddighin, Seddighin, and Sun, (2) provides an algorithm whose approximation scales with any subquadratic running time \(O(n^{2-\varepsilon})\), improving upon the naive bound of \(O(n^{\varepsilon/2})\) for any \(\varepsilon\), and (3) instead of only in expectation, succeeds with high probability.

### 1 Introduction

The longest common subsequence (LCS) of two strings _x_ and _y_ is the longest string that appears as a subsequence of both strings. The length of the LCS of _x_ and _y_, which we denote by _L(x,y_), is one of the most fundamental measures of similarity between two strings and has drawn significant interest in last five decades, see, e.g. [35, 6, 26, 27, 30, 32, 10, 31, 11, 36, 22, 16, 28, 2, 19, 4, 20, 3, 33, 34, 24]. On strings of length _n_, the LCS problem can be solved exactly in quadratic time _O(n_<sup>2</sup>) using a classical dynamic programming approach [35]. Despite an extensive line of research the quadratic running time has been improved only by logarithmic factors [30]. This lack of progress is explained by a recent result showing that any truly subquadratic algorithm for LCS would falsify the Strong Exponential Time Hypothesis (SETH); this has been proven independently by Abboud et al. [2] and by Bringmann and Künnemann [19]. Further work in this direction shows that even a high polylogarithmic speedup for LCS would have surprising consequences [4, 3]. For the closely related edit distance the situation is similar, as the classic quadratic running time can be improved by logarithmic factors, but any truly subquadratic algorithm would falsify SETH [12].

<sup>∗</sup>Saarland University and Max-Planck-Institute for Informatics, Saarland Informatics Campus, Saarbrücken, Germany. `bringmann@cs.uni-saarland.de`. This work is part of the project TIPEA that has received funding from the European Research Council (ERC) under the European Unions Horizon 2020 research and innovation programme (grant agreement No. 850979). <sup>†</sup>Sorbonne Université, UPMC Univ Paris 06, CNRS, LIP6, Paris, France. `vcohenad@gmail.com`. <sup>‡</sup>Basic Algorithm Research Copenhagen (BARC), University of Copenhagen, Denmark. `debaratix710@gmail.com`. Work supported by Basic Algorithms Research Copenhagen, grant 16582 from the VILLUM Foundation.

