subtree. This however implies that \(u'_i\in R(v)\) because \(\ell(u'_i)<\ell(u_i)\) and no node on the path between _u<sub>i</sub>_ and \(u'_i\)) has label smaller than \(\ell(u'_i)\). Moreover, \(u'_i\) precedes _u<sub>i</sub>_ in _R(v_) meaning that among one for the first _i_ queries, \(u'_i\) must have been queried -- a contradiction with the fact that \(u'_i\) belongs to \(T\langle U_i,x\rangle\).

**Lemma 5.7.** _For each target node, the total number of R-queries made by_ A<sub>_S_<sup>+</sup></sub> _is at most_ 2log<sub>2</sub>_n._

_Proof._ It follows from Lemmas 5.5 and 5.6 that after any two subsequent _R_-queries the value of parameter _C<sub>i</sub>_ increases by at least 1.

The next two lemmas will be used to bound the number of _S_-queries in _S_<sup>+</sup> receiving a ‘down’ reply to be at most 2log<sub>2</sub>_n_.

**Lemma 5.8.** _If all nodes in R(v_) _have been queried by_ A<sub>_S_<sup>+</sup></sub> _after an i-th query for some_ \(v\in V\) _and v is the root of_ \(T\langle U_i,x\rangle\)_, then_ \(\ell(v)=C_{i+1}\).

_Proof._ Suppose for a contradiction that \(\ell(v)\neq C_{i+1}\). Since _v_ belongs to \(T\langle U_i,x\rangle\), we have that \(\ell(v)>C_{i+1}\). Thus, by construction, there exists a light node _u_ in \(T\langle U_i,x\rangle\) with \(\ell(u)=C_{i+1}\) such that all internal nodes on the path between _v_ and _u_ have labels larger than \(\ell(u)\). Therefore, _u_ belongs to _R(v_) because _v_ is the root of \(T\langle U_i,x\rangle\). This implies that _u_ has been already queried -- a contradiction with _u_ being in \(T\langle U_i,x\rangle\).

**Lemma 5.9.** _If the i-th query of_ A<sub>_S_<sup>+</sup></sub> _is an S-query performed on a light node and the reply is ‘down’, then_ \(T\langle U_i,x\rangle\) _has no light node with label C<sub>i</sub>._

_Proof._ Suppose that the _i_-th query is performed on a node _u_ in _S(v_) for some \(v\in V\) . Clearly, _v_ is the root of \(T\langle U_{i-1},x\rangle\). Since the considered query is an _S_-query, all vertices in _R(v_) have been already queried. Thus, by Lemma 5.8, \(\ell(v)=C_i\). By construction, _v_ is the only light node in this subtree having label _C<sub>i</sub>_. Since the reply to the _i_-th query is ‘down’, _v_ does not belong to \(T\langle U_i,x\rangle\).

We are now ready to prove Proposition 3.2.

By Lemma 5.7, in A<sub>_S_<sup>+</sup></sub>, the total number of _R_-queries does not exceed 2log<sub>2</sub>_n_. Note that since _S_ is stable, for each target node _x_, the _S_-queries performed by A<sub>_S_<sup>+</sup></sub> are a subsequence of the queries performed by A_<sub>S</sub>_. Therefore, the potentially additional queries made by A<sub>_S_<sup>+</sup></sub> with respect to A_<sub>S</sub>_ are _R_-queries. By Observation 5.1, each _R_-query is made on a light node. By definition of function \(\mathtt{COST}^{(\omega,c)}\) and Observation 5.1, any _R_-query increases the value of \(\mathtt{COST}^{(\omega,c)}\) of A<sub>_S_<sup>+</sup></sub> with respect to the value of \(\mathtt{COST}^{(\omega,c)}\) of A_<sub>S</sub>_ by at most \((2c+1)\omega\). Hence we have:<tbc>

\(\mathtt{COST}_{\mathcal{A}_S^+}^{(\omega,c)}(T)\le\mathtt{COST}_{\mathcal{A}_S}^{(\omega,c)}(T)+2(2c+1)\omega log_2n.\)

<tbc>By Lemmas 5.6 and 5.9, the total number of queries in strategy A<sub>_S_<sup>+</sup></sub> to light nodes receiving ‘down’ replies can be likewise bounded by 2log<sub>2</sub>_n_. Since each such query introduces a rounding difference of at most \((2c+1)\omega\) when comparing cost functions \(\mathtt{COST}\) and \(\mathtt{COST}^{(\omega,c)}\), we thus obtain:

\(\mathtt{COST}_{\mathcal{A}_S^+}(T)\le\mathtt{COST}_{\mathcal{A}_S^+}^{(\omega,c)}(T)+2(2c+1)\omega log_2n.\)

Combining the above observations gives the claim of the Proposition.

