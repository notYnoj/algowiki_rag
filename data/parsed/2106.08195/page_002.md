These strong hardness results naturally bring up the question whether LCS or edit distance can be efficiently _approximated_ (namely, whether an algorithm with truly subquadratic time \(O(n^{2-\varepsilon})\) for any constant \(\varepsilon>0\), can produce a _good_ approximation in the worst-case). In the last two decades, significant progress has been made towards designing efficient approximation algorithms for edit distance \[14, 13, 15, 9, 7, 21, 23, 29, 17\]; the latest achievement is a constant-factor approximation in almost-linear<sup>1</sup> time \[8\].

For LCS the picture is much more frustrating. The LCS problem has a simple \(\widetilde{O}(n^{\varepsilon/2})\)-approximation algorithm with running time \(O(n^{2-\varepsilon})\) for any constant \(0<\varepsilon<1\), and it has a trivial \(|\Sigma|\)-approximation algorithm with running time _O(n_) for strings over alphabet \(\Sigma\). Yet, improving upon these naive bounds has evaded the community until very recently, making LCS a notoriously hard problem to approximate. In 2019, Rubinstein et al. \[33\] presented a subquadratic-time \(O(\lambda^3)\)-approximation, where \(\lambda\) is the ratio of the string length to the length of the optimal LCS. For binary alphabet, Rubinstein and Song \[34\] recently improved the 2-approximation. In the general case (where \(\lambda\) and the alphabet size are arbitrary), the naive \(O(\sqrt{n})\)- approximation in near-linear<sup>2</sup> time was recently beaten by Hajiaghayi et al. \[24\], who designed a linear-time algorithm that computes an _O(n_<sup>0.497956</sup>)-approximation _in expectation_.<sup>3</sup> Nonetheless, the gap between the upper bound provided by Hajiaghayi et al. \[24\] and the recent results on hardness of approximation \[1, 5\] remains huge.

### 1.1 Our Contribution

We present a randomized \(\widetilde{O}(n^{0.4})\)-approximation for LCS running in linear time _O(n_), where the approximation guarantee holds _with high probability_<sup>4</sup>. More generally, we obtain a tradeoff between approximation guarantee and running time: For any \(0<\varepsilon\le 1\) we achieve approximation ratio \(\widetilde{O}(n^{2\varepsilon/5})\) in time \(O(n^{2-\varepsilon})\). Formally we prove the following:

**Theorem 1.** _There is a randomized algorithm that, given strings x,y of length_ \(n\ge 1\) _and a time budget_ \(T\in[n,n^2]\)_, with high probability computes a multiplicative_ \(\widetilde{O}(n^{0.8}/T^{0.4})\)_-approximation of the length of the LCS of x and y in time O(T)._

The improvement over the state of the art can be summarized as follows:

1. An improved approximation ratio for the linear time regime: from _O(n_<sup>0.497956</sup>) \[24\] to \(\widetilde{O}(n^{0.4})\);<tbc>

2. The first algorithm which improves upon the naive bound _with high probability_<sup>4</sup>;<tbc>

3. A generalization to running time \(O(n^{2-\varepsilon})\), breaking the naive approximation ratio \(\widetilde{O}(n^{\varepsilon/2})\) in general.

## 2 Technical Overview

We combine classic exact algorithms for LCS with different subsampling strategies to develop several algorithms that work in different regimes of the problem. A combination of these algorithms then yields the full approximation algorithm.

Our Algorithm 1 covers the regime of short LCS, i.e., when the LCS has length at most \(n^\gamma\) for an appropriate constant \(\gamma<1\) depending on the running time budget. In this regime, we decrease the length of the string _x_ by subsampling. This naturally allows to run classic exact algorithms for LCS on the subsampled string _x_ (which now has significantly smaller size) and the original string _y_, while not deteriorating the LCS between the two strings too much.

<sup>1</sup>By _almost-linear_ we mean time \(O(n^{1+\varepsilon})\) for a constant \(\varepsilon>0\) that can be chosen arbitrarily small. <sup>2</sup>By _near-linear_ we mean time \(\widetilde{O}(n)\), where \(\widetilde{O}\) hides polylogarithmic factors in _n_. <sup>3</sup>While the SODA proceedings version of \[24\] claimed a high probability bound, the newer corrected Arxiv version \[25\] only claims that the algorithm outputs an _O(n_<sup>0.497956</sup>)-approximation in expectation. Personal communications with the authors confirm that the result indeed holds only in expectation, see also Remark 14. <sup>4</sup>We say that an event happens _with high probability_ (w.h.p.) if it has probability at least 1-_n_<sup>-_c_</sup>, where the constant _c\>_0 can be chosen in advance.

