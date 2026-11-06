### 5.6 Matter-Modified Mixing Angles

In the DMP framework \[47\] the matter-mixing angles satisfy the two-flavor block relations

\(\mathrm{sin}^22\theta_{13}^M=\frac{\mathrm{sin}^22\theta_{13}}{(\mathrm{cos}2\theta_{13}-\hat{A})^2+\mathrm{sin}^22\theta_{13}},\) (28)

\(\mathrm{sin}^22\theta_{12}^M\approx\frac{\mathrm{sin}^22\theta_{12}}{(\mathrm{cos}2\theta_{12}-c_{13}^2\hat{A}/\alpha)^2+\mathrm{sin}^22\theta_{12}},\) (29)

with \(\theta_{23}^M=\theta_{23}\) to this order. At resonance \(\hat{A}=\mathrm{cos}2\theta_{13}\), \(\mathrm{sin}^22\theta_{13}^M=1\), confirming maximal 1-3 mixing; the distinct quantity \(|V_{ee3}|^2=\mathrm{sin}^2\theta_{13}^M\) should not be conflated with \(\mathrm{sin}^22\theta_{13}^M\).

## 6 Density-Matrix Formalism

### 6.1 Pure-State Density Matrix and Von Neumann Equation

For a neutrino produced in flavor \(\alpha\), the density matrix \(\varrho(0)=|\nu_\alpha\rangle\langle\nu_\alpha|\) satisfies \(id\varrho/dx=[H_\mathrm{f},\varrho]\), with \(\varrho(L)=S(L)\varrho(0)S^\dagger(L)\) and

\(P_{\alpha\beta}(L)=\mathrm{Tr}[\Pi_\beta\varrho(L)]=|S_{\beta\alpha}(L)|^2,\Pi_\beta=|\nu_\beta\rangle\langle\nu_\beta|.\) (30)

In the mass basis, \(\varrho_{ij}^\mathrm{mass}(L)=\varrho_{ij}^\mathrm{mass}(0)e^{-i\Delta\lambda_{ij}L/(2E)}\): coherences oscillate at the rescaled eigenvalue differences \(\Delta\lambda_{ij}/(2E)\) while populations are constant.

### 6.2 Lindblad Master Equation

The general Markovian master equation preserving complete positivity and trace is the Lindblad equation \[31, 32\]<tbc>

\(\frac{d\varrho}{dx}=-i[H_\mathrm{f},\varrho]+\sum_k\left[L_k\varrho L_k^\dagger-\frac{1}{2}\{L_k^\dagger L_k,\varrho\}\right].\) (31)

<tbc>The simplest mass-basis model gives \(\varrho_{ij}^\mathrm{mass}(L)=\varrho_{ij}^\mathrm{mass}(0)e^{-i\Delta\lambda_{ij}L/(2E)}e^{-\Gamma_{ij}L}\), \(i\neq j\), modifying the probability to

\(P_{\alpha\beta}^\mathrm{dec}(L)=\delta_{\alpha\beta}-4\sum_{i>j}\mathrm{Re}[V_{e\beta i}V_{e\alpha i}^*V_{e\beta j}^*V_{e\alpha j}]\mathrm{sin}^2\frac{\Delta\lambda_{ij}L}{4E}e^{-\Gamma_{ij}L}\)<br>
\(+2\sum_{i>j}\mathrm{Im}[V_{e\beta i}V_{e\alpha i}^*V_{e\beta j}^*V_{e\alpha j}]\mathrm{sin}\frac{\Delta\lambda_{ij}L}{2E}e^{-\Gamma_{ij}L}.\) (32)

Current bounds are at the level \(\Gamma_{ij}\lesssim 10^{-23}\mathrm{GeV}\) \[33, 34\].

\begin{tabular}{cccc}
Method & Iterations & \(|X(\lambda)|\) & \(|\Delta P|/P_\mathrm{exact}\) \\
DMP0 seed & 0 & ∼10<sup>-3</sup> & ∼10<sup>-4</sup> \\
+1 NR step & 1 & ∼10<sup>-7</sup> & ∼10<sup>-9</sup> \\
+2 NR steps & 2 & ∼10<sup>-14</sup> & _\<_10<sup>-13</sup> \\
+1 Halley & 1 & ∼10<sup>-14</sup> & _\<_10<sup>-13</sup> \\
\end{tabular}

4: Newton-Raphson (NR) versus Halley convergence for \(\lambda_3\) at the DUNE configuration near \(E=E_{\hat{A}=1}\). Values are indicative of the tested point and are not a parameter-space-wide guarantee.

