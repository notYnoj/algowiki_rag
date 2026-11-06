To show that these are the only exceptions and thereby finish the proof, for every scale _s_, we show the (scale-_s_) proposition that _p<sub>s</sub>(x_-1_,x_\]=_p(x_-1_,x_\] for every column _x_ (even those before which the weight of _p_ is 0), such that both of the following conditions

1. _x_ does not hit any interval on an active scale \(s'>s\), and<tbc>

2. (24) is satisfied by every interval \((l,r]\unknown x\) on an active scale \(s'>s\).

This would imply that if every interval on an active scale containing _x_ satisfies (24), and _x_ does not hit any interval on an active scale, then we would have \(\widehat{p}(x-1,x]=p(x-1,x]\) (i.e., the only exceptions to the argument are these two cases above). We can prove the proposition by induction, using a step-wise decrement of 3 scales down from scale _S_ (for which the proposition is trivially true since there are no active scales above). As our induction assumption, suppose that the proposition is true for a scale _s_ that is a multiple of 3 and we want to argue that it is also true for scale (_s_-1), (_s_-2) and (_s_-3). If _s_ is not an active scale then no rounding takes place and the proposition is therefore true for scale (_s_-1) (and thus for scales (_s_-2) and (_s_-3) since active scales are multiples of 3). The remaining case is if _s_ is an active scale and the scale-(_s_-3) proposition conditions also hold for _x_ (i.e., _x_ also does not hit the scale-_s_ interval \((l_s,r_s]\unknown x\), and (24) holds for (_l<sub>s</sub>,r<sub>s</sub>_\]). Let (_l<sub>s</sub>,r<sub>s</sub>_\] be the scale-_s_ interval containing _x_. For every \(x'\in(l_s,r_s]\), for every scale \(s'\ge s\), the scale-\(s'\) interval containing \(x'\) is identical to the scale-\(s'\) interval containing _x_. Therefore the scale-_s_ proposition conditions hold for every \(x'\in(l_s,r_s]\) and we have _p<sub>s</sub>(l<sub>s</sub>,r<sub>s</sub>_\]=_p(l<sub>s</sub>,r<sub>s</sub>_\] by the induction assumption that the scale-_s_ proposition holds. Since (24) holds for _p(l<sub>s</sub>,r<sub>s</sub>_\], it also holds for _p<sub>s</sub>(l<sub>s</sub>,r<sub>s</sub>_\]. Since _x_ does not hit (_l<sub>s</sub>,r<sub>s</sub>_), from Claim 7.5, we must have _p_<sub>_s_-1</sub>(_x_-1_,x_\]=_p(x_-1_,x_\] (and thus _p_<sub>_s_-2</sub>(_x_-1_,x_\]=_p_<sub>_s_-3</sub>(_x_-1_,x_\]=_p(x_-1_,x_\] since (_s_-1) and (_s_-2) are not active scales and no rounding takes place).

Now we prove the three ingredients used in the proof of Lemma 7.3 above:

**Claim 7.4** (Restated)**.** _The number of frequent hitters does not exceed n/_2<sup>log<sup>0.02</sup>(_n_)</sup>.

_Proof._ For a column _x_ and a scale _s_ that is a multiple of 3, let \(g_{x,s}\in[0,1]\) be 1 if _x_ is a hitter of the interval \((l,r]\unknown x\) on scale _s_. Notice that the values of \(g_{x^\prime,s^\prime}\) for \(s'\ge s+3\) are identical for all \(x'\in(l,r]\) since those values depend on anchors of larger intervals \((l',r']\supseteq(l,r]\). Therefore _g<sub>x,s</sub>_ is independent of \(g_{x,s^\prime}\) for \(s'\ge s+3\). Furthermore, _g<sub>x,s</sub>_ is +1 for \(O\left(\frac{1}{M^2}\right)\) of the \(x\in(l,r]\). Let \(g_x:=\sum_{s\in[S]\cap 3\mathbb{Z}}g_{x,s}\). For a uniformly random \(x\in[n]\), We can see that _g<sub>x</sub>_ is the sum of _S/_2 i.i.d. samples of Ber(_O_(1_/M_<sup>2</sup>)), whose mean is _O(S/M_<sup>2</sup>)=_o(S_<sup>0.83</sup>).

By applying Hoeffding’s inequality (Lemma 3.1), the probability that _g<sub>x</sub>\>S_<sup>0.83</sup> is less than \(1/2^{\Omega(S^{0.66})}\checkmark 1/2^{\mathrm{log}^{0.02}(n)}\). This means that the number of frequent hitters is no more than _n/_2<sup>log<sup>0.02</sup>(_n_)</sup>.

**Claim 7.5** (Restated)**.** _Given a scale-s interval_ (_l,r_\]_, let p<sub>s</sub> be a path from column l to column r with_ |_p<sub>s</sub>(r_)-_p<sub>s</sub>(l_)|_\<r-l. Suppose that_<tbc>

\(\frac{\mathrm{TD}_{M^3}(\Delta p_s(l,r])}{(r-l)-|p_s(r)-p_s(l)|}=o\left(\frac{1}{M^3}\right),\)

<tbc>_where_ \(\mathrm{TD}_{M^3}(\Delta p_s(l,r])\) _is the M_<sup>3</sup>_-way total deviation of_ \(\Delta p_s(l,r]\):

\(\mathrm{TD}_{M^3}(\Delta p_s(l,r])=\sum_{1\le i^\prime\le M^3}\left|p_s(m_{i^\prime}^{^\prime})-p_s(m_{i^\prime-1}^{^\prime})-\frac{p_s(r)-p_s(l)}{M^3}\right|,\)

_where for every_ \(0\le i'\le M^3\)_, the_ \(i'\)_-th M_<sup>3</sup>_-way anchor is_ \(m_{i^\prime}^{^\prime}:=l+i'\cdot\frac{r-l}{M^3}\).

