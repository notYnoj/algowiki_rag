Simultaneously, we bound the baseline probability _p_. For every \(i\in S(A)\), exactly one support point is in _A_, contributing _w<sub>i</sub>/_2 to \(\nu_0(A)\). Therefore,<tbc>

\(p\ge\sum_{i\in S(A)}\frac{w_i}{2}=\frac{1}{2J}\sum_{i\in S(A)}\frac{1}{m_i^2}\Longrightarrow\sum_{i\in S(A)}\frac{1}{m_i^2}\le 2Jp.\)

<tbc>Combining these inequalities gives the desired result:

\((q-p)^2\le\frac{\Delta^2}{4J^2\sigma^2}\left(4\sum_{i\in S(A)}\frac{1}{m_i^2}\right)\le\frac{\Delta^2}{J^2\sigma^2}(2Jp)=\frac{2\Delta^2}{J\sigma^2}p.\)

**Lemma 36** (Uniform KL divergence bound)**.** _There exists an absolute constant C_<sub>0</sub>_\>_0 _such that for every measurable set_ \(A\subseteq\mathbb{R}\),<tbc>

\(max\{kl(q,p),kl(p,q)\}\le C_0\frac{\Delta^2}{J\sigma^2},\)

<tbc>_where_ \(kl(u,v)=ulog\frac{u}{v}+(1-u)log\frac{1-u}{1-v}\) _denotes the binary KL divergence. Moreover, writing_ \(p_\pm:=P_\pm(A)\)_, the opposite perturbations satisfy_<tbc>

\(max\{kl(p_-,p_+),kl(p_+,p_-)\}\le 4C_0\frac{\Delta^2}{J\sigma^2}.\)

<tbc>_Proof._ If _p_=0 or _p_=1, the perturbed laws assign the same probability to _A_, so all divergences vanish. Otherwise, we first establish that the likelihood ratio is bounded, specifically that<tbc>

\(\frac{q}{p}\in\left[\frac{1}{2},\frac{3}{2}\right].\)

<tbc>Using the structural properties of our construction, we bounded \(\xi_i\le w_i/4\). Therefore:<tbc>

\(|q-p|\le\sum_{i\in S(A)}\xi_i\le\frac{1}{4}\sum_{i\in S(A)}w_i=\frac{1}{2}\sum_{i\in S(A)}\frac{w_i}{2}\le\frac{1}{2}p.\)

<tbc>This implies \(-\frac{1}{2}p\le q-p\le\frac{1}{2}p\), which rearranges exactly to \(\frac{1}{2}p\le q\le\frac{3}{2}p\).

By complement invariance of binary KL divergence, kl(_q,p_)=kl(1-_q,_1-_p_). We may assume without loss of generality that \(p\le 1/2\) (if not, we simply replace _A_ with its complement _A<sup>c</sup>_, noting that _S(A_)=_S(A<sup>c</sup>_)).

Using the standard inequality \(kl(u,v)\le\frac{(u-v)^2}{v(1-v)}\) and Lemma 35, we obtain:<tbc>

\(kl(q,p)\le\frac{(q-p)^2}{p(1-p)}\le\frac{(q-p)^2}{p(1/2)}=2\frac{(q-p)^2}{p}\le 4\frac{\Delta^2}{J\sigma^2}.\)

<tbc>To bound the reverse direction kl(_p,q_), we require _q_(1-_q_) in the denominator. Since \(p\le 1/2\), our likelihood bounds give \(q\le 3/4\), meaning \(1-q\ge 1/4\). Furthermore, \(q\ge p/2\). Therefore, \(q(1-q)\ge(p/2)(1/4)=p/8\). Thus:<tbc>

\(kl(p,q)\le\frac{(p-q)^2}{q(1-q)}\le 8\frac{(q-p)^2}{p}\le 16\frac{\Delta^2}{J\sigma^2}.\)

<tbc>The first bound holds with the absolute constant _C_<sub>0</sub>=16. For the opposite perturbations, _p_<sub>+</sub>=_q_ and _p_<sub>-</sub>=2_p-q_, so \(|p_\pm-p|\le p/2\). With \(p\le 1/2\) as above, both denominators satisfy \(p_\pm(1-p_\pm)\ge p/8\). Since _p_<sub>+</sub>-_p_<sub>-</sub>=2(_q-p_), the same binary KL inequality gives

\(max\{kl(p_-,p_+),kl(p_+,p_-)\}\le 8\frac{4(q-p)^2}{p}\le 64\frac{\Delta^2}{J\sigma^2}=4C_0\frac{\Delta^2}{J\sigma^2}.\)

