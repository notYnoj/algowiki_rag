We call the marginal vector **x** _integral_ when every _x<sub>e,a</sub>_ is either zero or one, and _fractional_ otherwise. Every syndrome-consistent word **y** gives an integral feasible point _x<sub>e,a</sub>_=**1**{_a=y<sub>e</sub>_}, with objective value |**y**|. Conversely, normalization and local consistency ensure that every integral feasible marginal vector represents a syndrome-consistent word. An integral optimum therefore gives a minimum-weight word with the specified syndrome, and hence an ML correction on the _q_SC \[Fla+09\].

If the LP has several optimal solutions, select one using a fixed deterministic tie-breaking rule. If the selected symbol marginals are integral, output the corresponding word; otherwise declare failure. Let \(P_\mathrm{W}^\mathrm{LP}(G,p)\) be the probability of either a declared failure or an incorrect output when each position is corrupted independently with probability _p_; the nonzero values may have any distribution. The recovery condition below guarantees that the true error has the unique optimal marginal vector, so recovery under this condition is independent of the tie-breaking rule.

An equivalent formulation uses a directed trellis whose state records the running sum in each check. Unit flows through this trellis represent probability distributions on satisfying local assignments. Equating their symbol marginals gives an LP with _O(mq_<sup>2</sup>) variables and constraints, solvable in polynomial time; see Appendix B for more details. The LP decoder has a failure probability which we characterize in the following theorem:

## 3.3.2 A positive error-rate guarantee

**Theorem 6** (Finite-graph LP reliability)**.** _Let G be a simple graph with m edges, maximum degree at most_ \(D\ge 3\)_, and girth g<sub>G</sub>. Consider its homological cycle code over_ F_<sub>q</sub> with each position corrupted independently with probability_ 0_\<p\<_1/2 _and arbitrary nonzero error values. For every integer_ \(1\le h<g_G\)_, the probability that the LP decoder declares failure or returns an incorrect word satisfies_

\(P_\mathrm{W}^\mathrm{LP}(G,p)\le 2m(D-1)^{h-1}\left[2\sqrt{p(1-p)}\right]^h.\) (83)

_The same bound holds when exactly_ \(t\le pm\) _positions are chosen uniformly without replacement and assigned arbitrary nonzero error values._

The proof in Appendix B shows that the true error is the unique LP optimum whenever every simple path of _h_ edges contains fewer than _h/_2 corrupted positions. Counting paths and applying a binomial or hypergeometric tail bound gives (83). Related path-based conditions for binary LP decoding appear in \[EH12\]. Requiring fewer than _h/_2-1 corrupted positions on each path also guarantees recovery after every one-coordinate change. The failure probability for this stronger condition is at most

\(2m(D-1)^{h-1}\frac{1-p}{p}\left[2\sqrt{p(1-p)}\right]^h.\) (84)

The extra factor is independent of block length.

On the Linial-Simkin ensemble, the girth grows logarithmically with _n_. Choosing _h_ just below the girth in (83) gives the following positive error-rate guarantee.

**Corollary 2** (Linear-error LP recovery on the Linial-Simkin ensemble)**.** _Fix_ \(D\ge 3\)_, a finite field_ F_<sub>q</sub>, and_ \(c\in(0,1)\)_. Define the certified rate_

\(p_\mathrm{LP}^\mathrm{cert}(D,c):=\frac{1}{2}\left(1-\sqrt{1-(D-1)^{-2(1+1/c)}}\right)>0.\) (85)

