• \(\{T_n(f)\}_n\sim_\mathrm{GLT}\kappa(x,\theta)=f(\theta)\) for any \(f\in L^1([-\pi,\pi])\);<tbc>

• \(\{D_n(a)\}_n\sim_\mathrm{GLT}\kappa(x,\theta)=a(x)\) for any \(a:[0,1]\rightarrow\mathbb{C}\) continuous a.e.;<tbc>

• \(\{Z_n\}_n\sim_\mathrm{GLT}\kappa(x,\theta)=0\) if and only if \(\{Z_n\}_n\sim_\sigma 0\), i.e., {_Z<sub>n</sub>}<sub>n</sub>_ is zero-distributed.

**GLT3.** If \(\{A_n\}_n\sim_\mathrm{GLT}\kappa\) and \(\{B_n\}_n\sim_\mathrm{GLT}\zeta\), then<tbc>

• \(\{A_n^*\}_n\sim_\mathrm{GLT}\bar{\kappa}\), where \(A_n^*\) denotes the conjugate transpose of _A<sub>n</sub>_ and \(\bar{\kappa}\) the complex conjugate of \(\kappa\);<tbc>

• \(\{\alpha A_n+\beta B_n\}_n\sim_\mathrm{GLT}\alpha\kappa+\beta\zeta\) for any \(\alpha,\beta\in\mathbb{C}\);<tbc>

• \(\{A_nB_n\}_n\sim_\mathrm{GLT}\kappa\zeta\);<tbc>

• \(\{A_n^\dagger\}_n\sim_\mathrm{GLT}\kappa^{-1}\) for any \(\kappa\) invertible a.e., where \(A_n^\dagger\) denotes the Moore-Penrose pseudoinverse of _A<sub>n</sub>_.

**GLT4.** Let \(\{A_n\}_n\sim_\mathrm{GLT}\kappa\) and \(\{B_m\}_m\sim_\mathrm{GLT}\xi\) with<tbc>

\(\kappa(x_1,\theta_1):[0,1]\times[-\pi,\pi]\rightarrow\mathbb{C},\)<br>
\(\xi(x_2,\theta_2):[0,1]\times[-\pi,\pi]\rightarrow\mathbb{C}.\)

<tbc>Then, setting _N=N(n,m_):=_nm_, it holds \(\{A_n\otimes B_m\}_N\sim_\mathrm{GLT}\kappa\otimes\xi\), where \((\kappa\otimes\xi):[0,1]^2\times[-\pi,\pi]^2\rightarrow\mathbb{C}\) is given by

\((\kappa\otimes\xi)(x_1,x_2,\theta_1,\theta_2):=\kappa(x_1,\theta_1)\xi(x_2,\theta_2),\)

i.e. we obtain a two-level GLT matrix sequence (_d_=2). Notice that the axioms in the _d_-level setting are verbatim the same with \[0,1\] and \([-\pi,\pi]\) replaced by \[0,1\]_<sup>d</sup>_ and \([-\pi,\pi]^d\), respectively.

## 3. Discretization of (1) and the space-time linear system

We divide the section into two parts, one devoted to the time discretization and one devoted to the space discretization.

### 3.1. Temporal Discretizations

Let N<sup>+</sup> denote the set of all positive integers. For \(M\in\mathbb{N}^+\), define the temporal step size \(\Delta t=T/M\) and \(t_m=m\Delta T\). Using the L1 scheme (see, e.g., \[30, 32, 36, 47\]), the temporal discretization of the fractional derivative in (1) takes the form

\(\frac{1}{\Gamma(1-\beta)}\int_0^t\left.\frac{\partial u(x,s)}{\partial s}\left(t-s\right)^{-\beta} ds\right|_{t=t_m}=\frac{1}{\Gamma(2-\beta)}\frac{1}{(\Delta t)^\beta}\left[\ell_0^{(\beta)}u(x,t_m)+\sum_{j=1}^{m-1}\ell_j^{(\beta)}u(x,t_{m-j})+\ell_m^{(\beta)}\psi(x)\right]\)<br>
\(+O(\Delta t^{2-\beta}),x\in\Omega,\) (5)

where the coefficients are given by

\(\ell_j^{(\beta)}=\left\{\begin{array}{ c c }
b_0, & j=0, \\
(b_j-b_{j-1}), & j=1,\dots,m-1, \\
-b_{m-1}, & j=m.
\end{array}\right.\)

