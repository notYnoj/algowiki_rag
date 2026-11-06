<tbc>_Under a change of variables/coordinates, this problem is equivalent to computing the value of T_\[1_,n_\] _given the dynamic programming recurrence relation:_

\(T[i,j]=\left\{\begin{array}{ c c }
0 & \text{if}j-i\le 1 \\
\mathrm{min}_{i<k<j}\left\{T[i,k]+T[k,j]+w[i,j,k]\right\} & \text{otherwise.}
\end{array}\right.\)

It is not hard to see that polygon triangulation and 2D LWS<sup>PT</sup> are the same problem: let _T_\[_i,j_\] denote the weight of the sub-polygon containing nodes _i_ to _j_ and _w_\[_i,j,k_\] be the weight of triangle (_v<sub>i</sub>,v<sub>j</sub>,v<sub>k</sub>_). More generally, any problem which splits an interval \[_i,j_\] at some point _k_ where _k_ is between _i_ and _j_ can be understood as a 2D LWS<sup>PT</sup> instance. Figure 7 captures the idea of 2D LWS<sup>PT</sup>.

## 3 _k_-dimensional Least Weight Subsequence (kD LWS)

In this section, we discuss kD LWS with rank and slice rank respectively. For kD LWS with rank _d_, we prove the reductions in the following diagram.

1
10
2
9
3
8
4
7
5
6

T
i
j
i
j
O
O
j
n-i
T
n-j
i

Figure 6: An example polygon triangulation problem.

Figure 7: 2D LWS<sup>PT</sup>. To compute _T_\[_i,j_\] (black circle), we are taking the minimum over the sum of all possible **pairs** of white circles (plus their respective weight values _w_). The solution to 2D LWS<sup>PT</sup> is found at _T_\[1_,n_\] in the left figure and at _T_\[_n,n_\] in the right figure due to a change of variables.

