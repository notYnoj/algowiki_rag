_i_ and _j_. Thus our goal is to compute _T_\[1_,n_\], and these values satisfy the recurrence

\(T[i,j]=min_{i<k<j}\big\{T[i,k]+T[k,j]+w_i\cdot w_j\cdot w_k\big\}.\)

(Since there is an edge from _i_ to _j_ in the polygon, there must be a triangle involving those two nodes and a third node _k_; the recurrence corresponds to iterating over the choices of that third node.)

This recurrence leads to a DP algorithm which solves the problem in time _O(n_<sup>3</sup>). However, Hu and Shing showed in \[HS82, HS84\] that the problem can actually be solved much faster, in time _O(n_log_n_). This is a surprising example where geometric techniques lead to a faster algorithm than the natural DP formulation.

## 1.1 Least Weight Subsequence Problems

Künnemann, Paturi, and Schneider \[KPS17\] initiated a general study of these phenomena. They studied a general class of problems intended to capture many one-dimensional DP problems called Least Weight Subsequence (LWS) problems: Given as input a positive integer _n_ and an \(n\times n\) matrix _w_, compute the value _T_\[_n_\] defined by the recurrence:

\(T[j]=\left\{\begin{array}{ c c }
0 & \text{if}j=0 \\
min_{0\le i<j}\big\{T[i]+w[i,j]\big\} & \text{otherwise.}
\end{array}\right.\) (1)

LWS was first introduced by Hirschbert and Lamore \[HL87\] to capture many known DP problems, including longest increasing subsequence \[Fre75\], airplane refueling \[HL87\], coin change \[KPS17\], nested boxes \[KPS17\], pretty printing \[KP81\], and various knapsack problems.

For illustration purposes, consider the longest increasing subsequence (LIS) problem: given an array of _n_ integers _X_=\[_x_<sub>1</sub>_,...,x<sub>n</sub>_\], return the length of the longest strictly increasing subsequence in _X_ \[Fre75\]. LIS can be formulated as an LWS problem by setting

\(w[i,j]=\left\{\begin{array}{ c c }
-1 & \text{if}x_i<x_j \\
\infty & \text{otherwise.}
\end{array}\right.\)

Notice that _w_\[_i,j_\] equals negative one when _x<sub>i</sub>_ can be added to a subsequence which ends in _x<sub>j</sub>_, thus increasing the length of a strictly increasing subsequence by 1. Since LIS is a maximization problem and LWS is a minimization problem, the weights are -1, not 1, and the solution is given by -_T_\[_n_\]. Many algorithmic problems can be formulated as an LWS instance by appropriately setting the weight matrix _w_.

1
n
2
n - 1
i
j
j - 1
i + 1
k
k + 1

Figure 1: An example polygon triangulation problem. The polygon _P(i,j_) is partitioned into 3 parts by choosing _k_ and forming a triangle (_i,j,k_) whose weight is \(w_i\cdot w_j\cdot w_k\).

