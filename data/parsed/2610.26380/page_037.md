<tbc>_of a mean-zero U-variate normal vector with covariance matrix_ \(\widetilde{C}_\mathbf{x}\)_, let_ \(\unknown_{-u}(\mathbf{x})\) _denote the vector_ \(\unknown(\mathbf{x})\) _with its uth component removed, and let_ \((\widetilde{C}_\mathbf{x})_{-u|u}:=(\widetilde{C}_\mathbf{x})_{-u,-u}-(\widetilde{C}_\mathbf{x})_{-u,u}(\widetilde{C}_\mathbf{x})_{u,-u}\)_. Finally, define_ \(\unknown_\mathbf{x}\in\mathbb{R}^U\) _by_<tbc>

\((\unknown_\mathbf{x})_u=\frac{x_u}{\sqrt{C_{uu}}}\cdot\frac{\phi(\alpha_u(\mathbf{x}))\unknown_{U-1}\big(\unknown_{-u}(\mathbf{x})-(\widetilde{C}_\mathbf{x})_{-u,u}\alpha_u(\mathbf{x});(\widetilde{C}_\mathbf{x})_{-u|u}\big)}{\unknown_U(\unknown(\mathbf{x});\widetilde{C}_\mathbf{x})},u=1,\dots,U.\)

<tbc>_For U_=1_, the_ \(\unknown_{U-1}\) _factor is_ 1_. Then_

\((i)\mathbb{P}(\mathbf{X}=\mathbf{x}|n,p_{t-1})=\unknown_U(\unknown(\mathbf{x});\widetilde{C}_\mathbf{x}),\) (A.3)

\((ii)\unknown_t(\mathbf{x}|n,p_{t-1})=\unknown_{t-1}+\sum_{u=1}^U\beta_{j_u}(\unknown_\mathbf{x})_u\Sigma_{t-1}(\mathbf{e}_{i_u}-\mathbf{e}_{j_u}).\) (A.4)

Substituting (A.3) and (A.4) into (A.2) gives an explicit expression for \(V_\mathrm{myopic}(\cdot|p_{t-1})\). Since the general formula is not easy to read in its full _U_-dimensional form, we first work out the cases _U_=1 and _U_=2. These examples also point to the intractability for larger batches. Exact evaluation of (A.2) requires a sum over 2_<sup>U</sup>_ outcome vectors, with a _U_-dimensional multivariate normal CDF in each term. These CDFs must be evaluated numerically, which becomes expensive as _U_ grows (Genz and Bretz 2009). This motivates the approximate value function introduced in §A.2.2.

_Single evaluation (U_=1). Consider a batch with a single evaluation (_i_<sub>1</sub>_,j_<sub>1</sub>)=(_i,j_). Then \(C_{11}=1+\beta_j^2\sigma_{t-1,ij}^2\) and \(\alpha_1(x)=x\beta_j(\mu_{t-1,i}-\mu_{t-1,j})/\sqrt{C_{11}}\) for \(x\in\{-1,1\}\), so

\(\mathbb{P}(X=x|n,p_{t-1})=\Phi(\alpha_1(x)),\lambda_x=\frac{x\phi(\alpha_1(x))}{\Phi(\alpha_1(x))\sqrt{C_{11}}},\)<br>
\(\unknown_t(x|n,p_{t-1})=\unknown_{t-1}+\frac{x\beta_j\phi(\alpha_1(x))}{\Phi(\alpha_1(x))\sqrt{C_{11}}}\Sigma_{t-1}(\mathbf{e}_i-\mathbf{e}_j).\)

_Two evaluations (U_=2). Consider a batch with two evaluations (_i<sub>u</sub>,j<sub>u</sub>),u_=1,2. Then \(C_{uu}=1+\beta_{ju}^2\sigma_{t-1,i_uj_u}^2\), \(C_{12}=\beta_{j_1}\beta_{j_2}(\mathbf{e}_{i_1}-\mathbf{e}_{j_1})^\top\Sigma_{t-1}(\mathbf{e}_{i_2}-\mathbf{e}_{j_2})\), and \(\alpha_u(\mathbf{x})=x_u\beta_{j_u}(\mu_{t-1,i_u}-\mu_{t-1,j_u})/\sqrt{C_{uu}}\), and the correlation matrix \(\widetilde{C}_\mathbf{x}\) has off-diagonal entry \(x_1x_2\rho_{12}\) with \(\rho_{12}:=C_{12}/\sqrt{C_{11}C_{22}}\). Hence, for \(\mathbf{x}=(x_1,x_2)\in\{-1,1\}^2\), \(\mathbb{P}(\mathbf{X}=\mathbf{x}|n,p_{t-1})=\Phi_2\big(\alpha_1(\mathbf{x}),\alpha_2(\mathbf{x});x_1x_2\rho_{12}\big)\) and, for \(\{u,u'\}=\{1,2\}\),

\((\unknown_\mathbf{x})_u=\frac{x_u}{\sqrt{C_{uu}}}\cdot\frac{\phi(\alpha_u(\mathbf{x}))\Phi\left(\frac{\alpha_{u^\prime}(\mathbf{x})-x_1x_2\rho_{12}\alpha_u(\mathbf{x})}{\sqrt{1-\rho_{12}^2}}\right)}{\Phi_2\big(\alpha_1(\mathbf{x}),\alpha_2(\mathbf{x});x_1x_2\rho_{12}\big)},\unknown_t(\mathbf{x}|n,p_{t-1})=\unknown_{t-1}+\sum_{u=1}^2\beta_{j_u}(\unknown_\mathbf{x})_u\Sigma_{t-1}(\mathbf{e}_{i_u}-\mathbf{e}_{j_u}).\)

## A.2.2. Decomposing the myopic batch value

To obtain a tractable approximation of \(V_\mathrm{myopic}(\cdot|p_{t-1})\) when _U_ is large, we first decompose the myopic value of the batch into terms, one for each subset of the batch, and refer to the size of the subset (how many evaluations are in it) as the order of its term. We then approximate _V_<sub>myopic</sub>(_n|p_<sub>_t_-1</sub>) by truncating this decomposition at some order _w_, keeping all terms of order at most _w_ and discarding the rest.

Fix a batch with count matrix _n_ and ordered evaluations (_i_<sub>1</sub>_,j_<sub>1</sub>)_,...,(i<sub>U</sub>,j<sub>U</sub>_). For any subset \(G\subseteq\{1,\dots,U\}\), let _n<sub>G</sub>_ denote the sub-batch consisting of the evaluations whose positions are in _G_, and for any subset \(H\subseteq\{1,\dots,U\}\), define its _interaction term_<tbc>

\(\Gamma_H:=\sum_{G\subseteq H}(-1)^{|H|-|G|}V_\mathrm{myopic}(n_G|p_{t-1}).\)

