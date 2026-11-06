_Proof._ Let (_S,T_) be a minimum _s-t_ cut of G with value \(\nu(\mathcal{G})\). It suffices to show that (_S,T_) survives the contraction of _V_<sub>1</sub>_,...,V<sub>z</sub>_. Assume, for contradiction, that it did not. This means there exists _V<sub>i</sub>_ such that \(V_i\cap S\neq\emptyset\) and \(V_i\cap T\neq\emptyset\).

Since _H_ is a directed cut sparsifier of G, we have \(\nu(\mathcal{F})=\nu(H)\ge(1-\varepsilon)\cdot\nu(\mathcal{G})\). Therefore \(w_\mathcal{F}(S,T)\ge\nu(\mathcal{F})\ge(1-\varepsilon)\cdot\nu(\mathcal{G})\). Since (_S,T_) cuts through _V<sub>i</sub>_, we have<tbc>

\(w_K(S,T)\ge w_{K[V_i]}(S,T)\ge 3\varepsilon\cdot\nu(H)\ge 3\varepsilon(1-\varepsilon)\cdot\nu(\mathcal{G})\)

<tbc>where the second inequality uses the fact that _K_\[_V<sub>i</sub>_\] has connectivity (i.e. global min-cut value) at least \(3\varepsilon\cdot\nu(H)\). Furthermore, _K_ and F are disjoint and \(K\cup\mathcal{F}\unknown H\). We then have:

\(w_H(S,T)\ge w_\mathcal{F}(S,T)+w_K(S,T)\ge(1-\varepsilon)\cdot\nu(\mathcal{G})+3\varepsilon(1-\varepsilon)\cdot\nu(\mathcal{G})\)<br>
\(=(1-\varepsilon)(1+3\varepsilon)\cdot\nu(\mathcal{G}).\)

Finally, since G and _H_ are \((1\pm\varepsilon)\)-close in directed cut size, we then have

\(w_\mathcal{G}(S,T)\ge(1-\varepsilon)\cdot w_H(S,T)\ge(1-\varepsilon)^2(1+3\varepsilon)\cdot\nu(\mathcal{G})>\nu(\mathcal{G})\)

where the final inequality follows \(\varepsilon\in(0,\frac{1}{5})\). This gives rise to a contradiction as (_S,T_) is a minimum _s-t_ cut of G with value \(w_\mathcal{G}(S,T)=\nu(\mathcal{G})\).

## 4.1 Implementation in Cut-Query

We describe the implementation of Algorithm 1 in the cut-query model. As a reminder, in this setting, we do not have direct access to the full input graph _G_; instead, we are allowed to make _cut queries_ to _G_. The complexity of our algorithm is measured by the total number of such queries made during its execution.

**Lemma 3.2** (Modified RSW via cut query)**.** _Let_ G=(_G,F_) _be an input mixed graph where G is undirected and unweighted, and F be a directed bounded-weighted that is known explicitly. Then, there exists an algorithm that makes_ \(\widetilde{O}(n^{4/3}\nu(\mathcal{G})^{1/3})\) _cut-queries to G and w.h.p. computes a minimum s-t cut of_ G.

_Proof._ We specify such implementation as follows.

• In Step 2, we use Lemma 2.7 to w.h.p. construct \(G'\) which is an \(\varepsilon\)-cut sparsifier of _G_ with \(\widetilde{O}(n/\varepsilon^2)\) edges and edge weights bounded by \(\widetilde{O}(\varepsilon^2n)\).<tbc>

• Once obtained \(G'\), we can do Step 3,4,5,6 locally.<tbc>

• Step 7 can be done via Lemma 2.11.<tbc>

• Once Step 7 is completed, we can do Step 8 locally.

It remains to bound the query complexity. Following our implementation, Step 2 consumes \(\widetilde{O}(n/\varepsilon^2)\) cut queries. The number of queries in Step 7 is, up to a polylogarithmic factor, bounded by \(|G\langle V_1,..,V_z\rangle|\) via Lemma 2.11. This is also upper bounded by \((1+\varepsilon)\cdot|G'\langle V_1,..,V_z\rangle|\) as \(G'\) is a \(\varepsilon\)-cut sparsifier of _G_. Since \(G'\unknown K\cup\mathcal{F}\), we then have

\(|G'\langle V_1,..,V_z\rangle|\le|K\langle V_1,..,V_z\rangle|+|\mathcal{F}|\)<br>
\(\le 3\varepsilon n\cdot\nu(H)+n\cdot\sqrt{\nu(H)\cdot\widetilde{O}(\varepsilon^2n)}\text{(Lemma 2.5 and Lemma 2.2)}\)<br>
\(\le\widetilde{O}\left(\varepsilon n^{3/2}\nu(G)^{1/2}\right)\text{(}\nu(H)\le(1+\varepsilon)\nu(\mathcal{G})\text{)}\)

