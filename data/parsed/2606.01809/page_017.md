the preprocessing for _u_ that gives a cyclic ordering of DDG edges of _P_ outgoing from _u_. We let _h_ denote a hole of _P_ containing _u_.

Let _T_ be the shortest path tree from _u_ in _P_ found by FR-Dijkstra. This tree consists of DDG edges from child pieces of _P_. Given the precomputed cyclic orderings of these pieces, it is now fairly easy to find the ordering for _u_ in _P_. First, perform a DFS-traversal of _T_ where the next tree edge to be visited is the one that makes the sharpest right turn w.r.t. the parent tree edge; in case the parent tree edge does not exist in _T_, we regard it as a dummy edge from a vertex embedded inside _h_ to _u_. Given the precomputed information for child pieces, the DFS-traversal of _T_ can be done in _O_(|_T_|) time. The cyclic ordering of DDG edges of _P_ from _u_ is now the same as the DFS ordering of the heads of these edges.

This completes the description of the preprocessing step and we argued for its correctness. The running time is dominated by the time to compute DDGs of all pieces using FR-Dijkstra. Hence, the preprocessing step will not increase the overall time bound.

## B.2 Dealing with distinct holes

In this subsection, we give some details missing in the paper by Fakcharoenphol and Rao on how to deal with distinct holes. These details are important in our setting since we are not treating FR-Dijkstra as a black box.

Let _h_<sub>1</sub> and _h_<sub>2</sub> be two _distinct_ holes of a piece _P_ and consider a setting where FR-Dijkstra is run on some union of DDGs one of which is DDG(_P_). The issue with relaxing edges from _h_<sub>1</sub> to _h_<sub>2</sub> is that the Monge property no longer holds since _h_<sub>1</sub> and _h_<sub>2</sub> are distinct faces. We show how to extend FR-Dijkstra to handle this.

We can view the vertices of _h_<sub>2</sub> as an interval _R_ defined by starting in some arbitrary vertex and then following the cyclic ordering of _h_<sub>2</sub> until all vertices have been visited. Let _L_ be the vertices of _h_<sub>1</sub> with the cyclic ordering from _h_<sub>1</sub>. We wish to efficiently relax edges of the bipartite graph of DDG edges from _L_ to _R_.

Consider a step of FR-Dijkstra where a vertex \(u\in L\) is activated. We need to argue how to efficiently find the vertices of _R_ that get _u_ as their new parent. Clearly, these vertices induce a subpath of _h_<sub>2</sub> and hence at most two sub-intervals of _R_. Using the same procedure as in the standard FR-Dijkstra procedure, we traverse _L_ in order from _u_ until a vertex \(u'\) is found whose interval in _R_ is partially (but not fully) removed due to the activation of _u_.

FR-Dijkstra would now do binary search to determine which part of the interval of \(u'\) should belong to the interval of _u_. However, this fails since we are missing the following property: if two vertices _v_<sub>1</sub> and _v_<sub>2</sub> in _R_ have _u_ as their new parent then every vertex between them in _R_ also has _u_ as a parent.

Let _r_ be the endpoint of the rightmost DDG edge of _u_ in _P_. Split _R_ into two sub-intervals that share the endpoint _r_. Then we can in fact ensure the property above by doing binary search in each of the two sub-intervals. This follows using similar arguments to those in the proof of Lemma 5.6. Since _r_ can be obtained in constant time using the auxiliary data computed in the extension to FR-Dijkstra in Section B.1, we can thus deal with distinct holes without an asymptotic increase in the running time of FR-Dijkstra.

