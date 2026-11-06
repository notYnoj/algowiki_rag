Define<tbc>

\(x_n:=\frac{1}{\lambda_n}.\)

<tbc>Then<tbc>

\(\int_{-1}^1v_n^T\mathcal{A}^kfdx=x_n(\kappa_n^{(+)}g_k^+-\kappa_n^{(-)}g_k^-)+x_n\int_{-1}^1v_n^T\mathcal{A}^{k+1}fdx.\) (11)

<tbc>Starting with _k_=0 and iterating (11) _q_ times yields<tbc>

\(c_n=P_n+F_n,\) (12)

<tbc>where<tbc>

\(P_n=x_n\sum_{k=0}^{q-1}x_n^k(\kappa_n^{(+)}g_k^+-\kappa_n^{(-)}g_k^-),F_n=\lambda_n^{-q}\int_{-1}^1v_n^T(x)\mathcal{A}^qf(x)dx.\) (13)

<tbc>If, in addition, _f_<sup>(_q_)</sup> is absolutely continuous, one more integration by parts, combined with the asymptotics (3) and the Riemann-Lebesgue theorem (cf. \[2\]), gives the sharper expansion<tbc>

\(F_n=x_n^{q+1}\left[\kappa_n^{(+)}g_q^+-\kappa_n^{(-)}g_q^-\right]+o(|n|^{-q-1}),|n|\rightarrow\infty.\) (14)

<tbc>Following \[2\] we define the exact-jumps approximation<tbc>

\(S_{q,N}(f):=P(x)+\sum_{|n|\le N}F_nv_n(x),\) (15)

\(P(x):=\sum_{k=0}^{q-1}\big[G_k(x,1,0)f_k(1)-G_k(x,-1,0)f_k(-1)\big],\)

<tbc>where<tbc>

\(G_k(x,\xi,0)=\frac{1}{k!}\partial_\lambda^kG(x,\xi,\lambda)\big|_{\lambda=0},\)

<tbc>with _G_ denoting the Green’s matrix of (1)-(2). By the spectral representation of the Green’s matrix and its derivatives, the generalized Fourier coefficient of _P_ corresponding to _v<sub>n</sub>_ is precisely _P<sub>n</sub>_, that is,<tbc>

\(\int_{-1}^1v_n^T(x)P(x)dx=P_n.\)

<tbc>Substituting (9) into (14) and using the reduced boundary values \(g_q^\pm\) defined in (8),<tbc>

\(F_n=K_0x_n^{q+1}\big[(-1)^nA+B\big]+o(|n|^{-q-1}),\) (16)

<tbc>with the _Dirac jump constants_

\(A:=g_q^+=f_{q,1}(1)\mathrm{cos}\beta-f_{q,2}(1)\mathrm{sin}\beta,B:=-g_q^-=f_{q,2}(-1)\mathrm{sin}\alpha-f_{q,1}(-1)\mathrm{cos}\alpha.\) (17)

<tbc>Hence, by (12), the generalized Fourier coefficients of _f-P_ are precisely _F<sub>n</sub>_. Consequently,<tbc>

\(R_{q,N}(f)=f-S_{q,N}(f)=\sum_{|n|>N}F_nv_n.\)

<tbc>By Parseval and (16),

\(\mathrm{lim}_{N\rightarrow\infty} N^{2q+1}\|R_{q,N}(f)\|^2=\frac{2^{2q+2}}{\pi^{2q+2}(2q+1)}(A^2+B^2),\) (18)

