## 4.6 Many unaffected subproblems

What remains to be shown is that there are sufficiently many unaffected subproblems, such that the progress made there, by the previous section, justifies the cost of all performed comparisons. The setup is that we consider some current state of InversionSort as defined by one round of inversion search in all subproblems. We will show that for each unaffected subproblem there are at most _O_((log_N_)<sup>2</sup>) affected ones (creating the same cost, but not necessarily making progress).

A middle child with its three children currently being leafs is easy to analyse because the inversion that defines the boundaries between the children is described by Lemma 9. We will use the following lemma on partial refinement trees that describe any backbone InversionSort might work with at some time.

**Lemma 16.** _Let T be a (subtree of a) ternary tree of height h and let L_=(_v_<sub>1</sub>_,...,v<sub>k</sub>_) _be part of the left-to-right leaf-traversal of T of length_ \(k\ge 4(h+2)\)_. Then L must contain a middle child whose 3 children are leaves._

Observe that finished pairs of neighboring pivots on the backbone, i.e., subproblems where InversionSort verified that there are no further inversions, don’t spill out to their neighbors, and remember that over one pivot, spilling can only be in one direction.

**Lemma 17.** _Let L be a list of consecutive subproblems on the backbone, and assume there is no spill-in from the left to the first or from the right to the last (because of finished subproblems or the instance ending). Then at least one of the subproblems must be unaffected._

**Lemma 18.** _\[Not too many affected subproblems\] Let a be the number of active subproblems on the backbone at some stage of InversionSort and let u be the number of the unaffected subproblems. There exists a constant c such that_ \(Pr[a\le cu(logN)^2]\ge 1-1/N^3\).

## 4.7 Putting everything together: Proof of Theorem 1

With these ingredients, we are ready for a proof of

**Theorem 1** (Polylog Competitiveness of InversionSort)**.** _There exists an algorithm InversionSort for bichromatic sorting and a constant c\>_0_, such that for every instance_ I_, the cost of InversionSort on_ I_, with probability at least_ 1-1_/N, is at most c_(log_N_)<sup>3</sup>_H_<sub>I</sub>_, where H_<sub>I</sub> _is the cost of the Hamiltonian._

_Proof._ The cost of InversionSort consists of pivoting and inversion finding. Theorem 12 shows that pivoting uses _O(n_log_n_) bichromatic comparisons. Observe \(H_\mathcal{I}\ge n-1\), hence pivoting costs _O(H_<sub>I</sub>log_N_). Let _v_ be the cost of inversion finding, and _u_ be the cost of such comparisons in unaffected subproblems. Lemma 18 shows \(v\le u(logN)^2\) with probability 1-1_/N_ (union bound over the at most _N_<sup>2</sup> many rounds) and by Theorem 15 follows _u=O(H_<sub>I</sub>log_N_), showing the statement of the theorem.

