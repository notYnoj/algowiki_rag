# Exponential Time Approximations for Coloring 3-Colorable Graphs

Venkatesan Guruswami<sup>∗</sup>

Rhea Jain<sup>†</sup>

**Abstract**

The problem of efficiently coloring 3-colorable graphs with few colors has received much attention on both the algorithmic and inapproximability fronts. We consider exponential time approximations, in which given a parameter _r_, we aim to develop an _r_-approximation algorithm with the best possible runtime, providing a tradeoff between runtime and approximation ratio. In this vein, an algorithm to \(O(n\epsilon)\)-color a 3-colorable graphs in time \(2^{\Theta(n^{1-2\epsilon} log(n))}\) is given in (Atserias and Dalmau, SODA 2022.)

We build on tools developed in (Bansal et al., Algorithmic, 2019) to obtain an algorithm to color 3-colorable graphs with _O(r_) colors in \(exp\left(\tilde{O}\left(\frac{nlog^{11/2}r}{r^3}\right)\right)\) time, asymptotically improving upon the bound given by Atserias and Dalmau.

### 1 Introduction

Graph Coloring is a classic and fundamental problem in theoretical computer science with applications in scheduling, register allocation, and more. A graph is said to be _r_-colorable if there is an assignment of _r_ colors to vertices such that no two adjacent vertices share the same color. The question of whether a given graph can be colored using _r_ colors for \(r\ge 3\) was one of Karp’s NP- complete problems [19]. For any graph _G_, the minimum _r_ such that _G_ is _r_-colorable is called the _chromatic number_ of _G_; it is known that the chromatic number is hard to approximate to a factor _n_<sup>1-_o_(1)</sup> [15, 23].

It is natural to ask if one can obtain a valid coloring of a graph with few colors if its chromatic number is known. The first polynomial time algorithm for this problem was given by Wigderson [25], who obtained an \(O(n^{1-\frac{1}{r-1}})\)-coloring for _r_-colorable graphs. In this paper we focus on the special case where _G_ is 3-colorable. There are several known polynomial time algorithms for this setting. Blum obtained a polynomial improvement over [25] to \(\tilde{O}(n^{3/8})\) colors [7] when the input graph is 3-colorable. This was improved to _O(n_<sup>1/4</sup>) using semi-definite programming methods by Karger, Motwani, and Sudan [18]. A long line of subsequent work culminated in the the development of an algorithm using _O(n_<sup>0.19996</sup>) colors [20], very recently improved to _O(n_<sup>0.19747</sup>) [21]. On the hardness of approximation side, it is known to be NP-hard to color a 3-colorable graph using 4 colors [22, 16, 10], and until recently, no better lower bound was known. Barto et al. recently showed that it is NP-hard to color an _r_-colorable graph using 2_r_-1 colors; in particular, it is NP-hard to 5-color

<sup>∗</sup>Simons Institute for the Theory of Computing and the Dept. of EECS, Univ. of California, Berkeley, Berkeley, CA 94720. `venkatg@berkeley.edu`. Research supported in part by a Simons Investigator award and NSF grant CCF-2211972. <sup>†</sup>Dept. of Computer Science, Univ. of Illinois, Urbana-Champaign, Urbana, IL 61801. `rheaj3@illinois.edu`.

