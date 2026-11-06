<tbc>We compute the thin QR factorization

(3.7) \(\left[\begin{array}{ c }
P_1[u_2,\dots,u_m] \\
I_{m-1}
\end{array}\right]=\widehat{Q}_{m-1}\widehat{R}_{m-1},\)

which can be updated by incremental Gram-Schmidt, at a cost of O(_nm+m_<sup>2</sup>) arithmetic operations at step _m_. Then the middle factor in (3.6) satisfies

\(\left[\begin{array}{ c c }
a_1 & [u_2,\dots,u_m] \\
0 & I_{m-1}
\end{array}\right]=[g_1,\widehat{Q}_{m-1}]\left[\begin{array}{ c c }
\|a_1\| & a_1^*[u_2,\dots,u_m]/\|a_1\|_2 \\
0 & \widehat{R}_{m-1}
\end{array}\right].\)

Substituting this QR factorization into (3.6) yields

(3.8) \(Q_m=\left[\begin{array}{ c c }
I_n & 0 \\
0 & Q_{m-1}
\end{array}\right][g_1,\widehat{Q}_{m-1}],\)

(3.9) \(R_m=\left[\begin{array}{ c c }
\|a_1\| & \left(a_1^*[u_2,\dots,u_m]/\|a_1\|\right)R_{m-1} \\
0 & \widehat{R}_{m-1}R_{m-1}
\end{array}\right].\)

From the first _n_ rows of (3.8), we obtain

(3.10) \(q_{1,1}=a_1/\|a_1\|,[q_{1,2},\dots,q_{1,m}]=\widehat{Q}_{m-1}(1:n,:).\)

On the other hand, applying (3.9) and \(S_m=R_m(:,2:m)R_{m-1}^{-1}\) gives

(3.11) \(S_m=\left[\begin{array}{ c }
a_1^*[u_2,\dots,u_m]/\|a_1\| \\
\widehat{R}_{m-1}
\end{array}\right].\)

Thus, we have obtained _q_<sub>1_,m_</sub> and _S<sub>m</sub>_ within O(_nm+m_<sup>2</sup>) arithmetic operations at step _m_.

_Updating the recovery vector u_<sub>_m_+1</sub>. Notice that<tbc>

\(\left[\begin{array}{ c c c c }
a_2 & \cdots & a_{m+1} \\
a_1 & \cdots & a_m
\end{array}\right]=\left[\begin{array}{ c c c c }
u_2 & \cdots & u_{m+1} \\
q_{1,1} & \cdots & q_{1,m}
\end{array}\right]R_m.\)

<tbc>Let \(t_m=R_me_m\in\mathbb{C}^m\), then

\(a_{m+1}=[u_2,\dots,u_{m+1}]t_m,\)<br>
\(a_m=[q_{1,1},\dots,q_{1,m}]t_m.\)

If we can compute _t<sub>m</sub>_, then we can compute _u_<sub>_m_+1</sub> from \[_u_<sub>2</sub>_,...,u_<sub>_m_+1</sub>\]_t<sub>m</sub>=a_<sub>_m_+1</sub>, with O(_nm_) arithmetic cost. By

\(S_mt_{m-1}=R_m(:,2:m)R_{m-1}^{-1}R_{m-1}e_{m-1}=R_m(:,2:m)e_{m-1}=t_m,\)

we can get the recurrence for _t<sub>m</sub>_:

\(t_1=\|a_1\|,t_m=S_mt_{m-1},m\ge 2.\)

Thus, we have derived incremental recurrences for _q_<sub>1_,m_</sub>, _S<sub>m</sub>_, and _u<sub>m</sub>_ that require only O(_nm+m_<sup>2</sup>) arithmetic operations at step _m_. The resulting algorithm is summarized in Algorithm 3.1.

Let _F_<sub>LU</sub>(_n_) denote the cost of factoring _A_<sub>0</sub> and _S_<sub>LU</sub>(_n_) the cost of one pair of triangular solves with the stored factors. If nnz(_A<sub>j</sub>_)=O(_n_), the construction

