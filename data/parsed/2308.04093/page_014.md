Finally we remark that we do not need to sort all items of _J_ in _O_(|_J_|log|_J_|) time at the beginning. By Lemma 2.4, we only need to consider those with rank at most 2_w_<sub>max</sub>, which can be selected from _J_ and sorted in _O_(|_J_|+_w_<sub>max</sub>log_w_<sub>max</sub>) time \[BFP<sup>+</sup>73\].

## 3 Algorithm for 0-1 Knapsack

In this section we present our algorithm for 0-1 Knapsack (Theorem 1.1). In Section 3.1, we recall a crucial weight partitioning lemma from \[CLMZ24\] based on fine-grained proximity, which naturally gives rise to a two-stage algorithm framework. The second stage can be easily performed using previous techniques \[PRW21, CLMZ24\] and is described in Section 3.1, while the first stage contains our main technical challenge and is described in Sections 3.2, 3.3 and 4: In Section 3.2, we give a rank partitioning lemma based on another proximity result. Given this lemma, in Section 3.3 we abstract out a core subproblem called HintedKnapsackExtend<sup>+</sup>, and describe how to implement the first stage of our algorithm assuming this core subproblem can be solved efficiently. Our algorithm for HintedKnapsackExtend<sup>+</sup> will be described in Section 4.

### 3.1 Weight partitioning and the second-stage algorithm

Chen, Lian, Mao, and Zhang \[CLMZ24\] recently used additive-combinatorial results of Bringmann and Wellnitz \[BW21\] to obtain several powerful structural lemmas involving the support size of two integer multisets _A,B_ avoiding non-zero common subset sums. These structural results (called "fine-grained proximity" in \[CLMZ24\]) allowed them to obtain faster knapsack algorithms than the earlier works \[PRW21, EW20\] based on \(\ell_1\)-proximity (Eq. (7)) only. Here we recall one of the key lemmas from \[CLMZ24\].<sup>8</sup>

**Lemma 3.1** (\[CLMZ24, Lemma 3.1\], paraphrased)**.** _There is a constant C such that the following holds. Suppose two multisets A,B supported on_ \[_N_\] _satisfy_<tbc>

\(|supp(A)|\ge C\sqrt{NlogN}\)

<tbc>_and_

\(\Sigma(B)\ge\frac{CN^2\sqrt{logN}}{|supp(A)|}.\)

_Then,_ \(\mathcal{S}^*(A)\cap\mathcal{S}^*(B)\neq\varnothing\).

Using this fine-grained proximity result, Chen, Lian, Mao, and Zhang obtained a weight partitioning lemma \[CLMZ24, Lemma 4.1\], which is a key ingredient in their algorithm. Our algorithm also crucially relies on this weight partitioning lemma in a similar way, but for our purpose we need to extend it from the two-partition version in \[CLMZ24\] to _O_(log_w_<sub>max</sub>)-partition.<sup>9</sup>

Recall the following notations from Section 2.1: \(W(I)=\sum_{i\in I}w_i\), \(\mathcal{W}=supp(\{w_1,w_2,\dots,w_n\})\subseteq[w_{max}]\), and \(I_{\mathcal{W}^\prime}:=\{i\in[n]:w_i\in\mathcal{W}'\}\).

<sup>8</sup>The original statement of \[CLMZ24, Lemma 3.1\] had a worse log_N_ factor than the \(\sqrt{logN}\) factor in Lemma 3.1. By inspection of their proof, they actually proved the stronger version stated here in Lemma 3.1. <sup>9</sup>We remark that \[CLMZ24, Lemma 5.3\] also gave a three-partition extension of this lemma, but in a different way than what we need here.

