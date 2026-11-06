(_i)_ \([\lambda_n-t_0\|E\|_2,\lambda_{k+1}+t_0\|E\|_2]\) _contains the nonzero spectrum of_ \(\widehat{A}(t)\);<tbc>

_(ii)_ \([\lambda_n-t_0\|E\|_2,\lambda_k+t_0\|E\|_2]\) _contains the spectrum of_ \(A^\theta(t)\)_, for every_ \(\theta\in\Theta_\delta\).

_Proof._ First, let us present the projected matrix as a Schur complement. Since \([S_k,\overline{S_k}]\) is an orthonormal basis of R_<sup>n</sup>_, write _A(t_) in this basis as \(M_{11}:=S_k^\top A(t)S_k\), \(M_{12}:=S_k^\top A(t)\overline{S_k}\), and \(M_{22}:=\overline{S_k^\top} A(t)\overline{S_k}\). Using _A(t)S<sub>k</sub>=S<sub>k</sub>M_<sub>11</sub>+\(\overline{S_k}M_{12}^\top\) and \(S_k^\top A(t)=M_{11}S_k^\top+M_{12}\overline{S_k^\top}\), the matrix \(\widehat{A}(t)=A(t)-A(t)S_kM_{11}^{-1}S_k^\top A(t)\) expands to<tbc>

\(\widehat{A}(t)=A(t)-\big(S_kM_{11}+\overline{S_k}M_{12}^\top\big)M_{11}^{-1}\big(M_{11}S_k^\top+M_{12}\overline{S_k^\top}\big)=\overline{S_k}\big(M_{22}-M_{12}^\top M_{11}^{-1}M_{12}\big)\overline{S_k^\top}.\)

<tbc>Since \(\overline{S_k}\) has orthonormal columns, the nonzero spectrum of \(\widehat{A}(t)\) therefore coincides with the spectrum of \(M_{22}-M_{12}^\top M_{11}^{-1}M_{12}\), and it suffices to prove

(3.24) \(\overline{\Lambda_k}-t_0\|E\|_2I_{n-k}\unknown M_{22}-M_{12}^\top M_{11}^{-1}M_{12}\unknown\overline{\Lambda_k}+t_0\|E\|_2I_{n-k}.\)

We use the following characterization of the Schur complement: For any \(v\in\mathbb{R}^{n-k}\),<tbc>

\(v^\top(M_{22}-M_{12}^\top M_{11}^{-1}M_{12})v=min_{z\in\mathbb{R}^k}(S_kz+\overline{S_k}v)^\top A(t)(S_kz+\overline{S_k}v).\)

<tbc>Indeed, expanding the quadratic form gives

(3.25) \((S_kz+\overline{S_k}v)^\top A(t)(S_kz+\overline{S_k}v)=z^\top M_{11}z+2z^\top M_{12}v+v^\top M_{22}v,\)

and, since _M_<sub>11</sub> is SPD, the minimum of (3.25) with respect to _z_ is attained at \(z=-M_{11}^{-1}M_{12}v\); substituting back gives \(v^\top(M_{22}-M_{12}^\top M_{11}^{-1}M_{12})v\), as claimed.

We now prove the two bounds in (3.24). Since \(0\le t\le t_0\), we have \(A-t_0\|E\|_2I_n\unknown A(t)\unknown A+t_0\|E\|_2I_n\). For the lower bound, this and the characterization above give, for any \(v\in\mathbb{R}^{n-k}\),

\(v^\top(M_{22}-M_{12}^\top M_{11}^{-1}M_{12})v\ge min_{z\in\mathbb{R}^k}(S_kz+\overline{S_k}v)^\top(A-t_0\|E\|_2I_n)(S_kz+\overline{S_k}v)\)<br>
\(=min_{z\in\mathbb{R}^k}\big\{z^\top(\Lambda_k-t_0\|E\|_2I_k)z+v^\top(\overline{\Lambda_k}-t_0\|E\|_2I_{n-k})v\big\}\)<br>
\(=v^\top(\overline{\Lambda_k}-t_0\|E\|_2I_{n-k})v,\)

where we used \(S_k^\top A\overline{S_k}=0\) and \(S_k^\top\overline{S_k}=0\), and where the minimum is attained at _z_=0 because \(\Lambda_k-t_0\|E\|_2I_k\succ 0\). For the upper bound, evaluating (3.25) at _z_=0 and using \(A(t)\unknown A+t_0\|E\|_2I_n\) gives, for any \(v\in\mathbb{R}^{n-k}\),

\(v^\top(M_{22}-M_{12}^\top M_{11}^{-1}M_{12})v\le v^\top\overline{S_k^\top} A(t)\overline{S_k}v\le v^\top(\overline{\Lambda_k}+t_0\|E\|_2I_{n-k})v,\)

where we used \(\overline{S_k^\top} A\overline{S_k}=\overline{\Lambda_k}\). Together, the two bounds establish (3.24), and hence that the nonzero spectrum of \(\widehat{A}(t)\) lies in \([\lambda_n-t_0\|E\|_2,\lambda_{k+1}+t_0\|E\|_2]\).

For \(\theta\in\Theta_\delta\), the eigenvalues of \(A^\theta(0)\) lie in \([\lambda_n,\lambda_k]\), and \(\|U^\theta\|_2\le 1\). Hence

\(\|A^\theta(t)-A^\theta(0)\|_2=t\|U^\theta EU^\theta\|_2\le t\|E\|_2\le t_0\|E\|_2.\)

By Weyl’s inequality we prove (ii). □

We now state our main result: a second-order comparison of the energy-norm errors of PCG with \(U^\theta\) and deflated CG, with an explicit remainder.

