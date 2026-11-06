**Definition 2.1** _Let_ {_A<sub>n</sub>}<sub>n</sub> be a matrix sequence, with A<sub>n</sub> of size d<sub>n</sub>, and let_ \(\psi:D\subset\mathbb{R}^t\rightarrow\mathbb{C}^{r\times r}\) _be a measurable function defined on a set D with_ \(0<\mu_t(D)<\infty\).

• _We say that_ {_A<sub>n</sub>}<sub>n</sub> has an (asymptotic) singular value distribution described by_ \(\psi\)_, and we write_ \(\{A_n\}_n\sim_\sigma\psi\)_, if_<tbc>

<tbc>\(\mathrm{lim}_{n\rightarrow\infty}\frac{1}{d_n}\sum_{i=1}^{d_n}F(\sigma_i(A_n))=\frac{1}{\mu_t(D)}\int_D\frac{1}{r}\sum_{i=1}^rF(\sigma_i(\psi(x)))dx,\forall F\in C_c(\mathbb{R}).\)<tbc>

• _We say that_ {_A<sub>n</sub>}<sub>n</sub> has an (asymptotic) spectral (or eigenvalue) distribution described by_ \(\psi\)_, and we write_ \(\{A_n\}_n\sim_\lambda\psi\)_, if_<tbc>

<tbc>\(\mathrm{lim}_{n\rightarrow\infty}\frac{1}{d_n}\sum_{i=1}^{d_n}F(\lambda_i(A_n))=\frac{1}{\mu_t(D)}\int_D\frac{1}{r}\sum_{i=1}^rF(\lambda_i(\psi(x)))dx,\forall F\in C_c(\mathbb{C}).\)<tbc>

• _If_ \(\psi\) _describes both the singular value and eigenvalue distribution of_ {_A<sub>n</sub>}<sub>n</sub>, we write_ \(\{A_n\}_n\sim_{\sigma,\lambda}\psi\).

_In this case, the function_ \(\psi\) _is referred to as the eigenvalue (or spectral) symbol of_ {_A<sub>n</sub>}<sub>n</sub>.<br>
The same definition holds when the considered matrix sequence shows a multi-level structure. In that case n is replaced by **n** uniformly in A<sub>n</sub> and d<sub>n</sub>._

From an intuitive viewpoint, when the symbol \(\psi\) is continuous a.e. and the eigenvalues of _A<sub>n</sub>_ can be associated with evaluations of \(\psi\) on an equispaced grid over the domain _D_, the notion of spectral distribution reduces to the classical observation that a Riemann sum of a Riemann-integrable function converges to the corresponding integral. More generally, if \(\psi\) is continuous a.e. and the discretization parameter _n_ is sufficiently large, then the eigenvalues of _A<sub>n</sub>_, after a suitable ordering and possibly up to a negligible number of outliers of order _o(d<sub>n</sub>_), behave like uniform samples of \(\psi\) over _D_. An analogous interpretation holds for singular value distributions. Within this framework, the following result is therefore natural.

**Proposition 2.1** \(\{A_n\}_n\sim_\lambda\psi\) _and_ \(\Lambda(A_n)\subseteq S\) _for all_ \(n\in\mathbb{N}\)_, then_ \(\mathrm{essRan}\psi\subseteq\bar{S}\) _a.e., where_ \(S\subseteq\mathbb{C}\) _and_ \(\bar{S}\) _denotes its closure._

In particular \(\{A_n\}_n\sim_\lambda\psi\) and _A<sub>n</sub>_ positive definite for all _n_ imply that \(\psi\) is nonnegative definite almost everywhere, simply nonnegative almost everywhere if _r_=1. For singular values, the analogue of positivity is uniform invertibility. Suppose that \(\{A_n\}_n\sim_\sigma\psi\) and that there exists \(\delta>0\) such that \(\sigma_\mathrm{min}(A_n)\ge\delta\) for all _n_. Then \(\sigma_\mathrm{min}(\psi)>0\) almost everywhere, i.e.

\(\mu_t\big(\{x\in D:\sigma_\mathrm{min}(\psi(x))=0\}\big)=0.\)

Conversely, if \(\sigma_\mathrm{min}(\psi)=0\) on a set of positive measure, then the sequence {_A<sub>n</sub>}<sub>n</sub>_ cannot be uniformly invertible.

As will become apparent, determining the spectral distribution is generally more straightforward for Hermitian matrix sequences. Nevertheless, several effective techniques are available for treating sequences in which the non-Hermitian component is sufficiently small. In particular, the following proposition shows that perturbations of Hermitian sequences with small norm do not affect the asymptotic spectral distribution.

