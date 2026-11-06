**Definition 6.2** (\(\widetilde{S}\)-regular paths)**.** Given \(\widetilde{S}\subset[S]\), a path \(\widehat{p}\) is \(\widetilde{S}\)_-regular_ if for every \(s\in\widetilde{S}\) and every scale-_s_ interval (_l,r_\], for every \(0\le i\le M\), we have

\(\widehat{p}(m_i)=(I_{s-1}/\phi_y)\cdot\left\lfloor\frac{\widehat{p}(l)+i\cdot\frac{\widehat{p}(r)-\widehat{p}(l)}{M}}{I_{s-1}/\phi_y}\right\rfloor=:\overline{y_i}.\)

In other words, inside every active scale interval, an \(\widetilde{S}\)-regular path is the straight line rounded to nearest multiples of \(I_{s-1}/\phi_y\) (rounding is necessary due to the way the sparsified grid is defined).

For a column _x_, we use the shorthand "the weight of _p_ before column _x_" to denote the weight of the edge from \(\langle x-1,p(x-1)\rangle\) to \(\langle x,p(x)\rangle\). We show that if \(\widetilde{S}\subset[S]\) is such that each scale is chosen u.a.r. with probability 1_/S_<sup>0.98</sup> (thus of size \(\Theta(S^{0.02})\) with probability 1-_o_(1)), then enforcing \(\widetilde{S}\)-regularity does not increase the answer too much:

**Lemma 6.3** (Best regular path approximates best path)**.** _Let_ \(\widetilde{S}\subset[S]\) _be such that each scale is chosen u.a.r. with probability_ 1_/S_<sup>0.98</sup>_. Let p be the shortest_ \(\langle 0,n_X\rangle\)-\(\langle n_X+n_Y,n_Y\rangle\) _path with w(p_)=_n/_2<sup>_o_(log<sup>0.01</sup>(_n_))</sup>_. With probability at least_ 19/20_, we can round p to an_ \(\widetilde{S}\)_-regular_ \(\langle 0,n_X\rangle\)-\(\langle n_X+n_Y,n_Y\rangle\) _path_ \(\widehat{p}\) _such that_

\(w(\widehat{p})=\left(1+o\left(\frac{1}{Mlog^{0.02}(n)}\right)\right)w(p).\)

_Moreover, there are at most_ \(o\left(\frac{w(p)}{Mlog^{0.02}(n)}\right)\) _columns before which the weights of p and_ \(\widehat{p}\) _differ._

Towards proving Lemma 6.3, we first show that if the sum of total deviation is indeed small on some scale, then straight-line regularization on that scale does not incur too much error. For a path _p_ from \(\langle l,y_l\rangle\) to \(\langle r,y_r\rangle\), we let the forward difference operator \(\Delta p\) be the sequence

\(\Delta p:=(p(l+\mathcal{B}_x)-p(l),p(l+2\mathcal{B}_x)-p(l+\mathcal{B}_x),\dots,p(r)-p(r-\mathcal{B}_x)).\)

We show the following claim:

**Claim 6.4** (Regularizing on a single scale)**.** _Let_ \(s\in[S]\) _be some scale. Let p<sub>s</sub> be a_ \(\langle 0,n_X\rangle\)-\(\langle n_X+n_Y,n_Y\rangle\) _path. We can round p<sub>s</sub> to an_ {_s}-regular path p_<sub>_s_-1</sub>_. Specifically, for every scale-s interval_ (_l,r_\]_, we use Lemma 5.9 to adjust p<sub>s</sub>(m<sub>i</sub>_) _to_ \(p_{s-1}(m_i):=(I_{s-1}/\phi_y)\cdot\left\lfloor\frac{p_s(l)+i\cdot\frac{p_s(r)-p_s(l)}{M}}{I_{s-1}/\phi_y}\right\rfloor\).

_We have_

\(w(p_{s-1})\le w(p_s)+O(M\unknown\mathrm{TD}_{M,\{s\}}(\Delta p_s)).\)

_Moreover, there are at most_ \(O(M\unknown\mathrm{TD}_{M,\{s\}}(\Delta p_s))\) _columns where the weights of p<sub>s</sub> and p_<sub>_s_-1</sub> _differ._

_Proof._ It suffices to show that for every scale-_s_ interval (_l,r_\], rounding inside (_l,r_\] affects \(O(M\mathrm{TD}_M(\Delta p_s(l,r]))\)<sup>23</sup> weights. Due to Lemma 5.9, it suffices to show that

\(\sum_{1\le i<M}\left|p_s(m_i)-(I_{s-1}/\phi_y)\cdot\left\lfloor\frac{p_s(l)+i\cdot\frac{p_s(r)-p_s(l)}{M}}{I_{s-1}/\phi_y}\right\rceil\right|=O(M\mathrm{TD}_M(\Delta p_s(l,r])),\) (10)

<sup>23</sup>As a reminder, this is the notation for the total deviation (not tree total deviation).

