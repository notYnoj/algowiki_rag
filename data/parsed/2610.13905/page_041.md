where \(\Delta W=(\nu^{-1}\otimes I_{m/m_0})(W_\nu\otimes I_{m/m_0})-(\tilde{\nu}^{-1}\otimes I_{m/m_0})(\widetilde{W}_\nu\otimes I_{m/m_0})\). Applying (A.25) to the first term here yields

\(\left\|\left(\nu^{-1}\otimes I_{m/m_0}\right)\left(W_\nu\otimes I_{m/m_0}\right)\genfrac(){pt}{2}{M_1-\widetilde{M}_1}{\vdots}M_t-\widetilde{M}_t\right)\right\|\le\left\|\left(|\nu^{-1}|\cdot|W_\nu|\right)\genfrac(){pt}{2}{\left\|M_1-\widetilde{M}_1\right\|}{\vdots}\left\|M_t-\widetilde{M}_t\right\|\right\|_\infty\le\left((1+\delta)^4-1\right)(k/k_0^L)\left\|\left(|\nu^{-1}|\cdot|W_\nu|\right)\left((|\phi|\cdot|U_\phi|)^T\mathbb{1}\odot(|\psi|\cdot|V_\psi|)^T\mathbb{1}\right)\right\|_\infty E^{L-1}\|A\||B\|=\left((1+\delta)^4-1\right)(k/k_0^L)E^L\|A\||B\|.\) (A.27)

Similarly,

\(\left\|\Delta W\genfrac(){pt}{2}{\widetilde{M}_1}{\vdots}\widetilde{M}_t\right\|\le\left\|\Delta W\genfrac(){pt}{2}{\left\|\widetilde{M}_1\right\|}{\vdots}\widetilde{M}_t\right\|_\infty\le(2\delta+\delta^2)\left\|\left(|\nu^{-1}|\cdot|W_\nu|\right)\genfrac(){pt}{2}{\left\|M_t\right\|+((1+\delta)^4-1)(k/k_0^L)E^{L-1}\|A\||B\|\left((|\phi|\cdot|U_\phi|)^T\mathbb{1}\odot(|\psi|\cdot|V_\psi|)^T\mathbb{1}\right)_1}{\vdots}M_t\|+((1+\delta)^4-1)(k/k_0^L)E^{L-1}\|A\||B\|\left((|\phi|\cdot|U_\phi|)^T\mathbb{1}\odot(|\psi|\cdot|V_\psi|)^T\mathbb{1}\right)_t\right)\right\|_\infty\le(2\delta+\delta^2)\left\|\left(|\nu^{-1}|\cdot|W_\nu|\right)\genfrac(){pt}{2}{\left\|M_1\right\|}{\vdots}M_t\right\|_\infty+(2\delta+\delta^2)\left((1+\delta)^4-1\right)(k/k_0^L)\left\|\left(|\nu^{-1}|\cdot|W_\nu|\right)\left((|\phi|\cdot|U_\phi|)^T\mathbb{1}\odot(|\psi|\cdot|V_\psi|)^T\mathbb{1}\right)\right\|_\infty E^{L-1}\|A\||B\|\le(2\delta+\delta^2)(k/k_0^L)\left\|\left(|\nu^{-1}|\cdot|W_\nu|\right)\left((|\phi|\cdot|U_\phi|)^T\mathbb{1}\odot(|\psi|\cdot|V_\psi|)^T\mathbb{1}\right)\right\|_\infty E^{L-1}\|A\||B\|=((1+\delta)^6-(1+\delta^4)\left(k/k_0^L)E^L\|A\||B\|\) (A.28)

where we bound \(\|M_j\|\) by repeating the argument made above. Summing (A.27) and (A.28) yields

\(\|C-\widehat{C}\|\le\left((1+\delta)^6-1\right)(k/k_0^L)E^L\|A\||B\|.\) (A.29)

Combining this result with (A.21) implies that the stated bound holds for _L_ if it holds for _L_-1. To complete the proof, we note that the base case (when _L_=1) follows from the argument used to bound the first term \(\|C-\widehat{C}\|\), substituting (A.24) for the simpler bound (_k/k_<sub>0</sub>)∥_A_∥∥_B_∥ (since in this case the recursive call is replaced by matrix multiplication).

## B Encoding Matrices for \(\left\langle 2,4,5;31\right\rangle\)

This appendix contains encoding/residual matrices for a new APA \(\left\langle 2,4,5;31\right\rangle\) scheme, which establishes 31 as an upper bound on the border rank of \(\mathcal{M}_{\left\langle 2,4,5\right\rangle}\). The corresponding algorithm approximates the product of \(A\in\mathbb{C}^{2\times 4}\) and \(B\in\mathbb{C}^{4\times 5}\) - i.e.,

\(\left(\begin{array}{ c c c c c }
a_{11} & a_{12} & a_{13} & a_{14} \\
a_{21} & a_{22} & a_{23} & a_{24}
\end{array}\right)\times\left(\begin{array}{ c c c c c }
b_{11} & b_{12} & b_{13} & b_{14} & b_{15} \\
b_{21} & b_{22} & b_{23} & b_{24} & b_{25} \\
b_{31} & b_{32} & b_{33} & b_{34} & b_{35} \\
b_{41} & b_{42} & b_{43} & b_{44} & b_{45}
\end{array}\right)=\left(\begin{array}{ c c c c c }
c_{11} & c_{12} & c_{13} & c_{14} & c_{15} \\
c_{21} & c_{22} & c_{23} & c_{24} & c_{25}
\end{array}\right),\) (B.1)

and outputs

\(AB+\varepsilon^3R_3+\varepsilon^4R_4+\varepsilon^5R_5+\varepsilon^6R_6+\varepsilon^7R_7+\varepsilon^8R_8\) (B.2)

for a set of residual matrices _R_<sub>3</sub>_,R_<sub>4</sub>_,R_<sub>5</sub>_,R_<sub>6</sub>_,R_<sub>7</sub>_,R_<sub>8</sub> that depend on _A_ and _B_. Note that the search algorithm discussed in Section 2 actually found several \(\left\langle 2,4,5;31\right\rangle\) schemes; the one shown here achieves the largest improvement to its leading coefficient via sparsification (see row 15 of  2).

### B.1 Standard Basis Encoding Matrices

We first provide the encoding matrices for this scheme in the standard basis:

