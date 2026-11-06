An illustration of 2D LWS can be found in Figure 2.

Like \[KPS17\], we also define \[Static\]kD LWS, a generalization of \[Static\]LWS to higher dimensions which is central to our reductions.

**Definition 2.15.** (\[Static\]kD LWS) _Given intervals D_<sub>_a,a+N_</sub>_,D_<sub>_a+N,a_+2_N_</sub> _together with correctly computed values_ \(T_\ell[i_1,\dots,i_k]\) _for all_ \(1\le\ell\le k\) _and_ \((i_1,\dots,i_k)\in D_{a,a+N}\), \[Static\]kD LWS _asks to determine_

\(T'\big[j_1,\dots,j_k\big]=min_{1\le\ell\le k}\big\{min_{a-I_\ell\le i_\ell<a+N-I_\ell}\big\{T_\ell\big[j_1,\dots,j_{\ell-1},i_\ell,j_{\ell+1},\dots,j_k\big]+w_\ell\big[j_1,j_2,\dots,j_k,i_\ell\big]\big\}\big\}\)

_for all_ \((j_1,j_2,\dots,j_k)\in D_{a+N,a+2N}\).

An illustration of \[Static\]2D LWS can be found in Figure 3.

## 2.6 Tensor Ranks

We give definitions of rank and slice rank for tensors. For notational convenience, we say that a problem has rank _d_ if its associated array/tensor has rank _d_.

**Definition 2.16** (Rank)**.** _We say that a k-dimension array w has_ rank _d if there exists k sets_

\(X_1=\{x_{11},\dots,x_{1n}\},\dots,X_k=\{x_{k1},\dots,x_{kn}\}\)

_of vectors with length d such that_ \(w[i_1,\dots,i_k]=\langle x_{1,i_1},x_{2,i_2},\dots,x_{k,i_k}\rangle\) _for all_ \(1\le i_1,\dots,i_k\le n\).

**Definition 2.17** (Slice Rank)**.** _A k-dimensional (order-k) tensor_ \(w\in\mathbb{R}^{n_1\times n_2\times\cdots\times n_d}\) _has slice rank_ 1 _if there is a_ \(j\in[d]\)_, a vector_ \(a\in\mathbb{R}^{n_j}\)_, and a_ (_d_-1)_-dimensional tensor_ \(b\in\mathbb{R}^{n_1\times\cdots\times n_{j-1}\times n_{j+1}\times\cdots\times n_d}\) _such that, for all_ \(i_1\in[n_1],\dots,i_d\in[n_d]\) _we have_

\(w[i_1,\dots,i_d]=a[i_j]\cdot b[i_1,\dots,i_{j-1},i_{j+1},\dots,i_d].\)

_More generally, the slice rank of tensor w is the minimum non-negative integer k such that there are slice rank_ 1 _tensors w_<sub>1</sub>_,...,w<sub>k</sub> for which_ \(w=w_1+\cdots+w_k\).

## 2.7 Polygon Triangulation

In computational geometry, a polygon triangulation is a partition of a polygon _P_ into triangles. It is known that the number of partitions of a convex polygon is counted by the Catalan numbers \[Sta15\]. We discuss the problem of finding the triangulation that minimizes the sum of weights of all triangles.

**Definition 2.18** (Polygon Triangulation)**.** _Let P(n_) _denote an n-sided convex polygon and fix an ordering of the polygon vertices. A triangulation of P(n_) _is a partition of P(n_) _into disjoint triangles using straight, internal edges between pair of nodes of P(n). For each triangle_ (_v<sub>i</sub>,v<sub>j</sub>,v<sub>k</sub>), let w(i,j,k_) _be its weight, and the weight of a partition is the sum of all weights of its triangles. The polygon triangulation problem asks to determine the minimal weight of all partitions._

For an example, consider the polygon triangulation of a polygon _P_ with 10 sides (see figure 6). Starting from the side (1,10), we choose a node 6 and partitions _P_ into 3 parts _P_(1,6), triangle (1,6,10) and _P_(6,10), denoted by the black dashed lines. We further partitions _P(i,j_) by choosing a node _i\<k\<j_ and partitions it to _P(i,k_), triangle (_i,j,k_) and _P(k,j_).

The polygon triangulation problem can be solved via dynamic programming, motivating our 2D LWS<sup>PT</sup> problem.

**Definition 2.19** (2D LWS<sup>PT</sup>)**.** _Fix a tensor w. The_ 2D LWS<sup>PT</sup> _problem asks to compute the value of T_\[_n,n_\] _given the dynamic programming recurrence relation:_

\(T[i,j]=\left\{\begin{array}{ c c }
0 & \text{if}i+j\le n+2 \\
min_{0<k<i+j-n}\big\{T[n-j+k,j]+T[i,j-k]+w[i,j,k]\big\} & \text{otherwise}.
\end{array}\right.\)

