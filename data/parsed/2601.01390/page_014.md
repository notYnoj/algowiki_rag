<tbc>operator \(\mathsf{p}\text{-}\mathsf{MAX}(A)=\left\{(w,p^*)\in A:p^*=max_{(w,p)\in A}p\right\}\). The problem is then equivalent to the following: given a set of _n_ two-dimensional points \(X\subset[t]\times\mathbb{R}^+\), compute \(\mathsf{p}\text{-}\mathsf{MAX}(\Sigma(X)\cap([t]\times\mathbb{R}^+))\), where \(\Sigma(\cdot)\) is defined exactly as before (additions are now performed in two dimensions). We may assume that \(n\le t\) after an initial _O(n_)-time preprocessing (replacing _X_ with \(\mathsf{p}\text{-}\mathsf{MAX}(X\cap([t]\times\mathbb{R}^+))\)).

Cygan, Mucha, Węrzycki, and Włodarczyk \[CMWW19\] and Künnemann, Paturi, and Schneider \[KPS17\] gave deterministic reductions from min-plus convolution to all-targets 0-1 knapsack. In the reverse direction, Cygan et al. \[CMWW19\] gave a _randomized_ reduction from all-targets 0-1 knapsack to min-plus convolution, by modifying Bringmann’s randomized algorithm for subset sum \[Bri17\]. We can obtain a deterministic reduction from all-targets 0-1 knapsack to min-plus convolution by modifying the algorithm in Section 2.

The modification is mostly straightforward. We mention some of the main changes:

• Expressions such as \(X\cap I\) should be reinterpreted as \(X\cap(I\times\mathbb{R}^+)\).<tbc>

• Most occurrences of \(\Sigma_i(X)\) should be changed to \(\mathsf{p}\text{-}\mathsf{MAX}(\Sigma_i(X))\).<tbc>

• Each sumset _A+B_ should be changed to \(\mathsf{p}\text{-}\mathsf{MAX}(A+B)\). Given \(A,B\subseteq[t]\times\mathbb{R}^+\), the computation of \(\mathsf{p}\text{-}\mathsf{MAX}(A+B)\) is equivalent to max-plus convolution over two real vectors of length _O(t_), which is equivalent to min-plus convolution by negation.<tbc>

• In Definition 2.2 on halvers, the property is now:<tbc>

<tbc>For every subset \(S\subseteq X\) with \(|S|\le k\) and \(\sigma(S)\in\mathsf{p}\text{-}\mathsf{MAX}(\Sigma_{\le k}(X))\), there exists a subset \(\hat{S}\subseteq X\) with \(|\hat{S}|\le k\), \(\sigma(\hat{S})=\sigma(S)\), and \(|\hat{S}\cap X'|,|\hat{S}\cap X''|\le|\hat{S}|/2+\Delta\).<tbc>

• In Lemma 2.4 on canonical subset generation, the property is now:<tbc>

<tbc>For every subset \(S\subseteq X\) with \(\sigma(S)\in\mathsf{p}\text{-}\mathsf{MAX}(\Sigma_{|S|}(X))\), there exists a subset \(\hat{S}\subseteq X\) such that \(|\hat{S}|=|S|\), \(\sigma(\hat{S})=\sigma(S)\), and \(\hat{S}\) is expressible as a union of _O_((|_S|/b_+1)log_u_) disjoint canonical subsets in C.<tbc>

<tbc>Note that if \(\sigma(S)\in\mathsf{p}\text{-}\mathsf{MAX}(\Sigma_{|S|}(X))\), then for any interval _I_, we must also have \(\sigma(S\cap(I\times\mathbb{R}^+))\in\mathsf{p}\text{-}\mathsf{MAX}_{|S\cap(I\times\mathbb{R}^+)|}(X\cap(I\times\mathbb{R}^+))\).<tbc>

• In Lemma 2.6, we are now computing a set \(\mathsf{OUT}\subseteq[ku]\times\mathbb{R}^+\) such that \(\mathsf{p}\text{-}\mathsf{MAX}(\Sigma_{\le k}(X))\subseteq\{(w,p'):p'\ge p,(w,p)\in\mathsf{OUT}\}\) and \(\mathsf{OUT}\subseteq\Sigma(X)\).

The rest of the changes are easy to work out.

**Theorem A.1.** _If min-plus convolution for two real vectors of length n could be computed in T(n_) _deterministic time, then the all-capacities version of the 0-1 knapsack problem could be solved in_ \(\widetilde{O}(T(t))\) _deterministic time._

