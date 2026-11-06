cuss the results and conclude. Appendix A summarizes the Riemannian geometry used in Sec. 4, and Appendix B collects supplementary analyses.

## 2 Sample-based Krylov solver

### 2.1 Problem and sampling protocol

Let \(A=A^\dagger\in\mathbb{C}^{N\times N}\) be invertible, with _N_=2_<sup>n</sup>_ and \(\|b\|=1\). We assume spectral bounds

\(spec(A)\subseteq[-B,-a]\cup[a,B],0<a\le B,\kappa=B/a.\) (1)

The bounds may be conservative. The normalized solution is

\(|x\rangle=\frac{A^{-1}|b\rangle}{\|A^{-1}b\|},\) (2)

and we write \(x_z=\langle z|x\rangle\) for its amplitude at the basis string _z_.

In quantum Krylov-state sampling, each shot prepares \(|b\rangle\), evolves it under _A_ for a time _T_, and measures \(e^{-iAT}|b\rangle\) in the computational basis. If _T_ is drawn from a distribution \(\mu\), the outcome law is

\(q(z)=\mathbb{E}_{T\sim\mu}|\langle z|e^{-iAT}|b\rangle|^2.\) (3)

In this paper \(\mu\) is a finite set of times _T_<sub>1</sub>_,...,T<sub>d</sub>_ with equal or prescribed shot counts. The evolution can be compiled by product formulas or by randomized methods such as qDRIFT \[13\]. Let S be the set of distinct observed strings and S_<sub>M</sub>_ the set observed in _M_ independent shots.

### 2.2 Measurement in a general orthonormal basis

The computational basis is not essential to the protocol. Let _F_ be a unitary matrix with an efficient circuit _F<sub>q</sub>_, and define the basis vectors \(|z\rangle_F=F^\dagger|z\rangle\). Measuring \(F_qe^{-iAT}|b\rangle\) in the computational basis is equivalent to measuring \(e^{-iAT}|b\rangle\) in the basis \(\{|z\rangle_F\}\). Since

\(Fe^{-iAT}F^\dagger=e^{-i\tilde{A}T},\tilde{A}=FAF^\dagger,\tilde{b}=Fb,\) (4)

the protocol in the basis _F_ is the computational-basis protocol for the unitarily equivalent system \(\tilde{A}\tilde{x}=\tilde{b}\). The spectrum, the spectral bounds of Eq. (1), and \(\|A^{-1}b\|\) are unchanged. Therefore every statement about the computational-basis protocol holds in the basis _F_, with _x<sub>z</sub>_ replaced by the coefficients \(\langle z|_Fx\rangle\). We state the results of Sec. 3 directly in the basis _F_. The basis matters because concentration is basis dependent. For elliptic problems with smooth data, a sine or cosine basis matched to the boundary conditions concentrates the solution on a few low wave vectors, whereas the computational (grid-point) basis does not. Sections 4 and 5 use this freedom.

### 2.3 Positive-definite systems and Galerkin reconstruction

When _A_ is Hermitian positive definite, a second reconstruction is available. The duct examples use real symmetric matrices. Let _x_<sup>∗</sup>=_A_<sup>-1</sup>_b_ denote the unnormalized solution, with \(\|b\|=1\), and let \(\hat{x}_z=\langle z|_Fx^*\rangle\) be its coefficients in the measurement basis. For a set S we define \(V_\mathscr{S}=span\{|z\rangle_F:z\in\mathscr{S}\}\). The Galerkin solution \(x_\mathscr{S}\in V_\mathscr{S}\) satisfies \(\langle v,b-Ax_\mathscr{S}\rangle=0\) for all \(v\in V_\mathscr{S}\). With \(\hat{A}=FAF^\dagger\) and \(\hat{b}=Fb\), it is obtained from

\(\hat{A}[\mathscr{S},\mathscr{S}]y=\hat{b}[\mathscr{S}],x_\mathscr{S}=F^\dagger Embed(y,\mathscr{S}),\) (5)

where \(\hat{A}[\mathscr{S},\mathscr{S}]\) is the principal submatrix indexed by S . Since it is a principal submatrix of a positive- definite matrix, Eq. (5) has a unique solution.

**Lemma 1** (Galerkin optimality)**.** _Let_ \(\|v\|_A^2=\langle v,Av\rangle\)_. The Galerkin solution satisfies_ \(\|x_\mathscr{S}-x^*\|_A=min_{v\in V_\mathscr{S}}\|v-x^*\|_A\)_. If_ \(\mathscr{S}\subseteq\mathscr{S}'\)_, then_ \(\|x_{\mathscr{S}^\prime}-x^*\|_A\le\|x_\mathscr{S}-x^*\|_A\).

