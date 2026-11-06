# Quasi-popular Matchings, Optimality, and Extended tions

Yuri Faenza<sup>1</sup> and Telikepalli Kavitha<sup>2</sup><sup>⋆</sup>

<sup>1</sup> IEOR, Columbia University, New York, USA. `yf2414@columbia.edu`

<sup>2</sup> Tata Institute of Fundamental Research, Mumbai, India. `kavitha@tifr.res.in`

**Abstract.** Let \(G=(A\cup B,E)\) be an instance of the stable marriage problem where every vertex ranks its neighbors in a strict order of preference. A matching _M_ in _G_ is _popular_ if _M_ does not lose a head- to-head election against any matching. Popular matchings are a well-studied generalization of stable matchings, introduced with the goal of enlarging the set of admissible solutions, while maintaining a certain level of fairness. Every stable matching is a min-size popular matching. Unfortunately, when there are edge costs, it is NP-hard to find a popular matching of minimum cost - even worse, the min-cost popular matching problem is hard to approximate up to any factor.

Let `opt` be the cost of a min-cost popular matching. Our goal is to efficiently compute a matching of cost at most `opt` by paying the price of mildly relaxing popularity. Our main positive results are two bi-criteria algorithms that find in polynomial time a _near-popular_ or "quasi-popular" matching of cost at most `opt`. Moreover, one of the algorithms finds a quasi-popular matching of cost at most that of a min-cost popular fractional matching, which could be much smaller than `opt`.

Key to the other algorithm are new results for certain polytopes. In particular, we give a polynomial- size extended formulation for an integral polytope sandwiched between the popular and quasi-popular matching polytopes. We complement these results by showing that it is NP-hard to find a quasi- popular matching of minimum cost, and that both the popular and quasi-popular matching polytopes have near-exponential extension complexity.

This version of the paper goes beyond the conference version [12] in the following two points: (i) the algorithm for finding a quasi-popular matching of cost at most that of a min-cost popular fractional matching is new; (ii) the proofs from Section 6.1 and Section 7.3 are now self-contained (the conference version used constructions from [10] to show these lower bounds).

### 1 Introduction

Consider a bipartite graph \(G=(A\cup B,E)\) on _n_ vertices and _m_ edges where every vertex ranks its neighbors in a strict order of preference. Such an instance, commonly referred to as a _marriage_ instance, is a classical model in two-sided matching markets. A matching _M_ is stable if there is no _blocking pair_ with respect to _M_: a pair (_a,b_) blocks _M_ if both _a_ and _b_ prefer each other to their respective assignments in _M_. The notion of stability was introduced by Gale and Shapley [16] in 1962 who showed that stable matchings always exist in _G_ and one such matching can be efficiently computed.

A broad class of objectives can be captured by defining a function \(\text{\texttt{cost}}:E\rightarrow\mathbb{R}\) and asking for a stable matching whose sum of edge costs is minimized. Thus the min-cost stable matching problem includes several stable matching problems such as finding one with max-utility or with min-regret, or one with given forced and forbidden edges. More generally, a cost function allows a decision-maker to "access" the whole family of stable matchings (possibly of exponential size), while the Gale-Shapley algorithm will always return the same stable matching (i.e., the one that is optimal for one side of the bipartition). There are several polynomial time algorithms to compute a min-cost stable matching and special variants of this problem [14,15,28,39,44,45].

Stable matchings and their extensions are used in many optimization problems in computer science, economics, and operations research, such as matching students to schools/colleges [1,3] and medical interns<tbc>

<sup>⋆</sup> Supported by the DAE, Government of India, under project no. 12-R&D-TFR-5.01-0500. Part of this work was done while visiting MPI for Informatics, Saarland Informatics Campus, Germany.

