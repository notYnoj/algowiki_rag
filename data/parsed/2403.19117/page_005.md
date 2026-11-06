<tbc>Comparing Equation (5) with Equation (7) gives the lower bound

\(w_i=w([i])-w([i-1])\ge(2^i-1-\Delta)-(2^{i-1}-1+(i-1)\Delta)=2^{i-1}-i\Delta,\)

which is very close to the upper bound from Equation (6). Together we get

\(w_i-2^{i-1}\in[-i\Delta,\Delta]\) (8)

for all \(i\in[n]\).

Equation (8) gives a very rigid structure of the large input numbers. In the next lemma we exploit this structure to improve the naive meet-in-middle subset sum counting algorithm from Lemma 3.

\(\blacktriangleright\) **Lemma 7.** _For any given T\<_2_<sup>n</sup>, we can compute_ \(\sum_{t=0}^Tf_t\) _in_ \(O^*(\sqrt{\Delta})\) _time._

**Proof.** Let _i_<sup>∗</sup> be the minimum \(i^*\in[n]\) such that \(2^{i^*}\ge 3n^2\Delta\), which exists by our assumption \(\Delta\le 2^n/(3n^2)\). Let _A_={1,2_,...,i_<sup>∗</sup>} and _B_={_i_<sup>∗</sup>+1_,...,n_}.

By Equation (7), \(w(A)<2^{i^*}+n\Delta\).

For every \(B'\subseteq B\), by Equation (8) we have

\(\big|w(B')-\sum_{j\in B^\prime} 2^{j-1}\big|\le\sum_{j\in B^\prime}|w_j-2^{j-1}|\le\sum_{j\in B^\prime} j\Delta\le n^2\Delta.\)

In other words, the subset sums of \(\{w_j\}_{j\in B}\) are \(n^2\Delta\)-additively approximated by the subset sums of \(\{2^{j-1}\}_{j\in B}\). The subset sums of the latter set form an arithmetic progression \(\{k\cdot 2^{i^*}:0\le k<2^{n-i^*}\}\), namely all _n_-bit binary numbers whose lowest _i_<sup>∗</sup> bits are zeros. Notably, this arithmetic progression is very sparse: its difference 2<sup>_i_<sup>∗</sup></sup> is large enough compared to \(w(A)<2^{i^*}+n\Delta\).

Given query _T_, we want to count the number of pairs \((A',B')(A'\subseteq A,B'\subseteq B)\) such that \(w(A')+w(B')\le T\). To do this, we enumerate \(B'\subseteq B\), and consider three cases (the non-trivial case is Case 3, where \(w(B')\) and \(\sum_{j\in B^\prime} 2^{j-1}\) are close to _T_):

**Case 1:** \(\sum_{j\in B^\prime} 2^{j-1}\le T-2^{i^*}-(n+n^2)\Delta\). Then, for all \(A'\subseteq A\), we have \(w(A')+w(B')\le w(A)+w(B')\le(2^{i^*}+n\Delta)+(n^2\Delta+\sum_{j\in B^\prime} 2^{j-1})\le T\). Hence \(B'\) contributes 2<sup>|_A_|</sup> many pairs \((A',B')\).<br>
**Case 2:** \(\sum_{j\in B^\prime} 2^{j-1}>T+n^2\Delta\). Then, for all \(A'\subseteq A\), we have \(w(A')+w(B')\ge w(B')\ge\sum_{j\in B^\prime} 2^{j-1}-n^2\Delta>T\). Hence \(B'\) does not contribute any pairs \((A',B')\).<br>
**Case 3:** otherwise, \(\sum_{j\in B^\prime} 2^{j-1}\in(T-2^{i^*}-(n+n^2)\Delta,T+n^2\Delta]\). This interval has length \(2^{i^*}+(n+n^2)\Delta+n^2\Delta\le 2\cdot 2^{i^*}\) by our choice of _i_<sup>∗</sup>. Since \(\sum_{j\in B^\prime} 2^{j-1}\) is a multiple of 2<sup>_i_<sup>∗</sup></sup> in this interval, it has at most two possibilities, namely \(2^{i^*}\cdot\lfloor\frac{T-(n+n^2)\Delta}{2^{i^*}}\rfloor\) and \(2^{i^*}\cdot\left(\lfloor\frac{T-(n+n^2)\Delta}{2^{i^*}}\rfloor+1\right)\), and then \(B'\) is uniquely determined by the binary decomposition of \(\sum_{j\in B^\prime} 2^{j-1}\). For each possible \(B'\), we count the number of \(A'\subseteq A\) such that \(w(A')\le T-w(B')\) using meet-in-middle (Lemma 3) with time complexity \(O^*(2^{|A|/2})=O^*(2^{i^*/2})=O^*(\sqrt{\Delta})\) by the definition of _i_<sup>∗</sup>.<br>
Note that in _O_<sup>∗</sup>(1) time we can easily find the (at most two) subsets \(B'\) satisfying Case 3, and also count the total contribution of Case 1. Hence the overall time complexity is \(O^*(\sqrt{\Delta})\). \(\blacktriangleleft\)<tbc>

<tbc>Using Lemma 7 we can solve Pigeonhole Equal Sums using binary search, in the same way as described in the last paragraph of Section 2. The running time is \(O^*(\sqrt{\Delta})\). This finishes the proof of Lemma 4.

