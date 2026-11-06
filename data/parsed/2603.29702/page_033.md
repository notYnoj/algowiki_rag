Plugging into (18), we have<tbc>

\(\sum_{k\in[S]}Y_k=O(\left|\widetilde{S}\right|w(p_{s^\prime})S^{0.51}/S^{0.98}).\)

<tbc>With probability 1-_o_(1), \(\left|\widetilde{S}\right|=O(S^{0.02})\), and we have<tbc>

\(\sum_{k\in[S]}Y_k=O(w(p_{s^\prime})/S^{0.45}).\)

<tbc>Recall that \(M=\Theta\left(log^{0.109}(n)\right)\) and \(S=\Theta(log(n)/loglog(n))\), and therefore with probability 1-_o_(1),<tbc>

\(\sum_{k\in[S]}Y_k=O(w(p_{s^\prime})/S^{0.45})=o\left(\frac{w(p_{s^\prime})}{M^2log^{0.02}(n)}\right).\)

<tbc>Thus if we consider the expections over the randomness of \(\widetilde{S}\), with probability 1-_o_(1),

\(\mathbf{E}_\widetilde{S}\left[\sum_{k\in[S]}Y_k\right]=o\left(\frac{\mathbf{E}_\widetilde{S}\left[w(p_{s^\prime})\right]}{M^2log^{0.02}(n)}\right).\) (19)

## Finishing it off

By plugging (19) into (17), with probability 1-_o_(1), we have<tbc>

\(\mathbf{E}_\widetilde{S}\left[\mathcal{X}\right]=o\left(\frac{\mathbf{E}_\widetilde{S}\left[w(p_{s^\prime})\right]}{Mlog^{0.02}(n)}\right).\)

<tbc>Further note that \(w(p_{s^\prime})\le w(p)+\mathcal{X}\) since modifying an edge increases the length of a path by at most 1. Thus we have

\(\mathbf{E}_\widetilde{S}\left[\mathcal{X}\right]=o\left(\frac{w(p)+\mathbf{E}_\widetilde{S}\left[\mathcal{X}\right]}{Mlog^{0.02}(n)}\right).\)

Solving for \(\mathbf{E}_\widetilde{S}\left[\mathcal{X}\right]\), we get \(\mathbf{E}_\widetilde{S}\left[\mathcal{X}\right]=o\left(\frac{w(p)}{Mlog^{0.02}(n)}\right)\). The lemma follows from Markov’s Inequality.

In Section 6.2, we will present how we can approximate the length of \(\widehat{p}\) with a small multiplicative error with probability at least 3/4:

**Lemma 6.6.** _Let_ \(\widetilde{S}\subset[S]\) _be such that each scale is chosen u.a.r. with probability_ 1_/S_<sup>0.98</sup>_. Let_ \(\widehat{p}\) _be the short est_ \(\widetilde{S}\)_-regular_ \(\langle 0,n_X\rangle\)-\(\langle n_X+n_Y,n_Y\rangle\) _path. With probability at least_ 3/4_, we can_ \((1\pm o(1))\)_-approximate_ \(w(\widehat{p})\) _in o(n_<sup>0.09</sup>) _time by querying only_ \(\frac{n^2\phi_y^2}{\mathcal{B}_x^2}/2^{\Omega\left(log^{0.01}(n)\right)}\) _edge weights._

Assuming Lemma 6.6, we now show how to finish the rest of the proof for Lemma 5.12.

**Lemma 5.12** (Restated)**.** _Suppose that for every edge from_ \(\langle x,y\rangle\) _to_ \(\langle x+\mathcal{B}_x,y'\rangle\)_, we are given ("for free") a constant-factor approximation_ \(\mathrm{approrew}[x,y,x+\mathcal{B}_x,y']\) _of the edge weight_ \(\mathrm{ew}[x,y,x+\mathcal{B}_x,y']\) _(i.e.,_ \(\mathrm{ew}[x,y,x+\mathcal{B}_x,y']\le\mathrm{approrew}[x,y,x+\mathcal{B}_x,y']\le 4\mathrm{ew}[x,y,x+\mathcal{B}_x,y']\)_). To know the exact edge weight requires an edge-weight query. Then we can approximate the problem in Definition 5.6 in o(n_<sup>0.1</sup>) _time with high prob ability using_ \(\frac{n^2\phi_y^2}{\mathcal{B}_x^2}/2^{\Omega\left(log^{0.01}(n)\right)}\) _edge-weight queries, up to a multiplicative factor of_ (1+_o_(1))_, assuming that the answer is at least n/_2<sup>_o_(log<sup>0.009</sup>(_n_)</sup>)</sup>.

