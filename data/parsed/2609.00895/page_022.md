_Proof._ Since \(\widetilde{F}_n\) is the generalized Fourier coefficient of \(f-\widetilde{P}\), we have<tbc>

\(\widetilde{R}_{q,N}(f)=\sum_{|n|>N}\widetilde{F}_nv_n.\)

<tbc>Hence, by Parseval,<tbc>

\(\|\widetilde{R}_{q,N}(f)\|^2=\sum_{|n|>N}|\widetilde{F}_n|^2.\)

<tbc>Since<tbc>

\(\widetilde{F}_n=F_n+(P_n-\widetilde{P}_n),\)

<tbc>we first compute the second term. By the definitions of _P<sub>n</sub>_ and \(\widetilde{P}_n\),

\(P_n-\widetilde{P}_n=-x_n[\kappa_n^{(+)}\Delta^+(x_n)-\kappa_n^{(-)}\Delta^-(x_n)]\)<br>
\(=-x_n[\kappa_n^{(+)}\Phi^+(x_n)-\kappa_n^{(-)}\Phi^-(x_n)]\)<br>
\(-x_n^{q+1}[\kappa_n^{(+)}g_q^+-\kappa_n^{(-)}g_q^-],\)

where we used (31). Define<tbc>

\(\mathcal{Q}_n:=\kappa_n^{(+)}\Phi^+(x_n)-\kappa_n^{(-)}\Phi^-(x_n).\)

<tbc>Then (14) gives<tbc>

\(P_n-\widetilde{P}_n=-x_n\mathcal{Q}_n-F_n+r_n,|n|>N,\)

<tbc>where<tbc>

\(r_n=o(|n|^{-q-1})\)

<tbc>uniformly for |_n|\>N_. Therefore<tbc>

\(\widetilde{F}_n=-x_n\mathcal{Q}_n+r_n.\) (53)

<tbc>By (50),

\(\mathcal{Q}_n=-g_q^+[\kappa_n^{(+)}U^+(x_n)-\kappa_n^{(-)}U^-(x_n)]\)<br>
\(-g_q^-[\kappa_n^{(+)}V^+(x_n)-\kappa_n^{(-)}V^-(x_n)]\)<br>
\(+\kappa_n^{(+)}\rho^+(x_n)-\kappa_n^{(-)}\rho^-(x_n).\)

<tbc>Since<tbc>

\(\rho^\pm(x)=\sum_{k=0}^{q-1}\rho_k^\pm x^k,\rho_k^\pm=o(N^{k-q}),\)

<tbc>and |_x<sub>n</sub>_|=_O(N_<sup>-1</sup>) uniformly for |_n|\>N_, it follows that

\(\rho^\pm(x_n)=o(N^{-q}),\)

uniformly for |_n|\>N_ as \(N\rightarrow\infty\).

Using (34) and (38), we now distinguish the parity of the tail index _n_. For |_n|\>N_, we have<tbc>

\(U^\pm(x_n),V^\pm(x_n)=O(N^{-q}).\)

<tbc>Hence, if _n_ is even,<tbc>

\(\kappa_n^{(+)}U^+(x_n)-\kappa_n^{(-)}U^-(x_n)=K_0\Pi_E(x_n)+o(N^{-q}),\)

<tbc>and<tbc>

\(\kappa_n^{(+)}V^+(x_n)-\kappa_n^{(-)}V^-(x_n)=-K_0\Pi_E(x_n)+o(N^{-q}).\)

