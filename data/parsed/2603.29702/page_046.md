**Vertices** We only consider vertices \(\langle x,y\rangle\) such that

• \(\mathcal{B}_x|x\);<tbc>

• Let \(s\in[S]\cup\{0\}\) be the largest scale such that _I<sub>s</sub>|x_. Then \((I_s/\phi_y)|y\).

**Edges** There is an edge from \(\langle x,y\rangle\) to \(\langle x+\mathcal{B}_x,y'\rangle\) such that \(|y'-y|\le\mathcal{B}_x\) with weight \(\mathrm{ew}[x,y,x+\mathcal{B}_x,y']\) equal to the longest \(\langle x,y\rangle\)-\(\langle x+\mathcal{B}_x,y'\rangle\) path in the Rotated LCS Grid Graph.

**Objective** Find the longest path from \(\langle 0,n_X\rangle\) to \(\langle n_X+n_Y,n_Y\rangle\).

**Lemma 5.10** (Restated)**.** _Suppose that to know the exact edge weight of any edge from any_ \(\langle x,y\rangle\) _to any_ \(\langle x+\mathcal{B}_x,y'\rangle\) _requires an edge-weight query. We can approximate the problem in Definition 5.7 in o(n_<sup>0.1</sup>) _time with high probability_<sup>24</sup> _using_ \(\frac{n^2\phi_y^2}{\mathcal{B}_x^2}/2^{\Omega\left(\mathrm{log}^{0.01}(n)\right)}\) _edge-weight queries, up to a multiplicative factor of_ (1-_o_(1))_, assuming that the answer is at least n/_2<sup>_o_(log<sup>0.009</sup>(_n_)</sup>).

## 7.1 Regular Paths

Let \(\widetilde{S}\subset[S]\) be a subset of active scales (other scales are _passive_). We define the notion of \(\widetilde{S}\)-regularity:

**Definition 7.2.** Given \(\widetilde{S}\subset[S]\), a path \(\widehat{p}\) is \(\widetilde{S}\)-regular (or is an \(\widetilde{S}\)-regular path) if for every \(s\in\widetilde{S}\) and every scale-_s_ interval (_l,r_], for every \(0\le i\le M\), we have

\(\widehat{p}(m_i)=(I_{s-1}/\phi_y)\cdot\left\lfloor\frac{\widehat{p}(l)+i\cdot\frac{\widehat{p}(r)-\widehat{p}(l)}{M}}{I_{s-1}/\phi_y}\right\rfloor=:\overline{y_i}.\)

In other words, inside every active scale interval, an \(\widetilde{S}\)-regular path is the straight line rounded to nearest multiples of \(I_{s-1}/\phi_y\) (due to the way the sparsified grid is defined).

We show that if \(\widetilde{S}\subset[S]\cap 3\mathbb{Z}\) is such that each scale that is a multiple of 3 is chosen u.a.r. with probability 1_/S_<sup>0.98</sup> (thus of size \(\Theta(S^{0.02})\) with probability 1-_o_(1)), then enforcing \(\widetilde{S}\)-regularity does not decrease the answer too much:

**Lemma 7.3** (Best regular path approximates best path)**.** _Let_ \(\widetilde{S}\subset[S]\cap 3\mathbb{Z}\) _be such that every scale that is a multiple of_ 3 _is chosen u.a.r. with probability_ 1_/S_<sup>0.98</sup>_. Let p be the longest_ \(\langle 0,n_X\rangle\)_-_\(\langle n_X+n_Y,n_Y\rangle\) _path with w(p_)=_n/_2<sup>\(\left(\mathrm{log}^{0.01}(n)\right)\)</sup>_. With probability at least_ 19/20_, we can round p to an_ \(\widetilde{S}\)_-regular_ \(\langle 0,n_X\rangle\)- \(\langle n_X+n_Y,n_Y\rangle\) _path_ \(\widehat{p}\) _such that_

\(w(\widehat{p})>\left(1-o\left(\frac{1}{M\mathrm{log}^{0.02}(n)}\right)\right)w(p).\)

_Moreover, there are at most_ \(o\left(\frac{w(p)}{M\mathrm{log}^{0.02}(n)}\right)\) _columns before which the weights of p and_ \(\widehat{p}\) _differ._

Before formally proving Lemma 7.3, we first give an overview. Suppose the weight of _p_ before column _x_ is 1. We want to know if we can round _p_ to a \(\widetilde{S}\)-regular path such that the weight before column _x_ still remains 1. We will give an argument via Lemma 4.3 that for recursion intervals (_l,r_] that contain _x_, the curvatures of _p_ inside (_l,r_] are small on average, namely that _p(l,r_] is already "relatively straight," meaning that each _p(m<sub>i</sub>_) should already be close to <o>_y_</o><sub>i</sub>. Because of this, rounding _p(m<sub>i</sub>_) to <o>_y_</o><sub>i</sub> should only affect a<tbc>

<sup>24</sup>i.e., a probability of 1-1_/n<sup>c</sup>_ for some constant _c\>_0.

