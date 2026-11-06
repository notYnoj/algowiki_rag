<tbc>Fix \(q\in\mathcal{Q}\) and a triple \((i,j,K^{(\ell)})\). For a set \(S\subseteq[s+1]\), we let _r<sub>u</sub>=p<sub>u</sub>_ if \(u\unknown\in S\) and _p<sub>u</sub>q_ otherwise. We may rewrite the product<tbc>

\(\prod_p\left(C(i,j,K^{(\ell)},p)-C(i,j,K^{(\ell)},pq)\right)=\sum_{S\subseteq[s+1]}(-1)^{|S|}\prod_{u=1}^{s+1}C(i,j,K^{(\ell)},r_u).\)

<tbc>For a fixed set _S_, we will compute<tbc>

\((-1)^{|S|}\sum_{i,j,K^{(\ell)}}\prod_{u=1}^{s+1}C(i,j,K^{(\ell)},r_u).\) (3)

<tbc>To do so, we construct matrices over the ring \(\mathbb{Z}[z_1,\dots,z_{s+1}]/(z_1^{r_1}-1,\dots,z_{s+1}^{r_{s+1}}-1)\) as follows

\(X[i,(K^{(\ell)},k_1,\dots,k_{s+1})]=\prod_{u=1}^{s+1}z_u^{A[i,k_u]modr_u}\)<br>
\(Y[(K^{(\ell)},k_1,\dots,k_{s+1}),j]=\prod_{u=1}^{s+1}z_u^{B[k_u,j]modr_u}\)

The outer dimension of the matrices is \[_N_\] while the inner dimension is<tbc>

\(O\left(\frac{N}{B^{(\ell)}}\cdot(B^{(\ell)})^{s+1}\right)=O\left(\frac{NB^s}{2^{s\ell}}\right).\)

<tbc>The polynomials in the ring have degree less than _r<sub>u</sub>_ in _z<sub>u</sub>_ so that the total number of monomials is at most \(R:=\prod_{u=1}^{s+1}r_u\). Since every _r<sub>u</sub>_ is either _p<sub>u</sub>_ or _p<sub>u</sub>q_, where \(p_u\in[P,2P]\) and _q_ is \(\tilde{O}(logU)\), we have \(R=\tilde{O}\left(P^{s+1}log^{s+1}(U)\right)\). For constant _s_, ring multiplication can be performed in \(\tilde{O}(R)\) time by multivariate polynomial multiplication followed by reduction modulo \(z_u^{r_u}-1\). Thus the matrix product can be computed in time \(\tilde{O}\left(P^{s+1}log^{s+1}(U)\right)\mathsf{T}_\mathsf{MUL}\left(N,N(B^{(\ell)})^s,N\right)\). The computed entries are of the form<tbc>

\((XY)[i,j]=\sum_{K^{(\ell)},(k_1,\dots,k_{s+1})}\prod_{u=1}^{s+1}z_u^{A[i,k_u]+B[k_u,j]modr_u}.\)

<tbc>In particular, the coefficient of \(\prod_{u=1}^{s+1}z_u^{C[i,j]modr_u}\) is exactly the number of tuples (_k_<sub>1</sub>_,...,k_<sub>_s_+1</sub>) such that \(\Delta_{ik_uj}\equiv 0modr_u\) for all \(1\le u\le s+1\). In particular, summing the coefficients of \(\prod_{u=1}^{s+1}z_u^{C[i,j]modr_u}\) multiplied by (-1)<sup>|_S_|</sup> over all entries (_XY_)\[_i,j_\], we obtain exactly the desired sum in Equation (3). Iterating over _O(P_) candidate primes \(p'\), all \(q\in Q\), and all 2<sup>_s_+1</sup> choices of _S_, we compute every \(Z_{s+1}(p')\) in time

\(\tilde{O}(P^{s+2}log^{s+2}U)\mathsf{T}_\mathsf{MUL}\left(N,N(B^{(\ell)})^s,N\right),\)

as desired.

The above discussion motivates the following algorithm. Given \(\mathcal{P}_s^{(\ell)}\), compute \(Z_{s+1}(p')\) for every \(p'\in\mathcal{P}\backslash\mathcal{P}_s^{(\ell)}\), choose

\(p^*\in argmin_{p^\prime\in\mathcal{P}\backslash\mathcal{P}_s^{(\ell)}}Z_{s+1}(p'),\)

and set \(\mathcal{P}_{s+1}^{(\ell)}=\mathcal{P}_s^{(\ell)}\cup\{p^*\}\). By Lemma 3.9, summing over \(0\le s<t\) gives the time bound in Lemma 3.7. It remains to prove that the chosen primes satisfy Equation (1).

