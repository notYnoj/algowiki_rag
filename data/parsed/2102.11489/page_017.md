**Proof of Theorem 3.2:** Recall that \(\gamma=16\). We will choose \(\alpha\) such that \(4\cdot(16\gamma)^2\cdot\alpha^2=1\), i.e., \(\alpha=(32\gamma)^{-1}=\frac{1}{2^9}\). Moreover, suppose that we pick _C_<sub>zigzag</sub> to be sufficiently large and \(\epsilon\in(0,1)\) to be sufficiently small such that Lemma 3.3 is satisfied. We run the algorithm specified in Section 3.3.2 with the aforementioned parameters, and let _A_ be the output array. Without loss of generality, we may assume that 6_k\<_log_n_ since otherwise Ajtai et al. \[AKS83\] proved that the outcome _A_ would be sorted, and this would be the easy case.

We now divide _A_ into 2<sup>3_k_</sup> equally sized segments. We can equivalently view the 2<sup>3_k_</sup> equally sized segments as being created by the procedure specified in Fact 3.1, where \(\ell:=3k\). Pick an arbitrary segment, say, the _i_-th segment, among the 2<sup>3_k_</sup> equally sized segments. Henceforth, let _v_<sub>3_k,i_</sub> denote the _i_-th node in level 3_k_ of the 6_k_-AKS-tree.

Due to the procedure specified in Fact 3.1, we know that the _i_-th segment consists of

1. all 6_k_-AKS-intervals whose labels reside in Subtree(_v_<sub>3_k,i_</sub>) of the original 6_k_-AKS-tree (_not_ of the tree output by the procedure in Fact 3.1);<tbc>

2. a subset of the 6_k_-AKS-intervals whose labels reside in an ancestor node of _v_<sub>3_k,i_</sub> in the 6_k_-AKS- tree.

For convenience, whenever we say the level of a _t_-AKS-interval, we mean the level of its corresponding label in the _t_-AKS-tree. Let \(S_\ell\) denote the the total length of all 6_k_-AKS-intervals of level \(\ell\) contained in the _i_-th segment. It is not hard to see that for \(\ell\in[0,6k-1]\), \(S_\ell\le S_{\ell+1}/8\), by the definition of the lengths of the _t_-AKS-intervals.

For \(\ell\in[3k,6k]\), a 6_k_-AKS-interval of level \(\ell\) contained in the _i_-th segment must have tree distance at least \(\ell-3k+1\) from any 6_k_-AKS-interval not contained in the _i_-th segment.

We use the term "wrong elements" to mean elements that do not belong to the _i_-th segment if the array were sorted. Let \(W_\ell\) denote the total number of wrong elements in some 6_k_-AKS-interval of level \(\ell\) in the _i_-th segment. By Lemma 3.3, we have that<tbc>

\(W_\ell\le\alpha^{3(\ell-3k+1)+27}\cdot S_\ell\le\alpha^{3(\ell-3k+1)+27}\cdot\frac{S_{6k}}{8^{6k-\ell}}\)

<tbc>Therefore, we have that

\(\frac{\sum_{\ell\in[3k,6k]}W_\ell}{S_{6k}}\le\alpha^{3(3k+1)+27}\cdot\left(1+\frac{\alpha^{-3}}{8}+\left(\frac{\alpha^{-3}}{8}\right)^2+\dots+\left(\frac{\alpha^{-3}}{8}\right)^{3k}\right)\)<br>
\(\le\alpha\cdot\alpha^{9k}\cdot\left(\frac{\alpha^{-3}}{8}\right)^{3k}\cdot 2\le 2^{-9k}\) (⋆)

Moreover, we have that<tbc>

\(\frac{\sum_{\ell\in[0,3k-1]}S_\ell}{S_{6k}}\le\frac{1}{8^{3k+1}}\cdot\left(1+\frac{1}{8}+\dots+\frac{1}{8^{3k-1}}\right)\le\frac{1}{8^{3k+1}}\cdot 2\le 2^{-9k}\) (⋆)

<tbc>Combining (⋆) and (⋆⋆), we have that

\(\frac{\sum_{\ell\in[0,6k]}W_\ell}{S_{6k}}\le 2^{-9k}\cdot 2\le 2^{-8k}\)

Since _S_<sub>6_k_</sub> is smaller than the total length of the _i_-th segment, we have that the fraction of "misplaced" elements of the _i_-th segment must be upper bounded by 2<sup>-8_k_</sup>.

