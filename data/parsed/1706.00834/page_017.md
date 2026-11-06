<tbc>where \(\unknown\in\mathbb{N}^{|M|}\) is the best multipath and _L_<sup>∗</sup> its loss. Define \(\widehat{\mathbf{f}}^\mathrm{init}:=\frac{1}{|M|}\mathbf{1}\) where \(\mathbf{1}\in\mathbb{R}^{|M|}\) is a vector of all ones. Now let the initial point **_f_**init be the relative entropy projection of \(\widehat{\mathbf{f}}^\mathrm{init}\) onto the unit-flow polytope<sup>6</sup><tbc>

\(\mathbf{f}^\mathrm{init}=\mathrm{arg}\mathrm{min}_{\mathbf{f}\in P}\Delta(\mathbf{f}||\widehat{\mathbf{f}}^\mathrm{init}).\)

<tbc>Now we have:

\(\Delta(\unknown||\mathbf{f}^\mathrm{init})\le\Delta(\unknown||\widehat{\mathbf{f}}^\mathrm{init})\text{(Generalized Pythagorean Thm.)}\) (11)

\(\le D(\mathrm{log}|M|)+D\mathrm{log}D+|M|\frac{1}{|M|}-\sum_{m\in M}\pi_m\le D\mathrm{log}|M|+D\mathrm{log}D.\)

Thus, by Inequality (10) the regret bound will be:<tbc>

\(\mathcal{R}_\mathrm{CH}\le\sqrt{2L^*D\left(\mathrm{log}|M|+\mathrm{log}D\right)}+D\mathrm{log}|M|+D\mathrm{log}D.\)

<tbc>Note that if \(\unknown\) is a bit vector, then \(\sum_{m\in M}\pi_m\mathrm{log}\pi_m=0\), and consequently, the expression (11) can be bounded as follows:

\(\Delta(\unknown||\mathbf{f}^\mathrm{init})\le\sum_{m\in M}\pi_m(\mathrm{log}|M|)+\sum_{m\in M}\pi_m\mathrm{log}\pi_m+\sum_{m\in M}\frac{1}{|M|}-\sum_{m\in M}\pi_m\le D(\mathrm{log}|M|)+|M|\frac{1}{|M|}-\sum_{m\in M}\pi_m\le D\mathrm{log}|M|.\)

Again, using Inequality (10), the regret bound will be:

\(\mathcal{R}_\mathrm{CH}\le\sqrt{2L^*D\mathrm{log}|M|}+D\mathrm{log}|M|.\)

Notice that by setting |_U_|=1 for all multiedge \((v,U)\in M\) and |T|=1, the algorithm for path learning in Koolen et al. (2010) is recovered. Also observe that Theorem 2 is a corollary of Theorem 14 since every path is represented as a bit vector and \(|M|=|E|\le|V|^2\).<tbc>

6. This computation can be done as a pre-processing step.

