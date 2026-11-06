_Proof._ We give an isomorphism-preserving polynomial-time reduction from GI to the decision problem IS={(_K,k_)|_K_ has an independent set of size at least _k_}.

Let (_G,H_) be an instance of GI. If \(|V(G)|\neq|V(H)|\), output a fixed NO-instance of IS (e.g. (_K,_2) where _K_ is a single edge). Hence assume |_V(G_)|=|_V(H_)|=_n_.

## Reduction _R_.

We construct the conflict graph _K=K(G,H_) with

\(V(K):=V(G)\times V(H),\)

and for distinct \((u,v),(u',v')\in V(K)\) put an edge between them iff at least one of the following holds:

1. (_Function constraint_) \(u=u'\) or \(v=v'\).<tbc>

2. (_Adjacency inconsistency_) \(\mathbf{1}[(u,u')\in E(G)]\oplus\mathbf{1}[(v,v')\in E(H)]=1\).

<tbc>Define

\(R(G,H):=(K(G,H),n).\)

This is computable in polynomial time.

## Correctness.

We claim that

\((G,H)\in\mathsf{GI}\Longleftrightarrow(K(G,H),n)\in\mathsf{IS}.\)

If \(\varphi:V(G)\rightarrow V(H)\) is an isomorphism, then \(S:=\{(u,\varphi(u)):u\in V(G)\}\) is an independent set of size _n_ in _K(G,H_): type-(1) edges are avoided because \(\varphi\) is a bijection, and type-(2) edges are avoided because \(\varphi\) preserves adjacency. Hence \((K(G,H),n)\in\mathsf{IS}\).

Conversely, if _K(G,H_) has an independent set _S_ of size _n_, then constraint (1) implies that _S_ defines a bijection \(\varphi:V(G)\rightarrow V(H)\) by \(\varphi(u)=v\) iff \((u,v)\in S\). Independence of _S_ implies no type-(2) edge occurs between \((u,\varphi(u))\) and \((u',\varphi(u'))\), hence \((u,u')\in E(G)\) iff \((\varphi(u),\varphi(u'))\in E(H)\) for all \(u\neq u'\). Therefore \(\varphi\) is an isomorphism and \((G,H)\in\mathsf{GI}\).

## Isomorphism preservation.

View GI instances as attributed graphs \(\langle G,H\rangle\) (disjoint union with L/R vertex colors). If \((G,H)\cong(G',H')\), there exist isomorphisms \(\psi_G:G\rightarrow G'\) and \(\psi_H:H\rightarrow H'\). Define \(\Psi:V(K(G,H))\rightarrow V(K(G',H'))\) by

\(\Psi(u,v):=(\psi_G(u),\psi_H(v)).\)

Then \(\Psi\) preserves edges of type (1) (it preserves equality of coordinates) and of type (2) (since \(\psi_G,\psi_H\) preserve adjacency), hence \(K(G,H)\cong K(G',H')\). Also \(n=|V(G)|=|V(G')|\), so the parameter _k=n_ is preserved. Thus \(R(G,H)\cong R(G',H')\) as IS instances.

Therefore _R_ is an isomorphism-preserving reduction and \(\mathsf{GI}\le_p^\cong\mathsf{IS}\).

**Lemma 9.16.** GI \(\le_p^\cong\mathsf{SAT}\).

_Proof._ We define a polynomial-time, isomorphism-preserving many-one reduction from GI to SAT.

## Reduction.

Let (_G,H_) be an instance of GI. If \(|V(G)|\neq|V(H)|\), output a fixed unsatisfiable CNF (e.g. \((x)\wedge(\neg x)\)). Hence assume |_V(G_)|=|_V(H_)|=_n_.

Introduce Boolean variables

\(x_{u,v}\text{for each}u\in V(G),v\in V(H),\)

with the intended meaning "\(\varphi(u)=v\)".

We construct a CNF formula \(\Phi(G,H)\) consisting of the following clauses.

