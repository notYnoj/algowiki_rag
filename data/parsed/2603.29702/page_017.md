applying Hoeffding’s inequality (Lemma 3.1), the probability that |_g<sub>x</sub>|\>S_<sup>0.51</sup> is \(1/2^{\Omega\left(log_M^{0.02}(n)\right)}\) (recall that _S_=log_<sub>M</sub>(n_)). Therefore, there are at most an \(1/2^{\Omega\left(log_M^{0.02}(n)\right)}\)-fraction of tail indices _x_ such that |_g<sub>x</sub>|\>S_<sup>0.51</sup>, and each of these |_g<sub>x</sub>_| values is no more than _S_. By summing the contribution up of the "core" indices satisfying \(|g_x|\le S^{0.51}\) and the tail indices, we have

\(\sum_x|g_x||a_x|\le\left(\sum_x|a_x|\right)S^{0.51}+max_x|a_x|\cdot\left|\{x\text{s.t.}|g_x|>S^{0.51}\}\right|\cdot max\{|g_x|\}\)<br>
\(\le\left(\sum_x|a_x|\right)S^{0.51}+max_x|a_x|\cdot\left(n/2^{\Omega\left(log_M^{0.02}(n)\right)}\right)\cdot S\)<br>
\(=\left(\sum_x|a_x|\right)S^{0.51}+max_x|a_x|\cdot o\left(n/2^{log_M^{0.015}(n)}\right).\)

Plugging this into (4), we have that indeed,

\(\includegraphics{}\text{TD}_{M,S}(A)\le O\left(\left(\sum_x|a_x|\right)S^{0.51}+max_x|a_x|\cdot\left(n/2^{log_M^{0.015}(n)}\right)\right).\)

## 4.2 Tree Total Deviation Scaled by Another Sequence

Suppose we have another sequence _B_=(_b_<sub>1</sub>_,b_<sub>2</sub>_,...,b<sub>n</sub>_) of length _n_. We consider the following question: how much does _B_ concentrate on the high deviation regions of _A_? For an interval (_l,r_\] on some scale _s_, we define the _scaled total deviation_ of _A(l,r_\] by _B(l,r_\] to be TD_<sub>M</sub>(A(l,r_\]) scaled by the _B_-to-_A_ ratio:<tbc>

\(\text{SD}_M\left(A(l,r],B(l,r]\right):=\frac{B_{\Sigma(l,r]}}{A_{\Sigma(l,r]}}\text{TD}_M(A(l,r]),\)

<tbc>And specifically, if \(A_{\Sigma(l,r]}=0\), we let SD_<sub>M</sub>(A(l,r_\]_,B(l,r_\]):=0. We define the scaled tree total deviation of _A_ by _B_ to be the total sum of scaled total deviation over all recursion intervals:

\(\includegraphics{}\text{SD}_{M,S}(A,B):=\sum_{s\in[S]}\sum_{(l,r]\in s}\text{SD}_M(A(l,r],B(l,r])\)

We have the following lemma which states that _B_ does not concentrate on the high deviation regions of _A_ as long as the _B_-to-_A_ ratio is within some reasonable range in every recursion interval:

**Lemma 4.3.** _Let A_=(_a_<sub>1</sub>_,a_<sub>2</sub>_,...,a<sub>n</sub>_) _and B_=(_b_<sub>1</sub>_,b_<sub>2</sub>_,...,b<sub>n</sub>_) _be sequences of non-negative real numbers where n=M<sup>S</sup>. Suppose that there exists_ \(0<\alpha\le 1\) _such that for every recursion interval_ (_l,r_\]_, we have_<tbc>

\(\alpha A_{\Sigma(l,r]}\le B_{\Sigma(l,r]}\le A_{\Sigma(l,r]}.\)

<tbc>_Then we have_

\(\includegraphics{}\text{SD}_{M,S}(A,B)=O\left(\left(1+log\left(\frac{1}{\alpha}\right)\right)\left(\left(\sum_xb_x\right)S^{0.51}+max_{x^\prime}\left(a_{x^\prime}\right)\cdot\left(n/2^{log_M^{0.015}(n)}\right)\right)\right)\) (5)

