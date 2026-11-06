_Case 1._ If \(\mathbf{w}'\equiv\varepsilon\mathbf{w}(modr)\) for some \(\varepsilon\in\{\pm 1\}\), then \(b\equiv\varepsilon\sigma\) and every \(m_t\equiv 0\). Hence _g=r_, so _N=r_ and _P_=1_/r_.

_Case 2._ Suppose all \(m_t\equiv 0(modr)\). If \(r\ge 3\), then \(m_t\in\{0,\pm 1,\pm 2\}\) forces _m<sub>t</sub>_=0 for all _t_, i.e. \(\mathbf{w}'=\sigma b\mathbf{w}\) over Z; since \(\mathbf{w}'\neq\mathbf{0}\); this gives \(\mathbf{w}'=\pm\mathbf{w}\). If _r_=2, it gives \(\mathbf{w}'\equiv\mathbf{w}(mod2)\). Either way we are in Case 1. So in Case 2 some _m<sub>t</sub>_ is non-zero mod _r_, and since \(|m_t|\le 2\), we get \(g\in\{1,2\}\). Hence \(N\in\{1,2\}\), and _N_=2 requires 2|_r_. Thus \(P=N/r^2\in\{1/r^2,2/r^2\}\), with _P_=1_/r_<sup>2</sup> for odd _r_.

## D.2 Proof of Claim 6.0.2

Let **w** and **x** are two non-zero binary vectors such that \(\mathbf{w}\unknown\equiv_s\pm\mathbf{x}\). Consider the span of two vectors **w** and **x**, say _S_. Any vector in _S_ is of the form \(\alpha\mathbf{w}+\beta\mathbf{x}\). For this vector to be a 0/1 vector, \(\alpha,\beta\in\{0,1\}\) and \(\alpha+\beta\in\{0,1,2\}\). Considering all the possibilities of \(\alpha\) and \(\beta\), there can be at most 3 non-zero binary vectors in _S_. This completes the proof.

## D.3 Proof of Proposition 6.0.2

Fix a matrix \(\mathsf{M}\in\mathsf{M}_t\) of rank _t_. Permute the columns so that the first _t_ columns \(M_1,\dots,M_t\in\{0,1\}^n\) are linearly independent over Z_<sub>s</sub>_. Since these columns are independent, there exists a set of rows \(R\subseteq[n]\) with |_R_|=_t_ such that the \(t\times t\) submatrix _A_:=M[_R,_{1_,...,t_}] is invertible over Z_<sub>s</sub>_.

For each column index _i\>t_, since rank(M)=_t_, there exists a unique coefficient vector \(c_i\in\mathbb{Z}_s^t\) such that \(\left[M_1\cdots M_t\right]c_i\equiv_sM_i\). Restricting this identity to the rows in _R_ yields \(Ac_i\equiv_sa_i\), where \(a_i:=\mathsf{M}[R,i]\in\{0,1\}^t\).

Since \(A\in\{0,1\}^{t\times t}\) is invertible, Hadamard’s inequality implies \(|det(A)|\le t^{t/2}\). Define the set<tbc>

\(S:=\{xmods:x\in\mathbb{Z},|x|\le t^{t/2}\},\)

<tbc>so that |_S_|=O(_t_<sup>_t/_2</sup>) and \(det(A)\in S\backslash\{0\}\). Hence \(det(A)^{-1}\in S^{-1}\), where |_S_<sup>-1</sup>|=|_S_|. By Cramer’s rule, for each coordinate \(j\in[t]\),

\((c_i)_j\equiv_sdet(A_{i,j})\cdot det(A)^{-1},\)

where _A<sub>i,j</sub>_ is the matrix obtained from _A_ by replacing its _j_-th column with _a<sub>i</sub>_. Since \(A_{i,j}\in\{0,1\}^{t\times t}\), we also have \(det(A_{i,j})\in S\). Define the set \(S':=S\cdot S^{-1}\subseteq\mathbb{Z}_s\). Then \(|S'|\le|S|^2=\mathcal{O}(t^t)\), and each coordinate (_c<sub>i</sub>)<sub>j</sub>_ lies in \(S'\). Consequently, we get \(c_i\in(S')^t\) and \(|(S')^t|=\mathcal{O}(t^{t^2})\).

To construct a rank-_t_ matrix, we have the following procedure:

• choose the _t_ independent columns in O(2_<sup>tn</sup>_) ways,<tbc>

• choose each of the remaining _m-t_ columns via a coefficient vector \(c_i\in(S')^t\), contributing O((_t_<sup>_t_2</sup>)<sup>_m-t_</sup>) choices,<tbc>

• and finally permute the columns, contributing a factor of _m_!.

Multiplying these bounds gives the claimed estimate.

## D.4 Proof of Lemma 6.0.4

Recall that D_<sub>ij</sub>_ (and similarly D_<sub>lk</sub>_) is a binary random variable equal to 1 if and only if events \(\mathsf{E}_{\mathsf{LS},p}^{(i)}\), \(\mathsf{E}_{\mathsf{RS},p}^{(i)}\), \(\mathsf{E}_{\mathsf{LS},p}^{(j)}\), \(\mathsf{E}_{\mathsf{RS},p^\prime}^{(j)}\), \(\mathsf{E}_{\mathsf{TS},q^\prime}^{(i)}\), and \(\mathsf{E}_{\mathsf{TS},q}^{(j)}\) occur simultaneously (and analogously for indices _l,k_). Each E<tbc>

