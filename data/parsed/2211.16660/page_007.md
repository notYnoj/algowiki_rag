**Remark 4.2.** In item 5, it is easy to see that, if \(\gamma\le\delta_{code}/10\), we may additionally assume (by starting with \(\delta'_{code}=\delta_{code}/2\)) that the interval _I_ is \(\gamma w\)-aligned by taking \(I':=\text{round}_{\gamma w}(I)\). We do so in the application in Section 5.

We now provide some more intuition for Lemma 4.1. First, we describe the properties _P<sub>t</sub>_ and _Q<sub>t</sub>_ that we actually use (based on Definition 3.1). For convenience, to define the properties, we index them as \(P_{\ell,0},P_{\ell,1},P_\ell\) for \(\ell\le w\) a power of 2, for a total of roughly _T_∼3log_w_ properties.

• If \(\ell\ge\varepsilon^2w\) and \(b\in\{0,1\}\), then \(P_{\ell,b}\) is the property that _x_ is \(\ell\)-coarse, and its imbalanced interval of length \(\ell\) is imbalanced in the direction of _b_-bits (i.e. has more _b_’s than \(\bar{b}\)’s).<tbc>

• If \(\ell\ge\varepsilon^2w\) and \(b\in\{0,1\}\), then \(Q_{\ell,b}\) is the property that _y_ has at least \(\big(\frac{1+\varepsilon^2}{2}\big)\ell b\)-bits.<tbc>

• If \(\ell<\varepsilon^2w\), then \(P_\ell\) is the property that _x_ is \(\ell\)-fine.<tbc>

• If \(\ell<\varepsilon^2w\), then \(Q_\ell\) is the property that _y_ contains \(y_\ell=(0^\ell 1^\ell)^{\varepsilon w/(5\ell)}\) as a subsequence.

The properties _P<sub>t</sub>_ are based on one of the key technical lemmas of the deletion codes bound \[GHL22\], a combinatorial structure lemma. This structure lemma roughly says that for strings of length _n_, there are properties \(\tilde{P}_1,\dots,\tilde{P}_T\) with \(T\le O(logn)\), such that

(i) any binary string of length _n_ has some property \(\tilde{P}_i\), and<tbc>

(ii) if two strings _x_ and _y_ have property \(\tilde{P}_i\), then _x_ and _y_ have (contiguous) substrings \(x'\) and \(y'\) of length \(\Omega(n)\) with \(\text{LCS}(x',y')\ge(\frac{1}{2}+\delta)(\frac{|x^\prime|+|y^\prime|}{2})\) (the real guarantee is stronger but more technical to state).

Theorem 1.3, the deletion codes lower bound, is proved (very roughly) by partitioning each string in _C_ into polylog_n_ substrings, finding by pigeonhole two strings _x_ and _y_ such that the types of the corresponding substrings of _x_ and _y_ agree, and using guarantee (ii) to find a \((\frac{1}{2}+\delta')w\) overall LCS.

Lemma 4.1 is a generalization of this combinatorial structure lemma that is "algorithmic" and "handles unequal length strings." The properties _P<sub>t</sub>_ that we choose in Lemma 4.1 are similar to the properties \(\tilde{P}_t\) of \[GHL22\], and it is not hard to check by inspection that the properties \(\tilde{P}_t\) of \[GHL22\] can be tested in linear time. The difficulty lies in finding properties _Q<sub>t</sub>_ of strings _y_ that (a) can be "inherited" from properties like \(\tilde{P}_t\) if _y_ has a subsequence covering most of _x_, (b) can be tested efficiently, and (c) still guarantee an LCS advantage between _x_ and _y_.

Because of Lemma 4.1, we can define the following algorithms, which we use in our final LCS algorithm.

**Definition 4.3.** For an integer _w_, let _P_<sub>1</sub>_,...,P<sub>T</sub>,Q_<sub>1</sub>_,...,Q<sub>T</sub>_ be the properties from Lemma 4.1. Let GetPType_<sub>w</sub>(x_) denote the smallest index _t_ such that _x_ has property _P<sub>t</sub>_. Let IsQType_<sub>w</sub>(x,t_) be true if _x_ has property _Q<sub>t</sub>_ and false otherwise. For _x_ satisfying _P<sub>t</sub>_ for some _t_, let Getl_<sub>w</sub>(x,t_) denote a \(\gamma w\)-aligned interval _I_ such that \(\text{LCS}(x_I,y)\ge\frac{|I|}{2}+\delta_{code}w\) for all _y_ satisfying _Q<sub>t</sub>_. Such an interval exists by Lemma 4.1 and Remark4.2.

By Lemma 4.1, GetPType_<sub>w</sub>(x_) can be computed in _O(w_log<sup>2</sup>_w_) time, since one can simply test each of the _O_(log_w_) properties _P<sub>t</sub>_. By Lemma 4.1, any string _y_ can be preprocessed in _O_(|_y_|log|_y_|) time such that, for any contiguous substring \(y'\) of _y_, \(\text{IsQType}_w(y',t)\) can be computed in _O(w_) time. Note that the input to GetPType_<sub>w</sub>_ must have length _w_, but the string input to IsQType_<sub>w</sub>_ can have arbitrary length. By Lemma 4.1, Getl_<sub>w</sub>(x,t_) can be computed in _O(w_log_w_) time.

## 4.2 Combinatorial structure lemma and types

In a string _x_, an \(\ell\)_-flag_ is an index _i_ such that between the _i_th one and the \((i+\ell)\)-th one, there are strictly more than \(10(\ell-1)\) zeros. An \(\ell^+\)_-flag_ is an index _i_ that is a _t_-flag for some \(t\ge\ell\), where _t_ must be a power<tbc>

