\(\mathsf{LCS}(x_I,y)\ge(\frac{1+\varepsilon^2}{2})\ell\ge\frac{|I|}{2}+\frac{\varepsilon^4}{2}w\), as desired. Furthermore, _I_ can be found in linear time by a linear sweep, and the common subsequence is simply \(b^{(\frac{1+\varepsilon^2}{2})\ell}\) as desired.<tbc>

<tbc>Now suppose _x_ has property \(P_\ell\) for \(\ell<\varepsilon^2w\), and _y_ has property \(Q_\ell\). Thus, _x_ is \(\ell\)-fine and _y_ contains \(y_\ell\) as a subsequence. By Lemma 4.7, there exists an interval _I_ with \(\mathsf{LCS}(x_I,y)\ge\frac{|I|}{2}+\varepsilon^3|x|\), as desired. Furthermore, also by Lemma 4.7, _I_ and the common subsequence of _x<sub>I</sub>_ and _y_ can be computed from _x_ and _t_ in time _O(w_log_w_), independent of _y_, as desired.

This proves Lemma 4.1.

## 5 Almost-linear time algorithm

We now give the almost-linear time algorithm for the "equally balanced" case, which implies our main result. Specifically, we prove the following (see Section 6 for how Theorem 1.2 follows from Theorem 3.2).

**Theorem** (Theorem 3.2, restated)**.** For all \(\varepsilon>0\), there exists an absolute constant \(\delta=\delta(\varepsilon)>0\) and a deterministic algorithm that, on input strings _x_ and _y_ with \(0(x)=1(x)\le min(0(y),1(y))\), gives a \((\frac{1}{2}+\delta)\)- approximation of the longest common subsequence in time \(O(n^{1+\varepsilon})\).

The algorithm is given in Algorithm 2 with the covering step given in Algorithm 1. The rest of this section proves the correctness.

### 5.1 Parameters and notation conventions

Throughout _x_ and _y_ are the input strings satisfying \(0(x)=1(x)\le min(0(y),1(y))\), and throughout _n_=max(|_x|,|y_|). Let _w_ be the closest power of 2 to \(\frac{|x|}{log|x|}\). We may assume by deleting a negligible number of bits from _x_ and _y_ that |_x_| and |_y_| are multiples of _w_. Let \(m_x:=\frac{|x|}{w}\sim log|x|\) and \(m_y:=\frac{|y|}{w}\sim\frac{|y|log|x|}{|x|}\) . Throughout, we always denote intervals for string _x_ by the letter _I_, and intervals for string _y_ by the letter _J_. By abuse of notation, we let intervals _I_ (possibly with decorations) denote the substring _x<sub>I</sub>_, and we let intervals _J_ denote the substring _y<sub>J</sub>_.

Let \(\varepsilon>0\) be such that \(O(n^{1+\varepsilon})\) is the desired runtime. Let \(\delta_{code}\) be the constant from Lemma 4.1. Let \(\delta_{eq}=\delta_{eq}(\frac{\varepsilon}{2})\) be the constant from Theorem 2.2. Let \(\alpha,\beta,\gamma,\delta,\theta\) be constant powers of 1/2 that satisfy \(min(\delta_{eq},\delta_{code})\ge\alpha\gg\beta\gg\gamma\gg\delta=\theta\). That is, \(\delta\) is sufficiently small compared to \(\gamma\), which is sufficiently small compared to \(\beta\), which is sufficiently small compared to \(\alpha\). For completeness, we note it suffices to take \(\theta=\delta=\gamma^8,\gamma=\frac{1}{2}\beta^2,\beta=\alpha^2\). We did not try to optimize our constants. We give the following intuition for the above parameters.

• \(\alpha\) lower bounds the LCS advantage gained from both algorithmic structure lemma rectangles and nearly-square rectangles.<tbc>

• \(\beta\) is the "nearly-square" parameter: in the optimal LCS, intervals _I_ are called _nearly-square_ if they get matched to intervals of length \(\le(1+\beta)|I|\). We may assume at most \(\beta^2\) fraction of intervals are nearly-square or else the nearly-square rectangles (together with "trivial rectangles") give a \((\frac{1}{2}+\text{poly}\beta)\)- approximation by applying EqLCS to each of them.<tbc>

• \(\gamma\) is the "imbalanced" parameter and discretization parameter for _I_-intervals: we may assume most \(\gamma w\)-length intervals to be \(\gamma\)-balanced, or else the "Trivial rectangles" give a \((\frac{1}{2}+\text{poly}\gamma)\)-approximation. We also round all _I_-intervals so that they are \(\gamma w\)-aligned. \(\gamma\) is small enough so that the effect of this rounding is negligible.<tbc>

