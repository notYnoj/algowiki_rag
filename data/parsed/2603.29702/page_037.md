To obtain \(\mathrm{min}_{\widehat{Y}\in\text{\unknown}}\sum_{i=1}^M\mathrm{est}[m_{i-1},\widehat{y}_{i-1},m_i,\widehat{y}_i]\) (or \(\mathrm{min}_{\widehat{Y}\in\text{\unknown}}\sum_{i=1}^M\mathrm{appr}[m_{i-1},\widehat{y}_{i-1},m_i,\widehat{y}_i]\))), we can simply find the shortest \(\langle l,y_l\rangle\)-\(\langle r,y_r\rangle\) path.

We give the full pseudocode for computing est in Algorithm 1. We use the memoization technique to compute est values on demand (i.e., Line 12-13 and Line 22-23).

## 6.3 Algorithm Analysis

### 6.3.1 Overview

Our goal is to use our algorithm to prove Lemma 6.6:

**Lemma 6.6** (Restated)**.** _Let_ \(\widetilde{S}\subset[S]\) _be such that each scale is chosen u.a.r. with probability_ 1_/S_<sup>0.98</sup>_. Let_ \(\widehat{p}\) _be the shortest_ \(\widetilde{S}\)_-regular_ \(\langle 0,n_X\rangle\)_-_\(\langle n_X+n_Y,n_Y\rangle\) _path. With probability at least_ 3/4_, we can_ \((1\pm o(1))\)_- approximate_ \(w(\widehat{p})\) _in o(n_<sup>0.09</sup>) _time by querying only_ \(\frac{n^2\phi_y^2}{\mathcal{B}_x^2}/2^{\Omega\left(\mathrm{log}^{0.01}(n)\right)}\) _edge weights._

The analysis of our algorithm proof consists of three parts:

**Lemma 6.9** (Our estimate is complete)**.** _Let_ \(\widehat{p}\) _be the shortest_ \(\widetilde{S}\)_-regular_ \(\langle 0,n_X\rangle\)_-_\(\langle n_X+n_Y,n_Y\rangle\) _path. With probability at least_ 19/25, est\[0_,n<sub>X</sub>,n<sub>X</sub>+n<sub>Y</sub>,n<sub>Y</sub>_\]_\<_(1+_o_(1))_w_(\(\widehat{p}\)).

**Lemma 6.10** (Our estimate is sound)**.** _Let_ \(\widehat{p}\) _be the shortest_ \(\widetilde{S}\)_-regular_ \(\langle 0,n_X\rangle\)_-_\(\langle n_X+n_Y,n_Y\rangle\) _path. Suppose_ \(w(\widehat{p})=n/2^{o\left(\mathrm{log}^{0.01}(n)\right)}\)_. With probability_ 1-_o_(1), est\[0_,n<sub>X</sub>,n<sub>X</sub>+n<sub>Y</sub>,n<sub>Y</sub>_\]_\>_(1-_o_(1))_w_(\(\widehat{p}\));

**Lemma 6.11** (Our estimates can be computed efficiently)**.** _Computation of all_ appr _values take o(n_<sup>0.09</sup>) _time. With probability_ 1-_o_(1)_, to compute_ est\[0_,n<sub>X</sub>,n<sub>X</sub>+n<sub>Y</sub>,n<sub>Y</sub>_\]_, the running time is at most o(n_<sup>0.09</sup>)_, and the total number of edge weight queries is at most_ \(\frac{n^2\phi_y^2}{\mathcal{B}_x^2}/2^{\Omega\left(\mathrm{log}^{0.01}(n)\right)}\).

By union bound, we can see that our algorithm is both correct and efficient with probability at least 3/4, thereby proving Lemma 6.6.

### 6.3.2 Our Estimate Is Complete

We first show that our algorithm is complete. Recall that our sub-routine for obtaining the estimate has an error that is contingent on there being no outliers (Claim 6.7). To show that outliers are rare on average, we will use the following ingredient, which shows that the deviation of the weight distribution of \(\widehat{p}\) is small on active layers:

**Claim 6.12** (The deviation of the weight distribution of \(\widehat{p}\) is small on active layers)**.** _Assume that the length of the shortest_ \(\langle 0,n_X\rangle\)_-_\(\langle n_X+n_Y,n_Y\rangle\) _path p is at least n/_2<sup>_o_\(\left(\mathrm{log}^{0.02}(n)\right)\)</sup>_. Let_ \(\widetilde{S}\subset[S]\) _be such that each scale is chosen u.a.r. with probability_ 1_/S_<sup>0.98</sup>_. Let the shortest_ \(\widetilde{S}\)_-regular_ \(\langle 0,n_X\rangle\)_-_\(\langle n_X+n_Y,n_Y\rangle\) _path be_ \(\widehat{p}\)_. With probability at least_ 4/5_, we have_ \(\unknown\mathrm{TD}_{M,\widetilde{S}}(W(\widehat{p}))=o\left(\frac{w(\widehat{p})}{M}\right)\).

Before proving the ingredient above, we first give our main analysis that our estimate is complete:

**Lemma 6.9** (Restated)**.** _Let_ \(\widehat{p}\) _be the shortest_ \(\widetilde{S}\)_-regular_ \(\langle 0,n_X\rangle\)_-_\(\langle n_X+n_Y,n_Y\rangle\) _path. With probability at least_ 19/25, est\[0_,n<sub>X</sub>,n<sub>X</sub>+n<sub>Y</sub>,n<sub>Y</sub>_\]_\<_(1+_o_(1))_w_(\(\widehat{p}\)).

