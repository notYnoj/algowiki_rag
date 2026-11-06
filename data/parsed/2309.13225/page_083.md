**Corollary E.11.** _Let_ \(k\ge 4\) _be an even integer. Then, we can compute a_ (2,0)_-approximation for distances_ \(\delta(u,v)\ge k\) _ combinatorially in expected time_

\(\tilde{O}\left(\mathrm{min}\left(n^{2-\frac{2}{k+4}}m^\frac{2}{k+4},n^{2+\frac{1}{2(k-1)}},n^{2+\frac{2}{3k+2}}\right)\right)\)

_In particular, we output_ \(\hat{\delta}\) _such that_ \(\delta(u,v)\le\hat{\delta}(u,v)\) _for all u,v and_ \(\hat{\delta}(u,v)\le 2\delta(u,v)\) _whenever_ \(\delta(u,v)\ge k\).

_Proof._ We combine Theorem 4.1, Theorem E.1, Lemma 3.2 and Lemma E.10. If \(n^{2-\frac{2}{k+4}}m^\frac{2}{k+4}\) is the minimum term, we invoke the algorithm of Lemma E.10 with \(k'=k+2\) and the algorithm **SparseAPASP** of _Lemma_ 3.2 with \(\beta=k+2\). For paths of length \(k\le\delta(u,v)\le k+2\), we obtain a +_k_ approximation from Lemma E.10. For paths of length \(\delta(u,v)\ge k+2\), we obtain a +(_k_+2) approximation from **SparseAPASP**. In either case, we obtain a (2,0) approximation for all \(\delta(u,v)\ge k\). The overall running time is,

\(\tilde{O}(n^{2-\frac{2}{k+4}}m^\frac{2}{k+4})\)

On the other hand, if \(n^{2+\frac{1}{2(k-1)}}\) is the minimum term, we invoke Algorithm 4 and obtain a (2,0) approximation for paths of length at least _k_ following Theorem 4.1.

Finally, if \(n^{2+\frac{2}{3k+2}}\) is the minimum term, we call Theorem E.1 with \(k'=k+1\) and **DenseAPASP** with \(\beta=k+2\). For any path of length at least _k_+2, the estimate from **DenseAPASP** is a (2,0)- approximation. For paths of length \(k\le\delta(u,v)\le k+1\), the estimate from **ShortAdditiveAPASP** is a (2,0)-approximation. The overall computation time can be bounded by,

\(\tilde{O}\left(n^{2+\frac{2}{3k+2}}+n^{2+\frac{2}{3(k+2)-2}}\right)=\tilde{O}\left(n^{2+\frac{2}{3k+2}}\right)\)

Note that for _k_=6, \(n^{2+\frac{1}{2(k-1)}}=n^{21/10}=n^{2+\frac{2}{3k-2}}\). For larger _k_, the former term is smaller and we apply Theorem 4.1. However, for _k_=4,5, Algorithm 15 gives the best bound (see  1).

