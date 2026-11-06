<tbc>require confluence for sink _t_<sup>_q_+1</sup> (denoted _t_<sup>5</sup> in Figure 2), then some arc _a<sub>i</sub>_ must carry a total flow of 1+(1-1_/q_). Hence, in any confluent unsplittable transshipment, the capacity violation on that arc is at least 1-1_/q_, which tends to _d_<sub>max</sub>=1 as \(q\rightarrow\infty\).

## 4 Minimum number of rounds and maximum routable demand

In this section, let the digraph _D_=(_V,A_) have arc capacities \(c_a\ge 0\), \(a\in A\). We impose the _balance condition_ that \(d_\mathrm{max}:=\mathrm{max}_{t\in S^-}|b(t)|\le\mathrm{min}_{a\in A}c_a=:c_\mathrm{min}\) and assume that a feasible fractional transshipment exists for the given unsplittable transshipment instance. Let \(d_\mathrm{tot}:=\sum_{t\in S^-}|b(t)|\) denote the total demand of all sinks, and let \(b_\mathrm{avg}^+:=\sum_{s\in S^+}^{b(s)}/_{|S^+|}=^{d_\mathrm{tot}}/_{|S^+|}\) denote the average supply of a source. Note that we make no assumptions about the supply values; in particular, sources and sinks need not be symmetric with respect to supply and demand values.

In the context of unsplittable transshipments, the _minimum number of rounds_ problem asks for a partition of the set of sinks into a minimum number of subsets (rounds), together with a feasible unsplittable transshipment for each subset, such that for every source the total flow sent to sinks over all rounds equals its prescribed supply. Moreover, the _maximum routable demand_ problem seeks a feasible unsplittable transshipment that satisfies the demands of a subset of sinks, maximizes the total demand of this subset, and does not exceed the available supplies at the sources.

### 4.1 Minimizing the number of rounds

#### SSUF versus unsplittable transshipments.

Under the balance condition, it is shown in \[DGG99\] that all demands in an SSUF instance can be routed in polynomial time using at most five rounds, by partitioning demands into _small_ and _large_, and routing each class separately on suitably capacity- scaled copies of the network.

For unsplittable transshipments, however, routing in rounds poses additional challenges because rounds are _not independent_: the supply of a source consumed in earlier rounds reduces the supply available in later rounds. This cross-round ‘memory’ has no analogue in the SSUF setting. Moreover, unlike in SSUF, where all indivisible demands are known in advance, the Modified DGG Algorithm may generate arbitrarily small sub-demands during its execution, so that no meaningful global partition of demands into ‘small’ and ‘large’ classes exists. Furthermore, scaling down capacities does not guarantee that at most one demand uses a given arc. As a consequence, feasibility arguments based on capacity scaling, such as those used in \[DGG99\], no longer apply. Routing in rounds for unsplittable transshipments therefore requires more refined techniques.

For the case in which demand values are sufficiently smaller than _c_<sub>min</sub>, we prove bounds on the number of rounds for several such regimes in Appendix E. In the following, we present a unified strategy that routes all instances with _d_<sub>max</sub>_\<c_<sub>min</sub> in a number of rounds that depends only on the gap between _d_<sub>max</sub> and _c_<sub>min</sub>.

#### Routing demands in rounds when _d_<sub>max</sub>_\<c_<sub>min</sub>.

We may assume without loss of generality that \(d_\mathrm{max}\le(1-1/n)c_\mathrm{min}\) for some \(n\in\mathbb{N}\). Following the construction of \[DGG99, Fig. 6\], we construct an auxiliary digraph \(D'=(V',A')\) consisting of _n_+1 identical copies of _D_, where each copy \(a'\) of an arc \(a\in A\) has capacity \(c'_{a^\prime}:=c_a/_{(n+1)}\). For each sink \(t\in S^-\), we add a super-sink _T_ and connect every copy of _t_ to _T_ with an arc of capacity _d<sub>t</sub>/_<sub>(_n_+1)</sub>. Symmetrically, for each source \(s\in S^+\) we introduce a head-source _S_ and connect every copy of _s_ to _S_ with an arc of capacity _b(s_)/<sub>(_n_+1)</sub>, and finally connect every head-source _S_ to a global super-source _S_<sup>∗</sup> by an arc of capacity _b(s_).

