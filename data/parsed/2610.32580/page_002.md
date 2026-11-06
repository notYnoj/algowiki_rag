Write the subset sums of _a_<sub>1</sub>_,...,a_<sub>_n_-1</sub> in increasing order:<tbc>

\(0=t_1<t_2<\cdots<t_{2^{n-1}}=T.\)

<tbc>**Theorem 1.** If \(a_1<a_2<\cdots<a_n\) are positive integers with distinct subset sums, then

\(a_n\ge 2\genfrac(){pt}{2}{n-1}{\left\lfloor\frac{n-1}{2}\right\rfloor}.\)

In our proof, we combine ideas from \[4\] with the following observations. If _a<sub>n</sub>_ is \(\Omega(2^n)\), then the theorem is proven, i.e., we may assume that _a<sub>n</sub>=o_(2_<sup>n</sup>_).

**Lemma 1.** If \(i+a_n\le 2^{n-1}\), then<tbc>

\(t_{i+a_n}-t_i\ge 2a_n.\)

<tbc>_Proof._ Consider the _a<sub>n</sub>_+1 integers<tbc>

\(t_i,t_{i+1},\dots,t_{i+a_n}.\)

<tbc>By the pigeonhole principle, two of them, say _t<sub>k</sub>_ and \(t_\ell\), with \(k<\ell\), are congruent modulo _a<sub>n</sub>_. Hence<tbc>

\(t_\ell-t_k=ma_n\)

<tbc>for some positive integer _m_.

If _m_=1, then<tbc>

\(t_\ell=t_k+a_n.\)

<tbc>The left-hand side is a subset sum of _a_<sub>1</sub>_,...,a_<sub>_n_-1</sub>, while the right-hand side is a subset sum involving _a<sub>n</sub>_. This contradicts the distinctness of all subset sums. Therefore \(m\ge 2\), and

\(t_{i+a_n}-t_i\ge t_\ell-t_k\ge 2a_n.\)

**Lemma 2.** Define<tbc>

\(\mathcal{F}=\left\{I\subseteq[n-1]:\sum_{j\in I}a_j<\frac{T}{2}\right\}=\left\{t_i:t_i<\frac{T}{2}\right\}.\)

<tbc>Then<tbc>

\(|\mathcal{F}|=2^{n-2}.\)

<tbc>_Proof._ For any \(1\le i\le 2^{n-1}\), _t<sub>i</sub>+t_<sub>2<sup>_n_-1</sup>+1-_i_</sub>=_T_. Since all subset sums are distinct, no subset sum equals _T/_2. So, exactly one member of each pair belongs to F. Therefore,

\(|\mathcal{F}|=2^{n-2}.\)

Now, like in \[4\], identify subsets of \[_n_-1\] with vertices of the (_n_-1)-dimensional Boolean cube. For a family \(\mathcal{F}\subseteq 2^{[n-1]}\), let \(\partial\mathcal{F}\) denote its external vertex boundary. Harper’s vertex- isoperimetric inequality implies that if<tbc>

\(|\mathcal{F}|=2^{n-2},\)

