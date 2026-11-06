# COUNTING RANDOM _k_-SAT NEAR THE SATISFIABILITY THRESHOLD

ZONGCHEN CHEN, ADITYA LONKAR, CHUNYANG WANG, KUAN YANG, YITONG YIN

Abstract. We present efficient counting and sampling algorithms for random _k_-SAT when the clause density satisfies \(\alpha\le\frac{2^k}{poly(k)}\). In particular, the exponential term 2_<sup>k</sup>_ matches the satisfiability threshold \(\Theta(2^k)\) for the existence of a solution and the (conjectured) algorithmic threshold 2_<sup>k</sup>_(ln_k)/k_ for efficiently finding a solution. Previously, the best-known counting and sampling algorithms required far more restricted densities \(\alpha\lesssim 2^{k/3}\) [HWY23]. Notably, our result goes beyond the lower bound \(d\unknown 2^{k/2}\) for worst-case _k_-SAT with bounded-degree _d_ [BGG<sup>+</sup>19], showing that for counting and sampling, the average-case random _k_-SAT model is computationally much easier than the worst-case model.

At the heart of our approach is a new refined analysis of the recent novel coupling procedure by [WY24], utilizing the structural properties of random constraint satisfaction problems (CSPs). Crucially, our analysis avoids reliance on the 2-tree structure used in prior works, which cannot extend beyond the worst-case threshold 2<sup>_k/_2</sup>. Instead, we employ a witness tree similar to that used in the analysis of the Moser-Tardos algorithm [MT10] for the Lovász Local lemma, which may be of independent interest. Our new analysis provides a universal framework for efficient counting and sampling for random atomic CSPs, including, for example, random hypergraph colorings. At the same time, it immediately implies as corollaries several structural and probabilistic properties of random CSPs that have been widely studied but rarely justified, including replica symmetry and non-reconstruction.

### Contents

1. Introduction 1<tbc>

2. Preliminaries 7<tbc>

3. Structural properties of random hypergraphs 9<tbc>

4. Recursive coupling of random CSPs 12<tbc>

5. Linear program for counting and sampling 19<tbc>

References 30<tbc>

Appendix A. Proofs of structural properties 33

### 1. Introduction

Random constraint satisfaction problems (CSPs) have attracted lots of attention in both computer science and statistical physics in recent years. Typically, a random CSP consists of a set of \(m=\alpha n\) constraints imposed on _n_ variables with finite domains, where the constraints are randomly generated according to a specific rule and \(\alpha>0\) is a constant representing the density of the instance. The primary goal is to find a feasible solution satisfying all constraints or more generally, optimize a random objective function specified by the constraints. Usually, with sufficiently small \(\alpha\), the problem is easy and can be solved in polynomial time, while as \(\alpha\) grows, the problem becomes computationally hard at a certain point. It is, thus, important to understand the computational complexity of random CSPs with respect to the density \(\alpha\).

(Zongchen Chen, Aditya Lonkar) School of Computer Science, Georgia Institute of Technology, Atlanta, GA, USA. Email: `chenzongchen@gatech.edu`, `alonkar9@gatech.edu`. (Chunyang Wang, Yitong Yin) State Key Laboratory for Novel Software Technology, New Cornerstone Science Laboratory, Nanjing University, 163 Xianlin Avenue, Nanjing, Jiangsu Province, 210023, China. Email: `wcysai@smail.nju.edu.cn`, `yinyt@nju.edu.cn`. (Kuan Yang) John Hopcroft Center for Computer Science, Shanghai Jiao Tong University, Shanghai, China. Email: `kuan.yang@sjtu.edu.cn`. The research of K. Yang is supported by the NSFC grant No. 62102253.

