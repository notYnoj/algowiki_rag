**Lemma 9.** _Suppose that_ \(min_{x\in\mathcal{F}}\|x-\widehat{x}\|\le\varepsilon\)_. Then with probability_ \(1-\beta\), \(x'\) _satisfies_<tbc>

\(\sum_{j=1}^k\left(\sum_{i=1}^nx'_{i,j}-b_j\right)_+\le\sqrt{3klog(k/\beta)\widehat{V}}+\sqrt{nk}\varepsilon\)

<tbc>_Proof._ Based on the relation between \(\ell_1\) and \(\ell_2\) norm, we have<tbc>

\(min_{x\in\mathcal{F}}\|x-\widehat{x}\|_1\le\sqrt{nk}min_{x\in\mathcal{F}}\|x-\widehat{x}\|\le\sqrt{nk}\varepsilon\)

<tbc>This means<tbc>

\(\sum_{j=1}^k\left(\sum_{i=1}^n\widehat{x}_{i,j}-b_j\right)_+\le\sqrt{nk}\varepsilon\)

<tbc>Note that for each good _j_ and any \(\delta\in(0,1)\), we have from Chernoff-Hoeffding bound that<tbc>

\(Pr\left[\sum_{i=1}^nx'_{i,j}>(1+\delta)\sum_{i=1}^n\widehat{x}_{i,j}\right]<exp\left(-\delta^2n/3\right).\)

<tbc>Let \(X_j=\sum_{i=1}^n\widehat{x}_{i,j}\). If we set \(\beta/k=exp\left(-\delta^2n/3\right)\), then by union bound we have the following except with probability \(\beta\)<tbc>

\(\text{for all}j\in[k],\sum_{i=1}^nx'_{i,j}\le\left(1+\sqrt{3log(k/\beta)/X_j}\right)X_j\)

<tbc>Also, \(v(\widehat{x})=\|\widehat{x}\|_1\) because for any (_i,j_) such that _v<sub>i,j</sub>_=0, we must have \(\widehat{x}_{i,j}=0\), otherwise the player _i_ could increase the regularized objective value by having \(\widehat{x}_{i,j}=0\) in Equation (1). It follows that

\(\sum_{j=1}^k\left(\sum_{i=1}^nx'_{i,j}-X_j\right)\le\sum_{j=1}^k\sqrt{3log(k/\beta)X_j}\le\sqrt{3klog(k/\beta)\|\widehat{x}\|_1}=\sqrt{3klog(k/\beta)\widehat{V}}\)

Therefore,

\(\sum_{j=1}^k\left(\sum_{i=1}^nx'_{i,j}-b_j\right)_+\le\sqrt{nk}\varepsilon+\sqrt{3klog(k/\beta)\widehat{V}},\)

which recovers the stated bound.

**Theorem 4.** _There exists a coordination protocol with coordination complexity O(k_log(_nk_)) _such that the parties coordinate on a matching_ \(x'\) _with total weight:_

\(\sum_{j=1}^kmin\left\{\sum_{i=1}^nv_{i,j}x'_{i,j},b_j\right\}\ge\left(1-O\left(\frac{\sqrt{klog(k/\beta)}}{\sqrt{OPT}}\right)\right)OPT\)

_as long as_ \(OPT\ge 1\).

