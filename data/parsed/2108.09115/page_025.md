### Approximation (first iteration):

Recall that by Lemma 10 and Lemma 11, there is a low-skew monotone mapping that approximates the optimal transformation to within \((1+O(\epsilon))\)-factor. For any low-skew monotone mapping \(\mu\), the entire interval _I_<sub>A</sub> is mapped to a single \(\mathcal{B}^\tau\)-interval \(I_{\mathcal{B}^\tau}\). Suppose that \((1-\epsilon)\)-fraction of the sparse windows in _I_<sub>A</sub> are mapped to \(\mathcal{B}^\tau\)-windows (or \(\perp\)) of distance greater than \(\tau\). Then we can safely discard the \(\tau\)-edges for the remaining \(\epsilon\)-fraction of sparse windows with negligible loss in approximation factor. Hence in total we pay only \((1+O(\epsilon))\)- factor in approximation for sparse windows. Otherwise, w.h.p. at least one of the samples has a \((\mathcal{B}^\tau,\tau)\)-neighbor in \(I_{\mathcal{B}^\tau}\).

### Complexity (first iteration):

Each sparse A-window has only \(\tilde{O}\left(t_\tau^{1/2+\epsilon}\cdot t_\tau^{1/2-2\epsilon}\right)=\tilde{O}(t_\tau^{1-\epsilon})\) relevant windows. Since there are \(t_\tau^{1/2+2\epsilon}\mathcal{A}\)-intervals, we spend use a total of \(\tilde{O}(t_\tau^{3/2+\epsilon})\) queries.

### Recursion

We recurse on the sparse subroutine, with the following modifications for the \(\ell\)-th iteration.

• We increase the number of intervals to \(t_\tau^{1/2+(\ell+2)\epsilon}\), and their size decreases accordingly to \(\tilde{O}(t_\tau^{1/2-(\ell+2)\epsilon})\).<tbc>

• For each sparse sample, we only compute the restriction of its \((\mathcal{B}^\tau,\tau)\)-neighborhood to relevant windows. Hence we only spend \(\tilde{O}\left(t_\tau^{1-\ell\epsilon}\right)\) queries for each sample, or a total of \(\tilde{O}\left(t_\tau^{3/2+\epsilon}\right)\) queries across all intervals.<tbc>

• The relevant windows for the next level of recursion are a (strict) subset of the relevant windows in the current level.

The recursion continues until each interval has less than log<sup>2</sup>(_n_) sparse windows, after which we can simply query the distance of every remaining sparse window to all its relevant \(\mathcal{B}_\tau\)-windows.

### Completing the proof of Theorem 16

As we argued above, the algorithm finds a \((3+\epsilon)\)-approximation using \(\tilde{O}(t_\tau^{3/2+\epsilon})\) queries. Taking \(\epsilon\) to be slightly sub-constant completes the proof of Theorem 16.

## 7 Hardness

In this section we formalize, in the context of (approximate) edit distance, the folklore intuition (based on \[WW18\]) that polynomial preprocessing can not circumvent fine-grained complexity lower bounds. In Subsection 7.1 we show that known fine-grained complexity hardness results for exact edit distance and related problems extend to accommodate polynomial preprocessing.

In Subsection 7.2 we consider the problem of edit distance approximation. There are essentially no conditional hardness results for this problem, and in fact recent work obtained a truly- subquadratic constant factor approximation algorithm \[CDG<sup>+</sup>18\]. Improving this factor, and in particular obtaining a truly-subquadratic \((1+\epsilon)\)-approximation factor, is perhaps the most important open problem in this area. There are evidences that providing 1+_o_(1)-factor approximation might be hard, as it implies new circuit lower bounds \[AB17\]. Theorem 20 shows that essentially any approximation factor that is obtained with polynomial preprocessing can also be obtained without it. Note that this holds unconditionally, even if (BP)-SETH is false.

