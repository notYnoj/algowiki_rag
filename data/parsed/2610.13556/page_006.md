<tbc>Every word is proper: its first letter differs from the other four, its second differs from its third, and its fourth differs from its fifth. Weighted letter counts verify each profile. In no position do both targets have _C_, so their _C_-classes are disjoint.

Here _N_=24_t_ and \(p_C\ge 9t\). By (3.2), every source of an unbalanced profile has a repair retaining at least \(\lceil 3t/2\rceil\) vertices. For the balanced profile (8_t,_8_t,_8_t_), the three cyclic relabelings of any proper target still have that profile and together agree once at every vertex. Some target therefore retains at least 8_t_ vertices. Consequently

\(B(2J_t)\le 24t-\left\lceil\frac{3t}{2}\right\rceil,2B(J_t)-B(2J_t)\ge\left\lceil\frac{3t}{2}\right\rceil.\)

Choose an integer _t\>_2_C/_3. Then \(\lceil 3t/2\rceil>C\), which gives the stated strict inequality. The upper bound on _B_(2_J<sub>t</sub>_) is all that is needed here; no exact value for it is asserted. □

## 4. Profile composition and repeated unions

The counterexamples in Section 3 show the effect of permitting color counts to move between components. We now retain the local profile data and derive exact composition laws. For repeated copies, these laws give eventual linear growth with periodic corrections under both repair rules. Weak repair has the explicit slope _F<sub>k</sub>(G_); ordinary repair has a rational slope described by a finite fractional optimization.

### 4.1. Weak repair and transfer of color counts.

To analyze arbitrary summands, their colorings must first be expressed in a common palette.

**Definition 4.1** (Common-palette radii)**.** Fix \(k\ge\chi(J)\), and let P_<sub>k</sub>(J_) be the set of proper maps from _V(J_) to \[_k_\]. These maps may leave some labels unused. Write

\(\mathcal{A}_k(J)=\left\{\mathbf{a}\in\mathbb{Z}_{\ge 0}^k:\sum_{i=1}^ka_i=|V(J)|\right\},\mathcal{M}_k(J)=\{\mathbf{m}(y):y\in\mathcal{P}_k(J)\}.\)

Thus A_<sub>k</sub>(J_) contains all source profiles, whereas M_<sub>k</sub>(J_) contains the profiles realized by proper colorings. The distinction matters even when \(k=\chi(J)\): a source restricted to one summand of a union need not have a feasible profile on that summand.

For every \(\mathbf{a}\in\mathcal{A}_k(J)\), define<tbc>

\(\rho_{J,k}(\mathbf{a})=\mathrm{max}_{w:V(J)\rightarrow[k]}\mathrm{min}_{y\in\mathcal{P}_k(J)}d_\mathrm{H}(w,y).\)

<tbc>We shall use the two maxima

\(\beta_k(J)=\mathrm{max}_{\mathbf{p}\in\mathcal{M}_k(J)}\rho_{J,k}(\mathbf{p}),F_k(J)=\mathrm{max}_{\mathbf{a}\in\mathcal{A}_k(J)}\rho_{J,k}(\mathbf{a}).\) (4.1)

The first is weak villainy with the fixed palette \[_k_\]; in particular, \(\beta_{\chi(J)}(J)=B_\mathrm{w}(J)\). The second is the _k_-fixing number studied by Garnero et al. \[9\], in which the source coloring is unrestricted. Put

\(\varepsilon_k(J)=F_k(J)-\beta_k(J)\ge 0.\)

This difference measures how much is lost by requiring the source profile to be feasible.

\begin{tabular}{cccc}
Profile divided by _t_ & \multicolumn{2}{c}{First target} & Second target \\
(4,10,10) & _BACAC_ | _BACAC_ & _CABAB_ | _CABAB_ \\
(5,9,10) & _BACAC_ | _CBAAB_ & _CBAAB_ | _BACAC_ \\
(6,8,10) & _BACAC_ | _CABBA_ & _CABBA_ | _BACAC_ \\
(6,9,9) & _BCAAC_ | _CBAAB_ & _CBAAB_ | _BCAAC_ \\
(7,7,10) & _ABCBC_ | _BACAC_ & _CABAB_ | _CABABA_ \\
(7,8,9) & _ACBBC_ | _CABAB_ & _CABAB_ | _ACBBC_ \\
\end{tabular}

