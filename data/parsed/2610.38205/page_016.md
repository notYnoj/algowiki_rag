<tbc>with this approach is that PartialVoteCover only succeeds in covering enough constraints when given a parameter `opt` close enough to its true optimum cover size \(\mathsf{OPT}_{\alpha(1+\varepsilon)}\). To accomplish this, we run the entire procedure over doubling guesses of \(\mathsf{OPT}_{\alpha(1+\varepsilon)}\), ensuring that we find a serviceable value `opt` within \(\mathrm{log}(\mathsf{OPT}_{\alpha(1+\varepsilon)})\) attempts.

Only one detail remains. Recall from Lemma 3.6 that the running time of PartialVoteCover is proportional to the sum of all frequencies of the elements it samples. It is not hard to see that, across all set cover instances, the frequency of an element is large (roughly _n/_2) on average. Thus, we attach an additional preprocessing step alongside each guess `opt` which serves to bound the frequency of each element. Namely, we add `opt`ln_n_ random edges to each point. This covers a large number of constraints - in particular, it covers all constraints with high frequency. After having added these random edge, we use VerifyNav to identify the targets that remain uncovered, all of which have low frequencies.

This full algorithm, BatchedVoteCover, is laid out in Algorithm 3.2. It remains to be shown that BatchedVoteCover returns a near-optimally-sparse \(\alpha\)-navigable graph, and that it does so in \(\widetilde{O}(n^\omega\mathrm{log}(\Delta)/\varepsilon)\) time.

## 3.2.1 Approximation factor

Given that PartialVoteCover covers a constant fraction of the unsatisfied constraints for a given set cover instance, it is easy to see that BatchedVoteCover must successfully solve that set cover instance on or before the first iteration where `opt` exceeds the true optimal cover size for that instance.

**Observation 3.7.** _Given sufficiently-large constants C and c, as well as constant_ `opt` _satisfying_ \(\mathsf{OPT}_{\alpha(1+\varepsilon)}<\mathsf{opt}\le 2\mathsf{OPT}_{\alpha(1+\varepsilon)}\)_, BatchedVoteCover (Algorithm 3.2) covers U in no more than_ \(\mathrm{log}n+\gamma\) _calls to PartialVoteCover with probability_ \(\ge 1-O(1/n^{\gamma-1})\)_, for any constant_ \(\gamma\).

_Proof._ If a call to PartialVoteCover covers at least half of _U_, we’ll say this call was "successful". By Lemma 3.5, each call to PartialVoteCover is successful with probability at least 1-1_/n_ given adequate constants _C_ and _c_. All points in _U_ are covered after no more than \(\lceil\mathrm{log}_2n\rceil+1\) successful calls. Thus, if we call PartialVoteCover \(\lceil\mathrm{log}_2n\rceil+\gamma\) times, we can only fail to cover _U_ if the unsuccessful calls number at least \(\gamma\).

By a union bound over the possible sets of \(\gamma\) unsuccessful calls, the failure probability of BatchedVoteCover is at most<tbc>

\(\genfrac(){pt}{2}{\lceil\mathrm{log}_2n\rceil+\gamma}{\gamma}\left(\frac{1}{n}\right)^\gamma\le\left(\frac{e(\lceil\mathrm{log}_2n\rceil+\gamma)}{\gamma n}\right)^\gamma.\)

<tbc>In particular, for any constant \(\gamma\), this failure probability is

\(O\left(\frac{1}{n^{\gamma-1}}\right).\)

A bound on the size of the adjacency list constructed for a given point follows directly from Observation 3.2.

**Lemma 3.8.** _For a given point whose set cover instance has optimal cover size_ \(\mathsf{OPT}_{\alpha(1+\varepsilon)}\)_, Batched- VoteCover constructs an adjacency list of size_ \(O(\mathsf{OPT}_{\alpha(1+\varepsilon)}\mathrm{log}n)\) _with probability_ \(\ge 1-O(1/n^{\gamma-1})\).<tbc>

