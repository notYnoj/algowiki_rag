_graph with a distinguished vertex_ \(r_i\in V(G_i)\)_. Define G_<sup>_S_(0)</sup>:=_G. For i_=1_,...,l, construct G_<sup>_S(i_)</sup> _by performing the 1-sum of G_<sup>_S(i_-1)</sup> _and G<sub>i</sub> at the vertices u<sub>i</sub> and r<sub>i</sub>. After all steps, we obtain the graph G_<sup>_S(l_)</sup>_, which we denote by G_<sup>_S(L_)</sup>_, where_

\(L=\{(u_i,(G_i,r_i))|i=1,\dots,l\}.\)

_Informally, G_<sup>_S(L_)</sup> _is the graph obtained by taking the_ 1_-sum of G with the graphs G_<sub>1</sub>_,...,G<sub>l</sub>, simultaneously identifying u<sub>i</sub> with r<sub>i</sub> for all i_=1_,...,l. See Figure 4 for an illustration:_

**Theorem 7.** _Suppose that_ G _is closed under the 1-sum operation, contains K_<sub>2</sub>_, and is strongly SDD_(2_w,p)-acceptable. Let_ \(G\in\mathcal{G}\), \(r\in V(G)\)_, and_ \(k\in\{1,\dots,w\}\)_. Let l be a natural number, and let_ \(u_1,\dots,u_l\in V(G)\) _be arbitrary vertices. For each i_=1_,...,l, let_ \(G_i\in\mathcal{G}\) _with a distinguished vertex_ \(r_i\in V(G_i)\)_. Define_

\(L=\{(u_i,(G_i,r_i))|i=1,\dots,l\}.\)

_Then there exists an SDD(G_<sup>_S(L_)</sup>,2_w,p,r_) _distribution_ \(y=\{y_F|F\in\mathcal{F}_{2w}^w(G^{S(L)})\}\) _for G_<sup>_S(L_)</sup> _such that_

\(\sum_{F\in\mathcal{F}_{2w}^k(G^{S(L)},r)}y_F\ge R_{(\mathcal{G},2w,p)}^k\ge 1-(w-k)p,\)

_and moreover, for each i_=1_,...,l, the projection y(G<sub>i</sub>_) _is an SDD(G<sub>i</sub>,_2_w,p,r<sub>i</sub>_) _for G<sub>i</sub>._

_Proof._ Let \(\mathcal{F}_{2w}^w=\mathcal{F}_{2w}^w(G^{S(L)},r)\) and \(\mathcal{F}_{2w}^k=\mathcal{F}_{2w}^k(G^{S(L)},r)\). For each _i_=1_,...,l_, define<tbc>

\(\mathcal{F}_i=\big\{F\in\mathcal{F}_{2w}^w\big|F\cap E(G_i)\in\mathcal{F}_{2w}^w(G_i,r_i)\big\},\mathcal{F}=\cap_{i=1}^l\mathcal{F}_i.\)

<tbc>It suffices to show that the following LP is feasible and has optimal value 0:

\(\mathrm{min}\sum_{F\in\mathcal{F}_{2w}^w\backslash\mathcal{F}}y_F\)<br>
\(\mathrm{s}.\mathrm{t}.\sum_{F\in\mathcal{F}_{2w}^k}y_F\ge R_{(\mathcal{G},2w,p)}^k,\)<br>
\(\sum_{F\in\mathcal{F}_{2w}^we\in F}y_F\le p\forall e\in E\big(G^{S(L)}\big),\) (9)

\(\sum_{F\in\mathcal{F}_{2w}^w}y_F=1,y_F\ge 0\forall F\in\mathcal{F}_{2w}^w.\)

By Theorem 5 and by the definition of \(R_{(\mathcal{G},2w,p)}^k\) (see Definition 6), LP (9) is feasible. Suppose, for contradiction, that the optimal value of (9) is _z\>_0. Let \(m>\frac{l^2}{z}\) . For each _i_=1_,...,l_, let \(G_i^1,\dots,G_i^m\) be _m_ disjoint copies of _G<sub>i</sub>_, and let \(r_i^j\in V(G_i^j)\) be the vertex corresponding to _r<sub>i</sub>_. Form \(G'_i\) by taking the 1-sum of \(G_i^1,\dots,G_i^m\) at \(r_i^1,\dots,r_i^m\), and denote<tbc>

G1
u1 = r1
u3 = r3
G
u2 = r2
G3
G2

Figure 4: The construction of _G_<sup>_S(L_)</sup> with _L_={(_u_<sub>1</sub>,(_G_<sub>1</sub>_,r_<sub>1</sub>)),(_u_<sub>2</sub>,(_G_<sub>2</sub>_,r_<sub>2</sub>)),(_u_<sub>3</sub>,(_G_<sub>3</sub>_,r_<sub>3</sub>))}.

