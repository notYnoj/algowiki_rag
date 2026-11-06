## 6.4 Analysis

We start by showing that the solution that the algorithm returns is _T_-special.

**Observation 6.8** _Assuming that_ LeafBST(_X,T_) _returns a T-special solution, the solution Y_<sup>∗</sup> _returned by Algorithm_ RecursiveBST\((X,T,\rho)\) _is a T-special solution._

**Proof:** The proof is by induction on the recursion depth. The base of the induction is the calls to Procedure LeafBST(_X,T_), which return _T_-special solutions by our assumption.

Consider now some call to Algorithm RecursiveBST\((X,T,\rho)\). From the induction hypothesis, the resulting solution \(\hat{Y}\) for instance _X<sup>c</sup>_ is _T<sup>c</sup>_-special, and, for every vertex \(v\in U\), the resulting solution _Y<sub>v</sub>_ for instance \(X_v^s\) is _T<sub>v</sub>_-special. Since both _T<sup>c</sup>_ and every tree \(\{T_v\}_{v\in U}\) are subtrees of _T_, and since the points of _Z_ lie on boundaries of strips in \(\{S(v)\}_{v\in U}\), the final solution _Y_<sup>∗</sup> is _T_-special. \(\square\)

We next turn to prove that the solution _Y_<sup>∗</sup> computed by Algorithm RecursiveBST\((X,T,\rho)\) is feasible. In order to do so, we will use the following immediate observation.

**Observation 6.9** _Let Y_<sup>∗</sup> _be the solution returned by Algorithm_ RecursiveBST\((X,T,\rho)\)_, and let_ \(u\in U\) _be any vertex. Then:_

• _Any point_ \(y\in Y^*\) _that lies in the interior of S(u_) _must lie on an active row of instance_ \(X_u^s\).<tbc>

• _Any point_ \(y\in Y^*\) _that lies on the boundary of S(u_) _must belong to in_ \(\hat{Y}\cup Z\)_. Moreover, the points of_ \(\hat{Y}\cup Z\) _may not lie in the interior of S(u)._<tbc>

• _If R is an active row for instance_ \(X_u^s\)_, then set Z contains two points, lying on the intersection of R with the left and the right boundaries of S(u), respectively._

We are now ready to prove that the algorithm returns feasible solutions. In the following proof, when we say that a row _R_ is an active row of strip _S(u_), we mean that some point of instance \(X_v^s\) lies on row _R_, or equivalently, _R_ is an active row for instance \(X_v^s\).

**Theorem 6.10** _Assume that the recursive calls to Algorithm_ RecursiveBST _return a feasible special solution_ \(\hat{Y}\) _for instance X<sup>c</sup>, and for each_ \(v\in U\)_, a feasible special solution Y<sub>v</sub> for the strip instance_ \(X_v^s\)_. Then the point set_ \(Y^*=Z\cup\hat{Y}\cup(\bigcup_{v\in U}Y_v)\) _is a feasible solution for instance X._

**Proof:** It would be convenient for us to consider the set of all points in \(X^c\cup X\cup Y^*\) simultaneously. In order to do so, we start with the set \(X\cup Y^*\) of points. For every vertex \(v\in U\), we select an arbitrary active column _C<sub>v</sub>_ in strip _S(v_), and we then add a copy of every point \(p\in X_v^s\) to column _C<sub>v</sub>_. The resulting set of points, obtained after processing all strips _S(v_) is identical to the set _X<sup>c</sup>_ of points (except possibly for horizontal spacing between active columns), and we do not distinguish between them.

Consider any pair of points _p,q_ that lie in \(Y^*\cup X\), which are not collinear. Our goal is to prove that some point \(r\neq p,q\) with \(r\in X\cup Y^*\) lies in \(\square_{p,q}\). We assume w.l.o.g. that _p_ lies to the left of _q_. We also assume that _p.y\<q.y_ (that is, point _p_ is below point _q_); the other case is symmetric.

Assume first that at least one of the two points (say _p_) lies in the interior of a strip _S(u_), for some \(u\in U\). We then consider two cases. First, if _q_ also lies in the interior of the same strip, then<tbc>

