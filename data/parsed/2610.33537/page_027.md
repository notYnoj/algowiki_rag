where<tbc>

\(\phi_\mu^{(0)}(k)=\frac{1-\nu+\frac{\nu}{2}\left(1-\frac{\mu}{C_{M+1}}\right)e^{\mathrm{i}k\Delta x}}{1-\frac{\nu}{2}\left(1+\frac{\mu}{C_{M+1}}\right)e^{-\mathrm{i}k\Delta x}},\psi_\mu^{(0)}(k)=\frac{1-\nu+\frac{\nu}{2}\left(1+\frac{\mu}{C_{M+1}}\right)e^{-\mathrm{i}k\Delta x}}{1-\frac{\nu}{2}\left(1-\frac{\mu}{C_{M+1}}\right)e^{\mathrm{i}k\Delta x}}.\)

<tbc>Let \(\mathcal{G}_\mu^{(0)}(k)=\phi_\mu^{(0)}(k)\psi_\mu^{(0)}(k)\) as in (40), which represents the leading-order amplification factor of one SGS iteration. Note that **A**_<sub>h</sub>_ is the \(3\times 3\) upper-left block of **A** with eigenvalues \(\mu=-\sqrt{3},0,\sqrt{3}\). Define<tbc>

\(\mathbf{Q}(k)=\mathbf{V}\left(\begin{array}{ c c c }
\mathcal{G}_{-\sqrt{3}}^{(0)}(k) & 0 & 0 \\
0 & \mathcal{G}_0^{(0)}(k) & 0 \\
0 & 0 & \mathcal{G}_{\sqrt{3}}^{(0)}(k)
\end{array}\right)\mathbf{V}^{-1},\mathbf{V}=(\mathbf{v}_{-\sqrt{3}},\mathbf{v}_0,\mathbf{v}_{\sqrt{3}}).\)

<tbc>The leading order term of the propagation matrix \(\mathbf{T}(\varepsilon,k)\) can be expressed as

\(\mathbf{T}^{(0)}(k)=\left(\begin{array}{ c c c }
\mathbf{Q}(k) & \mathbf{B}_1(k) \\
\mathbf{0} & \mathbf{I}_{M-2}
\end{array}\right)^{\gamma_2}\left(\begin{array}{ c c c }
\mathbf{Q}(k) & \mathbf{B}_2(k) \\
\mathbf{0} & \mathbf{0}
\end{array}\right)^{\gamma_1}=\left(\begin{array}{ c c }
[\mathbf{Q}(k)]^{\gamma_1+\gamma_2} & [\mathbf{Q}(k)]^{\gamma_1+\gamma_2-1}\mathbf{B}_2(k) \\
\mathbf{0} & \mathbf{0}
\end{array}\right),\)

where we have dropped \(O(\varepsilon)\) terms in the expression of \(\mathbf{T}(\varepsilon,k)\) given in (C.10) using the block structures (C.11) and (C.12), and **B**<sub>1</sub> and **B**<sub>2</sub> are some matrices whose details are not important for our analysis. Below, we are going to show that at least _M_-2 eigenvalues of \(\mathbf{T}(\varepsilon,k)=\mathbf{T}^{(0)}(k)+\varepsilon\widetilde{\mathbf{T}}(\varepsilon,k)\) are \(O(\varepsilon)\), where \(\widetilde{\mathbf{T}}(\varepsilon,k)=O(1)\).

The proof begins with the diagonalization of **T**<sup>(0)</sup>(_k_). Let<tbc>

\(\mathbf{P}(k)=\left(\begin{array}{ c c c }
\mathbf{V} & -\mathbf{R}(k) \\
\mathbf{0} & \mathbf{I}_{M-2}
\end{array}\right),\mathbf{R}(k)=\mathbf{V}\left(\begin{array}{ c c c }
h_{-\sqrt{3}} & 0 & 0 \\
0 & h_0 & 0 \\
0 & 0 & h_{\sqrt{3}}
\end{array}\right)\mathbf{V}^{-1}\mathbf{B}_2(k),h_\mu=\left\{\begin{array}{ c c }
0, & \text{if}\mathcal{G}_\mu^{(0)}(k)=0, \\
[\mathcal{G}_\mu^{(0)}(k)]^{-1}, & \text{otherwise.}
\end{array}\right.\)

<tbc>Under the condition \(\gamma_1+\gamma_2\ge 2\), straightforward calculations show that<tbc>

\([\mathbf{P}(k)]^{-1}\mathbf{T}^{(0)}(k)\mathbf{P}(k)=\mathbf{D}(k):=\mathrm{diag}\left([\mathcal{G}_{-\sqrt{3}}^{(0)}(k)]^{\gamma_1+\gamma_2},[\mathcal{G}_0^{(0)}(k)]^{\gamma_1+\gamma_2},[\mathcal{G}_{\sqrt{3}}^{(0)}(k)]^{\gamma_1+\gamma_2},\underbrace{0,\dots,0}_{M-2}\right).\) (C.17)

<tbc>Since **P**(_k_) is independent of \(\varepsilon\), it follows that

\([\mathbf{P}(k)]^{-1}\mathbf{T}(\varepsilon,k)\mathbf{P}(k)=\mathbf{D}(k)+\varepsilon[\mathbf{P}(k)]^{-1}\widetilde{\mathbf{T}}(\varepsilon,k)\mathbf{P}(k)=\mathbf{D}(k)+O(\varepsilon).\) (C.18)

Let _m_ be the number of zero diagonal entries of **D**(_k_). Then by the Gershgorin circle theorem, when \(\varepsilon\) is sufficiently small, _m_ eigenvalues of \(\mathbf{T}(\varepsilon,k)\) are contained in the union of the _m_ disks with centers and radii of order \(O(\varepsilon)\), which are separated from the other _M_+1-_m_ disks. Since \(m\ge M-2\), we conclude that at least _M_-2 eigenvalues of \(\mathbf{T}(\varepsilon,k)\) are \(O(\varepsilon)\).

To summarize, we have shown that the three hydrodynamic leading-order amplification factors of the FIM iteration are

\(\Lambda_\mu^{(0)}(k)=\left[\mathcal{G}_\mu^{(0)}(k)\right]^{\gamma_1+\gamma_2},\mu\in\{-\sqrt{3},0,\sqrt{3}\},\) (C.19)

and the remaining _M_-2 eigenvalues are \(O(\varepsilon)\). The comparison of these three leading factors is the focus of the next subsection.

## Appendix C.4. Ordering of the three leading factors

In this subsection, we make two claims required in the main text:

**Proposition 1.** _Under_ (C.1)_, for each_ \(\mu\in\{-\sqrt{3},0,\sqrt{3}\}\)_, the quantity_ \(|\mathcal{G}_\mu^{(0)}(k)|\) _is an even function of_ \(\zeta=k\Delta x\) _and is nonincreasing with respect to_ \(|\zeta|\) _on_ \(0\le|\zeta|\le\pi\)_. In particular,_

\(|\mathcal{G}_\mu^{(0)}(k)|\le 1,\mu\in\{-\sqrt{3},0,\sqrt{3}\},\) (C.20)

_and equality holds at k_=0.

