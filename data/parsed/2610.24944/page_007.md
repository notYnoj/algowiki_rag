## 5 Case Studies

### 5.1 Refining a Published Packing

The task is to place 34 non-overlapping regular pentagons of unit side length inside an equilateral triangle of minimum side length. Each pentagon has a center and orientation. The evaluator checks containment and overlap and measures the required triangle size.

Épi starts from a published arrangement with triangle side length approximately 12.9814 (Friedman, 2026). It jointly refines the pentagons’ centers and orientations, checking containment and overlap after each candidate update. The final side length is approximately 12.9756, a reduction of 0.0445%. The released coordinates specify the construction at full precision.

Figure 3 shows nine retained geometric constructions. For pentagons, the objective reduces the size of the enclosing triangle. The circle-packing tasks increase the common radius inside a fixed container (Specht, 2026). Each panel is drawn directly from the released coordinates.

### 5.2 Separating the Cohn–Elkies Bound from Packing Density

The Cohn–Elkies method bounds sphere-packing density from above by optimizing an auxiliary function. We ask whether its best possible bound can equal the actual packing density. A strict separation would establish a limitation of the method itself.

Let \(\rho_d\) be the optimal sphere-packing center density in dimension _d_, and let _C<sub>d</sub>_ be the best upper bound attainable by the Cohn–Elkies linear program in the same normalization. Then \(\rho_d\le C_d\). To prove that the method is not sharp, it is enough to find a packing upper bound _U<sub>d</sub>_ and a lower bound _L<sub>d</sub>_ on the linear program’s optimum such that

\(\rho_d\le U_d<L_d\le C_d.\) (2)

The middle inequality creates a separation between the true packing problem and the best answer available from this method.

\begin{tabular}{cccc}
**Quantity** & **Previous bound** & **Épi** & **Evidence** \\
Wellens' D∞ ↓ & 4.393500 & 4.365467 & Rational witnesses \\
CE dual bounds ↑ & 1/20, 1/24, 1/24, 1/28 & 2: & \\
Spencer constant ↑ & 7/ √ 17 & 5/ √ 8 & All 256 sign assignments \\
Dimer entropy ↓ & 0.452130 & 0.452010 & Integer transfer inequalities \\
_n_-queens interval width & 3.30×10-7 & 3.94×10-9 & Rational and interval checks \\
Ramsey _c_<sub>4,5</sub> ↓ & 0.007932 & 0.007865 & A 1,024-vertex graph \\
MAX-4-CUT ratio ↓ & 0.987085 & 0.986411 & Integer weighted gadget \\
Klarner λ ↓ & 4.52380 & 4.29569 & Recurrence certificate \\
_Bh[g_] coefficients ↓ & Timmons'  1 & Five bounds, _h_=3_,...,_7 & Interval-certified kernels \\
Quartic dimension interval width & 7.80×10-3 & 2.13×10-9 & Full-domain interval proof \\
Quantum noise ↑ & 0.118371 & 0.1198803 & \\
(XZ / Two-Pauli) & 0.118067 & 0.1193415 & Positive coherent information \\
Waterund36 lower bound ↑ & 655.544171 & 662.807028 & Exact bound certificate \\
\end{tabular}



** 1:** Twenty numerical records across 12 families. Arrows indicate the improving direction. Interval widths are reduced. This overview uses rounded decimals. Precise bounds appear in the appendix and  2.

