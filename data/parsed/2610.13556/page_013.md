<tbc>For this fixed matrix and cost vector, the integer-programming proximity bound of Cook, Gerards, Schrijver, and Tardos \[4, Corollary 2\] gives a constant _D_, independent of **x**, such that

\(0\le C_G(\mathbf{x})-\Phi_G(\mathbf{x})\le D\) (4.19)

whenever an integer solution exists. To apply that bound, write the equalities as pairs of inequalities and include nonnegativity. The resulting integral constraint matrix and objective are fixed, and the row sums bound every feasible variable.

The function \(\Phi_G\) is convex and piecewise linear by linear programming duality. Its maximum on the rational polytope X_<sub>G</sub>_ is attained at a vertex. Such a vertex has at most _k_ positive coordinates: more than _k_ corresponding profile vectors would be linearly dependent, and a sufficiently small perturbation in that dependence would preserve both the average profile and the sum of the coordinates. Enumerating the vertices and solving the corresponding rational linear programs computes a rational value \(\Lambda(G)\). Any feasible integral source count vector with sum _m_ has \(\mathbf{x}/m\in\mathcal{X}_G\). Thus (4.19) gives \(B(mG)\le m\Lambda(G)+D\).

For the reverse bound, choose a rational maximizer \(\mathbf{x}^*\in\mathcal{X}_G\). Express its average profile as a rational convex combination of proper profiles, and choose a common denominator _d_ for these coefficients and **x**<sup>∗</sup>. Then _d_**x**<sup>∗</sup> is the source count vector of a feasible source on _dG_: the resulting integer numbers of source copies and proper target copies have the same total profile and may be paired arbitrarily. Fix a proper word _y_<sub>0</sub>. For _m=qd+r_, \(0\le r<d\), the integer vector **x**<sup>(_m_)</sup>=_qd_**x**<sup>∗</sup>+_r_**e**<sub>_y_<sub>0</sub></sub> is feasible. Take an optimal dual solution at **x**<sup>∗</sup>, and let **u** denote its coordinates corresponding to the row-sum constraints. Dual feasibility holds for every source count vector, so

\(B(mG)\ge C_G(\mathbf{x}^{(m)})\ge\Phi_G(\mathbf{x}^{(m)})\ge qd\Lambda(G)+ru_{y_0}=m\Lambda(G)-r(\Lambda(G)-u_{y_0}).\)

The final error is bounded independently of _m_, proving the first assertion of (4.17). The second follows from \(B(mG)\ge B_\mathrm{w}(mG)\) and Theorem 4.5.

Finally, the set of pairs (_m,b_) with _b=B(mG_) is definable in Presburger arithmetic, the language of integer linear inequalities and congruences combined by Boolean operations and quantifiers. Indeed, feasible sources, integer repairs, and their costs are described by the fixed linear system above. Let _P(m,t_) assert that some feasible integer source count vector of sum _m_ has every integer repair of cost at least _t_. This is a Presburger formula, and _B(mG_)=_b_ is expressed by \(P(m,b)\wedge\neg P(m,b+1)\). Write \(\Lambda(G)=a_0/h_0\) with integers \(a_0\ge 0\) and \(h_0\ge 1\). By (4.17), the integer _h_<sub>0</sub>_B(mG_)-_a_<sub>0</sub>_m_ belongs to a fixed finite set. For each of its possible values, the set of corresponding _m_ is a one-variable Presburger set, hence effectively eventually periodic by effective quantifier elimination \[10, 11\], which replaces a quantified formula by an equivalent formula without quantifiers. After elimination, each linear inequality is eventually constant and each congruence is periodic. Taking a common period _h_ divisible by _h_<sub>0</sub> and a common threshold proves (4.18). The proximity bound and the bound obtained from the dual solution are effective, so the finite set of possible errors can be bounded before applying quantifier elimination. □

Comparing this slope with the fixing-number slope in Theorem 4.5 determines whether the cost of preserving color counts accumulates under repetition.

**Corollary 4.12.** _For a fixed graph G with_ \(k=\chi(G)\),

\(B(mG)-B_\mathrm{w}(mG)=m\big(\Lambda(G)-F_k(G)\big)+O_G(1).\)

_The difference is bounded if and only if_ \(\Lambda(G)=F_k(G)\)_. In that case it is eventually periodic; otherwise it tends to infinity linearly. The boundedness condition is decidable from the finite linear programs defining_ \(\Lambda(G)\) _and the finite definition of F<sub>k</sub>(G)._

_Proof._ Subtract Theorem 4.5 from (4.17). When the two slopes agree, Theorems 4.6 and 4.11 give a common period for the difference. □

This gives a finite optimization criterion for bounded difference. A structural characterization of the graphs satisfying \(\Lambda(G)=F_{\chi(G)}(G)\) remains a separate question.

