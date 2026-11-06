Tensor Ranks and the Fine-Grained Complexity of Dynamic Programming

**Abstract**

Generalizing work of Künnemann, Paturi, and Schneider [ICALP 2017], we study a wide class of high- dimensional dynamic programming (DP) problems in which one must find the shortest path between two points in a high-dimensional grid given a tensor of transition costs between nodes in the grid. This captures many classical problems which are solved using DP such as the knapsack problem, the airplane refueling problem, and the minimal-weight polygon triangulation problem. We observe that for many of these problems, the tensor naturally has low tensor rank or low slice rank.

We then give new algorithms and a web of fine-grained reductions to tightly determine the complexity of these problems. For instance, we show that a polynomial speedup over the DP algorithm is possible when the tensor rank is a constant or the slice rank is 1, but that such a speedup is impossible if the tensor rank is slightly super-constant (assuming SETH) or the slice rank is at least 3 (assuming the APSP conjecture). We find that this characterizes the known complexities for many of these problems, and in some cases leads to new faster algorithms.

## 1 Introduction

Dynamic programming (DP) is one of the most common algorithmic paradigms, used throughout the theory and practice of diverse computational domains. See [CLRS01] chapter 14 for a detailed introduction.

When one solves a problem using DP, a natural question arises: is this the fastest algorithm to solve the problem? Recently, fine-grained complexity has been used to show that for many important problems, the answer is yes. For instance, researchers have established conditional lower bounds for the longest common subsequence [ABW15, BK15], edit distance [BI15], Fréchet distance [Bri14], and regular expression matching [BI16], showing that there is no algorithm (whether or not it uses DP) that is faster than the standard DP algorithm by a polynomial factor.

On the other hand, there are some notable examples where a natural DP formulation is _not_ the fastest known way to solve a problem. Consider, for instance, the polygon triangulation problem from computational geometry. In this problem, we are given as input a convex polygon with _n_ nodes, where each node _i_ has a weight _w<sub>i</sub>_. For each triple _i,j,k_ of nodes, a triangle with those nodes as vertices has weight \(w_i\cdot w_j\cdot w_k\). The weight of a triangulation of the polygon is the sum of the weights of its constituent triangles. The goal in the problem is to find the triangulation of the polygon with minimum weight. This problem has applications in point visibility [Her89], mesh generation [BE95], computer graphics [NM95], and even in visual cryptography [SSMB12].

Polygon triangulation has a natural DP formulation as follows. Let _T[i,j_] denote the minimum weight of a triangulation of the polygon consisting of just nodes _i,i_+1_,i_+2_,...,j_ with an edge drawn between nodes

<sup>∗</sup>Department of Computer Science, Columbia University, NY 10027. Email: `josh@cs.columbia.edu`. <sup>†</sup>Department of Computer Science, Columbia University, NY 10027. Email: `ezt2102@columbia.edu`. <sup>‡</sup>Department of Computer Science, Columbia University, NY 10027. Email: `hantao.yu@columbia.edu`. <sup>§</sup>Department of Computer Science, Columbia University, NY 10027. Email: `hz2663@columbia.edu`.

Josh Alman<sup>∗</sup> Ethan Turok<sup>†</sup> Hantao Yu<sup>‡</sup> Hengzhi Zhang §

January 3, 2024

arXiv:2309.04683v2 [cs.CC] 2 Jan 2024

