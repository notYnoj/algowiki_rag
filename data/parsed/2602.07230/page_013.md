<tbc>singular digraph, so the total flow on _a_ is strictly less than<tbc>

\(\frac{c_a}{(n+1)}+d_\mathrm{max}\sum_{\alpha=1}^{n+1}u_\alpha\)

<tbc>with the first term coming from the copy that contains the forward path(s) of the sinks of the group. Since<tbc>

\(\sum_\alpha u_\alpha=\sum_\alpha a_\alpha+(n+1)\cdot\varepsilon\le 1+(n+1)\varepsilon\text{and}\varepsilon\le\frac{1}{(n^2-1)(n+1)},\)

<tbc>we obtain

\(\frac{c_a}{(n+1)}+\left(1-\frac{1}{n}\right)\cdot c_\mathrm{min}\cdot\left(1+(n+1)\cdot\varepsilon\right)\le c_a\cdot\left(\frac{1}{(n+1)}+\frac{(n-1)}{n}+\frac{(n^2-1)\cdot\varepsilon}{n}\right)\le c_a.\)

This implies that all capacity constraints are satisfied. We conclude that the critically split sinks require at most \((n+1)\cdot N_\mathrm{tot}\) rounds. Adding the _n_+1 rounds needed for non-critically split sinks, the total number of routing rounds is \((n+1)\cdot(N_\mathrm{tot}+1)\).

## 4.2 Special cases for the maximum routable demand

When _d_max_\<c_min, the maximum routable demand admits an approximation factor depending on the gap between _d_max and _c_min. The boundary case _d_max=_c_min remains open, both for routing in rounds and for maximizing routable demand. We now identify settings where additional constraints on source supplies yield constant-factor approximations for the maximum routable demand.

### Assuming \(d_\mathrm{max}\le\mathrm{min}_{s\in S^+}b(s)\).

Under this assumption, the derived SSUF instance with super- source _s_<sup>∗</sup> satisfies the balance condition, since each dummy arc (_s_<sup>∗</sup>_,s_) has capacity \(b(s)\ge d_\mathrm{max}\). By \[DGG99, Corollary 5.4\], at least \(0.226\cdot d_\mathrm{tot}\) units of demand can be routed in this SSUF instance without violating arc capacities, and thus also in the original unsplittable transshipment instance without exceeding source supplies. Hence, there exists a feasible unsplittable routing that serves at least \(0.226\cdot d_\mathrm{tot}\) total demand, with no demand split across sources.

### Assuming \(d_\mathrm{max}\le 1/2\cdot b_\mathrm{avg}^+\).

When \(d_\mathrm{max}\le c_\mathrm{min}/3\) (i.e., for _small_ demands), there exists a feasible six-round unsplittable routing; see Appendix E. Hence, in this case, at least \(1/6\cdot d_\mathrm{tot}\) can be routed unsplitably in a single round. We therefore restrict our attention to the complementary case of _large_ demands in \[_d_max/3_,d_max\], which in particular contains \[_c_min/3_,d_max\].

Assume in the following that demands lie in the range \[_d_max/3_,d_max\] and that we are additionally given \(d_\mathrm{max}\le 1/2\cdot b_\mathrm{avg}^+=^{d_\mathrm{tot}/2|S^+|}\). Applying the original DGG algorithm to the derived SSUF instance with a super-source routes all demands unsplitably in four rounds \[DGG99, Lemma 4.2\]. When applied to unsplittable transshipment instances, individual sources may be overutilized, but by at most one sink \[DGG99, Theorem 3.7\], so the overutilization at any source is less than _d_max. Thus, the total overutilization is less than \(|S^+|\cdot d_\mathrm{max}\), which by assumption is at most \(1/2\cdot d_\mathrm{tot}\). Therefore, at least \(1/2\cdot d_\mathrm{tot}\) units of demand are routed without violating any source supply across the four rounds, and hence at least one round routes a feasible unsplittable flow of value at least \(1/4\cdot 1/2\cdot d_\mathrm{tot}=1/8\cdot d_\mathrm{tot}\). Thus, combining the cases of _small_ and _large_ demands, the<tbc>

