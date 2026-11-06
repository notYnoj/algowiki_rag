## 4.1 Basic Form

Given a sequence of real numbers _A_=(_a_<sub>1</sub>_,a_<sub>2</sub>_,...,a<sub>n</sub>_) with _n=M<sup>S</sup>_ for \(M\in 2\mathbb{Z}^+\) and \(S\in\mathbb{Z}^+\), we consider its _S_-scale recursive partition with branching factor _M_. In other words, for each scale \(s\in[S]\), we consider the partition of _A_ to disjoint length-_M<sup>s</sup>_ subsequences _A_<sub>(_l,r_]</sub>=(_a_<sub>_l_+1</sub>_,...,a<sub>r</sub>_). We say that (_l,r_] is a _scale-s interval_. Every interval (_l,r_] that is involved in the recursive partitioning (i.e., is a scale-_s_ interval for some scale \(s\in[S]\)) is called a _recursion interval_.

For a scale-_s_ interval (_l,r_], let the _i_-th (\(0\le i\le M\)) _anchor_ be \(m_i:=l+i\cdot\frac{r-l}{M}\) . Let (_m_<sub>_i_-1</sub>_,m<sub>i</sub>_] denote its _i_-th _sub-interval_. We consider the sum of each of _A_<sub>(_l,r_]</sub>’s sub-intervals, and compute the total deviation of the sums, namely the sum of how far each sub-interval is from the mean of the sub-intervals:

\(\mathrm{TD}_M(A_{(l,r]}):=\sum_{i=1}^M\left|A_{\Sigma(m_{i-1},m_i]}-\frac{1}{M}A_{\Sigma(l,r]}\right|,\)

where \(A'_{\Sigma(l^\prime,r^\prime]}\) denotes the sum \(\sum_{l^\prime<i\le r^\prime} a'_i\), a shorthand we will use throughout the paper.

We are particularly interested in the (_M_-way) _tree total deviation_, which sums the total deviation across the entire recursive partitioning of _A_:

\(\includegraphics{}\mathrm{TD}_{M,\mathcal{S}}(A):=\sum_{s\in[S]}\sum_{(l,r]\in s}\mathrm{TD}_M(A_{(l,r]}),\)

where we slightly abuse notation and use _s_ to denote both the scale and the set of scale-_s_ intervals. We also define a refined version of tree total deviation on a subset \(\mathcal{S}\subset[S]\) of scales.

\(\includegraphics{}\mathrm{TD}_{M,\mathcal{S}}(A):=\sum_{s\in\mathcal{S}}\sum_{(l,r]\in s}\mathrm{TD}_M(A_{(l,r]}).\)

Intuitively, TD_<sub>M</sub>(A_) is a measure of how "uneven" _A_ is after dividing it into _M_ parts -- namely if we divide _A_ into _M_ parts, how far they are from all having the same sum. \(\includegraphics{}\mathrm{TD}_{M,\mathcal{S}}(A)\) is a measure of the sum of the total deviation of _A_ over all scales in S.

Suppose \(|a_i|\le 1\) for all _i_. A naive upper bound on TD<sub>_M,S_</sub>(_A_) would count a contribution of _O_(1) from each _a<sub>i</sub>_ to the total deviation on each scale, or TD<sub>_M,S_</sub>(_A_)=_O(nS_) in total. A key observation for our analysis is that in fact we can show that TD<sub>_M,S_</sub>(_A_) is close to \(n\sqrt{S}\):

**Lemma 4.1.** _Let A_=(_a_<sub>1</sub>_,a_<sub>2</sub>_,...,a<sub>n</sub>_) _be a sequence of real numbers where n=M<sup>S</sup>. Then,_

\(\includegraphics{}\mathrm{TD}_{M,S}(A)=O\left(\left(\sum_x|a_x|\right)S^{0.51}+\mathrm{max}_x|a_x|\cdot\left(n/2^{\mathrm{log}_M^{0.015}(n)}\right)\right).\)

In Section B, we provide an information-theoretic proof for a slightly stronger version of the lemma. In this section, we provide a more accessible and self-contained proof using basic probabilistic arguments.

Towards proving Lemma 4.1, we will first prove the following claim:

**Claim 4.2.** _Let B_=(_b_<sub>1</sub>_,b_<sub>2</sub>_,...,b<sub>M</sub>_) _be a sequence of numbers. There exists_ \(\gamma\in\{-1,+1\}^M\) _with exactly M/_2 _(+1)’s such that_<tbc>

\(2\sum_ib_i\gamma_i\ge\mathrm{TD}_M(B).\)

