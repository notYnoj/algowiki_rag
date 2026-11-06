- Case (2i): \(q[z^*]<q'[z^*]\).<tbc>

<tbc>Then, in instance \(\mathrm{max}(K,K')\), (**_x_**<sup>∗</sup>_,z_<sup>∗</sup>) actually achieves a higher objective \(\bar{r}+q'[z^*]-q[z^*]\), a contradiction.<tbc>

**-** Case (2ii): \(q[z^*]\ge q'[z^*]\).<tbc>

<tbc>Then, in instance \(\mathrm{max}(K,K')\), by definition we have \(S''[z^*]\subseteq S[z^*]\). Hence, (**_x_**<sup>∗</sup>_,z_<sup>∗</sup>) is a maximizer solution for index _i_ in instance \(\mathrm{max}(K,K')\) that does not satisfy the support containment condition \(\mathrm{supp}(\mathbf{x}^*)\subseteq S''[z^*]\), a contradiction.

Hence, we have reached contradictions in all cases. This means \(\mathrm{max}(Y,Y')\) is a correct solution to \(\mathrm{max}(K,K')\).

## 4.3 Decomposing the problem via color-coding

In Section 4.1, we solved HintedKnapsackExtend<sup>+</sup> (Problem 1) in the base case where each hint set _S_\[_i_\] has size at most 1. In this section, we extend it to the case with larger size bound \(|S[i]|\le b\). This is achieved by using the color-coding technique \[AYZ95\] to isolate the elements in the sets _S_\[_i_\], and using the helper lemmas from Section 4.2 to combine the solutions for different color classes. Here we apply the two-level color-coding approach previously used by Bringmann \[Bri17\] in his near-linear time randomized subset sum algorithm.<sup>11</sup>

The following Lemma 4.8 gives an algorithm for HintedKnapsackExtend<sup>+</sup> which is suitable for _b_ slightly larger than 1 (for example, polylogarithmic).

**Lemma 4.8** (Algorithm for small _b_)**.** _HintedKnapsackExtend_<sup>+</sup> _(Problem 1) with_ \(|S[i]|\le b\) _for all_ \(-L\le i\le L\) _can be solved deterministically in O(Lb_<sup>2</sup>(_b_+log_L_)) _time._

Lemma 4.8 will be proved later in this section via color-coding. Using Lemma 4.8 as a building block, we can solve HintedKnapsackExtend<sup>+</sup> for even larger _b_, using another level of color- coding. The derandomized version of this color-coding is summarized in the following lemma.

**Lemma 4.9** (Deterministic balls-and-bins)**.** _Given integer r, and m sets_ \(S_1,S_2,\dots,S_m\subseteq[n]\) _such that_ \(|S_i|\le r\mathrm{log}_2(2m)\) _for all i, there is an O(mr_log_m_log_r+n_log_r)-time deterministic algorithm that finds an r-coloring_ \(C:[n]\rightarrow[r]\)_, such that for every_ \(i\in[m]\) _and every color_ \(c\in[r]\),

\(|\{j\in S_i:C(j)=c\}|\le O(\mathrm{log}m).\)

Lemma 4.9 follows from the results of \[Rag88, Spe87\] on deterministic set balancing using the method of pessimistic estimators. A proof of Lemma 4.9 is included in Appendix B.4.

Now we can prove our main Theorem 3.11, restated below.

**Theorem 3.11.** _HintedKnapsackExtend_<sup>+</sup> _(Problem 1) with_ \(|S[i]|\le b\) _for all_ \(-L\le i\le L\) _can be solved deterministically in O(Lb_log<sup>2</sup>(_Lb_)) _time._

_Proof of Theorem 3.11 assuming Lemma 4.8._ If \(b\le O(\mathrm{log}L)\), then we can directly invoke Lemma 4.8 in \(O(Lb^2(b+\mathrm{log}L))\le O(Lb\mathrm{log}^2L)\) time. Hence, in the following we assume _b\>_2log<sub>2</sub>(4_L_+2). Define parameter _r=b/_log<sub>2</sub>(4_L_+2)_\>_2, and use Lemma 4.9 to construct in _O(Lr_log_L_log_r_+<tbc>

<sup>11</sup>An advantage in our scenario is that the sets _S_\[_i_\] to be isolated are already given to us as input, so we can derandomize the color-coding technique, whereas in Bringmann’s subset sum algorithm \[Bri17\] the set to be isolated is the unknown solution set. Derandomizing Bringmann’s algorithm is an important open problem.

