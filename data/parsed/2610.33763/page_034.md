## 3.1.1 Relationship between the Toeplitz matrix and its generating function

By constructing a Toeplitz matrix _T<sub>n</sub>(f_) from a given matrix-valued function _f_ in \(L^1([-\pi,\pi]^d)\), we are essentially creating a map that takes functions and produces matrices:

\(T_n(\cdot):L^1([-\pi,\pi]^d,\mathbb{C}^{r\times r})\rightarrow\mathbb{C}^{N(n)r\times N(n)r}\)

for any fixed \(n\in\mathbb{N}^d\) and \(r\in\mathbb{N}\). The properties of the function _f_ are closely related to those of the Toeplitz matrix. To start, the operator \(T_n(\cdot)\) is linear. This follows directly from the linearity of the Fourier coefficient operation.

**Proposition 3.1** _For any_ \(\alpha,\beta\in\mathbb{C}\) _and_ \(f,g\in L^1([-\pi,\pi]^d,\mathbb{C}^{r\times r})\)_, it holds that_<tbc>

\(T_n(\alpha f+\beta g)=\alpha T_n(f)+\beta T_n(g).\)

<tbc>_Moreover, further results follow from the identities_

\((\widehat{f(-\theta)})_k=\hat{f}_{-k}\text{\textit{and}}\widehat{(f^*)}_k=\big(\hat{f}_{-k}\big)^*,\text{\textit{for all}}k\in\mathbb{Z}^d,\)

_where_ \(f^*(\theta):=\overline{f(\theta)^\top}\) _denotes the conjugate transpose of f._

**Proposition 3.2** _For any_ \(f\in L^1([-\pi,\pi]^d,\mathbb{C}^{r\times r})\)_, the following properties hold:_

\(T_n(f(\theta))^\top=T_n\big(f(-\theta)^\top\big),\)<br>
\(T_n(f)^*=T_n(f^*),\)

_where T<sub>n</sub>(f_)<sup>∗</sup> _is the Hermitian (conjugate transpose) of T<sub>n</sub>(f)._

In particular, if _f_ is Hermitian a.e., that is, \(f(\theta)=f(\theta)^*\) for almost every \(\theta\), then _T<sub>n</sub>(f_) is Hermitian, so that Hermitian matrix-valued generating functions produce block Toeplitz matrices with real eigenvalues. More precisely, the spectrum of _T<sub>n</sub>(f_) is contained within the essential infimum of the smallest eigenvalue of _f_ and the essential supremum of its largest eigenvalue.

**Theorem 3.1** _Given_ \(f\in L^1([-\pi,\pi]^d,\mathbb{C}^{r\times r})\)_, Hermitian a.e., let_<tbc>

\(m_f:=\mathrm{essinf}_\theta\lambda_{\mathrm{min}}\big(f(\theta)\big),M_f:=\mathrm{esssup}_\theta\lambda_{\mathrm{max}}\big(f(\theta)\big).\)

<tbc>_Then, for any_ \(n\in\mathbb{N}^d\)_, it holds that_<tbc>

\(\lambda_j\big(T_n(f)\big)\in[m_f,M_f],\forall j=1,\dots,N(n)r.\)

<tbc>_If, in addition, m<sub>f</sub>\<M<sub>f</sub>, or equivalently f is not constant a.e., then it holds_

\(\lambda_j\big(T_n(f)\big)\in(m_f,M_f),\forall j=1,\dots,N(n)r.\)

A valuable addition to this theorem is the following result concerning the extreme eigenvalues of _T<sub>n</sub>(f_): for any fixed \(j\ge 1\) and as \(n\rightarrow\infty\), the _j_ smallest eigenvalues of _T<sub>n</sub>(f_) converge to _m<sub>f</sub>_, while the _j_ largest eigenvalues converge to _M<sub>f</sub>_.

