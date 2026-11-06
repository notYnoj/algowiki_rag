<tbc>of (certified) rectangles is _ordered_ if any two (certified) rectangles are comparable under this partial order.

For any two strings _x_ and _y_, fix a canonical matching \(\tau=\tau(x,y)\) between the bits of _x_ and _y_ that achieves the longest common subsequence (\(\tau\) is not necessarily unique, but we can fix it to be, say, the lexicographically earliest one). For \(I\subset\left[|x|\right]\), let \(J_I^\tau\) denote the (unique) smallest interval such that the bits of _x<sub>I</sub>_ are only matched with bits in \(y_{J_I^\tau}\) in the matching \(\tau\). Note that clearly if \(I'\) and _I_ are disjoint, then \(J_I^\tau\) and \(J_{I^\prime}^\tau\) are disjoint.

For any string _x_, we write _d(x_) for the density of _x_, i.e. the ratio between the number of ones in _x_ and the length of _x_. For \(\gamma>0\), we say an interval _I_ is \(\gamma\)_-balanced in x_ if \(d(x_I)\in\left[\frac{1}{2}\pm\gamma\right]\), and we say _I_ is \(\gamma\)_-imbalanced in x_ otherwise. If _x_ is understood (as it always will be), we simply say \(\gamma\)-balanced and \(\gamma\)-imbalanced. A useful property of balanced strings _x_ is that we can find LCS close to |_x|/_2 with any other string of the same length.

**Lemma 2.1.** _If x and y are strings such that x is_ \(\gamma\)_-balanced and_ |_x_|=|_y|, then_ \(\mathsf{LCS}(x,y)\ge(\frac{1}{2}-\gamma)|x|\).

_Proof._ Suppose without loss of generality _y_ has at least |_y|/_2 ones. Then _y_ has at least |_x|/_2 ones. Since _x_ is \(\gamma\)-balanced, then _x_ has at least \((\frac{1}{2}-\gamma)|x|\) ones, so the LCS is at least \((\frac{1}{2}-\gamma)|x|\).

#### Algorithms

Let Trivial(_x,y_) denote the output of the simple algorithm that outputs the longest all-0s or all-1s subsequence. Clearly Trivial(_x,y_)=max(min(0(_x),_0(_y_)),min(1(_x),_1(_y_)).

Rubinstein and Song showed that one can obtain a \((\frac{1}{2}+\delta)\)-approximation of equal length LCS. Their result immediately extends to a \((\frac{1}{2}+\delta')\)-approximation for near-equal length LCS, which we use.

**Theorem 2.2** (Follows immediately from \[RS20\])**.** _For any_ \(\varepsilon>0\)_, there exists a_ \(\delta_{eq}=\delta_{eq}(\varepsilon)>0\) _and a_ \((\frac{1}{2}+\delta_{eq})\)_-approximation of the LCS of two binary strings x and y with_ \(|x|,|y|\in\left[(1-\delta_{eq})n,(1+\delta_{eq})n\right]\) _in time_ \(O(n^{1+\varepsilon})\).

Let EqLCS(_x,y_) denote the output of the algorithm from Theorem 2.2.

## 3 Proof sketch

In this section we give a high-level overview of our almost-linear time LCS approximation algorithm, Theorem 1.2. We start by describing the novel ingredient, our algorithmic structure lemma, Lemma 4.1. It states, roughly speaking, that binary strings _s_ of length _w_ can be classified among one of _O_(log_w_) oscillation types or scales, such that for any two strings _s,t_ with the same type, there is a long subinterval _s<sub>I</sub>_ in _s_ with \(\mathsf{LCS}(s_I,t)>(1/2+\delta)|s_I|\). Moreover, the lemma is algorithmic in that both the type of _s_ and the long subinterval _s<sub>I</sub>_ are computable from _s_ in time nearly linear in _w_.

To formally define oscillation types, we first introduce the notion of a flag. In a string _x_, an \(\ell\)_-flag_ is an index _i_ such that between the _i_th one and the \((i+\ell)\)-th one, there are strictly more than \(10(\ell-1)\) zeros. In other words, an \(\ell\)-flag is a one-bit in _s_ that is immediately followed by a 0-dense interval of length on the order of \(\ell\). The existence of many \(\ell\)-flags in _x_ means that _x_ "oscillates at scale \(\ell\)." An \(\ell^+\)_-flag_ is an index _i_ that is a _t_-flag for some \(t\ge\ell\), where _t_ must be a power of two. The oscillation types guaranteed by Lemma 4.1 are as follows.

**Definition 3.1** (Definition 4.5 below)**.** Let \(\ell\) be a power of two, \(\ell\in\left[1,w\right]\), and \(x\in\{0,1\}^w\).

1. We say that _x_ is \(\ell\)_-coarse_ if \(\ell\ge\varepsilon^2w\) and there is a \(\varepsilon^2\)-imbalanced interval _I_ in _x_ of length \(\ell\). We say _x_ is _coarse_ if it is \(\ell\)-coarse for some \(\ell\ge\varepsilon^2w\).<tbc>

2. We say that _x_ is \(\ell\)_-fine_ if it is not coarse, \(\ell<\varepsilon^2w\), the number of \(\ell^+\)-flags in _x_ is at least \(\varepsilon w\), and _x_ contains \((0^\ell 1^\ell)^{\varepsilon w/\ell}\) as a subsequence. We say _x_ is _fine_ if it is \(\ell\)-fine for some \(\ell<\varepsilon^2w\).<tbc>

