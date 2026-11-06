small fraction of the path in the vicinity of column _m<sub>i</sub>_. Equivalently, column _x_ is only affected if it is very close to an anchor _m<sub>i</sub>_. We call _x_ a _hitter_ of (_l,r_\] if there exist an anchor \(m_i=l+i\cdot(r-l)/M\) such that \(x\in(m_i-I_{s-3},m_i+I_{s-3}]\) (which is the union of the two scale-(_s_-3) intervals around _m<sub>i</sub>_). We call a column \(x'\) a _frequent hitter_ if there are more than _S_<sup>0.83</sup> scales \(s'\) that is a multiple of 3 such that \(x'\) is a hitter of the scale-\(s'\) interval \((l',r']\unknown x'\). Since each scale that is a multiple of 3 is in \(\widetilde{S}\) u.a.r with probability 1_/S_<sup>0.98</sup>, we can see that if \(x'\) is not a frequent hitter, then there is a probability of at least 1-1_/S_<sup>0.15</sup> that no interval where \(x'\) is a hitter lies on an active scale. Thus it suffices to prove two claims:

• There are not too many frequent hitters (Claim 7.4);<tbc>

• If \(x'\) is not a hitter of an interval that contains it, then on average, the rounding at that interval should not affect \(x'\) (Claim 7.5).

Now we introduce the two claims in detail. We claim that there are not too many frequent hitters:

**Claim 7.4.** _The number of frequent hitters does not exceed n/_2log<sup>0.02</sup>(_n)._

Recall that for any column \(x'\), \(|p(x'+1)-p(x')|\le 1\), namely that the slope of _p_ cannot be more than \(45^\circ\) anywhere (either in the (+1,+1) or the (+1,-1) direction). The closer _p(l,r_\] is to a 45-degree diagonal (i.e., the smaller (_r-l_)-|_p<sub>s</sub>(r_)-_p<sub>s</sub>(l_)| is), the less freedom the path _p(l,r_\] has. Therefore, it is beneficial to "normalize" curvature by dividing it by (_r-l_)-|_p<sub>s</sub>(r_)-_p<sub>s</sub>(l_)|. Recall that for a path _p_ from \(\langle l,y_l\rangle\) to \(\langle r,y_r\rangle\), we let the forward difference operator \(\Delta p\) be the sequence

\(\Delta p:=(p(l+\mathcal{B}_x)-p(l),p(l+2\mathcal{B}_x)-p(l+\mathcal{B}_x),\dots,p(r)-p(r-\mathcal{B}_x)).\)

We have the following claim which formally states that if such "normalized" total deviation is small, then rounding does not affect non-hitters:

**Claim 7.5.** _Given a scale-s interval_ (_l,r_\]_, let p<sub>s</sub> be a path from column l to column r with_ |_p<sub>s</sub>(r_)-_p<sub>s</sub>(l_)|_\<r-l. Suppose that_

\(\frac{\mathrm{TD}_{M^3}(\Delta p_s(l,r])}{(r-l)-|p_s(r)-p_s(l)|}=o\left(\frac{1}{M^3}\right),\)

_where_ \(\mathrm{TD}_{M^3}(\Delta p_s(l,r])\) _is the M_<sup>3</sup>_-way total deviation of_ \(\Delta p_s(l,r]\):

\(\mathrm{TD}_{M^3}(\Delta p_s(l,r])=\sum_{1\le i^\prime\le M^3}\left|p_s(m_{i^\prime}^{^\prime})-p_s(m_{i^\prime-1}^{^\prime})-\frac{p_s(r)-p_s(l)}{M^3}\right|,\)

_where for every_ \(0\le i'\le M^3\)_, the_ \(i'\)_-th M_<sup>3</sup>_-way anchor is_ \(m_{i^\prime}^{^\prime}:=l+i'\cdot\frac{r-l}{M^3}\).

_Then, there exists an_ {_s}-regular_ \(\langle l,p_s(l)\rangle\)-\(\langle r,p_s(r)\rangle\) _path p_<sub>_s_-1</sub> _such that_

\(p_s(x-1,x]=p_{s-1}(x-1,x]\)

_holds for every x that is not a hitter of_ (_l,r_\].

To facilitate the use of Claim 7.5, we later derive the following claim using Lemma 4.3:

**Claim 7.6.** _Let p be the path in Lemma 7.3. For a random column x such that the weight of p before x is non-zero, with probability_ \(1-o\left(\frac{1}{M\mathrm{log}^{0.02}(n)}\right)\)_, every interval_ \((l,r]\unknown x\) _on an active scale satisfies the following bound:_

\(\frac{\mathrm{TD}_{M^3}(\Delta(p(l,r]))}{(r-l)-|p(r)-p(l)|}=o\left(\frac{1}{M^3}\right),\) (24)

