<tbc>where (_n)<sub>q</sub>_ denotes the falling factorial. Thus, _o_<sub>R</sub>(_q;n_)=_q!u_<sub>R</sub>(_q;n_) is a quasip polynomial of period 1 (that is, a polynomial) and degree 2_q_, in accordance with our general theory. In our approach, we want to study its coefficients.

The coefficient of _n_<sup>2_q-i_</sup> is<tbc>

(3.2) \(q!\gamma_i=\sum_{k=0}^is(q,q-k)s(q,q-(i-k)),\)

<tbc>where _s(q,j_) denotes the Stirling number of the first kind, defined as 0 if _j\<_0 or _j\>q_. For instance,

\(q!\gamma_0=1,q!\gamma_1=-(q)_2,\)<br>
\(q!\gamma_2=(q)_2\frac{3q^2-5q+1}{6},q!\gamma_3=-(q)_3\frac{q(q-1)^2}{6}.\)

These formulas, derived from Equation (3.2), agree with the general partial queens formulas in Theorem III.3.1. (Recall that the rook is the partial queen Q<sup>20</sup>.)

The sign of each term in the summations in (3.2) is (-1)_<sup>i</sup>_, so that is the sign of \(\gamma_i\) for \(0\le i\le 2q-2\). For _i\>_2_q_-2, \(\gamma_i=0\) because _s(q,_0)=0. The rook is one of few pieces for which we know the sign of every term in _o_<sub>P</sub>(_q;n_).

**Proposition 3.1.** _The coefficient_ \(q!\gamma_i\) _is a polynomial in q of degree_ 2_i. It has a factor_ \((q)_{\lceil i/2\rceil+1}\)_. The coefficient of q_<sup>2_i_</sup> _is_

(3.3) \(\frac{1}{(2i)!}\sum_{k=0}^i\genfrac(){pt}{2}{2i}{2k}\sum_{r=0}^k(-1)^r\genfrac(){pt}{2}{2k}{k+r}S(k+r,r)\sum_{s=0}^{i-k}(-1)^s\genfrac(){pt}{2}{2(i-k)}{i-k+s}S(i-k+s,s),\)

_whose sign is_ (-1)_<sup>i</sup>._

_Proof._ Schlömlch’s formula \[8, p. 216\]<tbc>

(3.4) \(s(q,q-k)=\sum_{r=0}^k(-1)^r\genfrac(){pt}{2}{q-1+r}{k+r}\genfrac(){pt}{2}{q+k}{k-r}S(k+r,r)\)

<tbc>(which involves the Stirling numbers _S(n,k_) of the second kind) tells us that _s(q,q-k_) is a polynomial in _q_ of degree 2_k_ with leading term

\(\sum_{r=0}^k(-1)^r\frac{q^{k+r}}{(k+r)!}\frac{q^{k-r}}{(k-r)!}S(k+r,r)=\frac{q^{2k}}{(2k)!}\sum_{r=0}^k(-1)^r\genfrac(){pt}{2}{2k}{k+r}S(k+r,r).\)

This term, as the leading term, must have the same sign as _s(q,q-k_) for large _q_. So the leading coefficient of \(q!\gamma_i\) is as in Equation (3.3) and the sign of this coefficient is (-1)_<sup>i</sup>_.

It is easy to infer from (3.2) that the polynomial equals 0 if _i\>_2_q_-2, i.e., \(q\le\lceil i/2\rceil\); therefore \(q(q-1)\cdots(q-\lceil i/2\rceil)\) is a factor. □

The number of combinatorial types of nonattacking configuration of _q_ (unlabelled) rooks is _q_!. To prove it we may substitute _n_=-1 into Equation (3.1) (by Theorem I.5.3) or apply Theorem I.5.8, which says that every piece with two basic moves has _q_! combinatorial configuration types.

