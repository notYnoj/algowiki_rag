<tbc>are unable to guarantee that \(\mathsf{LCS}(x_I,y_J)>(1/2+\gamma)|x_I|\) as we did for the other two types, but we can instead guarantee the weaker assumption that _I_ has a long subinterval \(I'\) for which \(\mathsf{LCS}(x_{I^\prime},y_J)>(1/2+\gamma)|x_{I^\prime}|\). Handling this technicality requires some care, but to get across the main ideas we ignore this detail for the rest of this sketch and imagine that all certified rectangles satisfy \(\mathsf{LCS}(x_I,y_J)>(1/2+\gamma)|x_I|\).

We also certify using the trivial algorithm a weaker set of "default" rectangles \(I\times J\) where \(\mathsf{Trivial}(I,J)\ge(1/2-\gamma^4)|I|\) (the constants are chosen for illustration). These rectangles exist all over the place and are used in the DP to fill in the gaps between the efficient ones above. We may assume \(\mathsf{LCS}(x,y)\ge(1-\delta)|x|\) -- or else the trivial matching, which is always |_x_|/2 by the setup of Theorem 3.2, gets a \((\frac{1+\delta}{2})\)-approximation -- and this assumption guarantees we can certify many good rectangles and many default rectangles. We show that while most of the \(\kappa(I\times J)\) are \((1/2-\gamma^4)|I|\) coming from the default rectangles, a significant enough fraction of them are \((1/2+\gamma)|I|\) that for the final answer we get \(\mathsf{DP}[|x|][|y|]>(1/2+\delta)|x|\).

Since we are going for an almost-linear time algorithm (and not just subquadratic), we need to be careful to certify the rectangles quickly. Note that, naively, there are roughly \((\frac{|y|}{\theta w})^2\sim\widetilde{\Theta}(\frac{|y|}{|x|})^2\) possible _J_-intervals. If _y_ is much longer than _x_ (say |_y_|=|_x_|<sup>3</sup>), then we cannot simply try to certify every rectangle, or else the runtime is super-linear in the input size, even if we can certify rectangles in constant time. Instead, we restrict ourselves to certifying rectangles \(I\times J\) where _J_ is "minimal". That is, for each _x_-interval _I_ and each end(_J_), we look for the minimal _J_ where we can certify \(\kappa(I\times J)\ge(1/2+\gamma)|I|\). We can find such _J_ by binary search (the ability to binary search depends on a technical property of the algorithmic structure lemma), so that the number of rectangles we are checking is now only \(\widetilde{O}(\frac{|y|}{|x|})\), rather than \(\widetilde{O}(\frac{|y|}{|x|})^2\).

## 4 Algorithmic Structure Lemma

We now state and prove our algorithmic structure lemma. We note that the final algorithm uses this lemma as a black-box, and can be understood without the proof of this lemma. The interested reader can skip to Section 5 after Section 4.1.

### 4.1 Algorithm Structure Lemma Statement

The following is the key technical lemma. It is inspired by and builds upon the "Structure Lemma" of \[GHL22\], which was used to prove new deletion code bounds.

**Lemma 4.1** (Algorithm Structure Lemma)**.** _There exists an absolute constant_ \(\delta_{code}>0\) _such that for all sufficiently large w, there exists_ \(T\le 2\mathrm{log}w\) _and_ 2_T string properties P_<sub>1</sub>_,...,P<sub>T</sub>,Q_<sub>1</sub>_,...,Q<sub>T</sub> such that:_

1. _If string x has length w, then there exists a_ \(t\in[T]\) _such that x has property P<sub>t</sub>._<tbc>

2. _If_ \(\mathsf{LCS}(x,y)\ge(1-\delta_{code})|x|\) _and x has property P<sub>t</sub>, then y (not necessarily of length w) has property Q<sub>t</sub>._<tbc>

3. _Property Q<sub>t</sub> is hereditary, meaning that if y has Q<sub>t</sub> and y is a subsequence of_ \(y'\)_, then_ \(y'\) _has Q<sub>t</sub>._<tbc>

_4._ _For every_ \(t\in[T]\)_, and strings x and y, we can test if x satisfies P<sub>t</sub> in time O(w_log_w). We can also preprocess the string y in time O_(|_y_|log|_y_|)_, such that we can answer queries of the form "does_ \(y'\) _satisfy Q<sub>t</sub>," for substrings_ \(y'\) _of y, in O(w_) _time._<tbc>

_5._ _If string x has length w and property P<sub>t</sub> and string y has property Q<sub>t</sub>, then there exists an interval_ \(I\subset[w]\) _such that_ \(\mathsf{LCS}(x_I,y)\ge\frac{|I|}{2}+\delta_{code}w\)_. Furthermore, given x and t, the interval I and the promised common subsequence of x<sub>I</sub> and y can be chosen independent of y, and both can be found in time O(w_log_w)._<tbc>

