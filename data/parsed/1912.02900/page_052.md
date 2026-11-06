<tbc>\(p,q\in X_u^s\cup Y_u\), and, since we have assumed that _Y<sub>u</sub>_ is a feasible solution for instance \(X_u^s\), the two points are satisfied in \(X_u^s\cup Y_u\), and hence in \(X\cup Y^*\). Otherwise, _q_ does not lie in the interior of strip _S(u_). Then, from Observation 6.9, if _R_ is the row on which point _p_ lies, then _R_ is an active row for instance \(X_u^s\), and the point that lies on the intersection of the row _R_ and the right boundary of strip _S(u_) was added to _Z_. This point satisfies the pair (_p,q_).

Therefore, we can now assume that both _p_ and _q_ lie on boundaries of strips \(\{S(u)|u\in U\}\). Since every pair of consecutive strips share a boundary, and since, from the above assumptions, _p_ lies to the left of _q_, we can choose the strips _S(u_) and _S(v_), such that _p_ lies on the left boundary of _S(u_), and _q_ lies on the right boundary of _S(v_). Notice that it is possible that _S(v_)=_S(u_).

Notice that, if _p_ lies on a row that is active for strip _S(u_), then a point that lies on the same row and belongs to the right boundary of the strip _S(u_) has been added to _Z_; this point satisfies the pair (_p,q_). Similarly, if _q_ lies on a row that is active for strip _S(v_), the pair (_p,q_) is satisfied by a point of _Z_ that lies on the same row and belongs to the left boundary of _S(v_).

Therefore, it remains to consider the case where point _p_ lies on a row that is inactive for _S(u_), and point _q_ lies on a row that is inactive for _S(v_). From Observation 6.9, both _p_ and _q_ belong to \(\hat{Y}\cup Z\).

The following observation will be useful for us. Recall that the points of _X<sup>c</sup>_ are not included in \(X\cup Y^*\).

**Observation 6.11** _Assume that there is some point_ \(r\neq p,q\)_, such that_ \(r\in\square_{p,q}\)_, and_ \(r\in X^c\)_. Then the pair_ (_p,q_) _is satisfied in set_ \(X\cup Y^*\).

**Proof:** Since \(r\in X^c\), and \(r\in\square_{p,q}\), there must be some strip _S(w_), that lies between strips _S(u_) and _S(v_) (where possibly _w=u_ or _w=v_ or both), such that point _r_ lies on the column _C<sub>w</sub>_ (recall that this is the unique active column of _S(w_) that may contain points of _X<sup>c</sup>_). But then the row _R_ to which point _r_ belongs is an active row for strip _S(w_). Therefore, two points, lying on the intersection of _R_ with the two boundaries of strip _S(w_) were added to _Z_, and at least one of these points must lie in \(\square_{p,q}\). Since \(Z\subseteq Y^*\), the observation follows. □

From the above observation, it is sufficient to show that some point \(r\in\hat{Y}\cup Z\cup X^c\) that is distinct from _p_ and _q_, lies in \(\square_{p,q}\). We distinguish between three cases.

The first case happens when \(p,q\in\hat{Y}\). Since set \(\hat{Y}\) is a feasible solution for instance _X<sup>c</sup>_, there is some point \(r\in\square_{p,q}\) that is distinct from _p_ and _q_, and lies in \(\hat{Y}\cup X^c\).

The second case happens when neither _p_ nor _q_ lie in \(\hat{Y}\), so both \(p,q\in Z\). Let \(u'\in U\) be the vertex for which strip \(S(u')\) lies immediately to the left of strip _S(u_). Since _p_ lies on a row that is inactive for strip _S(u_), but \(p\in Z\), such a vertex must exist, and moreover, the row _R_ to which _p_ belongs must be active for strip \(S(u')\). Therefore, the point lying on the intersection of the column \(C_{u^\prime}\) (the unique active column of \(S(u')\) containing points of _X<sup>c</sup>_) and _R_ belongs to _X<sup>c</sup>_; we denote this point by \(p'\).

Similarly, we let \(v'\in U\) be the vertex for which strip \(S(v')\) lies immediately to the right of _S(v_). Since _q_ lies on a row that is inactive for strip _S(v_), but \(q\in Z\), such a vertex must exist, and moreover, the row \(R'\) to which _q_ belongs must be active for strip \(S(v')\). Therefore, the point lying on the intersection of \(C_{v^\prime}\) and \(R'\) belongs to _X<sup>c</sup>_; we denote this point by \(q'\).

Since the set \(X^c\cup\hat{Y}\) of points is satisfied, some point \(r\in X^c\cup\hat{Y}\) that is distinct from \(p'\) and \(q'\), lies in \(\square_{p^\prime,q^\prime}\). Moreover, from Observation 2.3, we can choose this point so that it lies on the boundary of the rectangle \(\square_{p^\prime,q^\prime}\). Assume first that _r_ lies on the left boundary of this rectangle. Then, since<tbc>

