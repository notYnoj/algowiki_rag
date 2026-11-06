<tbc>**Lemma 8 (implies Lemma 2).** _Assume T has a subtree as in Fig.3(a) with nodes_ \(\langle v=K_a\rangle\) _and_ \(\langle v\prec K_b\rangle\). **(i)** _Replacing that subtree the one in Fig.3(b) (if_ \(K_a\prec K_b\)_) or the one in Fig.3(c) (if_ \(K_a\unknown\unknown K_b\)_) preserves correctness. **(ii)** If_ \(K_a\prec K_b\)_, then_ \(\omega(K_a)\ge\omega(T_1)\)_; otherwise_ \(\omega(K_a)\ge\omega(T_0)\).

_Proof._ Assume that \(K_a\prec K_b\) (the other case is symmetric). By inspection of each case (_Q=K<sub>a</sub>_ or \(Q\neq K_a\)), subtree (b) classifies each query _Q_ the same way subtree (a) does, so the modified tree is correct. The modification changes the cost by \(\omega(K_a)-\omega(T_1)\), so (since _T_ has minimum cost) \(\omega(K_a)\ge\omega(T_1)\). □

**Lemma 9 (implies Lemma 3(i)). (i)** _If T has either of the two subtrees in Fig.7(a) or (c), then exchanging one for the other preserves correctness. **(ii)** If T has the subtree in Fig.7(a), then_ \(\omega(T_0)\ge\omega(T_{11})\).

_Proof. Part (i)._ The transformation from (a) to (c) is a standard rotation operation on binary search trees, but, since the comparison operators can be either \(<\) or \(\le\) in our context, we verify correctness carefully.

By inspection, replacing subtree (a) by subtree (b) (in Fig.7) gives a tree that classifies all queries as _T_ does, and so is correct.

Next we observe that, in subtree (b), replacing the right subtree by just _T_<sub>11</sub> (to obtain subtree (c)), maintains correctness. Indeed, since _T_ is irreducible, replacing (in (a)) the subtree _T_<sub>1</sub> by just _T_<sub>11</sub> would give an incorrect tree. Equivalently, \(\exists Q\). \(Q\unknown\unknown K_b\wedge Q\prec K_c\). Equivalently, the right-bounded interval \(\{Q\in\mathbb{R}:Q\prec K_c\}\) overlaps the left-bounded interval \(\{Q\in\mathbb{R}:Q\unknown\unknown K_b\}\). Equivalently, the complements of these intervals, namely \(\{Q\in\mathbb{R}:Q\unknown\unknown K_c\}\) and \(\{Q\in\mathbb{R}:Q\prec K_b\}\), are disjoint. Equivalently, \(\forall Q\). \(Q\unknown\unknown K_c\rightarrow Q\unknown\unknown K_b\). Hence, replacing the right subtree of (b) by _T_<sub>11</sub> (yielding (c)) maintains correctness.

In sum, replacing subtree (a) by subtree (c) maintains correctness. This shows part (i). This replacement changes the cost by \(\omega(T_0)-\omega(T_{11})\), so \(\omega(T_0)\ge\omega(T_{11})\). This proves part (iii). The proof of (ii) is symmetric to the proof of (i). □

**Lemma 10 (implies Lemma 3(ii)).** _If T has a subtree as in Fig.8(a), and_ \(K_a\unknown\unknown K_c\)_, then **(i)** replacing the subtree by Fig.8(c) preserves correctness, and **(ii)**_ \(\omega(K_a)\ge\omega(T_1)\).

