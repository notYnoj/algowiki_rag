<tbc>and GLWS) as proofs-of-concept to show that our new techniques and algorithms remain practical due to work efficiency, which is also the main motivation of our paper. We release our code at [35], which gives more details of our experiments.

**_Parallel LCS._** While as one of the classic algorithmic problem, LCS is widely studied in parallel, the existing parallel implementations we know of [6, 11, 26, 76, 87, 89, 94] do not take advantage of the sparsification. Most of them parallelizes the \(\Theta(nm)\) algorithm for two strings with sizes _n_ and _m_, and the experimental studies in these papers focus on input sizes up to 10<sup>5</sup>. They cannot process much larger instances in as the (sequential) sparse LCS algorithms (e.g., [7]) as discussed in Sec. 3. Hence, in our experiments, our baseline is our implementation of the sparse LCS in [7], which can process our input instances with large size (10<sup>8</sup>) and small number of effective edges _L_ (number of pairs (_i,j_) such that _A[i_]=_B[j_]).

We test two random strings _A_[1_..n_] and _B_[1_..n_] with length _n_=10<sup>8</sup>, while controlling _L_ and _k_ (the LCS length). The pre-processing time to find all matching pairs is not counted into the running time. Fig. 6 shows the results when _L_=10<sup>8</sup> and _L_=10<sup>9</sup>.

Overall, our algorithm has up to \(30\times\) speed up than the sequential version. Since the span of the algorithm is proportional to the LCS length _k_, the running time increases when _k_ increases. For _L_=10<sup>8</sup>, the parallel running time stays competitive to the sequential running time until the extreme case _k_=10<sup>8</sup> (i.e., the two sequences are exactly the same). Since our algorithm has _O(L_log_n_) work and _O(k_log_n_) span, there is no parallelism when _L=k_=10<sup>8</sup>. For _L_=10<sup>9</sup>, where the total work is larger, our parallel algorithm is always faster than the sequential algorithm regardless of the value of _k_, and always achieves good parallelism.

**_Parallel GLWS._** For GLWS, we use the setting of the post-office problem described in Sec. 4. We compare our parallel algorithm with the sequential solution in Sec. 4.1, as well as our own algorithm running on one core. We generate random data for _n_=10<sup>8</sup> and 10<sup>9</sup>, and use different weight functions to control the output size _k_, which is the number of post offices in the solution. Fig. 7 shows the result on different _n_ and _k_. The time for sequential algorithm does not change significantly, because it has _O(n_log_n_) work, which is independent of _k_. For our algorithm, the running time varies with _k_ due to the _O(k_log<sup>2</sup>_n_) span. When _k_ is small, our algorithm is \(20\times\) faster than the sequential algorithm and achieves \(30-40\times\) self-relative speedup. Our parallel algorithm is faster than the sequential algorithm for _k\<_10<sup>4</sup> when _n_=10<sup>8</sup>, and is faster than the sequential algorithm until _k_≈10<sup>5</sup> when _n_=10<sup>9</sup>.

## 7 CONCLUSION AND FUTURE WORK

We systematically studied general approaches to parallelize classic sequential dynamic programming algorithms, particularly those with non-trivial optimizations such as decision monotonicity and sparsification. We showed a novel framework, the Cordon Algorithm, and apply it to different DP recurrences. Theoretically, we gave the concept of optimal parallelism and perfect parallelism of a sequential algorithm, and showed that with a careful design, we can achieve optimal parallelism for the classic sequential DP algorithms in a (nearly) work-efficient manner, and perfect parallelism for some instances. Practically, we show that our carefully-designed<tbc>

<tbc>techniques do not include much overhead, and can outperform the original sequential version in a wide variety of cases.

We believe that the techniques in this paper opens a list of interesting questions. First, many of the new parallel algorithms are nearly work-efficient--we pick the most practical sequential algorithms for each problem, but they can be off the best work bound by up to an _O_(log_n_) factor. It is theoretically interesting to ask if we can match the best work bound in parallel. Second, among all these classic algorithms we looked at, one problem/algorithm that cannot be directly solved by the Cordon Algorithm is the RNA Secondary Structure [38]. Here, we may have 2_<sup>n</sup>_ different paths in a DP DAG, so applying Cordon Algorithm efficiently may need some complicated techniques. Finally, we show how to faithfully parallelize the sequential DP algorithms. We are aware of other approaches [6, 24, 68, 76, 87, 94] for LIS/LCS that can achieve stronger worst-case span bounds using divide-and-conquer. Hence, an interesting direction is to see if we can redesign other DP algorithms in a similar form to achieve better worst-case span.

## ACKNOWLEDGEMENT

This work is supported by NSF grants CCF-2103483, IIS-2227669, NSF CAREER Awards CCF-2238358 and CCF-2339310, the UCR Regents Faculty Development Award, and the Google Research Scholar Program.

## REFERENCES

L = 108
L = 109
101
102
Running Time (seconds)
Ours
Ours (1 thread)
100
101
102
105
108
102
105
108
k = LCS length
k = LCS length

n = 108
n = 109
102
103
101
102
Running Time (seconds)
Ours
Ours (1 thread) Sequential
100
101
101
103
105
101
103
105
k = # of post offices
k = # of post offices

**Figure 6:** Running time of our parallel LCS algorithm (in Sec. 3).

**Figure 7:** Running time of our parallel convex-GLWS algorithm (Alg. 1).

