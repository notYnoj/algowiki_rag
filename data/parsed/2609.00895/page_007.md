## 2.1 Determinant

**Theorem 2.2.** _The determinant of the block Vandermonde matrix_ (19) _is_<tbc>

\(det\Lambda=\sum_{T\subseteq[2q]|T|=q}\varepsilon(T)\left(\prod_{i\in T}\alpha_i\right)\left(\prod_{j\in T^c}\beta_j\right)det(V_T)det(V_{T^c}),\) (21)

<tbc>_where, for each_<tbc>

\(T=\{t_1<\cdots<t_q\},T^c=[2q]\backslash T=\{u_1<\cdots<u_q\},\)

<tbc>_we set_<tbc>

\(\varepsilon(T):=(-1)\sum_{k=1}^q(t_k-k).\)

<tbc>_Equivalently,_<tbc>

\(det\Lambda=\sum_{T\subseteq[2q]|T|=q}\varepsilon(T)\left(\prod_{i\in T}\alpha_i\right)\left(\prod_{j\in T^c}\beta_j\right)\prod_{1\le i<j\le q}(x_{t_j}-x_{t_i})\prod_{1\le i<j\le q}(x_{u_j}-x_{u_i}).\)

<tbc>_Proof._ Applying the Cauchy-Binet formula (see, for example, \[10\]) to the factorization \(\Lambda=BC\) in (20), we have

\(det\Lambda=\sum_{S\subseteq[4q]|S|=2q}det(B_{[:,S]})det(C_{[S,:]}),\)

where _B_<sub>\[:,_S_\]</sub> denotes the submatrix of _B_ formed by all rows and the columns indexed by _S_, while _C_<sub>\[_S,_:\]</sub> denotes the submatrix of _C_ formed by the rows indexed by _S_ and all columns.

A subset \(S\subseteq[4q]\) with |_S_|=2_q_ can contribute only if _B_<sub>\[:,_S_\]</sub> is nonsingular. Each column of _B_ is a scalar multiple of a standard basis vector **e**_<sub>i</sub>_: column _i_ is \(\alpha_i\mathbf{e}_i\), while column 2_q+i_ is \(\beta_i\mathbf{e}_i\). Hence _B_<sub>\[:,_S_\]</sub> is nonsingular only if exactly one column is selected from each pair {_i,_2_q+i_}, _i_=1_,...,_2_q_.

Define<tbc>

\(T:=S\cap[2q].\)

<tbc>Since exactly one element is selected from each pair {_i,_2_q+i_}, \(i\in[2q]\), we have<tbc>

\(T^c:=[2q]\backslash T=\{i\in[2q]:2q+i\in S\}.\)

<tbc>Since the indices in the first block of _C_ precede those in the second block, the submatrix _C_<sub>\[_S,_:\]</sub> has the block-diagonal form<tbc>

\(C_{[S,:]}=\left(\begin{array}{ c c }
\left(x_i^{j-1}\right)_{1\le j\le q} & 0 \\
0 & \left(x_i^{j-1}\right)_{1\le j\le q}
\end{array}\right).\)

<tbc>If _C_<sub>\[_S,_:\]</sub> is nonsingular, then its first _q_ columns must be linearly independent. Since these columns are supported only in the first |_T_| rows, this requires \(|T|\ge q\). Likewise, the last _q_ columns are supported only in the remaining 2_q_-|_T_| rows, so their linear independence requires

\(2q-|T|\ge q.\)

Hence \(|T|\le q\), and therefore |_T_|=_q_. Thus both diagonal blocks are the square Vandermonde matrices _V<sub>T</sub>_ and _V<sub>T<sup>c</sup></sub>_.

For each _q_-element subset \(T\subseteq[2q]\), the corresponding set _S_ is uniquely determined. If<tbc>

\(T=\{t_1<\cdots<t_q\},T^c=\{u_1<\cdots<u_q\},\)

