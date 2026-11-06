uncovered targets, so the algorithm adds the set with the most number of votes (after ∼log_n_ samples), then explicitly updates _U_ by removing every target now covered by that set.

This explicit update of _U_ is the bottleneck. Without efficient access to the points covered by a given edge, this is done in VoteCover through a full scan over _U_. Because the size of _U_ does not shrink quickly enough with each new edge, this takes \(\Omega(n\cdot\mathsf{OPT}_\alpha(s))\) total time in the worst case. Summed over all sources, this is too expensive for the desired \(n^\omega\)-time bound - recalling that \(\mathsf{OPT}_\alpha=\sum_{s=1}^n\mathsf{OPT}_\alpha(s)\), we would obtain a running time of \(\Omega(n\cdot\mathsf{OPT}_\alpha)\). It was shown in \[12\] that a preprocessing step could reduce this cost to amortized \(\widetilde{O}(n)\) per source by shrinking the initial size of _U_ when \(\alpha=1\), but the approach does not extend in general to \(\alpha>1\).

### Batched verification by matrix multiplication

To reduce the cost of updating _U_, our algorithm introduces a second main ingredient: the verification routine of Section 2.5.

Suppose first that the distances between input points take only _W_ distinct values. This can be enforced by rounding each continuous distance to the nearest discrete distance scale. For a fixed distance scale, the set of constraints satisfied by the current graph can be found by one Boolean matrix multiplication, as reviewed in Section 2.5. Repeating over all _W_ scales gives a verification procedure running in \(\widetilde{O}(n^\omega W)\) time. By rounding distances geometrically to powers of \((1+\varepsilon)\), we may take \(W=O(log(\Delta)/\varepsilon)\); this is the source of both the \((1+\varepsilon)\) resource augmentation slack and the \(log(\Delta)/\varepsilon\) factor in the running time.

Our algorithm uses this routine as a global replacement for the expensive scans inside VoteCover. Rather than updating the uncovered set after each selected edge, we let every source add a batch of edges, and then use a VerifyNav routine to refresh all their uncovered sets simultaneously. The rest of this section formalizes this batched voting procedure. In Section 3.1, we define PartialVoteCover, which covers a constant fraction of a given residual instance. In Section 3.2, we show how to obtain a fast overall runtime by running this partial cover routine for all sources in parallel and using VerifyNav to update the residual constraints between batches.

## 3.1 Partial Cover

Here we introduce PartialVoteCover (Algorithm 3.1), which differs from VoteCover in one fundamental way: given a set _U_ of uncovered elements, PartialVoteCover is only asked to cover at least |_U_|/2 elements of _U_ rather than all of them. The way this manifests itself is that PartialVoteCover constructs a cover over a sample _K_ of _U_ instead of over _U_ directly. Controlling the size of the sample allows us to bound both the amount of work we do and the number of sets in the partial cover. This approach bears similarity to sampling methods used in prior work on set cover algorithms in sublinear-time models of computation \[19\].

The voting process is largely as in VoteCover. Each uncovered sample casts votes for the sets containing it until some set receives _c_ln_n_ votes, where _c_ is a fixed constant. That set is then added to the cover, and the points that voted for it revert their votes for other sets. This repeats until all samples have voted, and the cover is returned.

### 3.1.1 Correctness and success probability

We now prove that PartialVoteCover covers at least half of _U_ with high probability. First, we note a few simple properties of the output of PartialVoteCover.

**Observation 3.2.** _PartialVoteCover returns a partial cover_ C _containing no more than_ \(\frac{C}{c}\cdot\mathsf{opt}\) _sets._

