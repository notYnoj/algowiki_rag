\(\blacktriangleright\) **Theorem 8.** _There is an_ \(\mathcal{O}((m+e(\varphi))logm)\)_-time algorithm that, given an m-clause 3-SAT formula_ \(\varphi\)_, outputs a graph_ \(G_\varphi\) _of twin-width at most 4 such that_

\(|V(G_\varphi)|=3m+(e(\varphi)+3m)\cdot 2\lceil log(3m)\rceil\)_, and_

\(\alpha(G_\varphi)=val(\varphi)+(e(\varphi)+3m)\cdot\lceil log(3m)\rceil\).

_Furthermore, a 4-sequence of_ \(G_\varphi\) _can be computed in_ \(\mathcal{O}(\|G_\varphi\|)\) _time._

**Proof.** Let \(J_\varphi\) be the graph with one vertex per literal occurrence in a clause of \(\varphi\), and an edge between every two literals that are either in the same clause or that are of the same variable with opposite signs. In particular, \(J_\varphi\) has exactly 3_m_ vertices and exactly \(3m+e(\varphi)\) edges (recall our definition of 3-SAT).

Then, \(G_\varphi\) is the _s_-subdivision of \(J_\varphi\) with \(s:=2\lceil log(3m)\rceil\). Note that \(G_\varphi\) can be built from \(\varphi\) in \(\mathcal{O}((m+e(\varphi))logm)\) time. By Lemma 5, \(G_\varphi\) has twin-width at most 4, and a 4-sequence of \(G_\varphi\) can be computed in \(\mathcal{O}(\|G_\varphi\|)\) time. Since \(G_\varphi\) is a _s_-subdivision of a 3_m_-vertex \((3m+e(\varphi))\)-edge graph, \(|V(G_\varphi)|=3m+(e(\varphi)+3m)\cdot s\).

The second item dates back to Poljak [25]. We sketch this classic fact.

The inequality \(\alpha(G_\varphi)\ge val(\varphi)+(e(\varphi)+3m)\cdot\frac{s}{2}\) holds, as there is an independent set of \(G_\varphi\) with one vertex corresponding to a satisfied literal for each clause satisfied by a fixed truth assignment that satisfies \(val(\varphi)\) clauses of \(\varphi\), and \(\frac{s}{2}\) vertices per subdivided edge of \(J_\varphi\).

The inequality \(\alpha(G_\varphi)\le val(\varphi)+(e(\varphi)+3m)\cdot\frac{s}{2}\) holds since a larger independent set of \(G_\varphi\) would contain more than \(val(\varphi)\) original vertices (those of \(J_\varphi\)). This would imply that \(J_\varphi\) has an independent set of size greater than \(val(\varphi)\). (We elaborate on this in the proof of Theorem 13.) The (consistent, partial) truth assignment setting the corresponding literals to true would contradict the definition of \(val(\varphi)\). \(\blacktriangleleft\)

Given a graph _G_ and a positive integer _k_, we denote by _G_<sup>[_k_]</sup> the _k-th lexicographic power_ of _G_ with _V(G_<sup>[_k_]</sup>)=_V(G)<sup>k</sup>_ and \((u_1,\dots,u_k)(v_1,\dots,v_k)\in E(G^{[k]})\) whenever there is some \(i\in[k]\) such that \(u_iv_i\in E(G)\) and for every \(h\in[i-1]\), _u<sub>h</sub>=v<sub>h</sub>_. The following is a folklore observation. We give a recent reference for completeness.

\(\blacktriangleright\) **Lemma 9** (see Lemma 7.12 in [10])**.** _For every graph G and integer_ \(k\ge 1\), \(\alpha(G^{[k]})=\alpha(G)^k\). _Furthermore, there is an algorithm that, given an independent set S of G_<sup>[_k_]</sup>_, outputs an independent set of G of size at least_ |_S_|<sup>1_/k_</sup> _in_ \(\mathcal{O}(\|G^{[k]}\|)\) _time._

The twin-width of every lexicographic power of a graph _G_ is equal to that of _G_.

\(\blacktriangleright\) **Lemma 10** (Lemma 7.11 in [10])**.** _For every graph G and integer_ \(k\ge 1\)_, tww(G_<sup>[_k_]</sup>)=_tww(G)._

_Furthermore, given a d-sequence of G, one can compute a d-sequence of G_<sup>[_k_]</sup> _in time_ O(|_V(G_<sup>[_k_]</sup>)|).

We now have all the ingredients to show our main result, which we restate for convenience.

\(\blacktriangleright\) **Theorem 1.** _Unless the ETH fails, there is a constant_ \(\gamma>0\) _such that Max Independent Set does not admit a polynomial-time_ \(n^{\gamma/(loglogn)^2}\)_-approximation algorithm on n-vertex graphs of twin-width at most 4, even when 4-sequences are given as part of the input._

**Proof.** Fix the constants \(\beta<1,B,c\) so as to satisfy Theorem 7. We make the following reduction. Every _N_-variable _m_-clause 3-SAT-_B_ formula \(\varphi\) is mapped to the graph \(H:=G_\varphi^{[k]}\) with \(k:=\lceil m/log^{c+2}m\rceil\). We will assume that _m_ is large enough. In particular, the following inequalities hold:

\(\text{1.}log\left(4(3B^2+6)log(3m)\right)<log(3m);\)<br> \(\text{2.}logm>2loglog^{c+2}m+log3;\)

