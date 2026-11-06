In the case of binary trees, the first condition of (b) implies the second one, which can therefore be dropped from the equivalence statement. Moreover, for binary trees the first condition of (b) can be expressed as: At most one leaf has a non-leaf sibling.

By Proposition 51, in a binary tree the condition that at most one leaf has no sibling is equivalent to the product condition, which implies the partition property of \(\Pi_T\), so the lower bound of Lemma 49 applies. This establishes Theorem 8 in the case of binary trees.

As a side note, Fig. 11 shows the simplest example of a full binary tree _T_ and a ranking \(\rho\) for which there exists an adjacent-rank transposition \(\tau\) to which \(\Pi_T\) is insensitive at \(\rho\) while the affected leaves are not siblings. The tree has two leaves without siblings, namely 1 and 2. The adjacent-rank transposition (3,4) acts on nodes that are not siblings, but leaves the minimum number of inversions at 4.

## 8.3 General trees

For general trees _T_ the sensitivity analysis of \(\Pi_T\) becomes more complicated than for binary trees, and we do not know of a simple sensitivity criterion like Proposition 31, but we can nevertheless extend the result for binary trees to arbitrary trees with similar constraints. For a given ranking \(\rho\) of L(_T_) and a given adjacent-rank transposition \(\tau\), we would like to figure out the effect of \(\tau\) on the objective \(\mathrm{MinInv}(T,\cdot)\), in particular when \(\mathrm{MinInv}(T,\tau\rho)=\mathrm{MinInv}(T,\rho)\). Recall the decomposition (5) of \(\mathrm{MinInv}(T,\cdot)\) from Section 4.2. By Proposition 27 the only term on the right-hand side of (5) that can be affected by the transposition \(\tau\) is

\(\mathrm{MinRInv}(T_v,\rho)\doteq\mathrm{min}_\sigma\mathrm{RInv}(T,\rho,\sigma)\)

corresponding to the node _v_ that is the least common ancestor \(\mathrm{LCA}(\ell_\mathrm{lo},\ell_\mathrm{hi})\) of the two leaves \(\ell_\mathrm{lo}\) and \(\ell_\mathrm{hi}\) that are affected by \(\tau\) under \(\rho\). In Section 5 we considered the two possible relative orderings \(\sigma_1\) and \(\sigma_2\) of the children of _v_, and derived a criterion for when the lowest cost does not change under \(\tau\). More precisely, when

\(\mathrm{min}(\mathrm{RInv}(T,\rho,\sigma_1),\mathrm{RInv}(T,\rho,\sigma_2))=\mathrm{min}(\mathrm{RInv}(T,\tau\rho,\sigma_1),\mathrm{RInv}(T,\tau\rho,\sigma_2)).\) (21)

There are two complications in generalizing this approach from binary to general trees.

\(\circ\) The expression (4) for \(\mathrm{RInv}(T,\rho,\sigma)\) involves multiple terms instead of just one as in (6). This complicates probabilistic analyses like the one we did in Section 5 because the difference in cost of the two relative orderings of two children is also affected by parts of the tree outside of their combined subtrees. The issue did not matter for the analysis in Section 4. We will be able to manage it here, as well.

\(\circ\) There now are not just two but multiple possible orderings \(\sigma\), and it is not clear what pairs \((\sigma_1,\sigma_2)\) we need to impose (21) on in order to guarantee that \(\mathrm{MinRInv}(T_v,\rho)=\mathrm{MinRInv}(T_v,\tau\rho)\) but no more.

