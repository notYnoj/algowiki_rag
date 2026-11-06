**Bijection constraints.**

1. _Each u maps somewhere:_<tbc>

<tbc>\(\vee_{v\in V(H)}x_{u,v}\text{for all}u\in V(G).\)<tbc>

2. _Each u maps to at most one v:_<tbc>

<tbc>\((\neg x_{u,v}\vee\neg x_{u,v^\prime})\text{for all}u\in V(G),v\neq v'\in V(H).\)<tbc>

3. _Injectivity (each v is used by at most one u):_<tbc>

<tbc>\((\neg x_{u,v}\vee\neg x_{u^\prime,v})\text{for all}v\in V(H),u\neq u'\in V(G).\)

## Adjacency consistency constraints.

For every pair of distinct vertices \(u,u'\in V(G)\) and distinct vertices \(v,v'\in V(H)\) such that<tbc>

\(\mathbf{1}[(u,u')\in E(G)]\oplus\mathbf{1}[(v,v')\in E(H)]=1,\)

<tbc>add the clause

\((\neg x_{u,v}\vee\neg x_{u^\prime,v^\prime}).\)

This construction is polynomial-time and yields a CNF formula of size polynomial in _n_.

## Correctness.

We show that \(\Phi(G,H)\) is satisfiable if and only if \(G\cong H\).

(\(\Rightarrow\)) Suppose \(\varphi:V(G)\rightarrow V(H)\) is an isomorphism. Set \(x_{u,\varphi(u)}=\) true for all \(u\in V(G)\) and all other variables to false. Then the bijection constraints are satisfied. For adjacency consistency, for any \(u\neq u'\) let \(v=\varphi(u)\) and \(v'=\varphi(u')\). Since \(\varphi\) is an isomorphism,

\((u,u')\in E(G)\Longleftrightarrow(v,v')\in E(H),\)

so the XOR condition is false and no adjacency-consistency clause is violated. Hence the assignment satisfies \(\Phi(G,H)\).

(\(\Leftarrow\)) Conversely, let _A_ satisfy \(\Phi(G,H)\). By constraints (1) and (2), for each \(u\in V(G)\) there is exactly one \(v\in V(H)\) with _A(x<sub>u,v</sub>_)= true; define \(\varphi(u)=v\). Constraint (3) implies that \(\varphi\) is injective, and since |_V(G_)|=|_V(H_)| it is a bijection. Now fix distinct \(u,u'\in V(G)\) and let \(v=\varphi(u)\), \(v'=\varphi(u')\). If exactly one of \((u,u')\in E(G)\) and \((v,v')\in E(H)\) holds, then the corresponding clause \((\neg x_{u,v}\vee\neg x_{u^\prime,v^\prime})\) would be falsified (both literals false), contradicting satisfaction. Therefore

\((u,u')\in E(G)\Longleftrightarrow(\varphi(u),\varphi(u'))\in E(H),\)

so \(\varphi\) is an isomorphism \(G\cong H\).

## Isomorphism preservation.

We take "isomorphism" between SAT instances to mean: there is a variable renaming (and clause permutation) mapping one CNF to the other. If \((G,H)\cong(G',H')\) as GI instances, there exist isomorphisms \(\psi_G:V(G)\rightarrow V(G')\) and \(\psi_H:V(H)\rightarrow V(H')\). Define the variable renaming \(\rho\) by

\(\rho(x_{u,v}):=x_{\psi_G(u),\psi_H(v)}.\)

Then \(\rho\) maps the three families of bijection constraints for (_G,H_) to the corresponding families for \((G',H')\), and it maps each adjacency-consistency clause to the corresponding clause in \(\Phi(G',H')\). Hence \(\Phi(G,H)\cong\Phi(G',H')\) as SAT instances, so the reduction is isomorphism-preserving.

Therefore \(\mathsf{GI}\le_p^\cong\mathsf{SAT}\).

**Lemma 9.17.** \(\mathsf{IS}\le_p^\cong\mathsf{MaxCut}\).

_Proof._ We use the standard gadget reduction from Independent Set to MaxCut from Barak’s online textbook \[Bar23\] and verify that it is also isomorphism-preserving.

