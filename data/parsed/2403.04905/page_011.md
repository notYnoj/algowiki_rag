polynomial time,<sup>6</sup> then we can also compute our separator in polynomial time. Indeed, we can then compute \(\mathcal{G}^\times(\mathcal{D})\) and the arrangement of the disk boundaries in polynomial time, which allows us to do Step 1 (reducing the ply) in polynomial time. Since a separator for string graphs can be computed in polynomial time [18], this is easily seen to imply that the separator construction runs in polynomial time. Thus we obtain the following result.

\(\blacktriangleright\) **Corollary 2.6.** _Let d be a shortest-path metric on a connected subset_ \(F\subset\mathbb{R}^2\) _and let_ D _be a set of n geodesic disks with respect to the metric d, where d is such that the boundaries_ \(\partial D_i\) _of the disks in_ D _can be computed in polynomial time. Let_ \(q\ge 1\) _and_ \(\varepsilon>0\) _be fixed constants. Then q-Coloring can be solved in_ \(2^{O(n^{\frac{3}{4}+\varepsilon})}\) _time on_ \(\mathcal{G}^\times(\mathcal{D})\).

## 2.3 Obtaining a proper path system

So far we assumed that \(\Pi(\mathcal{D})\) is a proper path set. In general this may not be the case, since the paths in \(\Pi(\mathcal{D})\) may overlap along 1-dimensional subpaths and a pair of paths can meet multiple times. (The latter can happen since shortest paths need not be unique). Lemma 2.7 will allow us to still work with a proper path set in our proof. The proof of this lemma requires two technical assumptions on our shortest-path metric _d_. We thus now introduce the concept of a _well-behaved shortest-path metric_.

Well-behaved shortest-path metrics. We assume that for any finite set _P_={_p_<sub>1</sub>_,...,p<sub>n</sub>_} of points in _F_, there exists a set \(\Pi(P)=\{\pi_{ij}:1\le i<j\le n\}\) of shortest paths between the points in _P_ with the following properties:

1. For any two paths \(\pi_{ij},\pi_{k\ell}\in\Pi(P)\), the intersection \(\pi_{ij}\cap\pi_{k\ell}\) consists of finitely many connected components.

2. Let \(P^+\supset P\) be the set of endpoints of these components, and let \(\Gamma_{ij}\) be the set of subpaths into which \(\pi_{ij}\) is partitioned by the points in _P_<sup>+</sup>. Note that any two subpaths \(\gamma\in\Gamma_{ij}\) and \(\gamma'\in\Gamma_{k\ell}\) either have disjoint interiors or they are identical. Let \(\Gamma=\bigcup_{i,j}\Gamma_{ij}\) be the set of all distinct subpaths. Then there are values \(\delta_1,\delta_2>0\) such that the following holds.

For any \(v\in P^+\), the Euclidean ball \(B(v,\delta_1)\) of radius \(\delta_1\) centered at _v_ only intersects paths from \(\Pi(P)\) that contain _v_, and inside \(B(v,\delta_1)\) any two paths are either disjoint (except at _v_) or they coincide. Moreover, the balls \(B(v,\delta_1)\) for \(v\in P^+\) are pairwise disjoint.

Outside the balls \(B(v,\delta_1)\), the minimum distance between any two subpaths \(\gamma,\gamma'\in\Gamma\) is at least \(\delta_2\).

We call a metric satisfying these conditions _well-behaved_. The conditions are easily seen to be satisfied when _F_ is a closed and connected polygonal region and the paths \(\pi_{ij}\) are shortest (in the Euclidean sense) paths inside _F_. In fact, _F_ does not have to be polygonal; its boundary may consist of finitely many constant-degree algebraic curves. Another example is when the paths in \(\pi_{ij}\) are projections onto R<sup>2</sup> of shortest paths on a polyhedral terrain, or when the paths are shortest paths in a weighted polygonal subdivision. (In the latter case, the length of a section of the path inside a region is multiplied by the weight of the region [21]. In this setting, shortest paths are piece-wise linear and so they satisfy the conditions.)

<sup>6</sup> Typically the time to do this would not only depend on _n_, but also on the complexity of _F_ and the distance function _d_. For simplicity we state our results in terms of _n_ only. (This, of course, puts restrictions on the complexity of _F_ and _d_.)

