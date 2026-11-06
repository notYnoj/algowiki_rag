Indeed, observe that whenever the algorithm completes step B, then it is the case that with high probability all but at most \(\epsilon\)-fraction of dense windows are already covered. If this is the case, then for each covered window \(a\in I_\mathcal{A}\) we have: \(\mathcal{E}(a,\mu(a))\le 7\mathrm{ED}(a,\mu(a))\). For the rest we have no guarantee on \(\mathcal{E}(a,\mu(a))\). However, even if we map _all_ these edges to \(\perp\), we only lose a \((1+\epsilon)\) factor in the edit distance. The claim follows.

We therefore have the following theorem.

_Theorem_ 15_. Given two strings_ \(A,B\in\Sigma^n\)_, we can approximate_ ED(_A,B_) _within_ 7+_o_(1) _approximation with probability at least_ \(1-\frac{1}{n}\) _with a preprocessing time of_ \(\tilde{O}_\epsilon(n^2)\) _and query time of_ \(\tilde{O}_\epsilon(n^{3/2+o(1)})\).

## 6 No preprocessing: 3+_o_(1)-approx in _n_<sup>1.6+_o_(1)</sup> time

In this section we introduce our (3+_o_(1))-approximation algorithm for edit distance that runs in time _n_<sup>1.6+_o_(1)</sup> without preprocessing. At a high level, it is similar to other recent triangle- inequality based approximation algorithms for edit distance. In particular, the previous state of the art algorithm by Andoni \[And19\] obtains a similar result when the edit distance is large (near- linear), but we can give an overall faster algorithm using the sublinear algorithm for small edit distance with preprocessing (Section 3). The preprocessing cost is negligible when we apply it once to each window, and use the sublinear algorithm to compute the distances of many pairs.

_Theorem_ 16 (Approximate edit distance without preprocessing).

_Given two strings_ \(A,B\in\Sigma^n\)_, we can approximate_ ED(_A,B_) _within_ 3+_o_(1) _approximation in_ \(\tilde{O}_\epsilon(n^{1.6+o(1)})\) _time with probability at least_ \(1-\frac{1}{n}\).

### High level idea

The algorithm enumerates over various thresholds \(\tau\). For each value of \(\tau\), the algorithm first marks all the A-windows as \(\tau\)-uncovered. Then, it uses sampling to estimate the degree of each A window, and classifies them as sparse or dense. It handles sparse windows similarly to Section 5. As for the dense windows, if there are few of them, it exhaustively finds their \((\mathcal{B},\tau)\)-neighbors. Otherwise, it sparsifies the set of uncovered dense windows as follows. It enumerates over the set of B windows: For each such a window _b_ it estimates its degree with respect to uncovered dense windows. If the degree is large, then it computes \(\mathcal{N}^{\mathcal{A},2\tau}(b),\mathcal{N}^{\mathcal{B},\tau}(b)\), marks that the relative distance between pairs in \(\mathcal{N}^{\mathcal{A},2\tau}(b)\times\mathcal{N}^{\mathcal{B},\tau}(b)\) as upper bounded by \(3\tau\). It then moves each uncovered dense window in \(\mathcal{N}^{\mathcal{A},2\tau}(b)\) to the set of covered windows. In such a way, since we remove the neighborhood of dense B-windows, we show that the number of uncovered dense A- windows decreases significantly. We recurse on the sparsification phase; each iteration uses a smaller degree threshold for dense B-windows and handles fewer remaining uncovered dense A-windows.

### Similarities to Section 5 Algorithm

Similar to Section 5 and other recent approximation algorithms, we partition the input strings into windows, and consider the close-window graph where two windows share an edge if they are close in edit distance. We handle high-degree ("dense") windows using triangle inequality, and low-degree ("sparse") by iteratively focusing on narrowing intervals.

### Main technical difference compared to Section 5 Algorithm

A subtle technicality of this algorithm is that in the sparsification phase, we can remove B-windows of high degree, and all their A-neighbors. This suffices to ensure that the remaining A-windows are sparse _on_<tbc>

