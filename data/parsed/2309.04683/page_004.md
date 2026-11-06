One commonly studied cost of traveling from \((i_1,\dots,i_{\ell-1},j_\ell,i_{\ell+1},\dots,i_k)\) to (_i_<sub>1</sub>_,...,i<sub>k</sub>_) is \(w[i_1,\dots,i_k,j_\ell]=(k-(i_\ell-j_\ell))^2\) for a fixed constant _k_ \[HL87\], which has rank 4 since

\((k-(i_\ell-j_\ell))^2=i_\ell^2\cdot 1+1\cdot j_\ell^2+(i_\ell-k)\cdot(-2j_\ell)+(i_\ell-\frac{k}{2})\cdot(-2k).\)

### Slice Rank

A _d_-dimensional (order-_d_) tensor \(w\in\mathbb{R}^{n_1\times n_2\times\cdots\times n_d}\) has slice rank 1 if there is a \(j\in[d]\), a vector \(a\in\mathbb{R}^{n_j}\), and a (_d_-1)-dimensional tensor \(b\in\mathbb{R}^{n_1\times\cdots\times n_{j-1}\times n_{j+1}\times\cdots\times n_d}\) such that, for all \(i_1\in[n_1],\dots,i_d\in[n_d]\) we have \(w[i_1,\dots,i_d]=a[i_j]\cdot b[i_1,\dots,i_{j-1},i_{j+1},\dots,i_d]\). More generally, the slice rank of tensor _w_ is the minimum non-negative integer _k_ such that there are slice rank 1 tensors _w_<sub>1</sub>_,...,w<sub>k</sub>_ for which \(w=w_1+\cdots+w_k\). Slice rank was recently introduced in the context of solving the cap set problem from extremal combinatorics \[CLP17, Tao16, TS16, BCC<sup>+</sup>17\], but it has since found applications in algorithm design and complexity theory \[BCC<sup>+</sup>17, AW21, Alm21, BL20, BIL<sup>+</sup>21\] and other areas of combinatorics \[EG17, NS17, Saw18, LS19\].

It is immediate that if a tensor _w_ has rank _d_, then it has slice rank at most _d_. However, there are many natural situations where the slice rank of a tensor may be much lower than its rank, and we could hope to take advantage of this to design faster algorithms.

For example, another reasonable cost function for the airplane refueling problem is the one that depends only on the destinations, e.g., each airport charges a fee for landing at that airport. In this scenario, the cost function would have slice rank 1 but very large rank. We discuss the details in Section 5.1.

## 1.3 Higher-dimensional LWS recurrences

Many problems solvable by LWS can be naturally generalized to higher dimensions, which motivates us to study high dimensional version of the LWS recurrence. We focus on two new recurrences which capture most examples. The first, which we call kD LWS, is perhaps the most general.

**Definition 1.1** (kD LWS)**.** _For a positive integer k, consider_ (_k_+1)_-dimensional tensors w_<sub>1</sub>_,...,w<sub>k</sub> of size_ \(n\times n\times\cdots\times n\)_, where_ \(w_\ell[i_1,\dots,i_k,j]\in\{-W,\dots,W,\infty\}\) _for all_ \(1\le\ell\le k\)_. The_ kD LWS _problem asks, given as input w_<sub>1</sub>_,...,w<sub>k</sub>, to determine T_\[_n,...,n_\] _given the dynamic programming recurrence relation:_

\(T\big[j_1,j_2,\dots,j_k\big]=\left\{\begin{array}{ c c }
0 & \text{if}j_1=j_2=\dots=j_k=1 \\
min_{1\le\ell\le k}\big\{min_{1\le i_\ell<j_\ell}\big\{T\big[j_1,\dots,j_{\ell-1},i_\ell,j_{\ell+1},\dots,j_k\big]+w_\ell\big[j_1,j_2,\dots,j_k,i_\ell\big]\big\}\big\}\text{otherwise}.
\end{array}\right.\)

Intuitively, to compute _T_\[_j_<sub>1</sub>_,j_<sub>2</sub>_,...,j<sub>k</sub>_\], we look at all _previous_ terms in the table _T_ that differ from (_j_<sub>1</sub>_,j_<sub>2</sub>_,...,j<sub>k</sub>_) by _one_ coordinate. For example, when _k_=2, 2D LWS can be expressed as

\(T[i,j]=\left\{\begin{array}{ c c }
0 & \text{if}i=j=1 \\
min\left\{min_{1\le k<i}\{T[k,j]+w_1[i,j,k]\}min_{1\le k<j}\{T[i,k]+w_2[i,j,k]\}\right. & \text{otherwise}.
\end{array}\right.\)

kD LWS captures high-dimensional analogs of many previous problems solved by LWS and also some new problems which we discuss below. This includes higher dimensional airplane refueling (see Section 5.1 below), kMin-IP (Section 3.1), all-pairs shortest paths (Section 3.2), multiple nested box chains (Section 5.2), etc. An illustration of 2D LWS is shown in Figure 2.

### Static kD LWS

Similar to \[KPS17\], we also define a notion of "static" kD LWS in which we are given some entries in the DP table, and we would like to compute new entries which depend only on the given entries. The main idea of \[Static\]kD LWS is that we have the information (_T_\[_i_<sub>1</sub>_,...,i<sub>k</sub>_\]) for all (_i_<sub>1</sub>_,...,i<sub>k</sub>_) on a "band" _D_<sub>_a,a+N_</sub> and we want to compute _T_\[_i_<sub>1</sub>_,...,i<sub>k</sub>_\] for all (_i_<sub>1</sub>_,...,i<sub>k</sub>_) on the next "band" _D_<sub>_a+N,a_+2_N_</sub>. A band \(D_{\alpha,\beta}\) is defined to be all (_i_<sub>1</sub>_,...,i<sub>k</sub>_) such that their sum \(i_1+\cdots+i_k\) is in the interval \([\alpha,\beta)\).

