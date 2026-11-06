**Proof.** We write \(nX=X+\cdots+X\) for the _n_-fold iterated sumset of _X_. The proof is by repeated applications of Ruzsa’s triangle inequality (Lemma 2.17). The first application is with \(X'=2X\), \(Y'=2Y\) and \(Z'=Z\) to conclude that<tbc>

\(|Z+Z|=|2X+2Y|\le\frac{|2X+Z||2Y+Z|}{|Z|}=\frac{|3X+Y||X+3Y|}{|Z|}.\)

<tbc>The second application is with \(X'=3X\), \(Y'=Y\) and \(Z'=X\) to obtain<tbc>

\(|3X+Y|\le\frac{|3X+X||X+Y|}{|X|}=\frac{|4X||Z|}{|X|}\le\frac{K^4|X||Z|}{|X|}=K^4|Z|;\)

<tbc>here we also used the Plünnecke-Ruzsa inequality (Lemma 2.16) \(|nX|\le K^n|X|\). The third application is symmetric:

\(|X+3Y|\le\frac{|X+Y||3Y+Y|}{|Y|}=\frac{|Z||4Y|}{|Y|}\le\frac{|Z|K^4|Y|}{|Y|}=K^4|Z|.\)

The statement follows from putting these three bounds together.

**Lemma 4.13** (Reduction from Uniform Regular to Uniform Low-Doubling Exact Triangle)**.** _For any parameter_ \(K\ge 1\) _there is a potential-adjusting reduction from any D_-uniform 1_/D_-regular _Exact Triangle instance to O(K_<sup>1/112</sup>) _instances that are each D_-uniform, 1_/D_-regular _and K_-doubling. _The reduction runs in deterministic time_ \(\tilde{O}(n_1n_2n_3/K^{1/112}+(n_1n_2+n_2n_3+n_1n_3)DK^{1/112})\)_. In particular:_

\(\text{ExactTri}(n_1,n_2,n_3|D;\rho\le 1/D)\)<br>
\(\le\tilde{O}\big(K^{1/112}\cdot\text{ExactTri}(n_1,n_2,n_3|D;\rho\le 1/D;K)+\frac{n_1n_2n_3}{K^{1/112}}+(n_1n_2+n_2n_3+n_1n_3)DK^{1/112}\big).\)

**Proof.** Let _X_ denote the set of entries in the given _D_-uniform instance, i.e., \(|X|\le D\). We apply BSG Covering with _X=Y=Z_ with some parameter _L_ to be picked later, resulting in sets _X_<sub>1</sub>_,...,X<sub>L</sub>,Y_<sub>1</sub>_,...,Y<sub>L</sub>_ and _R_. We say that a triangle (_i,k,j_) is in the _structured_ part if \((A[i,k],B[k,j])\in X_\ell\times Y_\ell\) (for some \(\ell\in[L]\)), and otherwise, if \((A[i,k],B[k,j])\in R\), we say that it is in the _remainder_. We deal with these two types of triangles in two separate steps:

1. _(Remainder)_ We will explicitly list all exact triangles in the remainder. Enumerate all pairs \((x,y)\in R\), enumerate all \(k\in[n_2]\) and enumerate all \(i\in[n_1]\) with _A_\[_i,k_\]=_x_ and all \(j\in[n_3]\) with _B_\[_k,j_\]=_y_. All exact triangles (_i,k,j_) that we detect in this way are stored in a set T .<tbc>

<tbc>_Running Time:_ Recall that the given instance is 1_/D_-regular, hence for all fixed _k,x_ there are at most _n_<sub>1</sub>_/D_ indices _i_ with _A_\[_i,k_\]=_x_, and similarly for _B_. It follows that the running time is:<tbc>

<tbc>\(O(|R|\cdot n_2\cdot(n_1/D)\cdot(n_3/D))=O(n_1n_2n_3/L).\)<tbc>

2. _(Structured Part)_ Enumerate all \(\ell\in[L]\). We compute the set \(X_\ell+Y_\ell\) (by brute-force, say) and construct the matrices

\(A_\ell[i,k]=\left\{\begin{array}{ c c }
A[i,k] & \text{if}A[i,k]\in X_\ell, \\
\perp & \text{otherwise},
\end{array}\right.\)<br>
\(B_\ell[k,j]=\left\{\begin{array}{ c c }
B[k,j] & \text{if}B[k,j]\in Y_\ell, \\
\perp & \text{otherwise},
\end{array}\right.\)<br>
\(C_\ell[i,j]=\left\{\begin{array}{ c c }
C[i,j] & \text{if}C[i,j]\in X_\ell+Y_\ell, \\
\perp & \text{otherwise}.
\end{array}\right.\)

