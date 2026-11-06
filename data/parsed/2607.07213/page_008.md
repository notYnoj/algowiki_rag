### 4.3 Cayley-Hamilton Structure of the Evolution Operator

By the Cayley-Hamilton theorem, _H_<sub>f</sub> satisfies its own characteristic polynomial, so any analytic function _f(H_<sub>f</sub>) is a polynomial of degree at most two,

\(f(H_\mathrm{f})=c_0\mathbf{1}+c_1H_\mathrm{f}+c_2H_\mathrm{f}^2,\) (13)

with \(f(\omega_i)=c_0+c_1\omega_i+c_2\omega_i^2\) for the three eigenvalues \(\omega_i\) of _H_<sub>f</sub> (energy units). These are related to the rescaled mass-squared eigenvalues \(\lambda_i\) of \(\Lambda=2EH_\mathrm{f}\) used from Section 5 onward by \(\omega_i=\lambda_i/(2E)\). Applied to \(f(\omega)=e^{-i\omega L}\),<tbc>

\(S(L)=c_0(L)\mathbf{1}+c_1(L)H_\mathrm{f}+c_2(L)H_\mathrm{f}^2,\) (14)

<tbc>with the coefficients fixed by the Vandermonde system

\(\left(\begin{array}{ c c c }
1 & \omega_1 & \omega_1^2 \\
1 & \omega_2 & \omega_2^2 \\
1 & \omega_3 & \omega_3^2
\end{array}\right)\left(\begin{array}{ c }
c_0 \\
c_1 \\
c_2
\end{array}\right)=\left(\begin{array}{ c }
e^{-i\omega_1L} \\
e^{-i\omega_2L} \\
e^{-i\omega_3L}
\end{array}\right),\omega_i=\lambda_i/(2E).\) (15)

The three-flavor amplitude in constant-density matter is thus determined entirely by the three eigenvalues. While the Cayley-Hamilton property is implicit in the matrix- exponential literature, the explicit Vandermonde system (15) connecting eigenvalues to evolution-operator coefficients is not, to our knowledge, written out in this form in prior neutrino references.

## 5 Exact Hamiltonian Diagonalization

### 5.1 Exact Cubic Eigenvalue Solution

It is convenient to diagonalize the rescaled matrix \(\Lambda\equiv 2EH_\mathrm{f}\), whose coefficients _A_, _B_, _C_ (Eqs. 10-12) carry dimensions of mass-squared; we denote its eigenvalues \(\lambda_i\) (units eV<sup>2</sup>), so that in vacuum \(\lambda_i\rightarrow m_i^2-m_1^2\) and the eigenvalue differences reduce to \(\Delta\lambda_{ij}\rightarrow\Delta m_{ij}^2\). The physical phase entering the evolution operator and the oscillation probabilities is \(\lambda_iL/(2E)\); accordingly the oscillation probabilities of Section 5.4 are written with the combination \(\Delta\lambda_{ij}/(2E)\), which is dimensionally an inverse length. Substituting \(\lambda=\mu+A/3\) gives the depressed cubic \(\mu^3+p\mu+q=0\) with _p=B-A_<sup>2</sup>/3 and _q_=-2_A_<sup>3</sup>/27+_AB/_3-_C_. Since \(\Lambda\) is Hermitian, all roots are real, the discriminant \(\Delta_\mathrm{cubic}=-4p^3-27q^2\ge 0\), and _p\<_0. The three real roots follow from Cardano’s trigonometric method \[20, 56\],

\(\lambda_k=\frac{A}{3}+\frac{2}{3}\sqrt{A^2-3B}\mathrm{cos}\left(\frac{1}{3}\mathrm{arccos}\left(\frac{2A^3-9AB+27C}{2(A^2-3B)^{3/2}}\right)-\frac{2\pi k}{3}\right),k=0,1,2,\) (16)

the Zaglauer-Schwarzer result \[21\]. The cosine (not hyperbolic) form is the correct branch for a Hermitian matrix with three real roots.

### 5.2 DMP Approximation and Its Accuracy

Defining \(x\equiv a/\Delta m_{ee}^2\), DMP \[47\] approximate the largest eigenvalue by

\(\lambda_3\approx\Delta m_{31}^2+\frac{\Delta m_{ee}^2}{2}\left(x-1+\sqrt{(1-x)^2+4xs_{13}^2}\right).\) (17)

