• The case where exactly one vertex is in _S<sub>b,h</sub>_ is similar. W.l.o.g assume \(v_j(h)\in S_{b,h}\). We continue the search with new \(v_i(h)=v_{i-\lfloor\frac{i-j}{2}\rfloor}(h)\) and new \(v_j(h)=v_{j-\lfloor\frac{s_h-(k-j)}{2}\rfloor}(h)\).

Thus it follows that we can do binary search in \(\tilde{O}(1)\) time using the above procedures.

## Detecting _e<sup>t</sup>_ in a Region.

It remains to prove the following Lemma.

**Lemma 5.8.** _Given any two vertices v<sub>i</sub>(h),v<sub>j</sub>(h_) _on h, such that_ \(v_i(h),v_j(h)\unknown\in S_{b,h}\)_, there is an algorithm that in_ \(\tilde{O}(1)\) _time detects whether the edge e<sup>t</sup> is contained in the region of the plane to the right of the directed cycle consisting of the shortest path_ \(\pi_{b,v_i(h)}\) _from b to v<sub>i</sub>(h), the path in h from v<sub>i</sub>(h_) _to v<sub>j</sub>(h_) _on h, and the reverse of the shortest path_ \(\pi_{b,v_j(h)}\) _from b to v<sub>j</sub>(h_) _(see Figure 1(b))._

## Overview.

To prove the Lemma, we employ the following algorithm: first let us assume that the first edge on the shortest paths \(\pi_{b,v_i(h)},\pi_{b,v_j(h)}\) and the shortest path \(\pi_{b,v^t}\) from _b_ to _v<sup>t</sup>_ are all distinct. Here, we can use the planar embedding of _G_ to conclude whether \(\pi_{b,v^t}\) uses as a first edge an edge to the right of \(\pi_{b,v_i(h)}\) and to the left of \(\pi_{b,v_j(h)}\) (or not) and if so we know that _e<sup>t</sup>_ is in the region; otherwise _e<sup>t</sup>_ must be outside the region.

Unfortunately, the paths \(\pi_{b,v_i(h)}\) and \(\pi_{b,v^t}\) might share the first few (or many) edges and \(\pi_{b,v^t}\) only takes a right-turn after a while (the case where \(\pi_{b,v_j(h)}\) and \(\pi_{b,v^t}\) share many edges is analogous). We thus have to find the last vertex _x_ that is on both \(\pi_{b,v_i(h)}\) and \(\pi_{b,v^t}\). Deciding whether \(\pi_{b,v^t}\) makes a left-turn after following \(\pi_{b,v_j(h)}\) is then again simple using the embedding. Observe that the edge _e<sup>t</sup>_ is not on \(\pi_{b,v_i(h)}\) and \(\pi_{b,v_j(h)}\) so that we can concentrate on finding the last common vertex on the shortest paths of \(\pi_{b,u^t}\) and \(\pi_{b,v_i(h)}\) and \(\pi_{b,v_j(h)}\), respectively.

## Storing Additional Information.

To find the vertex _x_, we need to store additional information. We use the following results.

**Theorem 5.9** (Level-Ancestor Data Structure, see \[6\])**.** _Given a tree T rooted at vertex r, there is a data structure that with preprocessing time O_(|_T_|) _and query time O_(1) _that on query for a vertex x and a positive integer d returns the d<sup>th</sup> edge on the r-to-x path in T._

We assume that on initialization of our data structure, additionally to the DDG edges, we also store for each piece \(P'\), and vertex \(b'\in\partial P'\) the shortest path out-tree \(T_{b^\prime}\) over the lower level DDGs of \(P'\), as can be computed by using Appendix B. Additionally, we know that \(T_{b^\prime}\) spans all boundary nodes of \(P'\)’s child pieces, denoted \(\partial_\text{\textit{child}}P'\). We mark these vertices in the tree and let \(T'_{b^\prime}\) be the tree derived from restricting the vertex set to \(\partial_\text{\textit{child}}P'\) (by recursively removing leaves that are not in \(\partial_\text{\textit{child}}P'\) and by contracting paths between two vertices in \(\partial_\text{\textit{child}}P'\)).

Then for each such tree, we initialize a level-ancestor data structure on \(T'_{b^\prime}\) as described in Theorem 5.9. We do the same for the in-tree \(\overleftarrow{T}_{b^\prime}\). It is not hard to observe that these computations can be done in time \(O(|T_{b^\prime}|+|\overleftarrow{T}_{b^\prime}|)=\tilde{O}(\sqrt{|P|})\) time, thus the pre-processing can still be bound by \(\tilde{O}(r)\).

After each update \((e^t,\omega^t)\), we do the same to the trees _T<sub>v<sup>t</sup></sub>_ rooted at _v<sup>t</sup>_ and the tree \(\overleftarrow{T}_{u^t}\) rooted at _u<sup>t</sup>_ computed on dense distance graphs with edge reversed. Again, this incurs at most \(\tilde{O}(\sqrt{r})\) update time over all levels for each update.

## Implementing the Query Efficiently.

Now, returning to the paths \(\pi_{b,v_i(h)}\) and \(\pi_{b,u^t}\), we distinguish two cases:

