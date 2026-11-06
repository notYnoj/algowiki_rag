_Proof._ Let A denote the set of active men before executing the inner loop in **ASM**. Suppose that after \(\ell\) iterations of the inner loop, there are _b_ bad men in A. We claim that there must have been at least _b_ bad players in every iteration of the inner loop. To see this, first note that by Lemma 3.1, the number of matched players (and hence matched men) can only increase with each call to **ProposalRound**. Second, if a man is rejected by all women on his preference list, he will never become bad. Therefore, the number of good players can only increase with each iteration of the inner loop. Thus there must have been at least _b_ bad men after each of the \(\ell\) iterations of the inner loop.

Suppose _m_ was bad before some call to **QuantileMatch**, so that \(A^m\neq\varnothing\). By Lemma 3.2, after **QuantileMatch** _m_ is either matched, or has been rejected by all women \(w\in A^m\). In the former case, _p(m_) rejected all men in her quantile containing _m_. In either case, _m_ witnessed the rejection of a quantile of men--either by precipitating the rejection of _p(m_)’s quantile, or by being rejected by all women in _A_. Notice that the number of women who are matched with new partners during an iteration of the outer loop cannot exceed |A|, as if |A| women did receive new partners, all active men would be matched. Therefore, the women can send at most _k_|A| quantile rejections (after which all active men will be rejected by all women). Similarly, the men can receive at most _k_|A| quantile rejections. Thus, in total the active men can witness at most 2_k_|A| quantile rejections. Therefore, if there are _b_ bad men after \(\ell\) calls to **QuantileMatch**, we must have \(b\ell\le 2k|\mathcal{A}|\). Choosing \(\ell=2\delta^{-1}k\) gives the desired result.

We say that a man _m_ is **_bad in the_** _i**th iteration**_ of the outer loop in **ASM** if _m_ became bad during the _i_th iteration and |_Q<sup>m</sup>|\<_2_<sup>i</sup>_. Thus, \(m\in B_i\) is bad and will not participate in any further calls to **QuantileMatch**, so he will be bad when **ASM** terminates. We denote the set bad men in the _i_ iteration by _B<sub>i</sub>_, so that \(B=B_1\cup B_2\cup\cdots\cup B_{logn}\).

**Lemma 4.6** (Few (2_/k_)-blocking pairs)**.** Each \(m\in B_i\) participates in fewer than 2_<sup>i</sup>_(2_/k_)- blocking pairs at the termination of **ASM**.

_Proof._ We will show that each bad \(m\in B\) participates in at most |_Q<sup>m</sup>_|(2_/k_)-blocking pairs, whence the lemma follows. To this end, notice that if \(w\notin Q^m\), then _w_ must have rejected _m_ in some call to **QuantileMatch**. Therefore, _w_ must have been matched with some \(m'\) that is in the same or better quantile as _m_. By Lemma 3.1, when **ASM** terminates, _w_ is still matched with someone in at least as desirable quantile as _m_, implying that (_m,w_) is not (2_/k_)-blocking. Thus, every (2_/k_)-blocking pair (_m,w_) must have \(w\in Q^m\).

_Proof of Lemma 4.4._ Let \(G_i\subseteq G\) be the set of men which are good at the termination of **ASM** and active after the _i_th iteration of the outer loop in **ASM**. Then we have \(G=G_1\cup G_2\cup\cdots\cup G_{logn}\). Since the number of bad men cannot increase after a call to **QuantileMatch**. By Lemma 4.5, if there were _b_ men which became bad in some iteration of the outer loop of **ASM**, there were \(\frac{1-\delta}{\delta}b\) good men still active during the _i_th iteration. Since the number of good men can only increase in subsequent iterations, we have<tbc>

\(|B_i\cup B_{i+1}\cup\cdots\cup B_{logn}|\le b\le\frac{\delta}{1-\delta}|G_i\cup G_{i+1}\cup\cdots\cup G_{logn}|.\) (2)

<tbc>Applying (2), we can greedily form disjoint sets<tbc>

\(H_{logn}\subseteq G_{logn},H_{logn-1}\subseteq G_{logn-1}\cup G_{logn},\dots,H_1\subseteq G\)

<tbc>such that for all _i_, _H<sub>i</sub>_ is active in the _i_th iteration and \(|H_i|=\frac{1-\delta}{\delta}|B_i|\). Then we compute

\(\sum_{m\in B}|Q^m|=\sum_{i=1}^{logn}\sum_{m\in B_i}|Q^m|\le\sum_{i=1}^{logn}|B_i|2^i\le\sum_{i=1}^{logn}\frac{2\delta}{1-\delta}|H_i|2^i\le\frac{2\delta}{1-\delta}\sum_{m\in G}|Q^m|\le\frac{2\delta}{1-\delta}|E|.\)

The first inequality holds by Lemma 4.6, while the second holds by the choice of the _H<sub>i</sub>_ and the definition of the _G<sub>i</sub>_.

