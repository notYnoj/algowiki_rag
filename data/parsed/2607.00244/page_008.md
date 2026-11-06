where the last inequality holds by Item 2. Hence,

\((loglogn)^2>\frac{1}{4}log^2(3m).\) (2)

On the one hand,

\(log(r^{1/k})=log\left(\left(2^{\gamma logn/(loglogn)^2}\right)^{1/k}\right)=\frac{\gamma logn}{k(loglogn)^2}<\frac{\gamma\cdot 2log(3m)}{\frac{1}{4}log^2(3m)}=\frac{0.8(1-\beta)}{(\beta+\Delta)log(3m)},\)

where the inequality comes from the upper bound on the numerator by (1) and the lower bound on the denominator by (2).

On the other hand,

\(log\left(\frac{m+\delta mlog(3m)}{\beta m+\delta mlog(3m)}\right)=log\left(1+\frac{(1-\beta)m}{\beta m+\delta mlog(3m)}\right)\)<br> \(=log\left(1+\frac{1-\beta}{\beta+\delta log(3m)}\right)>\frac{0.8(1-\beta)}{\beta+\delta log(3m)}>\frac{0.8(1-\beta)}{(\beta+\delta)log(3m)}\ge\frac{0.8(1-\beta)}{(\beta+\Delta)log(3m)},\)

where the first inequality holds because for every \(x\in(0,1/2)\), log(1+_x)\>_0.8_x_, and by Item 3 \((1-\beta)/(\beta+\delta log(3m))\in(0,1/2)\), and the second inequality holds because log(3_m)\>_1.

Therefore,

\(\frac{m+\delta mlog(3m)}{\beta m+\delta mlog(3m)}>r^{1/k},\)

and we conclude.

By Claim 11, if \(|I|\le\beta m+\delta mlog(3m)\), then \(\alpha(G_\varphi)<m+\delta mlog(3m)\). By Theorem 8, this indeed implies that \(\varphi\) is unsatisfiable.

If instead, \(|I|>\beta m+\delta mlog(3m)\), there is a truth assignment that satisfies strictly more than \(\beta m\) clauses of \(\varphi\). So, in this promise-problem setting, we correctly concluded that \(\varphi\) is satisfiable. \(\blacktriangleleft\)

## 4 Coloring Approximation Hardness in Graphs of Bounded Twin-Width

We show the same hardness of approximation for Min Coloring as we showed in the previous section. The general strategy is the same but several elements need to be changed. The following consequence of [5, Thm. 14] and Theorem 7 is a convenient alternative to the mere Theorem 7 of Section 3.

\(\blacktriangleright\) **Theorem 12.** _There are positive constants_ \(\beta<1,\Delta,c\) _such that, for n-vertex graphs H of maximum degree at most_ \(\Delta\) _promised to satisfy one of the following two conditions_

_H is 3-colorable, or_

_no induced subgraph of H on at least_ \(\beta n\) _vertices is 3-colorable_

_determining which one holds requires_ \(2^{\Omega(n/log^cn)}\) _time, unless the ETH fails._

**Proof.** We run the linear reduction from 3-SAT-_B_ to 3-Coloring of [5, Thm. 14] on the hard instances of Theorem 7. To avoid a notational clash, we rename the constant \(\beta\) as \(\beta'<1\) in the latter theorem, and denote by _N_ the number of variables of the 3-SAT-_B_ instances, and by _m_ the number of clauses in each instance.

The reduction of [5] (see the description preceding Theorem 14) produces graphs with at most \(\kappa N\) vertices and maximum degree at most \(\Delta\) for some constants \(\kappa:=\kappa(B),\Delta\). The

