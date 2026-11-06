**Lemma 7.7** (Restated)**.** _Let_ \(\widetilde{S}\subset[S]\) _be such that each scale that is a multiple of_ 3 _is chosen u.a.r. with prob ability_ 1_/S_<sup>0.98</sup>_. Let_ \(\widehat{p}\) _be the longest_ \(\widetilde{S}\)_-regular_ \(\langle 0,n_X\rangle\)_-_\(\langle n_X+n_Y,n_Y\rangle\) _path with_ \(w(\widehat{p})=n/2^{\left(\mathrm{log}^{0.01}(n)\right)}\)_. With probability at least_ 3/4_, we can_ \((1\pm o(1))\)_-approximate_ \(w(\widehat{p})\) _in o(n_<sup>0.09</sup>) _time by querying only_ \(\frac{n^2\phi_y^2}{\mathcal{B}_x^2}/2^{\Omega\left(\mathrm{log}^{0.01}(n)\right)}\) _edge weights._

The analysis of our algorithm proof consists of three parts:

**Lemma 7.10** (Our estimate is complete)**.** _Let_ \(\widehat{p}\) _be the longest_ \(\widetilde{S}\)_-regular_ \(\langle 0,n_X\rangle\)_-_\(\langle n_X+n_Y,n_Y\rangle\) _path. With probability at least_ 19/25, est\[0_,n<sub>X</sub>,n<sub>X</sub>+n<sub>Y</sub>,n<sub>Y</sub>\]_\>_(1-_o_(1))_w_(\(\widehat{p}\)).

**Lemma 7.11** (Our estimate is sound)**.** _Let_ \(\widehat{p}\) _be the longest_ \(\widetilde{S}\)_-regular_ \(\langle 0,n_X\rangle\)_-_\(\langle n_X+n_Y,n_Y\rangle\) _path. Suppose_ \(w(\widehat{p})=n/2^{\left(\mathrm{log}^{0.01}(n)\right)}\)_. With probability_ 1-_o_(1), est\[0_,n<sub>X</sub>,n<sub>X</sub>+n<sub>Y</sub>,n<sub>Y</sub>\]_\<_(1+_o_(1))_w_(\(\widehat{p}\));

**Lemma 7.12** (Our estimates can be computed efficiently)**.** _With probability_ 1-_o_(1)_, to compute_ est\[0_,n<sub>X</sub>,n<sub>X</sub>+n<sub>Y</sub>,n<sub>Y</sub>\]_, the running time is at most o(n_<sup>0.09</sup>)_, and the total number of edge weight queries is at most_ \(\frac{n^2\phi_y^2}{\mathcal{B}_x^2}/2^{\Omega\left(\mathrm{log}^{0.01}(n)\right)}\).

By union bound, we can see that our algorithm is both correct and efficient with probability at least 3/4, thereby proving Lemma 7.7.

## 7.3.2 Our Estimate Is Complete

We first show that our algorithm is complete. Recall that our sub-routine for obtaining the estimate has an error that is contingent on there being no outliers (Claim 7.8). To show that outliers are rare on average, we will use the following ingredient, which shows that the deviation of the weight distribution of \(\widehat{p}\) is small on active layers:

**Claim 7.13** (The deviation of the weight distribution of \(\widehat{p}\) is small on active layers)**.** _Assume that the length of the longest_ \(\langle 0,n_X\rangle\)_-_\(\langle n_X+n_Y,n_Y\rangle\) _path is at least n/_2<sup>_o_(log<sup>0.02</sup>(_n_))</sup>_. Let_ \(\widetilde{S}\subset[S]\) _be such that each scale that is a multiple of_ 3 _is chosen u.a.r. with probability_ 1_/S_<sup>0.98</sup>_. Let the longest_ \(\widetilde{S}\)_-regular_ \(\langle 0,n_X\rangle\)_-_\(\langle n_X+n_Y,n_Y\rangle\) _path be_ \(\widehat{p}\) _with_ \(w(\widehat{p})=\Omega(w(p))\)_. Recall that_ \(W(\widehat{p})\) _is the sequence of length n/_B_<sub>x</sub> whose i-th entry is:_

\(W(\widehat{p})_i:=w(\widehat{p}(i\mathcal{B}_x,(i+1)\mathcal{B}_x]),\) (32)

_which captures the "weight distribution" of_ \(\widehat{p}\).

_With probability at least_ 4/5_, we have_ \(\includegraphics{}\mathrm{TD}_{M,\widetilde{S}}(W(\widehat{p}))=o\left(\frac{w(\widehat{p})}{M}\right)\).

Before proving the ingredient above, we first give our main analysis that our estimate is complete:

**Lemma 7.10** (Restated)**.** _Let_ \(\widehat{p}\) _be the longest_ \(\widetilde{S}\)_-regular_ \(\langle 0,n_X\rangle\)_-_\(\langle n_X+n_Y,n_Y\rangle\) _path. With probability at least_ 19/25, est\[0_,n<sub>X</sub>,n<sub>X</sub>+n<sub>Y</sub>,n<sub>Y</sub>\]_\>_(1-_o_(1))_w_(\(\widehat{p}\)).

_Proof._ For each active scale _s_, we consider the following question: how much would we underestimate if there were no subsampling on active scales larger than _s_? We can see that the final estimate is at least:<tbc>

\(\mathcal{P}_s:=\sum_{i=1}^{n/I_s}\mathrm{est}[(i-1)\cdot I_s,\widehat{p}((i-1)\cdot I_s),i\cdot I_s,\widehat{p}(i\cdot I_s)].\)

