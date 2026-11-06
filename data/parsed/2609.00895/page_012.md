for some fixed constant \(0<\alpha_0<1\), and form the following linear system, obtained by discarding the remainder term _F<sub>n<sub>s</sub></sub>_ in (12)-(13):<tbc>

\(c_{n_s}=x_{n_s}\sum_{k=0}^{q-1}x_{n_s}^k[\kappa_{n_s}^{(+)}\widetilde{g}_k^+-\kappa_{n_s}^{(-)}\widetilde{g}_k^-],s=1,\dots,2q.\) (28)

<tbc>Introducing the polynomial pair<tbc>

\(\widetilde{G}^+(x):=\sum_{k=0}^{q-1}\widetilde{g}_k^+x^k,\widetilde{G}^-(x):=\sum_{k=0}^{q-1}\widetilde{g}_k^-x^k,\mathrm{deg}\widetilde{G}^\pm\le q-1,\)

<tbc>we can rewrite the system (28) as the interpolation problem<tbc>

\(\kappa_{n_s}^{(+)}\widetilde{G}^+(x_{n_s})-\kappa_{n_s}^{(-)}\widetilde{G}^-(x_{n_s})=\lambda_{n_s}c_{n_s},s=1,\dots,2q.\) (29)

<tbc>The coefficient matrix of (29) is<tbc>

\(\Lambda_N:=\left(\begin{array}{ c c c c c c c c c c c }
\kappa_{n_1}^{(+)} & \kappa_{n_1}^{(+)}x_{n_1} & \cdots & \kappa_{n_1}^{(+)}x_{n_1}^{q-1} & -\kappa_{n_1}^{(-)} & -\kappa_{n_1}^{(-)}x_{n_1} & \cdots & -\kappa_{n_1}^{(-)}x_{n_1}^{q-1} \\
\vdots & \vdots &  & \vdots &  & \vdots &  & \vdots &  & \vdots \\
\kappa_{n_2q}^{(+)} & \kappa_{n_2q}^{(+)}x_{n_2q} & \cdots & \kappa_{n_2q}^{(+)}x_{n_2q}^{q-1} & -\kappa_{n_2q}^{(-)} & -\kappa_{n_2q}^{(-)}x_{n_2q} & \cdots & -\kappa_{n_2q}^{(-)}x_{n_2q}^{q-1}
\end{array}\right).\)

<tbc>Thus, \(\Lambda_N\) is the block Vandermonde matrix (19) with the identification

\(\alpha_s:=\kappa_{n_s}^{(+)},\beta_s:=-\kappa_{n_s}^{(-)},x_s:=x_{n_s}.\)

Since \(\lambda_{n_s}\neq 0\), multiplying the _s_-th equation of (28) by \(\lambda_{n_s}\) does not change its solvability. Thus (28) and (29) are equivalent linear systems, and \(\Lambda_N\) is the coefficient matrix of the latter. Theorem 2.2 therefore gives an explicit criterion for the unique solvability of (28). By Theorem 2.4, when \(\Lambda_N\) is invertible, the solution is the unique pair of polynomials \(\widetilde{G}^\pm\) of degree at most _q_-1 satisfying (29).

## 3.2 Error polynomials

Comparing (28) with (12)-(13), we see that the error polynomials<tbc>

\(\Delta^\pm(x):=\sum_{k=0}^{q-1}(\widetilde{g}_k^\pm-g_k^\pm)x^k(\mathrm{deg}\le q-1)\)

<tbc>satisfy

\(\kappa_{n_s}^{(+)}\Delta^+(x_{n_s})-\kappa_{n_s}^{(-)}\Delta^-(x_{n_s})=\lambda_{n_s}F_{n_s},s=1,\dots,2q.\) (30)

From (30) and (14), setting

\(\Phi^\pm(x):=\Delta^\pm(x)-g_q^\pm x^q(\mathrm{deg}\le q),\) (31)

the system becomes the almost homogeneous system

\(\kappa_{n_s}^{(+)}\Phi^+(x_{n_s})-\kappa_{n_s}^{(-)}\Phi^-(x_{n_s})=\varepsilon_s,s=1,\dots,2q,\) (32)

where, by (14) and (27),

\(\varepsilon_s=\lambda_{n_s}\big(F_{n_s}-x_{n_s}^{q+1}[\kappa_{n_s}^{(+)}g_q^+-\kappa_{n_s}^{(-)}g_q^-]\big)=o(N^{-q})\text{uniformly in}s.\) (33)

The leading-order behavior of \(\Delta^\pm\) is thus governed by how small the left-hand side of (32) can be, and this depends on the parity of the indices _n<sub>s</sub>_, which we study in the next subsection.

