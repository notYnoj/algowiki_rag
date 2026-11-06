IDs of these nodes on a BFS tree (or low-congestion shortcuts) of _G_ in deterministic \(\tilde{O}(D)\) rounds by [17] (resp. by Lemma 7).

**Lemma 14.** _There is an_ \(\tilde{O}(D)\) _deterministic round algorithm that finds a_ \((\frac{1}{4},\frac{3}{4})\)_-balanced dual node if exists in T_<sup>∗</sup>_, and a_ \((\frac{1}{4},\frac{3}{4})\)_-critical dual node otherwise. Upon termination, all vertices of G learn the ID of the balanced or critical node._

_Proof._ Given the cotree _T_<sup>∗</sup> (computed in Step 1), either a \((\frac{1}{4},\frac{3}{4})\)-balanced node or a \((\frac{1}{4},\frac{3}{4})\)-critical node exists in _T_<sup>∗</sup> (by Lemma 4). We find one of them as follows.

1. We want to compute the weight of \(w(T_f^*)\) for all nodes \(f\in T^*\). To do that, we want to use Lemma 11, but first we must provide its input format: (a) From Lemma 13, each \(v\in G\) knows the weight of each face _f_ that contains _v_. In addition, (b) by Lemma 9 and Lemma 12, each vertex _v_ knows for each incident edge _e_ whether it is in _T_<sup>∗</sup>, and _v_ knows the two IDs of faces that _e_ participates in. Finally, (c) we pick a root for _T_<sup>∗</sup> by aggregating the IDs of faces in _G_, picking the maximum ID face (node of _T_<sup>∗</sup>) as the root. This is implemented in \(\tilde{O}(D)\) deterministic rounds (Lemma 7).<tbc>

<tbc>Henceforth, we match the input format of Lemma 11, so we use it to root _T_<sup>∗</sup> and to compute the subtree sums of _T_<sup>∗</sup> in deterministic \(\tilde{O}(D)\) rounds. Upon termination, all vertices of \(v\in G\) on a face _f_, know the weight of _f_’s subtree \(w(T_f^*)\).<tbc>

2. To detect a balanced node or a critical node, vertices of _G_ on the (face corresponding to the) root node _g_ of _T_<sup>∗</sup>, broadcast the weight of _g_’s subtree (i.e., _w(T_<sup>∗</sup>)) to the entire graph _G_, then all vertices of _G_ learn _w(T_<sup>∗</sup>). This is implemented in \(\tilde{O}(D)\) rounds, either via the low-congestion shortcuts (Lemma 6) in case we are working in a subgraph _G<sub>i</sub>_ of _G_, or via a BFS tree if we work in _G_ [17].<tbc>

3. Next, because each vertex \(v\in G\) knows _w(T_<sup>∗</sup>) and the subtree weight \(w(T_f^*)\) of faces _f_ that _v_ participates in, _v_ locally detects if _f_ is a \((\frac{1}{4},\frac{3}{4})\)-balanced node. All vertices aggregate on _G_, in \(\tilde{O}(D)\) deterministic rounds (Lemma 7), the ID of balanced-nodes _f_ that they detected, choosing the maximum ID face _f_ to be the desired balanced node.<tbc>

4. If no balanced node was identified in the previous step, there must be a \((\frac{1}{4},\frac{3}{4})\)-critical node. Again, in the same manner as in the previous step, the ID of a critical node _f_ is known to vertices that participate in it and is learned by all vertices of _G_.

**Marking the separator (Step 4).** In this step, we mark the _u_-to-_v_ path separator _P_ of _T_ and inform the vertices _u_, _v_ that they are the endpoints of the (possibly artificial) edge _e_ that closes a cycle with _P_. We first detect the vertices _u_, _v_. Then, we mark the path _P_ by a simple subtree sum computation on _T_: _u_, _v_ have an input of 1, and other vertices 0. Thus, the edges that have one endpoint that has a sum of 1 and one endpoint that has a sum of at least one <sup>5</sup>, are the edges of _P_. This terminates in \(\tilde{O}(D)\) rounds (Lemmas 7 and 8).

The detection of _u_, _v_ is done by using a procedure of [9] (Appendices B.2 and B.3 of their paper) with different constants. In a high level, they investigate two cases (similar to what we do in Theorem 2). Namely, the case where a balanced node exists, and the case where a critical node exists, and for each they show how to deduce the vertices _u_, _v_. Note, in Lemma 5 we proved that given a balanced or a critical node, such a separator exists using our way of assigning weights. The procedure uses simple primitives: subtree sums and previously computed weights (so, it can easily be made deterministic). More details on the procedure are provided in Appendix A.1.

<sup>5</sup>I.e, all internal nodes of _P_, and only those nodes, have a sum that is exactly one; except for the lowest common ancestor of _u_, _v_ in _T_ that has a sum of two.

