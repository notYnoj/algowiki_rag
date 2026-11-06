# Asteroidal Triples and Friendsin (Likely Necessary) Matrix Multiplication Time

**Abstract**

In a seminal paper, Kratsch and Spinrad [SODA 2003 and SIAM Journal on Computing 2006] studied several important problems in structural graph theory that anticipated two trends in fine-grained complexity, both from the upper- and lower-bound side:

From the upper-bound side, for each of these problems the authors give an _intermediate_ running time strictly _between_ \(n^\omega\) _and n_<sup>3</sup>, where \(\omega<2.371177\) is the matrix multiplication exponent. When optimized, this running time can be made \(\tilde{\mathcal{O}}(n^{(3+\omega)/2})\). By now, many more problems can be solved in this running time: directed unweighted or node-weighted APSP, a variety of matrix products such as max-min and dominance, RNA Folding and many more. For some of these, the community has also developed tools suggesting that this intermediate running time is necessary.

From the lower-bound side, the authors give lower bounds of \(n^{\omega-o(1)}\), conditioned on three natural hardness hypotheses on the complexity of quantified variants of triangle detection that account for different types of hardness of such problems.

Despite this, it has remained open for over 20 years which of these two pieces of evidence reflects the truth for the problems that Kratsch and Spinrad study: whether the intermediate running time is indeed necessary and stronger lower bounds hold, or whether the hardness evidence of Kratsch and Spinrad is essentially tight. In this paper, we resolve this question and show that the latter is the case: all problems admit an \(\tilde{\mathcal{O}}(n^\omega)\) time algorithm.

As an additional contribution, we make partial algorithmic progress on further problems in structural graph theory of intermediate complexity, improving over previous work [Chiu and Lu, STACS 2022 and Information and Computation 2024][Spinrad, Discrete Applied Math 2004].

Funding _Jakob Nogler_: Supported by the Akamai Presidential Fellowship and by a fellowship from the Siebel Scholars Foundation; _Agnès Totschnig_: Supported by a MathWorks Fellowship; _Virginia Vassileoska Williams_: Supported by NSF Grant CCF-2330048, BSF Grant 2024233 and a Simons Investigator Award

### 1 Introduction

Many problems in graph and matrix algorithms have natural cubic running times in terms of _n_, the number of nodes in the graph or the number of rows/columns of the matrices. For some perhaps infamous examples, such as All-Pairs Shortest Paths (APSP) in weighted graphs, this cubic running time has persisted for many decades, except for _n_<sup>_o_(1)</sup> improvements, leading to conjectures that cubic time is the best possible (e.g.,[Vas18, WW10, VW18]). For other problems, substantial polynomial improvements have been obtained. The prime example for this is matrix multiplication. The exponent \(\omega\) is defined as the smallest real value for which \(n\times n\) matrices can be multiplied in \(\mathcal{O}(n^{\omega+\varepsilon})\) time for all \(\varepsilon>0\). It has been known since 1969 that \(\omega<3\) [Str69], and while the popular belief among computer scientists is that \(\omega=2\), the best known upper bound is \(\omega<2.371177\) [DEK<sup>+</sup>26].

Via reductions to matrix multiplication, a huge variety of problems have truly subcubic<sup>1</sup> time algorithms: many linear algebraic operations (matrix inverse, linear system solving, LUP decompositions and more), a variety of “funny” matrix products over other algebraic structures such as the max-min product of matrices [VWY09], many graph problems in unweighted graphs such as unweighted APSP [Zwi02, Sei95], structure similarity problems such as RNA-Folding [BGSV19], and many more.

<sup>1</sup> \(O(n^{3-\varepsilon})\) time for constant \(\varepsilon>0\).

**Jakob Nogler** <sup>1</sup> Massachusetts Institute of Technology Cambridge, United States

**Agnès Totschnig** <sup>1</sup> Massachusetts Institute of Technology Cambridge, United States

**Virginia Vassilevska Williams** <sup>1</sup> Massachusetts Institute of Technology Cambridge, United States

