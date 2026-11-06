# Stable Matching with Deviators and Conformists<sup>∗</sup>

**Abstract**

In the Stable Marriage and Stable Roommates problems, there are inherent trade- offs between the size and stability of solutions. While in the former problem, a stable matching always exists and can be found efficiently using the Gale-Shapley algorithm, the existence of a stable matching is not guaranteed in the latter problem, but can be determined efficiently using Irving’s algorithm. However, the computation of matchings that minimise the instability, either due to the presence of constraints on the size of the matching or due to restrictive preference cycles, gives rise to a collection of infamously intractable _almost-stable matching_ problems.

In practice, however, not every agent is able or likely to initiate deviations caused by blocking pairs. Suppose we knew, for example, due to a set of requirements or estimates based on historical data, which agents are likely to initiate deviations - the _deviators_ - and which are likely to comply with whatever matching they are presented with - the _conformists_. Can we decide efficiently whether a matching exists in which no deviator is blocking, i.e., in which no deviator has an incentive to initiate a deviation? Furthermore, can we find matchings in which only a few deviators are blocking?

We characterise the computational complexity of this question in bipartite and non- bipartite settings. Surprisingly, these problems prove intractable in very strong ways. On the positive side, we identify polynomial-time and fixed-parameter tractable cases (with respect to the number of deviators and the preference list length), providing novel algorithms for problems where stability cannot be fully guaranteed, and resolving some open cases from the literature along the way.

**Keywords** Stable Marriage, Stable Roommates, Almost-Stable Matching, Parametrised Com- plexity, Fairness, Efficient Algorithm

<sup>∗</sup>Sections 3 and 4 extend and strengthen the results in a preliminary version of this paper in the Proceedings of AAMAS 2026 [24]. The proof of Theorem 3.1 builds on a construction in Augustine Kwanashie’s PhD thesis [37, Thm. 5.3.1]. <sup>†</sup>Work done whilst at the University of Glasgow.

Frederik Glitzner<sup>1</sup>, Augustine Kwanashie<sup>†</sup><sup>2</sup>, and David Manlove<sup>1</sup>

<sup>1</sup>School of Computing Science, University of Glasgow, Glasgow G12 8QQ, UK

<sup>2</sup>Lloyds Banking Group, Westminster House, 11 Portland Street, Manchester M1 3HU, UK

