For sufficiently large _N_, this forces _m_=0. Thus _R<sub>E</sub>_ and _R<sub>O</sub>_ vanish at the _q_ nodes of their respective parity classes. Since<tbc>

\(degR_E,degR_O\le q-1,\)

<tbc>we have

\(R_E\equiv R_O\equiv 0.\)

Hence

\(\Delta^+=\Delta^-=0.\)

Thus the homogeneous system has only the trivial solution, and \(\Lambda_N\) is invertible for all sufficiently large _N_.

Combining Lemma 3.3 with (33), we obtain the decomposition

\(\Phi^\pm(x)=-g_q^+U^\pm(x)-g_q^-V^\pm(x)+\rho^\pm(x),\) (50)

where

\(\rho^\pm(x)=\sum_{k=0}^{q-1}\rho_k^\pm x^k,\rho_k^\pm=o(N^{k-q}),k=0,\dots,q-1.\)

In particular, the coefficient of _x<sup>q</sup>_ in \(\rho^\pm\) is exactly zero.

**Theorem 3.4.** _Suppose_<tbc>

\(f\in C^q([-1,1];\mathbb{R}^2),p,r\in C^q[-1,1],\)

<tbc>_with f_<sup>(_q_)</sup> _absolutely continuous, where_ \(q\ge 1\)_. Assume that the indices n<sub>s</sub>=n<sub>s</sub>(N_) _satisfy_ (27) _with_<tbc>

\(lim_{N\rightarrow\infty}\frac{n_s}{N}=c_s\neq 0,s=1,\dots,2q,\)

<tbc>_that the strict-balance condition_ (35) _holds, and that the limits_ \(\{c_s:s\in E\}\) _are pairwise distinct, as are_ \(\{c_s:s\in O\}\)_. Then_

\(\widetilde{g}_k^\pm=g_k^\pm-g_q^+U_k^\pm-g_q^-V_k^\pm+o(N^{k-q}),k=0,\dots,q-1,\) (51)

_where_ \(U_k^\pm\) _and_ \(V_k^\pm\) _denote the coefficients of x<sup>k</sup> in the polynomials_ \(U^\pm\) _and_ \(V^\pm\) _given by_ (38)_. In particular,_<tbc>

\(\widetilde{g}_k^\pm-g_k^\pm=O(N^{k-q}),k=0,\dots,q-1.\)

<tbc>_Proof._ By Lemma 3.3, the matrix \(\Lambda_N\) is invertible for all sufficiently large _N_, so the KEG-D system has a unique solution. Moreover, by (33),<tbc>

\(\varepsilon=max_s|\varepsilon_s|=o(N^{-q}).\)

<tbc>Hence (50) gives<tbc>

\(\Phi^\pm(x)=-g_q^+U^\pm(x)-g_q^-V^\pm(x)+\rho^\pm(x),\)

<tbc>where

\(\rho^\pm(x)=\sum_{k=0}^{q-1}\rho_k^\pm x^k,\rho_k^\pm=o(N^{k-q}).\)

<tbc>By (31), for _k_=0_,...,q_-1,

\(\Phi_k^\pm=\widetilde{g}_k^\pm-g_k^\pm.\)

Comparing the coefficients of _x<sup>k</sup>_ therefore gives (51).

Finally, by (38) and the node estimates (44),

\(U_k^\pm,V_k^\pm=O(N^{k-q}),k=0,\dots,q-1.\)

The final assertion follows.

