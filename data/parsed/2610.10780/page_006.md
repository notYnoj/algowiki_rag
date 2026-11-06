We say that a cutting \(\Xi'c\)_-refines_ a cutting \(\Xi\) if every cell of \(\Xi'\) is contained in a cell of \(\Xi\) and every cell of \(\Xi\) contains at most _c_ cells of \(\Xi'\).

A _hierarchical_ (1_/r)-cutting_ for D is a sequence of cuttings \(\Xi_0,\Xi_1,\dots,\Xi_k\) such that:

1. \(\Xi_ic\)-refines \(\Xi_{i-1}\) for every \(1\le i\le k\), for some constant _c_;<tbc>

2. for each \(1\le i\le k\), \(\Xi_i\) is a \((1/\rho^i)\)-cutting of size \(O(\rho^{2i})\), for some constant \(\rho\);<tbc>

3. \(\Xi_0\) consists of a single cell equal to the entire plane.

Setting \(k=\lceil log_\rho r\rceil\) makes the last cutting \(\Xi_k\) a (1_/r_)-cutting of size _O(r_<sup>2</sup>), which is also the total size of all cuttings in the hierarchy.

If a cell \(\sigma\in\Xi_i\) is contained in a cell \(\sigma'\in\Xi_{i-1}\), then \(\sigma'\) is called the _parent_ of \(\sigma\), and \(\sigma\) is called a _child_ of \(\sigma'\). In this way, the cells form a tree, called the _cutting tree_, whose root is the unique cell of \(\Xi_0\). We often use \(\Xi\) to denote the set of all cells in all cuttings in the hierarchy. We also view \(\Xi\) as the corresponding cutting tree and use the notions of ancestors and descendants.

A hierarchical (1_/r_)-cutting for D can be computed in _O(mr_) time for any \(1\le r\le m\), e.g., by the algorithm of Wang \[24\], which adapts Chazelle’s construction \[12\]. The algorithm also computes the conflict list \(\mathcal{D}_\sigma\) for every cell \(\sigma\in\Xi\). Consequently, the total size of all conflict lists is _O(mr_).

## Algorithm for Lemma 1.

We briefly review the algorithm; see \[28\] for details.

We first construct a hierarchical (1_/r_)-cutting \(\{\Xi_0,\Xi_1,\dots,\Xi_k\}\) for D, which takes _O(mr_) time. We use \(\Xi\) to denote the set of all cutting cells.

For each cell \(\sigma\in\Xi\), we compute a canonical subset \(B(\sigma)=B\cap\sigma\). This can be done in _O(n_log_r_) time by processing the points of _B_ in a top-down manner through the cutting tree. Since \(k=\Theta(logr)\), each point of _B_ is stored in _O_(log_r_) canonical subsets. Hence, the total size of all canonical subsets \(B(\sigma)\), \(\sigma\in\Xi\), is _O(n_log_r_).

Next, for each cell \(\sigma\in\Xi\), we compute another canonical subset \(A_\sigma\subseteq A\). Specifically, a point \(a\in A\) belongs to \(A_\sigma\) if the annulus _D<sub>a</sub>_ contains \(\sigma\) but does not contain the parent of \(\sigma\). Since each cell has _O_(1) children, all subsets \(A_\sigma\) can be computed in _O(mr_) time in a top-down manner. The total size of all subsets \(A_\sigma\) is also _O(mr_).

By definition, for every cell \(\sigma\in\Xi\), every pair \((a,b)\in A_\sigma\times B(\sigma)\) satisfies \(\|ab\|\in I\). Therefore, we add the biclique \(A_\sigma\times B(\sigma)\) to \(\Gamma\). The resulting bicliques are edge-disjoint. We have shown that \(\sum_{\sigma\in\Xi}|A_\sigma|=O(mr)\) and \(\sum_{\sigma\in\Xi}|B(\sigma)|=O(nlogr)\).

Consider now a cell \(\sigma\) of the last cutting \(\Xi_k\). Since \(|\mathcal{D}_\sigma|\le m/r\), define \(\hat{A}_\sigma=\{a\in A|D_a\in\mathcal{D}_\sigma\}\). We do not know whether distances between points of \(\hat{A}_\sigma\) and points of \(B(\sigma)\) lie in _I_. If \(|B(\sigma)|>n/r^2\), then we partition \(B(\sigma)\) into subsets of size between _n/_(2_r_<sup>2</sup>) and _n/r_<sup>2</sup>, called _standard subsets_. Since |_B_|=_n_ and \(\Xi_k\) contains _O(r_<sup>2</sup>) cells, the total number of standard subsets over all cells of \(\Xi_k\) is _O(r_<sup>2</sup>).

For each standard subset \(\hat{B}(\sigma)\subseteq B(\sigma)\), we form a recursive subproblem \((\hat{A}_\sigma,\hat{B}(\sigma))\). There are _O(r_<sup>2</sup>) such subproblems. Since \(|\hat{A}_\sigma|\le m/r\) and \(|\hat{B}(\sigma)|\le n/r^2\), the running time satisfies the recurrence

\(T(m,n)=O(mr+nlogr)+O(r^2)\cdot T\big(\frac{m}{r},\frac{n}{r^2}\big).\) (1)

Throughout the paper, we use _T(m,n_) interchangeably to denote both the running time and the corresponding subproblem involving two point sets of sizes _m_ and _n_.

We next solve the problem in a dual setting by switching the roles of _A_ and _B_, i.e., defining annuli centered at the points of _B_. Symmetrically, we obtain

\(T(m,n)=O(nr+mlogr)+O(r^2)\cdot T\big(\frac{m}{r^2},\frac{n}{r}\big).\) (2)

