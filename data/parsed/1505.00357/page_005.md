<tbc>**Assumption 1 (i)** _All nodes on the path from_ \(\langle v=K_a\rangle\) _to_ \(\langle v=K_z\rangle\) _do inequality comparisons. (ii) Along the path, some other node_ \(\langle v\prec K_s\rangle\) separates _key K<sub>a</sub> from K<sub>z</sub>: either_ \(K_a\prec K_s\) _but_ \(K_z\unknown\prec K_s\)_, or_ \(K_z\prec K_s\) _but_ \(K_a\unknown\prec K_s\).

It suffices to prove the lemma assuming (i) and (ii) above. (Indeed, if the lemma holds given (i), then, by transitivity, the lemma holds in general. Given (i), if (ii) doesn’t hold, then exchanging the two nodes preserves correctness, changing the cost by \((\omega(K_a)-\omega(K_z))\times d\) for \(d\ge 1\), so \(\omega(K_a)\ge\omega(K_z)\) and we are done.)

By Assumption 1, the subtree rooted at \(\langle v=K_a\rangle\), call it \(T'\), is as in Fig.3(a):

Let child \(\langle v\prec K_b\rangle\), with subtrees _T_<sub>0</sub> and _T_<sub>1</sub>, be as in Fig. 3.

**Lemma 2.** _If_ \(K_a\prec K_b\)_, then_ \(\omega(K_a)\ge\omega(T_1)\)_, else_ \(\omega(K_a)\ge\omega(T_0)\).

(This and subsequent lemmas in this section are proved in Appendix 7.2. The idea behind this one is that correctness is preserved by replacing \(T'\) by subtree (b) if \(K_a\prec K_b\) or (c) otherwise, implying the lemma by the optimality of _T_.)

<u>Case 1</u>: _Child_ \(\langle v\prec K_b\rangle\) _separates K<sub>a</sub> from K<sub>z</sub>._ If \(K_a\prec K_b\), then \(K_z\unknown\prec K_b\), so descendant \(\langle v=K_z\rangle\) is in _T_<sub>1</sub>, and, by this and Lemma 2, \(\omega(K_a)\ge\omega(T_1)\ge\omega(K_z)\), and we’re done. Otherwise \(K_a\unknown\prec K_b\), so \(K_z\prec K_b\), so descendant \(\langle v=K_z\rangle\) is in _T_<sub>0</sub>, and, by this and Lemma 2, \(\omega(K_a)\ge\omega(T_0)\ge\omega(K_z)\), and we’re done.

<u>Case 2</u>: _Child_ \(\langle v\prec K_b\rangle\) _does not separate K<sub>a</sub> from K<sub>z</sub>._ Assume also that descendant \(\langle v=K_z\rangle\) is in _T_<sub>1</sub>. (If descendant \(\langle v=K_z\rangle\) is in _T_<sub>0</sub>, the proof is symmetric, exchanging the roles of _T_<sub>0</sub> and _T_<sub>1</sub>.) Since descendant \(\langle v=K_z\rangle\) is in _T_<sub>1</sub>, and child \(\langle v\prec K_b\rangle\) does not separate _K<sub>a</sub>_ from _K<sub>z</sub>_, we have \(K_a\unknown\prec K_b\) and two facts:

_Fact A:_ \(\omega(K_a)\ge\omega(T_0)\) (by Lemma 2), and

_Fact B:_ the root of _T_<sub>1</sub> does an inequality comparison (by Assumption 1).

By Fact B, subtree \(T'\) rooted at \(\langle v=K_a\rangle\) is as in Fig.4(a):

As in Fig. 4(a), let the root of _T_<sub>1</sub> be \(\langle v\prec K_c\rangle\), with subtrees _T_<sub>10</sub> and _T_<sub>11</sub>.

**Lemma 3.** _(i)_ \(\omega(T_0)\ge\omega(T_{11})\)_. (ii) If_ \(K_a\unknown\prec K_c\)_, then_ \(\omega(K_a)\ge\omega(T_1)\).

(As replacing \(T'\) by (b) or (c) preserves correctness; proof in Appendix 7.2.)

<u>Case 2.1</u>: \(K_a\unknown\prec K_c\). By Lemma 3(ii), \(\omega(K_a)\ge\omega(T_1)\). Descendant \(\langle v=K_z\rangle\) is in _T_<sub>1</sub>, so \(\omega(T_1)\ge\omega(K_z)\). Transitively, \(\omega(K_a)\ge\omega(K_z)\), and we are done.

(a)
(b)
(c)
v = K a
v K b
v K b
y
y
n
n
n
K a
v K b
v = K a
T
T
v = K a
y
n
y
n
n
n
T
T
K a
T
K a
T
T
1
T
1

**Fig.3.** (a) The subtree \(T'\) rooted at \(\langle v=K_a\rangle\) and possible replacements (b), (c).

