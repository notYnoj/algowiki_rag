In this paper, our focus is on classes of bounded twin-width [11] and of bounded merge- width [17]. These graph parameters were introduced in 2020 and 2025, respectively. Classes of bounded twin-width include classes of bounded clique-width, classes excluding a fixed minor, unit interval graphs, and _d_-dimensional grids [11]. Classes of bounded merge-width are even more general and further include classes of bounded expansion [17]. The main algorithmic application of classes of bounded twin-width and of bounded merge-width, when bounded-width witnesses are given, is that first-order model checking is fixed-parameter tractable [11, 17].

As we detail in the next paragraph, some improved approximation algorithms exist on classes of bounded twin-width. In general, however, there is no precise understanding of the provably best algorithms achievable when twin-width or merge-width is bounded. This is reflected in large approximability gaps and the lack of tight lower bounds under the Exponential-Time Hypothesis (ETH). Our motivation is to fill those gaps.

In classes of effectively<sup>1</sup> bounded twin-width, \(n\varepsilon\)-approximation algorithms for MIS, Min Coloring, and other related problems were shown for every \(\varepsilon>0\) [4]. The proof in [4] reveals that the approximation factor for MIS is more specifically _n_<sup>_c/_loglog_n_</sup>, for some constant _c_. While it was known that Max Independent Set is NP-hard on graphs of bounded twin-width [11], even bounded by 4 [3] (also see [8] for the status of other graph problems on graphs of low twin-width), no conditional hardness of approximation was established on classes of bounded twin-width. Even a polynomial-time approximation scheme (PTAS) was not excluded. Indeed, the existence of a PTAS was raised several times [9, 10, 4, 14, 7]. It was nonetheless observed that any O(1)-approximation algorithm would imply the existence of a PTAS [10].

We rule this out under the ETH and show a much tighter hardness-of-approximation result that nearly matches the _n_<sup>_c/_loglog_n_</sup>-approximation algorithm.

\(\blacktriangleright\) **Theorem 1.** _Unless the ETH fails, there is a constant_ \(\gamma>0\) _such that Max Independent Set does not admit a polynomial-time_ \(n^{\gamma/(loglogn)^2}\)_-approximation algorithm on n-vertex graphs of twin-width at most 4, even when a 4-sequence is given as part of the input._

The reduction uses, in order, three ingredients: (1) a classical reduction from 3-SAT to MIS, (2) a long even subdivision of the resulting instances, and (3) a lexicographic power of the resulting graphs.

"Long" subdivisions have twin-width at most 4 [3], which explains the role of (2). _Even_ subdivisions preserve the NP-hardness of MIS [25]. However, "long" subdivisions do not preserve any hardness of approximation. There is a straightforward PTAS on these graphs: select every other vertex along each subdivided edge. So, there is a psychological barrier in using (2). Nevertheless, with the right exponent, (3) resurrects this seemingly defunct approximation gap, while keeping the reduction within the desired running-time budget.

Similar ingredients can be adapted to give the same result for Min Coloring.

\(\blacktriangleright\) **Theorem 2 (** \(\includegraphics{}\)**).** _Unless the ETH fails, there is a constant_ \(\gamma>0\) _such that Min Coloring does not admit a polynomial-time_ \(n^{\gamma/(loglogn)^2}\)_-approximation algorithm on n-vertex graphs of twin-width at most 4, even when a 4-sequence is given as part of the input._

Theorem 2 implies Theorem 1. Indeed, a polynomial-time _r_-approximation algorithm for MIS implies a polynomial-time O(_r_log_n_)-approximation algorithm for Min Coloring. Repeatedly removing an _r_-approximate maximum independent set and assigning it a new

<sup>1</sup> See this and all relevant definitions in Section 2.

