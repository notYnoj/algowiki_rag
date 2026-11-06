Substituting \(\xi_i=\frac{\Delta}{2Jm_i\sigma}\), we obtain \(\mathbb{E}_{\nu_1}[X]=\sum_{i=1}^J\frac{\Delta}{J}=\Delta\).

The second moment of \(\nu_1\) remains unchanged because the \(\xi_i\) perturbations are added and subtracted at squared symmetric points:

\(\mathbb{E}_{\nu_1}[X^2]=\sum_{i=1}^J\left[\left(\frac{w_i}{2}+\xi_i\right)(m_i\sigma)^2+\left(\frac{w_i}{2}-\xi_i\right)(-m_i\sigma)^2\right]=\sum_{i=1}^Jw_im_i^2\sigma^2=\sigma^2.\)

Thus, \(\mathrm{Var}_{\nu_1}(X)=\mathbb{E}_{\nu_1}[X^2]-(\mathbb{E}_{\nu_1}[X])^2=\sigma^2-\Delta^2\le\sigma^2\).

For the _K_-arm embedding, write \(P_0:=\nu_0\) and \(P_+:=\nu_1\), and define _P_<sub>-</sub> by reversing the signs of the perturbations:

\(P_-:=\left(1-\sum_{i=1}^Jw_i\right)\delta_0+\sum_{i=1}^J\left(\frac{w_i}{2}-\xi_i\right)\delta_{m_i\sigma}+\sum_{i=1}^J\left(\frac{w_i}{2}+\xi_i\right)\delta_{-m_i\sigma}.\)

By reflection, \(\mathbb{E}_{P_-}[X]=-\Delta\) and \(\mathrm{Var}_{P_-}(X)=\sigma^2-\Delta^2\le\sigma^2\). All three distributions admit the same valid anchor _c_=0, since their means have absolute value at most \(\Delta\le\sigma\).

## D.2 A uniform one-query KL bound

Consider an arbitrary measurable query set \(A\subseteq\mathbb{R}\). A 1-bit observation \(Y=\mathbf{1}\{X\in A\}\) follows a Bernoulli distribution: Ber(_p_) under \(\nu_0\) and Ber(_q_) under \(\nu_1\), where \(p:=\nu_0(A)\) and \(q:=\nu_1(A)\).

We categorize the scales based on how they intersect with _A_. Let _S(A_) denote the set of index scales \(i\in\{1,\dots,J\}\) where exactly one of the two support points \(\{\pm m_i\sigma\}\) belongs to _A_.

**Lemma 35** (One-query probability difference bound)**.** _For every measurable set_ \(A\subseteq\mathbb{R}\),<tbc>

\((q-p)^2\le\frac{2\Delta^2}{J\sigma^2}p.\)

<tbc>_Proof._ We analyze the mass difference _q-p_. For any scale \(i\notin S(A)\), either both \(\pm m_i\sigma\in A\) or neither are in _A_. If both are in _A_, the mass difference contributed by scale _i_ is

\((\frac{w_i}{2}+\xi_i)+(\frac{w_i}{2}-\xi_i)-w_i=0.\)

If neither are, the contribution is naturally 0. The origin 0 also contributes equal mass to both distributions.

Thus, only scales in _S(A_) cause a discrepancy. For \(i\in S(A)\), the difference is either \(+\xi_i\) (if \(m_i\sigma\in A\)) or \(-\xi_i\) (if \(-m_i\sigma\in A\)). We can write \(q-p=\sum_{i\in S(A)}s_i\xi_i\) for some signs \(s_i\in\{-1,1\}\). By the triangle inequality:<tbc>

\(|q-p|\le\sum_{i\in S(A)}\xi_i=\frac{\Delta}{2J\sigma}\sum_{i\in S(A)}\frac{1}{m_i}.\)

<tbc>If _S(A_) is empty, then _q-p_=0 and the claimed bound is immediate. Otherwise, let \(S(A)=\{i_1<i_2<\cdots<i_r\}\) be ordered such that _i_<sub>1</sub> is the smallest index. Because _m<sub>i</sub>_ grows geometrically as 2<sup>_i_-1</sup>, the sum is dominated by its largest term:<tbc>

\(\sum_{k=1}^r\frac{1}{m_{i_k}}\le\sum_{k=0}^{r-1}\frac{1}{m_{i_1}2^k}<\frac{2}{m_{i_1}}.\)

<tbc>Squaring this strict bound gives:<tbc>

\(\left(\sum_{i\in S(A)}\frac{1}{m_i}\right)^2<\frac{4}{m_{i_1}^2}.\)

<tbc>Because _i_<sub>1</sub> is an element of _S(A_), we have \(\frac{4}{m_{i_1}^2}\le 4\sum_{i\in S(A)}\frac{1}{m_i^2}\).

