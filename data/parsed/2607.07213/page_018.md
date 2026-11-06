where the \(\mathcal{O}(\alpha^2\epsilon_{13})\) contribution from differentiating the \(c_{13}^2\) factor in _T_<sub>sol</sub> is dropped as beyond the \(\mathcal{O}(\alpha^2)\) accuracy of the perturbative probability;

\(\frac{\partial P_{\mu e}}{\partial\theta_{23}}=8s_{23}c_{23}s_{13}^2c_{13}^2\mathcal{S}_\mathrm{a}^2+8\alpha\frac{\partial J_\mathrm{CP}}{\partial\theta_{23}}\mathrm{cos}(\Delta+\delta_\mathrm{CP})\mathcal{S}_\mathrm{i}\mathcal{S}_\mathrm{a}-8\alpha^2c_{13}^2s_{23}c_{23}s_{12}^2c_{12}^2\mathcal{S}_\mathrm{i}^2,\) (52)

\(\frac{\partial P_{\mu e}}{\partial\theta_{12}}=8\alpha\frac{\partial J_\mathrm{CP}}{\partial\theta_{12}}\mathrm{cos}(\Delta+\delta_\mathrm{CP})\mathcal{S}_\mathrm{i}\mathcal{S}_\mathrm{a}+4\alpha^2c_{13}^2c_{23}^2\frac{\partial(s_{12}^2c_{12}^2)}{\partial\theta_{12}}\mathcal{S}_\mathrm{i}^2,\) (53)

\(\frac{\partial P_{\mu e}}{\partial\delta_\mathrm{CP}}=-8\alpha J_\mathrm{CP}\mathrm{sin}(\Delta+\delta_\mathrm{CP})\mathcal{S}_\mathrm{i}\mathcal{S}_\mathrm{a},\) (54)

\(\frac{\partial P_{\mu e}}{\partial\Delta m_{21}^2}=\frac{1}{\Delta m_{31}^2}\frac{\partial P_{\mu e}}{\partial\alpha},\frac{\partial P_{\mu e}}{\partial\alpha}=8J_\mathrm{CP}\mathrm{cos}(\Delta+\delta_\mathrm{CP})\mathcal{S}_\mathrm{i}\mathcal{S}_\mathrm{a}+8\alpha c_{13}^2c_{23}^2s_{12}^2c_{12}^2\mathcal{S}_\mathrm{i}^2,\) (55)

\(\frac{\partial P_{\mu e}}{\partial\Delta m_{31}^2}=\frac{\partial P_{\mu e}}{\partial\Delta}\frac{\partial\Delta}{\partial\Delta m_{31}^2}+\frac{\partial P_{\mu e}}{\partial\hat{A}}\frac{\partial\hat{A}}{\partial\Delta m_{31}^2}-\frac{\alpha}{\Delta m_{31}^2}\frac{\partial P_{\mu e}}{\partial\alpha},\) (56)

with \(\partial\Delta/\partial\Delta m_{31}^2=\Delta/\Delta m_{31}^2\), \(\partial\hat{A}/\partial\Delta m_{31}^2=-\hat{A}/\Delta m_{31}^2\), and \(\partial J_\mathrm{CP}/\partial\theta_{ij}\) obtained by dif ferentiating \(J_\mathrm{CP}=s_{12}c_{12}s_{23}c_{23}s_{13}c_{13}^2\). The two derivatives \(\partial P_{\mu e}/\partial\Delta\) and \(\partial P_{\mu e}/\partial\hat{A}\) follow from Eqs. (36)-(38) and (50) by direct differentiation of S<sub>a</sub>,S<sub>i</sub>; the explicit forms are collected in Appendix D. The two \(\delta_\mathrm{CP}\)- and \(\theta_{13}\)-derivatives, Eqs. (54) and (51), dominate the appearance-channel budget ( 8).

### 13.3 Boundary Caveat and Feldman-Cousins Validation

Wilks’ theorem is routinely violated in oscillation analyses due to physical boundaries, the cyclic variable \(\delta_\mathrm{CP}\in[0,2\pi)\), and discrete degeneracies. The Gaussian Jacobian linearization can produce unphysical negative probability excursions near \(\theta_{13}\rightarrow 0\) and near the cyclic boundary \(\delta_\mathrm{CP}\rightarrow 0\equiv 2\pi\). All Jacobian-based bands reported here are therefore validated against a Feldman-Cousins unified profile-likelihood mapping \[54\] before use in fits. Parameter correlations enter through the off-diagonal terms of the covariance matrix,

\(\mathrm{Var}[P]=\underbrace{\sum_iJ_i^2\sigma_i^2}_\text{diagonal}+2\underbrace{\sum_{i<j}J_iJ_j\Sigma_{ij}}_\text{correlation},\) (57)

so a diagonal-only error budget systematically misestimates the band width whenever the global fit reports non-negligible off-diagonal \(\Sigma_{ij}\). When the full covariance is available-- for example from a joint experimental likelihood, or from the public \(\chi^2\) profiles of the global fit \[15, 16\]--it should be propagated directly through Eq. (57); the closed-form Jacobian (Section 13.2) makes this a single matrix product.

## 14 Analytic Validation Against Limiting Cases

### Vacuum limit (\(\hat{A}\rightarrow 0\)).

By L’Hôpital’s rule \(\mathrm{sin}(\hat{A}\Delta)/\hat{A}\rightarrow\Delta\), \(\mathrm{sin}[(1-\hat{A})\Delta]/(1-\hat{A})\rightarrow\mathrm{sin}\Delta\), and \(\mathrm{sin}^2[(1-\hat{A})\Delta]/(1-\hat{A})^2\rightarrow\mathrm{sin}^2\Delta\), recovering

\(P_{\mu e}^\mathrm{vac}=4s_{23}^2s_{13}^2c_{13}^2\mathrm{sin}^2\Delta+8\alpha J_\mathrm{CP}\mathrm{cos}(\Delta+\delta_\mathrm{CP})\Delta\mathrm{sin}\Delta+4\alpha^2c_{13}^2c_{23}^2s_{12}^2c_{12}^2\Delta^2+\mathcal{O}(\alpha^3).\) (58)

### High-energy limit.

For \(E\rightarrow\infty\) at fixed _L,V_<sub>CC</sub>, \(\hat{A}\rightarrow\infty\), \(H_\mathrm{f}\rightarrow\mathrm{diag}(V_\mathrm{CC},0,0)\), and all three terms vanish: \(T_\mathrm{atm}\propto\hat{A}^{-2}\), \(T_\mathrm{int}\propto\hat{A}^{-1}\), \(T_\mathrm{sol}\propto\hat{A}^{-2}\).

