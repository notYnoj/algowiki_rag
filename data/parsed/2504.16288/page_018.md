<tbc>to go over successive buckets. (Note that the sequence of priorities of the vertices that we extract out of the priority queue in Dijkstra’s algorithm is nondecreasing, so we only need to go once over the sequence of buckets throughout the algorithm.) One may remark that the path of minimum weight that we obtain is always a simple path.

## Unbounded weight st-path.

To check whether there exist _st_-paths of unbounded weight, we compute the condensation of _G_ (see Section 4.2) in time _O_(|_G_|). Obviously, there is a strongly connected component (SCC) that contains an edge with nonzero weight if and only if there are _st_-paths of unbounded weight. Indeed, if there is an SCC that contains an edge with nonzero weight, then we can repeat a cycle of the SCC containing this edge as many times as we want, and combining it with a path from _s_ to the SCC and from the SCC to _t_ (these paths must exist by our preprocessing of _G_ at the beginning of the proof). On the other hand, if no such SCC with an edge of nonzero weight exists, then every possible _st_-path in _G_ has only cycles with weight-0 edges, which means that there are only a finite number of possible weights for _st_-paths.

## Maximum weight st-path.

Finally, let us assume that there are no _st_-paths with unbounded weight and let us show how to compute a largest weight _st_-path. For this purpose, we will compute a path of maximum weight that leads to _t_ from every node. However, the paths can be of linear size, so we store them in a compressed way, by remembering for every node _v_ only the first edge on a maximum weight _vt_-path. Then the path can be retrieved edge-by-edge, starting from _s_, until we reach node _t_. In addition to the first edge, we also store the total weight _X_\[_v_\] of the _vt_-path of maximum weight.

We process all SCCs of the condensation of _G_ in reverse topological ordering. Observe that within every SCC all edges have weight 0, thanks to our assumption that there are no _st_-paths with unbounded weight. First we process C_<sub>t</sub>_=SCC\[_t_\], the SCC containing _t_. Clearly, for all nodes from this component, every path to _t_ has weight 0, so we can use any such path. Now we show how to make a consistent choice of first edge towards _t_ from every node. For this, let _E<sup>rev</sup>_ be the set of all edges of C_<sub>t</sub>_, but with reversed direction, that is \(\{(q',q)|(q,q')\in E(G)\}\). We run a depth-first search from _t_ only on the nodes from C_<sub>t</sub>_, but along the reversed edges _E<sup>rev</sup>_. For every considered node \(v\neq t\), we store the edge to its parent in the recursion tree as the first edge on a _vt_-path with maximum weight. Observe that all the nodes of C_<sub>t</sub>_ will be visited, as C_<sub>t</sub>_ is a strongly connected component and so is its counterpart with edges reversed. Moreover, the chosen edges correctly define paths to _t_, as they correspond to going up the recursion tree towards the root _t_.

For every other SCC C of _G_ in reverse topological ordering, we calculate the value:

\(x:=max_{u\in\mathcal{C}}max_{(u,v)\in E(G)v\notin\mathcal{C}}\{weight((u,v))+X[v]\}\)

and we set _X_\[_u_\]:=_x_ for all \(u\in\mathcal{C}\). Note that all such edges to outside of C point to SCCs that have been already visited and hence the values _X_\[_v_\] have already been calculated for all \(v\notin\mathcal{C}\) such that there is an edge from a node from C to _v_. Let _z_ and _e_=(_z,v_) be a node and edge for which the above maximum is attained and set _e_ as the first edge on a _zt_-path with largest weight. For all nodes \(u\in\mathcal{C}\backslash\{z\}\) we find the first edge on the _ut_-path with maximum weight similarly as in C_<sub>t</sub>_, but now we start the DFS from _z_. Again, all edges within C have weight 0, so it suffices to find any path to _z_.

Finally, after processing all the SCCs, _X_\[_s_\] stores the total weight of the _st_-path of maximum weight and we can retrieve such path in linear time. This concludes the proof of the last case and hence the lemma holds.

One graph which will often be relevant is the _product graph_ of an automaton and a string:

**Definition 5.3.** _The_ product graph _G<sub>A,w</sub> of an_ \(\varepsilon NFA\) _A on states Q and a string_ \(w\in\Sigma^*\) _is the labelled and weighted graph with vertex set_ \(\{0,\dots,|w|\}\times Q\) _constructed as follows:_

• _For each transition_ \((q,\varepsilon,q')\) _in A and for each_ \(i\in\{0,\dots,|w|\}\)_, there is an edge from_ (_i,q_) _to_ \((i,q')\) _in G<sub>A,w</sub> with label_ \(\varepsilon\) _and weight_ 0.<tbc>

