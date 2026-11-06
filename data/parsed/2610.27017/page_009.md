For the TGM, Ruge and Stüben established the following analytical framework, which reduces the overall convergence analysis of the method to the separate examination and characterization of the properties of the smoother and prolongation operators.

**Lemma 3.1.** \[24\] Let \(A=(a_{ij})\in\mathbb{R}^{n\times n}\) be a symmetric positive definite matrix, and let _G_ be the smoother for the TGM. Suppose the prolongation operator \(I_H^h\in\mathbb{R}^{n\times n_c}\) (_n<sub>c</sub>\<n_) is a column-full-rank matrix. If<br>
(1): There exists a constant \(\alpha>0\) such that

\(\|Ge^h\|_{1,A}^2\le\|e^h\|_{1,A}^2-\alpha\|e^h\|_{2,A}^2,\forall e^h\in\mathbb{R}^n.\text{(Smoothing property)}\) (3.7)

(2): There exists a constant \(\beta>0\) such that

\(min_{e^H\in\mathbb{R}^{n_c}}\|e^h-I_H^he^H\|_{0,A}^2\le\beta\|e^h\|_{1,A}^2,\forall e^h\in\mathbb{R}^n.\text{(Approximation property)}\) (3.8)

Then \(\beta\ge\alpha\) and spectral radius of _E<sub>TG</sub>_ satisfies

\(\rho(E_{TG})\le\|E_{TG}\|_{1,A}\le\sqrt{1-\frac{\alpha}{\beta}}<1.\)

Ruge and Stüben also rigorously discussed the range of the relaxation parameter \(\omega\) when the smoother _G_ is taken as the weighted Jacobi iteration method, in order to guarantee the smoothing property, namely the following lemma:

**Lemma 3.2.** \[24\] Let \(A=(a_{ij})\in\mathbb{R}^{n\times n}\) be a symmetric positive definite matrix, and let<tbc>

\(G=I_n-\omega\mathrm{diag}(A)^{-1}A.\)

<tbc>If the relaxation parameter \(\omega\) satisfies

\(\omega\in\left(0,\frac{2}{\rho(\mathrm{diag}(A)^{-1}A)}\right),\)

then there exists a constant \(\alpha>0\) such that inequality (3.7) in Lemma 3.1 holds.

We first establish a TGM analysis for _A<sub>N</sub>_, verifying that it satisfies both the smoothing property and the approximation property. Building upon this, by utilizing the perturbation property of positive diagonal matrices, we further derive the TGM analysis for \(A_N^{(m)}\).

**Theorem 3.1.** Let \(A_N=T_n^{(2)}\left(f_{\gamma_1,\gamma_2}(\theta_1,\theta_2)\right)\), where \(f_{\gamma_1,\gamma_2}(\theta_1,\theta_2)\) is given by (2.7). Let \(G=I_n-\omega\left(\mathrm{diag}(A_N)\right)^{-1}A_N\). If \(\omega\) satisfies \(0<\omega<\frac{2a_0}{\|f_{\gamma_1,\gamma_2}\|_\infty}\), where \(a_0=-2g_1^{(\gamma_1)}-\frac{2\eta_2}{\eta_1}g_1^{(\gamma_2)}\), then there exists a constant \(\alpha\) satisfying (3.7) in Lemma 3.1.

_Proof._ Since all diagonal entries of _A<sub>N</sub>_ are _a_<sub>0</sub>, we have<tbc>

\(\frac{2}{\lambda_\mathrm{max}(\mathrm{diag}(A_N)^{-1}A_N)}=\frac{2a_0}{\lambda_\mathrm{max}(A_N)}.\)

<tbc>By Lemma 2.3, we obtain<tbc>

\(\frac{2a_0}{\|f_{\gamma_1,\gamma_2}\|_\infty}\le\frac{2a_0}{\lambda_\mathrm{max}(A_N)}.\)

<tbc>Thus, from Lemma 3.2, a sufficient condition for \(\omega\) is

\(\omega\in\left(0,\frac{2a_0}{\|f_{\gamma_1,\gamma_2}\|_\infty}\right).\)

The Proof is completed.

