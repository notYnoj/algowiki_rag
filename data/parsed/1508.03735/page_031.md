_Proof._ We instantiate our coordination mechanism for linearly separable convex programs with \(\eta=\varepsilon=1/(100n^3k^3)\), and round the solution to \(x'\). Applying our previous lemmas, we get that with probability at least \(1-\beta\):

\(\sum_{j=1}^kmin\left\{\sum_{i=1}^nv_{i,j}x'_{i,j},b_j\right\}\ge\widehat{V}-log(4/\beta)\sqrt{\widehat{V}}-\sqrt{nk}\varepsilon-\sqrt{3klog(2k/\beta)\widehat{V}}\)<br>
\(\ge OPT-n(\varepsilon+\eta)-log(4/\beta)\sqrt{\widehat{V}}-\sqrt{nk}\varepsilon-\sqrt{3klog(2k/\beta)\widehat{V}}\)<br>
\(\ge OPT-n(\varepsilon+\eta)-\left(log(4/\beta)+\sqrt{3klog(2k/\beta)}\right)\sqrt{OPT+n(\varepsilon+\eta)}-\sqrt{nk}\varepsilon\)<br>
\(\ge OPT-n(\varepsilon+\eta)-4\sqrt{k}log(2k/\beta)\sqrt{OPT+n(\varepsilon+\eta)}-\sqrt{nk}\varepsilon\)<br>
\(\ge OPT-8\sqrt{k}log(2k/\beta)\sqrt{OPT}\)

which recovers the stated bound. Note that the coordination complexity of this mechanism is _O(k_log(_nk_)) by Lemma 5.

