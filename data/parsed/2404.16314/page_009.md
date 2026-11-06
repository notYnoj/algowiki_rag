Theorem 4.1. _Given an input sequence of size n, and the sequential GLWS algorithm_ \(\Gamma_{l_\mathrm{ws}}\) _introduced in Sec. 4.1, let_ \(k=\hat{d}(G_{\Gamma_{l_\mathrm{ws}}}^*)\) _be the effective depth of the_ \(\Gamma_{l_\mathrm{ws}}\)_-perfect DAG. Then the Cordon Algorithm for the_ convex _GLWS has O(n_log_n) work and O(k_log<sup>2</sup>_n_) _span. It is a_ perfect parallelization _of_ \(\Gamma_{l_\mathrm{ws}}\).

More intuitively, _k_ in Thm. 4.1 is also the number of best decisions to make in the final solution: for instance, for the post-office problem, it is the number of post offices in the optimal solution.

Theorem 4.2. _Given an input sequence of size n, and the sequential GLWS algorithm_ \(\Gamma_{l_\mathrm{ws}}\) _introduced in Sec. 4.1, let_ \(k=\hat{d}(G_{\Gamma_{l_\mathrm{ws}}})\) _be the effective depth of the_ \(\Gamma_{l_\mathrm{ws}}\)_-optimized DAG. Then the Cordon Algorithm for the_ concave _GLWS has O(n_log_n_) _work and O(k_log<sup>2</sup>_n_) _span. It is an_ optimal parallelization _of_ \(\Gamma_{l_\mathrm{ws}}\).

We first prove that both algorithms are nearly work-efficient and have _O(n_log_n_) work.

Lemma 4.3. _The Cordon Algorithm for GLWS has O(n_log_n_) _work for both convex and concave case._

_Proof._ Combining Lemma 4.1 and 4.2 (and the discussion in Sec. 4.3), the work for each round is _O(h_log_n_), where _h=cordon-now_-1 is the frontier size. Since the frontier sizes _h_ across all rounds add up to _n_, the entire algorithm has _O(n_log_n_) work. □

We then show that the number of rounds in both convex and concave cases is the effective depth of \(G_{\Gamma_{l_\mathrm{ws}}}\). Recall that the DAG \(G_{\Gamma_{l_\mathrm{ws}}}\) includes normal edges between all states _j_ and _i\<j_, and effective edges between a state _j_ and its best decision. The effective depth \(\hat{d}(G_{\Gamma_{l_\mathrm{ws}}})\) is the largest number of effective edges in any path.

Lemma 4.4. _The Cordon Algorithm for GLWS finishes in k rounds, where k is_ \(\hat{d}(G_{\Gamma_{l_\mathrm{ws}}})\).

_Proof._ Define the effective depth \(\hat{d}(s)\) of a state _s_ as the largest number of effective edges of a path ending at _s_. We will inductively prove that a state _s_ is in the frontier of round _r_ iff. _s_ has effective depth _r_. The base case (boundary cases) holds trivially.

Assume the conclusion is true for _r_-1. We first prove the "if" direction, i.e., if a state _s_ has effective depth _r_, it must be in the frontier of round _r_. This is equivalent to show that there is no sentinel on all states from _now_ to _s_. Assume to the contrary that there is a state \(y\in(now,s]\) with a sentinel, which is put by state \(x\in(now,y]\). This means that _x_ is a better decision for _y_ than all states before _now_, indicating that _y_’s best decision \(y^*\ge now\). Based on the induction hypothesis, the effective depth of _y_<sup>∗</sup> must be larger than _r_-1. Therefore, \(\hat{d}(y)=\hat{d}(y^*)+1>r-1+1=r\), which means that \(\hat{d}(y)\) is at least _r_+1. Based on the recurrence, there is a normal edge from _y_ to _s_, so \(\hat{d}(s)\ge r+1\), leading to a contradiction.

We then prove the "only if" condition, i.e., if a state _s_ is in the frontier of round _r_, it must have effective depth _r_. The induction hypothesis suggests that all states with effective depth smaller than _r_ have been finalized in previous rounds, so we only need to show that \(\hat{d}(s)\) cannot be larger than _r_. Assume to the contrary that \(\hat{d}(s)\ge r+1\). Let the path to _s_ with effective depth \(\hat{d}(s)\) be _x_<sub>1</sub>_,x_<sub>2</sub>_,...,s_. Since the total number of effective edges on this path is at least _r_+1, there must exist an effective edge \(x_i\rightarrow x_{i+1}\) on the path such that \(\hat{d}(x_i)=r\) and \(\hat{d}(x_{i+1})=r+1\). However, based on the induction hypothesis, _x<sub>i</sub>_’s best decision must have been finalized.<tbc>

