**Case 3.** \(0(x)=min(0(x),0(y)),1(y)=min(1(x),1(y))\)**.** Symmetric to case 2.

**Theorem** (Theorem 1.2, restated)**.** For all \(\varepsilon>0\), there exists an absolute constant \(\delta=\delta(\varepsilon)>0\) and a deterministic algorithm that, given two binary strings _x_ and _y_ of not-necessarily-equal length, outputs a \((\frac{1}{2}+\delta)\)-approximation of the longest common subsequence in time \(O(n^{1+\varepsilon})\) where _n_=max(|_x|,|y_|).

_Proof._ Let \(\delta_0\) be the constant in Lemma 6.2. Let \(\delta=\delta_0/5\). Let the input strings be _x_ and _y_ and assume without loss of generality \(|x|\le|y|\) and that \(min(0(x),0(y))\ge min(1(x),1(y))\). We have Trivial(_x,y_)=min(0(_x),_0(_y_)) and \(\mathsf{LCS}(x,y)\le min(0(x),0(y))+min(1(x),1(y))\).

If \(min(0(x),0(y))\ge(1+\delta_0)min(1(x),1(y))\), then because \(\frac{1+\delta_0}{2+\delta_0}>\frac{1}{2}+\delta\) the trivial algorithm gives a \((\frac{1}{2}+\delta)\)-approximation of the LCS. Thus we may assume \(min(0(x),0(y))\le(1+\delta_0)min(1(x),1(y))\). Delete \(min(0(x),0(y))-min(1(x),1(y))\le\delta_0min(1(x),1(y))\) zeros from each of _x_ and _y_ arbitrarily to obtain \(x'\) and \(y'\) with \(min(0(x'),0(y'))=min(1(x'),1(y'))\). We have

\(\mathsf{LCS}(x',y')\ge\mathsf{LCS}(x,y)-\delta_0min(1(x),1(y))\ge(1-\delta_0)\mathsf{LCS}(x,y).\)

Running the algorithm in Lemma 6.2 gives an approximation to \(\mathsf{LCS}(x',y')\) that is at least \((\frac{1}{2}+\delta_0)(1-\delta_0)\mathsf{LCS}(x,y)>(\frac{1}{2}+\delta)\mathsf{LCS}(x,y)\), as desired.

## 7 Conclusion and open questions

We close with some related open questions.

• What is the best possible approximation factor of binary LCS in almost-linear or truly subquadratic time? We give a \(\frac{1}{2}+\delta\) in almost-linear time. We made no attempt to optimize \(\delta\), and currently it depends on the runtime exponent \(1+\varepsilon\).<tbc>

• Related to the above, can we prove fine-grained hardness of approximation results for LCS? It is known that a deterministic \(2^{-(logn)^{1-\delta}}\) approximation in \(n^{2-\varepsilon}\) time for LCS over alphabet _n_<sup>_o_(1)</sup> would imply new circuit lower bounds, as would a deterministic \(1-\frac{1}{polylogn}\)-approximation for binary inputs \[AB17, AR18, CGL<sup>+</sup>19\].<tbc>

• We studied the algorithmic question of computing LCS, where, as the previous two questions highlight, the optimal approximation factor is open. We showed this algorithmic question is closed related to an analogous combinatorial question, which is also open: What is the largest constant \(\alpha\in(0,1)\) such that in any set \(C\subset\{0,1\}^n\) of \(|C|\ge 2^{\Omega(n)}\) binary strings, there are always two strings _x,y_ with \(\mathsf{LCS}(x,y)\ge\alpha n\)? The optimal \(\alpha\) is known to be in \(\left[\frac{1}{2}+10^{-40},2-\sqrt{2}\right]\) \[GHL22, BGH17\], and \(1-\alpha\) quantifies the maximum fraction of adversarial deletions that can be tolerated by a (asymptotically) positive rate code.<tbc>

<tbc>It would also be interesting to understand how strong is the connection between the deletion codes question and the algorithmic LCS question. At first blush, it seems that techniques derived solely from analysis of deletion codes should not give an \(\alpha\)-approximation for \(\alpha>2-\sqrt{2}\approx 0.59\) (because of the deletion codes construction \[BGH17\]), so beating this ratio would show some separation between the two questions.<tbc>

• How does the optimal subquadratic time or almost-linear time approximation factor grow with the alphabet size? Over alphabet size _q_, we show that we can beat (barely) the trivial \(\frac{1}{q}\)-approximation. We know that we can always get a randomized \(\frac{1}{n^{o(1)}}\)-approximation in linear time \[ANSS22, Nos21\], which is much better than \(\frac{1}{q}\) for large alphabets.<tbc>

