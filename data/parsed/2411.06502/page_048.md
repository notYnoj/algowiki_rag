Consequently, we may write

\(\mathrm{sim}(F[x..y),F'[x'..y'))=\mathrm{max}_{z\in[l(s)..l(r)]:x\le z}\big\{\mathrm{sim}(F[x..z),F'[x'..l(q')))\)<br> \(+\mathrm{sim}(F[z..y),F'[l(q')..r(s')))\big\}.\)

In this last expression the first summand can be obtained from Main Theorem 4 and Theorem 4.1 on \(F[l(s)..l(r)),F'[l(s')..l(q'))\), and the second summand from Lemma 5.9.

For (21), it suffices to use the reverse symmetry on (20).

For (22), note that it is a subset of the output of the \((r,s',q,q')\)-DISED instance.

This concludes the proof of Lemma 5.3.

## 5.4 Handling the base case

**Lemma 5.2.** _Consider an_ \((s,s',q,q')\)_-DISED instance of size m such that s immediately precedes q or s_<sup>∗</sup> _immediately precedes q_<sup>∗</sup>_. Then, we can solve the_ \((s,s',q,q')\)_-DISED instance in time_ \(\mathcal{O}(\mathrm{T}_\mathrm{MUL}(m)+m^{2+o(1)})\).

_Furthermore, if the DISED instance is unweighted and has global tree size_ D_, then the algorithm takes time_ \(\mathcal{O}(\mathrm{T}_\mathrm{MonMUL}(m,m,m,\mathrm{D})+m^{2+o(1)}g(\mathrm{D}))\) _where_ T<sub>MonMUL</sub>(_m,m,m,_D)=O(_f(m)g_(D)) _for some functions f,g._

**Proof.** It suffices to prove the case where _s_ immediately precedes _q_ since the case where \(s'\) immediately precedes \(q'\) equals to the former case under swap symmetry.

We perform a case distinction on where/whether the spine nodes are mapped by \(\mathrm{sim}(F[x..y),F'[x'..y'))\).

If neither _s_ nor any node \(r'\in S'\) such that \(s'\le r'<q'\) is mapped, then \(\mathrm{sim}(F[x..y),F[x'..y'))=\mathrm{sim}(F[x..l(q))+F[l(q)..y),F'[x'..l(q'))+F'[l(q')..y')\), as the spine node do not contribute to the similarity of the two forests. Via Proposition 3.10(ii) we compute

\(\mathrm{sim}(F[x..y),F'[x'..y'))=\mathrm{max}_{(z,z^\prime)\in B_1^\mathrm{T}(s,s^\prime,q,q^\prime):z\ge x,z^\prime\ge x^\prime}\big\{\mathrm{sim}(F[x..z),F'[x'..z'))\)<br> \(+\mathrm{sim}(F[z..w),F'[z'..w'))\)<br> \(+\mathrm{sim}(F[w..y),F'[w'..y'))\big\},\)

where the first and third summand can be obtained from Main Theorem 4 on the forests \(F[l(s)..l(q))\), \(F'[l(s')..l(q'))\) and \(F[r(q)..r(s)),F'[r(q')..r(s'))\), respectively, and the second summand from Input (i) of the \((s,s',q,q')\)-DISED instance. Note that in the unweighted setting, all values are at most global tree size O(D) and we can apply Theorem 4.1 in place of Main Theorem 4.

If _s_ is not mapped and a node \(r'\in S'\) such that \(s'\le r'<q'\) is mapped to a node in \(F[x..l(q))\), then we can use Lemma 4.10.

If _s_ is mapped to a node \(r'\in S'\) such that \(s'\le r'<q'\), then we must have \(F[x..y)=\mathrm{sub}(s)\) and we can compute

\(\mathrm{sim}(\mathrm{sub}(s),F[x'..y'))=\)<br> \(\mathrm{max}_{r^\prime\in S^\prime:s^\prime\le r^\prime<q^\prime}\big\{\eta(s,r')+\mathrm{sim}(F[x..l(q))+F[l(q)..y),F'[l(r')+1..r(r')-1))\big\}.\)

Note that the values \(\mathrm{sim}(F[x..l(q))+F[l(q)..y),F'[l(r')+1..r(r')-1))\) were already computed in the first two cases (distinguishing whether another node in \(S'\) is mapped or not). Therefore, there is nothing further to compute in this case.

