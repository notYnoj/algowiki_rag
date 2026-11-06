By Cauchy-Schwarz inequality,

\(|P+H|=\sum_z[r_{P+H}(z)>0]\ge\frac{(\sum_zr_{P+H}(z))^2}{\sum_zr_{P+H}(z)^2}\ge\frac{|P|^2|H|^2}{O(|P||H|)}\ge\Omega(|P||H|).\)

As \(|H+H|\ge|P+H|\), the doubling constant of _H_ is at least \(\Omega(|P|)=\Omega(n^{c/(k-1)})\), which is greater than \(n^\epsilon\) when \(k\checkmark\frac{c}{\epsilon}\).

## 3.2 Existential Proof

It is more convenient to re-express having popular sums in terms of the higher-order energy _T<sub>k</sub>(A_). \[Shk14\]. The proof relies on the following lemma:

**Lemma 3.4.** _For every_ \(\epsilon,c>0\)_, there is some_ \(k=k(c,\epsilon)\) _such that the following holds. Let_ \(A\subseteq\mathbb{Z}\) _be such that_ \(T_k(A)\ge\Omega(|A|^{2k-1-c})\)_. Then there exists a set_ \(H\subseteq\mathbb{Z}\) _and some_ \(K=O_{c,\epsilon}(|A|^\epsilon)\) _such that:_

• \(|H|\le K|A|^{1+c}\),<tbc>

• \(|H+H|\le K|H|\),<tbc>

• \(|A\cap H|\ge|A|/K\).

Let us postpone the proof of Lemma 3.4 for the moment, and first see how Theorem 1.2 can be concluded from the lemma.

**Proof of Theorem 1.2.** Let \(k=k(\epsilon,c)\) be chosen as in Lemma 3.4. Let _A_ be a set with a _p_-popular 2_k_-sum _z_ for some \(p=\Omega(|A|^{2k-1-c})\). Let \(A^*=\pm(A\cup\{z\})\), then \(T_k(A^*)\ge p\) (as each solution \(a_1+\cdots+a_{2k}=z\) in _A_ can be mapped to a unique solution \(a_1+\cdots+a_k=b_1+\cdots+b_k\) in _A_<sup>∗</sup>). Apply Lemma 3.4 to _A_<sup>∗</sup>. This yields a set _H_<sup>∗</sup> satisfying the first two properties for some \(K=O_{c,\epsilon}(|A|^\epsilon)\) and that \(|A^*\cap H^*|\ge|A^*|/K\). As _A_<sup>∗</sup> can be seen of the union of four copies of _A_, possibly translated or negated, one such copy is covered by _H_<sup>∗</sup> in at least |_A|/_4_K_ elements. Thus, by possibly translating and negating _H_<sup>∗</sup> (leaving the first two properties unaffected), one obtains the claimed set _H_.

**Proof of Lemma 3.4.** We determine \(k=k(c,\epsilon)\) later. If \(T_{k-1}(A)\ge|A|^{2(k-1)-1-c+\delta}\) for \(\delta:=2c/k\), then we instead apply this lemma inductively for _k_-1. This recursive process continues for less than _k_ steps before reaching a contradiction, and thus never reaches a base case. Instead, at some inductive call we must be in the opposite case that \(T_{k-1}(A)\le|A|^{2(k-1)-1-c+\delta}\).

For _D_ a power of 2, let \(P_D\subseteq(k-1)A\) be the subset of (_k_-1)-sums with multiplicity in the range \[_D,_2_D_\], i.e.,<tbc>

\(P_D=\{x\in\mathbb{Z}:D\le|\{(a_1,\dots,a_k)\in A^k:a_1+\cdots+a_k=z\}|<2D\}.\)

