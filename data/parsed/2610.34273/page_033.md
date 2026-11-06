## 4.5 The complete graph bound and its consequences

We apply the preceding growth estimate to the symmetric spectral profile \(P_\phi\). Its lower growth rate, compared with the interpolation upper bound from Subsection 4.1, constrains the average edge weight \(t_\phi\). Since a complete graph contains every pair of vertices as an edge, this average determines its value under \(\phi\). Spectral duality then gives the desired rank upper bound, while a maximum cut gives the lower bound.

**Theorem 4.11** (complete graph bound)**.** _For every integer_ \(n\ge 2\)_, over the complex numbers,_

\(\left\lfloor\frac{n^2}{4}\right\rfloor\le\mathrm{log}_2\widetilde{\text{R}}\big(\mathsf{GT}_2(K_n)\big)\le\frac{n^2}{4}.\)

_Proof._ First suppose that \(n\ge 3\), and fix an arbitrary spectral point \(\phi\in\Phi_n\). Let \(P_\phi\) and \(t_\phi\) be as in Definition 4.5. Lemma 4.6 gives positivity, symmetry, and \(P_\phi(1,\dots,1)=1\). Lemmas 4.8 and 4.9 give the two inequalities required by Lemma 4.10. Therefore, for every positive integer _a_,<tbc>

\(a^{2(n-1)/n}\le P_\phi(a,\dots,a)\le\big((n-1)(a-1)+1\big)^{1/t_\phi}.\)

<tbc>For \(a\ge 2\), take logarithms and divide by log_a_. The expression ((_n_-1)(_a_-1)+1)_/a_ tends to the positive constant _n_-1. Hence<tbc>

\(\frac{2(n-1)}{n}\le\frac{1}{t_\phi}\frac{\mathrm{log}((n-1)(a-1)+1)}{\mathrm{log}a}\longrightarrow\frac{1}{t_\phi}.\)

<tbc>It follows that \(t_\phi\le n/(2(n-1))\). By the definition of the average spectral edge weight \(t_\phi\) and Lemma 4.4,

\(\phi(\mathsf{GT}_2(K_n))=2\sum_{1\le i<j\le n}p_{i,j}^{(\phi)}=2^{\genfrac(){pt}{2}{n}{2}t_\phi}\le 2^{n^2/4}.\)

This holds for every \(\phi\in\Phi_n\). Taking the maximum over \(\Phi_n\) and applying Theorem 2.19 gives \(\widetilde{\text{R}}(\mathsf{GT}_2(K_n))\le 2^{n^2/4}\). The argument fixes _n_ throughout; only the input length _a_ tends to infinity in the preceding comparison.

For the lower bound, Proposition A.4 gives \(\mathrm{log}_2\widetilde{\text{R}}(\mathsf{GT}_2(K_n))\ge\mathrm{MaxCut}(K_n)\). A cut with _s_ vertices on one side has _s(n-s_) crossing edges, where \(1\le s\le n-1\). Since _s(n-s_)=_n_<sup>2</sup>/4-(_s-n/_2)<sup>2</sup>, its maximum is attained at \(s=\lfloor n/2\rfloor\) or \(s=\lceil n/2\rceil\), and equals \(\lfloor n^2/4\rfloor\). This proves both inequalities for \(n\ge 3\).

Finally, GT<sub>2</sub>(_K_<sub>2</sub>) is the \(2\times 2\) identity matrix viewed as a complex second-order tensor. Its _N_-th Kronecker power has matrix rank 2_<sup>N</sup>_, so its asymptotic rank is 2. Thus both bounds are equal to 1 when _n_=2, completing the proof.

The next two consequences identify the questions from \[CVZ19\] answered by the theorem. The edge exponent \(\tau(G)\) is defined in Definition 2.22.

**Corollary 4.12** (maximum-cut equality for even complete graphs)**.** _For every positive integer m,_

\(\mathrm{log}_2\widetilde{\text{R}}\big(\mathsf{GT}_2(K_{2m})\big)=\mathrm{MaxCut}(K_{2m})=m^2,\tau(K_{2m})=\frac{m}{2m-1}.\)

_Thus the equality asked for in \[CVZ19, Question 1.3.2\] holds for every even complete graph._

_Proof._ Apply Theorem 4.11 with _n_=2_m_. Its lower and upper bounds both equal _m_<sup>2</sup>. A balanced cut of _K_<sub>2_m_</sub> has _m_<sup>2</sup> edges and is a maximum cut. Finally, _K_<sub>2_m_</sub> has \((\genfrac(){pt}{2}{2m}{2}=m(2m-1)\) edges, so dividing the exponent _m_<sup>2</sup> by this number gives the formula for \(\tau(K_{2m})\).

