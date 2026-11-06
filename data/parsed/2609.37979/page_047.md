## NO case.

If \((I,J)\in\text{Iso-}\Pi_\text{NO}\), then \(I\in\Pi\) and \(J\notin\Pi\). By correctness of _R_, we have \(R(I)\in\Pi'\) and \(R(J)\notin\Pi'\). Hence \(f(I,J)\in\text{Iso-}\Pi'_\text{NO}\).

Thus _f_ is a valid many-one reduction Iso-\(\Pi\le_m\text{Iso-}\Pi'\). By transitivity,

\(\mathsf{GI}\le_m\text{Iso-}\Pi\le_m\text{Iso-}\Pi',\)

so Iso-\(\Pi'\) is GI-hard.

Thus, by using isomorphism-preserving reductions, we can obtain GI-completeness for many different Iso-\(\Pi\) problems. To this end, we use the reductions shown in Figure 3. We use this property to show that the promise problems based on the problems in H are GI-complete.

**Theorem 9.14.** _For every_ \(\Pi\in\mathcal{H}\)_, the promise problem_ Iso-\(\Pi\) _is_ GI_-complete._

_Proof._ Fix \(\Pi\in\mathcal{H}\). By Lemma 9.11, Iso-\(\Pi\in\mathsf{GI}\). Next, we use the fact that isomorphism-preserving reductions are transitive together with Lemma 9.15, Lemma 9.16, Lemma 9.17, Lemma 9.22, Lemma 9.23, Lemma B.26, Lemma B.27, Lemma B.28, Lemma B.29, Lemma B.30, Lemma B.31 and Lemma B.32 . Thus, we obtain \(\mathsf{GI}\le_p^\cong\Pi\) for each \(\Pi\in\mathcal{H}\) (see Figure 3). By Lemma 9.10, Iso-GI is GI-hard. Hence, the theorem follows from Lemma 9.13.

The proof of Theorem 9.14 relies on having all necessary isomorphism-preserving reductions. We moved to proofs of most of our reductions to Section B since these reductions are standard reductions form the literature. However, we exemplify how our isomorphism-preserving reductions work by present three different ones in this section.

**Lemma 9.15.** \(\mathsf{GI}\le_p^\cong\mathsf{IS}\).

Gap-k-Center 1,2
Gap-TSP 1,c
Lemma B.32
Feedback Vertex Set
Lemma B.31
(Un)directed-Hamilton
Lemma B.26
Lemma B.29
MaxCut
Lemma 9.17
IS
Lemma B.27
VC
Lemma B.26
Set Cover
Lemma B.30
k-Median
Metric TSP
Lemma B.26
Lemma B.28
Max 2-SAT
Lemma 9.15
Clique Cover
Feedback Arc Set
Lemma B.26
Lemma 9.16
SET
Lemma B.26
Coloring
Lemma 9.22
3-Coloring
Lemma 9.23
3-SAT
Lemma B.26
Lemma B.26
Lemma B.26
Steiner Tree
0/1-Integer Linear Programming
Clique
Exact Cover
Lemma B.26
3D-Matching
Lemma B.26
Lemma B.26
Set Packing
Hitting Set

Figure 3: A tree that shows the different isomorphism-preserving reductions. An edge from _A_ to _B_ means \(A\le_p^\cong B\).

