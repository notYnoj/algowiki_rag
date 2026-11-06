For the reference configuration \(V_\mathrm{CC}\approx 9.8\times 10^{-14}\mathrm{eV}\). The neutral-current amplitude is flavor-universal and proportional to the identity in flavor space; it drops out after a global phase redefinition.

### 3.2 Flavor-Basis Hamiltonian and Schrödinger Equation

The matter-modified flavor Hamiltonian is

\(H_\mathrm{f}=\frac{1}{2E}U\mathrm{diag}(0,\Delta m_{21}^2,\Delta m_{31}^2)U^\dagger+\mathrm{diag}(V_\mathrm{CC},0,0),\) (6)

after subtracting \(m_1^2/(2E)\cdot\mathbf{1}\). _H_<sub>f</sub> is Hermitian, and the flavor state satisfies \(id\left|\nu(x)\right\rangle/dx=H_\mathrm{f}\left|\nu(x)\right\rangle\). For constant density,

\(\left|\nu(L)\right\rangle=S(L)\left|\nu(0)\right\rangle,S(L)=\mathrm{exp}(-iH_\mathrm{f}L),\) (7)

with _S(L_) unitary, so \(\sum_\beta P_{\alpha\beta}(L)=1\).

### 3.3 Numerical Stability: Hermitian Symmetrization

In floating-point arithmetic, construction of _U_ introduces anti-Hermitian noise at O(10<sup>-16</sup>). Projecting onto the Hermitian subspace via \(H_\mathrm{f}\leftarrow\frac{1}{2}(H_\mathrm{f}+H_\mathrm{f}^\dagger)\) removes this noise without altering the physics; afterward unitarity violations in _S(L_) are suppressed below O(10<sup>-10</sup>).

## 4 SU(3) Structure and the Evolution Operator

### 4.1 Embedding in the Lie Algebra u(3)

_H_<sub>f</sub> is an element of \(\mathfrak{u}(3)=\mathfrak{u}(1)\oplus\mathfrak{su}(3)\), with the u(1) factor the trace and the su(3) factor the traceless part. Since the trace contributes only an overall phase to _S(L_),

\(H_\mathrm{f}=\frac{\mathrm{Tr}H_\mathrm{f}}{3}\mathbf{1}+\tilde{H}_\mathrm{f},\mathrm{Tr}\tilde{H}_\mathrm{f}=0,\tilde{H}_\mathrm{f}\in\mathfrak{su}(3).\) (8)

The Gell-Mann matrices \(\{\lambda_a\}_{a=1}^8\) \[26\] give \(\tilde{H}_\mathrm{f}=\sum_ah_a\lambda_a/2\) with \(h_a=\mathrm{Tr}(H_\mathrm{f}\lambda_a)\) (Appendix C).

### 4.2 Invariants and the Characteristic Polynomial

With \(\Lambda\equiv 2EH_\mathrm{f}\) and invariants \(I_n=\mathrm{Tr}(H_\mathrm{f}^n)\), the characteristic equation is

\(\Lambda^3-I_1\Lambda^2+\frac{1}{2}(I_1^2-I_2)\Lambda-\frac{1}{6}(I_1^3-3I_1I_2+2I_3)=0.\) (9)

In terms of _a_=2_EV_<sub>CC</sub>,

\(A=I_1=\Delta m_{21}^2+\Delta m_{31}^2+a,\) (10)

\(B=\frac{1}{2}(I_1^2-I_2)=\Delta m_{21}^2\Delta m_{31}^2+a\big[\Delta m_{21}^2(1-|U_{e2}|^2)+\Delta m_{31}^2(1-|U_{e3}|^2)\big],\) (11)

\(C=\mathrm{det}(2EH_\mathrm{f})=a\Delta m_{21}^2\Delta m_{31}^2|U_{e1}|^2.\) (12)

These are the Le Verrier-Faddeev coefficients \[27\], computable without explicit matrix inversion.

