We now prove Lemma 8.5 which provides a lower bound on the expected size of the longest common subsequence of two random blocks of \(U'\) and \(\overline{U'}\).

Lemma 8.5. _The expected size of the longest common subsequence of two randomly selected blocks of_ \(U'\) _and_ \(\overline{U'}\) _is_ \(\Omega(n^{(1/2-26\delta-4\zeta-\eta)/3})\).

As mentioned in Section 4, to prove Lemma 8.5, we use two well-known theorems, one in the context of order theory and the other in the graph theory. Here we present these two theorems and use them to prove Lemma 8.5. We begin by Dilworth’s theorem. Before we state the theorem, we need some basic definitions.

A partially ordered set (poset) _P_ is consisted of a ground set _X_ and a partial order \(\unknown\) that satisfies the following conditions:

• (reflexive) \(a\unknown a\) for all \(a\in X\).<tbc>

• (assymetricity) If \(a\unknown b\) and \(b\unknown a\), then we have _a=b_.<tbc>

• (transitivity) If \(a\unknown b\) and \(b\unknown c\), then we have \(a\unknown c\).

A chain of length _k_ is defined as a sequence _a_<sub>1</sub>_,a_<sub>2</sub>_,...,a<sub>k</sub>_ of elements in _X_, such that \(a_1\unknown a_2\unknown\dots\unknown a_k\). An antichain of size _k_ is defined as a set {_a_<sub>1</sub>_,a_<sub>2</sub>_,...,a<sub>k</sub>_}, where for every \(i,j\in[k]\), _a<sub>i</sub>_ and _a<sub>j</sub>_ are incomparable, i.e., neither \(a_i\unknown a_j\) nor \(a_j\unknown a_i\) holds. A chain decomposition of _X_ is a partition of the elements of _X_ into disjoint chains.

Theorem (Dilworth-1950 \[17\]). _Let_ \(\ell\) _be the size of the maximum antichain in poset P. Then, P can be decomposed into_ \(\ell\) _chains._

Here, we use the dual form of this theorem, which is proved by Mirsky in 1971 \[26\].

Theorem 1. (dual of Dilworth \[26\]) _Let_ \(\ell\) _be the size of the maximum chain in poset P. Then, P can be decomposed into_ \(\ell\) _disjoint antichains._

Now, let \(\pi\) and \(\overline{\pi}\) be two permutations of the characters in \(\Sigma\). According to \(\pi\) and \(\overline{\pi}\), we define a poset _P_ as follows: the ground set is \(\Sigma\), and for two symbols \(c_1,c_2\in\Sigma\), we have \(c_1\unknown c_2\), if and only if _c_<sub>1</sub> appears before _c_<sub>2</sub> in both \(\pi\) and \(\overline{\pi}\). It is easy to observe that any chain in _P_ is corresponding to a common subsequence of \(\pi\) and \(\overline{\pi}\). Therefore, we can restate the dual form of Dilworth’s theorem as follows.

Theorem 8.1. (Dilworth-restated) _Given two strings_ \(\pi\) _and_ \(\overline{\pi}\)_, each of which is a permutation of the symbols in_ \(\Sigma\)_, where_ \(|\Sigma|=m\) _. If_ \(|lcs(\pi,\overline{\pi})|=x\)_, then_ \(\overline{\pi}\) _can be decomposed into x substrings, such that the characters in each of these strings appear exactly in the reverse order as appeared in_ \(\pi\)_, i.e., the longest common subsequence of each of these substrings and_ \(\pi\) _is_ 1.

We use a nontrivial consequence of Theorem 8.1 which we state in Lemma 8.6.

Lemma 8.6. _Let_ \(\pi_1,\pi_2,\pi_3\) _be three permutations of the symbols in_ \(\Sigma\) _where_ \(|\Sigma|=m\)_. Then,_<tbc>

\(|lcs(\pi_1,\pi_2)|\cdot|lcs(\pi_2,\pi_3)|\cdot|lcs(\pi_3,\pi_1)|\ge m.\)

