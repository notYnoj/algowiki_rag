# Approximating LCS in Linear Time: Beating the \(\sqrt{n}\) Barrier<sup>∗†</sup>

**Abstract**

Longest common subsequence (LCS) is one of the most fundamental problems in combinatorial optimization. Apart from theoretical importance, LCS has enormous applications in bioinformatics, revision control systems, and data comparison programs<sup>1</sup>. Although a simple dynamic program computes LCS in quadratic time, it has been recently proven that the problem admits a conditional lower bound and may not be solved in truly subquadratic time [2]. In addition to this, LCS is notoriously hard with respect to approximation algorithms. Apart from a trivial sampling technique that obtains a _n<sup>x</sup>_ approximation solution in time _O(n_<sup>2-2_x_</sup>) nothing else is known for LCS. This is in sharp contrast to its dual problem _edit distance_ for which several linear time solutions are obtained in the past two decades [4, 5, 9, 10, 16].

In this work, we present the first nontrivial algorithm for approximating LCS in linear time. Our main result is a linear time algorithm for the longest common subsequence which has an approximation factor of _O(n_<sup>0.497956</sup>). This beats the \(\sqrt{n}\) barrier for approximating LCS in linear time.

### 1 Introduction

Longest common subsequence (LCS) is a central problem in combinatorial optimization and has been subject to many studies since the 1950s [2, 7, 11, 12, 13, 18, 20, 21, 22, 23, 25, 27, 28, 31]. In this problem, we are given two strings _s_ and <o>_s_</o> of size _n_ and the goal is to find the longest string _t_ which appears as a (not necessarily consecutive) subsequence in both _s_ and <o>_s_</o>. It is known since 1950 [11] that LCS can be dynamically solved in time _O(n_<sup>2</sup>) using the following recursive formula:

\(T[i][j]=\left\{\begin{array}{ c c } 1+T[i-1][j-1], &  \\ \mathrm{max}\left\{\begin{array}{ c } T[i-1][j-1], &  \\ T[i][j-1], &  \end{array}\right\} & \text{if}s_i\neq\overline{s_j}.\)

Although this solution is almost as old as the emergence of dynamic programming as an algorithmic tool, thus far the only improvements to this algorithm were limited to shaving

<sup>∗</sup>A portion of this work was completed while some of the authors were visiting Simons Institute for Theory of Computing. <sup>†</sup>Supported in part by NSF CAREER award CCF-1053605, NSF AF:Medium grant CCF-1161365, NSF BIGDATA grant IIS-1546108, NSF SPX grant CCF-1822738, and two small UMD AI in Business and Society Seed Grant and UMD Year of Data Science Program Grant <sup>‡</sup>University of Maryland \(^\mathsection\)Sharif University of Technology \(^\unknown\)University of Illinois at Chicago <sup>1</sup>A notable example is the UNIX application diff

MohammadTaghi Hajiaghayi<sup>‡</sup>

Masoud Seddighin<sup>§</sup>

Saeed Seddighin<sup>†</sup>

Xiaorui Sun\(^\unknown\)

