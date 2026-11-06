<tbc>because the intervals \(\tilde{I}_i^R,\tilde{I}_i^L,\tilde{I}_i\) are all \(\gamma w\)-aligned and thus \(\gamma\)-balanced. Thus, by Lemma 5.2, the output of FullLCSAAlgorithm(_x,y_) is at least

\(\sum_{i\unknown m_x^{\prime\prime} t\unknown i}\left(\kappa_i^L+\kappa_i^M+\kappa_i^R\right)+\sum_{i\unknown m_x^{\prime\prime} t\unknown i}\kappa_i\unknown\sum_{i\unknown m_x^{\prime\prime} t\unknown i}\left(\left(\frac{1}{2}-\gamma\right)(|\tilde{I}_i^L|+|\tilde{I}_i^M|+|\tilde{I}_i^R|)+\alpha w\right)+\sum_{i\unknown m_x^{\prime\prime} t\unknown i}\left(\frac{1}{2}-\gamma\right)|\tilde{I}_i|\)<br>
\(\unknown\left(\frac{1}{2}-\gamma\right)w\cdot m''_x+\alpha w\cdot\frac{\beta}{3}m''_x\)<br>
\(\unknown\left(\frac{1+\delta}{2}\right)\mathsf{LCS}(x,y)\)

In the third inequality, we used that \(m''_xw\unknown(m'_x-t)w\unknown(1-3\beta^2)m_xw\) and \(m_xw=|x|\unknown\mathsf{LCS}(x,y)\).

We can now finish the proof of Theorem 3.2.

_Proof of Theorem 3.2._ We have now proved that (2) and (3) always hold, and that FullLCSAAlgorithm runs in time \(O(n^{1+\varepsilon})\), so FullLCSAAlgorithm gives a \((\frac{1+\delta}{2})\)-approximation of the LCS of two binary strings with \(0(x)=1(x)\unknown min(0(y),1(y))\) in time \(O(n^{1+\varepsilon})\), as desired.

## 6 Putting it all together

In this final section we use standard techniques to finish the proof of Theorem 1.2 given the balanced case Theorem 3.2. This proved in \[RS20\] for equal length strings and in \[AW21\] for unequal length strings (see also \[Akm21\]).

**Lemma 6.1** (Lemma 13 of \[AW21\], see also Lemma 3.5 of \[Akm21\])**.** _For every_ \(\rho>0\)_, there exists_ \(\delta=\delta(\rho)>0\) _such that the following holds. There exists an algorithm which, given binary strings x,y with_ \(|x|\unknown|y|\) _and_ \(0(x)=1(y)\unknown(\frac{1}{2}-\rho)|x|\)_, computes a_ \((\frac{1}{2}+\delta)\)_-approximation of_ LCS(_x,y_) _in deterministic linear time._ <sup>2</sup>

**Lemma 6.2.** _For all_ \(\varepsilon>0\)_, there exists an absolute constant_ \(\delta=\delta(\varepsilon)>0\) _and a deterministic algorithm that, given two strings x and y with_ \(|x|\unknown|y|\) _and_ min(1(_x),_1(_y_))=min(0(_x),_0(_y_))_, outputs a_ \((\frac{1}{2}+\delta)\)_- approximation of_ LCS(_x,y_) _in time_ \(O(|y|^{1+\varepsilon})\).

_Proof._ Let \(\delta_1=\delta_1(\varepsilon)>0\) be the absolute constant in Theorem 3.2. Let \(\delta_2>0\) be the absolute constant in Lemma 6.1 with parameter \(\rho=\delta_1/10\). Let \(\delta=min(\delta_1/2,\delta_2)\). As \(|x|\unknown|y|\), we have three cases, and we find a \((\frac{1}{2}+\delta)\)-approximation to LCS(_x,y_) in each.

### Case 1.

0(_x_)=min(0(_x),_0(_y_)),1(_x_)=min(1(_x),_1(_y_)). Then 0(_x_)=1(_x_)=|_x|/_2 and \(\mathsf{LCS}(x,y)\unknown|x|/2\). The algorithm in Theorem 3.2, gives a \((\frac{1}{2}+\delta_1)\)-approximation of the LCS.

### Case 2.

0(_y_)=min(0(_x),_0(_y_)),1(_x_)=min(1(_x),_1(_y_)). We have \(1(x)=0(y)\unknown 0(x)\). There are two subcases.

**Subcase 2a.** \(1(x)\unknown(\frac{1}{2}-\rho)|x|\)**.** In this case, delete \(0(x)-1(x)\unknown\rho|x|\) zeros from _x_ arbitrarily to get a balanced subsequence \(x'\). Then \(\mathsf{LCS}(x',y)\unknown\mathsf{LCS}(x,y)-\rho|x|\unknown(1-\rho)\mathsf{LCS}(x,y)\). Thus, the algorithm in Theorem 3.2 gives a common subsequence of length \((\frac{1}{2}+\delta_1)(1-\rho)\mathsf{LCS}(x,y)\unknown(\frac{1}{2}+\delta)\mathsf{LCS}(x,y)\).

**Subcase 2b.** \(1(x)\unknown(\frac{1}{2}-\rho)|x|\)**.** In this case, Lemma 6.1 with parameter \(\rho\) finds a common subsequence of length at least \((\frac{1}{2}+\delta)\mathsf{LCS}(x,y)\).

<sup>2</sup>There are several minor differences between this statement and the statement in \[AW21\]. First, the statement in \[AW21\] says subquadratic time but it actually runs in linear time, similar to the analogous algorithm in \[RS20\] who proved Lemma 6.1 for equal-length strings. This was confirmed in private communication with the authors. Second, \[AW21\] prove the statement when 0(_x_) and 1(_y_) are within \(\varepsilon|x|\) of each other for some |_x_|, while we only consider when they are equal.

