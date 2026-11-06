**Lemma 3.5.** Let \(A=(a_{ij})\in\mathbb{R}^{n\times n}\) be a symmetric positive definite matrix, and there exists a constant \(\beta>0\) such that for any \(e^h\in\mathbb{R}^n\),<tbc>

\(min_{e^H\in\mathbb{R}^{n_c}}\|e^h-I_H^he^H\|_{0,A}^2\le\beta\|e^h\|_{1,A}^2.\)

<tbc>Define _B=A+D_, where \(D=(d_{ij})\in\mathbb{R}^{n\times n}\) is a nonnegative diagonal matrix. Then for any \(e^h\in\mathbb{R}^n\), we have

\(min_{e^H\in\mathbb{R}^{n_c}}\|e^h-I_H^he^H\|_{0,B}^2\le\beta\left(1+\frac{d_\mathrm{max}}{a_\mathrm{min}}\right)\|e^h\|_{1,B}^2,\)

where _d_<sub>max</sub>=max{_d_<sub>11</sub>_,...,d<sub>nn</sub>_} and _a_<sub>min</sub>=min{_a_<sub>11</sub>_,...,a<sub>nn</sub>_}.

_Proof._ For any \(e^h\in\mathbb{R}^n\) and \(e^H\in\mathbb{R}^{n_c}\), we have

\(\|e^h-I_H^he^H\|_{0,B}^2=\|e^h-I_H^he^H\|_{0,A}^2+\|e^h-I_H^he^H\|_{0,D}^2\)<br>
\(\le\left(1+\frac{d_\mathrm{max}}{a_\mathrm{min}}\right)\|e^h-I_H^he^H\|_{0,A}^2.\)

Now, suppose that for a fixed \(e^h\in\mathbb{R}^n\), _e<sup>H</sup>(h_) is chosen such that<tbc>

\(min_{e^H\in\mathbb{R}^{n_c}}\|e^h-I_H^he^H\|_{0,A}^2=\|e^h-I_H^he^H(h)\|_{0,A}^2.\)

<tbc>Then, for any \(e^h\in\mathbb{R}^n\)

\(min_{e^H\in\mathbb{R}^{n_c}}\|e^h-I_H^he^H\|_{0,B}^2\)<br>
\(\le\|e^h-I_H^he^H(h)\|_{0,B}^2\)<br>
\(\le\left(1+\frac{d_\mathrm{max}}{a_\mathrm{min}}\right)\|e^h-I_H^he^H(h)\|_{0,A}^2\)<br>
\(\le\left(1+\frac{d_\mathrm{max}}{a_\mathrm{min}}\right)\beta\|e^h\|_{1,A}^2\)<br>
\(\le\left(1+\frac{d_\mathrm{max}}{a_\mathrm{min}}\right)\beta\|e^h\|_{1,B}^2.\)

The proof is completed.

The convergence of the TGM for _A<sub>N</sub>_ has been analyzed previously. For the case \(d(x,y,t)\ge 0\), although \(A_N^{(m)}\) may no longer be a BTTB matrix, the coefficient matrix at each time level can be expressed as \(A_N^{(m)}=A_N+\frac{1}{\eta_1}D^{(m)}\), and it follows from Lemma 3.4 that

**Corollary 3.1.** Let \(A_N^{(m)}\) be given by (2.4) . If the coefficient function _d(x,y,t_) is nonnegative and uniformly bounded, then there exists a constant \(\alpha\) independent of the time _m_ such that the weighted Jacobi smoother _G_ satisfies (3.7).

_Proof._ Since \(\frac{1}{\eta_1}D^{(m)}\) is nonnegative for any \(1\le m\le M\). By Lemma (3.4), we have<tbc>

\(\rho(\mathrm{diag}(A_N^{(m)})^{-1}A_N^{(m)})\le\rho(\mathrm{diag}(A_N)^{-1}A_N).\)

<tbc>Moreover,

\(0<\frac{2a_0}{\|f_{\gamma_1,\gamma_2}\|_\infty}\le\frac{2}{\rho(\mathrm{diag}(A_N)^{-1}A_N)}\le\frac{2}{\rho(\mathrm{diag}(A_N^{(m)})^{-1}A_N^{(m)})},\)

and \(\frac{2a_0}{\|f_{\gamma_1,\gamma_2}\|}\) is independent of the time level _m_, there always exists an \(\alpha\) independent of _m_ such that (3.7) holds. The Proof is completed.

