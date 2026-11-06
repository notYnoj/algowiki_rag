<tbc>For treedepth, arrange the vertices of _C_ on one root-to-leaf chain. If _k\>_0, make every original vertex outside _C_ a child of the last vertex of this chain. Every edge of _G_ has an endpoint in _C_, so its endpoints are comparable in the resulting rooted tree. Attach a pendent vertex of a vertex outside _C_ below that vertex. Attach a pendent vertex of a vertex in _C_ directly below its center. If _k_=0, instead take every original vertex as a root and hang its pendent vertices below it. All edges of _H_ then join comparable vertices, and the height is at most _k_+2. Thus \(td(H)+fvs(H)\le 2k+2\), completing the parameterized reduction from the W\[1\]-hard List Coloring problem of Fiala et al. \[14\].

### C.2 Reductions from Equitable Coloring

Let (_G,q_) be an Equitable Coloring instance with _n_ vertices. We may assume \(q\le n\), since instances with _q\>n_ are trivially positive and can be mapped to a fixed yes-instance. Write _n=aq+r_, where \(0\le r<q\). Choose any initial coloring \(\varphi\) in which colors 1_,...,r_ occur _a_+1 times and the remaining colors occur _a_ times.

#### Arbitrary swaps.

Use the instance \((G,q,\varphi,n-1)\). If _G_ has an equitable coloring, rename its colors so that the _r_ large color classes receive names 1_,...,r_. It now has exactly the initial histogram and is reachable by Lemma 1. Conversely, swaps preserve every color-class size, so any reachable proper coloring is equitable. The graph, and hence both bandwidth and distance to disjoint paths, is unchanged. The known hardness of Equitable Coloring proves the two claims for arbitrary swaps.

#### A cone for distance to disjoint paths.

Create _H_ by adding a universal vertex _z_ to _G_, use the palette \[_q_+1\], and set \(\varphi(z)=q+1\). For swaps use budget _n_. For slides use budget 3_n_. If \(\psi\) is an equitable coloring of _G_, rename it to the initial histogram and keep color _q_+1 on _z_. Choose a token matching that fixes _z_. The induced permutation on _V(G_) admits a factorization into at most _n_-1 transpositions, so the swap budget suffices. For slides, perform every such transposition of \(u,v\in V(G)\) by (_u,z),(z,v),(u,z_). This restores the color of _z_, and 3_n_ moves suffice.

For the reverse implication, let \(\psi\) be a reachable proper coloring of _H_. Its color histogram equals the initial one. Since _z_ is universal, \(\psi(z)\) occurs exactly once. If \(\psi(z)=q+1\), restriction to _G_ is immediately an equitable _q_-coloring. Otherwise, let \(\psi(z)=i\in[q]\). Then the initial multiplicity of _i_ was one, and the unique token of color _q_+1 lies in _G_. Exchanging the names _i_ and _q_+1 in \(\psi\) gives a proper coloring with _z_ colored _q_+1 whose restriction to _G_ has precisely the original equitable multiplicities. Finally, if _S_ is a modulator of _G_ to disjoint paths, then \(S\cup\{z\}\) is such a modulator of _H_. Hence \(ddp(H)\le ddp(G)+1\), the new palette has size _q_+1, and _z_ is dominating.

#### Sliding with bounded bandwidth.

For slides, we make the construction connected as follows. For each \(j\in[n]\), add a clique _C<sub>j</sub>_ of size _q_+1 and initially use every color in \[_q_+1\] once on it. For _j\<n_, join the color-(_q_+1) vertex of _C<sub>j</sub>_ to the color-1<tbc>

