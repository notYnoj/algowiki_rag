Fast Sparse \(\alpha\)-Navigable Graph Construction with Improved Resource Augmentation

**Abstract**

Graph-based nearest neighbor search methods have surged in popularity in recent years. These methods are based on running greedy search on a directed graph constructed over a set of _n_ points, _x_<sub>1</sub>_,...,x<sub>n</sub>_, endowed with some distance function. A common goal is to construct a search graph that has the \(\alpha\)-_navigability_ property, which ensures that greedy search returns provably good approximate nearest neighbors and converges in a small number of iterations. As the parameter \(\alpha\ge 1\) increases, accuracy improves, as does convergence rate, but there is a tradeoff: higher values of \(\alpha\) require the graph to have more edges, which increases both the data structure’s space and search time. This tradeoff has motivated the study of algorithms for constructing a _sparsest_ \(\alpha\)-_navigable graph_ for a given set of points.

In this work, we present improved algorithms for constructing \(\alpha\)-navigable graphs. For any point set and any distance function, we show how to compute an \(\alpha\)-navigable graph _G_ with a number of edges no more than _O_(log_n_) times that of the sparsest \((1+\varepsilon)\alpha\)-navigable graph. The algorithm runs in \(O(n^\omega log(\Delta)/\varepsilon)\) time, where \(\omega<2.372\) is the exponent of fast matrix multiplication and \(\Delta\) is the ratio between the largest and smallest pairwise distances in the input set. This result improves on recent work by Khanna, Padaki, and Waingarten (SODA 2026), who achieve the same runtime, but are only competitive with the sparsest \(2(1+\varepsilon)\alpha\)- navigable graph. Since sparsity often increases rapidly with \(\alpha\) (typically \(\alpha\) is chosen \(\le 1.1\)) such a result can be significantly weaker than our bound. Previously, the best algorithm that could compete with the sparsest \((1+\varepsilon)\alpha\)-navigable graph required _O(n_<sup>2.5</sup>) time. Beyond our main result, we show that our techniques extend to the related problem of constructing sparse \(\tau\)-monotonic graphs, another popular target in nearest neighbor search. Moreover, we provide a fine-grained complexity analysis that suggests that improving the \(O(n^\omega)\) running time in our result is unlikely, or at least would require a very different algorithmic approach. This analysis is based on proving hardness results for problems related to _verifying_ whether a graph is navigable, which is a topic of independent interest.

## 1 Introduction

Nearest neighbor search has been a central problem in computer science for decades [4, 6, 7, 9-11, 23, 27, 29]. Given a dataset _P_={_p_<sub>1</sub>_,...,p<sub>n</sub>_} together with a distance function \(d(\cdot,\cdot)\), the goal is to construct a data structure that can answer (approximate) nearest-neighbor queries: given _q_, return a \(p\in P\) that (approximately) minimizes _d(p,q_). Interest in this problem has recently surged due

<sup>∗</sup>Cornell University (`me@ajhconway.com`, `btl46@cornell.edu`) <sup>†</sup>University of Maryland (`laxman@umd.edu`, `rwen1@umd.edu`) <sup>‡</sup>New York University (`mlf9579@nyu.edu`, `cmusco@nyu.edu`, `ys6378@nyu.edu`, `torsten.suel@nyu.edu`)

Alex Conway<sup>∗</sup> Laxman Dhulipala<sup>†</sup> Martin Farach-Colton<sup>‡</sup> Ben Landrum<sup>∗</sup> Christopher Musco<sup>‡</sup> Yarin Shechter<sup>‡</sup> Torsten Suel<sup>‡</sup> Richard Wen<sup>†</sup>

arXiv:2610.38205v1 [cs.DS] 28 Oct 2026

