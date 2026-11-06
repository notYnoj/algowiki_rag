<tbc>_Proof._ (i) Assume _T_ has the subtree in Fig.7(a) (the other case is symmetric). By Lemma 9(i) (applied to the subtree of (a) with root \(\langle v\prec K_b\rangle\)), replacing subtree (a) by subtree (b) gives a correct tree. Then, by Lemma 8(i) (applied to subtree (b), but note that node \(\langle v\prec K_c\rangle\) in (b) takes the role of node \(\langle v\prec K_b\rangle\) in Fig.3(a)!) replacing (b) by (c) gives a correct tree. This proves part (i). Part (ii) follows because replacing (a) by (c) changes the cost of _T_ by \(\omega(K_a)-\omega(T_1)\), and _T_ has minimum cost, so \(\omega(K_a)\ge\omega(T_1)\). \(\square\)

**Lemma 11 (implies Lemma 4).** _If T has a subtree as in Fig.9(a), then_ **(i)** _replacing that subtree by the one in Fig.9(c) preserves correctness, and_ **(ii)** \(\omega(T_0)\ge\omega(T_{10})\).

_Proof._ Applying Lemma 9(i) to the subtree of (a) with root \(\langle v\prec K_c\rangle\), replacing subtree (a) by subtree (b) gives a correct tree.<sup>9</sup> Then, applying Lemma 9(i) to the subtree of (b) with root \(\langle v\prec K_b\rangle\), replacing subtree (b) by subtree (c) gives a correct tree. This shows part (i). Part (ii) follows, because replacing (a) by (c) changes the cost of _T_ by \(\omega(T_0)-\omega(T_{10})\), so \(\omega(T_0)\ge\omega(T_{10})\). \(\square\)

<sup>9</sup> Technically, to apply Lemma 9(i), we need (b) to be correct and _irreducible_. The overall argument remains valid though as long as the tree from Fig.9(a) is optimal.

