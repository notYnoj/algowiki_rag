To bound the second term in (A.13), let \(\hat{\mathfrak{c}}\) be a block-vectorized version of \(\widehat{C}\), which can be written as

\(\hat{\mathfrak{c}}=\left(\tilde{\nu}^{-1}\otimes I_{m/m_0}\right)\left(\widetilde{W}_\nu\otimes I_{m/m_0}\right)\left(\begin{array}{ c }
\widetilde{M}_1 \\
\vdots \\
\widetilde{M}_t
\end{array}\right)\) (A.14)

for \(\widetilde{M}_j=\langle(\widetilde{U}_\phi(:,j)^T\otimes I_{m/m_0})(\tilde{\phi}^T\otimes I_{m/m_0})\mathfrak{a},(\widetilde{V}_\psi(:,j)^T\otimes I_{k/k_0})(\tilde{\psi}^T\otimes I_{k/k_0})\mathfrak{b}\rangle_{L-1}\), where \(\langle\cdot,\cdot\rangle_{L-1}\) is the bilinear map obtained by applying \(\langle\cdot,\cdot\rangle\) recursively _L_-1 times (and again defaulting to matrix multiplication at that point). To obtain (A.14), we exploit the fact that, in exact arithmetic, this expression is equivalent to evaluating the perturbed alternative basis algorithm as done in Section 4 - e.g., where the basis transformations are applied recursively to _A_ and _B_ first before evaluating the bilinear algorithm corresponding to \(\widetilde{U}_\phi\), \(\widetilde{V}_\psi\), and \(\widetilde{W}_\nu\) and finally applying \(\tilde{\nu}^{-1}\). This is implied by the following observation. Suppose that

\(\left(\tilde{\phi}^T\otimes I_{m/m_0}\right)\mathfrak{a}=\mathfrak{a}'=\left(\begin{array}{ c }
A'_{11} \\
A'_{12} \\
\vdots \\
A'_{m_0k_0}
\end{array}\right)\) (A.15)

for some \((m/m_0)\times(k/k_0)\) matrices \(A'_{11},\dots,A'_{m_0k_0}\). In this case, the left input to \(\langle\cdot,\cdot\rangle_{L-1}\) in block row _j_ of (A.14) is

\(A_j:=\left(\widetilde{U}_\phi(:,j)^T\otimes I_{m/m_0}\right)\mathfrak{a}'=\widetilde{U}_\phi(1,j)A'_{11}+\cdots+\widetilde{U}_\phi(m_0k_0,j)A'_{m_0k_0}\in\mathbb{C}^{(m/m_0)\times(k/k_0)}.\) (A.16)

The subsequent recursive call begins by multiplying a_<sub>j</sub>_, the block-vectorized copy of _A<sub>j</sub>_ obtained by breaking it into submatrices of size \((m/m_0^2)\times(k/k_0^2)\), by \((\tilde{\phi}^T\otimes I_{m/m_0^2})\). If \(\mathfrak{a}'_{11},\dots,\mathfrak{a}'_{m_0k_0}\) are similarly block-vectorized copies of \(A'_{11},\dots,A'_{m_0k_0}\), then

\(\mathfrak{a}_j=\widetilde{U}_\phi(1,j)\mathfrak{a}'_{11}+\cdots+\widetilde{U}_\phi(m_0k_0,j)\mathfrak{a}'_{m_0k_0}\) (A.17)

and therefore

\(\left(\tilde{\phi}^T\otimes I_{m/m_0^2}\right)\mathfrak{a}_j=\widetilde{U}_\phi(1,j)\left(\tilde{\phi}^T\otimes I_{m/m_0^2}\right)\mathfrak{a}'_{11}+\cdots+\widetilde{U}_\phi(m_0k_0,j)\left(\tilde{\phi}^T\otimes I_{m/m_0^2}\right)\mathfrak{a}'_{m_0k_0}=\left(\widetilde{U}_\phi(:,j)^T\otimes I_{m/m_0}\right)\left(I_{m_0k_0}\otimes\left(\tilde{\phi}^T\otimes I_{m/m_0^2}\right)\right)\left(\begin{array}{ c }
\mathfrak{a}'_{11} \\
\vdots \\
\mathfrak{a}'_{m_0k_0}
\end{array}\right),\) (A.18)

where \(\left(I_{m_0k_0}\otimes\left(\tilde{\phi}^T\otimes I_{m/m_0^2}\right)\right)\left(\begin{array}{ c }
\mathfrak{a}'_{11} \\
\vdots \\
\mathfrak{a}'_{m_0k_0}
\end{array}\right)\) is exactly what we get if we break _A_ into \((m/m_0^2)\times(k/k_0^2)\) blocks and multiply the corresponding block vectorization by \(((\tilde{\phi}^{\otimes 2})^T\otimes I_{m/m_0^2})\). Continuing recursively - and applying the same argument to the other encoding matrices/basis transformations - implies the claimed equivalence.

We now continue bounding \(\|\widehat{C}-\widetilde{C}\|\). By our induction hypothesis, the block-vectorized copy of \(\widetilde{C}\) satisfies

\(\tilde{\mathfrak{c}}=\left(\tilde{\nu}^{-1}\otimes I_{m/m_0}\right)\left(\widetilde{W}_\nu\otimes I_{m/m_0}\right)\left(\begin{array}{ c }
\widetilde{M}_1+E_1 \\
\vdots \\
\widetilde{M}_t+E_t
\end{array}\right),\) (A.19)

for _E_<sub>1</sub>_,...,E<sub>t</sub>_ with

\(\|E_j\|\le\left((1+\delta)^{6(L-1)}-1\right)(k/k_0^L)E^{L-1}\left\|\left(\widetilde{U}_\phi(:,j)^T\otimes I_{m/m_0}\right)\left(\tilde{\phi}^T\otimes I_{m/m_0}\right)\mathfrak{a}\right\|\left\|\left(\widetilde{V}_\psi(:,j)^T\otimes I_{k/k_0}\right)\left(\tilde{\psi}^T\otimes I_{k/k_0}\right)\mathfrak{b}\right\|.\) (A.20)

