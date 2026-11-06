<tbc>During a DP algorithm, we may maintain the DP value of a state and update it by the recurrence. We call the process of updating _D_\[_i_\] by _D_\[_j_\] a **_relaxation_**, or say _j **relaxes** i_. A relaxation is successful if the DP value is updated to a **_better_** value, i.e., a lower (higher) value if the objective is minimum (maximum). We call the actual DP value of a state the **_true_** or **_finalized_** DP value to distinguish from the DP value being updated during the algorithm, which we call the **_tentative_** DP value. We say a state _i_ is finalized if we can ensure that its true DP value has been computed, and tentative otherwise. Among all tentative states, we say a state is **_ready_**, if all its decisions are finalized, and **_unready_** otherwise. A naïve DP algorithm will process all transitions and states based on a topological ordering.

**_DP Optimizations._** Instead of computing the recurrence straightforwardly, many algorithms can optimize the computation by skipping vertices and/or edges in the DAG to save work. We call such algorithms **_optimized DP algorithms_**. For example, given an input sequence _A_\[1_..n_\], the optimized LIS algorithm \[65\] maintains a data structure to precisely find the best decision of each state in _O_(log_n_) cost, and only processes _O(n_) transitions instead of _O(n_<sup>2</sup>) as suggested by the recurrence. Similarly, given two input sequences _A_\[1_..n_\] and _B_\[1_..m_\], the optimized LCS algorithm only needs to process all states _D_\[_i,j_\] where _A_\[_i_\]=_B_\[_j_\], instead of _O(nm_) states in the recurrence. Another typical optimization is decision monotonicity where the best decisions of previous states can narrow down the range for best decisions for later states, which skips transitions and saves work. Typical examples include concave/convex generalized LWS (see Sec. 4), OAT (see Sec. 5.1), GAP (see Sec. 5.2), etc. We will discuss all these algorithms in this paper.

## 2.2 Parallelizing Sequential DP Algorithms

We now discuss our goal to parallelize a sequential DP algorithm. Our primary goal is to achieve (asymptotically) the same computation as an optimized sequential algorithm. More formally, for a sequential algorithm \(\Gamma\) computing a recurrence _R_ with certain optimizations, we define the \(\Gamma\)**-_optimized DAG_**, denoted as \(G_\Gamma=(V_\Gamma,E_\Gamma)\), as follows. \(G_\Gamma\) is the same as the DP DAG on _R_ with some edges highlighted: for all edges that are processed by \(\Gamma\), we highlight them in \(G_\Gamma\), and call them the **_effective edges_**. We call the other edges _normal edges_. These effective edges can be used to fully complete the computation. For a sequential DP algorithm \(\Gamma\), we hope its faithful and best possible parallelization \(\Lambda\) to:

\(\bullet\) process the same effective edges in \(G_\Gamma\) and achieve the same work as \(\Gamma\), and<tbc>

\(\bullet\) have span proportional to the **_effective depth_** of \(G_\Gamma\), defined as the largest number of effective edges in any path in \(G_\Gamma\).

Namely, if our goal is to parallelize \(\Gamma\) and perform the same computation, the parallel algorithm \(\Lambda\) has to process all edges \(j\rightarrow i\) processed by \(\Gamma\). This means _i_ can be finalized only after j is finalized, so the span is related to the effective depth as defined above. We use \(\hat{E}_\Gamma\) to denote the set of effective edges, and \(\hat{d}(G_\Gamma)\) as the effective depth of \(G_\Gamma\). More formally, we define the following concepts.

We say a parallel algorithm \(\Lambda\) is an **_optimal parallelization_** of a sequential DP algorithm \(\Gamma\), if 1) the set of edges processed in \(\Lambda\) and \(\Gamma\) satisfies \(\hat{E}_\Gamma\subseteq\hat{E}_\Lambda\) and \(|\hat{E}_\Lambda|=O(|\hat{E}_\Gamma|)\), 2) the work of the two algorithms are asymptotically the same, and 3) the span of \(\Lambda\) is \(\tilde{O}(\hat{d}(G_\Gamma))\). Namely, \(\Lambda\) can process a superset of edges of that in \(\Gamma\),<tbc>

<tbc>but not asymptotically more, and its span is proportional to the effective depth of the \(\Gamma\)-optimized DAG.

In addition, we define the **_perfect parallelization_**. In an omniscient version of \(\Gamma\), we only need to process the best decisions based on their dependencies. We define the \(\Gamma\)**-_perfect DAG_**, denoted as \(G_\Gamma^*\), as subgraph of \(G_\Gamma\) that only contains the best decision edges (both effective and normal edges). We say an optimal parallelization \(\Lambda\) of \(\Gamma\) is also a _perfect parallelization_ if the span of \(\Lambda\) is \(\tilde{O}(\hat{d}(G_\Gamma^*))\).

While the definitions seem abstract, we will later show that they are intuitive for concrete problems. For example, in longest common subsequence (LCS), both \(\hat{d}(G_\Gamma)\) and \(\hat{d}(G_\Gamma^*)\) are the output LCS length _k_ (but for other algorithms they can be different), and our goal is to achieve \(\tilde{O}(k)\) span for a perfect parallelization.

Note that the "perfect parallelization" of a sequential algorithm does not directly suggest optimality in work or span bounds for the same _problem_. One can possibly achieve better bounds by redesigning the recurrence and/or sequential algorithm with fewer edges or a shallower depth. Instead of finding or redesigning a different DAG to obtain new optimizations, our focus is to provide parallelization of existing sequential algorithms with optimizations.

In the following, we first present our new algorithmic framework: the Cordon Algorithm, which provides a correct, although not necessarily efficient parallelization for general DP algorithms. On top of it, for each specific problem, we will show how to achieve low work, which, as discussed in Sec. 4 and 5, can be highly non-trivial.

## 2.3 Our Framework: the Cordon Algorithm

Our idea is based on the _phase-parallel_ framework \[81\] (see below) adapted to DP algorithms. The phase-parallel framework by Shen et al. aims to identify (as many as possible) operations that do not depend on each other, and process them in parallel. Directly applying this framework to DP algorithms will give the following algorithm outline:

**Phase-Parallel Framework for DP algorithms**

While there exist any tentative states:

\(\bullet\) Find the set of ready states as F<tbc>

\(\bullet\) Process all states in F in parallel and mark all of them as finalized

We call each iteration of the while-loop a **_round_**. We call the set of states being processed in round _i_ the **_frontier_** of round _i_, denoted as F_<sub>i</sub>_. While the phase-parallel framework gives a high- level approach in achieving parallelism, it does not indicate how to do so (i.e., how to identify the ready states in each round).

We now introduce our Cordon Algorithm, which uses a novel approach to identify the frontier F_<sub>i</sub>_ in each round, particularly for a DP computation \(G_\Gamma\). The Cordon Algorithm identifies the unready tentative states and put **_sentinels_** on them; then it uses all sentinels to outline a **_cordon_** to mark the boundary of the frontier. We summarize the algorithm in the following steps. Note that every step can be processed in parallel.

**Step 1** Mark all states as tentative and initialize them by the boundary condition.

**Step 2** If a tentative state _j_ can successfully relax another tentative state _i_ (i.e., update _D_\[_i_\] to a better value), put a sentinel on state _i_. Such a sentinel means that all the descendants (inclusive)<tbc>

