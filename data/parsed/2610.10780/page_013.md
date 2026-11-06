**Lemma 3.** \(\sum_{\sigma\in\Sigma}|\mathcal{A}'(\sigma)|=O(m'r')\) _and_ \(\sum_{\sigma\in\Sigma}(|\mathcal{A}'(\sigma)|+|B'(\sigma)|)=O(m'r'+n')\).

_Proof._ First, since the sets \(B'(\sigma)\) are pairwise disjoint for all capture cells \(\sigma\in\Sigma\), we have \(\sum_{\sigma\in\Sigma}|B'(\sigma)|=O(n')\). It therefore suffices to bound \(\sum_{\sigma\in\Sigma}|\mathcal{A}'(\sigma)|\).

For every capture cell \(\sigma\), regardless of whether it is Type-I or Type-II, its parent \(\sigma'\) does not satisfy the capture condition. Hence, \(|\mathcal{A}'(\sigma')|<|\hat{A}'_{\sigma^\prime}|\).

Every point of \(\mathcal{A}'(\sigma)\) belongs either to \(\mathcal{A}'(\sigma')\) or to \(\hat{A}'_{\sigma^\prime}\) (but not both). Therefore<tbc>

\(|\mathcal{A}'(\sigma)|\le|\mathcal{A}'(\sigma')|+|\hat{A}'_{\sigma^\prime}|<2|\hat{A}'_{\sigma^\prime}|.\)

<tbc>Summing over all capture cells and using the fact that every cell has _O_(1) children gives

\(\sum_{\sigma\in\Sigma}|\mathcal{A}'(\sigma)|=O\left(\sum_{\sigma^\prime\in\Xi}|\hat{A}'_{\sigma^\prime}|\right).\)

Since the total size of the conflict lists of all cells of \(\Xi\) is \(O(m'r')\), we have \(\sum_{\sigma^\prime\in\Xi}|\hat{A}'_{\sigma^\prime}|=O(m'r')\). The lemma follows.

**Lemma 4.** _All bicliques of_ C _can be computed in_ \(O(m'r'+n')\) _time._

_Proof._ We first identify all capture cells. After the hierarchical cutting is constructed, the conflict list \(\mathcal{D}'_\sigma\) is available for every cell \(\sigma\in\Xi\), and therefore \(|\hat{A}'_\sigma|\) is also known. We traverse the cutting tree \(\Xi\) in a top-down manner while maintaining \(|\mathcal{A}'(\sigma)|\) for every cell \(\sigma\). Since each cell has _O_(1) children, all values \(|\mathcal{A}'(\sigma)|\) can be computed in \(O(m'r')\) time. Consequently, all capture cells can be identified in \(O(m'r')\) time.

Next, we compute \(\mathcal{A}'(\sigma)\) for every capture cell \(\sigma\). For each cell \(\sigma\in\Xi\), let \(A'_\sigma\) denote the set of points \(a\in A'\) such that the annulus _D<sub>a</sub>_ contains \(\sigma\) but not the parent of \(\sigma\). As discussed in the proof of Lemma 1, all sets \(A'_\sigma\) can be computed in \(O(m'r')\) time.

Observe that \(\mathcal{A}'(\sigma)\) is precisely the union of \(A'_{\sigma^\prime}\) over all ancestors \(\sigma'\) of \(\sigma\) (where a cell is considered an ancestor of itself). Thus, for every capture cell \(\sigma\), we compute \(\mathcal{A}'(\sigma)\) by taking the union of the nonempty sets \(A'_{\sigma^\prime}\) over all ancestors \(\sigma'\) of \(\sigma\). By Lemma 3, the total size of all such sets is \(O(m'r')\), so all sets \(\mathcal{A}'(\sigma)\) can be computed within the same bound.

It remains to compute \(B'(\sigma)\) for all capture cells \(\sigma\). We first locate every point \(b\in B'\) in the last cutting. As in Section 3.2, we use the \(\Gamma\)-framework and perform each point location in amortized _O_(1) time. Hence, all point locations take \(O(n')\) amortized time.

If a capture cell \(\sigma\) is a leaf cell, then \(B'(\sigma)\) is already available. Otherwise, \(B'(\sigma)\) is the union of \(B'(\sigma'')\) over all leaf descendants \(\sigma''\) of \(\sigma\). These descendants can be found by traversing the cutting tree. Therefore, all sets \(B'(\sigma)\) can be computed in \(O(n')\) time (or \(O(n'+m'r')\) if the tree traversal is included).

Combining the above steps, all bicliques of C can be computed in \(O(m'r'+n')\) time.

Combining Lemmas 3 and 4, the subproblem \(T(m',n')\) can be solved in \(O(m'r'+n')\) time, and the total size of all bicliques produced is also \(O(m'r'+n')\).

Since \(r'=m'/g^6\), \(m'\le q^{1/3}g^4\), and \(n'\le q^{2/3}g^2\), we obtain \(T(m',n')=O(q^{2/3}g^2)\). Substituting this bound into (6) yields _T(q,q_)=_O(q_<sup>4/3</sup>_/g_<sup>2</sup>). Substituting again into (5) gives _T(n,n_)=_O(n_<sup>4/3</sup>_/g_<sup>2</sup>). Re placing _g_ by log<sup>(_i_-2)</sup>_q_ with _q_=log<sup>6</sup>log_n_, we conclude that the total running time is _O(n_<sup>4/3</sup>/(log<sup>(_i_)</sup>_n_)<sup>2</sup>). By the same analysis, the total size of all bicliques in \(\Gamma\) is also _O(n_<sup>4/3</sup>/(log<sup>(_i_)</sup>_n_)<sup>2</sup>).

The running-time and representation-size bounds of Theorem 3 are now established. It remains to prove the constant-fraction guarantee, namely that the bicliques of \(\Gamma\) record at least forty percent of the distances in \(S\cap I\). We prove this in the next subsection.

