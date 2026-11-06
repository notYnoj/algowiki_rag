expensive or disallowed, the stripe subinstance is the structure the algorithm is faced with. Note that elements of the subproblem that are not in the subinstance make inversion finding more difficult because such elements cannot form an inversion, but the algorithm cannot distinguish them from elements in the subinstance. We say that such elements in the bucket of one pivot _spill in_ to the subproblem. This spill-in is the shaded part in Figure 1.

**Definition 13** (unaffected subproblem)**.** _Let r,b be two neighboring pivots on the backbone in some round of inversion search of InversionSort. Then the subproblem r,b is_ unaffected _if the number of red elements in the stripe subinstance of r,b is at least 1/4 of the number of red elements in the subproblem of r,b and the number of blue elements in the stripe subinstance of r,b is at least 1/4 the number of blue elements in the subproblem of r,b._

Note that in the course of running InversionSort, by refining the backbone, subproblems can turn from affected to unaffected, but not vice versa.

Observe that neighboring subinstances share the stripe of the pivot; this stripe does not constitute spill-in. Still, over a single pivot, there typically is spill-in of the same color in both directions, but only one of them can affect the receiving subproblem: _R<sub>k</sub>_ consists of the red elements in the two neighboring subproblems, \(S_i\subset R_k\cup\{r_k\}\) is part of both, so one of the two sets of spilling-in elements must be less than half of _R<sub>k</sub>_, so clearly not both of them can be more than 3/4 of _R<sub>k</sub>_.

## 4.5 Constant local competitiveness of inversion finding

In this section, we will argue that inversion finding for unaffected subinstances is justified by the cost of the Hamiltonian in the subinstance. In Section 2.1, we already argued that non-successful inversion searches that lead to a certificate that there are no further inversions are justified by parts of the Hamiltonian. Here, we (also) consider successful searches, and relate their cost to the cost of the Hamiltonian between and including the stripes of the representatives InversionSort has as neighbors on the backbone.

The proofs of the following Lemmas and Theorems are given in Appendix C.

**Lemma 14.** _\[local competitiveness of inversion finding\] Let r,b be two neighboring pivots of InversionSort, and let t be the number of rounds (up to a constant the cost of comparisons) until InversionSort finds an inversion or concludes that there is none, starting from the first round when the subproblem of r,b is unaffected. Let H<sub>r,b</sub> be the cost of the Hamiltonian of the stripe subinstance between the stripe of r and the stripe of b. Then_ E\[_t_\]=_O(H<sub>r,b</sub>), and_ \(Pr[t\le\mathbb{E}[t]+t']\ge 1-(1/8)^{t^\prime}\).

## Overall cost of inversion finding in unaffected subproblems

Observe that each layer in the refinement tree almost partitions the original instance into subinstances: Only the buckets of the pivots on the backbone are counted twice. In other words, if we take all subinstances of the same polarity (every other) of one level of the refinement tree, they are disjoint, and the sum of the cost of the Hamiltonian in the subinstances is at most the cost of the Hamiltonian. By Theorem 5 we can hence bound the total cost of inversion search / finding in unaffected subproblems to be only a _O_(log_N_) factor higher than the cost of the Hamiltonian.

**Theorem 15.** _Let u be the total cost of comparisons that InversionSort performed in unaffected subproblems when running on instance_ I _of size N, and let H_<sub>I</sub> _be the cost of the Hamiltonian of_ I_. Then, with probability at least_ 1-1_/N, u=O(H_<sub>I</sub>log_N)._

