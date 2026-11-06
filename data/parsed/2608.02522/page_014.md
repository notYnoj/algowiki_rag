implies that \(L_{j,c}(u)\neq L_{j,c}(v)\). Altogether, this verifies invariant (i) also in the case that _u,v_ belong to different blocks.

We now move on to invariant (iii). So consider any two distinct palettes \(P,Q\in\mathcal{P}_j\) and consider any edge _uv_ with \(u\in V_P\) and \(v\in V_Q\). It follows from our definition of \(\kappa_j(uv)\), that the primary color of the edge _uv_ under \(\kappa_j\) always lies in the union of _s_ colors chosen from _Q_\\_P_ and _s_ colors chosen from _P_\\_Q_. Hence, the primary color of _uv_ always lies in the symmetric difference \(P\Delta Q\). This verifies the first part of invariant (iii).

Now consider any \(c\in[M_j]\) which is active on _V<sub>P</sub>_ but missing on _V<sub>Q</sub>_ (so \(c\in Q\backslash P\)), and fix any vertex \(v\in V_Q\). We have to show that all \(u\in V_P\) for which the primary color of _uv_ under \(\kappa_j\) equals _c_ are assigned the same color by \(L_{j,c}(\cdot)\).

To prove this, consider first the case that _P\<Q_. If any edge from _V<sub>P</sub>_ to _v_ has the first coordinate of \(\kappa_j\) equal to _c_, then we must have \(c\in\{a_1^{PQ},\dots,a_s^{PQ}\}\). In fact, there will be a unique \(d_0\in[s]\) such that \(c=a_{d_0}^{PQ}\) and

\(L_{j,a_{d_0}^{PQ}}(u)=f((L_{j,b_d^{PQ}}(v))_{d=1}^s)_{d_0}.\)

In particular, _u_ must satisfy \(L_{j,c}(u)=f((L_{j,b_d^{PQ}}(v))_{d=1}^s)_{d_0}\). Since the right hand side depends only on _v_ and _d_<sub>0</sub> (and since _d_<sub>0</sub> is uniquely determined by _c_), we can see that the color _L<sub>j,c</sub>(u_) is uniquely determined, independent of our choice of _u_.

Similarly, if _Q\<P_ and at least one edge from _V<sub>P</sub>_ to _v_ has primary color under \(\kappa_j\) equal to _c_, then there is a unique index \(d_0\in[s]\) such that \(c=b_{d_0}^{QP}\) which satisfies

\(L_{j,c}(u)=g((L_{j,a_d^{QP}}(v))_{d=1}^s)_{d_0}.\)

Again, this shows that _L<sub>j,c</sub>(u_) is uniquely determined by _v_ and _c_, independent of our choice of _u_.

Thus, in both cases we obtain the desired statement claimed in the invariant (iii), concluding its proof.

So far we have proved invariants (i)-(iii) at stage _j_. It remains to verify invariant (iv), which we do next. Suppose towards a contradiction that a member of O<sub>_r_+1</sub>, i.e., an odd cycle of length at most 2_r_+3, was a monochromatic subgraph of the edge-colored complete graph \((K_{V_j},\kappa_j)\). Fix such a cycle _C_ and denote its cyclic vertex-sequence as<tbc>

\(v_1v_2\cdots v_\ell v_1,\)

<tbc>where \(\ell\in\{3,5,\dots,2r+3\}\) is the length of _C_. Let \((c,b)\in[M_j]\times[q]\) be the color such that every edge of _C_ is assigned color (_c,b_) by \(\kappa_j\).

Put<tbc>

\(z_i=L_{j,c}(v_i)(1\le i\le\ell).\)

<tbc>By invariant (i) for counter _j_, cyclically consecutive colors _z<sub>i</sub>_ are distinct. Hence, the cyclic sequence of vertex-colors

\(z_1z_2\cdots z_\ell z_1\)

can be seen as a closed odd walk in the complete graph \(K_{[j+1]}\subseteq K_{[H+1]}\) all of whose edges have color _b_ under \(\tau\). By our initial assumption on the edge-coloring \(\tau\) of _K_<sub>[_H_+1]</sub>,<tbc>

