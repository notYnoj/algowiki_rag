\(2^{\mathrm{min}\{\ell,r\}}\ge 2^{\mathrm{min}\{\ell_h,r_h\}}\ge\frac{M_{ij}}{16m}.\) (2)

Consider the number of nodes in L surviving the subsampling, i.e., \(Z:=|\mathcal{L}\cap\widetilde{U}_{ij}|\). If _Z\>_0, then some node in L survived, and thus by (2) the computed value \(\widetilde{L}_{ij}\) is at least \(\frac{M_{ij}}{16m}\) . It thus remains to analyze Pr\[_Z\>_0\].

In case some \((\sigma,\ell,r)\in\mathcal{L}\) has \(p_{\ell,r}=1\), we have _Z\>_0 with probability 1. Otherwise all \((\sigma,\ell,r)\in\mathcal{L}\) have \(p_{\ell,r}<1\) and thus \(p_{\ell,r}=2^{\ell+r+3}/q\). In this case, we write _Z_ as a sum of independent Bernoulli random variates in the form \(Z=\sum_{(\sigma,\ell,r)\in\mathcal{L}}\mathrm{Ber}(p_{\ell,r})\). In particular,<tbc>

\(\mathbb{E}[Z]=\sum_{(\sigma,\ell,r)\in\mathcal{L}}2^{\ell+r+3}/q\ge^{(1)}\frac{4\overline{M_{ij}}}{q}\ge\frac{M_{ij}}{q}.\)

<tbc>Since _Z_ is a sum of independent {0,1}-variables, multiplicative Chernoff applies and yields \(\mathrm{Pr}[Z<\mathbb{E}[Z]/2]\le\mathrm{exp}(-\mathbb{E}[Z]/8)\). We thus obtain

\(\mathrm{Pr}[Z>0]\ge 1-\mathrm{Pr}\big[Z<\mathbb{E}[Z]/2\big]\ge 1-\mathrm{exp}\big(-\mathbb{E}[Z]/8\big)\ge 1-\mathrm{exp}\big(-\frac{M_{ij}}{8q}\big).\)

In case \(M_{ij}\ge q\), we obtain \(\mathrm{Pr}[Z>0]\ge 1-\mathrm{exp}(-1/8)\ge 0.1\), and thus we have \(\widetilde{L}_{ij}\ge\frac{M_{ij}}{16m}\) with probability at least 0.1. Otherwise, in case _M<sub>ij</sub>\<q_, we can only use the trivial bound \(\widetilde{L}_{ij}\ge 0>\frac{M_{ij}-q}{16m}\) . In any case, we have \(\widetilde{L}_{ij}\ge\frac{M_{ij}-q}{16m}\) with probability at least 0.1. Similar to the proof of Lemma 6, we run _O_(log_n_) independent repetitions of this algorithm and return for each _i,j_ the maximum of all computed values \(\widetilde{L}_{ij}\), to boost the success probability and finish the proof.

## 5 Main Algorithm

In this section we prove Theorem 1. First we show that Theorem 9 implies Theorem 1, and then in the remainder of this section we prove Theorem 9.

**Theorem 9** (Main Result, Relaxation)**.** _Given strings x,y of length n and a time budget_ \(T\in[n,n^2]\)_, in expected time_ \(\widetilde{O}(T)\) _we can compute a number_ \(\widetilde{L}\) _such that_ \(\widetilde{L}\le L:=L(x,y)\) _and w.h.p._ \(\widetilde{L}\ge\widetilde{\Omega}(LT^{0.4}/n^{0.8})\).

Recall Theorem 1:

**Theorem 1.** _There is a randomized algorithm that, given strings x,y of length_ \(n\ge 1\) _and a time budget_ \(T\in[n,n^2]\)_, with high probability computes a multiplicative_ \(\widetilde{O}(n^{0.8}/T^{0.4})\)_-approximation of the length of the LCS of x and y in time O(T)._

_Proof of Theorem 1 assuming Theorem 9._ Note that the difference between Theorems 1 and 9 is that the latter allows _expected_ running time and has an additional slack of logarithmic factors in the running time.

In order to remove the _expected_ running time, we abort the algorithm from Theorem 9 after \(\widetilde{O}(T)\) time steps. By Markov’s inequality, we can choose the hidden constants and logfactors such that the probability of aborting is at most 1/2. We boost the success probability of this adapted algorithm by running _O_(log_n_) independent repetitions and returning the maximum over all computed values \(\widetilde{L}\). This yields an \(\widetilde{O}(n^{0.8}/T^{0.4})\)- approximation with high probability in time \(\widetilde{O}(T)\).

To remove the logfactors in the running time, as the first step in our algorithm we subsample the given strings _x,y_, keeping each symbol independently with probability _p_=1/polylog(_n_), resulting in subsampled strings \(\tilde{x},\tilde{y}\). Since any common subsequence of \(\tilde{x},\tilde{y}\) is also a common subsequence of _x,y_, the estimate \(\widetilde{L}\) that we compute for \(\tilde{x},\tilde{y}\) satisfies \(\widetilde{L}\le L(\tilde{x},\tilde{y})\le L(x,y)\). Moreover, if \(L(x,y)\ge\mathrm{polylog}(n)\) then by Chernoff bound with high probability we have \(L(\tilde{x},\tilde{y})=\widetilde{\Omega}(L(x,y))\), so that an \(\widetilde{O}(n^{0.8}/T^{0.4})\)-approximation on \(\tilde{x},\tilde{y}\) also yields an \(\widetilde{O}(n^{0.8}/T^{0.4})\)-approximation on _x,y_. Otherwise, if \(L(x,y)\le\mathrm{polylog}(n)\), then in order to<tbc>

