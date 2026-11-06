_Proof._ Let \(\widetilde{S}\subset[S]\) be such that each scale is chosen u.a.r. with probability 1_/S_<sup>0.98</sup>. Let _p_ be the short est \(\langle 0,n_X\rangle\)-\(\langle n_X+n_Y,n_Y\rangle\) path with _w(p_)=_n/_2<sup>_o_\(\big(\)log<sup>0.01</sup>(_n_)\(\big)\)</sup>. Let \(\widehat{p}\) be the shortest \(\widetilde{S}\)-regular \(\langle 0,n_X\rangle\)- \(\langle n_X+n_Y,n_Y\rangle\) path.

From Lemma 6.3, with probability at least 19/20, we have

\(w(\widehat{p})>(1+o(1))w(p).\)

From Lemma 6.6, with probability at least 3/4, we can obtain \((1\pm o(1))\)-approximate \(w(\widehat{p})\) by querying only \(\frac{n^2\phi_y}{\mathcal{B}_x^2}/2^{\Omega\big(\mathrm{log}^{0.01}(n)\big)}\) edge weights. By scaling up the answer by (1+_o_(1)) this becomes a (1+_o_(1))- approximation.

By the union bound, with probability at least 7/10, we can (1+_o_(1))-approximate _w(p_) in _o(n_<sup>0.09</sup>) time by querying only \(\frac{n^2\phi_y^2}{\mathcal{B}_x^2}/2^{\Omega\big(\mathrm{log}^{0.01}(n)\big)}\) edge weights. By repeating the procedure \(\Theta(\mathrm{log}(n))\) times and taking the median, we can approximate _w(p_) with a multiplicative error of (1+_o_(1)) with high probability in _o(n_<sup>0.09</sup>log(_n_))=_o(n_<sup>0.1</sup>) time by querying only \(\frac{n^2\phi_y^2\mathrm{log}(n)}{\mathcal{B}_x^2}/2^{\Omega\big(\mathrm{log}^{0.01}(n)\big)}=\frac{n^2\phi_y^2}{\mathcal{B}_x^2}/2^{\Omega\big(\mathrm{log}^{0.01}(n)\big)}\) edge weights.

## 6.2 Algorithm Description

Let \(\widetilde{S}\subset[S]\) be such that each scale is chosen u.a.r. with probability 1_/S_<sup>0.98</sup>. Our goal now is to approximate the length of the shortest \(\widetilde{S}\)-regular \(\langle 0,n_X\rangle\)-\(\langle n_X+n_Y,n_Y\rangle\) path \(\widehat{p}\):

**Lemma 6.6** (Restated)**.** _Let_ \(\widetilde{S}\subset[S]\) _be such that each scale is chosen u.a.r. with probability_ 1_/S_<sup>0.98</sup>_. Let_ \(\widehat{p}\) _be the shortest_ \(\widetilde{S}\)_-regular_ \(\langle 0,n_X\rangle\)_-_\(\langle n_X+n_Y,n_Y\rangle\) _path. With probability at least_ 3/4_, we can_ \((1\pm o(1))\)_- approximate_ \(w(\widehat{p})\) _in o(n_<sup>0.09</sup>) _time by querying only_ \(\frac{n^2\phi_y^2}{\mathcal{B}_x^2}/2^{\Omega\big(\mathrm{log}^{0.01}(n)\big)}\) _edge weights._

We can design an _M_-way _S_-scale divide-and-conquer scheme to compute \(\widehat{\mathrm{ans}}[l,y_l,r,y_r]\) which is the length of the shortest \(\widetilde{S}\)-regular \(\langle l,y_l\rangle\)-\(\langle r,y_r\rangle\) path where (_l,r_\] is a scale-_s_ interval.

• If _s_=0, we obtain \(\widehat{\mathrm{ans}}[l,y_l,r,y_r]\) using an edge weight query;<tbc>

• Suppose that _s\>_0 and \(s\notin\widetilde{S}\). Recall that the _i_-th anchor is \(m_i:=l+i\cdot\frac{r-l}{M}\) . We find \(\widehat{\mathrm{ans}}[l,y_l,r,y_r]\) by minimizing over every anchor path defined by the sequence \(\widehat{Y}=(y_l=\widehat{y}_0,\widehat{y}_1,\dots,\widehat{y}_M=y_r)\), where for \(1\le i\le M\), \(|\widehat{y}_i-\widehat{y}_{i-1}|\le\frac{r-l}{M}\) , visiting valid vertices \((\langle m_i,\widehat{y}_i\rangle)_i\) in the sparsified grid graph. We use \(\unknown\) to denote the set of possible anchor paths \(\widehat{Y}\).<tbc>

• Suppose \(s\in\widetilde{S}\). Recall that we regularize the row after column _m<sub>i</sub>_ to \(\overline{y_i}:=(I_{s-1}/\phi_y)\cdot\left\lfloor\frac{y_l+i\frac{y_r-y_l}{M}}{I_{s-1}/\phi_y}\right\rfloor\). \(\widehat{\mathrm{ans}}[l,y_l,r,y_r]\) is simply the sum of \(\widehat{\mathrm{ans}}[m_{i-1},\overline{y_i},m_i,\overline{y_i}]\) over \(1\le i\le M\).

The full recursion is as follows:

\(\widehat{\mathrm{ans}}[l,y_l,r,y_r]:=\left\{\begin{array}{ c c }
\mathrm{ew}[l,y_l,r,y_r], & \text{if}s=0 \\
\mathrm{min}_{\widehat{Y}\in\unknown}\sum_{i=1}^M\widehat{\mathrm{ans}}[m_{i-1},\widehat{y}_{i-1},m_i,\widehat{y}_i], & \text{if}s\notin\widetilde{S} \\
\sum_{i=1}^M\widehat{\mathrm{ans}}[m_{i-1},\overline{y_i},m_i,\overline{y_i}], & \text{if}s\in\widetilde{S}
\end{array}\right..\) (20)

Unfortunately, this scheme still queries too many edge weights.

