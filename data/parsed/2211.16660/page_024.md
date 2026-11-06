**Claim.** _If_ \(k\ge 0\), \(1<i\le 2^{K-k}\), \(I_{k,i}\in\mathcal{S}\)_, t_=2<sup>max(0_,k_-5)</sup>_, and_ pred(_I<sub>k,i</sub>_) _is dense, then the number of t-flags in_ pred(_I<sub>k,i</sub>_) _is at least_ \(0.01\cdot|\mathsf{pred}(I_{k,i})|\).

_Proof._ If _k\<_5 then the assumption that _I<sub>k,i</sub>_ is sparse implies that it contains only zeros, so the first one-bit in pred(_I<sub>k,i</sub>_) is a 1-flag, and this is sufficient. Assume now that \(k\ge 5\). Observe that since _I<sub>k,i</sub>_ is sparse, it contains at least \(0.99\cdot 2^k>2^{k-1}>10(t-1)\) zeros and at most \(0.01\cdot 2^k<2^{k-6}=t/2\) ones. In particular, the last _t/_2=2<sup>_k_-6</sup> ones in _x_<sub>pred(_I<sub>k,i</sub>_)</sub> (or all of them if there are fewer than 2<sup>_k_-6</sup>) must all be _t_-flags. As pred(_I<sub>k,i</sub>_) is dense, we are done.

Thus, dense predecessors of elements of S contain many flags. In order to make sure these flags are not double-counted, we first pass to a subcollection of S, defined as follows. Write if \(I,J\in\mathcal{S}\), write _I\<J_ if both pred(_I_) and pred(_J_) exist, and \(\mathsf{pred}(I)\subset\mathsf{pred}(J)\). Define \(\mathcal{S}'\) to be the subcollection of S obtained by removing the (at most one) element of the form _I_<sub>_k,_0</sub> without a predecessor, and then removing all elements non-maximal with respect to _\<_. Observe that if two dyadic intervals satisfy \(I\unknown J\), then \(I\subseteq\mathsf{pred}(J)\), so for any dyadic interval _J_, the total length of all elements _I_ of S satisfying \(I\unknown J\) is at most |_J_|. By passing to \(\mathcal{S}'\), we deleted at most half of the total length in S, plus possibly one interval with no predecessor, which has length at most \(\varepsilon^2w\). Thus,<tbc>

\(\sum_{I\in\mathcal{S}^\prime}|I|\ge\frac{1}{2}\sum_{I\in\mathcal{S}}|I|-\varepsilon^2w\ge 0.1w.\)

<tbc>Writing \(\mathcal{S}'_{\ge k}\) for the collection of all intervals in \(\mathcal{S}'\) with length at least 2_<sup>k</sup>_, we pick _k_<sub>0</sub> to be the largest \(0\le k_0\le K\) for which

\(\sum_{I\in\mathcal{S}_{\ge k_0}^\prime}|I|\ge 0.01w.\)

Our choice of \(\ell\) is \(\ell:=2^{\mathrm{max}(0,k_0-5)}\). Note that \(\ell<\varepsilon^2w\) because S_<sub>k</sub>_ is empty when \(2^k\ge\varepsilon^2w\). We separately prove each of the two required hypotheses.

**Claim.** _For_ \(\ell=2^{\mathrm{max}(0,k_0-5)}\)_, the number of_ \(\ell^+\)_-flags in x is at least_ \(\varepsilon w\).

_Proof._ For any two dyadic intervals _I_, _J_, either _I\<J_ or \(I\cap J=\emptyset\). Thus, \(\{\mathsf{pred}(I)|I\in\mathcal{S}'_{\ge k}\}\) is a collection of pairwise-disjoint intervals with total length at least 0.01_w_. By the previous claim, the number of \(\ell^+\)-flags in one of these intervals pred(_I_) is at least 0.01|pred(_I_)|=0.01|_I_|, and so in total the number of \(\ell^+\)-flags in _x_ is at least 10<sup>-4</sup>_w_, as desired.

It remains to check that _x_ contains \((0^\ell 1^\ell)^{\varepsilon w/\ell}\).

**Claim.** _For_ \(\ell=2^{\mathrm{max}(0,k_0-5)}\)_, x contains_ \((0^\ell 1^\ell)^{\varepsilon w/\ell}\) _as a subsequence._

_Proof._ Let _k=k_<sub>0</sub>+1. By the maximality of _k_<sub>0</sub>, we have \(\sum_{I\in\mathcal{S}_{\ge k}^\prime}|I|<0.01w\). Let \(\mathcal{S}_{\ge k}\) denote the collection of maximal sparse dyadic intervals of length at least 2_<sup>k</sup>_. Reversing the analysis which led to a lower bound on the total length of \(\mathcal{S}'\), we obtain

\(\sum_{I\in\mathcal{S}_{\ge k}}|I|\le 2\sum_{I\in\mathcal{S}_{\ge k}^\prime}|I|+\varepsilon w\le 0.1w.\)

Since all sparse dyadic intervals of length 2_<sup>k</sup>_ lie inside some element of \(\mathcal{S}_{\ge k}\), we see that in total at most \(0.1\cdot 2^{K-k}\) of the dyadic intervals _I<sub>k,i</sub>_ are sparse.

On the other hand, at most \(0.7\cdot 2^{K-k}\) of them have density greater than 0.99, since otherwise these very dense intervals alone account for at least 0.68_w_ ones, making the entire interval \[_w_\] 0.1-imbalanced, which is a contradiction. In sum, out of 2<sup>_K-k_</sup> total intervals _I<sub>k,i</sub>_, at most \(0.1\cdot 2^{K-k}\) have density less than 0.01, and at most \(0.7\cdot 2^{K-k}\) have density greater than 0.99, leaving at least \(0.2\cdot 2^{K-k}\) that must each contain \(0.01\cdot 2^k\)<tbc>

