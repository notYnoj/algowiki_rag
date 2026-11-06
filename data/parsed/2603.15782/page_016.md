we will approximately solve the maximum \(\mu\)-uniform Q-flow problem (Sec. 6.2). If this flow has a large value then we will use it to output a valid feedback matrix (Sec. 6.3). Otherwise, calling `DirectionalFlowCut`(_u_) for _u_∼N(0_,I<sub>d</sub>_) will give a balanced element cut with a sufficiently high probability (Sec. 6.4).

## 6.1 Generating rectangular cover

The construction will be based on the following lemma.

**Lemma 15.** _Consider the following procedure for parameter_ \(\sigma=\sqrt{6\varepsilon lnn}\):

• _Sample u_∼N(0_,I<sub>d</sub>)._<tbc>

• _For an integer k and operator_ \(\circ\in\{\le,\ge\}\) _define_ \(S_{\circ k}=\{x\in S:\langle x,u\rangle\circ k\sigma\}\).<tbc>

• _Output set of rectangles_ \(\mathcal{Q}=\{S_{\le k}\times S_{\ge k+1}:k\in\mathbb{Z},S_{\le k}\) _and_ \(S_{\ge k+1}\) _are non-empty_}.

_(a) With probability at least_ \(1-\frac{1}{n}\)_, every_ \(\{x,y\}\in\langle\mathcal{Q}\rangle\) _satisfies_ \(\|x-y\|^2\ge\varepsilon\).<tbc>

_(b) With probability at least_ \(1-\frac{1}{n}\), \(|\mathcal{Q}|\le O\left(\frac{\sqrt{lnn}}{\sigma}\right)=O\left(\frac{1}{\sqrt{\varepsilon}}\right)\).

_(c) Every_ \(\{x,y\}\in\genfrac(){pt}{2}{S}{2}\) _with_ \(\|x-y\|^2\ge\Delta\) _satisfies_ \(\mathtt{Pr}\left[\{x,y\}\in\langle\mathcal{Q}\rangle\right]\ge e^{-O((\sigma/\sqrt{\Delta}+1)^2)}\)_. In particu lar, if_ \(\Delta=\Theta(1)\) _and_ \(\sigma=\Omega(1)\) _then this lower bound is_ \(e^{-O(\sigma^2)}=n^{-O(\varepsilon)}\).

_Proof._ For \(x\in\mathbb{R}^d\) write \(h_x=\langle x,u\rangle\). Note that for any distinct \(x,y\in\mathbb{R}^d\), the quantity \(h_x-h_y=\langle x-y,u\rangle\) is normal with zero mean and variance \(\|x-y\|^2\).

**(a)** Consider pair \(\{x,y\}\in\genfrac(){pt}{2}{S}{2}\) with \(r^2=\|x-y\|^2<\varepsilon=\sigma^2/(6lnn)\). If \(\{x,y\}\in\langle\mathcal{Q}\rangle\) then \(|h_x-h_y|\ge\sigma\). Therefore,

\(\mathtt{Pr}\left[\{x,y\}\in\langle\mathcal{Q}\rangle\right]\le\mathtt{Pr}\left[|\mathcal{N}(0,r^2)|\ge\sigma\right]=2\mathtt{Pr}\left[\mathcal{N}(0,1)\ge\sigma/r\right]\le 2e^{-\sigma^2/(2r^2)}\le 2n^{-3}\)

A union bound over at most \(\genfrac(){pt}{2}{n}{2}\) pairs proves the claim.

**(b)** For each \(x\in S\) we have \(\|x\|^2\le r^2=^\text{def}4/c\) by Assumption 1. Therefore,

\(\mathtt{Pr}\left[|h_x|\ge\Theta(\sqrt{lnn})\right]\le\mathtt{Pr}\left[|\mathcal{N}(0,r^2)|\ge\Theta(\sqrt{lnn})\right]\le n^{-2}\)

for an sufficiently large constant in the \(\Theta(\cdot)\) notation. By the union bound, with probability at least \(1-\frac{1}{n}\) we have \(|h_x|\le\Theta(\sqrt{lnn})\) for all \(x\in S\). It remains to notice that \(|\mathcal{Q}|\le O(max_{x\in S}|h_x|/\sigma)\) by construction.

**(c)** Consider \(\{x,y\}\in\genfrac(){pt}{2}{S}{2}\) with \(\|x-y\|^2\ge\Delta\). By construction, if \(|h_x-h_y|\ge 2\sigma\) then \(\{x,y\}\in\langle\mathcal{Q}\rangle\). Therefore,

\(\mathtt{Pr}\left[\{x,y\}\in\langle\mathcal{Q}\rangle\right]\ge\mathtt{Pr}\left[|\mathcal{N}(0,\Delta)|\ge 2\sigma\right]=2\mathtt{Pr}\left[\mathcal{N}(0,1)\ge 2\sigma/\sqrt{\Delta}\right]\ge e^{-O((\sigma/\sqrt{\Delta}+1)^2)}\)

**Corollary 16.** _Running the procedure in Lemma 15 independently_ \(N=n^{\Theta(\varepsilon)}logn\) _times and taking the union gives set_ Q _which with probability at least_ 1-_n_<sup>-1/2</sup> _is a_ \((\varepsilon,\Delta)\)_-rectangular cover and has_ \(q=|\mathcal{Q}|\le n^{O(\varepsilon)}log^{3/2}n\) _rectangles, assuming that_ \(\Delta=\Theta(1)\) _and_ \(\varepsilon\in[\Theta(1/logn),\Theta(1)]\) _with appropriate constants._

_Proof._ The probability that a given \(\{x,y\}\in\genfrac(){pt}{2}{S}{2}\) with \(\|x-y\|^2\ge\Delta\) will **not** be included in any \(\langle\mathcal{Q}\rangle\) is at most \((1-n^{-O(\varepsilon)})^N\le\frac{2}{n^3}\) with an appropriate choice of constants. The number of such pairs is at most \(\genfrac(){pt}{2}{n}{2}\). By the union bound, the output Q will have desired properties with probability at least \(1-N\cdot\frac{2}{n}-\genfrac(){pt}{2}{n}{2}\cdot\frac{2}{n^3}\ge 1-n^{-1/2}\).

From now on we assume that we a given a \((\varepsilon,\Delta)\)-rectangular cover Q={_Q_<sub>1</sub>_,...,Q<sub>q</sub>_} with \(q\le n^{O(\varepsilon)}log^{3/2}n\) rectangles. We denote `OPT<sub>Q</sub>` to be the maximum value of the \(\mu\)-uniform Q-flow, where constant \(\mu\) will be specified later.

