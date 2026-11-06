### Query.

Given a modification matrix _C_, if the short-circuit flag \(\delta>\delta_C\) is active, we return 0. Otherwise, the query algorithm identifies the \(k\le\delta_C\) coordinates of the nonzero entries to form the standard basis selection matrices _U<sub>C</sub>_ and _V<sub>C</sub>_.

To form the inner matrix \(Y^TM_\mathrm{pad}^{-1}X\), we simply extract the relevant rows and columns from our precomputed matrix _W<sub>Q</sub>_. Because _U<sub>C</sub>_ and _V<sub>C</sub>_ map directly to indices within _Q_, this amounts to an \(O(\delta_C)\times O(\delta_C)\) submatrix lookup, alongside the static _U_ and _V_ blocks. Since \(\delta\le\delta_C\), the total dimension of this inner matrix is at most \(2\delta_C\times 2\delta_C\).

We multiply this submatrix by \(\Sigma\), add \(I_{k+\delta}\), and evaluate its determinant.

• **For** _d_=0**:** Computing the determinant of this \(O(\delta_C)\times O(\delta_C)\) scalar matrix costs \(O(\delta_C^\omega)\) field operations.<tbc>

• **For** \(d\ge 1\)**:** The entries extracted from _W<sub>Q</sub>_ have rational degree _O(dN_). Computing the determinant of an \(O(\delta_C)\times O(\delta_C)\) matrix with entries of degree _O(dN_) takes \(\widetilde{O}(dN\delta_C^\omega)\) operations.

Multiplying this final determinant by the precomputed scalar det(_M_<sub>pad</sub>) completes the query procedure. \(\square\)

## A.3 Proof of Theorem 3.2

_Proof._ We treat the diagonal entries \(\{c_{i,e}:i\in[k],e\in E\}\) of the matrices _C_<sub>1</sub>_,...,C<sub>k</sub>_ as formal variables and work over the polynomial ring F\[{_c<sub>i,e</sub>_}\].

We first show that \(S\subseteq E\) is independent in \(M^{\vee k}\) if and only if the submatrix _U<sub>S</sub>_ has full column rank over the polynomial ring (i.e., some maximal minor of _U<sub>S</sub>_ is a non-zero polynomial).

Fix \(S\subseteq E\) with |_S_|=_s_. Suppose _S_ is independent in \(M^{\vee k}\). By definition, there is a partition \(S=S_1\unknown\cdots\unknown S_k\) such that each _S<sub>i</sub>_ is independent in _M_. Since _M_ is represented by _A_, for each \(i\in[k]\) there exists a subset \(R_i\subseteq[r]\) with |_R<sub>i</sub>_|=|_S<sub>i</sub>_| such that \(\mathrm{det}(A_{R_i,S_i})\neq 0\).

Let _R_ be the set of _s_ rows in _U_ formed by taking the rows corresponding to _R<sub>i</sub>_ from the _i_-th block _AC<sub>i</sub>_ (more formally, the set of the rows in _R_ is given by \(\{(i-1)r+j:i\in[k],j\in R_i\}\)).

Consider the \(s\times s\) square submatrix _U<sub>R,S</sub>_. By the generalized Laplace expansion (Lemma 2.6), on expanding along the _k_ row blocks _R_<sub>1</sub>_,...,R<sub>k</sub>_, det(_U<sub>R,S</sub>_) can be written as:

\(\mathrm{det}(U_{R,S})=\sum_{T_1\unknown\cdots\unknown T_k=S|T_i|=|R_i|}\pm\prod_{i=1}^k\mathrm{det}\big((AC_i)_{R_i,T_i}\big).\) (4)

For each _i_ and block _T<sub>i</sub>_, we can factor out the diagonal variables:

\(\mathrm{det}\big((AC_i)_{R_i,T_i}\big)=\mathrm{det}\big(A_{R_i,T_i}\big)\prod_{e\in T_i}c_{i,e},\)

where _c<sub>i,e</sub>_ denotes the (_e,e_) diagonal entry of the matrix _C<sub>i</sub>_.

For two distinct partitions (_T_<sub>1</sub>_,...,T<sub>k</sub>_) and \((T'_1,\dots,T'_k)\), the monomials \(\prod_{i\in[k]}\prod_{e\in T_i}c_{i,e}\) and \(\prod_{i\in[k]}\prod_{e\in T_i^\prime} c_{i,e}\) are distinct (since the variable indices (_i,e_) differ). Therefore, distinct partitions contribute linearly independent monomials, and det(_U<sub>R,S</sub>_) is a non-zero polynomial if at least one partition yields a non-zero coefficient. The partition (_S_<sub>1</sub>_,...,S<sub>k</sub>_) contributes the coefficient \(\prod_{i=1}^k\mathrm{det}(A_{R_i,S_i})\neq 0\). Therefore, det(_U<sub>R,S</sub>_) is a non-zero polynomial.

Conversely, suppose the submatrix _U<sub>S</sub>_ has full column rank. Then det(_U<sub>R,S</sub>_) is a non-zero polynomial for some choice of rows \(R=R_1\unknown\cdots\unknown R_k\). By (4), there exists a partition (_T_<sub>1</sub>_,...,T<sub>k</sub>_) with \(\prod_{i=1}^k\mathrm{det}(A_{R_i,T_i})\neq 0\), implying each _T<sub>i</sub>_ is independent in _M_. Hence _S_ is independent in \(M^{\vee k}\).

