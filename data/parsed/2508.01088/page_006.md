These vectors will be simply called _sum-vector by row/column/diagonal_ of _v_.

## 3.1 The largest and the least eigenvalue

In this section, the largest and the least eigenvalues of T(_n_) and associated eigenvectors are investigated.

**Theorem 3.6.** _For_ \(n\in\mathbb{N}\)_, the largest eigenvalue of_ T(_n_) _is_ 2_n_-2_. Furthermore,_ 2_n_-2 _is simple and_ **1**<sup>_T(n_)</sup> _is an eigenvector associated with_ 2_n_-2.

_Proof._ Since T(_n_) is (2_n_-2)-regular, as it is well known (see for instance Theorem 1.1.2 in \[7\]) the result follows.

Let’s introduce the family of vectors<tbc>

\(\mathbf{T}_n=\{t_n^{(x,y)}\in\mathbb{R}^{T(n)}|x\in[n-3],y\in[x]\}\)

<tbc>where \(t_n^{(x,y)}\) is the vector defined by

\(\left[t_n^{(x,y)}\right]_{(i,j)}=\left\{\begin{array}{ c c }
t_{(i-x+1,j-y+1)}, & \text{if}x\le i\le x+3\text{and}y\le j\le y+3, \\
0, & \text{otherwise;}
\end{array}\right.\) (3)

with \(t=t_4^{(1,1)}=[0,1,-1,-1,0,1,0,1,-1,0]\) as presented in Figure 6.

Note that each vector of **T**_<sub>n</sub>_ is obtained placing _t_ in all the possible ways over T_<sub>n</sub>_ and completing the remaining entries with zeros. The ordered pair (_x,y_) in Equation (3) corresponds to the entry in T(_n_) where the first coordinate of _t_ is<tbc>

0
0
0
0
0
1
0
0
0
0
1
0
1
1
1
1
0
1
0
0
0
0
0
0
0
0
1
0
0
0
0
0
0
0
1
0
0
0
0
R6,4
C6,2
1
0
1
0
0
1
0
0
0
1
0
0
0
1
0
0
0
0
1
0
0
0
0
1
0
0
0
0
0
1
D6,0

Figure 5: The vectors _R_<sub>6,4</sub>_,C_<sub>6,2</sub> and _D_<sub>6,0</sub>.

