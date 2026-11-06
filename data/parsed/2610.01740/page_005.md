\(=\left[\begin{array}{ c }
0_{n\times m} \\
Q_m
\end{array}\right]\left[\begin{array}{ c c }
\frac{\|a_1\|_2}{\|z\|_2}e_1 & R_m(:,2:m)R_{m-1}^{-1} \\
\frac{\|a_1\|_2}{\|z\|_2}e_1 & R_m(1:m,2:m)R_{m-1}^{-1}
\end{array}\right].\)

This proves (3.3). Finally,

\([I_n,0,\dots,0]\mathcal{L}_0^{-1}\mathcal{U}_m=\left[\frac{a_1}{\|z\|_2},-A_0^{-1}[A_1,\dots,A_{m-1}]Q_{m-1}\right]\)<br>
\(=\left[\frac{a_1}{\|z\|_2},-A_0^{-1}[A_1,\dots,A_{m-1}]V_{m-1}R_{m-1}^{-1}\right]\)<br>
\(=\left[\frac{a_1}{\|z\|_2},[a_2,\dots,a_m]R_{m-1}^{-1}\right].\)

Multiplying by _y<sub>s</sub>_ proves (3.4). □

Define

\(S_m:=R_m(1:m,2:m)R_{m-1}^{-1}\in\mathbb{C}^{m\times(m-1)}.\)

From Lemma 3.1, solution recovery requires only _S<sub>m</sub>_ and the _n_-dimensional recovery vectors \([u_2,\dots,u_m]:=[a_2,\dots,a_m]R_{m-1}^{-1}\). Together with \(a_1/\|z\|_2\), these vectors form the recovery basis in (3.4). Computing full Arnoldi vectors is unnecessary.

Let _q<sub>i,m</sub>_:=_Q<sub>m</sub>_((_i_-1)_n_+1:_in,m_), _i_=1_,...,m_, which is the _i_-th block row, _m_-th column of _Q<sub>m</sub>_. In the proof of the above lemma, we have seen that<tbc>

\([a_2,\dots,a_m]R_{m-1}^{-1}=-A_0^{-1}[A_1,\dots,A_{m-1}]Q_{m-1}.\)

<tbc>By taking the last column, we can derive that

(3.5) \(u_m=-A_0^{-1}\sum_{i=1}^{m-1}A_iq_{i,m-1},\)

which can be an equivalent definition of _u<sub>m</sub>_.

**3.2. Incremental recurrences.** We derive recurrences for _q_<sub>1_,m_</sub>, _S<sub>m</sub>_, and _u<sub>m</sub>_. Let

\(g_1=\left[\begin{array}{ c }
a_1/\|a_1\| \\
0_{m-1}
\end{array}\right],P_1=I-\frac{a_1a_1^*}{a_1^*a_1},\)

where _P_<sub>1</sub> is a projection operator. Assume that all quantities through step _m_-1 are available.

_Updating q_<sub>1_,m_</sub> _and S<sub>m</sub>._ By the block Toeplitz structure of _V<sub>m</sub>_, the definition \([u_2,\dots,u_m]=[a_2,\dots,a_m]R_{m-1}^{-1}\), and _V_<sub>_m_-1</sub>=_Q_<sub>_m_-1</sub>_R_<sub>_m_-1</sub>, we have

(3.6) \(V_m=\left[\begin{array}{ c c }
a_1 & [a_2,\dots,a_m] \\
0 & V_{m-1}
\end{array}\right]\)<br>
\(=\left[\begin{array}{ c c }
I_n & 0 \\
0 & Q_{m-1}
\end{array}\right]\left[\begin{array}{ c c }
a_1 & [u_2,\dots,u_m] \\
0 & I_{m-1}
\end{array}\right]\left[\begin{array}{ c c }
1 & 0 \\
0 & R_{m-1}
\end{array}\right].\)

The leftmost factor has orthonormal columns, so only the middle matrix requires factorization.

