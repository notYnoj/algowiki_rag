\(\blacktriangleright\) **Lemma 19.** _Let_ G _be a directed graph with a designated source node s, and let t be a vertex satisfying_ max-flow(_s,t,_G)=_f, for some positive integer f. Then a_ \((min\{f,\lambda\}+k-1)\)_- FTRS of_ G _that differs from_ G _only at in-edges of t is a_ \((\lambda,k)\)_-FT-BFP for_ G.

**Proof.** Let H be a \((min\{f,\lambda\}+k-1)\)-FTRS of G that deviates from G only at in-edges of _t_. It follows from Lemma 18 that the subgraph H is a \((min\{f,\lambda\},k)\)-FT-BFP for G.

The claim trivially holds true if \(f\ge\lambda\), so let us consider the scenario \(f<\lambda\). Consider a set _F_ of at most _k_ edge failures in G, and let _p_ be max-flow(_s,t,_G\\_F_). Since \(p\le f<\lambda\) and H is a (_f,k_)-FT-BFP, the max-flow from _s_ to _t_ in H\\_F_ must be exactly _p_.

Since G and H only differs at in-edges of _t_, it follows from Lemma 12 that for each \(v\in V(\mathcal{G})\), max-flow\((s,v,\mathcal{H}\backslash F)\ge min(\lambda,max-flow(s,v,\mathcal{G}\backslash F))\). This proves that H is a \((\lambda,k)\)-FT-BFP for G.

We now provide construction of a \((\lambda,k)\)-FT-BFP that bounds the in-degree of a single destination node _t_.

\(\blacktriangleright\) **Lemma 20.** _Let_ G _be an n vertex, m edges directed graph with a designated source node s, and t be any arbitrary vertex in_ G_. Then for any_ \(\lambda,k\ge 1\)_, we can compute in_ \(O(2^k\lambda m)\) _time a_ \((\lambda,k)\)_-FT-BFP for_ G _in which the in-degree of t is bounded above by_ \(2^k\lambda\).

**Proof.** Let _f_=max-flow(_s,t,_G). We present a construction of a \((\lambda,k)\)-FT-BFP, say H, by considering the following two cases.

Case 1. max-flow\((s,t,\mathcal{G})\ge\lambda+k\):<br> Let us start by taking a look at the scenario \(f\ge\lambda+k\). In this case we can choose any \(\lambda+k\) incoming edges of _t_ which carry a flow of \(\lambda+k\) from _s_ to _t_ and discard all other incoming edges of _t_ to construct H. The resulting graph H will be a \((\lambda,k)\)-FT-BFP of G due to Lemma 19, and the in-degree of _t_ in H will be \(\lambda+k\le 2^k\lambda\).

Case 2. max-flow\((s,t,\mathcal{G})<\lambda+k\):<br> We next consider the case \(f<\lambda+k\). In this case we use Theorem 14 to compute a \((min\{f,\lambda\}+k-1)\)-FTRS of G, say H<sub>0</sub>, such that the in-degree of _t_ in H<sub>0</sub> is at most \(2^kmin\{f,\lambda\}\). We obtain the graph H from G by limiting the incoming edges of _t_ to those present in H<sub>0</sub>. The resulting graph H will be a \((\lambda,k)\)-FT-BFP of G due to Lemma 19.

We conclude with the following theorem that directly follows by combining together Lemma 13 and Lemma 20.

\(\blacktriangleright\) **Theorem 21.** _Let_ G _be an n vertex, m edges directed graph with a designated source node s. Then for any_ \(\lambda,k\ge 1\)_, we can compute in_ \(O(2^k\lambda mn)\) _time a_ \((\lambda,k)\)_-FT-BFP for_ G _in which the in-degree of every vertex is bounded above by_ \(2^k\lambda\).

## 5 Matching Lower Bound

We shall now show that for each \(\lambda,k\), \(n(n\ge 3\lambda 2^k)\), there exists a directed graph G with _O(n_) vertices whose \((\lambda,k)\)-FT-BFP must have \(\Omega(2^k\lambda n)\) edges.

The construction of graph G is as follows. Let \(B_1,\dots,B_\lambda\) be vertex-disjoint complete binary trees of height _k_ rooted at vertices _r_<sub>1</sub>_,...,r<sub>k</sub>_, and let _s_ be a new vertex have an edge to each of the _r<sub>i</sub>_’s. Let _X_ denote the set of leaf nodes of these \(\lambda\) trees, and let _Y_ be another set containing \(n-\sum_{i=1}^\lambda|V(B_i)|-1(\ge n/3)\) vertices. Then the graph _G_ is obtained by adding an

