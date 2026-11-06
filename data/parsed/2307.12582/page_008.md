To see why the claim is true, take _d_ arbitrary numbers from _B_. For \(i\in\{1,\dots,d\}\), Let _h<sub>i</sub>_ be the sum of the first _i_ numbers. If any of \(h_i\equiv 0(modd)\), then we are done. Otherwise, by the pigeonhole principle, there must be _i\<j_ such that \(h_i\equiv h_j(modd)\). This implies that there is a subset of _j-i_ numbers whose sum is \(h_j-h_i\equiv 0(modd)\). Note that \(0<j-i\le d\). So this subset is non-empty and has its sum at most _dw_. \(\sqcap\sqcup\)

Lemma 3.1 has no requirement on the multiplicities of elements in _A_. Therefore, in order to be dense, _A_ must contain at least _c<sub>A</sub>w_<sup>1/2</sup>log_w_ distinct integers. The following Lemma 3.2 generalizes Lemma 3.1 by taking the multiplicity of integers into consideration. Its proof is similar to that of Lemma 3.1, so we defer it to the appendix B.

Lemma 3.2. _Let w be a positive integer. Let A and B be two multisets of integers from_ {1_,...,w_} _such that_

(i) _at least c<sub>A</sub>w_<sup>2/5</sup>log<sup>2</sup>_w distinct integers in A have multiplicity of at least w_<sup>1/5</sup>,<tbc>

(ii) \(\Sigma_B\ge c_Bw^{8/5}\),

_where c<sub>A</sub> and c<sub>B</sub> are two sufficiently large constants. Then there must exist a non-empty subset_ \(A'\) _of A and a non-empty subset_ \(B'\) _of B such that_ \(\Sigma_{A^\prime}=\Sigma_{B^\prime}\).

## 4 An \(\widetilde{O}(n+w_{max}^{5/2})\)-time Algorithm for Knapsack

To illustrate our main idea, we first present a simpler algorithm that runs in \(\widetilde{O}(n+w_{max}^{5/2})\). The algorithm uses the proximity-based (min,+)-convolution framework (See Subsection 2.3). By Lemma 2.2, the key to obtaining a fast algorithm is to find a good partition of _W_.

Polak et al. \[26\] did not partition _W_ at all. That is, they used _k_=1 and _W_<sub>1</sub>=_W_. Lemma 2.1 implies an upper bound of \(2w_{max}^2\) on \(\Delta(\mathcal{I}^W)\). Together with the fact that \(|W|\le w_{max}\), they obtained a running time of \(O(n+w_{max}^3)\). Although the upper bound of \(O(w_{max}^2)\) on \(\Delta(\mathcal{I}^W)\) is actually tight, an improvement in the running time is still possible. Indeed, our first proximity result states that \(\Delta(\mathcal{I}^W)\) concentrates at the small set _W_<sup>∗</sup> of roughly \(w_{max}^{1/2}\) weights, and that the rest of the weights together contribute at most \(O(w_{max}^{3/2})\). Moreover, _W_<sup>∗</sup> can be identified in \(\widetilde{O}(n)\) time. Then an \(\widetilde{O}(n+w_{max}^{5/2})\)-time algorithm directly follows by Lemma 2.2.

This section is divided into two parts: the structural part and the algorithmic part. The structural part proves the existence of _W_<sup>∗</sup>, and the algorithmic part gives algorithms for finding _W_<sup>∗</sup> and solving Knapsack.

### 4.1 Structural Part - Fine-Grained Proximity

In the structural part, Bounded Knapsack and 0-1 Knapsack are equivalent, in the sense that every item with _u<sub>i</sub>_ copies can be viewed as _u<sub>i</sub>_ items. Therefore, only 0-1 Knapsack is discussed in the structural part. In 0-1 Knapsack, each item _i_ has only one copy, so there is no difference between items and copies of items. We can use them interchangeably. As a result, any solution to 0-1 Knapsack can be represented as a subset of I. Let \(\mathbf{x}\in\{0,1\}^{|\mathcal{I}|}\) be a solution to 0-1 Knapsack. With slight abuse of notation, we also use **x** to denote the set of items selected by **x**. For any subset \(\mathcal{I}'\) of items, \(\mathbf{x}(\mathcal{I}')=\mathcal{I}'\cap\mathbf{x}\) and \(\overline{\mathbf{x}}(\mathcal{I}')=\mathcal{I}'\backslash\mathbf{x}\) denote the sets of items from \(\mathcal{I}'\) that are selected and not selected by **x**, respectively.

Our first proximity result is the following.

Lemma 4.1. _There exists a partition_ (_W_<sup>∗</sup>_,<o>W</o>_<sup>∗</sup>) _of W such that_

(i) \(|W^*|=4c_Aw_{max}^{1/2}logw_{max}\)_, and_<tbc>

(ii) \(\Delta(\mathcal{I}^\overline{W^*})\le 4c_Bw_{max}^{3/2}\),

_where c<sub>A</sub> and c<sub>B</sub> are two large constants used in Lemma 3.1._

_Proof._ We will define _W_<sup>∗</sup> via a partition of I, and then show that _W_<sup>∗</sup> satisfies properties in the lemma.

**Defining _W_<sup>∗</sup> via a partition of I**.** Recall that we label the items in decreasing order of efficiency. That is, \(p_1/w_1\ge\dots\ge p_n/w_n\). Without loss of generality, we assume that for any two items _i\<j\<b_, if _i_ and _j_ have the same efficiency, then \(w_i\le w_j\), and that for any two items _b\<i\<j_, if _i_ and _j_ have the same efficiency, then \(w_i\ge w_j\). We partition the items into four groups (I<sub>1</sub>,I<sub>2</sub>,I<sub>3</sub>,I<sub>4</sub>) according to their indices. See Figure 1 for an illustration. We shall define I<sub>2</sub> and I<sub>3</sub> in such a way that (i) they are "close" to the break item _b_ and that (ii)

