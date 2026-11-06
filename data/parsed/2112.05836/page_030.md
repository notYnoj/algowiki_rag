## Case 2 \[There is 1 "good" _k_-tuple, upper bound\]:

If there is a singular "good" _k_-tuple we can not re-arrange the strings to get a larger alignment. If we skip or merge any strings in _Y_ we loose \(2\ell\) symbols from _B_ at least, giving a maximum LCS of \(D-2\ell\). If we skip or merge strings in _X<sub>i</sub>_ then we loose at least \(2\ell\) symbols from $_<sub>i</sub>_ characters. We gain at most \(\ell\) matches, giving a maximum LCS if we merge or skip of \(D-\ell\). Thus, the largest LCS possible is _D_.

## Case 3 \[There are zero "good" _k_-tuples, upper bound\]:

In this case, if we follow a perfect alignment we achieve an LCS of \(2\ell m+2\ell(m+(k-1)n)+zm=D-1\). If we skip a string in _Y_ we miss out on \(2\ell\) characters. If we match a single string in _Y_ to multiple strings in _X<sub>i</sub>_ we loose at least \(2\ell\) characters and match an additional \(\ell\) characters at most for a total LCS of at most \(D-\ell\). Finally, if we skip over strings in _X<sub>i</sub>_, we miss out on \(2\ell\) characters $_<sub>i</sub>_, for no benefit. All _k_-tuples have a value of _z_ regardless, so the maximum LCS is \(D-2\ell\).

From all these cases we can say that if there is exactly one "good" _k_-tuple, and it is reachable in a perfect alignment then

\(\mathrm{LCS}(SAG_1(X_1),SAG_2(X_2),\dots,SAG_{k-1}(X_{k-1}),SAG_y(Y))=D.\)

If there are no "good" _k_-tuples

\(\mathrm{LCS}(SAG_1(X_1),SAG_2(X_2),\dots,SAG_{k-1}(X_{k-1}),SAG_y(Y))=D-1.\)

For the compression, \(D<\ell n\). So we add an additional \(\mathrm{lg}(n)+\mathrm{lg}(\ell)\). So if _c_ is the size of an SLP that gives a single variable for all (_k_-1)_n+m_ strings _X<sub>i</sub>_\[_j_\] and _Y_\[_j_\]. Then there is a SLP representation of all the strings _AG_<sub>1</sub>(_X_<sub>1</sub>)_,...,AG_<sub>_k_-1</sub>(_X_<sub>_k_-1</sub>)_,AG<sub>y</sub>(Y_) of size \(O(c+\mathrm{lg}(\ell)k+\mathrm{lg}(n)+kn+m)\). Unchanged.

## 6.5.2 Zero and One Strings

First we will use the gadgets for representing zeros and ones from \[ABV15\].

**Lemma 6.13** (Zero and One Strings \[ABV15\])**.** _There are strings CG<sub>i</sub>_(0)_,CG<sub>i</sub>_(1) _such that:_

\(k-LCS(CG_1(b_1),\dots,CG_k(b_k))=\left\{\begin{array}{ c c }
C & \text{\textit{if}}b_1\cdots b_k=0 \\
C+1 & \text{\textit{if}}\forall b_1\cdots b_k=1
\end{array}\right.\)

_for some positive integer C that is a function of k. Note this corresponds to our desired relationship from k-OV. If we have one "zero string" then we get a small k-LCS, if there are all "one strings" then we get a larger k-LCS. These strings use an alphabet of size O_(1)_. If k is a constant the length of these strings is O_(1).

## 6.5.3 Interleave Gadget

Now we will build the gadget that checks if our interleave representations represent a yes instance of orthogonal vectors. For this next Lemma recall Definition 6.8, where we define \(\mathbf{Vec}\mathbf{S}_{\mathbf{I}\ell}(L,v_i)\).

**Lemma 6.14.** _Let L be a list of n_ {0,1} _vectors each of dimension d=n_<sup>_o_(1)</sup>_. Let v_<sub>1</sub>_,...,v<sub>k</sub> be_ {0,1} _vectors each of dimension d. Given the lists, We produce strings:_ \(IVG_1(L,\ell,v_1),\dots,IVG_{k-1}(L,\ell,v_{k-1})\)_, and EIVG(v<sub>k</sub>_) _such that_<tbc>

\(\mathrm{LCS}(IVG_1(L,\ell,v_1),\dots,IVG_{k-1}(L,\ell,v_{k-1}),EIVG(v_k))=C\)

<tbc>_if there are_ \((k-1)\ell\) _vectors in L such that are orthogonal with v_<sub>1</sub>_,...,v<sub>k</sub>. If there do not exist_ \((k-1)\ell\) _vectors in L that are orthogonal with v_<sub>1</sub>_,...,v<sub>k</sub> then_

\(\mathrm{LCS}(IVG_1(L,\ell,v_1),\dots,IVG_{k-1}(L,\ell,v_{k-1}),EIVG(v_k))=C-1.\)

_These strings have length at most_ \(O(n^\ell d)\) _and an alphabet of size O(k)._

_Additionally we can compress x strings_ \(IVG_i(L,\ell,v_1),\dots,IVG_i(L,\ell,v_x)\) _or_ \(EIVG(v_1),\dots,EIVG(v_x)\) _with a total compression size of_ \(O(xd+nd+\ell\mathrm{lg}(n))\).

