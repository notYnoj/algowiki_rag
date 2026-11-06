**Corollary B.5** _There is a c-approximation polynomial-time algorithm for the offline version of Problem B.3 iff there is an O(c)-approximation polynomial-time algorithm for the offline_ Min-Sat _problem. Similarly, there is a c-competitive algorithm for the online version of Problem B.3 iff there is a O(c)-competitive algorithm for the online_ Min-Sat _problem._

## C Proofs Omitted from Preliminaries

### C.1 Proof of Observation 2.7

For simplicity, we denote \(X'=X\cap S(v_1)\) and \(X''=X\cap S(v_2)\). Assume w.l.o.g. that \(|X'|\le|X''|\). Notice that, if the pair (_p<sub>i</sub>,p_<sub>_i_+1</sub>) of points in _S(v_) define a crossing of _L(v_), then one of _p<sub>i</sub>,p_<sub>_i_+1</sub> must lie in \(X'\). Every point \(p_j\in X'\) may participate in at most two pairs of points that define crossings: the pairs (_p_<sub>_j_-1</sub>_,p<sub>j</sub>_) and (_p<sub>j</sub>,p_<sub>_j_+1</sub>). Therefore, the total number of crossings of _L(v_) is at most \(2|X'|\).

### C.2 Proof of Observation 2.3

Since the set _Z_ is satisfied, rectangle \(\square_{p,q}\) must contain at least one point of _Z_ that is distinct from _p_ and _q_. Among all such points, let _r_ be the one with smallest \(\ell_1\)-distance to _p_. We claim that either _p.x=r.x_, or _p.y=r.y_. Indeed, assume otherwise. Then _p_ and _r_ are non-collinear, but no point of _Z_ lies in \(\square_{p,r}\backslash\{p,r\}\), contradicting the fact that _Z_ is a satisfied point set.

### C.3 Proof of Observation 2.4

It is sufficient to prove the observation for the case where C contains two consecutive active columns, that we denote by _C_ and \(C'\), which are collapsed into the column _C_. We can then apply this argument iteratively to collapse any number of columns.

Assume for contradiction that the set _S_<sub>|C</sub> of points is not satisfied, and let \(p,q\in S_{|\mathcal{C}}\) be a pair of points that are not satisfied. Note that, if _p_ and _q_ cannot both lie on the column _C_ in _S_<sub>|C</sub>. Moreover, if both _p_ and _q_ lie to the right, or to the left of the column _C_, then they continue to be satisfied by the same point \(r\in S\) that satisfied them in set _S_. We now consider two cases.

Assume first that _p_ lies to the left of the column _C_, and _q_ lies to the right of the column _C_ in point set _S_<sub>|C</sub>. Let _r_ be the point that satisfied the pair (_p,q_) in point set _S_. If _r_ lied on column _C_ in _S_, then it remains on column _C_ in _S_<sub>|C</sub>. If _r_ lied on column \(C'\) in _S_, then a copy of _r_ lies on column _C_ in _S_<sub>|C</sub>, and this copy continues to satisfy the pair (_p,q_). Otherwise, point _r_ belongs to set _S_<sub>|C</sub>, and it continues to satisfy the pair (_p,q_).

It now remains to consider the case when exactly one of the two points (say _p_) lies on the column _C_ in _S_<sub>|C</sub>. Assume w.l.o.g. that _q_ lies to the right of _p_ and below it in _S_<sub>|C</sub>. Then either _p_ belongs to _S_ (in which case we denote \(p'=p\)), or _p_ is a copy of some point \(p'\) that lies on column \(C'\) in _S_. Let _r_ be the point that satisfies the pair \((p',q)\) of points in _S_. Using the same reasoning as before, it is easy to see that either _r_ belongs to _S_<sub>|C</sub>, where it continues to satisfy the pair (_p,q_) of points, or a copy of _r_ belongs to _S_<sub>|C</sub>, and it also continues to satisfy the pair (_p,q_).

It is easy to verify that an analogue of Observation 2.4 holds for collapsing rows as well.

