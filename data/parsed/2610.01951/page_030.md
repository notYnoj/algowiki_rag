## F.3 Centered quantile integration

**Theorem F.3** (Centered quantile integration)**.** _Let_ \(X\ge 0\) _be a random variable. Let_ \(A\ge 0\) _and let_ \(r:(0,1]\rightarrow[0,\infty)\) _satisfy_<tbc>

\(\mathbb{P}(X\le A+r(\eta))\ge 1-\eta\forall\eta\in(0,1].\)

<tbc>_Define the monotone envelope_<tbc>

\(r^\downarrow(\eta):=sup_{\xi\in[\eta,1]}r(\xi).\)

<tbc>_Then_<tbc>

\(\mathbb{E}[X]\le A+\int_0^1r^\downarrow(u)du.\)

<tbc>_Moreover, if_<tbc>

\(\sum_{k\ge 0}2^{-k}r^\downarrow(2^{-k})<\infty,\)

<tbc>_then_<tbc>

\(\mathbb{E}[X]\le A+\sum_{k\ge 0}2^{-k}r^\downarrow(2^{-k}).\)

<tbc>_Proof of Theorem F.3._ Let<tbc>

\(Q_X(u):=inf\{x\ge 0:\mathbb{P}(X\le x)\ge 1-u\},u\in(0,1],\)

<tbc>be the upper-tail quantile of _X_. The assumed upper-quantile inequality gives<tbc>

\(Q_X(u)\le A+r(u)\le A+r^\downarrow(u)\forall u\in(0,1].\)

<tbc>The quantile representation of expectation for nonnegative random variables therefore yields<tbc>

\(\mathbb{E}[X]=\int_0^1Q_X(u)du\le A+\int_0^1r^\downarrow(u)du.\)

<tbc>For the dyadic bound, note that \(r^\downarrow\) is nonincreasing as a function of \(\eta\). Hence, for \(u\in[2^{-k-1},2^{-k}]\),<tbc>

\(r^\downarrow(u)\le r^\downarrow(2^{-k-1}).\)

<tbc>Consequently,

\(\int_0^1r^\downarrow(u)du\le\sum_{k\ge 0}2^{-k-1}r^\downarrow(2^{-k-1})\le\sum_{k\ge 0}2^{-k}r^\downarrow(2^{-k}).\)

Combining this estimate with the first part proves the theorem.

**Lemma F.4** (Monotone summable upper-quantile bound)**.** _Let_ \(T\ge 0\) _be a random time. Suppose that T admits a summable upper-quantile bound function u<sub>T</sub>, namely_ \(\mathbb{P}(T\le u_T(\eta))\ge 1-\eta,\forall\eta\in(0,1]\)_, and_ \(\sum_{k\ge 0}2^{-k}u_T(2^{-k})<\infty\)_. Define the upper-tail quantile_

\(q_T(\eta):=inf\{x\ge 0:\mathbb{P}(T\le x)\ge 1-\eta\},\eta\in(0,1].\)

_Then q<sub>T</sub> is a nonincreasing upper-quantile bound for T, and_ \(\sum_{k\ge 0}2^{-k}q_T(2^{-k})<\infty\)_. Consequently, whenever a random time admits a summable upper-quantile bound, it admits a nonincreasing summable upper-quantile bound._

_Proof of Lemma F.4._ By definition of _q<sub>T</sub>_, one has<tbc>

\(\mathbb{P}(T\le q_T(\eta))\ge 1-\eta\forall\eta\in(0,1].\)

<tbc>Thus _q<sub>T</sub>_ is a upper-quantile bound. If \(\eta_1\le\eta_2\), then \(1-\eta_1\ge 1-\eta_2\), so the confidence requirement at level \(\eta_1\) is at least as stringent as the one at level \(\eta_2\). Therefore

\(q_T(\eta_1)\ge q_T(\eta_2),\)

which means that _q<sub>T</sub>_ is nonincreasing as a function of \(\eta\).

