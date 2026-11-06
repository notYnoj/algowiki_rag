We can now proceed with the proof of the lemma. It might be known, but we have not been able to find a reference. Recall that _E_ is the edge set of \(\mathcal{G}^\times(\mathcal{D})\).

\(\blacktriangleright\) **Lemma 2.7.** _Let d be a well-behaved shortest-path metric on a closed and path-connected subset_ \(F\subset\mathbb{R}^2\)_, and let_ \(\Pi(\mathcal{D})=\{\pi_{ij}:(Di_i,D_j)\in E\}\) _be a set of shortest paths with the properties stated above. Then there is a proper path set_ \(\Pi'(\mathcal{D})=\{\pi'_{ij}:(Di_i,D_j)\in E\}\) _in_ R<sup>2</sup> _with the following property: for every pair_ \(\pi'_{ij},\pi'_{k\ell}\) _of crossing paths in_ \(\Pi'(\mathcal{D})\)_, the corresponding paths_ \(\pi_{ij},\pi_{k\ell}\) _in_ \(\Pi(\mathcal{D})\) _intersect._

**Proof.** We will prove the lemma in two steps. First, we modify the paths such that any two paths \(\pi_{ij}\) and \(\pi_{k\ell}\) meet in a single connected component, and then we perturb these paths slightly to obtain a set \(\Pi'(\mathcal{D})\) where any two paths cross in at most two points.

The first modification is done as follows. For each pair \(\pi_{ij},\pi_{k\ell}\in\Pi(\mathcal{D})\), and for each connected component \(I\subset\pi_{ij}\cap\pi_{k\ell}\), we add both endpoints of _I_ to the set _P_, thus (by the first property of well-behaved shortest-path metrics) obtaining a finite set _P_<sup>+</sup>. The set _P_<sup>+</sup>, together with the pieces of the paths \(\pi_{ij}\) connecting them, forms a plane graph G<sup>+</sup>=(_P_<sup>+</sup>_,E_<sup>+</sup>). We now slightly modify the edge lengths in G<sup>+</sup>, to ensure that there is a unique shortest path between any two points in _P_<sup>+</sup>, and we replace each original path \(\pi_{ij}\) by the shortest path between _pi<sub>i</sub>_ and _p<sub>j</sub>_ in G<sup>+</sup>; see Fig. 2(i) for an example. Since the shortest paths between

any two vertices in G<sup>+</sup> are unique, two paths \(\pi_{ij},\pi_{k\ell}\) do not intersect in more than one connected component. Moreover, the new paths are still shortest paths under the original metric. Formally, the perturbation of the edges lengths is done as follows. Let _e_<sub>1</sub>_,e_<sub>2</sub>_,...,e<sub>k</sub>_ be any ordering on the edges of G<sup>+</sup>. Then, perturb the edge lengths such that the new lengths are given by \(|e'_i|=|e_i|+2^i\varepsilon\), for an arbitrarily small \(\varepsilon>0\). Any path that was shortest initially, will remain shortest and no two paths have the same length.

Next we show how to slightly perturb the paths such that all crossings are proper. For that, we will make use of the second property of well-behaved shortest-path metrics to thicken the graph G<sup>+</sup>. Intuitively, we replace the edges of G<sup>+</sup> by thick curves and its vertices by small balls. Within each thick curve, we can slightly separate all paths that use the corresponding edge. Curves going to the same vertex meet at the disk around it. We then show that it’s possible to route paths within these balls, such that paths only possibly cross within the balls where they meet for the first time or for the last time. Formally this is done as follows.

Let \(\delta_1,\delta_2>0\) be the values specified in the second property of well-behaved metrics. We thicken G<sup>+</sup> by replacing each vertex \(v\in P^+\) by the ball \(B(v,\delta_1)\)--we call this ball a _thick vertex_--and by replacing each edge in G<sup>+</sup> by a _thick edge_ of width \(2\delta_2/3\). (Formally, we take the Minkowski sum of the original edge and a ball of radius \(\delta/3\), and remove the parts of the

(i)
(iii)
(ii)

**Figure 2** (i) The input paths (left) and the graph G<sup>+</sup> after re-routing the paths (right). (ii) The thickened graph. (iii) Drawing the paths inside a thick vertex.

