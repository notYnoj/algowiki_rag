## C Omitted proofs from Section 4

_Proof of Lemma 4.6._ The upper bound on the value is immediate, and the non-negativity follows since<tbc>

\(\sum_{j=1}^s(3nM)^{j-1}w_j\ge-M\sum_{j=1}^s(3nM)^{j-1}>-(3nM)^s.\)

<tbc>For any \(T\subseteq U\),

\(\sum_{i\in T}g(w_i)=(3nM)^s\cdot|T|+\sum_{j=1}^s(3nM)^{j-1}\cdot\left(\sum_{i\in T}w_{i,j}\right).\)

Here \(|T|\in[0,n]\) and each \(\sum_{i\in T}w_{i,j}\in[-nM,nM]\). Thus, \(\sum_{i\in T}g(w_i)\) is a base-(3_nM_) encoding of the tuple \((|T|,\sum_{i\in T}w_{i,1},\dots,\sum_{i\in T}w_{i,s})\), which can be uniquely decoded. Hence, equality of the encoded sums holds iff the corresponding vector sums are equal.

**Lemma 4.7** (Separation for Linear Matroids)**.** _Given a linear matroid_ M=(_U,_I)_, non-negative integers c_<sub>1</sub>_,c_<sub>2</sub>_,...,c<sub>n</sub> for elements in U, and a set of non-negative values_ \(Z=\{z_1,\dots,z_\ell\}\)_, we can identify a basis_ \(S\in\mathcal{F}\) _of_ M _such that_ \(c(S)\notin Z\) _(or decide that no such basis exists) in_ \(\mathrm{poly}(n,\ell,\mathrm{log}M)\) _time, where_ \(M=\mathrm{max}_{i\in[n],j\in[\ell]}\{c_i,z_j\}\).

_Proof of Lemma 4.7._ Consider the polynomial _P(x_) defined in (11):

\(P(x)=\mathrm{det}\left(\sum_{i=1}^nx^{c_i}v_iv_i^T\right)=\sum_{S\in\mathcal{F}}x^{\sum_{i\in S}c_i}\mathrm{det}(V_S)^2=\sum_{S\in\mathcal{F}}x^{c(S)}\mathrm{det}(V_S)^2.\)

As established, the set of exponents with non-zero coefficients in _P(x_) is precisely the set of basis costs, \(\{c(S)|S\in\mathcal{F}\}\).

Assume there exists a basis _S_<sup>∗</sup> such that its cost _c=c(S_<sup>∗</sup>) is not in _Z_. Our goal is to find such a _c_. Instead of explicitly computing _P(x_) which has degree can be _O(nM_), we compute _Q(x_)=_P(x_) (mod _x<sup>p</sup>_-1) for a carefully chosen prime _p_. Indeed, we would like a prime _p_ that does not divide any of the integers in the set \(D=\{z_i-z_j|i\neq j\in[\ell]\}\cup\{c-z_j|j\in[\ell]\}\). If _p_ satisfies this property, then all residues \(\{z_i(\mathrm{mod}p)\}_{i\in[\ell]}\) are distinct, and _c_ (mod_p_) is distinct from all of them.

This reduces the original problem to a smaller one: finding an exponent \(c'\) in _Q(x_) (which has degree at most _p_-1) such that \(c'\notin\{z_i(\mathrm{mod}p)\}_{i\in[\ell]}\). This new problem can be solved in poly(_n,p_) time from the warmup proof, which also recovers the witness basis _S_ using the self-reducibility approach.

The final step is to show that a "small" prime _p_ with this property exists and can be found efficiently. The set _D_ contains \(O(\ell^2)\) integers. Each integer in _D_ is bounded in magnitude by _O(nM_) (since \(c_i,z_j\le M\)). The product of all these non-zero integers has at most \(L:=O(\ell^2\mathrm{log}(nM))\) distinct prime factors.

By a simple pigeonhole argument, a prime _p_ that does not divide any of these integers must exist among the first _L_+1 primes. The prime number theorem tells us that the _t_-th prime has magnitude _O(t_log_t_), the smallest such _p_ has a value of _O(L_). This prime can be found deterministically in poly(_L_) time. Hence, the overall runtime of the self-reduction algorithm is \(\mathrm{poly}(L)=\mathrm{poly}(n,\ell,\mathrm{log}M)\), as required. Conversely, if the search through all primes in this range yields no such exponent, we can conclude that no basis _S_ with \(c(S)\notin Z\) exists.

