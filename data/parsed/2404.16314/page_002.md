The challenge of using DM in parallel lies in two aspects. First, sequentially we skip the transitions for state _i_ by observing the best decisions of all states before _i_. When multiple states are processed in parallel, they cannot see each other’s best decision, making it hard to skip the same set of "useless" transitions as in the sequential setting. Second, many classic sequential DP algorithms with DM relies on efficient data structures such as monotonic queues, which are inherently sequential. Achieving the same work bound in parallel also requires careful redesign of the underlying data structures.

In this paper, we study parallel DP algorithms to achieve the same work as highly-optimized sequential algorithms. Given a sequential algorithm \(\Gamma\) with certain optimizations, our goal for work-efficiency is to process (asymptotically) the same number of transitions and states as in \(\Gamma\). Regarding parallelism, we hope to achieve the best possible parallelism indicated by the transitions processed by \(\Gamma\). We formalize our goals in Sec. 2.3. Our solution is based on an algorithmic framework that generally applies to almost _all_ DP algorithms. We call this framework the **_Cordon Algorithm_**. At a high level, our framework specifies how to _correctly_ identify a subset of states that do not depend on each other and process them in parallel. We then present how to do so _efficiently_ for specific problems. To achieve work-efficiency, our key ideas are two-fold. First, many of our algorithms use _prefix-doubling_ to bound the additional work on processing unnecessary states. Second, we design _new parallel data structures_ to skip unnecessary transitions.

This paper studies general approaches for parallel DP, with a special focus on applying the non-trivial, effective optimizations found in the sequential context to parallel algorithms. We select classic DP problems and their optimized sequential solutions, and parallelize them using novel techniques. Our framework unifies one existing parallel LIS algorithm [47], and provides new parallel algorithms for various problems such as sparse LCS, convex/concave generalized LWS and GAP edit distance (GAP), and optimal alphabetic tree (OAT). All the algorithms are (nearly) work-efficient with non- trivial parallelism. Among them, we highlight our contributions on parallelizing the DP algorithms with decision monotonicity. The core of our idea is a parallel algorithm for convex/concave generalized LWS. We apply it to other problems such as GAP and OAT, and achieve new theoretical results. For OAT, we partially solve the open problem in [72] by providing a work-efficient algorithm with polylogarithmic span when the inputs are positive integers with word size _n_polylog(_n_). We present our theoretical results in Thm. 3.1, 3.2, 4.1, 4.2, 5.1 and 5.2. We believe this is the first paper that achieves near work-efficiency in parallel for a class of DP algorithms with DM.

Although the main focus of this paper is to achieve low work in theory, an additional goal is to make the algorithms simple and practical. We implement two algorithms as proofs-of-concept (code<tbc>

<tbc>available at [35]). On 10<sup>9</sup> input size, both of them outperform sequential solutions when the depth of the DP DAG is within 10<sup>5</sup>, and achieve 20-30\(\times\) speedup with smaller depth of the DP DAG.

**_Related Work_**. Dynamic programming (DP) is one of the most studied topics in algorithm design. The seminal survey [44] by Galil and Park reviewed two types of optimization techniques sequentially, including decision monotonicity (e.g., [37, 41, 43, 44, 62, 62, 63, 93]) and sparsity (e.g., [39, 40, 51, 56]). This paper mainly focuses on parallelizing the sequential algorithms in this scope, and we will review the literature of each problem in the corresponding section.

DP is also widely studied in parallel. There exists rich literature on optimizing various goals in different models, such as span (time) in PRAM (e.g. [6, 9, 11, 45, 54, 69, 70, 72, 73, 76, 80]), I/O cost in the external-memory/ideal-cache model (e.g., [27-30, 59, 86]), rounds in the MPC model [12, 22, 50, 57], or on the BSP model [5, 67, 68]. However, these papers either only considered the DP algorithms without the optimizations, or incur polynomial work overhead, except for [23, 25] for one specific problem. Instead, our paper tries to parallelize the efficient and practical sequential algorithms while maintaining low work. Some other works try to parallelize certain types of DP algorithms or applications using DP (e.g., [3, 10, 20, 34, 60, 75, 92]). Alternately, our work aims to provide a general approach to parallelize almost all DP algorithms.

## 2 MODEL AND FRAMEWORK

We use the **_work-span model_** in the classic multithreaded model with **_binary-forking_** [8, 17, 21]. We assume a set of threads that share the memory. Each thread acts like a sequential RAM plus a fork instruction that forks two threads running in parallel. When both threads finish, the original thread continues. A parallel-for is simulated by forks in a logarithmic number of steps. A computation can be viewed as a DAG. The **_work W_** of a parallel algorithm is the total number of operations, and the **_span (depth) S_** is the longest path in the DAG. In practice, we can execute the computation with work _W_ and span _S_ using a randomized work-stealing scheduler [21, 48] in time _W/P+O(S_) with _P_ processors with high probability. A parallel algorithm is **_work-efficient_**, if its work is _O(W_), where _W_ is the work of the best known or the corresponding sequential algorithm, and **_nearly work-efficient_** if its work is \(\tilde{O}(W)\). We use \(\tilde{O}(\cdot)\) to hide polylog(_n_) where _n_ is the input size.

### 2.1 Basic Concepts in Dynamic Programming

A DP algorithm solves an optimization problem by breaking it down to subproblems, memoizing the answers to the subproblems, and using them to find the answer to the original problem. The subproblems are usually indexed by integers, referred to as **_states_**. With clear context, we directly use _i_ to refer to "state _i_". The DP value of a state is determined either by a **_boundary_** condition (i.e., initial values), or from other states, specified by a **_DP recurrence_**. This paper studies recurrences in the following form:

\(D[i]=min/maxf_{i,j}(D[j])\) (1)

where _j_ is a decision at _i_. Function \(f_{i,j}(\cdot)\) indicates how the DP value of state _j_ can be used to update state _i_. The transitions (i.e., dependencies) among states form a DAG _G=(V,E_) as introduced in Sec. 1. We use \(j\rightarrow i\) to denote an edge from _j_ to _i_ in the DAG, and use _best[i_] to denote the best decision of state _i_.

i*
j*
i
j
j*
i*
i
j*
j
(a): Convex Case
(b): Concave Case
Figure 1: Convex and concave decision monotonicity. (a). Convexity: for two states i,j, their best decisions satisfy i*
j*. (b). Concavity: for two states i,j, their best decisions satisfy either j*
i* or j*
i*
i*
j*
(a): Convex Case
(b): Concave Case

**Figure 1:** Convex and concave decision monotonicity. (a). Convexity: for two states _i\<j_, their best decisions satisfy \(i^*\le j^*\). (b). Concavity: for two states _i\<j_, their best decisions satisfy either \(j^*\le i^*\) or \(j^*\ge i\).

