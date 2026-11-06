<tbc>(otherwise the definition proceeds the same way after renaming _u_ and \(u'\)). Now consider the tuples of vertex-colors<tbc>

\(x(u)=\big(L_{j,a_d^{PQ}}(u)\big)_{d=1}^s,y(u')=\big(L_{j,b_d^{PQ}}(u')\big)_{d=1}^s.\)

<tbc>The colors \(a_d^{PQ}\) are active on _V<sub>P</sub>_ and the colors \(b_d^{PQ}\) are active on _V<sub>Q</sub>_, so by our previous definition of the vertex-color maps \(L_{j,c}(\cdot)\) we have \(x(u),y(u')\in[j]^s\subseteq[H]^s\). If<tbc>

\(x_d(u)=(f(y(u')))_d\)

<tbc>for some _d_, let _d_<sub>0</sub> be the least such index and put \(c=a_{d_0}^{PQ}\). Otherwise, Lemma 3.1 gives an index _d_ for which<tbc>

\(y_d(u')=(g(x(u)))_d;\)

<tbc>let _d_<sub>0</sub> be the least such index and put \(c=b_{d_0}^{PQ}\). Finally, we define

\(\kappa_j(uu')=\big(c,\tau(L_{j,c}(u)L_{j,c}(u'))\big).\)

In either case, _c_ is active on exactly one of _V<sub>P</sub>,V<sub>Q</sub>_ and missing on the other. Hence, by definition of \(L_{j,c}(\cdot)\), one of \(L_{j,c}(u),L_{j,c}(u')\) lies in \[_j_\] and the other equals _j_+1, so the argument of \(\tau\) is indeed always an edge of _K_<sub>_H_+1</sub>. This completes the description of the recursive construction of the edge- and vertex-color maps. We now move on to the proof of the invariants.

## Verifying the invariants.

We prove by induction on the counter _j_=0,1_,...,H_ that the maps \(\kappa_j\) and _L<sub>j,c</sub>_ defined in the previous paragraph indeed satisfy the invariants (i)-(iv) claimed before. The assertions are immediately checked for _j_=0.

Now consider any \(1\le j\le H\), and suppose we already proved the invariants for all the counters 0,1_,...,j_-1. All the statements in invariant (ii) follow directly from the construction of the maps, and so this invariant indeed holds for counter _j_.

Next, we verify (i) for counter _j_. To do so, consider any edge _uv_ of _K<sub>V<sub>j</sub></sub>_ and let \((c,b)\in[M_j]\times[q]\) be the color assigned to _uv_ by \(\kappa_j\).

Suppose first that _uv_ is internal to some block _V<sub>P</sub>_. By invariant (ii), we have that \(\kappa_{j-1}(uv)=(d,b)\) where _d_ is unique such that \(\phi_P(d)=c\) and \(\phi_P:[M_{j-1}]\rightarrow[M_j]\backslash P\) is the fixed bijection from invariant (ii). By invariant (i) for counter _j_-1 which we assume inductively, we now have

\(b=\tau\big(L_{j-1,d}(u)L_{j-1,d}(v)\big)\text{and}L_{j-1,d}(u)\neq L_{j-1,d}(v).\)

Note that _c_ is active on _V<sub>P</sub>_. Hence, by our definition of _L<sub>j,c</sub>_ and since \(d=\phi_P^{-1}(c)\), we find that _L<sub>j,c</sub>(u_)=_L_<sub>_j_-1_,d_</sub>(_u_) and _L<sub>j,c</sub>(v_)=_L_<sub>_j_-1_,d_</sub>(_v_). Combining this with the equation line above implies that invariant (i) indeed holds in this case.

Next, suppose that _u_ and _v_ lie in different blocks _V<sub>P</sub>,V<sub>Q</sub>_. Our definition of \(\kappa_j(uv)\) for this case then directly implies that \(b=\tau(L_{j,c}(u)L_{j,c}(v))\), as desired, and that _c_ is active in one of _V<sub>P</sub>,V<sub>Q</sub>_ and missing in the other. The latter, together with the definition of \(L_{j,c}(\cdot)\), implies that one of _L<sub>j,c</sub>(u),L<sub>j,c</sub>(v_) must be in \[_j_\] while the other equals _j_+1. This<tbc>

