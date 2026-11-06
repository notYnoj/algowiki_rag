<tbc>**Theorem 2.** _Let_ \(n\ge 4\) _an integer. Any 1-round quantum-PN algorithm has a monochromatic_ (_n_-2)_-block in its support._

The proof of Theorem 2 follows from Lemmas 5.1 and 5.2. The former describes the output distribution as the trace of product of certain matrices, while the latter provides some structure on those matrices. We state the lemmas here, derive the proof of Theorem 2, and prove them in Section 5.1 and Section 5.2 respectively.

Call \(d\in\mathbb{N}\) the dimension of the local registers: \(\mathsf{L}(p),\mathsf{M}(p),\mathsf{R}(p)\simeq\mathbb{C}^d\) and let \(H=\mathbb{C}^d\otimes\mathbb{C}^d\otimes\mathbb{C}^d\). The communication round swapping each L(_p_) with R(_p_-1) is implemented by the unitary matrix _C_ defined as

\(C\left(\otimes_{p=1}^n|\ell_p\rangle_{\mathsf{L}(p)}|m_p\rangle_{\mathsf{M}(p)}|r_p\rangle_{\mathsf{R}(p)}\right)=\otimes_{p=1}^n|r_{p-1}\rangle_{\mathsf{L}(p)}\otimes|m_p\rangle_{\mathsf{M}(p)}\otimes|\ell_{p+1}\rangle_{\mathsf{R}(p)},\)

for all \(\ell_p,m_p,r_p\in[d]\) and all \(p\in\{0,1,\dots,n\}\) such that \(\ell_0=\ell_n\) and _r_<sub>0</sub>=_r<sub>n</sub>_. In Lemma 5.1, the state _u_ should be thought of as the local state of each player _before_ the first (and unique) communication round, and \(C|u,\dots,u\rangle\) as the global state after the communication round.

**Lemma 5.1.** _For all_ \(n\ge 4\), \(|u\rangle\in H\backslash\{0\}\)_, there exists a conjugate-linear map_\(4L:H\rightarrow\mathrm{Mat}_{d^2}(\mathbb{C})\) _and a Hilbert space_ \(V\subseteq\mathrm{Mat}_d(\mathbb{C})\) _with_ \(0<\mathrm{dim}(V)\le d\) _such that_<tbc>

\(\mathrm{im}(L)=(V\otimes\mathrm{Mat}_d(\mathbb{C}))P\text{\textit{where}}\forall\alpha,\beta\in\mathbb{C}^d\text{\textit{we have}}P(\alpha\otimes\beta)=\beta\otimes\alpha,\)

<tbc>_and for all_ \(v_1,\dots,v_n\in H\)_, we have that_<tbc>

\(\langle v_1,v_2,\dots,v_n|C|u,\dots,u\rangle=\mathrm{Tr}\left(\prod_{p=1}^nL(v_p)\right).\)

<tbc>The matrices _M=L(x_) for some \(x\in H\) have some special structure: indeed, with respect to the right basis, the matrix _M_ has the following block decomposition

\(M=\left[\begin{array}{ c c c c }
\tau(M) & 0 & * & 0 \\
* & 0 & * & 0 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0
\end{array}\right].\)

We also use that this decomposition is compatible with products of matrices and that the map \(\tau\) is surjective. Formally, we prove the following; see Section 5.2 for the proof.

**Lemma 5.2.** _Let_ \(d\in\mathbb{N}\backslash\{0\}\) _and V be a subspace of_ Mat_<sub>d</sub>_(C) _with_ \(0<\mathrm{dim}(V)\le d\)_. Call_ \(S=(V\otimes\mathrm{Mat}_d(\mathbb{C}))P\) _and S<sup>k</sup>_=span{_M_<sub>1</sub>_M_<sub>2</sub>_...M<sub>k</sub>:M_<sub>1</sub>_,M_<sub>2</sub>_,...,M<sub>k</sub>_\(\in S\}\)_. There exists a subspace E of_ \(\mathbb{C}^d\otimes\mathbb{C}^d\) _and a map_ \(\tau:\mathrm{Mat}_{d^2}(\mathbb{C})\rightarrow\mathrm{End}(E)\) _with the following properties:_

(_T1)_ \(\tau(MN)=\tau(M)\tau(N)\) _for all_ \(M,N\in\bigcup_{k\ge 1}S^k\),<tbc>

(_T2)_ \(\mathrm{Tr}(M)=\mathrm{Tr}(\tau(M))\) _for all_ \(M\in\bigcup_{k\ge 1}S^k\),<tbc>

_(T3)_ _for all_ \(X\in\mathrm{End}(E)\)_, there exists_ \(M\in S^2\) _such that_ \(\tau(M)=X\).

Given these technical lemmas, we are ready to derive the proof of Theorem 2.

_Proof of Theorem 2._ The proof is by contradiction. Suppose there exists an algorithm \(\mathscr{A}=(U_0,U_1,\Pi)\) with output labels \(\Sigma=[c]\) for some \(c\in\mathbb{N}\) and no monochromatic (_n_-2)-block in its support. Denote the local state of every vertex before the communication round by \(u=U_0|000\rangle\). In particular, the global state of after the communication round is \(\rho=C|u\rangle^{\otimes n}\langle u|^{\otimes n}C^\dagger\). Let _V_

4a conjugate-linear map \(f:U\rightarrow V\) between complex vector spaces is additive, i.e., _f(x+y_)=_f(x_)+_f(y_) for all vectors \(x,y\in U\), but conjugates the scalar factors, i.e., \(f(\lambda x)=\overline{\lambda}f(x)\) for all \(x\in U\) and \(\lambda\in\mathbb{C}\)

