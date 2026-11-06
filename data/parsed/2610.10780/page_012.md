In Section 3.2, the subproblem _T(q_<sup>1/3</sup>_g_<sup>4</sup>_,q_<sup>2/3</sup>_g_<sup>2</sup>) was solved by counting, for each cell of the last cutting, how many annuli completely contain the cell. That approach is sufficient for approximate counting because the goal is merely to compute a number.

For distance representation, the situation is different. We must organize the target pairs into bicliques, and therefore the numbers computed in Section 3.2 are no longer useful by themselves. To overcome this difficulty, we introduce a new notion called _capture cells_. Capture cells allow us to represent a constant fraction of the certified pairs while maintaining the desired running-time bound.

In what follows, we first define capture cells and then show how they lead to the distance representation theorem.

## 4.2.1 Capture cells

For a cell \(\sigma\in\Xi\), define \(\mathcal{A}'(\sigma)\) to be the set of points \(a\in A'\) whose annuli _D<sub>a</sub>_ completely contain \(\sigma\). We further define \(\hat{A}'_\sigma\) to be the set of points \(a\in A'\) whose annuli belong to the conflict list \(\mathcal{D}'_\sigma\).

**Definition 3.** _The inequality_ \(|\mathcal{A}'(\sigma)|\ge|\hat{A}'_\sigma|\) _is called the_ capture condition.

A cell \(\sigma\) is called a _Type-I capture cell_ if it satisfies the capture condition but its parent does not. More precisely, \(\sigma\) is a Type-I capture cell if \(|\mathcal{A}'(\sigma)|\ge|\hat{A}'_\sigma|\) and \(|\mathcal{A}'(\sigma')|<|\hat{A}'_{\sigma^\prime}|\), where \(\sigma'\) is the parent of \(\sigma\). Note that a cell of \(\Xi_0\) can never satisfy the capture condition. Indeed, \(\Xi_0\) consists of a single cell equal to the entire plane, and thus \(|\mathcal{A}'(\sigma)|=0\) while \(|\hat{A}'_\sigma|=m'\).

Recall that the cells of \(\Xi\) form a tree and the cells of the last cutting \(\Xi_k\) are _leaf cells_. We consider a cell to be both an ancestor and a descendant of itself.

A leaf cell whose root-to-leaf path contains no Type-I capture cell is called a _Type-II capture cell_.

We refer to both Type-I and Type-II cells as _capture cells_, and use \(\Sigma\) to denote the set of all capture cells.

**Lemma 2.** _Every root-to-leaf path in_ \(\Xi\) _contains exactly one capture cell._

_Proof._ The Type-II capture cells guarantee that every root-to-leaf path contains at least one capture cell. Since only leaf cells can be Type-II capture cells, it suffices to show that every root-to-leaf path contains at most one Type-I capture cell.

Let \(\sigma\) be a Type-I capture cell and let \(\sigma'\) be its parent. By definition, \(|\mathcal{A}'(\sigma')|<|\hat{A}'_{\sigma^\prime}|\).

Consider any ancestor \(\sigma''\) of \(\sigma'\). Since \(\sigma''\) contains \(\sigma'\), we have \(\hat{A}'_{\sigma^\prime}\subseteq\hat{A}'_{\sigma^{\prime\prime}}\) and therefore \(|\hat{A}'_{\sigma^\prime}|\le|\hat{A}'_{\sigma^{\prime\prime}}|\). On the other hand, \(\mathcal{A}'(\sigma'')\subseteq\mathcal{A}'(\sigma')\), and thus \(|\mathcal{A}'(\sigma'')|\le|\mathcal{A}'(\sigma')|\).

Since \(|\mathcal{A}'(\sigma')|<|\hat{A}'_{\sigma^\prime}|\), it follows that \(|\mathcal{A}'(\sigma'')|<|\hat{A}'_{\sigma^{\prime\prime}}|\). Hence, \(\sigma''\) cannot satisfy the capture condition. Therefore no ancestor of \(\sigma\) (other than \(\sigma\) itself) can be a Type-I capture cell, proving the lemma.

Lemma 2 immediately implies the following.

**Corollary 1.** _Every two capture cells have disjoint interiors._

_Proof._ By Lemma 2, two capture cells cannot belong to the same root-to-leaf path. According to the definition of the hierarchical cuttings, two cells of \(\Xi\) have overlapped interiors only if one cell is the ancestor of the other. Hence, the two capture cells cannot have overlapped interiors.

For every capture cell \(\sigma\), every pair recorded by the biclique \(\mathcal{A}'(\sigma)\times B'(\sigma)\) has distance in _I_. Let C denote the collection of all such bicliques. By Corollary 1, no point of \(B'\) belongs to two sets \(B'(\sigma)\) for two capture cells. Consequently, the bicliques of C are edge-disjoint.

We add all bicliques of C to \(\Gamma\).

Lemma 3 shows that the total size of all bicliques of C is \(O(m'r'+n')\).