<tbc>During Line 14, _x_ must get its true DP value, and will find itself able to update _x_<sub>_i_+1</sub>. Therefore, there will be a sentinel on \(x_{i+1}\le s\), and _s_ cannot be identified in the frontier of round _r_. □

We will then show that the number of rounds of the convex case is also the effective depth of the \(\Gamma_{l_\mathrm{ws}}\)**_-perfect DAG_** \(G_{\Gamma_{l_\mathrm{ws}}}^*\). This is stronger than the \(\Gamma_{l_\mathrm{ws}}\)-optimized DAG as shown above. Recall that the perfect DAG \(G_{\Gamma_{l_\mathrm{ws}}}^*\) contains all best decision edges in \(G_{\Gamma_{l_\mathrm{ws}}}\).

Lemma 4.5. _The Cordon Algorithm for convex GLWS runs in k_<sup>∗</sup> _rounds, where k_<sup>∗</sup> _is_ \(\hat{d}(G_{\Gamma_{l_\mathrm{ws}}}^*)\).

_Proof._ Define the perfect depth _d_<sup>∗</sup>(_s_) of a state _s_ as the largest number of effective edges of any path ending at _s_ in \(G_{\Gamma_{l_\mathrm{ws}}}^*\). Similarly, we will show by induction that in round _r_, all states with perfect depth _r_ will be processed. The base case holds trivially. Assume the conclusion holds for _r_-1. In round _r_, we will show that a state _s_ with perfect depth _r_ must be put in the frontier. Let _s_<sup>∗</sup> be the best decision of _s_, then _d_<sup>∗</sup>(_s_<sup>∗</sup>)=_r_-1 and therefore _s_<sup>∗</sup>_\<now_. According to DM, any state _x_ between _now_ and _s_ must have its best decisions \(x^*\le s^*<now\), indicating that \(d^*(x^*)\le r-1\). Therefore, _x_ must find its true best decision in _B_, and cannot be updated by any other tentative states in Line 15. This means that there will be no sentinel between _now_ and _s_, so _s_ must be identified ready in round _r_. Therefore, a state with perfect depth _r_ must be finalized in round _r_, leading to the stated theorem. □

Combining Lemma 4.1, 4.2, 4.4 and 4.5 proves the span bounds in Thm. 4.1 and 4.2.

## 5 OTHER PARALLEL DP ALGORITHMS

We now show that our algorithmic framework can be used to parallelize a wide variety of classic sequential DP algorithms. In particular, for the optimal alphabetic tree (OAT) problem (Sec. 5.1), we partially answered a long-standing open problem by Larmore et al. \[72\] for reasonable input instances (for instance, positive integer weights in range _n_polylog(_n_)). For the GAP problem (Sec. 5.2), we showed the first nearly work-efficient algorithm with non-trivial parallelism. More interestingly, this algorithm combines all techniques in the algorithms for convex GLWS and sparse LCS.

### 5.1 Parallel Optimal Alphabetic Trees (OAT)

The optimal alphabetic tree (OAT) problem is a classic problem and has been widely studied both sequentially \[32, 46, 53, 58, 61, 71, 79, 90\] and in parallel \[69, 70, 72, 80\]. Given a sequence of non-negative weights _a_<sub>1_...n_</sub>, the OAT is a binary search tree with _n_ leaves and has the minimum cost, where the cost of a tree _T_ is defined as:

\(cost(T)=\sum_{i=1}^na_id_i\) (7)

Here _d<sub>i</sub>_ is the depth of the _i_-th leaf (from the left) of _T_ (the root has depth 0). One can view the weight _a<sub>i</sub>_ as the frequency of accessing leaf _i_, and the depth of a leaf is the cost of accessing it. Then the cost of _T_ is the total expected cost of accessing all leaves in _T_. The OAT problem is closely related to other important problems such as the optimal binary search tree (OBST) \[64\] and Huffman tree \[55\].

Sequentially, Hu and Tucker \[53\] showed an OAT algorithm with _O(n_log_n_) work. Later, Garsia and Wachs \[46\] simplified this algorithm. In parallel, Larmore et al. \[72\] showed an algorithm based on Garsia-Wachs. We will apply our techniques to this algorithm to<tbc>

