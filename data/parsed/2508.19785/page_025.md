By Lemma 5.5, each element moves by at most \(\frac{8w}{1-\rho}<\frac{8}{\rho(1-\rho)}+\frac{48}{\rho(1-\rho)\cdot\kappa(p,q,\rho)}lnm\) positions in all subsequent rounds. Therefore, the maximum dislocation of the permutation returned by \(\mathsf{BasketSort}\) is at most \(\frac{9}{\rho(1-\rho)}+\frac{54}{\rho(1-\rho)\cdot\kappa(p,q,\rho)}lnm\) with the aforementioned probability. □

## 5.3 Analysis of the Total Dislocation

In this section we prove that the total dislocation of the sequence returned by \(\mathsf{BasketSort}\) is _O(m_) with high probability. We first define a condition, denoted by (⋆), which allows us to analyze the expected dislocation of a single element. Roughly speaking, if an element _x_ satisfies (⋆) w.r.t. a window size _w_, then _x_ still satisfies (⋆) until a window size of _O_(log_w_) with probability 1-_O_(1_/w_<sup>2</sup>) (Lemma 5.15). Then, in Section 5.3.1, we make use of the above fact to prove that the expected dislocation of each element is _O_(1). In order to do so, our analysis partitions the _O_(log_m_) rounds of \(\mathsf{BasketSort}\) into _O_(loglog_m_) phases, where each phase extends from a round having some window size _w_ to a round having a window size in _O_(log_w_). Finally, Section 5.3.2, uses the constant upper bound on the expected dislocation of each element to prove that the total dislocation is _O(m_) with high probability.

We start by formally defining (⋆). Given an element _x_ and a window size _w_, _x_ satisfies (⋆) w.r.t. _w_ if _both_ the following conditions hold:

(a) All elements _y_ with \(|\sigma_w(y)-x|\le\frac{15}{1-\rho}w\) are good; and<tbc>

(b) All elements _y_ with \(|\sigma_w(y)-x|\le(\frac{15}{1-\rho}-3)w\) are happy.

Lemma 5.13. _Let x be an element that satisfies_ (⋆) _w.r.t. w and assume that all elements z with_ \(|\sigma_w(z)-x|\le(\frac{15}{1-\rho}\rho+8)w\) _satisfy_ \(|\tau_w(z)-z|\le\rho\frac{w}{2}\)_. Then, x satisfies condition (a) of_ (⋆) _w.r.t._ \(\lfloor\rho w\rfloor\)_. Moreover, all elements z such that_ \(|\tau_w(z)-x|\le(\frac{15}{1-\rho}\rho+4)w\) _are good w.r.t._ \(\lfloor\rho w\rfloor\).

Proof. Let _Y_ denote the set of all elements _y_ for which \(|\tau_w(y)-x|\le(\frac{15}{1-\rho}\rho+4)w\). For any \(y\in Y\), by Lemma 5.2, we have \(|\tau_w(y)-\sigma_w(y)|<4w\), thus implying that

\(x-\left(\frac{15}{1-\rho}\rho+8\right)w\le\tau_w(y)-4w<\sigma_w(y)<\tau_w(y)+4w\le x+\left(\frac{15}{1-\rho}\rho+8\right)w.\)

That is, for any \(y\in Y\) , we have \(|\sigma_w(y)-x|\le\left(\frac{15}{1-\rho}\rho+8\right)w\). In particular, the hypotheses of the lemma imply that any \(y\in Y\) satisfies \(|\tau_w(y)-y|\le\rho\frac{w}{2}\) . Moreover, since \(\frac{15}{1-\rho}\rho+8\le\frac{15}{1-\rho}-3\), condition (a) of (⋆) w.r.t. _w_ for element _x_ ensures that _y_ is both good and happy w.r.t. _w_. Observe further that _Y_ contains all elements \(y'\) with \(|\sigma_w(y')-x|\le\frac{15}{1-\rho}\lfloor\rho w\rfloor\), which are those considered by condition (a) of (⋆) w.r.t. \(\lfloor\rho w\rfloor\) for element _x_. Indeed, for any \(y'\) with \(|\sigma_{\lfloor\rho w\rfloor}(y')-x|\le\frac{15}{1-\rho}\cdot\lfloor\rho w\rfloor\), by Lemma 5.3,

\(|x-\tau_w(y')|\le|x-\sigma_{\lfloor\rho w\rfloor}(y')|+|\sigma_{\lfloor\rho w\rfloor}(y')-\tau_w(y')|\le\frac{15}{1-\rho}\cdot\lfloor\rho w\rfloor+4w\le\left(\frac{15}{1-\rho}\rho+4\right)w.\)

Hence, to prove the claim, it suffices to show that all elements in _Y_ are good w.r.t. \(\lfloor\rho w\rfloor\). In the rest of the proof we focus on an element \(y\in Y\) and show that any element _z_ such that \(z<y-\rho w\) (resp. \(z>y+\rho w\)) must appear before (resp. after) _y_ in \(S_{\lfloor\rho w\rfloor}\), thus implying that _y_ is good w.r.t. \(\lfloor\rho w\rfloor\). We distinguish two cases depending on the value of \(|\sigma_w(z)-x|\).

