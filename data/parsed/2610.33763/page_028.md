<tbc>_Furthermore, if the essential range of_ \(\psi\) _consists of a single number_ \(s\in\mathbb{C}\)_, then_

\(\{A_n\}_n\sim_\lambda\psi\Longleftrightarrow\{A_n\}_n\text{\textit{is weakly clustered at s in the sense of the eigenvalues.}}\)

_The latter case is typically of interest in the context of preconditioning. Corresponding statements can be given for the singular values, with the obvious suitable changes._

A corresponding definition can be given for singular values by considering sets \(S\subseteq\mathbb{R}^+\). When the term clustering is used without further specification, it is implicitly understood in the weak sense. The special case of _single-point clustering_, where _S_={_s_} consists of a single element, plays a particularly important role in the theory of preconditioning.

If a matrix sequence admits a continuous spectral distribution, clustering naturally follows. More precisely, if {_A<sub>n</sub>}<sub>n</sub>_ has eigenvalue distribution described by a function \(\psi\), the eigenvalues can be interpreted as a uniform sampling of \(\psi\), and are therefore clustered around its range. This intuition is formalized in the following result.

**Proposition 2.3** _If_ \(\{A_n\}_n\sim_\lambda\psi\)_, then_ {_A<sub>n</sub>}<sub>n</sub> is weakly clustered at the essential range of_ \(\psi\) _in the sense of the eigenvalues. Moreover, if_ \(\mathrm{essRan}\psi=\{s\}\) _with_ \(s\in\mathbb{C}\) _fixed, then_ \(\{A_n\}_n\sim_\lambda\psi\) _if and only if_ {_A<sub>n</sub>}<sub>n</sub> is weakly clustered at s in the sense of the eigenvalues._

An analogous statement holds for singular values.

**Proposition 2.4** _If_ \(\{A_n\}_n\sim_\sigma\psi\)_, then_ {_A<sub>n</sub>}<sub>n</sub> is weakly clustered at the essential range of_ \(\psi\) _in the sense of the singular values. Furthermore, if_ \(\mathrm{essRan}\psi=\{s\}\) _with_ \(s\in\mathbb{R}\) _fixed, then_ \(\{A_n\}_n\sim_\sigma\psi\) _if and only if_ {_A<sub>n</sub>}<sub>n</sub> is weakly clustered at s in the sense of the singular values._

## 2.2 Approximating classes of sequences

We introduce the notion of an approximating class of sequences (a.c.s.), which plays a fundamental role in the modern analysis of matrix sequences. In essence, an a.c.s. associated with a given matrix sequence {_A<sub>n</sub>}<sub>n</sub>_ consists of a family of matrix sequences that approximate {_A<sub>n</sub>}<sub>n</sub>_ asymptotically, up to perturbations that are negligible in a precise sense. Such perturbations typically include a component of low rank relative to the matrix dimension and another component whose spectral norm vanishes in the limit. This framework provides a rigorous notion of convergence for matrix sequences and induces a natural topology on their space. The formal definition of a.c.s. and the corresponding convergence results originate from earlier works and are presented in a comprehensive and modern form in \[121, 134, 41, 42\].

**Definition 2.3** _Let_ {_A<sub>n</sub>}<sub>n</sub> be a matrix sequence and let_ {{_B<sub>n,j</sub>}<sub>n</sub>}<sub>j</sub> be a class of matrix sequences, with A<sub>n</sub> and B<sub>n,j</sub> of size d<sub>n</sub>. We say that_ {{_B<sub>n,j</sub>}<sub>n</sub>}<sub>j</sub> is an a.c.s. for_ {_A<sub>n</sub>}<sub>n</sub> if the following condition is met: for every j, there exists n<sub>j</sub> such that, for every_ \(n\ge n_j\),

\(A_n=B_{n,j}+R_{n,j}+N_{n,j},\)<br>
\(\text{\textit{rank}}(R_{n,j})\le c(j)d_n\text{\textit{and}}\|N_{n,j}\|\le\omega(j),\)

