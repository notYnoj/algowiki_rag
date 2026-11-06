For every \(\pi\in S_n\), also \(\pi X\unknown_{\mathrm{poly},n}\pi Y\) .<tbc>

(ii) _Algebraic identities._ The associativity and commutativity identities for \(\oplus_K,\otimes_K\), distributivity of \(\otimes_K\) over \(\oplus_K\), and \(X\otimes_K\mathbf{I}_n(1)\doteq X\) are rules. For each fixed edge _e_, all orders and bracketings of a partial sum are related by \(\doteq\). Products distribute over partial sums in the same direction: for positive integers _r,s_,<tbc>

<tbc>\((X_1\boxplus_e\cdots\boxplus_eX_r)\otimes_K(Y_1\boxplus_e\cdots\boxplus_eY_s)\doteq\boxplus_e_{1\le i\le r1\le j\le s}(X_i\otimes_KY_j).\)<tbc>

<tbc>The right-hand side means the partial sum over the displayed pairs in lexicographic order; a sum with one term means that term. In addition, for every edge _e_=(_u,v_) and positive integers _q,t,r_,<tbc>

<tbc>\(\mathbf{E}_{u,v}^{(q)}\otimes_K\mathbf{E}_{u,v}^{(t)}\doteq\mathbf{E}_{u,v}^{(qt)},\underbrace{X\boxplus_e\cdots\boxplus_eX}_{r\mathrm{copies}}\doteq X\otimes_K\mathbf{E}_{u,v}^{(r)}.\)<tbc>

(iii) _Elementary restrictions and interpolation._ For all expressions for which the partial sum is defined,<tbc>

<tbc>\(X\unknown_{\mathrm{poly},n}X\oplus_KY,X\unknown_{\mathrm{poly},n}X\boxplus_eY,X\boxplus_eY\unknown_{\mathrm{poly},n}X\oplus_KY.\)<tbc>

<tbc>For positive integer vectors **a**=(_a_<sub>1</sub>_,...,a_<sub>_n_-1</sub>) and **b**=(_b_<sub>1</sub>_,...,b_<sub>_n_-1</sub>) with \(b_i\le a_i\) for every \(1\le i\le n-1\), and \(D=1+\sum_{i=1}^{n-1}(a_i-1)\), the rules are<tbc>

<tbc>\(\mathsf{C}_n(\mathbf{b})\unknown_{\mathrm{poly},n}\mathsf{C}_n(\mathbf{a})\unknown_{\mathrm{poly},n}\mathbf{I}_n(D),\mathsf{C}_n(\mathbf{a})\unknown_{\mathrm{poly},n}\otimes_{i=1}^{n-1}\mathbf{E}_{i,n}^{(a_i)}.\)<tbc>

(iv) _Polynomial comparisons._ Let **a**=(_a_<sub>1</sub>_,...,a_<sub>_n_-2</sub>) be a positive integer vector, put \(S=\sum_{i=1}^{n-2}(a_i-1)\), and let _e_=(_n_-1_,n_). For every integer \(b\ge 2\), include<tbc>

<tbc>\(\mathsf{C}_n(\mathbf{a},b+1)\boxplus_e\mathsf{C}_n(\mathbf{a},b-1)\unknown_{\mathrm{poly},n}\mathsf{C}_n(\mathbf{a},b)\boxplus_e\mathsf{C}_n(\mathbf{a},b).\)<tbc>

<tbc>For every positive integer _h_, with \(\sigma\) exchanging legs _n_-1_,n_, include<tbc>

<tbc>\(\mathsf{C}_n(\mathbf{a},h)\boxplus_e\sigma\mathsf{C}_n(\mathbf{a},h)\boxplus_e\mathsf{C}_n(\mathbf{a},h)\unknown_{\mathrm{poly},n}\mathsf{C}_n(\mathbf{a},3h+S).\)<tbc>

<tbc>Both comparisons are also rules after appending the same partial summand \(\boxplus_eU\) to their two sides, whenever it has the required shared dimensions.<tbc>

(v) _Separation._ For all \(m,t\ge 1\) and expressions _X_<sub>0</sub>_,...,X_<sub>_m_-1</sub> as in Lemma 5.4, include

<tbc>\(\left(\begin{array}{ c }
m-1 \\
\oplus_{h=0}^KX_h
\end{array}\right)\otimes_K\mathbf{E}_{n-1,n}^{(t)}\unknown_{\mathrm{poly},n}(X_0\boxplus_e\cdots\boxplus_eX_{m-1})\otimes_K\mathsf{C}_n(m,\dots,m,t),e=(n-1,n).\)<tbc>

<tbc>There are no further rules. In particular, the definition does not identify all expressions representing locally isomorphic tensors and does not allow an arbitrary comparison to be substituted inside a partial sum.

The next lemma verifies that the syntactic rules describe valid tensor constructions. The shared-coordinate issue in the tripling rule is the reason for using the reflected atoms above.

