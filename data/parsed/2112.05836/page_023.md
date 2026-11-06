characters _c<sub>i</sub>_, or try to line up the % characters. If we line up the % characters, the edit distance is _ky_. If we line up the _c<sub>i</sub>_ characters and they all match \((c_i=c_j\forall i,j)\), the edit distance is _xk_<sup>2</sup>/4 if _k_ is even and _x(k_<sup>2</sup>-1)/4 if _k_ is odd. If the characters don’t match the edit distance is at least _xk_<sup>2</sup>/4+_y_ if _k_ is even and _x(k_<sup>2</sup>-1)/4+_y_ if _k_ is odd. Consider the case of _k_ even, we can choose integer values of _x_ and _y_ such that \(xk^2/4<yk\le xk^2/4+y\). By doing so, if all the characters match, then the median _k_-edit distance is _xk_<sup>2</sup>/4, otherwise it is _yk_. In some sense this gadget is causing characters to act like they do in _k_-LCS, where only a match across all strings gives us a benefit. Using these selector gadgets and ideas from the edit distance and LCS lower bounds, we get a lower bounds for both median _k_-edit distance and center _k_-edit distance from SETH.

**Theorem 6.5.** _If the_ \(k'\)_-OV hypothesis is true for all constants_ \(k'\)_, then for all constant_ \(\epsilon\in(0,1]\) _grammar-compressed k-median edit distance requires_ \(\left(M^{k-1}m\right)^{1-o(1)}\) _time when the alphabet size is_ \(|\Sigma|=\Theta(k)\) _and_ \(m=M^{\epsilon\pm o(1)}\)_. Here, M and m denote the total uncompressed and compressed length of the k input strings respectively._

The lower bound for median _k_-edit distance immediately implies a lower bound for center _k_-edit distance following \[HBGT20\].

**Reminder of Theorem 6.29 .** _We are given k strings of length M with a SLP of size m. The center k-edit distance problem on these strings requires_ \(\left(M^{k-1}m\right)^{1-o(1)}\) _time if SETH is true._

Given these lower bounds for the case of compressed _k_-LCS, median _k_-edit distance and center _k_-edit distance, we want to consider not just compression but also approximation.

## 6.2 Lower Bound with LCS

In this section we will argue that if we have _k_ strings each of length _M_ and they have a SLP compression of size _m_ then the problem requires _M_<sup>_k_-1-_o_(1)</sup>_m_<sup>1-_o_(1)</sup> if SETH is true. In the next section we use these hardness results for _k_-LCS to prove hardness for \(k'\)-Edit Distance.

The core of this section is building a generalized "perfect alignment" gadget. This is a gadget that causes substrings to be aligned with no skips or merges. We use this generalized alignment gadget to generalize the work of \[ABBK17\]. The main idea for this perfect alignment gadget is that between every string we want to align, we add symbols $<sub>1</sub>$<sub>2</sub>_..._$_<sub>k</sub>_. Additionally, at the end of each string _S<sub>i</sub>_ in our gadget, we add many copies of these characters, excepting $_<sub>i</sub>_. That is, we add $<sub>1</sub>_..._$<sub>_i_-1</sub>$<sub>_i_+1</sub>_..._$_<sub>k</sub>_. Via this construction, any valid perfect alignment will match all available copies of $_<sub>i</sub>_ for all _i_. Any alignment that isn’t perfect (for example it skips matching some sub-string in the middle of _S<sub>i</sub>_) will miss out on one of these $_<sub>i</sub>_ characters in _S<sub>i</sub>_, thus lowering the value of a potential _k_-LCS.

Recall that LCS(_S_<sub>1</sub>_,...,S<sub>k</sub>_) is a function that returns the _k_-LCS of the strings _S_<sub>1</sub>_,...,S<sub>k</sub>_. Recall that \(\delta_D(S_1,\dots,S_k)=\sum_{i\in[1,k]}(S_i-\text{LCS}(S_1,\dots,S_k))\). That is, the count of all unmatched characters.

## 6.3 Representations of Many Lists at Once

The key idea is going to be different ways to represent many lists of OV instances at once. This representation comes from \[ABBK17\].

**Definition 6.6.** Let _L_ be the list of vectors to a _k_-OV instance. Let |_L_|=_n_.

The list representation of \(\ell\) copies of _L_ is made up of \(n^\ell\) vectors \(\vec{v}=\text{\textbf{List}}_\ell(L)[j_1][j_2]\dots[j_\ell]\).<tbc>

\(\text{\textbf{List}}(L)_\ell[j_1][j_2]\dots[j_\ell][i]=\vec{v}[i]=L[j_1][i]\cdot L[j_2][i]\cdots L[j_\ell][i]\)

<tbc>As a convenience of notation we will allow indexing with a single index into **List**(_L_):

\(\text{\textbf{List}}(L)_\ell\left[\sum_{i=1}^\ell j_in^{i-1}\right]=\text{\textbf{List}}(L)_\ell[j_1][j_2]\dots[j_\ell]\)

When writing down this list of vectors into a string there are two ways to do it. The serial way of writing out each vector in order, or the interleaving way. The serial way of writing vectors is in many ways easier to use for gadgets. However, the interleaved version is easier to compress. We will describe both and use both in our gadgets.

