_Proof._ For every positive integer _a_, write _D<sub>a</sub>=F(a,...,a_). We first compare _D_<sub>_a_+1</sub> with _D<sub>a</sub>_. Start from (_a,...,a_) and increase its coordinates one at a time until reaching (_a_+1_,...,a_+1).

Fix an integer _j_ with \(1\le j\le n-1\), and consider the step that increases coordinate _j_. The earlier coordinates already equal _a_+1, and the later coordinates still equal _a_. Define<tbc>

\(F_j(b)=\underbrace{F(a+1,\dots,a+1,b,\underbrace{a,\dots,a}_{j-1})}_{n-1-j\text{coordinates}})(b\in\mathbb{N}_{>0}).\)

<tbc>The total degree in the other coordinates is<tbc>

\(S_j=\sum_{i=1}^{j-1}a+\sum_{i=j+1}^{n-1}(a-1)=(j-1)a+(n-1-j)(a-1)\le(n-2)a.\)

<tbc>By shifted tripling, \(F_j(3a+S_j)\ge 3F_j(a)\). Concavity gives \(F_j(h+1)-F_j(h)\le F_j(h)-F_j(h-1)\) for every integer \(h\ge 2\). Thus every forward difference starting at an integer \(h\ge a\) is at most _F<sub>j</sub>(a_+1)-_F<sub>j</sub>(a_). In particular,

\(2F_j(a)\le F_j(3a+S_j)-F_j(a)\)<br>
\(=\sum_{h=a}^{3a+S_j-1}\big(F_j(h+1)-F_j(h)\big)\)<br>
\(\le(2a+S_j)\big(F_j(a+1)-F_j(a)\big).\)

Since \(2a+S_j\le na\) and _F<sub>j</sub>(a)\>_0, division by 2_a+S<sub>j</sub>_ gives<tbc>

\(F_j(a+1)\ge\left(1+\frac{2}{2a+S_j}\right)F_j(a)\ge\left(1+\frac{2}{na}\right)F_j(a).\)

<tbc>The values at successive steps agree: _F_<sub>1</sub>(_a_)=_D<sub>a</sub>_, _F<sub>j</sub>(a_+1)=_F_<sub>_j_+1</sub>(_a_) for \(1\le j<n-1\), and _F_<sub>_n_-1</sub>(_a_+1)=_D_<sub>_a_+1</sub>. Multiplying the _n_-1 inequalities therefore gives

\(D_{a+1}\ge\left(1+\frac{2}{na}\right)^{n-1}D_a.\) (4)

This argument also applies when _a_=1, since concavity at input length 2 compares the first two forward differences.

For every positive real number _x_ and every real \(r\ge 1\), Bernoulli’s inequality gives \((1+x)^r\ge 1+rx\). With _x_=2/(_na_) and _r=n/_2, it follows that<tbc>

\(\left(1+\frac{2}{na}\right)^{n/2}\ge 1+\frac{1}{a}.\)

<tbc>Raise this inequality to the positive power 2(_n_-1)_/n_ and combine it with (4). We find<tbc>

\(\frac{D_{a+1}}{D_a}\ge\left(\frac{a+1}{a}\right)^{2(n-1)/n}.\)

<tbc>Finally, _D_<sub>1</sub>=1. Multiplying the last inequality for _a_=1_,...,A_-1 gives

\(D_A\ge\prod_{a=1}^{A-1}\left(\frac{a+1}{a}\right)^{2(n-1)/n}=A^{2(n-1)/n}\)

for every integer \(A\ge 2\). The statement for _A_=1 follows directly from the normalization.

