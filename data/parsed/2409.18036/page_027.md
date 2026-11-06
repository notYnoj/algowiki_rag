<tbc>When the size of _I_ doubles or halves, we can rebuild the entire data structure. The rebuilding cost can be charged to those updates, making each update cost _O_(1) amortized. Here, we can use de-amortization techniques to ensure the complexity becomes _O_(1) in the worst case.

\(\square\)

## C Proofs for Section 3 (Sampling Random Variates in the Word RAM Model)

LEMMA 3.3. _These two claims hold simultaneously: (i) the numerator and the denominator of p=p_<sup>∗</sup> _both can be represented with O(n_) _words and p can be evaluated in O(poly(n_)) _time; and (ii) there exists an algorithm that can evaluate each i-bit approximation_ \(\tilde{p}_i\) _of p=p_<sup>∗</sup>_, satisfying all conditions stated in Theorem 3.1, in O(poly(i_)) _time._

PROOF. We first prove claim (i). Let _A_ and _B_ denote the numerator and denominator of _q_. By definition, both _A_ and _B_ fit in _O_(1) words. Then it can be verified that the numerator and the denominator of _p_<sup>∗</sup> can be computed as _B<sup>n</sup>_-(_B-A)<sup>n</sup>_ and _B<sup>n</sup>-nAB_<sup>_n_-1</sup> in _O_(poly(_n_)) time, respectively. And each of them fits in _O(n_) words as they are just multiplication results of _n_ constant-word integers. As a result, \(p^*=\frac{1-(1-q)^n}{n\cdot q}\) is a rational number with _O(n_)-word numerator and denominator and it can be evaluated in _O_(poly(_n_)) time.

Next we prove claim (ii). According to the binomial theorem, \(1-(1-q)^n=\sum_{j=1}^n\genfrac(){pt}{2}{n}{j}(-1)^{j+1}q^j\). Thus, \(p^*=\frac{1-(1-q)^n}{n\cdot q}\) can be written as \(p^*=\sum_{j=1}^na_j\) , where \(a_j=\frac{(-1)^{j+1}q^{j-1}(n-1)!}{j!(n-j)!}\) . Note that \(\frac{(n-1)!}{(n-j)!}\le n^{j-1}\) and \(nq\le 1\). We can bound the absolute value of _a<sub>j</sub>_ with \(|a_j|\le\frac{1}{j!}\le\frac{1}{2^{j-1}}\). Further, \(|\sum_{j=i+3}^na_j|\le\sum_{j=i+3}^n|a_j|\le\frac{1}{2^{i+1}}\). In other words, the sum of _a<sub>j</sub>_ for \(1\le j\le i+2\) achieves a good approximation of _p_<sup>∗</sup>. Denoting \(\tilde{p}_i=\sum_{j=1}^{i+2}a_j\), we have \(|p^*-\tilde{p}_i|\le\frac{1}{2^{i+1}}\).

Now we discuss how to compute \(\tilde{p}_i\) in the Word RAM model. We perform the computation with _working precision r_, which means we work with floating point numbers and each of these floating point numbers contains an exact exponent encoded by an array of words and a mantissa which is an array of \(\lceil r/d\rceil\) words. Each mathematical operation between two floating point numbers under working precision _r_ can be done in _O(poly(r_)) time. Since \(\tilde{p}_i\) can be evaluated with _O(poly(i_)) such floating point mathematical operations, thus an approximation (with working precision _r_) of \(\tilde{p}_i\), denoted by \(\tilde{p}_i(r)\), can be computed in _O(poly(i,r_)) time. Analogous to the analysis in Appendix C of \[7\], it suffices to choose _r=O(poly(i_)) to achieve an absolute error \(|\tilde{p}_i(r)-\tilde{p}_i|\le\frac{1}{2^{i+1}}\).

As a result, \(|\tilde{p}_i(r)-p^*|\le|\tilde{p}_i(r)-\tilde{p}_i|+|p^*-\tilde{p}_i|\le\frac{1}{2^{i+1}}+\frac{1}{2^{i+1}}=\frac{1}{2^i}\). Therefore, \(\tilde{p}_i=\tilde{p}_i(r)\) is a valid _i_-bit approximation of _p_<sup>∗</sup>, and the overall computational cost is bounded by _O_(poly(_i_)). \(\square\)

LEMMA 3.4. _These two claims hold simultaneously: (i) the numerator and the denominator of_ \(p=\frac{1}{2p^*}\) _both can be represented with O(n_) _words and p can be evaluated in O(poly(n_)) _time; and (ii) there exists an algorithm that can evaluate each i-bit approximation_ \(\tilde{p}_i\) _of_ \(p=\frac{1}{2p^*}\)_, satisfying all conditions stated in Theorem 3.1, in O(poly(i_)) _time._

PROOF. Analogous to the proof of Lemma 3.3, the numerator and the denominator of \(p=\frac{1}{2p^*}\) fit in _O(n_) words and _p_ can be evaluated in _poly(n_) time. Thus, claim (i) holds.

To prove claim (ii), by Lemma 3.3, for an arbitrary integer \(r\ge 3\), an _r_-bit approximation \(\tilde{p}_r^*\) of _p_<sup>∗</sup> can be computed in _O(poly(r_)) time, such that \(|\tilde{p}_r^*-p^*|\le\frac{1}{2^r}\). By Newton’s method \[6\], an approximate reciprocal of \(2\tilde{p}_r^*\), denoted by _u(r_), can be computed in _O(poly(i_)) time with error at most \(\frac{1}{2^{i+1}}\), namely, \(|u(r)-\frac{1}{2\tilde{p}_r^*}|\le\frac{1}{2^{i+1}}\).

Therefore, the absolute error, |_p-u(r_)|, is bounded by \(|\frac{1}{2p^*}-u(r)|\le|\frac{1}{2p^*}-\frac{1}{2\tilde{p}_r^*}|+|u(r)-\frac{1}{2\tilde{p}_r^*}|\le\frac{|2p^*-2\tilde{p}_r^*|}{2p^*\cdot 2p_r^*}+\frac{1}{2^{i+1}}\le\frac{1}{2^{r-1}}+\frac{1}{2^{i+1}}\), where the last inequality comes from the upper bound of \(p^*\ge 1-1/e\ge\frac{1}{2}\) and \(\tilde{p}_r^*\ge p^*-\frac{1}{2^r}\ge\frac{1}{2}\).

Thus, it suffices to choose _r=i_+2 to obtain an _i_-bit approximation _u(r_) of _p_, and the overall computational cost is bounded by _O(poly(i_)). \(\square\)

