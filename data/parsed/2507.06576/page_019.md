the identified vertex again by _r<sub>i</sub>_. Define<tbc>

\(L'=\{(u_i,(G'_i,r_i))|i=1,\dots,l\}.\)

<tbc>Since G is closed under the 1-sum operation, we have \(G^{S(L^\prime)}\in\mathcal{G}\). See Figure 5 for an illustration:

By the assumption that G is strongly _SDD_(2_w,p_)-acceptable, and using Theorem 5 together with Definition 6, there exists an \(SDD(G^{S(L^\prime)},2w,p,r)\) distribution<tbc>

\(x=\{x_{F^\prime}|F'\in\mathcal{F}_{2w}^w(G^{S(L^\prime)})\},\)

<tbc>with the property that<tbc>

\(\sum_{F^\prime\in\mathcal{F}_{2w}^k(G^{S(L^\prime)},r)}x_{F^\prime}\ge R_{(\mathcal{G},2w,p)}^k.\)

<tbc>For each _j_=1_,...,m_, let _H<sub>j</sub>_ be the induced subgraph of \(G^{S(L^\prime)}\) on the vertex set

\(V(H_j)=V(G)\cup\big(\bigcup_{i=1}^lV(G_i^j)\big).\)

Observe that each _H<sub>j</sub>_ is an identical copy of _G_<sup>_S(L_)</sup>. Moreover, by construction of \(G^{S(L^\prime)}\) and the subgraphs _H<sub>j</sub>_, the following two properties hold for every fixed \(j\in\{1,\dots,m\}\):

1. For each vertex \(v\in V(H_j)\), we have<tbc>

<tbc>\(d_{H_j}(r,v)=d_{G^{S(L^\prime)}}(r,v).\)<tbc>

2. For each \(i\in\{1,\dots,l\}\) and each vertex \(v\in V(G_i^j)\), we have<tbc>

<tbc>\(d_{G_i^j}(v,r_i)=d_{H_j}(v,r_i)=d_{G^{S(L^\prime)}}(v,r_i).\)<tbc>

<tbc>**Claim 4.** _Fix_ \(j\in\{1,\dots,m\}\)_. The projection x(H<sub>j</sub>_) _is a feasible solution to LP_ (9).

_Proof of Claim._ Since _x_ is an _SDD(G_<sup>_S(L_)</sup>),2_w,p_), Lemma 2 implies that _x(H<sub>j</sub>_) is an _SDD(H<sub>j</sub>,_2_w,p_). Note that \(r\in V(G)\), and hence \(r\in V(H_j)\). Moreover, since<tbc>

\(\sum_{F^\prime\in\mathcal{F}_{2w}^w(G^{S(L^\prime)},r)}x_{F^\prime}=1,\) (10)

<tbc>we must also have<tbc>

\(\sum_{F^{\prime\prime}\in\mathcal{F}_{2w}^w(H_j,r)}x(H_j)_{F^{\prime\prime}}=1.\) (11)

G' 1
G1
u1 = r1
u3 = r3
u1 = r1
u3 = r3
G
G
u2 = r2
G3
u2 = r2
G2
G' 3
G' 2

Figure 5: The left graph is _G_<sup>_S(L_)</sup> and the right graph is \(G^{S(L^\prime)}\).

