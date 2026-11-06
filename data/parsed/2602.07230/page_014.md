<tbc>maximum routable demand is lower bounded by \(max\left\{d/6,1-d/8\right\}\cdot d_\text{tot}\) for \(d\in[0,1]\), which attains its minimum at _d_=3/7 and is therefore always at least \(0.07143\cdot d_\text{tot}\).

## 5 Conclusion and open problems

We have introduced unsplittable transshipments as a natural extension of single source unsplittable flows. Our results and techniques indicate that unsplittable transshipment problems pose new and interesting algorithmic challenges and are inherently more difficult than their single source counterparts. We conclude by highlighting several open questions and problems that may stimulate future research.

The Modified DGG Algorithm can be adapted to guarantee lower bounds on arc flows in unsplittable transshipments; see Theorem 6. Whether arc-wise upper and lower bounds can be achieved simultaneously remains an intriguing open question, even in the special SSUF case. Extending a conjecture for SSUF by Morell and Skutella [MS22], we conjecture that such transshipments exist and can be computed efficiently.

**Conjecture.** _Given a b-transshipment x, one can efficiently compute an unsplittable b-transshipment y such that_

\(x_a-d_\text{max}\le y_a\le x_a+d_\text{max}\text{\textit{for all}}a\in A.\)

Motivated by a famous conjecture of Goemans, many authors have studied cost-based variants of SSUF; see, e.g., [KS01; Sku02; TVZ24; Swa+26]. Generalizing some of these results to unsplittable transshipments poses an interesting challenge.

In Section 4, we study the problem of minimizing the number of rounds while imposing the balance condition \(d_\text{max}\le c_\text{min}\). Our techniques exploit the additional restriction to _d_max_\<c_min, allowing one to sufficiently separate the demands from _c_min. It remains open whether explicit bounds can be obtained even if _d_max=_c_min, both for routing in rounds and for maximizing the routable demand. Other variants, such as constant-factor approximations for minimizing the number of rounds, may also provide further insight.

Another related model is the _k-splittable flow_ problem, introduced by Baier, Köhler, and Skutella [BKS05], in which given supplies and demands must be routed using at most _k_ paths per source- sink pair. They studied the maximum _k_-splittable _s-t_ flow problem, establishing tight approximation guarantees for small values of _k_ and polynomial-time algorithms for maximum uniform _k_-splittable _s-t_ flows. Subsequent work investigated congestion- and cost-based variants in the single source setting, including approximation results for _k_=2 by Kolliopoulos [Kol05] and for general _k_ by Salazar and Skutella [SS09].

The model extends naturally to _k-splittable b-transshipments_, where each source-sink pair may use at most _k_ paths. By pre-splitting sink demands and applying the Modified DGG Algorithm, one obtains congestion bounded by _d_max_/k_ for the _k_-splittable transshipment problem. Other optimization variants that arise in the context of _k_-splittable flows remain open for the _k_-splittable transshipment setting, suggesting several promising directions for future research.

## References

[AMO93] Ravindra K. Ahuja, Thomas L. Magnanti, and James B. Orlin. _Network Flows: Theory, Algorithms, and Applications_. Upper Saddle River, NJ, USA: Prentice-Hall, Inc., 1993. ISBN: 0-13-617549-X.

[BKS05] Georg Baier, Ekkehard Köhler, and Martin Skutella. "The k-splittable flow problem". In: _Algorithmica_ 42.3 (2005), pp. 231-248.

