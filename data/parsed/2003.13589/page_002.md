### Our contribution.

We design a faster subquadratic \(\mathcal{O}(n^2loglogn/\sqrt{logn})\) time algorithm for LCIS. Interestingly, instead of using the combinatorial properties of LCIS as in the previous work we apply a technique based on exploiting tabulation (but differently than in the classical "Four Russians" approach). This allows our algorithm to be modified to solve the Longest Common Weakly Increasing Subsequence (LCWIS) problem (for which an \(\mathcal{O}(n^{2-\epsilon})\) time algorithm is also known to refute SETH \[8\]). This doesn’t seem to be the case for Duraj’s approach based on bounding the number of so-called significant symbol matches, that for LCWIS might be \(\Omega(n^2)\). Throughout the paper we assume that _A_ and _B_ are of the same length, and the goal is to calculate the length of LCIS. However, the algorithm can be easily modified to avoid this assumption and recover the subsequence itself.

### Overview of the paper.

Our algorithm is based on combining two different procedures. By appropriately selecting the parameters, the overall complexity becomes \(\mathcal{O}(n^2loglogn/\sqrt{logn})\) as explained in Section 5.

The first procedure described in Section 3 works fast when there are only few distinct elements in both sequences. We start with a solution based on dynamic programming working in \(\mathcal{O}(t\cdot n^2)\) time, where _t_ is the number of distinct elements in both sequences. Then, we exploit tabulation to decrease its running time to \(\mathcal{O}(t\cdot n^2/logn)\).

The second procedure described in Section 4 is efficient when there are not too many matching pairs, that is, pairs (_i,j_) such that _A_\[_i_\]=_B_\[_j_\]. The main idea is to calculate, for every such pair, LCIS of _A_\[1_..i_\] and _B_\[1_..j_\] that ends with _A_\[_i_\]=_B_\[_j_\]. This is done by applying an appropriate dynamic predecessor structure. This roughly follows the ideas of Duraj, except that instead of using van Emde Boas trees we notice that, in fact, one can plug in any balanced search trees with efficient split/merge.

In Section 6 we explain the necessary modification required to adapt our solution for LCWIS.

## 2 Preliminaries

We work with sequences consisting of integers. For such a sequence _A_, we write _A_\[_i_\] to denote the _i_-th element, and _A_\[1_..i_\] to denote the prefix of length _i_. |_A_| is the length of _A_. Let \(\sigma\) be the sequence consisting of all distinct integers present in _A_ and _B_, arranged in the increasing order, and cnt(_v_) be the total number of occurrences of \(\sigma[v]\) in _A_ and _B_.

We call a pair of indices (_x,y_) a _matching pair_ when _A_\[_x_\]=_B_\[_y_\]. Further, we call it a \(\sigma[i]\)_-pair_ when \(A[x]=B[y]=\sigma[i]\).

We write _LCIS(i,j_) to denote _LCIS(A_\[1_..i_\]_,B_\[1_..j_\]), that is, the longest increasing common subsequence of _A_\[1_..i_\] and _B_\[1_..j_\]. We write \(LCIS\unknown(i,j)\) to denote the longest strictly increasing subsequence of _A_\[1_..i_\] and _B_\[1_..j_\] which includes both _A_\[_i_\] and _B_\[_j_\] (so in particular, _A_\[_i_\]=_B_\[_j_\]).

Throughout the paper, log_x_ denotes log<sub>2</sub>_x_.

## 3 First Solution

In this section we describe an algorithm for finding LCIS in \(\mathcal{O}(|\sigma|\cdot n^2/logn)\) time.

Let _dp<sub>v</sub>_\[_i_\]\[_j_\] denote the largest possible length of a sequence _C_ such that:

1. _C_ is an increasing common subsequence of _A_\[1_..i_\] and _B_\[1_..j_\],<tbc>

2. _C_ consists of elements not larger than \(\sigma[v]\).

