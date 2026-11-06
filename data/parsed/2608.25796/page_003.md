<tbc>structure arise; see \[19, 44, 4\] where the external level is related to discretization with respect to the time variable and the internal _d_ levels are related to the approximation formulae in the _d_ spatial variables.

The paper is organized as follows. Section 2 introduces the theoretical framework and provides a summary of the essential tools. Section 3 presents the discretization of the nonlocal evolutionary FDE using finite difference schemes in time and space, and derives the resulting all-at-once linear system, emphasizing the structural features of the matrices. In Section 4, the coefficient matrix sequence is studied via GLT tools and its symbol is derived. Section 5 is devoted to algorithmic proposals, to preconditioning strategies, and to the same type of spectral analysis for the preconditioned matrix sequences, proving clustering results both in the singular value and eigenvalue sense. In Section 6, numerical experiments are conducted to assess the effectiveness of the proposed preconditioner in terms of iteration counts and CPU time. Concluding remarks are presented in Section 7 together with a sketch of the main ideas for the _d_ dimensional space case and further open problems.

## 2. Preliminaries

We concisely introduce the basic tools employed in this work, which are discussed in detail in \[18\]. For simplicity, we restrict the definitions and theorems to the unilevel scalar case, which is sufficient for the purposes of the current paper. However, all the concepts can be extended to the multilevel \[19\] and block \[5, 6\] settings, that arise from more complex differential problems such as systems of partial differential equations \[15, 38\] or more precise approximations such the high order finite elements \[21\] and isogeometric analysis with intermediate regularity \[22\]. We observe that the approximation of the _d_-dimensional space equation (1) leads to (_d_+1)-level GLT matrix sequence with a specific tensor structure which can be treated using only unilevel GLT structures (see Axiom **GLT4**).

Let us first establish some useful notation.

• Given a square matrix _A<sub>n</sub>_, we denote with \(\lambda_j(A_n)\) and \(\sigma_j(A_n)\) the _j_-th eigenvalue and singular value of _A<sub>n</sub>_, respectively, as _j_=1_,...,n_.<tbc>

• The spectral norm for a square matrix _A<sub>n</sub>_ is denoted as \(\|A_n\|\).<tbc>

• Whenever we use terminology from measure theory, for instance "measurable set", "measurable function", "a.e.", we always refer to the Lebesgue measure in R_<sup>t</sup>_, denoted with \(\mu_t\).

### 2.1. Spectral tools

Throughout the paper, we deal with matrix sequences, referring to any sequence of the form {_A<sub>n</sub>}<sub>n</sub>_, where _A<sub>n</sub>_ is a square matrix of size _d<sub>n</sub>_ and \(d_n\rightarrow\infty\) monotonically as \(n\rightarrow\infty\). To a given matrix sequence, it is often possible to associate a spectral or singular value distribution, according to the following definition.

**Definition 2.1.** _Let_ {_A<sub>n</sub>}<sub>n</sub> be a matrix sequence, where A<sub>n</sub> has size_ \(d_n\times d_n\)_, and let_ \(\psi:D\subset\mathbb{R}^t\rightarrow\mathbb{C}\) _be a measurable function defined on a set D with_ \(0<\mu_t(D)<\infty\)_. Denote with C<sub>c</sub>_(K) _the set of continuous complex-valued functions with bounded support on_ \(\mathbb{K}\in\{\mathbb{R},\mathbb{C}\}\).

• {_A<sub>n</sub>}<sub>n</sub> has an (asymptotic) singular value distribution described by_ \(\psi\) _if for any_ \(F\in C_c(\mathbb{R})\)<tbc>

<tbc>\(lim_{n\rightarrow\infty}\frac{1}{d_n}\sum_{i=1}^{d_n}F(\sigma_i(A_n))=\frac{1}{\mu_t(D)}\int_DF(|\psi(x)|)dx,\)<tbc>

<tbc>_where_ \(\sigma_i(A_n)\)_, i_=1_,...,d<sub>n</sub>, are the singular values of A<sub>n</sub>. We use the notation_ \(\{A_n\}_n\sim_\sigma\psi\).<tbc>

