Since \(F=\bigcup_{i=1}^f\mathcal{F}_i\), we can compute _X_ by summing over the flows:<tbc>

\(X=\sum_{e\in E}w_F(e)\cdot\phi(e)=\sum_{i=1}^f\sum_{e\in\mathcal{F}_i}\phi(e)\le\sum_{i=1}^fn=nf.\) \(\text{(4)}\)

2. For any vertex \(v\in V\) , let _N(v_) denote the set of out-neighbors of _v_. Then, we can compute _X_ by summing over the vertices:<tbc>

\(X=\sum_{e\in E}w_F(e)\cdot\phi(e)=\sum_{v\in V}\sum_{u\in N(v)}w_F(v,u)\cdot\phi(v,u)\)<br>
\(\ge\sum_{v\in V}\sum_{u\in N(v)}\phi(v,u)\text{(weights are at least 1)}\)<br>
\(=\sum_{v\in V}\sum_{u\in N(v)}(\phi(u)-\phi(v)).\)

Since \(\phi\) is an injection and is a topological ordering, the values \(\phi(u)-\phi(v)\) among \(u\in N(v)\) are all distinct positive integers. Therefore, we have:<tbc>

<tbc>\(\sum_{u\in N(v)}(\phi(u)-\phi(v))\ge\sum_{j=1}^{|N(v)|}j\ge\frac{1}{2}\cdot|N(v)|^2.\)<tbc>

<tbc>Continuing the bound for _X_, we get:<tbc>

\(X\ge\sum_{v\in V}\frac{1}{2}\cdot|N(v)|^2\ge\frac{1}{2n}\cdot|E|^2\) \(\text{(5)}\)

where the last inequality follows from Cauchy-Schwarz and the fact that \(|E|=\sum_{v\in V}|N(v)|\).

Combining (4) and (5), we obtain:

\(nf\ge X\ge\frac{1}{2n}\cdot|E|^2.\)

Rearranging it completes the proof.

**Corollary 2.8.** _For any_ \(\varepsilon\in(0,1)\)_, there is a randomized algorithm that computes f such that_ \((1-\varepsilon)\nu(G)\le f\le(1+\varepsilon)\nu(G)\)_. The algorithm uses_ \(\widetilde{O}(n/\varepsilon^2)\) _cut queries to G and succeeds w.h.p._

_Proof._ Let _H_ be an \(\varepsilon\)-cut sparsifier computed by Lemma 2.7. Then, we have<tbc>

\(\nu(H)=min_{s-t\text{cut}(S,T)}|w_H(S,T)|\ge min_{s-t\text{cut}(S,T)}(1-\varepsilon)\cdot|E_G(S,T)|=(1-\varepsilon)\cdot\nu(G)\)

<tbc>and

\(\nu(G)=min_{s-t\text{cut}(S,T)}|E_G(S,T)|\le min_{s-t\text{cut}(S,T)}(1+\varepsilon)\cdot|w_H(S,T)|=(1+\varepsilon)\cdot\nu(H).\)

Hence, \(f=\nu(H)\), which can be computed free of costs given _H_, satisfies the desired bounds.

**Proposition 2.10.** _Let G_=(_V,E_) _be an underlying graph. Then, for any disjoint sets_ \(A,B\subseteq V\) _, we can determine_ FindEdge(_A,B_) _using either_

• _O_(1) _cut queries to G if_ FindEdge(_A,B_) _outputs_ "NONE" _(i.e._ \(E\cap(A\times B)=\emptyset\)_), or_<tbc>

