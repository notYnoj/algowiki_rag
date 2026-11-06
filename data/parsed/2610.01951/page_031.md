Since _u<sub>T</sub>_ is also a upper-quantile bound, the definition of _q<sub>T</sub>_ gives

\(q_T(\eta)\le u_T(\eta)\forall\eta\in(0,1].\)

Hence

\(\sum_{k\ge 0}2^{-k}q_T(2^{-k})\le\sum_{k\ge 0}2^{-k}u_T(2^{-k})<\infty.\)

This proves the claim.

**Lemma F.5** (Finite mean gives summable dyadic quantiles)**.** _Let_ \(X\ge 0\) _satisfy_ \(\mathbb{E}[X]<\infty\)_, and let_<tbc>

\(q_X(\eta):=inf\{x\ge 0:\mathbb{P}(X\le x)\ge 1-\eta\},\eta\in(0,1].\)

<tbc>_Then_

\(\sum_{k\ge 0}2^{-k}q_X(2^{-k})<\infty.\)

<tbc>_Proof of Lemma F.5._ The map \(\eta\mapsto q_X(\eta)\) is nonincreasing. For each \(k\ge 0\) and \(u\in[2^{-k-1},2^{-k}]\), one has \(q_X(u)\ge q_X(2^{-k})\). Hence<tbc>

\(2^{-k}q_X(2^{-k})\le 2\int_{2^{-k-1}}^{2^{-k}}q_X(u)du.\)

<tbc>Summing over _k_ and using the quantile representation of expectation gives

\(\sum_{k\ge 0}2^{-k}q_X(2^{-k})\le 2\int_0^1q_X(u)du=2\mathbb{E}[X]<\infty.\)

## F.4 Threshold inversion

**Theorem F.6** (Threshold inversion with a linear entrance delay)**.** _Fix constants T\>_0, \(C_0\ge 0\)_, and_ \(a,b,d\ge 0\)_. For_ \(\eta\in(0,1]\) _and_ \(t\ge 1\)_, define_<tbc>

\(\widetilde{H}_t(\eta):=log\frac{K}{\eta}+log(et).\)

<tbc>_There exists a finite constant A_<sub>inv</sub>_, depending only on T,C_<sub>0</sub>_,a,b,d and K, such that the following holds. For every_ \(\delta\in(0,1/2]\) _and_ \(\eta\in(0,1/4]\)_, set_<tbc>

\(L_\delta:=log\frac{1}{\delta},M_{\delta,\eta}:=log\frac{K}{\eta}+loglog\frac{e}{\delta},\)

<tbc>_and_<tbc>

\(s_{\delta,\eta}:=\left[TL_\delta+A_\mathrm{inv}\sqrt{L_\delta M_{\delta,\eta}}+A_\mathrm{inv}M_{\delta,\eta}+A_\mathrm{inv}\right].\)

<tbc>_Then, for every_ \(L\ge 0\) _and_<tbc>

\(t=(1+C_0)L+s_{\delta,\eta},\)

<tbc>_one has_<tbc>

\(\frac{L+s_{\delta,\eta}}{T}-a\sqrt{t\widetilde{H}_t(\eta)}-b\widetilde{H}_t(\eta)-d>c(t,\delta).\)

<tbc>_Proof of Theorem F.6._ Write

\(\overline{c}:=1+C_0,s:=s_{\delta,\eta},M:=M_{\delta,\eta},L_\delta:=log\frac{1}{\delta}.\)

Because \(\delta\in(0,1/2]\) and \(\eta\in(0,1/4]\), there is a positive constant _m_<sub>0</sub>=_m_<sub>0</sub>(_K_) such that \(M\ge m_0\). We first record two elementary bounds. Put<tbc>

\(R:=\sqrt{L_\delta M}+M+1.\)

