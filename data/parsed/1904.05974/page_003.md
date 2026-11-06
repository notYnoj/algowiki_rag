Interestingly, all known algorithms \[5,26,29\] for computing unpopular matchings with bounded unpopularity factor bound _u(M_), where _M_ is the output matching, by a value 2 or more<sup>3</sup> (see Section 1.2). Thus, matchings _M_ with \(u(M)\le 2\) can be regarded as being close to popular.

Observe that no matching wins more than 1/2-fraction of the votes cast in its head-to-head election against a popular matching. Similarly, no matching wins more than 2/3-fraction of the votes cast in its head-to-head election against a matching with unpopularity factor at most 2.

**Definition 1** _A matching M in_ \(G=(A\cup B,E)\) _is_ quasi-popular _if_ \(u(M)\le 2\).

Summarizing, for the sake of efficiency in computation, when comparing two matchings, we are ready to relax _never losing_ (the definition of popular matchings) to _losing within a factor bounded by 2_ (the definition of quasi-popularity). Note that if we scale the votes in favor of _M_ by 2, then a quasi-popular matching _M_ never loses an election. We show that relaxing popularity to quasi-popularity allows us to design efficient algorithms for finding good matchings in _G_.

## 1.1 Our Results and Techniques

Given the discussion above, our objective would be to show an efficient algorithm for the min-cost quasi- popular matching problem. However, as we show here, this problem is as hard as the starting problem - i.e., computing a min-cost popular matching.

**Theorem 1.** _Given a marriage instance_ \(G=(A\cup B,E)\) _with a function_ \(\mathsf{cost}:E\rightarrow\{0,1\}\)_, it is NP-hard to compute a min-cost quasi-popular matching in G. Moreover, it is NP-hard to approximate its cost within any multiplicative factor._

Thus finding or approximating a min-cost popular or quasi-popular matching is hard. Our next attempt is to overcome this hardness by considering the following intriguing question: can we find a quasi-popular matching of cost at most that of a min-cost popular matching? Surprisingly (in the midst of all these hard problems), this problem is tractable and this is our main result.

**Theorem 2.** _Given a marriage instance_ \(G=(A\cup B,E)\) _with a function_ \(\mathsf{cost}:E\rightarrow\mathbb{R}\)_, there is a polynomial time algorithm to compute a quasi-popular matching M such that_ \(\mathsf{cost}(M)\le\mathsf{opt}\)_, where_ opt _is the cost of a min-cost popular matching in G._

We give two proofs of Theorem 2, based on two different algorithms. The first approach is as follows. Let M<sub>1</sub> (respectively, M<sub>2</sub>) be the set of popular (resp., quasi-popular) matchings in _G_. We will show a set M<sup>∗</sup> such that \((1)\mathcal{M}_1\subseteq\mathcal{M}^*\subseteq\mathcal{M}_2\) and (2) conv(M<sup>∗</sup>) admits a formulation of size _O(m+n_) in R<sup>_m+n_</sup>, where conv(M<sup>∗</sup>) is the convex hull of edge incidence vectors of matchings in M<sup>∗</sup>. Linear programming over this formulation yields Theorem 2.

This result is proved in Section 3, where we show that conv(M<sup>∗</sup>) is a linear projection of one of the faces F<sub>_G_<sup>∗</sup></sub> of a new extension<sup>4</sup> of the _dominant matching_ polytope of a supergraph _G_<sup>∗</sup> of _G_.

**Definition 2** _A popular matching M in G is_ dominant _if M is more popular than every strictly larger matching, i.e.,_ \(\phi(M,M')>\phi(M',M)\) _for every strictly larger matching_ \(M'\).

<sup>3</sup> The symmetric difference \(M\oplus N\) of 2 matchings _M_ and _N_ may have _short_ alternating paths wrt _M_ which force \(u(M)\ge 2\). Forbidding such paths for an unpopular matching _M_ is necessary to ensure _u(M)\<_2. <sup>4</sup> Using the terminology from polyhedral combinatorics, we say that a polytope _Q_ that linearly projects to a polytope _P_ is an _extension_ of _P_, and that a linear description of _Q_ is an _extended formulation_ for _P_.

