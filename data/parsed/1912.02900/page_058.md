and from \(\rho_{\pi^\prime}\) the columns of C<sub>1</sub>, then the two orderings are defined over the same set of columns and they are identical.

It is easy to verify that the resulting profile \(\pi'\) must be legal for _t_. Therefore, profile \(\pi'\) was considered by the algorithm. Since \(\hat{Z}'\) and _P_ are not conflicting, it is easy to verify that for any other set \(\tilde{Z}\) of points that lie on rows _R_<sub>1</sub>_,...,R<sub>t</sub>_ and are consistent with profile \(\pi'\), set \(\mathrm{top}(\tilde{Z})\) does not conflict with _P_. Therefore, \(\pi'\) must be a candidate profile for \(\pi\). We conclude that \(|T[t,\pi']|\le|\hat{Z}|\), and \(|T[t,\pi]|\le|T[t,\pi']|+|P|=|Z^*|\), so \(|Z|\le|Z^*|\) must hold.

The output of the algorithm is a set \(T[m,\pi]\backslash X\) of smallest cardinality among all profiles \(\pi\in\Pi\) that are consistent with _m_. It is immediate to verify that this is a feasible and optimal solution for _X_.

As observed before, the number of entries in the dynamic programming table is \(m\cdot n^{O(n)}\), and computing each entry takes time _n_<sup>_O(n_)</sup>. Therefore, the total running time of the algorithm is bounded by \(m\cdot n^{O(n)}\).

## 6.6 Leaf Instances: Proof of Theorem 6.7

In this section we provide we prove 6.7. Recall that the input is a semi-permutation point set _X_ and a partitioning tree _T_ for _X_. Our goal is to compute a _T_-special solution for _X_, of cost at most 2_mh_ where _m_=|_X_| and _h_=height(_T_) in time poly(_m_).

For every point \(p\in X\), we define a new set of points _Z(p_), as follows. For every vertex \(v\in V(T)\) of the tree with \(p\in S(v)\), we add two points to _Z(p_), that have the same _y_-coordinate as _p_: one lying on the left boundary of _S(v_), and one lying on its right boundary; we call these two points the _projection of p to the boundaries of S(v_). We then set \(Y=\bigcup_{p\in X}Z(p)\).

First, it is easy to see that the solution is _T_-special, as _Y_ only contains points on boundaries of strips _S(v_), for \(v\in V(T)\). Moreover, for every point \(p\in X\), the set of all vertices \(v\in V(T)\) with \(p\in S(v)\) lie on a single root-to-leaf path of the tree _T_. Therefore, \(|Z(p)|\le 2h\), and \(|Y|\le 2mh\).

Finally, we argue that the set \(X\cup Y\) of points is satisfied. Consider any pair of points \(p,q\in X\cup Y\) , where _p.x\<q.x_. We assume that and _p.y\<q.y_ (other case is symmetric). Assume first that at least one of these two points, say _p_, lies in _X_. Let \(v\in V(T)\) be the unique leaf vertex with \(p\in S(v)\). Then the copy of _p_ lying on the right boundary of _S(v_) was added to _Z(p_), and this point lies in \(\square_{p,q}\backslash\{p,q\}\).

Therefore, we can assume that both _p_ and _q_ lie in _Y_ . Denote by \(p'\) and \(q'\) be the points in _X_, such that \(p\in Z(p')\) and \(q\in Z(q')\).

Let _v_ be the node of the tree for which _S(v_) contains both \(p'\) and \(q'\), such that the width of _S(v_) is the smallest. Let _u_ and _w_ be children of _v_ such that _S(u_) contains \(p'\) and _S(w_) contains \(q'\), and _L_ be the vertical line in the middle that splits _S(v_) into _S(u_) and _S(w_). Assume first that at least one of the two points, _p_ or _q_ (say _p_) lies either on the boundary of _S(v_), or outside _S(v_). Since for every ancestor _x_ of vertex _v_, both \(p',q'\in S(x)\), both \(p'\) and \(q'\) were projected to the boundaries of _S(x_). Therefore, there is a copy of \(q'\) on the same column where _p_ lies, satisfying \(\square_{p,q}\).

We can therefore assume from now on that both _p_ and _q_ lie in the interior of _S(v_). But then _p_ must lie _S(u_) and _q_ must lie in _S(w_). Since both \(p',q'\) are projected to the line _L=L(v_), the pair (_p,q_) must be satisfied.

We remark that this approximation algorithm corresponds to an algorithm that uses a static tree<tbc>

