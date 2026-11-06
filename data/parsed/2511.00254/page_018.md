**Lemma 5.1.** _Let f be a strongly uncrossed walk-multiflow, with a fixed strongly uncrossed parallelization_ \(\phi\)_. For distinct commodities_ \(h,h'\in E(H)\)_, the sets of inner edges of h and_ \(h'\) _are disjoint._

_Proof._ To prove the result, we show that if an edge _e_ is shared between the two single-commodity flows in _G_, then it is an outer edge for one of the commodities.

**Claim 5.2.** \(G_\phi[h']\) _is entirely contained within a single sector of h, and_ \(G_\phi[h]\) _is entirely contained within a single sector of_ \(h'\).

_Proof._ By symmetry, it suffices to prove the first part. Recall that in \(G_\phi\), two paths for distinct commodities are completely disjoint, so each individual \(\widehat{P}\in\widehat{\mathcal{P}}^{h^\prime}\) lies in at most one sector of _h_. However, all paths of \(\widehat{\mathcal{P}}^{h^\prime}\) share common terminals in \(G_\phi\), so it must be the same sector for all of \(\widehat{\mathcal{P}}^{h^\prime}\). \(\diamond\)

**Claim 5.3.** _Either_ \(G_\phi[h']\) _is contained in the outer sector of h, or_ \(G_\phi[h]\) _is contained in the outer sector of_ \(h'\).

_Proof._ By the previous claim and by symmetry, it suffices to show that if \(G_\phi[h']\) is contained within an inner sector of _h_, then \(G_\phi[h]\) is contained within the outer sector of \(h'\). Suppose \(G_\phi[h']\) is contained within the inner sector of _h_ defined by paths \(\widehat{P}_i\) and \(\widehat{P}_{i+1}\). Since \(\text{CW}(\widehat{P}_i,\widehat{P}_{i+1})\) is an inner sector, it is bounded, which means \(G_\phi[h']\) is contained in the interior of the curve \(\widehat{P}_i\bullet\widehat{P}_j\) rather than the exterior. This implies that \(\widehat{P}_i\) and \(\widehat{P}_{i+1}\) are contained within the infinite face of \(G_\phi[h']\), and so therefore are in the outer sector of \(h'\). Since the entirety of \(G_\phi[h]\) is within the same sector of \(h'\), it is within the outer sector of \(h'\). \(\diamond\)

Now, without loss of generality, suppose that \(G_\phi[h]\) is contained within the outer sector of \(h'\). Then \(G_\phi[h]\) and \(G_\phi[h']\) both contain one of the copies of the shared edge _e_. The copy belonging to _h_ is contained in the infinite face of \(G_\phi[h']\), and (by how \(G_\phi\) is constructed) so too is the copy belonging to \(h'\). So then _e_ is an outer edge of \(h'\), not an inner edge.

Now, associating the circular ordering _P_<sub>1</sub>_,...,P<sub>k</sub>_ to P_<sup>h</sup>_ corresponding to the clockwise ordering \(\widehat{P}_1,\dots,\widehat{P}_k\) of \(\widehat{\mathcal{P}}^h\), we prove the second key property.

**Lemma 5.4.** _Suppose that in G,_ \(P_i,P_j\in\mathcal{P}^h\) _share an edge e. One of the following holds:_

• _every path between P<sub>i</sub> and P<sub>j</sub> in the circular ordering also uses e, or_<tbc>

• _every path between P<sub>j</sub> and P<sub>i</sub> in the circular ordering also uses e._

_Proof._ In \(G_\phi\), consider subdividing the copies of _e_ belonging to \(\widehat{P}_i\) and \(\widehat{P}_j\) by adding one node into each edge. Then add an edge \(e'\) between the two new nodes, adding \(e'\) such that it only crosses copies of _e_. The new edge either separates \(\text{CW}(\widehat{P}_i,\widehat{P}_j)\) or it separates \(\text{ACW}(\widehat{P}_i,\widehat{P}_j)\), where by separates we mean that any path of \(\widehat{\mathcal{P}}^h\) that is within the sector must cross \(e'\). The paths between \(\widehat{P}_i\) and \(\widehat{P}_j\) in the clockwise ordering all lie in \(\text{CW}(\widehat{P}_i,\widehat{P}_j)\), and the paths between \(\widehat{P}_j\) and \(\widehat{P}_i\) in the clockwise ordering all lie in \(\text{ACW}(\widehat{P}_i,\widehat{P}_j)\). If a path P_<sub>r</sub>_ crosses \(e'\), then it means that it uses a copy of _e_, and hence its corresponding path _P<sub>r</sub>_ in _G_ also uses _e_. The result follows.

## 5.2 Main Congestion Argument

We are now ready to prove Theorem 1.3.

_Proof of Theorem 1.3._ First, we show how to prove Item 2 (unsplittable flow), since Item 1 ultimately follows from it. Let _f_ be a feasible strongly uncrossed flow with a fixed strongly uncrossed parallelization \(\phi\). Recall that we let \(f(e)=\sum_{P:e\in P}f(P)\) and let _f<sup>h</sup>_ be the single-commodity flow for \(h\in E(H)\).

Consider a commodity _h_. Let _P_<sub>1</sub>_,...,P<sub>k</sub>_ be paths of P_<sup>h</sup>_, ordered according to the cyclic clockwise ordering of their corresponding paths \(\widehat{P}_1,\dots,\widehat{P}_k\in\widehat{\mathcal{P}}^h\) in \(G_\phi\). Re-index so that _P_<sub>1</sub> and _P<sub>k</sub>_ are the outer paths. Let _i_<sup>∗</sup> be the smallest index _i_ such that \(\sum_{j\le i}f^h(P_j)\ge\frac{d(h)}{2}\) . We define _Q<sup>h</sup>=P_<sub>_i_<sup>∗</sup></sub>, and call it the _central path_ for _h_. Note that it is straightforward to find _Q<sup>h</sup>_ in polynomial time.

