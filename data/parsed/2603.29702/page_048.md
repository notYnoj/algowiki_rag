_which is the requirement in Claim 7.5 with p<sub>s</sub> replaced by p_<sup>25</sup>.

We first present the full proof using these three claims:

_Proof of Lemma 7.3._ To prove the lemma, we perform rounding on a scale-by-scale basis. Let _p<sub>S</sub>_:=_p_. For each scale \(s\in[S]\) in decreasing order, if \(s\in\widetilde{S}\), we round _p<sub>s</sub>_ to an {_s_}-regular path _p_<sub>_s_-1</sub>. Specifically, for every scale-_s_ interval (_l,r_\], we adjust _p<sub>s</sub>(m<sub>i</sub>_) to \(p_{s-1}(m_i):=(I_{s-1}/\phi_y)\cdot\left\lfloor\frac{p_s(l)+i,\frac{p_s(r)-p_s(l)}{M}}{I_{s-1}/\phi_y}\right\rfloor\). If _p<sub>s</sub>(l,r_\] satisfies the condition in Claim 7.5, then we use the claim to obtain _p_<sub>_s_-1</sub>(_l,r_\] in a way that does not change any column that is not a hitter. If _p<sub>s</sub>(l,r_\] does not satisfy the condition in Claim 7.5, we round _p<sub>s</sub>(l,r_\] to _p_<sub>_s_-1</sub>(_l,r_\] arbitrarily (e.g., using Lemma 5.9). If \(s\notin\widetilde{S}\) we simply let _p_<sub>_s_-1</sub>:=_p<sub>s</sub>_. Let the final path be \(\widehat{p}:=p_0\).

For the rest of the proof, we bound the number of columns before which the weight of _p_ and the weight of \(\widehat{p}\) differ. This is the sum of:

• X:= the number of columns before which the weight of _p_ is 1 and the weight of \(\widehat{p}\) is 0;<tbc>

• Y:= the number of columns before which the weight of _p_ is 0 and the weight of \(\widehat{p}\) is 1.

Since _p_ is the longest path, we have \(w(p)\ge w(\widehat{p})=w(p)-\mathcal{X}+\mathcal{Y}\), and hence \(\mathcal{X}\ge\mathcal{Y}\). Thus it suffices to prove that \(\mathcal{X}=o\left(\frac{w(p)}{Mlog^{0.02}\left(n\right)}\right)\). Now consider uniformly randomly sampling a column _x_ such that the weight of _p_ before column _x_ is 1. We will argue that the weight of \(\widehat{p}\) before column _x_ is 0 with probability \(o\left(\frac{1}{Mlog^{0.02}\left(n\right)}\right)\), which would mean that the expected number of columns where the weights of _p_ and \(\widehat{p}\) differ is \(o\left(\frac{w(p)}{Mlog^{0.02}\left(n\right)}\right)\), and would finish the proof due to Markov’s inequality.

To present this argument, we will show that the only few exceptions to \(\widehat{p}(x-1,x]=p(x-1,x]\) are the columns _x_ such that either (24) is not satisfied by some interval \((l,r]\unknown x\) on an active scale, or _x_ hits an interval on an active scale. We first demonstrate that these two cases of exceptions indeed only happen with \(o\left(\frac{1}{Mlog^{0.02}\left(n\right)}\right)\) probability when _x_ is a uniformly random column with before which the weight of _p_ is non-zero.

## Case I: (24) is not satisfied by some interval \((l,r]\unknown x\) on an active scale

Claim 7.6 shows that (24) is not satisfied by some interval \((l,r]\unknown x\) on an active scale with probability \(o\left(\frac{1}{Mlog^{0.02}\left(n\right)}\right)\).

## Case II: _x_ hits an interval on an active scale

This can be further categorized into the following:

**Frequent hitters** From Claim 7.4, the number of _x_’s that are frequent hitters is at most \(n/2^{log^{0.02}\left(n\right)}=o\left(\frac{w(p)}{Mlog^{0.02}\left(n\right)}\right)\), so _x_ is a frequent hitter with probability \(o\left(\frac{1}{Mlog^{0.02}\left(n\right)}\right)\);

**Non-frequent-hitter columns that hit intervals on active scales by chance** Given an _x_ that is not a frequent hitter, since the number of scales _s_, such that _x_ is a hitter of the interval \((l,r]\unknown x\) on scale _s_, is at most _S_<sup>0.83</sup>, and since each scale that is a multiple of 3 is added u.a.r. with probability 1_/S_<sup>0.98</sup> to \(\widetilde{S}\), only with probability at most \(1/S^{0.15}=o\left(\frac{1}{Mlog^{0.02}\left(n\right)}\right)\) can there be an interval \((l,r]\unknown x\) on an active scale such that _x_ is a hitter of (_l,r_\].

<sup>25</sup>Note that |_p(r_)-_p(l_)|_\<r-l_ is automatically satisfied from the lemma condition.

