## 4.4 Proof of the Algorithmic Structure Lemma

_Proof of Lemma 4.1._ Let \(\delta_{code}=\varepsilon^4/2\). We define the properties _P<sub>t</sub>_ and _Q<sub>t</sub>_ based on the types in Definition 4.5. For convenience, we index them not as _P_<sub>1</sub>_,P_<sub>2</sub>_,...,P<sub>T</sub>_, but rather as \(P_{\ell,0},P_{\ell,1},P_\ell\) for \(\ell\le w\) a power of 2, for a total of roughly _T_∼3log_w_ properties.

• If \(\ell\ge\varepsilon^2w\) and \(b\in\{0,1\}\), then \(P_{\ell,b}\) is the property that _x_ is \(\ell\)-coarse, and its imbalanced interval of length \(\ell\) is imbalanced in the direction of _b_-bits (i.e. has more _b_’s than <o>_b_</o>’s).<tbc>

• If \(\ell\ge\varepsilon^2w\) and \(b\in\{0,1\}\), then \(Q_{\ell,b}\) is the property that _y_ has at least \(\big(\frac{1+\varepsilon^2}{2}\big)\ell b\)-bits.<tbc>

• If \(\ell<\varepsilon^2w\), then \(P_\ell\) is the property that _x_ is \(\ell\)-fine.<tbc>

• If \(\ell<\varepsilon^2w\), then \(Q_\ell\) is the property that _y_ contains \(y_\ell=(0^\ell 1^\ell)^{\varepsilon w/(5\ell)}\) as a subsequence.

We now verify the conditions of Lemma 4.1.

1. _For every length-w string x, there exists a t such that x has property P<sub>t</sub>._<br>
This follows immediately from Lemma 4.4.<tbc>

2. _If_ \(\mathsf{LCS}(x,y)\ge(1-\delta_{code})|x|\) _and x has property P<sub>t</sub>, then y has property Q<sub>t</sub>._<br>
First suppose \(\ell\ge\varepsilon^2w\), \(b\in\{0,1\}\), and _x_ has property \(P_{\ell,b}\). Then _x_ has a substring _x<sub>I</sub>_ of length at least \(\varepsilon^2w\) with at least \((\frac{1}{2}+\varepsilon^2)\ell b\)-bits. The longest common subsequence of _x<sub>I</sub>_ and _y_ has at least \(|I|-\delta_{code}w\) of the bits of _x<sub>I</sub>_, so _y_ has at least \((\frac{1}{2}+\varepsilon^4)\ell-\delta_{code}w\ge(\frac{1+\varepsilon^4}{2})\ell b\)-bits, satisfying property \(Q_{\ell,b}\).<br>
If _x_ has property \(P_\ell\) for \(\ell<\varepsilon^2w\), _x_ is \(\ell\)-fine. By Lemma 4.6, _y_ has property \(Q_\ell\).<tbc>

3. _For every t, property Q<sub>t</sub> is hereditary, meaning that if y has Q<sub>t</sub> and y is a subsequence of_ \(y'\)_, then_ \(y'\) _has Q<sub>t</sub>._<br>
This follows from the definition of _Q<sub>t</sub>_ and that being a subsequence is a transitive relation.<tbc>

4. _For every t, property P<sub>t</sub> can be tested in time O(w_log_w), and property Q<sub>t</sub> can be tested in time O(w_) _on substrings of a string y, after O_(|_y_|log|_y_|) _preprocessing._<br>
Testing the _P<sub>t</sub>_’s can be done in _O(w_log_w_) because, after _O(w_) preprocessing by storing all prefix sums, we can check whether any particular index is an \(\ell\)-flag or not in _O_(1) time, and for any particular property _P<sub>t</sub>_, we need to check at most _O(w_log_w_) flags.<br>
To test _Q<sub>t</sub>_, first note that if we are working with a coarse property \(Q_{\ell,b}\), this can be tested in _O_(1) time after preprocessing prefix sums. To test a fine property \(Q_\ell\), preprocess the string _y_ as follows: for every index \(j\in\{0,1,\dots,|y|\}\) and bit \(b\in\{0,1\}\), compute \(\mathsf{next}_{b,\ell}(j)\), the smallest index \(j'\) such that the substring \(y_{[j,j^\prime]}\) has at least \(\ell\) bits equal to _b_. For any _j_ and _b_, \(\mathsf{next}_{b,\ell}(j)\) can be computed by a binary search in log(|_y_|) time, so the preprocessing takes time _O_(|_y_|log|_y_|). Now property _Q<sub>t</sub>_ can be tested on a substring _y<sub>J</sub>_ in _O(w_) time by evaluating \(\mathsf{next}_{1,\ell}(\mathsf{next}_{0,\ell}(\cdots\mathsf{next}_{1,\ell}(\mathsf{next}_{0,\ell}(\mathsf{start}J))\cdots))\), where there are \(\varepsilon w/(5\ell)\) calls to each of \(\mathsf{next}_{0,\ell}\) and \(\mathsf{next}_{1,\ell}\), and checking if the result is at most end _J_.<tbc>

5. _If x has property P<sub>t</sub>,_ |_x_|=_w, and y has property Q<sub>t</sub>, then there exists an interval_ \(I\subset[w]\) _such that_ \(\mathsf{LCS}(x_I,y)\ge\frac{|I|}{2}+\delta_{code}w\)_. Furthermore, given x and t, the interval I and the promised common subsequence of x<sub>I</sub> and y can be chosen independent of y, and both can be found in time O(w_log_w)._<br>
First suppose _x_ has property \(P_{\ell,b}\) and _y_ has property \(Q_{\ell,b}\) for \(\ell\ge\varepsilon^2w\) and \(b\in\{0,1\}\). Then _x_ has a substring _x<sub>I</sub>_ of length \(\ell\) with at least \((\frac{1}{2}+\varepsilon^2)\ell b\)-bits and _y_ has at least \((\frac{1+\varepsilon^2}{2})\ell b\)-bits, so<tbc>

