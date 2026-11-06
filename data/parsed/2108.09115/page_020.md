### Complexity:

Notice that if the \((\mathcal{B}^\tau,\tau)\)-neighborhoods of two dense windows (or one dense and one sparse) _a_ and \(a'\) intersect, then when we process one of them as dense we will cover both. Hence we only need to run the dense subroutine at most \(t_\tau^{2/3}\) times. Each run requires \(\tilde{O}(t_\tau^{2/3})\) queries, and hence in total over the entire \(\tau\)-th iteration we only need \(\tilde{O}(t_\tau^{4/3})\) queries.

## D: Sparse windows

For each interval _I_<sub>A</sub>, out of the set of windows \(a\in I_\mathcal{A}\) which were declared sparse, we pick at random a set _S(I_<sub>A</sub>) of size log<sup>2</sup>(_n_). For every window in _S(I_<sub>A</sub>), we query its entire \((\mathcal{B}^\tau,\tau)\)- neighborhood using \(t_\tau\) queries. For each interval _I_<sub>A</sub> we record the union of all \(\tilde{O}(t_\tau^{1/3})\) intervals \(\widehat{I_{\mathcal{B}^\tau}}\) that contain any \((\mathcal{B}^\tau,\tau)\)-neighbors of any of the sparse samples \(a\in S(I_\mathcal{A})\). We call these B-windows the _relevant windows_ for the windows in _I_<sub>A</sub>. We henceforth no longer look to match windows from _I_<sub>A</sub> to irrelevant B-windows. Note that in a low-skew mapping (for more precise statement, see Lemma 14), windows in _I_<sub>A</sub> cannot be mapped to any irrelevant B-windows under that mapping. (Hence in total across all \(t_\tau^{1/3+\epsilon}\) intervals the sparse samples take \(\tilde{O}(t_\tau^{4/3+\epsilon})\) queries.)

### Approximation:

Recall that by Lemma 10 and Lemma 11, there is a low-skew monotone mapping that approximates the optimal transformation to within \((1+\epsilon)\)-factor. For any low-skew monotone mapping \(\mu\), the entire interval _I_<sub>A</sub> is mapped to a single \(\mathcal{B}^\tau\)-interval \(I_{\mathcal{B}^\tau}\). Suppose that \((1-\epsilon)\)-fraction of the sparse windows in _I_<sub>A</sub> are mapped to \(\mathcal{B}^\tau\)-windows (or \(\perp\)) of distance greater than \(\tau\). Then we can safely discard the \(\tau\)-edges for the remaining \(\epsilon\)-fraction of sparse windows with negligible loss in approximation factor. Hence in total we pay only \((1+O(\epsilon))\)-factor in approximation for sparse windows. Otherwise, w.h.p. at least one of the samples has a \((\mathcal{B}^\tau,\tau)\)-neighbor in \(I_{\mathcal{B}^\tau}\). For more details, see Lemma 14.

### Complexity:

Each uncovered A-window has only \(\tilde{O}\big(t_\tau^{1/3}\cdot t_\tau^{2/3-\epsilon}\big)=\tilde{O}(t_\tau^{1-\epsilon})\) relevant windows.

## Recursion

We recurse on Parts A-D of the algorithm, with the following modifications for the \(\ell\)-th level of the recursion.

• We increase the number of intervals to \(t_\tau^{1/3+(\ell+1)\epsilon}\), and their size decreases accordingly to \(\tilde{O}(t_\tau^{2/3-(\ell+1)\epsilon})\).<tbc>

• We only sample relevant windows when we estimate degrees. The degree-threshold for a window to be considered "dense" remains \(t_\tau^{1/3}\). Notice that a window may be dense with respect to the entire graph, but sparse with respect to its relevant windows.<tbc>

• Once we discover a dense window, we run Part C without regard to relevant/irrelevant windows. In particular the calculation of total number of queries spent on dense windows is global for the entire \(\tau\)-th iteration of the algorithm, including recursion.<tbc>

• For each sparse sample, we only compute the restriction of its \((\mathcal{B}^\tau,\tau)\)-neighborhood to relevant windows. Hence we only spend \(\tilde{O}\big(t_\tau^{1-\ell\epsilon}\big)\) queries for each sample, or a total of \(\tilde{O}\big(t_\tau^{4/3+\epsilon}\big)\) queries across all intervals.<tbc>

• The relevant windows for the next level of recursion are a (strict) subset of the relevant windows in the current level.<tbc>

