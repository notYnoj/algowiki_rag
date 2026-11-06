Assuming \(\frac{2(p-1)M_\varepsilon\delta}{\mathrm{gap}_\varepsilon-2M_\varepsilon\delta}<1\) and again applying \[31, Lemma 3.1\], we can rewrite \(\prod_{k\neq j}(1+\mu_k)\) as follows:

\(\prod_{k\neq j}(1+\mu_k)=1+\theta\text{for}|\theta|\le\frac{2(p-1)M_\varepsilon\delta}{\mathrm{gap}_\varepsilon-2pM_\varepsilon\delta}.\) (A.10)

Inserting this above and rearranging yields the bound.

## A.2 Perturbation Bound for Bilinear Algorithms

Finally, we prove a perturbation bound for evaluating a recursive, alternative-basis bilinear algorithm in exact arithmetic.

**Proposition A.3.** _Let_ \(U_\phi\in\mathbb{C}^{m_0k_0\times t}\), \(V_\psi\in\mathbb{C}^{k_0n_0\times t}\), \(W_\nu\in\mathbb{C}^{m_0n_0\times t}\), \(\phi\in\mathbb{C}^{m_0k_0\times m_0k_0}\), \(\psi\in\mathbb{C}^{k_0n_0\times k_0n_0}\)_, and_ \(\nu^{-1}\in\mathbb{C}^{m_0n_0\times m_0n_0}\) _denote the encoding matrices and basis transformations defining an alternative basis bilinear map_<tbc>

\(\langle\cdot,\cdot\rangle:\mathbb{C}^{m_0\times k_0}\times\mathbb{C}^{k_0\times n_0}\rightarrow\mathbb{C}^{m_0\times n_0}\)

<tbc>_evaluated as_<tbc>

\(c=\nu^{-1}\left[W_\nu\left(U_\phi^T(\phi^Ta)\odot V_\psi^T(\psi^Tb)\right)\right],\)

<tbc>_where a and b are vectorized copies of input matrices_ \(A\in\mathbb{C}^{m_0\times k_0}\) _and_ \(B\in\mathbb{C}^{k_0\times n_0}\) _and c is a vectorized copy of the corresponding output_ \(\langle A,B\rangle=C\in\mathbb{C}^{m_0\times n_0}\)_. Suppose that a corresponding "perturbed" bilinear form is defined by encoding matrices_ \(\widetilde{U}_\phi\in\mathbb{C}^{m_0k_0\times t}\), \(\widetilde{V}_\psi\in\mathbb{C}^{k_0n_0\times t}\)_, and_ \(\widetilde{W}_\nu\in\mathbb{C}^{m_0n_0\times t}\) _and basis transformations_ \(\tilde{\phi}\in\mathbb{C}^{m_0k_0\times m_0k_0}\), \(\tilde{\psi}\in\mathbb{C}^{k_0n_0\times k_0n_0}\)_, and_ \(\tilde{\nu}^{-1}\in\mathbb{C}^{m_0n_0\times m_0n_0}\)_, which are obtained by applying entry-wise, relative perturbations to_ \(U_\phi\), \(V_\psi\), \(W_\nu\), \(\phi\), \(\psi\)_, and_ \(\nu^{-1}\)_, respectively, of size at most_ \(\delta>0\) _(e.g.,_ \(\widetilde{U}_\phi(i,j)=U_\phi(i,j)(1+\Delta_{ij})\) _for some_ \(|\Delta_{ij}|\le\delta\)_). Let_ \(C,\widetilde{C}\in\mathbb{C}^{m\times n}\) _be the result of evaluating recursive versions of these bilinear algorithms at input matrices_ \(A\in\mathbb{C}^{m\times k}\) _and_ \(B\in\mathbb{C}^{k\times n}\) _in exact arithmetic, where we assume that both default to matrix multiplication after L recursive steps for_ \(L\in\mathbb{N}\) _satisfying_<tbc>

\(L\le\mathrm{min}\left\{\mathrm{log}_{m_0}(m),\mathrm{log}_{n_0}(n),\mathrm{log}_{k_0}(k)\right\}.\)

<tbc>_In this case,_

\(\|C-\widetilde{C}\|\le\left((1+\delta)^{6L}-1\right)(k/k_0^L)E^L\|A\|\|B\|\)

_where_ \(\|\cdot\|\) _is the maximum-entry norm and E is the stability factor corresponding to_ \(U_\phi\), \(V_\psi\), \(W_\nu\), \(\phi\), \(\psi\)_, and_ \(\nu^{-1}\) _(see Theorem 4.3 )._

_Proof._ We prove the result via induction on _L_, starting with the inductive step. Assume that the given bound holds for _L_-1 and consider \(L\ge 2\). To evaluate our bilinear forms, we partition the input matrices into blocks as follows (assuming _m_<sub>0</sub>, _k_<sub>0</sub>, and _n_<sub>0</sub> divide _m_, _k_, and _n_):

\(A=\left(\begin{array}{ c c c c }
A_{11} & \cdots & A_{1k_0} \\
\vdots &  & \vdots \\
A_{m_01} & \cdots & A_{m_0k_0}
\end{array}\right)\text{and}B=\left(\begin{array}{ c c c c }
B_{11} & \cdots & B_{1n_0} \\
\vdots &  & \vdots \\
B_{k_01} & \cdots & B_{k_0n_0}
\end{array}\right).\) (A.11)

Each _A<sub>ij</sub>_ is \((m/m_0)\times(k/k_0)\) while each _B<sub>ij</sub>_ is (_k/k_<sub>0</sub>) by (_n/n_<sub>0</sub>). For this block partition, let a and b be _block_ vectorized copies of _A_ and _B_ - e.g.,

\(\mathfrak{a}=\left(\begin{array}{ c }
A_{11} \\
A_{12} \\
\vdots \\
A_{m_0k_0}
\end{array}\right)\in\mathbb{C}^{mk_0\times(k/k_0)}\text{and}\mathfrak{b}=\left(\begin{array}{ c }
B_{11} \\
B_{12} \\
\vdots \\
B_{k_0n_0}
\end{array}\right)\in\mathbb{C}^{kn_0\times(n/n_0)}.\) (A.12)

Additionally, let \(\widehat{C}\) be the output of a hybrid, recursive bilinear algorithm applied to _A_ and _B_, which uses \(\widetilde{U}_\phi\), \(\widetilde{V}_\psi\), \(\widetilde{W}_\nu\), \(\tilde{\phi}\), \(\tilde{\psi}\), and \(\tilde{\nu}^{-1}\) at the highest level and \(U_\phi\), \(V_\psi\), \(W_\nu\), \(\phi\), \(\psi\), \(\nu^{-1}\) thereafter. In this case, we have

\(\|C-\widetilde{C}\|\le\|C-\widehat{C}\|+\|\widehat{C}-\widetilde{C}\|.\) (A.13)

