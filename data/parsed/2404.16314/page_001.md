# Parallel and (Nearly) Work-Efficient Dynamic Programming

### ABSTRACT

The idea of dynamic programming (DP), proposed by Bellman in the 1950s, is one of the most important algorithmic techniques. However, in parallel, many fundamental and sequentially simple problems become more challenging, and open to a (nearly) work- efficient solution (i.e., the work is off by at most a polylogarithmic factor over the best sequential solution). In fact, sequential DP algorithms employ many advanced optimizations such as decision monotonicity or special data structures, and achieve better work than straightforward solutions. Many such optimizations are inherently sequential, which creates extra challenges for a parallel algorithm to achieve the same work bound.

The goal of this paper is to achieve (nearly) work-efficient parallel DP algorithms by parallelizing classic, highly-optimized and practical sequential algorithms. We show a general framework called the _Cordon Algorithm_ for parallel DP algorithms, and use it to solve several classic problems. Our selection of problems includes Longest Increasing Subsequence (LIS), sparse Longest Common Subsequence (LCS), convex/concave generalized Least Weight Sub- sequence (LWS), Optimal Alphabetic Tree (OAT), and more. We show how the Cordon Algorithm can be used to achieve the same level of optimization as the sequential algorithms, and achieve good parallelism. Many of our algorithms are conceptually simple, and we show some experimental results as proofs-of-concept.

### CCS CONCEPTS

• Theory of computation \(\rightarrow\) Parallel algorithms.

### KEYWORDS

Parallel Algorithms, Dynamic Programming, Longest Increasing Subsequence, Longest Common Subsequence, Least Weighted Sum, Optimal Alphabetic Tree, Decision Monotonicity

### 1 INTRODUCTION

The idea of dynamic programming (DP), since proposed by Richard Bellman in the 1950s [13], has been extensively used in algorithm design, and is one of the most important algorithmic techniques. It is covered in classic textbooks and basic algorithm classes, and is widely used in research and industry. The goal of this paper is to achieve **(nearly) work-efficient** (defined below) and **parallel** DP algorithms based on parallelizing classic, highly-optimized and practical sequential algorithms.

At a high level, a DP algorithm computes the **DP values** for a set of **states** (labeled by integers) by a **recurrence**. The recurrence specifies a set of **transitions** from state _j_ to state _i_, i.e., how _D[j_] can be used to compute _D[i_]<sup>1</sup>. We call _j_ a **decision** at _i_. _D[i_] is then computed by taking the best (minimum or maximum) among

all decisions, which we call the **best decision** at _i_. Throughout the paper, we will use _i_<sup>∗</sup> to denote the best decision of state _i_. We introduce more concepts about DP in Sec. 2.

One can view the states and transitions as a directed acyclic graph (DAG), which we refer to as a **DP DAG**. In this DAG, each vertex is a state, and an edge _j_ to _i_ denotes a transition from _j_ to _i_. Since such an edge indicates that computing _D[i_] logically requires _D[j_], we also call it a **dependency**, and say _i_ **depends on** _j_. Sequentially, we can compute all states based on a topological ordering. For simplicity, we always assume that the (integer) order of the states is a valid topological ordering.

Unfortunately, many DP algorithms (even some simple ones sequentially) are hard to parallelize, and are especially hard to achieve work-efficiency (the work asymptotically matches the best sequential algorithm) or even near work-efficiency (off by a polylogarithmic factor). We note that on today’s multicore machines with tens to hundreds of processors, achieving low work is one of the most crucial objectives for designing _practical_ parallel algorithms. One particularly intriguing and somewhat ironic challenge for achieving work-efficient parallel DP algorithms is that, sequential algorithms are extremely well-optimized. In many cases, an optimized DP algorithm does not need to process all edges (transitions) in the DP DAG; some even do not need to process all vertices (states). We review the literature at the end of this section. In fact, almost all textbook DP solutions can be optimized to achieve lower work than the straightforward solution that directly computes the DP values of all states based on the recurrence. Such examples include longest increasing subsequence (LIS), (sparse) longest common subsequence (LCS), (convex/concave) least weight subsequence (LWS), and many others discussed in this paper.

One typical DP optimization that is both theoretically elegant and practically useful is **decision monotonicity (DM)**. At a high level, DM indicates that two states _i_ and _j\>i_ must have their best decisions \(j^*\ge i^*\), called the _convex_ case<sup>2</sup>, or the _concave_ case where either \(j^*≤i^*\) or \(j^*\ge i\) (see Fig. 1). Hence, when finding the best decision for state _j_, one can narrow down the possible range of _j_<sup>∗</sup> based on the known best decisions of previous states, and thus avoid processing all transitions. DM has been widely studied in the sequential setting (e.g., [37, 41, 43, 44, 62, 62, 63]), and is also closely related to concepts such as quadrangle inequalities [96, 97] and Monge property [78]. Sequentially, using DM saves a polynomial factor than the naïve DP algorithm in many applications [1, 2, 18, 42, 66, 77, 93]. In the parallel setting, however, among the papers we know of [23, 25, 31, 45, 54, 69, 80], most from the 90s, very few of them take advantage of DM to reduce work. Indeed, none of them are work-efficient, and most of them have a polynomial overhead, which limits their potential applicability on today’s multicore machines. The only nearly work-efficient results [23, 25] focus on the concave case of one specific problem.

<sup>1</sup>More generally, a transition may compute _D[i_] from multiple other states. All algorithms in this paper only requires one state _j_ in the transition to compute _D[i_]. <sup>2</sup>The definitions of convexity and concavity are interchanged in some other papers.

Xiangyun Ding<br> University of California, Riverside<br> xding047@ucr.edu

Yan Gu<br> University of California, Riverside<br> ygu@cs.ucr.edu

Yihan Sun<br> University of California, Riverside<br> yihans@cs.ucr.edu

