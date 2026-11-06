blocks we set \(\widetilde{L}_{ij}=\frac{\hat{L}}{4\sqrt{T}}\), while for the remaining blocks we set \(\widetilde{L}_{ij}=0\). Finally, we perform dynamic programming to determine the maximum \(\sum_{(i,j)\in\mathcal{S}}\widetilde{L}_{ij}\) over all block sequences S.

Observe that for each block in \(\mathcal{G}\cap\mathcal{R}\) this algorithm sets \(\widetilde{L}_{ij}=\frac{\hat{L}}{4\sqrt{T}}\), so it detects a random subset of G. We thus obtain a _p_-fraction of the LCS guaranteed by the block sequence G.

Note that in this algorithm we may focus on blocks with \(M_{ij}=O(\frac{\mu n}{L\sqrt{T}})\), since this holds for all blocks in G. Moreover, since \(\lambda\) is small, most blocks outside of G have small LCS _L<sub>ij</sub>_. These bounds on _L<sub>ij</sub>_ and _M<sub>ij</sub>_ for the considered blocks allow us to bound the running time of the basic decision algorithm. We elaborate this algorithm in the following theorem.

**Theorem 17** (Algorithm 4)**.** _We can compute in expected time_ \(\widetilde{O}(T)\) _an estimate_ \(\widetilde{L}\le L\) _that w.h.p. satisfies_

\(\widetilde{L}=\Omega\big(min\big\{\frac{L^3}{n^2},\frac{L^3T}{\lambda n^2},\frac{L^4T}{\lambda\mu n^2}\big\}\big),\text{\textit{assuming that}}\frac{L^2T^{0.5}}{n^2},\frac{L^2T^{1.5}}{\lambda n^2},\frac{L^3T^{1.5}}{\lambda\mu n^2}=n^{\Omega(1)}.\)

_Proof._ Algorithm 4 works as follows.

1. Run Lemma 6 with \(q:=\frac{M}{T}\) to compute values \(\widetilde{M}_{ij}\). Initialize \(\widetilde{L}_{ij}=0\) for all _i,j_.<tbc>

2. Run the preprocessing of the basic decision algorithm (Lemma 5) on each string _y<sub>j</sub>_.<tbc>

3. Sample a set \(\mathcal{R}\subseteq[n/m]^2\) by including each block (_i,j_) independently with probability<tbc>

\(p:=min\big\{\frac{\hat{L}}{n},\frac{\hat{L}T}{\hat{\lambda}n},\frac{\hat{L}^2T}{\hat{\lambda}\hat{\mu}n}\big\}.\)

4. For each \((i,j)\in\mathcal{R}\) with \(\widetilde{M}_{ij}\le 64\hat{\mu}n/(\hat{L}\sqrt{T})\): Run the query of the basic decision algorithm (Lemma 5) to test whether \(L_{ij}\ge\frac{\hat{L}}{4\sqrt{T}}\). If this test is successful then set \(\widetilde{L}_{ij}:=\frac{\hat{L}}{4\sqrt{T}}\).<tbc>

5. Perform dynamic programming over \[_n/m_\]<sup>2</sup> to determine the maximum \(\sum_{(i,j)\in\mathcal{S}}\widetilde{L}_{ij}\) over all block sequences S. Output this maximum value \(\widetilde{L}\).

## Upper Bound:

Since Lemma 5 has no false positives, we ensure \(\widetilde{L}_{ij}\le L_{ij}\) and thus \(\widetilde{L}\le L\).

## Approximation Guarantee:

The values \(\widetilde{M}_{ij}\) computed in Step 1 w.h.p. satisfy \(M_{ij}/8-q\le\widetilde{M}_{ij}\le 4M_{ij}\). For all blocks \((i,j)\in\mathcal{G}\) we have \(M_{ij}\le\frac{8\mu n}{L\sqrt{T}}\) (by Lemma 11) and thus w.h.p. \(\widetilde{M}_{ij}\le\frac{32\mu n}{L\sqrt{T}}\). We may assume that our guesses \(\hat{L},\hat{\mu}\) satisfy \(L/2\le\hat{L}\le L\) and \(\mu/2\le\hat{\mu}\le\mu\); then we obtain \(\widetilde{M}_{ij}\le\frac{64\hat{\mu}n}{L\sqrt{T}}\) .

Therefore, each block in \(\mathcal{G}\cap\mathcal{R}\) satisfies the property checked in Step 4, that is, for each such block we run the basic decision algorithm. Since for each \((i,j)\in\mathcal{G}\) we have \(L_{ij}\ge\frac{L}{4\sqrt{T}}\ge\frac{\hat{L}}{4\sqrt{T}}\), in Step 4 for each block in \(\mathcal{G}\cap\mathcal{R}\) w.h.p. we obtain an estimate \(\widetilde{L}_{ij}=\frac{\hat{L}}{4\sqrt{T}}\). Since G is a block sequence, also \(\mathcal{G}\cap\mathcal{R}\) is a block sequence, and thus the dynamic programming in Step 5 returns an estimate of<tbc>

\(\widetilde{L}\ge\sum_{(i,j)\in\mathcal{G}\cap\mathcal{R}}\widetilde{L}_{ij}=|\mathcal{G}\cap\mathcal{R}|\cdot\frac{\hat{L}}{4\sqrt{T}}.\)

<tbc>Note that the size \(|\mathcal{G}\cap\mathcal{R}|\) is distributed as a binomial random variable Bin(|G|_,p_), with expectation _p_|G|. Assuming that our guesses \(\hat{L},\hat{\lambda},\hat{\mu}\) are correct up to constant factors, we have

\(p|\mathcal{G}|=\Omega\big(min\big\{\frac{L}{n},\frac{LT}{\lambda n},\frac{L^2T}{\lambda\mu n}\big\}\cdot\frac{L\sqrt{T}}{n}\big)=\Omega\big(min\big(\frac{L^2T^{0.5}}{n^2},\frac{L^2T^{1.5}}{\lambda n^2},\frac{L^3T^{1.5}}{\lambda\mu n^2}\big)\big)=n^{\Omega(1)},\)

