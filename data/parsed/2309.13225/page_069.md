**Definition B.9.** _An_ \(n\times n\) _matrix is called b_**-bounded difference** _if for all i,j,_ \(|A_{i,j}-A_{i,j+1}|\le b\) _and_ \(|A_{i,j}-A_{i+1},j|\le b\)_. If only the former holds, the matrix is_ **row bounded difference**_. If only the latter holds, the matrix is_ **column bounded difference**.

A more general requirement may be that the entries are monotone. That is, the values of each row (or column) are monotonically increasing.

**Definition B.10.** _An_ \(n\times n\) _matrix is called_ **row-monotone** _if all entries are non-negative integers bounded by O(n_) _and each row of this matrix is non-decreasing. A_ **column-monotone** _matrix is defined similarly._

**Theorem B.11.** _(\[CDXZ22\]) Let A,B be two_ \(n\times n\) _integer matrices with entries A<sub>ij</sub>,B<sub>ij</sub>=O(n). Suppose furthermore that B is either row-monotone or column-monotone. Then, there is an algo rithm **MonotoneMinPlus** computing the_ (min,+) _product C=A∗B in time_ \(\tilde{O}\left(n^\frac{3+\omega}{2}\right)\)

See Chi, Duan, Xie, and Zhang \[CDXZ22\] for a detailed proof. We also provide a proof overview in the proof of Theorem 5.1. Given a _b_-bounded difference matrix, it is easy to construct a row- monotone matrix, by adding the \(b\cdot j\) to the _j_-th column. To recover the (min,+) product, simply subtract the same constant from each column in the result. We describe this procedure as **BDtoMonotone**. By a similar argument, we can convert row-bounded difference matrices to row- monotone matrices, and column-bounded difference matrices to column-monotone matrices. We will also use the simple observation that the sub-matrix of a monotone matrix (chosen by selecting a subset of rows or columns) is a monotone matrix.

We also require the approximate (min,+) product of Zwick \[Zwi02\].

**Theorem B.12.** _Let A,B be two integer_ \(n\times n\) _matrices with non-negative entries. Let_ \(\varepsilon>0\)_. There is an algorithm **ApproximateMinPlus** that returns C in time_ \(\tilde{O}\left(n^\omega/\varepsilon\right)\) _such that for all_ \(1\le i,j\le n\),<tbc>

\((A*B)_{ij}\le C_{ij}\le(1+\varepsilon)(A*B)_{ij}\)

<tbc>_Proof._ Suppose the entries of _A,B_ are in the range \[0_,M_\]. Let the resolution _R_ be a parameter to be set later. Initialize \(C_{ij}\leftarrow\infty\) for all _i,j_. For every \(\left\lfloor logR\right\rfloor\le r\le\left\lceil logM\right\rceil\), define,

\(A_{ik}^{(r)}\leftarrow\left\{\begin{array}{ c c }
\lceil RA_{ik}/2^r\rceil & 0\le A_{ik}\le 2^r \\
\infty & \text{o/w}
\end{array}\right.\)<br>
\(B_{kj}^{(r)}\leftarrow\left\{\begin{array}{ c c }
\lceil RB_{kj}/2^r\rceil & 0\le B_{kj}\le 2^r \\
\infty & \text{o/w}
\end{array}\right.\)

and compute \(C^{(r)}\leftarrow\text{\textbf{boundedMinPlus}}(A^{(r)},B^{(r)},R)\). Update \(C_{ij}\leftarrow min\left(C_{ij},\frac{2^r}{R}C^{(r)}\right)\). The inequality \((A*B)_{ij}\le C_{ij}\) follows as _A_<sup>(_r_)</sup>_,B_<sup>(_r_)</sup> always round its entries up. Suppose \((A*B)_{ij}=A_{iq}+B_{qj}\) and without loss of generality \(A_{iq}\le B_{qj}\). Let \(1\le s\le\left\lceil logM\right\rceil\) where \(2^{s-1}\le B_{kj}\le 2^s\). If \(s\le logR\), then the _C_log_R_ computes (_A∗B)<sub>ij</sub>_ exactly. Thus, assume \(s\ge logR\). Then,

\(\frac{2^r}{R}C_{ij}^{(r)}\le\frac{2^r}{R}\left(A_{iq}^{(r)}+B_{qj}^{(r)}\right)\le A_{iq}+B_{qj}+\frac{2^{r+1}}{R}\le\left(1+\frac{4}{R}\right)(A*B)_{ij}\)

Then, if we set \(R=O\left(1/\varepsilon\right)\), we obtain the approximation error \((1+\varepsilon)\) and note that each invocation of **boundedMinPlus** requires \(\tilde{O}(n^\omega/\varepsilon)\) time.

