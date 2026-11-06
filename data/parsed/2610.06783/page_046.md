For a box \(\pi\) with \(e\ge 1\) stars, let \(\ell\) be the highest level at which \(\pi\) has a star. The leaves of \(\pi\) are the leaves of the ten strings \(\pi[\ell\leftarrow\lambda]\) obtained by replacing that star by a term \(\lambda\), and each of these strings is again a box, with _e_-1 stars. Indeed, if \(\lambda=P_0\), then the number of symbols that are _P_<sub>0</sub> or stars stays the same, and the new _P_<sub>0</sub> at level \(\ell\) is above all the remaining stars. If \(\lambda\) is any other term, then that number decreases by one, and every star is still below every _P_<sub>0</sub>. Thus conditions (i) and (ii) in the definition of a box hold in both cases. (We expand the highest star because replacing a lower star by _P_<sub>0</sub> would leave a star above a _P_<sub>0</sub>, which is not a box.) Hence we compute

\(val(\pi)=\sum_\lambda val(\pi[\ell\leftarrow\lambda])\)

with ten lookups in the trie, in _O(L_) operations. Generating the boxes with _e_ stars and inserting them into the trie also takes _O(L_) operations per box, and adds at most _L_ vertices per box.

See Figure 7 for an illustration of these counts (in that figure, the switching order _t_ is set to _m/_9). At every order _d_, the pruned recursion of Section 2.4 visits at most \(min\{|U|\alpha_d,\beta_d\}\) leaves of order _d_ in a tile whose wanted output strings form the set _U_ (see the proof of Lemma 11), the smaller of the two bounds at that order. The data structure cannot do this, since _U_ is not known in advance. Instead, a query computes \(\alpha_d\) products at every order _d\<t_, and looks up \(\alpha_t\) boxes at the order _t_. The data structure also stores at most \((m+1)\sum_{d\ge t}\beta_d\) boxes per tile, even if they are not used by a query. The preprocessing time is therefore dominated by the sum \(\sum_{d\ge t}\beta_d\), and hence by how fast the \(\beta_d\) decay. Let<tbc>

\(\rho:=\frac{9m}{L-m+1},\)

<tbc>which is less than 1 since \(L\ge 10m\). It plays the role of \(\frac{1}{2}\) in (5): for \(1\le d\le m\),

\(\frac{\beta_d}{\beta_{d-1}}=\frac{9(m-d+1)}{L-m+d}\le\frac{9m}{L-m+1}=\rho,\text{so}\beta_d\le\rho^dM.\) (7)

The closer the ratio _c=L/m_ is to 10, the closer \(\rho\) is to 1, and the more boxes the preprocessing has to compute. This is one side of the trade-off mentioned at the beginning of this section between the time savings and how thin the product must be.

We can now bound the costs. The theorem below assumes that \(N\ge\sqrt{K}N_0\). Since a tile spans \(K_0N_0\le\sqrt{K}N_0\) rows and as many columns of the \(N\times N\) product _XY_ , this ensures that a tile fits inside _XY_ , so padding _N_ to a multiple of _K_<sub>0</sub>_N_<sub>0</sub> at most doubles it. We checked the same requirement in Section 2.4.4, where it was the first of the two consequences of \(N\ge D^{18}\). Here it will also follow, in Section 4.4, from the requirement that computing the encodings takes at most \(N^2/D^\gamma\) time, since \(10^L\ge M\).

**Theorem 30.** _Let_ \(m\ge 1\)_, D_=4_<sup>m</sup>,_ \(L\ge 10m\), \(0\le t\le m\)_, and_ \(N\ge\sqrt{K}N_0\)_. Given as input matrices_ \(X\in\mathbb{Z}^{N\times D}\) _and_ \(Y\in\mathbb{Z}^{D\times N}\)_, whose entries are integers of absolute value at most N_<sup>_O_(1)</sup>_, we can preprocess them deterministically in time and space_

\(O\big(Lm\frac{\rho^t}{1-\rho}N^2+\frac{N\cdot 10^L}{\sqrt{K}N_0}\big).\) (8)

_After this, any single entry_ (_XY_)\[_I,J_\] _can be computed deterministically in_ \(O\big(L\sum_{d=0}^t\alpha_d\big)\) _time. In particular, for every set W of positions of an_ \(N\times N\) _matrix, the entries_ \((XY)[I,J]\), \((I,J)\in W\),<tbc>

