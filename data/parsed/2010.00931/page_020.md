Consider now a rotation of the edge {_q,p_} that transforms _T_ into \(T'\). We know that \(\delta(T'_q)=\delta(T_p)\), and we can compute \(\delta(T'_p)\) as described above. For all other \(x\in V(T)\backslash\{p,q\}\), we have \(\delta(T'_x)=\delta(T_x)\). It follows that the boundary-size data structure can be updated with _O(k_) oracle calls.

### The algorithm.

We proceed via a modified depth-first search, starting with a pointer at the root. Mark nodes as `unvisited`, `visited`, or `finished`, with all nodes initially `unvisited`.

Let _T_ denote the current tree, and let _y_ be the node at the pointer. If _y_ is `unvisited`, we mark it `visited`. If all children of _y_ are `finished`, we mark _y_ as `finished` and move the pointer to the parent of _y_, unless _y_ is the root, in which case we are done.

Otherwise, if _y_ has an `unvisited` child, we pick one such child _x_. If \(|\delta(T_x)|\le k-1\), then we move the pointer to _x_. Otherwise, we rotate the edge {_y,x_}, mark _x_ as `visited`, and keep the pointer at _y_.

By Lemma 10, the algorithm uses at most _n-k_ rotations. Boundary-size queries are handled by the previously described data structure. It remains to show that the algorithm terminates with _O(n_) pointer moves and produces a (_k_-1)-cut tree. Towards this claim, observe the following invariants, easily shown by induction:

(i) if a node is `finished`, resp. `unvisited` then all its descendants in _T_ are `finished`, resp. `unvisited`,<tbc>

(ii) if the node at the pointer is `visited` then all its children are either `finished` or `unvisited`,<tbc>

(iii) every node _x_ marked `visited` or `finished` satisfies \(|\delta(T_x)|\le k-1\).

Invariants (i)-(ii) imply that the algorithm does not get stuck, and since every pointer move changes a marking from `unvisited` to `visited` or from `visited` to `finished`, after 2_n_ steps all nodes are `finished`, with the pointer at the root.

Invariant (iii) implies that all rotations performed are of the kind defined in Lemma 9, and that the algorithm produces a (_k_-1)-cut tree.

## 4.2. Steiner-closed trees

We now prove the equivalence between 2-cut STTs and _Steiner-closed STTs_, defined in §2.

**Lemma 12.** _A search tree T on S is Steiner-closed if and only if it is a_ 2_-cut STT._

_Proof._ Suppose that there is a node \(x\in V(T)\) such that \(|\delta(T_x)|\ge 3\). Since _S_\[_V(T<sub>x</sub>_)\] is connected, every pair of nodes from \(\delta(T_x)\) is connected through a path that lies entirely in _V(T<sub>x</sub>_), except for its endpoints. Thus \(V(\mathtt{ch}(\delta(T_x)))\backslash\delta(T_x)\subseteq V(T_x)\). Moreover, \(\mathtt{ch}(\delta(T_x))\) is a tree with leaves \(\delta(T_x)\) (by Observation 6). As there are more than two leaves, there must be an inner node \(v\in V(T_x)\) with degree at least 3 in \(\mathtt{ch}(\delta(T_x))\). Let _P_ be the search path of the parent of _x_ in _T_. Then \(v\notin P\), but _v_ has degree at least 3 in `ch`(_P_), so _P_ is not Steiner-closed.

Suppose _T_ is not Steiner-closed. Then there is a path with node set _P_ from the root to some node _x_ such that _P_ is not Steiner-closed. Let \(y\in\mathtt{ch}(P)\backslash P\) be a node with degree at<tbc>

