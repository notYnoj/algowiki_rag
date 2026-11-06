It remains to determine the asymptotic behavior of \(\kappa_n^{(\pm)}\). By (4) and (5),<tbc>

\(\xi_n(1)-\alpha=n\pi-\beta+O\left(\frac{1}{n}\right),\xi_n(-1)-\alpha=-\alpha.\)

<tbc>Substituting these relations into (3) gives<tbc>

\(v_n(1)=K_0(-1)^n\genfrac(){pt}{2}{cos\beta}{-sin\beta}+O\left(\frac{1}{n}\right),\)

<tbc>and<tbc>

\(v_n(-1)=K_0\genfrac(){pt}{2}{cos\alpha}{-sin\alpha}+O\left(\frac{1}{n}\right).\)

<tbc>Since the boundary-direction vectors in (6) have unit norm, taking the scalar product with the corresponding direction in the above asymptotic formulas and using (6) yields

\(\kappa_n^{(+)}=K_0(-1)^n+O\left(\frac{1}{n}\right),\kappa_n^{(-)}=K_0+O\left(\frac{1}{n}\right).\) (9)

## 1.2 Approximation with exact boundary corrections

For \(q\ge 1\), let<tbc>

\(f\in C^q([-1,1];\mathbb{R}^2),p,r\in C^q[-1,1].\)

<tbc>Define the generalized Fourier coefficients of _f_ with respect to the orthonormal Dirac eigenfunctions \(\{v_n\}_{n\in\mathbb{Z}}\) by<tbc>

\(c_n:=\langle f,v_n\rangle_{L_2}=\int_{-1}^1v_n^T(x)f(x)dx.\)

<tbc>We first derive a one-step integration-by-parts identity. Since \(\mathcal{A}v_n=\lambda_nv_n\), for any sufficiently regular vector-valued function _h_,<tbc>

\(\lambda_n\int_{-1}^1v_n^Thdx=\int_{-1}^1(\mathcal{A}v_n)^Thdx.\)

<tbc>Using \(\mathcal{A}v_n=Jv'_n-Qv_n\), _J<sup>T</sup>_=-_J_, _Q<sup>T</sup>=Q_, we obtain

\(\int_{-1}^1(\mathcal{A}v_n)^Thdx=\int_{-1}^1\left(-v'_n^TJh-v_n^TQh\right)dx\)<br>
\(=-\left[v_n^TJh\right]_{-1}^1+\int_{-1}^1v_n^T(Jh'-Qh)dx\)<br>
\(=v_n^T(-1)Jh(-1)-v_n^T(1)Jh(1)+\int_{-1}^1v_n^T\mathcal{A}hdx.\)

Therefore,

\(\int_{-1}^1v_n^Thdx=\lambda_n^{-1}\left[v_n^T(-1)Jh(-1)-v_n^T(1)Jh(1)\right]+\lambda_n^{-1}\int_{-1}^1v_n^T\mathcal{A}hdx.\) (10)

We now apply (10) with _h_=A_<sup>k</sup>f_. Using (7), (6) and the definition (8),

\(v_n^T(-1)J\mathcal{A}^kf(-1)-v_n^T(1)J\mathcal{A}^kf(1)\)<br>
\(=-v_n^T(-1)f_k(-1)+v_n^T(1)f_k(1)\)<br>
\(=-\kappa_n^{(-)}g_k^-+\kappa_n^{(+)}g_k^+.\)

