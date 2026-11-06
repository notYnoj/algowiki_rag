# Combinatorial Optimization using Comparison Oracles

**Abstract**

In a linear combinatorial optimization problem, we are given a family \(\mathcal{F}\subseteq 2^U\) of _feasible subsets_ of a ground set _U_ of _n_ elements, and our goal is to find \(S^*=argmin_{S\in\mathcal{F}}\langle w,1_S\rangle\). Traditionally, we are either given the weight vector up-front, or else we are given a _value oracle_ which allows us to evaluate \(w(S):=\langle w,1_S\rangle\) for any \(S\in\mathcal{F}\). Motivated by recent practical interest in solving problems via pairwise comparisons, and also by the intrinsic theoretical quest to understand fundamental computational models, we consider the weaker and more robust _comparison oracle_, which for any two feasible sets \(S,T\in\mathcal{F}\), reveals only if _w(S_) is less than/equal to/greater than _w(T_). We ask:

When can we find the optimal feasible set \(S^*=argmin_{S\in\mathcal{F}}w(S)\) using a small number of comparison queries? If so, when can we do this efficiently?

We present three main contributions:

1. Our first main result is a surprisingly general answer to the query complexity. We establish that the query complexity for the above problem over any arbitrary set system \(\mathcal{F}\subseteq 2^U\) is \(\widetilde{O}(n^2)\). This result leverages the inference dimension framework, and demonstrates a fundamental separation between information complexity and computational complexity, as the runtime may still be exponential for NP-hard problems (assuming the Exponential Time Hypothesis).

2. Having resolved the query complexity, we turn to the algorithmic question. We develop two general algorithmic frameworks:

(a) **Optimization from Certification:** We present a novel Dual Ellipsoid framework that establishes an efficient reduction from optimization to certification. This framework demonstrates that to optimize efficiently, it is sufficient to design an efficient certification for the optimality of a candidate set _S_<sup>∗</sup> with the knowledge of _w_<sup>∗</sup> using only comparisons between feasible sets. Moreover, this framework also yields a deterministic low query complexity algorithm.

(b) **Global Subspace Learning (GSL):** Tailored for integer objective functions bounded by _B_, we sort all feasible sets using only _O(nB_log(_nB_)) queries, improving upon the \(\widetilde{O}(n^2)\) bound when _B=o(n_). We efficiently implement this framework for linear matroids via algebraic techniques, yielding efficient algorithms with improved query complexity for problems like _k_-SUM, SUBSET-SUM, and _A+B_ sorting.

3. Our third set of results gives the first polynomial-time, low-query algorithms for several classic combinatorial problems. We develop such algorithms for finding minimum cuts in simple graphs, minimum weight spanning trees (and matroid bases in general), bipartite matching (and matroid intersection), and shortest _s-t_ paths.

Our work provides the first general query complexity bounds and efficient algorithmic results for this fundamental model.

<sup>∗</sup>Google Research. Emails: `{vcohenad,gurug,renatoppl,jschnei}@google.com` †Bocconi University. Email: `tommasodorsi@gmail.com` ‡New York University. Emails: `{anupam.g,madhusudhan.p}@nyu.edu` §University of Michigan. Email: `euiwoong@umich.edu` ¶Duke University. Email: `debmalya@cs.duke.edu` <sup>†</sup>Carnegie Mellon University. Email: `dwoodruf@andrew.cmu.edu`

Vincent Cohen-Addad<sup>∗</sup> Tommaso d’Orsi<sup>†</sup> Anupam Gupta<sup>‡</sup> Guru Guruganesh<sup>∗</sup> Euiwoong Lee<sup>§</sup> Renato Paes Leme<sup>∗</sup> Debmalya Panigrahi<sup>¶</sup> Madhusudhan Reddy Pittu<sup>‡</sup> Jon Schneider<sup>∗</sup> David P. Woodruff<sup>‖</sup>

