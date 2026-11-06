<tbc>Theorem 4.1 (Structured representation for _Q<sub>m</sub>_). _For every_ \(1\le m\le p\),

\(G_m^*G_m+K_m^*K_m=I_m,Q_m=\left[\begin{array}{ c }
G_m \\
G_mK_m \\
\vdots \\
G_mK_m^{m-1}
\end{array}\right],\)

_Proof._ Let \(Q_m^{(i)}\) denote the _i_th \(n\times m\) block row of _Q<sub>m</sub>_, so that \(Q_m^{(1)}=G_m\). The identity \((J_m\otimes I_n)Q_m=Q_mK_m\) gives

\(Q_m^{(i+1)}=Q_m^{(i)}K_m,i=1,\dots,m-1.\)

Thus \(Q_m^{(i)}=G_mK_m^{i-1}\), proving the stated representation of _Q<sub>m</sub>_.

Since \(Q_m^*Q_m=I_m\) and \(J_m^*J_m=I_m-e_1e_1^*\), we have

\(K_m^*K_m=(Q_mK_m)^*(Q_mK_m)=\big((J_m\otimes I_n)Q_m\big)^*\big((J_m\otimes I_n)Q_m\big)\)<br>
\(=Q_m^*(J_m^*J_m\otimes I_n)Q_m=I_m-G_m^*G_m.\)

This proves the remaining identity. □

For computation, _G<sub>m</sub>_ and _K<sub>m</sub>_ can be obtained directly from the QR factor \(\widehat{Q}_{m-1}\) in (3.7):

\(G_m=[q_{1,1},\widehat{Q}_{m-1}(1:n,:)],\) (4.1)

\(K_m=\left[\begin{array}{ c c }
0_{(m-1)\times 1} & \widehat{Q}_{m-1}(n+1:n+m-1,:) \\
0 & 0_{1\times(m-1)}
\end{array}\right].\) (4.2)

The first formula follows from (3.8). Identity (3.9) and direct multiplication yield

\(K_m=R_mJ_mR_m^{-1}=\left[\begin{array}{ c }
R_{m-1} \\
0_{1\times(m-1)}
\end{array}\right]\left[0_{(m-1)\times 1}R_{m-1}^{-1}\widehat{R}_{m-1}^{-1}\right]=\left[\begin{array}{ c c }
0_{(m-1)\times 1} & \widehat{R}_{m-1}^{-1} \\
0 & 0_{1\times(m-1)}
\end{array}\right].\)

The lower block of (3.7) gives \(\widehat{Q}_{m-1}(n+1:n+m-1,:)\widehat{R}_{m-1}=I_{m-1}\), which establishes the stated formula for _K<sub>m</sub>_.

**4.2. Computing the recovery vector.**

_Hypothesis_ 4.2. The matrix-valued function _A(s_) is available in the split form

(4.3) \(A(s)=\sum_{\ell=0}^{d-1}f_\ell(s)M_\ell,\)

where _d_ is fixed and small, \(f_0(s)\equiv 1\) and each \(f_\ell\) is analytic at _s_=0, and \(\mathrm{nnz}(M_\ell)=\mathcal{O}(n)\).

Write \(f_\ell(s)=\sum_{j\ge 0}f_{\ell,j}s^j\). Comparing (4.3) with the Taylor expansion (2.1) gives

(4.4) \(A_j=\sum_{\ell=1}^{d-1}f_{\ell,j}M_\ell,j\ge 1.\)

The split form of _A(s_) now allows us to express the recovery vector _u_<sub>_m_+1</sub> simply using _G<sub>m</sub>_ and matrix functions of _K<sub>m</sub>_.

