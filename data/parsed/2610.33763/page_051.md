Further results connecting Schatten _p_-norms, unitarily invariant norms (see \[16\]), variational characterization, and Toeplitz/Hankel structures can be found in \[128\].

## 4.4 Multi-level block Toeplitz matrices

Given \(\mathbf{n}\in\mathbb{N}^d\), a matrix of the form<tbc>

\([A_{\mathbf{i}-\mathbf{j}}]_{\mathbf{i},\mathbf{j}=\mathbf{1}}^\mathbf{n}\in\mathbb{C}^{N(\mathbf{n})r\times N(\mathbf{n})r},\)

<tbc>with blocks \(A_\mathbf{k}\in\mathbb{C}^{r\times r}\), \(\mathbf{k}\in\{-(\mathbf{n}-\mathbf{1}),\dots,\mathbf{n}-\mathbf{1}\}\), is called a _multi-level block Toeplitz matrix_, or, more precisely, a _d_-level _r_-block Toeplitz matrix.<br>
Given a matrix-valued function \(f:[-\pi,\pi]^d\rightarrow\mathbb{C}^{r\times r}\) belonging to \(L^1([-\pi,\pi]^d)\), the **_n_**-th Toeplitz matrix associated with _f_ is defined as<tbc>

\(T_\mathbf{n}(f):=[\hat{f}_{\mathbf{i}-\mathbf{j}}]_{\mathbf{i},\mathbf{j}=\mathbf{1}}^\mathbf{n}\in\mathbb{C}^{N(\mathbf{n})r\times N(\mathbf{n})r},\)

<tbc>where

\(\hat{f}_\mathbf{k}=\frac{1}{(2\pi)^d}\int_{[-\pi,\pi]^d}f(\theta)e^{-i(\mathbf{k}\cdot\unknown)}d\unknown\in\mathbb{C}^{r\times r},\mathbf{k}\in\mathbb{Z}^d,\)

are the Fourier coefficients of _f_.<br>
The family \(\{T_\mathbf{n}(f)\}_{\mathbf{n}\in\mathbb{N}^d}\) is called the family of (multi-level block) Toeplitz matrices associated with _f_, which is referred to as the _generating function_.

## 4.5 Block diagonal sampling matrices

Given \(d\ge 1\), \(\mathbf{n}\in\mathbb{N}^d\) and a function \(a:[0,1]^d\rightarrow\mathbb{C}^{r\times r}\), we define the multi-level block diagonal sampling matrix _D<sub>**n**</sub>(a_) as the block diagonal matrix

\(D_\mathbf{n}(a)=\mathrm{diag}_{\mathbf{i}=\mathbf{1},\dots,\mathbf{n}}\left(a\left(\frac{\mathbf{i}}{\mathbf{n}}\right)\right)\in\mathbb{C}^{N(\mathbf{n})r\times N(\mathbf{n})r}.\) (4.1)

Essentially, _D<sub>**n**</sub>(a_) is a diagonal matrix whose entries are the evaluations of _a(x_) at the points of a uniform mesh over the domain \[0,1\]_<sup>d</sup>_, with the points arranged in lexicographical order.

## 4.6 The ∗-algebra of _d_-level _r_-block GLT matrix sequences

Let \(r\ge 1\) be a fixed integer. A multi-level _r_-block GLT sequence, or simply a GLT sequence if _r_ does not need to be specified, is a special multi-level _r_-block matrix sequence equipped with a measurable function \(\kappa:[0,1]^d\times[-\pi,\pi]^d\rightarrow\mathbb{C}^{r\times r}\), \(d\ge 1\), called the _symbol_. We write \(\{A_n\}_n\sim_\mathrm{GLT}\kappa\) to denote that {_A<sub>n</sub>}<sub>n</sub>_ is a GLT sequence with symbol \(\kappa\). A fundamental property of the GLT symbol is that it is unique: if two symbols are associated with the same matrix sequence, then they must coincide almost everywhere.

**Proposition 4.1** _If_ \(\{A_\mathbf{n}\}_\mathbf{n}\sim_\mathrm{GLT}\kappa\) _and_ \(\{B_\mathbf{n}\}_\mathbf{n}\sim_\mathrm{GLT}\xi\)_, then_ \(\kappa=\xi\) _a.e._

