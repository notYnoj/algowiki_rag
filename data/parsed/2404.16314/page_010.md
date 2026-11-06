improve the span bounds. Due to page limit, we provide the details of \[72\] in appendix A, and review the high-level idea here. The algorithm computes an _l_-tree \[46\], which has the same depth with and will be finally converted to the OAT in _O(n_) work and polylogarithmic span. The key insight of \[72\] is to start with a sequence of _n_ leaf nodes with the input weights, and find several disjoint intervals in the sequence to process in parallel. This partition is done by various operations on the Cartesian tree of the input sequence, which requires _O(n_log_n_) work and _O_(log<sup>2</sup>_n_) span. Larmore et al. showed that processing each interval can be reduced to a convex LWS. The solution of the LWS will connect items in this interval into a forest, which becomes a subgraph in the final _l_-tree. Finally, for each tree in the forest, we insert its root back to the sequence and repeat the process. This reinsertion step takes _O(n_log_n_) work and _O_(log_n_) span by basic parallel primitives such as sorting and range-minimum queries. The further rounds will connect the forest to the final _l_-tree. Larmore et al. also showed that the number of such intervals shrinks to half in each iteration, so the algorithm will finish in _O_(log_n_) rounds. Here all other steps in addition to solving convex LWS take _O(n_log<sup>2</sup>_n_) work and _O_(log<sup>3</sup>_n_) span. The remaining cost of the algorithm is to solve convex LWS in each round, multiplied by the number of rounds, which is _O_(log_n_).

Larmore et al. originally used the parallel convex LWS algorithm from \[4, 6\], which has _O(m_<sup>2</sup>log_m_) work and _O_(log<sup>2</sup>_m_) span when taking an input interval of length _m_. Later, Larmore and Przytycka \[69\] improved the parallel convex LWS algorithm to _O(m_<sup>1.5</sup>log_m_) work and \(O(\sqrt{m}logm)\) span, yielding _O(n_<sup>1.5</sup>log<sup>2</sup>_n_) work and \(O(\sqrt{n}log^2n)\) span for the OAT algorithm--the work overhead is still polynomial. Larmore et al. \[72\] left the open problem on whether there exists an OAT algorithm with \(\tilde{O}(n)\) work and polylog(_n_) span, which remains unsolved for three decades.

Note that the convex LWS problem is a special case of the convex GLWS problem discussed in Sec. 4.1 with _E_\[_i_\]=_D_\[_i_\]. Hence, Alg. 1 directly gives _O(m_log_m_) work and _O(k_log<sup>2</sup>_m_) span for convex LWS problem, and here _k_ is the longest dependency path of best decisions. In Larmore’s algorithm, the forest for each interval is constructed iteratively by the DP algorithm on LWS: if iteration _i_ finds the best decision at iteration _j\<i_, then iteration _i_ creates one more level on top of the forest at iteration _j_. This means that the _k_ is equivalent to the depth of the forest, which is upper bounded by the final OAT height _h_. We present more details in appendix A. Hence, we can parameterize our final bounds using _h_ as:

Theorem 5.1. _The optimal alphabetic tree (OAT) can be constructed in O(n_log<sup>2</sup>_n_) _work and O(h_log<sup>3</sup>_n_) _span, where n is the size of input weight sequence and h is the height of the OAT._

This algorithm is nearly work-efficient with span parameterized on _h_. One useful observation is that the OAT height _h_ is polylogarithmic with real-world input instance with positive integer weights and fixed word length. More formally, we can show that:

Lemma 5.1. _If all input weights are positive integers in word size W, the OAT height is O_(log_W)._

The proof is not complicated and given in appendix A. With this lemma, we can state the following corollary.

Corollary 5.1.1. _If the input key weights are positive integers with word size W=n_polylog_n, the OAT can be constructed in O(n_log<sup>2</sup>_n) work and_ polylog(_n_) _span, where n is the input size._

The bounds also hold for real number weights if the ratio between the largest and smallest weight is _n_polylog_n_. We note that in realistic models we usually assume word-size _W=n_<sup>_O_(1)</sup>, in which case Cor. 5.1.1 affirmatively answers the open problem in \[72\].

## 5.2 The GAP Edit Distance Problem

The GAP problem is a variant of the famous edit distance problem. The GAP problem aligns two input strings with sizes _n_ and \(m\le n\), and allows editing a substring with certain cost function (formally defined below). This problem has been widely studied both sequentially \[28, 38, 42\] and in parallel \[18, 27, 30, 45, 59, 85, 88\]. As noted by Eppstein et al. \[38\], most real-world cost functions are either convex or concave, yielding \(\tilde{O}(nm)\) work for the GAP problem sequentially. Unfortunately, to the best of our knowledge, these existing parallel algorithms for the GAP problem need \(\Omega(n^2m)\) work, and the polynomial overhead makes them less practical.

More specifically, GAP takes two strings _A_\[1_..n_\] and _B_\[1_..m_\], and computes the minimum cost to align _A_ and _B_ using the following operations: 1) deleting _A_\[_l_+1_..r_\] with cost _w_<sub>1</sub>(_l,r_), and 2) deleting _B_\[_l_+1_..r_\] with cost _w_<sub>2</sub>(_l,r_). Here we consider the following recurrence, which is usually referred to as the GAP recurrence:

\(P[i,j]=min_{0\le i^\prime<i}D[i',j]+w_1(i',i)Q[i,j]=min_{0\le j^\prime<j}D[i,j']+w_2(j',j)D[i,j]=min\{P[i,j],Q[i,j],D[i-1,j-1]|A[i]=B[j]\}.\)

Here _P_\[_i,j_\] and _Q_\[_i,j_\] indicate the edits on the two strings. Directly computing the recurrence uses _O(n_<sup>2</sup>_m_) work. Since most real-world cost functions in machine learning, NLP, and bioinformatics \[38\] are either convex or concave, sequentially each row in _P_ or column in _Q_ is a convex or concave GLWS and can be computed in \(\tilde{O}(n)\) or \(\tilde{O}(m)\) work. Hence, computing the entire _P_ and _Q_ takes \(\tilde{O}(nm)\) work, leading to the same cost for computing _D_ and the entire problem. We denote this standard sequential algorithm as \(\Gamma_{gap}\).

Parallelizing this approach is extremely challenging even with the parallel convex/concave GLWS in Sec. 4 as a subroutine, and we are unaware of any existing work on this. The challenge here is that the rows in _P_ interact with the columns in _Q_. For instance, computing a row in _P_ requires one element from each column in _Q_, but computing those elements again requires previous rows in _P_.

Our key insight to parallelize this algorithm is to use the Cordon Algorithm to efficiently mark the ready region to be computed in each round. Note that as a generalization of the classic edit distance/LCS, the GAP recurrence is similar to Recurrence 3, but with "jumps" in computing _P_ and _Q_. An illustration is given in Fig. 4.<tbc>

8
8
7
7
6
6
5
5
(a)
4
(b)
4
3
3
2
2
1
1
1
2
3
4
5
6
7
8
1
2
3
4
5
6
7
8

**Figure 4**: Example of a cordon in the GAP problem.

