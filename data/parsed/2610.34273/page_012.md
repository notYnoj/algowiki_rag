The entrywise sum is different from the direct sum defined next. We retain the subscript _K_ in both operations that preserve tensor order.

**Definition 2.2** (Kronecker direct sum and product)**.** Let _k_ be a positive integer, and let \(A,B\in\mathsf{Arr}_k(\mathcal{R})\) have dimensions (_n_<sub>1</sub>_,...,n<sub>k</sub>_) and (_m_<sub>1</sub>_,...,m<sub>k</sub>_), respectively. Their _Kronecker direct sum_ \(A\oplus_KB\) has dimension (_n_<sub>1</sub>+_m_<sub>1</sub>_,...,n<sub>k</sub>+m<sub>k</sub>_) and entries<tbc>

\((A\oplus_KB)_{u_1,\dots,u_k}=\left\{\begin{array}{ c c }
A_{u_1,\dots,u_k}, & 0\le u_d<n_d\text{for}1\le d\le k, \\
B_{u_1-n_1,\dots,u_k-n_k}, & n_d\le u_d<n_d+m_d\text{for}1\le d\le k, \\
0_\mathcal{R}, & \text{otherwise,}
\end{array}\right.\)

<tbc>for \(0\le u_d<n_d+m_d\) and \(1\le d\le k\). Their _Kronecker product_ \(A\otimes_KB\) has dimension (_n_<sub>1</sub>_m_<sub>1</sub>_,...,n<sub>k</sub>m<sub>k</sub>_) and entries<tbc>

\((A\otimes_KB)_{i_1m_1+j_1,\dots,i_km_k+j_k}=A_{i_1,\dots,i_k}\cdot_\mathcal{R}B_{j_1,\dots,j_k}\)

<tbc>for \(0\le i_d<n_d\), \(0\le j_d<m_d\), and \(1\le d\le k\). For every positive integer _r_, write

\(A^{\oplus_Kr}=\oplus_Kh=1^rA,A^{\otimes_Kr}=\otimes_Kh=1^rA\)

for the repeated direct sum and repeated Kronecker product, respectively. Repeated operations on distinct arrays use their displayed order.

**Definition 2.3** (tensor construction)**.** Let _p,q_ be positive integers. For arrays \(A\in\mathsf{Arr}_p(\mathcal{R})\) and \(B\in\mathsf{Arr}_q(\mathcal{R})\) with dimensions (_n_<sub>1</sub>_,...,n<sub>p</sub>_) and (_m_<sub>1</sub>_,...,m<sub>q</sub>_), define \(A\otimes_CB\in\mathsf{Arr}_{p+q}(\mathcal{R})\) by<tbc>

\((A\otimes_CB)_{i_1,\dots,i_p,j_1,\dots,j_q}=A_{i_1,\dots,i_p}\cdot_\mathcal{R}B_{j_1,\dots,j_q}\)

<tbc>for \(0\le i_d<n_d\) and \(1\le d\le p\), and for \(0\le j_d<m_d\) and \(1\le d\le q\). For every positive integer _q_ and \(d\in[q]_0\), let \(e_d^{(q)}\) be the first-order tensor array of dimension (_q_) with entries \((e_d^{(q)})_i=1_\mathcal{R}\) if _i=d_ and 0<sub>R</sub> otherwise, for \(i\in[q]_0\). For positive integers _k,q_, define the _diagonal tensor array_

\(\mathsf{l}_k(q)=\sum_{d=0}^{q-1}\otimes_{h=1}^ke_d^{(q)}.\)

Thus dim(l_<sub>k</sub>(q_))=(_q,...,q_) and \(\mathsf{l}_k(q)=\mathsf{l}_k(1)^{\oplus_Kq}\) as arrays. The notation l_<sub>k</sub>_(0) will be defined after we introduce the tensor semiring.

**Definition 2.4** (local maps and restriction)**.** Let _k_ be a positive integer. Let \(T,S\in\mathsf{Arr}_k(\mathcal{R})\) have dimensions (_n_<sub>1</sub>_,...,n<sub>k</sub>_) and (_m_<sub>1</sub>_,...,m<sub>k</sub>_), respectively. Given matrices \(L_d\in\mathcal{R}^{m_d\times n_d}\) for \(1\le d\le k\), put _L_=(_L_<sub>1</sub>_,...,L<sub>k</sub>_) and define

\((L\cdot T)_{j_1,\dots,j_k}=\sum_{0\le i_d<n_d1\le d\le k}T_{i_1,\dots,i_k}\prod_{d=1}^k(L_d)_{j_d,i_d}\)

for \(0\le j_d<m_d\) and \(1\le d\le k\). We say that _S_ is a _restriction_ of _T_, and write \(S\unknown T\) or \(T\unknown S\), if \(S=L\cdot T\) for some such matrices. We write \(S\cong T\) if their dimensions agree and the matrices can be chosen invertible. Finally, write _S∼T_ if \(S\unknown T\) and \(T\unknown S\).

