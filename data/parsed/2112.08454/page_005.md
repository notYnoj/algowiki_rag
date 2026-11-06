## 3 Reduction Algorithm

In this section we prove Lemma 6. Namely, we are given an algorithm A<sub>BL</sub> for solving Block-LIS(_z_) with additive error parameter \(\lambda\), and we use it to estimate LCS(_x,y_).

The algorithm is the straight-forward one:

### 3.1 Analysis

We show the above algorithm provides the guarantees of Lemma 6.

_Proof of Lemma 6._ First, let us argue \(\widehat{\ell}\in\left[\frac{1-o(1)}{f(nlogn)},1\right]\cdot\text{LCS}(x,y)\).

**Upper Bound.** The upper-bound is immediate since the output of A<sub>BL</sub> is promised to be at most Block-LIS(_z_)=LCS(_x,y_), and since \(d\le\text{LCS}(x,y)\) from Lemma 9.

**Lower Bound.** Let \(\widehat{\ell_\mathcal{A}}\) be the output of A<sub>BL</sub>. Then, we are guaranteed

\(\widehat{\ell_\mathcal{A}}\ge\frac{\text{Block-LIS}(z)}{f(|z|/\lambda)}-\lambda n=\frac{\text{LCS}(x,y)}{f(nlogn)}-\frac{2d}{logn}.\)

Therefore, \(\widehat{\ell}=max\{\widehat{\ell_\mathcal{A}},d\}\ge(1-o(1))\cdot\frac{\text{LCS}(x,y)}{f(nlogn)}\) as needed.

Last, we show the runtime is at most \(t\left(O(n\cdot log(n)),n\right)+O(n)\).

**Runtime Analysis.** The runtime for the first 2 steps is clearly _O(n_). It remains to show the runtime on the Block-LIS algorithm, which is promised to be at most

\(t\left(\frac{|z|}{\lambda n},n\right)=t\left(\frac{2d}{\lambda},n\right)=t\left(O(n\cdot log(n)),n\right).\)

This concludes the proof.

## 4 Acknowledgements

The author would like to thank Alexandr Andoni for useful discussion and comments on earlier drafts of this note.

EstimateLCS(x,y):
1. Store the function y-1 over (say, in the sparse matrix representation).
2. Set d |z/2n, where z is defined as in Equation (1).
3. Run ABL with input z and () (n logn
4. Output () the maximum between d and the output of ABL.
Figure 1: Description of the algorithm for estimating the LCS between x and y
We show the above algorithm provides the guarantees of Lemma 6.

Figure 1: Description of the algorithm for estimating the LCS between _x_ and _y_

