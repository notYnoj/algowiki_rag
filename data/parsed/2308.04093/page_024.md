\(a\in A^*\backslash J_{\le j}^+\subseteq(J_{j+1}^+\cup\cdots\cup J_k^+)\) (by Definition 3.5), so we must have \(|I_{\{w_a\}}\cap J_j^+|>x[\hat{i}]_{w_a}\), which means some item \(a'\in I_{\{w_a\}}\cap J_j^+\) is not included in the set \(Y\subseteq J_j^+\) that encodes \(x[\hat{i}]\). Hence, the _I_<sub>W<sub>1</sub></sub>-optimal partial solution \((\widetilde{A}^*,\widetilde{B}^*)\) in Eq. (19) contains _a_ but not \(a'\). Since \(\text{rank}(a')<\text{rank}(a)\) and \(w_{a^\prime}=w_a\), this violates the prefix property (Lemma 2.4) and hence contradicts the _I_<sub>W<sub>1</sub></sub>-optimality of \((\widetilde{A}^*,\widetilde{B}^*)\).<tbc>

• Case \(B^*\backslash J_{\le j-1}^-\unknown\subseteq I_{T^-[\hat{i}]}\):<tbc>

<tbc>By definition, \(T^-[\hat{i}]=S^-\big[z[\hat{i}]\big]=S^-[z'']\) where \(z''=W(A'')-W(B'')\). Note that the _I_<sub>W<sub>1</sub></sub>- optimal partial solution \((\widetilde{A}^*,\widetilde{B}^*)\) in Eq. (19) satisfies \(W(\widetilde{A}^*\cap J_{\le j-1}^+)-W(\widetilde{B}^*\cap J_{\le j-1}^-)=W(A'')-W(B'')=z''\), so by the assumption that _q_\[\] (with hints \(S^-[],S^+[]\)) is hinted- \((J_{\le j-1}^+\cup J_{\le j-1}^-)\)-optimal, we must have \(\widetilde{B}^*\backslash J_{\le j-1}^-\subseteq I_{S^-[z^{\prime\prime}]}\) by Definition 3.8 (Item 2). However, \(\widetilde{B}^*\backslash J_{\le j-1}^-=B^*\backslash J_{\le j-1}^-\unknown\subseteq I_{T^-[\hat{i}]}=I_{S^-[z^{\prime\prime}]}\), a contradiction.

Hence, we have verified that \(T^+[\hat{i}]\) and \(T^-[\hat{i}]\) satisfy Item 2 of Definition 3.8 for the DP table entry \(r[\hat{i}]\), so _r_\[\] (with hints _T_<sup>+</sup>\[\]_,T_<sup>-</sup>\[\]) is indeed a hinted-\((J_{\le j}^+\cup J_{\le j-1}^-)\)-optimal DP table. This finishes the proof of the correctness of our algorithm.

The time complexity of applying Theorem 3.11 is _O(L<sub>j</sub>b<sub>j</sub>_log<sup>2</sup>(_L<sub>j</sub>b<sub>j</sub>_)), and the time complexity of preprocessing functions \(Q_w(\cdot)\) is \(O(|J_j^+|+|\mathcal{W}_1|w_\mathrm{max}\mathrm{log}w_\mathrm{max})\). Since \(|\mathcal{W}_1|\le O((w_\mathrm{max}\mathrm{log}w_\mathrm{max})^{1/2})\) and \(L_jb_j=\Theta(w_\mathrm{max}^2\mathrm{log}w_\mathrm{max})\) (by Eqs. (12) and (13)), the total running time is \(O(L_jb_j\cdot\mathrm{log}^2(L_jb_j)+|J_j^+|)\).

## 4 Algorithm for HintedKnapsackExtend<sup>+</sup>

In this section we describe our algorithm for the HintedKnapsackExtend<sup>+</sup> problem (Problem 1), proving Theorem 3.11. In Lemma 4.1, we solve the special case where the hints are singleton sets. Then in Section 4.2, we provide several helper lemmas that allow us to decompose an instance into multiple instances with smaller hint sets. Finally in Section 4.3 we put the pieces together to solve the general case.

### 4.1 The base case with singleton hint sets

The following lemma is the most interesting building block of our algorithm for Problem 1.

**Lemma 4.1.** _HintedKnapsackExtend_<sup>+</sup> _(Problem 1) with_ \(|S[i]|\le 1\) _for all_ \(-L\le i\le L\) _can be solved deterministically in O(L_log_L) time._

_More precisely, the algorithm runs in O(L+L_<sub>1</sub>log_L) time, where_ \(L_1=\{-L\le i\le L:S[i]\neq\emptyset\}\).

The pseudocode of our algorithm for Lemma 4.1 is given in Algorithm 1. Here we first provide an overview. Algorithm 1 contains two stages:

• In the first stage, we enumerate \(w\in[w_\mathrm{max}]\) and _c_ (mod_w_), and collect indices \(j\equiv c(\mathrm{mod}w)\) such that \(w\in S[j]\). Then we try to extend from these collected indices _j_ by adding integer multiples of _w_ (which does not interfere with other congruence classes modulo _w_): using SMAWK algorithm \[AKM<sup>+</sup>87\], for every \(i\equiv c(\mathrm{mod}w)\), find _j_ among the collected indices to maximize \(q[j]+Q_w(\frac{i-j}{w})\). This is the same idea as in the proof of the standard batch-update Lemma 2.7 (used in e.g., \[KP04, Cha18, AT19, PRW21\]). However, in our scenario with small<tbc>

