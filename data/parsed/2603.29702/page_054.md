Assuming Lemma 7.7, we now show how to finish the rest of the proof for Lemma 5.10.

**Lemma 5.10** (Restated)**.** _Suppose that to know the exact edge weight of any edge from any_ \(\langle x,y\rangle\) _to any_ \(\langle x+\mathcal{B}_x,y'\rangle\) _requires an edge-weight query. We can approximate the problem in Definition 5.7 in o(n_<sup>0.1</sup>) _time with high probability_<sup>26</sup> _using_ \(\frac{n^2\phi_y^2}{\mathcal{B}_x^2}/2^{\Omega\big(\mathrm{log}^{0.01(n)}\big)}\) _edge-weight queries, up to a multiplicative factor of_ (1-_o_(1))_, assuming that the answer is at least n/_2<sup>_o_(log<sup>0.009</sup>(_n_)</sup>)</sup>.

_Proof._ Let \(\widetilde{S}\subset[S]\) be such that each scale that is a multiple of 3 is chosen u.a.r. with probability 1_/S_<sup>0.98</sup>. Let _p_ be the longest \(\langle 0,n_X\rangle\)-\(\langle n_X+n_Y,n_Y\rangle\) path. Let \(\widehat{p}\) be the longest \(\widetilde{S}\)-regular \(\langle 0,n_X\rangle\)-\(\langle n_X+n_Y,n_Y\rangle\) path with \(w(\widehat{p})=n/2^{o\big(\mathrm{log}^{0.01(n)}\big)}\).

From Lemma 7.3, with probability at least 19/20, we have

\(w(\widehat{p})=(1-o(1))w(p).\)

From Lemma 7.7, with probability at least 3/4, we can obtain \((1\pm o(1))\)-approximate \(w(\widehat{p})\) by querying only \(\frac{n^2\phi_y}{\mathcal{B}_x^2}/2^{\Omega\big(\mathrm{log}^{0.01(n)}\big)}\) edge weights.

By the union bound, with probability at least 7/10, we can \((1\pm o(1))\)-approximate _w(p_) in _o(n_<sup>0.09</sup>) time by querying only \(\frac{n^2\phi_y^2}{\mathcal{B}_x^2}/2^{\Omega\big(\mathrm{log}^{0.01(n)}\big)}\) edge weights. By scaling down the answer by (1-_o_(1)) this becomes a (1-_o_(1))-approximation. By repeating the procedure \(\Theta(\mathrm{log}(n))\) times and taking the median, we can approximate _w(p_) with a multiplicative error of (1-_o_(1)) with high probability in \(o\left(n^{0.09}\mathrm{log}(n)\right)=o(n^{0.1})\) time by querying only \(\frac{n^2\phi_y^2\mathrm{log}(n)}{\mathcal{B}_x^2}/2^{\Omega\big(\mathrm{log}^{0.01(n)}\big)}=\frac{n^2\phi_y^2}{\mathcal{B}_x^2}/2^{\Omega\big(\mathrm{log}^{0.01(n)}\big)}\) edge weights.

## 7.2 Algorithm Description

Let \(\widetilde{S}\subset[S]\) be such that each scale that is a multiple of 3 is chosen u.a.r. with probability 1_/S_<sup>0.98</sup>. Our goal now is to approximate the length of the longest \(\widetilde{S}\)-regular \(\langle 0,n_X\rangle\)-\(\langle n_X+n_Y,n_Y\rangle\) path \(\widehat{p}\):

**Lemma 7.7** (Restated)**.** _Let_ \(\widetilde{S}\subset[S]\) _be such that each scale that is a multiple of_ 3 _is chosen u.a.r. with prob ability_ 1_/S_<sup>0.98</sup>_. Let_ \(\widehat{p}\) _be the longest_ \(\widetilde{S}\)_-regular_ \(\langle 0,n_X\rangle\)-\(\langle n_X+n_Y,n_Y\rangle\) _path with_ \(w(\widehat{p})=n/2^{o\big(\mathrm{log}^{0.01(n)}\big)}\)_. With probability at least_ 3/4_, we can_ \((1\pm o(1))\)_-approximate_ \(w(\widehat{p})\) _in o(n_<sup>0.09</sup>) _time by querying only_ \(\frac{n^2\phi_y^2}{\mathcal{B}_x^2}/2^{\Omega\big(\mathrm{log}^{0.01(n)}\big)}\) _edge weights._

We can design an _M_-way _S_-scale divide-and-conquer scheme to compute \(\widehat{\mathrm{ans}}[l,y_l,r,y_r]\) which is the length of the longest \(\widetilde{S}\)-regular \(\langle l,y_l\rangle\)-\(\langle r,y_r\rangle\) path where (_l,r_\] is a scale-_s_ interval.

• If _s_=0, we obtain \(\widehat{\mathrm{ans}}[l,y_l,r,y_r]\) using an edge weight query;<tbc>

• Suppose that _s\>_0 and \(s\notin\widetilde{S}\). We find \(\widehat{\mathrm{ans}}[l,y_l,r,y_r]\) by maximizing over every anchor path defined by the sequence \(\widehat{Y}=(y_l=\widehat{y}_0,\widehat{y}_1,\dots,\widehat{y}_M=y_r)\) where for \(1\le i\le M\), \(|\widehat{y}_i-\widehat{y}_{i-1}|\le\frac{r-l}{M}\) , visiting valid vertices \((\langle m_i,\widehat{y}_i\rangle)_i\) in the sparsified grid graph. We use \(\includegraphics{}\) to denote the set of possible anchor paths \(\widehat{Y}\).<tbc>

• Suppose \(s\in\widetilde{S}\). Recall that we regularize the row at column _m<sub>i</sub>_ to \(\overline{y_i}:=(I_{s-1}/\phi_y)\cdot\left[\frac{y_l+i\cdot\frac{y_{r-y_l}}{M}}{I_{s-1}/\phi_y}\right]\). \(\widehat{\mathrm{ans}}[l,y_l,r,y_r]\) is simply the sum of \(\widehat{\mathrm{ans}}[m_{i-1},\overline{y_i},m_i,\overline{y_i}]\) over \(1\le i\le M\).<tbc>

<sup>26</sup>i.e., a probability of 1-1_/n<sup>c</sup>_ for some constant _c\>_0.

