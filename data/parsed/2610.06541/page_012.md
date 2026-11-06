## 5. Layer-cake truncation and comparison

In this section, we extend bit truncation to levels that may better suit a problem, replacing \(d\lambda\) in the layer-cake identity \[20\]

\(x=\int_{(0,\infty)}\mathbf{1}_{\{\lambda\le x\}}d\lambda(x\ge 0)\)

with any level measure. We bound the Hamiltonian error, count pieces, and recover the fine-step comparison of Lemma 3.8, before proving the assembly bound (Theorem 5.5) used at unit steps in Section 6.

**Definition 5.1** (Level measure)**.** A _level measure_ \(\mu\) is the Stieltjes measure of a nondecreasing, right- continuous function _F_, zero on \((-\infty,0]\) and taking finitely many values on every \[0_,R_\]. Thus, \(F(x)=\mu((0,x])\) for \(x\ge 0\). Set

\([x]_\mu=\int_{(0,\infty)}\mathbf{1}_{\{\lambda\le x\}}d\mu(\lambda)=F(x)(x\ge 0),[-x]_\mu=-[x]_\mu.\)

Applying this entrywise to real and imaginary parts defines \(H^{(\mu)}\). The _discrepancy_ on \[0_,R_\] is \(D_R(\mu)=sup_{0\le x\le R}|x-F(x)|\). The _crossing number_ \(cr_\mu(x,y)\) is one less than the number of distinct values \([z]_\mu\) for \(min(x,y)\le z\le max(x,y)\). It counts the levels that a coordinate moving monotonically from _x_ to _y_ crosses, so it bounds how many times its truncation changes. For a map _q_ on \[0_,T_\], a _layer_ is a pre-image _q_<sup>-1</sup>({_v_}).

A uniform grid of spacing _c\>_0 corresponds to \(\mu=\sum_{m\ge 1}c\delta_{mc}\), with \([x]_\mu=ctrunc(x/c)\) and \(D_R(\mu)\le c\). Bit truncation uses spacing 2<sup>-_k_</sup>, and then \(cr_\mu(x,y)\) is about 2_<sup>k</sup>|x-y_|, the count in Proposition 4.2. We now extend Lemma 3.3, replacing 2<sup>-_k_</sup> by \(D_R(\mu)\).

**Theorem 5.2.** _Let_ \(\mu\) _be a level measure, and let H be a_ \(\sigma\)_-sparse family whose coordinates (Definition 4.1) have magnitude at most R for every t. Then_ \(H^{(\mu)}\) _is Hermitian, has a zero entry wherever H does and hence is_ \(\sigma\)_-sparse, and, for every t,_

\(\|H(t)-H^{(\mu)}(t)\|\le\sqrt{2}\sigma D_R(\mu).\)

_Proof._ The odd extension fixes zero, and oddness makes truncation of real and imaginary parts commute with complex conjugation, so \(H^{(\mu)}\) is Hermitian and preserves zeros. Since every coordinate lies in \[-_R,R_\], the definition of \(D_R(\mu)\) and oddness bound each coordinate error by \(D_R(\mu)\), hence each complex entry error by \(\sqrt{2}D_R(\mu)\), and the row-sum bound of Lemma 3.3 gives the result. □

We count pieces as in Proposition 4.2.

**Theorem 5.3.** _Let q be a map on_ \[0_,T_\] _taking finitely many values, with each layer q_<sup>-1</sup>({_v_}) _an interval. Then q is constant on each piece of a partition of_ \[0_,T_\] _into at most_ |_q_(\[0_,T_\])| _pieces (Definition 2.1). Consequently, if the coordinates h of H (Definition 4.1) are monotone on each interval_ \([\xi_r,\xi_{r+1}]\)_, where_ \(0=\xi_0<\cdots<\xi_N=T\)_, then, for each level measure_ \(\mu\) _with crossing number_ \(cr_\mu\) _(Definition 5.1),_ \(H^{(\mu)}\) _is piecewise constant, with at most_

\(\sum_{r=0}^{N-1}\big(1+\sum_hcr_\mu\big(h(\xi_r),h(\xi_{r+1})\big)\big)\)

_pieces._

_Proof._ Cut \[0_,T_\] at 0 and each layer’s supremum. These at most 1+|_q_(\[0_,T_\])| cuts include _T_, the supremum of its layer, giving at most |_q_(\[0_,T_\])| open pieces. Finitely many layers cover each piece (_a,b_), so one contains points arbitrarily close to _a_ and, being an interval, contains some (_a,c_) with _c\>a_. If it missed a point of (_a,b_), its supremum would be a cut inside the piece, a contradiction.

For \(t\in[\xi_r,\xi_{r+1}]\), monotonicity puts _h(t_) between \(h(\xi_r)\) and \(h(\xi_{r+1})\), so \([h(t)]_\mu\) takes at most \(1+cr_\mu(h(\xi_r),h(\xi_{r+1}))\) values. Rank them from 0 in the order in which \([h(t)]_\mu\) attains them. Since \([\cdot]_\mu\) is nondecreasing, \([h(t)]_\mu\) is monotone in _t_, so each rank is nondecreasing in _t_, the layers of the tuple of ranks are intervals, and the sum of the ranks increases whenever the tuple changes. Hence, the number of values of the tuple is at most the _r_th summand. Equal ranks give equal truncated coordinates, and Hermiticity determines the lower-triangular entries, so the first claim, applied to the tuple, bounds the pieces of \(H^{(\mu)}\) on \([\xi_r,\xi_{r+1}]\) by that summand. Summing over _r_ gives the bound. □

