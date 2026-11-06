**Proof.** To bound \(\mathrm{MinPlus}(n_1,n_2,n_3|D\le n_2;K)\) we design an algorithm for the _n_<sub>2</sub>-uniform _K_-doubling Min-Plus Product problem of size \(n_1\times n_2\times n_3\). Let \(A,B\in(X\cup\{\perp\})^{n\times n}\) be the given matrices where \(X\subseteq\mathbb{Z}\) denotes their set of integer entries, i.e., \(|X|\le n_2\) and \(|X+X|\le K|X|\). Our goal is to compute their product _C_.

We first use the algorithm from Hypothesis 1.12 to compute a set \(Y\subseteq X\) of size \(|Y|\ge|X|/K^c\) and a sum-order-preserving additive hash function \(h:Y\rightarrow\{0,\dots,|X|\}\). Then apply Lemma 5.11 to construct a set _S_ satisfying that \(X\subseteq Y+S\). We enumerate all pairs \(s,t\in S\), and for each such pair construct the following two matrices:

\(A_s[i,k]=\left\{\begin{array}{ c c }
h(A[i,k]-s) & \text{if}A[i,k]-s\in Y, \\
\perp & \text{otherwise},
\end{array}\right.\)<br>
\(B_t[k,j]=\left\{\begin{array}{ c c }
h(B[k,j]-t) & \text{if}B[k,j]-t\in Y, \\
\perp & \text{otherwise}.
\end{array}\right.\)

Clearly this is well-defined--we only apply _h_ to elements in _Y_ . Moreover, the Min-Plus Product instance (_A<sub>s</sub>,B<sub>t</sub>_) has a universe size of \(|X|\le n_2\). We solve the instance and report for each output pair (_i,j_) a witness _k_ by Lemma 5.1. We update \(C[i,j]\leftarrow\mathrm{min}\{C[i,j],A[i,k]+B[k,j]\}\) for each triple (_i,k,j_) listed in this way.

## Correctness.

Fix any pair (_i,j_) and let _k_ be a witness of (_i,j_). We have that \(A[i,k],B[k,j]\in X\subseteq Y+S\), hence there are \(s,t\in S\) such that \(A[i,k]-s,B[k,j]-t\in Y\) . In particular, we have that _A<sub>s</sub>_\[_i,k_\]=_h(A_\[_i,k_\]-_s_) and _B<sub>t</sub>_\[_k,j_\]=_h(B_\[_k,j_\]-_t_), so it follows that \((A_s*B_t)[i,j]\le h(A[i,k]-s)+h(B[k,j]-t)\). Conversely, for any non-witness \(k'\) we have<tbc>

\(A[i,k]+B[k,j]<A[i,k']+B[k',j]\)

<tbc>and thus<tbc>

\((A[i,k]-s)+(B[k,j]-t)<(A[i,k']-s)+(B[k',j]-t).\)

<tbc>As the function _h_ is sum-order-preserving, it follows that<tbc>

\(h(A[i,k]-s)+h(B[k,j]-t)<h(A[i,k']-s)+h(B[k',j]-t),\)

<tbc>or equivalently,

\(A_s[i,k]+B_t[k,j]<A_s[i,k']+B_t[k',j]\)

(unless one of these entries is \(\perp\)). Thus, \(k'\) is not a witness of (_A<sub>s</sub>∗B<sub>t</sub>_)\[_i,j_\]. All in all, this proves that _k_ is a witness of (_A∗B_)\[_i,j_\] if and only if _k_ is a witness of \(\mathrm{min}_{s,t\in S}(A_s*B_t)[i,j]\). Therefore, the algorithm is forced to enumerate a proper witness _k_ of (_A∗B_)\[_i,j_\] and to correctly assign _C_\[_i,j_\].

## Running Time.

First we compute the set \(Y\subseteq X\) and the hash function _h_ in time \(|X|^{1+o(1)}\cdot K^{c^\prime}\), for some constant \(c'\), by Hypothesis 1.12. Then we apply Lemma 5.11 which runs in time \(|Y-X||S|\cdot(\mathrm{log}u)^{O(1)}\). By the Plünnecke-Ruzsa inequality (Lemma 2.16) we can bound \(|Y-X|\le|X-X|\le K^2|X|\). The set _S_ is promised to have size \(|S|\le O(|Y-X|/|Y|\cdot\mathrm{log}|X|)\le O(K^2|X|/|Y|\cdot\mathrm{log}|X|)\) by Lemma 5.11, which, using the bound \(|Y|\ge|X|/K^c\) from Hypothesis 1.12, is at most _O(K_<sup>_c_+2</sup>log|_X_|). Hence, this step takes time at most \(|X|\cdot K^{c+4}(\mathrm{log}u)^{O(1)}\). Then we enumerate all \(|S|^2\le O(K^{2c+4}\mathrm{log}^2|X|)\) pairs \(s,t\in S\), and for each pair solve an _n_<sub>2</sub>-unverse Min-Plus product instance. The total time is:

\(\tilde{O}\big(|X|^{1+o(1)}\cdot K^{c^\prime}+|X|\cdot K^{c+4}+K^{2c+4}\cdot\mathrm{MinPlus}(n_1,n_2,n_3|u\le n_2)\big)\)

Recall that \(|X|\le n_2\). Therefore, the lemma statement follows for the constant that is the maximum of \(c'\) and 2_c_+4.

