whose edges lie in both _G_ and _G+U_. Toggling it yields \(M'':=M'\triangle\mathcal{T}\) , which preserves every vertex degree and is therefore again an \(\alpha\)-factor of _G+U_. Moreover, \(\mathcal{T}\subseteq G+U\) ensures that \(M''\) is feasible in _G+U_. Since \(M'\) is min-cost \(\alpha\)-factor of _G+U_, \(c(M'')\ge c(M')\), meaning \(c(\mathcal{T}\cap M')\le c(\mathcal{T}\cap M)\). Similarly, \(\mathcal{T}\subseteq G\) implies that \(M\triangle\mathcal{T}\) is an \(\alpha\)-factor of _G_. Since _M_ is min-cost \(\alpha\)-factor of _G_, we get that \(c(\mathcal{T}\cap M)\le c(\mathcal{T}\cap M')\). The two inequalities together imply \(c(\mathcal{T}\cap M')=c(\mathcal{T}\cap M)\) and hence, \(c(M'')=c(M')\). Thus, \(M''\) is a min-cost \(\alpha\)-factor of _G+U_ such that \(|M\triangle M''|<|M\triangle M'|\), contradicting the minimality of \(M'\). This proves the claim. □

The following claim gives the last structural observation over \(M\triangle M'\) needed for our oracle.

**Lemma 7.6.** _Consider any minimal closed alternating trail_ T _in_ \(M\triangle M'\)_, i.e., no sub-trail of_ T _is a closed alternating trail. Then,_ T _is incident to any vertex of G through at most two edges of M and two edges of_ \(M'\).

_Proof._ We proceed by contradiction. Suppose there exists a minimal closed alternating trail T that is incident on a vertex _v_ through at least 6 edges (at least 3 from _M_ and 3 from \(M'\)). Because the subgraph induced by T is Eulerian, any vertex with a degree greater than 2 in this subgraph can be split to decompose the trail into smaller, edge-disjoint closed trails. Consequently, we can extract a smaller sub-trail \(\mathcal{T}'\) of T that passes through exactly 2 edges of _M_ and 2 edges of \(M'\) incident to _v_. This sub-trail \(\mathcal{T}'\) forms a valid closed alternating trail on its own, which directly contradicts the minimality of T . Hence, the claim holds. □

Now, we bound the number of edges of \(M\triangle M'\) incident on any vertex by analysing the closed alternating trails induced by the edges \(M\triangle M'\). It follows that if \(M'\) is the optimal witness of Theorem 7.5, then \(M\triangle M'\) can be decomposed into at most _f_ closed alternating trails. Consider the decomposition \(S^*=\{\mathcal{T}_1,\mathcal{T}_2,\dots,\mathcal{T}_j\},j\le f\) such that the number of closed alternating trails is maximised. Then, for each T_<sub>i</sub>_, no closed alternating sub-trail exists. From Theorem 7.6, the number of _M_-edges dropped at any vertex _v_ due to each T_<sub>i</sub>_ is at most 2. Combining this over all trails in _S_<sup>∗</sup>, we get that \(|\delta_G(v)\cap M\cap(M\triangle M')|=|\delta_{G+U}(v)\cap M'\cap(M\triangle M')|\le 2f\), i.e., the total number of _M_-edges dropped at any vertex _v_ is bounded by 2_f_. We now leverage this local bound to construct the auxiliary graph _H_.

## Construction of the auxiliary graph.

Let _M_ be the fixed initial \(\alpha\)-factor of the graph _G_=(_V,E_) and define \(f_v:=min(2f,\alpha(v))\), for \(v\in V\) . We construct an auxiliary graph \(H=(V_1\cup V_2\cup R\cup S,E_H)\), and define its degree bounds \(\beta\) as follows:

• **Layer 1 (drop layer):** Make a copy _V_<sub>1</sub> of the vertex set _V_ , such that for any vertex \(v\in V\) , _v_<sub>1</sub> denotes its copy in the set _V_<sub>1</sub>. Now, for each edge \(e=(a,b)\in M\), add the edge (_a_<sub>1</sub>_,b_<sub>1</sub>) with cost -**_c_**(_e_), and set \(\beta(v_1)=f_v\). (Selecting this edge in a \(\beta\)-factor of _H_ implies _e_ is _dropped_ from \(M'\)).<tbc>

• **Layer 2 (add layer):** Make another copy _V_<sub>2</sub> of the vertex set _V_ , such that for any vertex \(v\in V\) , _v_<sub>2</sub> denotes its copy in the set _V_<sub>2</sub>. Now, for each edge _e_=(_a,b_) of _G_ such that \(e\notin M\), add the edge (_a_<sub>2</sub>_,b_<sub>2</sub>) with cost +**_c_**(_e_), and set \(\beta(v_2)=f_v\). (Selecting this edge implies _e_ is _added_ to \(M'\)).<tbc>

• **Parallel edges:** For each \(v\in V\) , add _f<sub>v</sub>_ parallel edges from _v_<sub>1</sub> to _v_<sub>2</sub>, each with cost 0.<tbc>

• **Budget sinks** (_S,R_)**:** For each \(v\in V\) , add two vertices _s<sub>v</sub>,r<sub>v</sub>_ with degree bounds \(\beta(s_v)=\beta(r_v)=f_v\). Furthermore, add _f<sub>v</sub>_ parallel edges between _s<sub>v</sub>_ and _r<sub>v</sub>_, all of cost 0.

Because \(\beta\le 2f\) everywhere, the corresponding sensitivity oracle matrix for _H_ has a bounded dimension _N<sub>H</sub>=O(nf_), independent of the maximum capacity \(\alpha\).

