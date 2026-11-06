## 13 Uncertainty Propagation

### 13.1 Parameter Space and Covariance

The probabilities depend on \(\mathbf{p}=(\theta_{12},\theta_{13},\theta_{23},\delta_\mathrm{CP},\Delta m_{21}^2,\Delta m_{31}^2)\), with Taylor expansion \(P(E;\mathbf{p})=P_0(E)+J(E)\cdot(\mathbf{p}-\unknown)+\frac{1}{2}(\mathbf{p}-\unknown)^TH_P(E)(\mathbf{p}-\unknown)+\cdots\).  8 lists the dominant variance contributions.

### 13.2 Monte Carlo and Jacobian Schemes

Drawing _N_ samples \(\mathbf{p}_i\sim\mathcal{N}(\unknown,\Sigma)\) and evaluating _P<sub>i</sub>(E_) yields the mean and percentile band \[_P_<sub>16</sub>_,P_<sub>84</sub>\]; for _N_=500 the statistical uncertainty on the percentiles is below 1% of the band width. The Jacobian scheme uses \(\mathrm{Var}[P(E)]\approx J(E)\Sigma J(E)^T\) with the closed- form derivatives below. It is convenient to define the two oscillatory structure factors<tbc>

\(\mathcal{S}_\mathrm{a}\equiv\frac{\mathrm{sin}[(1-\hat{A})\Delta]}{1-\hat{A}},\mathcal{S}_\mathrm{i}\equiv\frac{\mathrm{sin}(\hat{A}\Delta)}{\hat{A}},\) (50)

<tbc>so that \(P_{\mu e}=4s_{23}^2s_{13}^2c_{13}^2\mathcal{S}_\mathrm{a}^2+8\alpha J_\mathrm{CP}\mathrm{cos}(\Delta+\delta_\mathrm{CP})\mathcal{S}_\mathrm{i}\mathcal{S}_\mathrm{a}+4\alpha^2c_{13}^2c_{23}^2s_{12}^2c_{12}^2\mathcal{S}_\mathrm{i}^2\). The complete set of six analytic Jacobian components \(J_k=\partial P_{\mu e}/\partial p_k\) is then

\(\frac{\partial P_{\mu e}}{\partial\theta_{13}}=8s_{23}^2s_{13}c_{13}\mathrm{cos}2\theta_{13}\mathcal{S}_\mathrm{a}^2+8\alpha\frac{\partial J_\mathrm{CP}}{\partial\theta_{13}}\mathrm{cos}(\Delta+\delta_\mathrm{CP})\mathcal{S}_\mathrm{i}\mathcal{S}_\mathrm{a},\) (51)

\begin{tabular}{cccc}
Parameter & \(\sigma_i\) & \(f_i(P_{\mu e})\) & \(f_i(P_{\mu\mu})\) \\
\(\delta_\mathrm{CP}\) & \(\sim 33^\circ\) & 0.90 & 0.17 \\
\(\theta_{23}\) & \(0.9^\circ\) & 0.06 & 0.82 \\
\(\theta_{13}\) & \(0.11^\circ\) & 0.04 & _\<_0.01 \\
\(\theta_{12}\) & \(0.70^\circ\) & _\<_0.01 & 0.01 \\
\(\Delta m_{21}^2\) & \(0.19\times 10^{-5}\mathrm{eV}^2\) & _\<_0.01 & 0.01 \\
\(\Delta m_{31}^2\) & \(0.024\times 10^{-3}\mathrm{eV}^2\) & _\<_0.01 & _\<_0.01 \\
\end{tabular}

8: Fractional variance contributions \(f_i=J_i^2\sigma_i^2/\mathrm{Var}[P]\) for the T2K/HK configuration (_L_=295km, \(\rho=2.6\mathrm{gcm}^{-3}\)), computed by closed-form linearization (Section 13.2) using the NuFIT 6.0 with-SK NO central values and \(1\sigma\) widths of  1. Contributions are averaged over the appearance band \(E\in[0.45,0.85]\mathrm{GeV}\) for \(P_{\mu e}\) (first appearance maximum) and over the same band for \(P_{\mu\mu}\) (first disappearance maximum). The \(\delta_\mathrm{CP}\) dominance of the \(P_{\mu e}\) budget is a direct consequence of the large NuFIT 6.0 \(\delta_\mathrm{CP}\) uncertainty (\(\sigma\approx 33^\circ\)) relative to the now sub-percent \(\theta_{13}\) precision (\(\sigma=0.11^\circ\)). For \(P_{\mu\mu}\), \(\Delta m_{31}^2\) governs the _position_ of the minimum rather than its depth; the small _f<sub>i</sub>_ quoted here reflects the band being symmetric about the minimum, and its weight is larger in a spectral fit.

