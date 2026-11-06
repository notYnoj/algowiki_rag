### 9.3 Solar MSW and the LMA Solution

In the adiabatic limit the solar survival probability is \[19, 59, 75\] \(P_{ee}^\odot=\frac{1}{2}+\frac{1}{2}cos2\theta_{12}^\mathrm{prod}cos2\theta_{12}\). For the Large Mixing Angle solution at \(E\unknown 1\mathrm{MeV}\), \(\theta_{12}^\mathrm{prod}\approx\pi/2\) and \(P_{ee}^\mathrm{LMA}\approx sin^2\theta_{12}\approx 0.31\), in agreement with SNO \[5\] and Borexino \[76\]. This regime is a tangent to the constant-density LBL focus and is included only for completeness.

## 10 Resummation Interpretation of the DMP Rotation

### 10.1 Origin of the Divergence

The divergence near \(\hat{A}\rightarrow 1\) arises because the unperturbed Hamiltonian (at \(\alpha=0\)) has eigenvalues _V_<sub>CC</sub> and \(\Delta m_{31}^2/(2E)\) that become degenerate at \(\hat{A}=1\); the perturbative denominator \(\Delta\lambda_{13}^{(0)}\sim(1-\hat{A})\Delta m_{31}^2/(2E)\) then vanishes.

### 10.2 DMP Rotation as a Resummation

The DMP procedure \[47\] first performs an exact rotation in the 13-sector by \(\theta_{13}^M\), \(H_e=R_{13}^{-1}(\theta_{13}^M)H_\mathrm{f}R_{13}(\theta_{13}^M)\), after which the 13-sector off-diagonals vanish exactly. The remaining expansion parameter is \[47, 43\]

\(\epsilon_0=\frac{\Delta m_{21}^2}{\Delta m_{ee}^2}sin(\theta_{13}^M-\theta_{13})s_{12}c_{12},|\epsilon_0|\le\frac{\Delta m_{21}^2}{\Delta m_{ee}^2}s_{12}c_{12}\lesssim 0.015,\) (46)

where the upper bound follows from \(|sin(\theta_{13}^M-\theta_{13})|\le 1\) and is reached only near the atmospheric resonance. The key point is that \(\epsilon_0\) is bounded uniformly in \(\hat{A}\): the resonant denominator that was unbounded in the naive expansion is absorbed into the matter rotation angle \(\theta_{13}^M\), leaving a finite expansion parameter at all energies. The series \(P_{\mu e}^\mathrm{DMP}=P_{\mu e}^{(0)}+\epsilon_0P_{\mu e}^{(1)}+\epsilon_0^2P_{\mu e}^{(2)}+\cdots\) therefore converges uniformly in energy. The original DMP papers \[47, 43\] demonstrate the 10<sup>-4</sup> accuracy numerically; the complementary question of rotations versus perturbative expansions is analysed in detail by Denton, Parke, and Zhang \[48\]. What the present framing adds is the reason why this accuracy follows from first principles: the DMP rotation is a degenerate-eigenvalue resummation, in which the troublesome \((1-\hat{A})^{-1}\) is absorbed into \(\theta_{13}^M\) and replaced by the bounded \(\epsilon_0\).

\begin{tabular}{ccc}
Scheme & Expansion par. & Near \(\hat{A}=1\) \\
Madrid/AJLOS \[49, 45\] & \(\epsilon_{13}\), \(\alpha\) & \(\mathcal{O}((1-\hat{A})^{-1})\) \\
MP \[46\] & \(\alpha\) & \(\mathcal{O}((1-\hat{A})^{-1})\) \\
DMP0 \[47\] & \(\epsilon_0\le 0.015\) & O(1) \\
DMP1 \[47\] & \(\epsilon_0^2\le 2\times 10^{-4}\) & O(1) \\
NuFast \[44\] & \(X/X'\) & O(1) \\
\end{tabular}

6: Behavior of the expansion parameter near \(\hat{A}=1\) in various schemes. The uniform bound \(\epsilon_0\le 0.015\) distinguishes the DMP resummation from the naive expansion. Entries summarize the scaling reported in the cited works.

