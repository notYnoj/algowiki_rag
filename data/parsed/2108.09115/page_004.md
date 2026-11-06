**Approximate edit-distance without preprocessing** Interestingly, using our algorithms _with_ preprocessing (for small and large edit distance regime), we give the fastest algorithm for approximating edit distance within \(3+\epsilon\) approximation _without_ preprocessing. Our algorithm runs in \(\tilde{O}(n^{1.6+o(1)})\) time whereas the best running time so far was \(\tilde{O}(n^{1.69+o(1)})\) \[And19\].

## More context on our results

Below we explain how the parameters in our results compare to existing literature without preprocessing. We note that another feature of our algorithms is that they are all relatively simple. Even our most technically involved contribution, the algorithm for general edit distance, is significantly simpler than related literature (e.g. \[BR19, KS19, RSSS19\]).

### Permutation-LCS

Our _O(k_log(_n_)) query time is most closely related to (and inspired by) the classic _O(n_log(_n_)) for longest increasing subsequence (LIS) without preprocessing. Note that for exact computation, even after arbitrary preprocessing \(\Omega(k)\) bits of communication are necessary, so our running time is tight up to the log(_n_) factor. Contrasting to \[AN10\], we get exact result as opposed to approximation and significantly better query time bounds for \(k=O(\sqrt{n})\).

### Small edit distance

Our _O(k_<sup>2</sup>log(_n_))-time algorithm is most closely related to (and inspired by) a classic \(\tilde{O}(n+k^2)\)-time algorithm without preprocessing. Note that our near-_n_<sup>2</sup> SETH-lower- bound for general edit distance with preprocessing extends to _k_<sup>2</sup> SETH-lower-bound by a trivial padding argument (see also \[BK18\]). Hence our running time is near-tight assuming (BP)-SETH. Contrasting to \[GKS19\], we again get exact result and better query time bound for all regimes of _k_, even when we allow single string preprocessing.

### Approximate edit distance

This result is most closely related to (and inspired by) recent subquadratic time approximation algorithms for edit distance \[BEG<sup>+</sup>18, CDG<sup>+</sup>18, And19, BR19, KS19\]. Here, the state of the art results include a \((3+\epsilon)\)-approximation in \(\tilde{O}(n^{12/7})\) time \[CDG<sup>+</sup>18\] and later improvement to time \(\tilde{O}(n^{1.69})\) \[And19\], \(f(\epsilon)\)-approximation in time \(O(n^{1.5+\epsilon})\) \[And19\], or \(f'(\epsilon)\)-approximation in time \(O(n^{1+\epsilon})\) when the true edit distance is large \[BR19, KS19\] (here \(f,f'\) are functions that go to infinity as \(\epsilon\) decreases). While the improvement is not as dramatic as for sublinear algorithms, after near-quadratic preprocessing, our algorithm is clearly faster than \[CDG<sup>+</sup>18, And19\] (_n_<sup>1.5</sup> vs _n_<sup>1.69</sup>), while obtaining much better approximation guarantees than \[And19, BR19, KS19\] (\(7+\epsilon\) vs \(f(\epsilon)\)). Interestingly, this algorithm combines ideas from aforementioned recent advances on approximate edit distance computation \[BEG<sup>+</sup>18, CDG<sup>+</sup>18, Rub18a,<tbc>

<sup>1</sup>The original paper \[CDG<sup>+</sup>18\] reported an approximation factor of 1680, but the authors confirmed that the approximation factor can be brought down to \(3+\epsilon\).

\begin{tabular}{cccc}
Authors & Time & Approximation Factor & comments \\
\[CDG<sup>+</sup>18\] & _O(n_<sup>1.714</sup>) & \(3+\epsilon^1\) & \\
\[And19\] & \(\tilde{O}(n^{1.69})\) & \(3+\epsilon\) & \\
**This paper** & \(\tilde{O}(n^{1.6+\epsilon})\) & \(3+\epsilon\) & \\
\[And19\] & \(\tilde{O}(n^{1.5+\epsilon})\) & \(f_1(\delta)\) & \\
**This paper** & \(\tilde{O}(n^{1.5+\epsilon})\) & \(7+\epsilon\) & **using \(\tilde{O}(n^2)\)-time preprocessing** \\
\[KS19, BR19\] & \(\tilde{O}(n^{1+\delta})\) & \(f_2(\delta)\) & \(+n^{1-f_3(\delta)}\) additive error \\
\end{tabular}

1: Taxonomy of Algorithms Approximating Edit Distance

