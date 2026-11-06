**Definition 14** (Centered aggregate)**.** _For_ \(P\subseteq F\)_, define_

\(\mathcal{A}_\mathcal{S}(P)=\sum_{\mathbf{j}\in\unknown 0,n\unknown^{F\backslash P}}\left(\sum_{1\le t\le mP\subseteq U_t}\Gamma_{U_t}^P(X^{(t)})_\mathbf{j}\right)\left(\sum_{1\le t\le mP\subseteq V_t}\Gamma_{V_t}^P(Y^{(t)})_\mathbf{j}\right)\left(\sum_{1\le t\le mP\subseteq W_t}\Gamma_{W_t}^P(Z^{(t)})_\mathbf{j}\right),\) (82)

_For nonempty P, the correction_ (-1)<sup>|_P_|</sup>(_n_+1)<sup>|_P_|</sup>A<sub>S</sub>(_P_) _is called a_ singleton, pair, triple_, or_ quadruple _correction when_ |_P_|=1,2,3,4_, respectively. The name specifies the number of deleted coordinates._

Its rank satisfies

\(R\big(\mathcal{A}_\mathcal{S}(P)\big)\le(n+1)^{d-|P|}.\) (83)

**Definition 15** (Mixed trilinear form)**.** _For three selected tensor blocks X_<sup>(_i_)</sup>_,Y_<sup>(_j_)</sup>_,Z_<sup>(_k_)</sup>_, whose modes are indexed by_ \(U_i^c,V_j^c,W_k^c\)_, respectively, define_

\(\phi_{ijk}=\sum_{\unknown\in\unknown 0,n\unknown^F}\Gamma_{U_i}(X^{(i)})_\unknown\Gamma_{V_j}(Y^{(j)})_\unknown\Gamma_{W_k}(Z^{(k)})_\unknown.\) (84)

_Its set of replicated coordinates is_ \(\mathcal{R}_{ijk}=U_i\cap V_j\cap W_k\).

Expanding the inner sums in Definition 14 gives

\(\mathcal{A}_\mathcal{S}(P)=(n+1)^{-|P|}\sum_{i,j,kP\subseteq\mathcal{R}_{ijk}}\phi_{ijk},\) (85)

since summing over each coordinate in _P_ contributes a factor _n_+1. For any family Q of nonempty subsets of _F_, define

\(c_\mathcal{Q}(R)=1+\sum_{P\in\mathcal{Q}P\subseteq R}(-1)^{|P|}(R\subseteq F).\) (86)

Then

\(\mathcal{A}_\mathcal{S}(\emptyset)+\sum_{P\in\mathcal{Q}}(-1)^{|P|}(n+1)^{|P|}\mathcal{A}_\mathcal{S}(P)=\sum_{i,j,k}c_\mathcal{Q}(\mathcal{R}_{ijk})\phi_{ijk}.\) (87)

Retain the local multiplicity notation \(\eta_r(i,j,k)\) from Section 5.2. A mixed choice is annihilated by centering whenever \(\eta_r=2\) for some _r_. If it has no coordinate of multiplicity two and \(\mathcal{R}_{ijk}\neq\emptyset\), its replicated coordinates can be removed by inclusion-exclusion.

**Definition 16** (Correction support)**.** _The correction support is_

\(\mathcal{P}(\mathcal{S})=\left\{\begin{array}{ c }
P\subseteq F\left|\begin{array}{ c }
P\neq\emptyset,\text{\textit{and there exist}}i,j,k\text{\textit{such that}} \\
P\subseteq\mathcal{R}_{ijk},(i,j,k)\notin\{(t,t,t):1\le t\le m\},\eta_r(i,j,k)\neq 2\text{\textit{for all}}r
\end{array}\right\}.\) (88)

Let

\(\kappa_s=\big|\{P\in\mathcal{P}(\mathcal{S}):|P|=s\}\big|\) (89)

and define the multiplication budget for the main aggregate \(\mathcal{A}_\mathcal{S}(\emptyset)\) and the corrections A<sub>S</sub>(_P_) indexed by \(P\in\mathcal{P}(\mathcal{S})\)

\(\rho_\mathcal{S}(n)=(n+1)^d+\sum_{P\in\mathcal{P}(\mathcal{S})}(n+1)^{d-|P|}=(n+1)^d+\sum_{s=1}^d\kappa_s(n+1)^{d-s}.\) (90)

**Definition 17** (Mixed products after replicated-term cancellation)**.** _The mixed choices not eliminated by centering and the corrections indexed by_ P(S) _are_

\(\mathcal{B}(\mathcal{S})=\{(i,j,k)\notin\{(t,t,t):1\le t\le m\}:\eta_r(i,j,k)\le 1\text{\textit{for every}}r\in F\}.\) (91)

