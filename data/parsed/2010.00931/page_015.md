**Algorithm 2.** Finding the optimal _k_-cut STT on _A_

Input: k-admissible set of nodes \(A\subseteq V(S)\), search frequencies \(p:A\rightarrow\mathbb{N}\).<br>
Output: (r,c), for optimal k-cut STT on A with root r and cost c.<br>
procedure OPT-STT(A)<br>
   if A={r} then \(\triangleright\) single node<br>
   return (r,p(r))<br>
   for k-admissible root \(r\in A\) do<br>
   \(A_1,\dots,A_t\leftarrow\) node sets of the connected components of S[A]\\r.<br>
   for i=1,...,t do<br>
   \((r_i,c_i)\leftarrow\text{OPT-STT}(A_i)\triangleright\) optimal subtrees T<sub>1</sub>,...,T<sub>t</sub><br>
   Let \(C_r=\sum_{x\in A}p(x)+\sum_{i\in[t]}c_i\). \(\triangleright\) cost of tree with root r<br>
   return (r,C<sub>r</sub>) for r that minimizes C<sub>r</sub>.

Only the root and the total cost are returned, the full tree can be reconstructed by collecting the roots from the recursive calls with standard bookkeeping.

Line 2-3 is the base case (a tree of a single node). In Line 4 the _k_-admissible root of the current subset is selected, and in Line 5-7 the optimal subtrees are found. In Line 8 the total cost is computed with the chosen root and the roots of the optimal subtrees as its children. The first term counts the number of times the root is accessed, and the second term adds the costs of accesses in the subtrees. The correctness of the algorithm follows from the preceding discussion.

## Preprocessing.

The dynamic program is over all nonempty _k_-admissible subsets of _V(S_). In a preprocessing step we enumerate all such sets, indexed by their cuts. As only cuts of size at most _k_ are relevant, we can iterate through them by traversing _S_ with _k_ pointers. For each cut, we do another traversal of the tree, enumerating the set of nodes in the corresponding _k_-admissible subset. Observe that some cuts lead trivially to an empty set of nodes (when cut-edges point away from each other), and some cuts contain redundant edges. We can easily detect and remove these cases.

## Admissible roots.

We now discuss the finding of _k_-admissible roots (Line 4).

**Lemma 7.** _Let_ \(A\subseteq V(S)\) _be a k-admissible set and assume_ \(k\ge 2\).

(_i)_ _If_ \(|\delta(A)|<k\)_, then every node_ \(r\in A\) _is a k-admissible root of A._<tbc>

_(ii)_ _If_ \(|\delta(A)|=k\)_, then the set of k-admissible roots of A is_ \(\mathtt{ch}(\delta(A))\cap A\).

_Proof. (i)_ Let \(|\delta(A)|<k\), let \(r\in A\), and let _C_ be a connected component of _S_[_A_]\\_r_. Then, by Lemma 2, \(\delta(C)\subseteq\delta(A)\cup\{r\}\), and thus \(|\delta(C)|\le|\delta(A)|+1\le k\). Thus, _r_ is a _k_-admissible root of _A_.

_(ii)_ Let \(|\delta(A)|=k\).

Let \(r\in A\) be a _k_-admissible root. If two or more boundary nodes of _A_ are neighbors of _r_, then _r_ is in \(\mathtt{ch}(\delta(A))\). Otherwise, at least one boundary node \(u\in\delta(A)\) is not a neighbor<tbc>

