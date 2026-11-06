<tbc>uses the following recurrence:

\(D[i,j]=\left\{\begin{array}{ c c }
0, & \text{if}i=0\text{or}j=0 \\
D[i-1,j-1]+1, & \text{if}A[i]=B[j] \\
max\{D[i-1,j],D[i,j-1]\}, & \text{otherwise.}
\end{array}\right.\) (3)

These transitions correspond to horizontal, vertical and diagonal edges on a grid (see an example in Fig. 2(c)). A known sequential optimization (i.e., sparsification) \[7, 40, 51, 56\] to this recurrence is to observe that only the edges correspond to the diagonal edges with _A_\[_i_\]=_B_\[_j_\] are useful. The computation is equivalent to finding the longest path from the bottom-left to top-right corresponds to these effective (red) edges, and all other edges and states can be skipped. This can lead to a sequential algorithm with _O(L_log_n_) cost, where _L_ is the number of pairs (_i,j_) such that _A_\[_i_\]=_B_\[_j_\]. For LIS, there are exactly _L=n_ such effective edges.

We will show how Cordon Algorithm can be used to parallelize this optimization. Starting with the boundary where _D_\[_i,j_\]=0, we observe that the DP value _D_\[_i,j_\] of any state with _A_\[_i_\]=_B_\[_j_\] can be updated to a _better_ value. Therefore, we will put a sentinel at each of such states to indicate that they should be updated. All such sentinels will block the top-right part of the grid. In this way, the blocked region is clearly marked by a **_staircase_** region, as shown in Fig. 2(d). Therefore, the entire region within the first cordon has the DP value 0. By repeatedly doing this, we will effectively find that the region between the cordons of round _i_+1 and _i_ are those states with DP value (LCS length) _i_. The algorithm finishes in _k_ rounds where _k_ is the LCS length.

The problem boils down to efficiently identifying the cordon (i.e., the staircase) in each round. Note that in LIS there is at most one effective edge in each column (see Fig. 2(d)), while in LCS there can be multiple effective edges in each column (see Fig. 2(e)). We will show an interesting modification to the original LIS algorithm that can handle this more complicated setting. Here we sort all edges by column index as the primary key (from the smallest to largest) and row index as the secondary key (but from largest to smallest). An example is illustrated in Fig. 2(f). Then, we will still use a tournament tree to maintain this list, and apply prefix-min on the row indexes. It is easy to see that a state/edge is on the cordon if its row index is smaller than or equal to the prefix-min. A tournament tree can identify, mark, and remove these states in _O(l_log(_L/l_)) work and _O_(log_n_) span \[47\], where _l_ is the number of diagonal edges on the cordon. We thus have the following theorem.

Theorem 3.2. _Combining with a tournament tree, Cordon Algorithm leads to a perfect parallelization (O(L_log_n_) _work and O(k_log_n_) _span) of sequential LCS algorithm in \[7\], where n and m\<n are the input sequence sizes, L is the number of pairs_ (_i,j_) _such that A_\[_i_\]=_B_\[_j_\]_, and k is the LCS length._

Since _L=O(n_<sup>2</sup>), the _O_(log_L_) terms in the cost of the tournament trees is stated as _O_(log_n_) in the theorem.

Interestingly, to the best of our knowledge, this is the first parallel LCS algorithm with _o(mn_) work and _o_(min(_n,m_)) span for sparse LCS problem (i.e., _L=o(mn_) and _k=o_(min(_n,m_))). Meanwhile, this algorithm is quite simple--we provide our implementation in \[35\] and experimentally study it in Sec. 6. Another interesting finding is that our algorithm implies how to map LCS to LIS (we only know the other direction). Given two input strings _A_ and _B_, if we sort all (_i,j_) pairs for _A_\[_i_\]=_B_\[_j_\] by increasing _i_ (primary key) and decreasing _j_ (secondary key), then LCS is equivalent to the LIS on the secondary keys (the _j_(s)) of this sorted list.

We will show more sophisticated parallelization of DP algorithms in the next sections. Our LCS algorithm will be a subroutine in the more involved parallel GAP algorithm introduced in Sec. 5.2.

## 4 PARALLEL GENERALIZED LWS

We now discuss the convex/concave **_generalized least weight subsequence (GLWS)_** problem, which is one of the most classic cases of decision monotonicity (DM). Given a cost function _w(j,i_) for integers \(0\le j<i\le n\) and _D_\[0\], the GLWS problem computes:

\(D[i]=min_{0\le j<i}\{E[j]+w(j,i)\}\) (4)

for \(1\le i\le n\), where _E_\[_j_\]=_f(D_\[_j_\]_,j_) can be computed in constant time. The original least weight subsequence (LWS) problem \[52\] is a special case when _E_\[_j_\]=_D_\[_j_\]. Here we use the general case _E_\[_j_\]=_f(D_\[_j_\]_,j_) that has the same sequential work bound \[37, 38, 41, 43, 44, 62\], because the generalized version is needed in many applications (see examples in Sec. 5). The GLWS problem is also referred to as 1D/1D DP by Galil and Park \[44\]. The GLWS problem is highly relevant to other important problems (e.g., line breaking \[66\], optimal alphabetic trees \[72\], and a number of computational geometry problems \[1\]). The essence of GLWS is to cluster a list of 1D objects based on spatial proximity and minimize the total weighted sum of all clusters. As an intuitive example, consider selecting a subset of villages on a road (with their coordinates known) to build post offices to minimize the total cost,<tbc>

Ai
8
8
Prefix min
On Cordon?
LiS = 1
8
7
7
7
States
7
(3,6)
6
7
LIS = 2
6
6
6
6
(4,8)
6
X
LIS = 3
5
5
5
5
4
4
4
4
3
3
3
3
(6,4)
4
3
2
2
2
2
(7,7)
4
X
7
3
6
8
1
4
2
5
1
1
1
1
(7,3)
3
(7,2)
2
i
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
1
2
3
4
5
6
7
8
(a)
(b)
(c)
(d)
(e)
(f)

**Figure 2**: Illustrations for the LIS/LCS problem and the Cordon Algorithm. Subfigure (a): An input sequence for LIS with the DP value of each element. Subfigure (b): A geometric view of the input sequence on a 2D plane with each element represented as (_i,A<sub>i</sub>_). Subfigure (c): The corresponding LCS on this input--the answer is the longest path from (0,0) to (8,8) using the maximum number of red edges. Subfigure (d): The process to compute the second cordon. The ready states are marked in the shaded gray region. The cordon is decided by the three cells with LIS=2 in the original input. Subfigure (e): A general LCS case where every diagonal can be a red edge. Subfigure (f): An example execution of our LCS algorithm. Here we only show unready states for simplicity.

