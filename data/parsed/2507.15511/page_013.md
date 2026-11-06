## Inline Key Invariants.

We use the following invariants in the main bound; proofs and extended details appear in Appendix E.

• **Lane Invariant.** For each \((\tilde{\sigma},\chi)\) the memo table stores the lex-minimal witness among all subsets mapping to that key; lanes \(\chi\in\{0,1\}\) are disjoint.<tbc>

• **Suppression-on-overwrite (lane-wise).** When a witness for \((\tilde{\sigma},\chi)\) is overwritten by a lexicographically smaller mask, the displaced state is never expanded.<tbc>

• **CNF Safety.** Any non-canonical (0,1) state has the same aliased key as its canonical (1,0) counterpart and all of its descendants are _shadowed_ by the canonical branch; forbidding expansion from (0,1) is therefore complete and sound.

These invariants, particularly CNF safety, allow us to prove a strict reduction in the number of states that must be explored. As we formally prove in Lemma 9 (Appendix E), the CNF expansion policy ensures that for any base set of choices outside the alias pair, at most three of the four possible inclusion patterns are ever expanded. This deterministically prunes the search space, guaranteeing that the number of expanded states in a half of size _k_ is at most \(\frac{3}{4}\cdot 2^k\).

## Compensatory Merge.

During the final merge phase we evaluate all valid interpretations of aliased sums. Let \(\tilde{s}_L\in\tilde{\Sigma}(\ell_0)\) and \(\tilde{s}_R\in\tilde{\Sigma}(\ell_1)\) be aliased sums, with alias pairs (_x_<sub>0</sub>_,x_<sub>1</sub>) in \(\ell_0\) and (_y_<sub>0</sub>_,y_<sub>1</sub>) in \(\ell_1\). For tags \(\chi_L,\chi_R\in\{0,1\}\) define the corrected sums<tbc>

\(s_L(\chi_L)=\tilde{s}_L+\chi_L\left(x_1-x_0\right),s_R(\chi_R)=\tilde{s}_R+\chi_R\left(y_1-y_0\right).\)

<tbc>We check the four combinations

\(s_L(0)+s_R(0)=t,s_L(1)+s_R(0)=t,s_L(0)+s_R(1)=t,s_L(1)+s_R(1)=t.\)

This ensures correctness of the decision logic under value collision.

## Correctness Guarantee.

The Controlled Aliasing mechanism is guaranteed to find a solution if one exists, without producing false positives. We formalize this below.

_Theorem_ 5 (Correctness of Controlled Aliasing). _The Controlled Aliasing solver, using the 2-lane_ \((\tilde{\sigma},\chi)\) _memoization structure and the compensatory merge logic above, correctly solves the decision variant of_ Subset-Sum_. Furthermore, if a solution exists, the witness reconstruction procedure returns a valid subset_ \(W\subseteq S\).

_Proof._ The proof proceeds via the lane invariant, lane-wise suppression-on-overwrite, and CNF safety (inline invariants above), plus the soundness/completeness of the \(2\times 2\) corrected merge (Appendix E). Together these imply the theorem.

## Worst-Case Complexity.

We now state the worst-case running-time guarantee obtained from Controlled Aliasing.

_Theorem_ 6 (Worst-Case Complexity of Controlled Aliasing under CNF). _Consider the interleaved double-meet-in-the-middle solver that applies a single alias pair_ (_x_<sub>0</sub>_,x_<sub>1</sub>) _with_ \(x_0\neq x_1\) _in each half_ \(\ell_0,\ell_1\)_, uses the 2-lane_ \((\tilde{\sigma},\chi)\) _memoization structure, performs compensatory merging as in §5.2,_<tbc>

