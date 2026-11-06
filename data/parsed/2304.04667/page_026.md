6. finally, for every pair of nodes _u,v_ such that<tbc>

(a) \(u\in S_{f(v),p}\) (i.e., _u_ and _v_ are not separated) in the final instances of at least _k_ repetitions, or<tbc>

(b) \(u\in C_{p,f(v)}\) or \(v\in C_{p,f(u)}\) in at least _k_ repetitions,<tbc>

<tbc>query Max-Flow(_u,v_) directly.

## Queries

For data structure 1 of Theorem 3.1, to answer a query for a pair of nodes _u_ and _v_, we operate similarly to the Monte Carlo algorithm; first check if Max-Flow(_u,v_) was computed directly. If so, we output the corresponding separator, and otherwise we pick the answer with minimal value in the recursion trees that separated _u_ and _v_ in all relevant stages. The number of terminals in a \[_k,_2_k_\] stage is at most \(t_k=min\{\alpha(V)/k,n\}\), and so the total time to preprocess all node pairs in all stages and repetitions is \(\tilde{O}(max_k\left\{t_k^2\cdot k\right\})\le\tilde{O}(\alpha(V)n)\), bringing the query time to \(\tilde{O}(1)\), as required. On the bounds in data structure 2 of Theorem 3.1 we elaborate in the _Space usage_ paragraph, later in this section.

## Correctness

Let _u,v_ be any pair of nodes. We claim that if the pair _u,v_ is not queried directly, then it must be separated by a pivot _p_ such that \(p\notin C_{u,v}\), and then the correctness follows from the correctness proof in Section 3.1. Next, we bound the amount of times a single pivot is chosen throughout the algorithm.

**Lemma 3.6.** _With high probability, each pivot is chosen at most_ 8log_n times throughout all repetitions and depths._

_Proof._ Pivots are only chosen in instances of size greater than 60_k_log<sup>3</sup>_n_, and each recursion depth has always at most 60_k_log<sup>3</sup>_n_ instances containing _p_. As a result, the probability that the same pivot _p_ is chosen more than 8log_n_ times in the same recursion depth is at most 1_/n_<sup>6</sup>. By the union bound over all nodes, repetitions, and depths, with high probability no node is selected as a pivot more than 8log_n_ times, as required.

We say that a recursion tree becomes _invalid_ for a pair _u,v_ if _u_ and _v_ are separated in the tree (_u,v_ were assigned to different sets, i.e., \(f(u)\neq f(v)\)) but in a sub-optimal way, due to a pivot choice _p_ that belonged to _C<sub>u,v</sub>_. By Lemma 3.6, at every depth of the recursion at most 16_k_log_n_ recursion trees become invalid for the pair _u,v_. This is because the size of optimal separators in this stage is bounded by 2_k_. Since the height of the recursion tree is at most log<sub>4/3</sub>_n_ (see below), at the end of the recursion at least \(60klog^3n-16\cdot(1/log(4/3))\cdot klog^2n\ge 20klog^3n\) repetitions must not be invalid for _u,v_. In those 20_k_log<sup>3</sup>_n_ remaining repetitions, one of the following three options must occur.

(i) _u_ and _v_ are not separated in the final instances of at least _k_ repetitions.<tbc>

(ii) \(u\in C_{p,v}\) (or \(v\in C_{p,u}\), symmetrically) in at least _k_ repetitions.<tbc>

(iii) _u_ and _v_ are separated \(\left(\text{i.e.,}u\in S_{f(u),p}\text{and}v\in S_{p,f(u)}\right)\) in at least one repetition by a pivot _p_ that does not belong to _C<sub>u,v</sub>_.

In cases (i) and (ii) we must have queried the pair _u,v_ directly in steps 6a and 6b, respectively. Otherwise, as the at most 2(_k_-1) repetitions where _u_ and _v_ fail to satisfy the requirements of step 6 can be identified, case (iii) occurs and we immediately have the right answer in a recursion tree.

