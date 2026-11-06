<tbc>The diagonal entries account for direct edges. For a pair (_s,t_) whose distance rounds to \(r_\ell\), we report the constraint as unsatisfied if the corresponding entry of \(AB^{(\ell)}\) is zero. If \(\mathcal{U}_\eta(G)\) denotes the set of unsatisfied \(\eta\)-monotonicity constraints, the resulting set \(\mathcal{N}_\tau(G)\) satisfies

\(\mathcal{U}_\tau(G)\subseteq\mathcal{N}_\tau(G)\subseteq\mathcal{U}_{\tau+\epsilon}(G).\)

Indeed, rounding down cannot cause an unsatisfied \(\tau\)-constraint to be removed, while any constraint satisfied with additive progress \(\tau+\epsilon\) remains satisfied after its source-target distance is rounded down by less than \(\epsilon\). The procedure uses \(O(\Delta/\epsilon)\) matrix multiplications and therefore runs in \(\widetilde{O}(n^\omega\Delta/\epsilon)\) time.

We may now apply BatchedVoteCover without further modification.

**Corollary 3.12.** _Let P be a set of n points with aspect ratio_ \(\Delta_P\)_, after normalizing its minimum nonzero pairwise distance to_ 1_. For every_ \(\tau\ge 0\) _and_ \(0<\epsilon\le 1\)_, there is a randomized algorithm running in_<tbc>

\(\widetilde{O}\left(n^\omega\frac{\Delta_P}{\epsilon}\right)\)

<tbc>_time that constructs a_ \(\tau\)_-monotonic graph G such that, with high probability, every_ \(s\in P\) _has out- degree at most_ \(O(\mathsf{OPT}_{\tau+\epsilon}(s)logn)\)_, where_ \(\mathsf{OPT}_{\tau+\epsilon}(s)\) _is the minimum out-degree required at s in any_ \((\tau+\epsilon)\)_-monotonic graph. Consequently,_

\(|E|\le O(logn)\cdot\mathsf{OPT}_{\tau+\epsilon}.\)

_Proof._ The analysis of BatchedVoteCover uses only constant-time access to MemberOf, FreqOf, and SetOf, together with a verification procedure whose output lies between the constraints unsatisfied at the desired parameter and those unsatisfied at the resource-augmented parameter. The set-access construction and the additive version of VerifyNav above provide these properties for parameters \(\tau\) and \(\tau+\epsilon\), respectively. The remainder of the proof of Theorem 3.1 applies unchanged.

The change from a logarithmic to linear dependency on \(\Delta_P\) in the running time when transitioning from \(\alpha\)-navigability to \(\tau\)-monotonicity is not surprising, as this reflects the increase in number of relevant distance scales from \(O(log_\alpha(\Delta_P))\) to \(O(\Delta_P/\tau)\). In contrast to \(\alpha\)-navigable graphs, which guarantee a logarithmic search convergence of \(O(log_\alpha(\Delta_P))\) steps, \(\tau\)-monotonic graphs likewise inherit a linear bound of \(O(\Delta_P/\tau)\) steps to converge.

## 4 Hardness

This section addresses two natural questions about the algorithms from the previous sections.

1. Can the running time of the resource augmented algorithm be improved? The main bottleneck is the subroutine that, at a fixed distance scale _d_<sub>0</sub>, lists all source-target pairs (_s,t_) whose \(\alpha\)-navigability constraints become satisfied after the newly added edges are inserted. In our current implementation, this subroutine is based on fast matrix multiplication and runs in \(O(n^\omega)\) time. Is there a substantially faster implementation?<tbc>

2. Can one eliminate the discretization step and obtain a more efficient exact single-criterion algorithm? More precisely, can one efficiently test, in the original metric, which \(\alpha\)-navigability constraints are satisfied by the current edge set? Any \(O(n^{2.5-\varepsilon})\)-time algorithm for this task, for a fixed constant \(\varepsilon>0\), would improve upon the current worst-case running time of the best known single-criterion algorithm.<tbc>

