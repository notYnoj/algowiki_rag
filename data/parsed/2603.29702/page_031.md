_and_<tbc>

\(\includegraphics{}\text{\textit{T}}_{M,S}(\Delta p')=O(w(p')\cdot S^{0.51}),\) (14)

<tbc>_where_<tbc>

\(\Delta p':=\left(p'(\mathcal{B}_x)-p'(0),p'(2\mathcal{B}_x)-p'(\mathcal{B}_x),\dots,p'(n_X+n_Y)-p'(n_X+n_Y-\mathcal{B}_x)\right).\)

<tbc>_Proof._ The underlying (unsparsified) Rotated Edit Distance Grid Graph ensures that every vertical move between adjacent rows has weight at least 1. Thus, the total vertical deviation over any subinterval (_l,r_\] satisfies:

\(\sum_i\left|(\Delta p')_i\right|\le w(p'),\)

establishing (13).

Recall that _n=n<sub>X</sub>+n<sub>Y</sub>_. From Lemma 4.1, we also have:<tbc>

\(\includegraphics{}\text{T}_{M,S}(\Delta p')=O\left(\left(\sum_i\left|(\Delta p')_i\right|\cdot S^{0.51}\right)+\left(\underbrace{\mathcal{B}_x}_{max\text{absolute value of}\Delta p^\prime}\cdot\underbrace{(n/\mathcal{B}_x)}_{\text{number of entries in}\Delta p^\prime}\cdot\frac{1}{2\mathrm{log}^{0.015}(n)}\right)\right).\)

<tbc>The second term is \(o(w(p'))\) since \(w(p')\ge\frac{n}{2^{o(\mathrm{log}^{0.01}n)}}\). Plugging in (13):

\(\includegraphics{}\text{T}_{M,S}(\Delta p')=O(w(p')\cdot S^{0.51})+o(w(p'))=O(w(p')\cdot S^{0.51}),\)

which gives (14).

We now prove our main regularity lemma:

**Lemma 6.3** (Restated)**.** _Let_ \(\widetilde{S}\subset[S]\) _be such that each scale is chosen u.a.r. with probability_ 1_/S_<sup>0.98</sup>_. Let p be the shortest_ \(\langle 0,n_X\rangle\)-\(\langle n_X+n_Y,n_Y\rangle\) _path with w(p_)=_n/_2<sup>_o_(log<sup>0.01</sup>(_n_))</sup>_. With probability at least_ 19/20_, we can round p to an_ \(\widetilde{S}\)_-regular_ \(\langle 0,n_X\rangle\)-\(\langle n_X+n_Y,n_Y\rangle\) _path_ \(\widehat{p}\) _such that_

\(w(\widehat{p})=\left(1+o\left(\frac{1}{M\mathrm{log}^{0.02}(n)}\right)\right)w(p).\)

_Moreover, there are at most_ \(o\left(\frac{w(p)}{M\mathrm{log}^{0.02}(n)}\right)\) _columns before which the weights of p and_ \(\widehat{p}\) _differ._

_Proof._ We perform rounding on a scale-by-scale basis. Let _p<sub>S</sub>_:=_p_. For each scale \(s\in[S]\) in decreasing order, if \(s\in\widetilde{S}\), we round _p<sub>s</sub>_ in the manner described in Claim 6.4 to obtain _p_<sub>_s_-1</sub>, and if \(s\notin\widetilde{S}\) we simply let _p_<sub>_s_-1</sub>:=_p<sub>s</sub>_. Let the final path be \(\widehat{p}:=p_0\). This affects \(O\left(M\sum_{s\in\widetilde{S}}\includegraphics{}\text{T}_{M,\{s\}}\left(\Delta p_s\right)\right)\) weights.

As a warm-up, suppose that the error is \(O\left(M\sum_{s\in\widetilde{S}}\includegraphics{}\text{T}_{M,\{s\}}\left(\Delta p\right)\right)\) (namely _p_ instead of _p<sub>s</sub>_). This error is equal to \(O(M\includegraphics{}\text{T}_{M,\widetilde{S}}\left(\Delta p\right))\). Since each scale is in \(\widetilde{S}\) u.a.r. with probability 1_/S_<sup>0.98</sup>, we must have \(\mathbf{E}_\widetilde{S}\left[\includegraphics{}\text{T}_{M,\widetilde{S}}\left(\Delta p\right)\right]=\includegraphics{}\text{T}_{M,S}\left(\Delta p\right)/S^{0.98}\). From (14), this means that \(\mathbf{E}_\widetilde{S}\left[M\includegraphics{}\text{T}_{M,\widetilde{S}}\left(\Delta p\right)\right]=O(Mw(p)\cdot S^{0.51})/S^{0.98}\). Since \(M=\Theta\left(\mathrm{log}^{0.109}(n)\right)\) and \(S:=3\cdot\left\lfloor\mathrm{log}_M\left(n^{0.01}\right)\right\rfloor=\Theta(\mathrm{log}(n)/\mathrm{loglog}(n))\), \(\mathbf{E}_\widetilde{S}\left[M\includegraphics{}\text{T}_{M,\widetilde{S}}\left(\Delta p\right)\right]=o\left(\frac{w(p)}{M\mathrm{log}^{0.02}(n)}\right)\), which implies that \(M\includegraphics{}\text{T}_{M,\widetilde{S}}\left(\Delta p\right)=o\left(\frac{w(p)}{M\mathrm{log}^{0.02}(n)}\right)\) with probability at least 19/20 due to Markov’s Inequality.

A technical hurdle for going from _p_ to _p<sub>s</sub>_ is that every _p<sub>s</sub>_ changes in response to scales being added to \(\widetilde{S}\), so we need to be more careful in our analysis.

