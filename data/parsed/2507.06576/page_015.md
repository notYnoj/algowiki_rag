This implies that,<tbc>

\(\sum_{i=1}^m\sum_{F\in\mathcal{F}_{2w}(G_i)\backslash\mathcal{F}_{2w}^w(G_i,r)}y_F^i\ge mz>1.\)

<tbc>Using same argument as in the proof of Theorem 4, we can show that there exists \(1\le i\neq j\le m\) and \(F'\in\mathcal{F}_{2w}^w(H,v)\) such that

\(y_{F^\prime}>0,F'\cap E_i\notin\mathcal{F}_{2w}^w(G_i,r)\text{and}F'\cap E_j\notin\mathcal{F}_{2w}^w(G_j,r).\)

This means that there exists a vertex \(a\in V_i,b\in V_j\) such that the distance of _a_ and _b_ from _r_ is at least _w_, and they are both included in the connected component containing _r_ in \(H-F'\). Hence _u_ and _v_ are at least 2_w_ distance apart, and this contradicts the fact that \(F'\) is a 2_w_-diameter decomposition. Hence _z_=0 and this completes the proof of the theorem.

So far, we have shown that SDDs for any graph class closed under the 1-sum operation are consistent with those constructed for trees in Observation 1. We now state a simple Lemma 3, which will be useful in proving the lower bound on the integrality gap for cactus graphs in Section 6. From this point onward, by Theorem 4 and Theorem 5, we may restrict our attention to \(\mathcal{F}_{2w}^w(G,r)\) instead of F<sub>2_w_</sub>(_G_), for a given graph _G_ and vertex \(r\in V(G)\).

**Lemma 3.** _Let_ \(G\in\mathcal{G}\) _and let_ \(r\in V(G)\) _be an arbitrary vertex. Let P be any shortest path of length w starting at r, and denote its other endpoint by_ \(r'\)_. If_ \(y=\{y_F|F\in\mathcal{F}_{2w}^w(G,r)\}\) _is an SDD(G,_2_w,p,r), then:_<tbc>

\(F\cap E(P)\neq\emptyset\text{\textit{for all}}F\in\mathcal{F}_{2w}^w(G,r),\)

<tbc>_and_<tbc>

\(\sum_{F\in\mathcal{F}_{2w}^w(G,r)|F\cap E(P)|\ge 2}y_F\le(w\cdot p)-1.\)

<tbc>_Proof._ If there exists \(F\in\mathcal{F}_{2w}^w(G,r)\) such that \(F\cap E(P)=\emptyset\), then \(r,r'\) are within the same connected component in _G-F_, which contradicts the fact that \(F\in\mathcal{F}_{2w}^w(G,r)\). Let,<tbc>

\(A=\{F\in\mathcal{F}_{2w}^w(G,r)||F\cap E(P)|\ge 2\}\text{and}B=\{F\in\mathcal{F}_{2w}^w(G,r)||F\cap E(P)|=1\}.\)

<tbc>Note that _A,B_ forms a partition of \(\mathcal{F}_{2w}^w(G,r)\). Using the definition of _A_ and _B_, and the fact that \(\sum_{F\in A}y_F+\sum_{F\in B}y_F=1\), we can derive the statement of the theorem as follows:

\(\sum_{F\in A}y_F+1=2\cdot\sum_{F\in A}y_F+\sum_{F\in B}y_F\le\sum_{e\in E(P)}\sum_{F\in\mathcal{F}_{2w}^w(G,r)e\in F}y_F\le\sum_{e\in E(P)}p\le w\cdot p.\)

Note that the first inequality can be derived by showing that _y<sub>F</sub>_ appears at least twice in the right hand side if \(F\in A\), and exactly once if \(F\in B\).

We are now equipped to prove the lower bound on the integrality gap for cactus graphs, which will be the focus of the next Section 6.

## 6 \(\frac{20}{9}\) Lower Bound For Cactus Graphs

We are now ready to prove our first theorem. Suppose that _w_ is a fixed even integer. We will apply the tools developed in the previous sections to the family of cactus graphs. Let G be the family of cactus graphs, and define \(\alpha=\alpha_{\mathcal{M}(\mathcal{G})}\). Since G is closed under minors and subdivisions, Theorem 2 implies that G is \(SDD\big(2w,\frac{\alpha}{2w}\big)\)-acceptable. Let \(p=\frac{\alpha}{2w}\). Since G is<tbc>

