In this paper we consider the algorithmic problem of comparison-sorting a \(\pi\)-avoiding _S_.

## Decision Tree Complexity.

Fredman \[Fre76\] observed that if _S_ is known to be selected from a permutation set \(\Gamma\), that _S_ can be sorted with \(O(n+log|\Gamma|)\) comparisons. The _Stanley-Wilf conjecture_ (see Bóna \[Bón22\]) states that if \(\Gamma_\pi\) is the set of all \(\pi\)-avoiding permutations, that \(|\Gamma_\pi|\le(c(\pi))^n\), for some constant \(c(\pi)\). This conjecture was reduced to the _Füredi-Hajnal conjecture_ \[FH92\] by Klazar \[Kla00\] and both conjectures were proved by Marcus and Tardos \[MT04\]. Together with Fredman \[Fre76\], this implies that the decision-tree complexity of sorting _S_ is \(O(nlogc(\pi))=O_k(n)\). Subsequent work has attempted to pin down the leading constant \[Kla00, MT04, Cib09, Fox13, CK17\]. Fox \[Fox13\] proved that<sup>1</sup>

\(nlogc(\pi)=\left\{\begin{array}{ c c }
O(kn) & \text{For all}k\text{-permutations}\pi, \\
\Omega(k^{1/2}n) & \text{For some}k\text{-permutation}\pi, \\
\Omega((k/logk)^{1/2}n) & \text{For almost all}k\text{-permutations}\pi.
\end{array}\right.\)

## Algorithmic Complexity.

There are two natural ways to approach the _algorithmic_ complexity of sorting a \(\pi\)-free _S_. The first is to use knowledge of \(\pi\) to structure the sorting process. This approach is sufficient to sort optimally in _O(n_) time when _k_=3 \[Knu73, Art07\], and has had limited success for some patterns with _k_=4. Arthur \[Art07\] gave _O(n_)-time sorting algorithms when \(\pi\in\{(1,2,3,4),(1,2,4,3),(2,1,4,3)\}\), and _O(n_logloglog_n_)-time sorting algorithms when \(\pi\in\{(1,3,2,4),(1,3,4,2),(1,4,2,3),(1,4,3,2)\}\). The _oblivious_ approach to sorting _S_ is to simply use a general-purpose sorting algorithm, but analyze its behavior when _S_ happens to be \(\pi\)-free. This is the approach taken by Chalermsook, Goswami, Kozma, Mehlhorn, and Saranurak \[CGK<sup>+</sup>15b\], Kozma and Saranurak \[KS20\], and by our paper. Consider these two general-purpose sorting algorithms:

**BST Sort.** Fix some dynamic binary search tree (BST) algorithm T . Beginning from an empty BST, insert the elements _S_(1)_,...,S(n_) in that order, reorganizing the tree between inserts as T dictates. The number of comparisons is the sum of depths of \((S(i))_{1\le i\le n}\) at the time of their insertion; the _time_ is linear in the number of comparisons and that needed to reorganize the tree via rotations.

**Heap Sort.** Fix some heap data structure H. Insert the elements _S_(1)_,...,S(n_) into the heap in that order, then perform _n_ Delete-Min operations, thereby sorting the sequence.

Chalermsook et al. \[CGK<sup>+</sup>15b\] analyzed the performance of BST Sort when T is GreedyFuture \[DHI<sup>+</sup>09\], an online BST that is _O_(1)-competitive with the natural offline Greedy algorithm \[Luc88, Mun00\]. Define _A<sub>S</sub>_ to be the \(n\times n0\)-1 permutation matrix where _A<sub>S</sub>(i,S(i_))=1. If _S_ avoids a _k_-permutation \(\pi\), then _A<sub>S</sub>_ is \(P_\pi\)-free, where \(P_\pi(i,\pi(i))=1\). Define _A_<sub>Greedy(_S_)</sub>(_i,j_)=1 iff the element with rank _j_ is touched by the insertion of _S(i_). Chalermsook et al. \[CGK<sup>+</sup>15b\] proved that any occurrence of the "hat" pattern (<u>**?**</u>) in _A_<sub>Greedy(_S_)</sub> contains, within its bounding box, an input point of _A<sub>S</sub>_, and as a consequence, _A_<sub>Greedy(_S_)</sub> avoids \(Q=P_\pi\otimes(\underline{\bullet})\), where \(\otimes\) is the Kronecker product, i.e., each 1 of \(P_\pi\) is replaced by (<u>**?**</u>). (Following convention, 0-1 matrices are<tbc>

<sup>1</sup>The manuscript \[Fox13\] only gives an \(\Omega(k^{1/4}n)\) lower bound on the decision tree complexity of sorting a \(\pi\)-free _S_. The \(\Omega(k^{1/2}n)\) lower bound is unpublished.

