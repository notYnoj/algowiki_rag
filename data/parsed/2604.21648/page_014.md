## 4. Optimal transfer operators.

Recall the two error propagation matrices

\(E_+^{\nu_1,\nu_2}=(I-(M^{-1}A)^+)^{\nu_2}(I-P(R^HAP)^{-1}R^HA)(I-M^{-1}A)^{\nu_1},\) (3.2)

\(E^{\nu_1,\nu_2}=(I-M^{-1}A)^{\nu_2}(I-P(R^HAP)^{-1}R^HA)(I-M^{-1}A)^{\nu_1}.\) (3.3)

The second error operator \(E^{\nu_1,\nu_2}\) has been analyzed in \[16, 31\]. For \(\nu_1=1\) and \(\nu_2=0\), we obtain the simplified operator \(E_+^{1,0}=E^{1,0}\) that has been studied in \[2, 1, 24, 39\]. Therefore, all of the following results containing convergence bounds for any of the two error operators can be interpreted as generalizations of the result in \[2, 1, 24, 39\]. In the HPD case, the convergence analysis and the construction of optimal transfer operators use the eigenvalues and eigenvectors of the symmetrized smoother matrix multiplied by the system matrix \[38, 4\]. This idea was also used for nonsymmetric AMG in \[16, 2, 1\]. For our analysis of \(E_+^{\nu_1,\nu_2}\) we follow a similar approach and use the eigenpairs of \(\widehat{M}^{-1}B\).

Theorem 4.1. _Let the smoothing assumption be satisfied. Let_<tbc>

\(\widehat{M}^{-1}B=V\mathrm{diag}(\mu_1,\dots,\mu_n)V^{-1}\)

<tbc>_be a B-unitary diagonalization of_ \(\widehat{M}^{-1}B\) _with sorted eigenvalues_ \(\mu_1\le\cdots\le\mu_n\) _and corresponding B-unitary eigenvectors_ \(V=\left[v_1\cdots v_n\right]\)_. Let_ \(\hat{P},\hat{R}\in\mathbb{C}^{n\times n_c}\) _be defined such that_<tbc>

\(\mathcal{R}(\hat{P})=\mathcal{R}(\left[v_1\cdots v_{n_c}\right])\text{\textit{and}}\mathcal{N}(\hat{R}^HA)=\mathcal{R}(\left[v_{n_c+1}\cdots v_n\right]).\)

<tbc>_For_ \((\nu_1,\nu_2)\in\{(0,1),(1,0),(1,1)\}\) _it then holds_

\(\|E_+^{\nu_1,\nu_2}(\hat{P},\hat{R})\|_B^2=\|E_+^{\nu_1,\nu_2}(P_*,\hat{R})\|_B^2=\|E_+^{\nu_1,\nu_2}(\hat{P},R_*)\|_B^2=(1-\mu_{n_c+1})^2<1.\)

_Proof._ Let the smoothing assumption be satisfied. By Proposition 3.3 the matrix \(\widehat{M}^{-1}B\) is _B_-orthogonal and thus it is _B_-unitarily diagonalizable with real eigenvalues \(\mu_1\le\cdots\le\mu_n\) and correspondingly sorted _B_-unitary eigenvector matrix _V_ . The smoothing assumption together with Theorem 3.5 imply that \(0<\mu_1\le\cdots\le\mu_n\le 1\). Due to Lemma 3.11 we know that the projection \(\Pi_A(\hat{P},\hat{R})\) is _B_-orthogonal. Similarly, by the definition of _P_<sub>∗</sub> and _R_<sub>∗</sub>, the projections \(\Pi_A(P_*,\hat{R})\) and \(\Pi_A(\hat{P},R_*)\) are also _B_- orthogonal. It holds \(\mathcal{R}(P_*)=\mathcal{R}(\hat{P})\) and by Lemma 3.11 we also have \(\mathcal{N}(R_*^HA)=\mathcal{N}(\hat{R}^HA)\). Thus

\(\Pi_A(\hat{P},\hat{R})=\Pi_A(\hat{P},R_*)=\Pi_A(P_*,\hat{R})\)

and \(E_+^{\nu_1,\nu_2}(\hat{P},\hat{R})\), \(E_+^{\nu_1,\nu_2}(P_*,\hat{R})\) and \(E_+^{\nu_1,\nu_2}(\hat{P},R_*)\) coincide.

It holds \(\hat{P}=V\left[\begin{array}{ c }
I_{n_c} \\
0
\end{array}\right]Z\) for some nonsingular \(Z\in\mathbb{C}^{n_c\times n_c}\). The definition of \(\mathcal{N}(\hat{R}^HA)\) implies that \(\hat{R}^HAV\left[\begin{array}{ c }
0 \\
I_{n_f}
\end{array}\right]=0\). The same calculation as in (3.16) then shows

\(\Pi_A(\hat{P},\hat{R})=V\left[\begin{array}{ c c }
I_{n_c} & 0 \\
0 & 0
\end{array}\right]V^{-1}.\)

Now, \(\widehat{M}^{-1}B\) and \(\Pi_A(\hat{P},\hat{R})\) are simultaneously _B_-unitarily diagonalizable and there fore they commute (cf. \[14, Theorem 1.3.21\]). Finally, for any pair \((\hat{P},\hat{R})\), \((P_*,\hat{R})\) or \((\hat{P},R_*)\) we get

\(\|E_+^{\nu_1,\nu_2}\|_B^2=\lambda_{max}\left((I-(M^{-1}A)^+)^{\nu_1}(I-\Pi_A)^+(I-M^{-1}A)^{\nu_2}(I-(M^{-1}A)^+)^{\nu_2}\right.\)<br>
\(\left.(I-\Pi_A)(I-M^{-1}A)^{\nu_1}\right)\)

