All our reductions preserve the rank of the problem, so this diagram shows that there exists truly sub-cubic algorithm for kD LWS and \[Static\]kD LWS when the rank is constant (because Min-IP does \[Wil18\]). In addition, we show that kMin-IP reduces to kD LWS and \[Static\]kD LWS, so their hardness are established. We delay our proof of SAT reducing to kMin-IP to Appendix A because it mimics the proof of SAT reducing to Min-IP in \[Che20\].

In addition, we show that 2D LWS,\[Static\]2D LWS with slice rank 3 or above is APSP-hard, and give truly sub-cubic algorithms for 2D LWS,\[Static\]2D LWS with slice rank 1.

## 3.1 Rank _d_ \[Static\]kD LWS Hierarchy

In this section we establish a hierarchy for kD LWS and \[Static\]kD LWS with rank _d_.

**Notations:**

• \(I_j=(\sum i_\ell)-i_j\), \(I_{j,t}=(\sum i_\ell)-i_j-i_t\).<tbc>

• \(I'_j=(\sum i'_\ell)-i'_j\), \(I'_{j,t}=(\sum i'_\ell)-i'_j-i'_t\).<tbc>

• _D<sub>a,b</sub>_ is the set of all (_i_<sub>1</sub>_,...,i<sub>k</sub>_) such that \(a\le i_1+\dots+i_k<b\).<tbc>

• _D<sub>a</sub>=D_<sub>_a,a_+1</sub> is the set of all (_i_<sub>1</sub>_,...,i<sub>k</sub>_) such that _a=i_<sub>1</sub>+_...+i<sub>k</sub>_.

**Theorem 3.1.** (kMin-IP \(\rightarrow(\mathsf{k}-1)\mathsf{D}\mathsf{LWS}\)) _Suppose there exists an algorithm for_ (k-1)D LWS _with rank d with running time_ \(O(n^{k-\varepsilon})\) _for some_ \(\varepsilon>0\)_, then there exists an algorithm for_ kMin-IP _with rank d with running time_ \(O(n^{k-\delta})\) _for some_ \(\delta>0\).

_Proof._ Given an kMin-IP instance with<tbc>

\(X_1=\{x_{11},\dots,x_{1n}\},\dots,X_k=\{x_{k1},\dots,x_{kn}\},\)

<tbc>such that \(x_{ij}\in\{-W,\dots,W,\infty\}^d\) for all \(1\le i\le k,1\le j\le n\), we define _k_ sets of vectors<tbc>

\(Y_1=\{y_{11},\dots,y_{1n}\},\dots,Y_{k-1}=\{y_{k-1,1},\dots,y_{k-1,n}\},Y_k=\{y_{k1},\dots,y_{kn}\}\)

<tbc>as follows: for all \(1\le\ell\le k-1\),<tbc>

\(y_{\ell,j}=\left\{\begin{array}{ c c }
0^d & \text{if}1\le j\le(k-1)n \\
x_{\ell,j\mathrm{mod}n} & \text{if}(k-1)n+1\le j\le kn.
\end{array}\right.\)

<tbc>In addition, let<tbc>

\(y_{kj}=\left\{\begin{array}{ c c }
x_{k,j\mathrm{mod}n} & \text{if}1\le j\le(k-1)n \\
0^d & \text{if}(k-1)n+1\le j\le kn.
\end{array}\right.\)

SAT
Theorem A.6
[Wil05, Che20]
kMin-IP
(k - 1)Min-IP
3Min-IP
Min-IP
Lemma 2.7
Theorem 3.1
[KPS17]
(k - 1)D LWS
(k - 2)D LWS
2D LWS
LWS
Theorem 3.2
[KPS17]
[Static](k - 1)D LWS
[Static](k - 2)D LWS
[Static]2D LWS
[Static]LWS
Theorem 3.4

