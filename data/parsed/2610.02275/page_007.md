<tbc>The merges _L⋆L_, _C⋆L_, and _L⋆C_ are invalid. They would create a path with three edges: a label _L_ already places the active vertex at a leaf of a star with at least two edges, and the other nonpending child adds a second neighbour to that leaf.

For pair states on the same two vertices _x,y_, the valid merges are

\(\begin{array}{ c c c }
E\star E=E, & E\star S_x=S_x, & S_x\star E=S_x, \\
E\star S_y=S_y, & S_y\star E=S_y, & S_x\star S_x=S_x, \\
 &  & S_y\star S_y=S_y.
\end{array}\)

The merges _S<sub>x</sub>⋆S<sub>y</sub>_ and _S<sub>y</sub>⋆S<sub>x</sub>_ are invalid because they would place attachments at both endpoints of _xy_.

The join recurrence is

\(\mathrm{DP}[t,\tau]=\mathrm{max}_{\sigma_1\star\sigma_2=\tau}\big\{\mathrm{DP}[t_1,\sigma_1]+\mathrm{DP}[t_2,\sigma_2]\big\},\)

where undefined merges are ignored. No edge is counted at a join node. An edge entirely inside the bag remains uncounted in both children, while every selected edge with an endpoint outside the bag belongs to exactly one child subtree and has already been counted there.

## 4.3 Correctness

The root bag is empty, so the only accepting state at the root _r_ is \(\varnothing\). The value returned by the algorithm is \(\mathrm{DP}[r,\varnothing]\).

**Lemma 6.** _Every finite DP entry satisfies the invariant. Consequently, every accepting computation at the root represents an edge open packing whose cardinality is its DP value._

_Proof._ We argue by induction over the nice tree decomposition. The statement is immediate at a leaf.

At an introduce node, an inactive introduced vertex does not change the partial solution. An active introduced vertex can interact only with active vertices already in the current bag, because it has no neighbour in \(V(G_{t^\prime})\backslash B_{t^\prime}\). The transition from the empty state creates a pending vertex; the transition from (_x,P_) selects _xv_ and creates a _K_<sub>2</sub>-component; and the transition from (_x,C_) attaches _v_ as a new leaf of the star centred at _x_. The excluded cases are precisely those that would give a leaf a second selected neighbour or place three active vertices in one clique. Thus, every introduce transition preserves the invariant.

At a forget node, a pending singleton is rejected. If a singleton centre or leaf is forgotten, its component is complete; the separation property implies that the forgotten vertex has no neighbour outside _V(G<sub>t</sub>_). If _v_ belongs to a pair state with _x_, the edge _vx_ is counted once and the remaining role of _x_ is recorded correctly. Thus, all forget transitions preserve the invariant and count each selected edge exactly once.

At a join node, put _X<sub>i</sub>=V(G<sub>t<sub>i</sub></sub>_)\\_B<sub>t</sub>_ for \(i\in\{1,2\}\). There is no edge between _X_<sub>1</sub> and _X_<sub>2</sub>, so no hidden common edge can be created between selected vertices lying strictly in different child subtrees. All interactions occur through the common bag. Requiring equal active subsets and using the listed merge table preserves exactly the compatible partial-star shapes. In particular, all attachments of a boundary edge lie at the same endpoint. No selected edge is counted twice.

At the root, there is no pending vertex and no uncounted boundary edge. The selected vertices therefore induce a disjoint union of induced stars. By Observation 1, the selected edges form an edge open packing, and every selected edge has been counted exactly once.

**Lemma 7.** _Every edge open packing of G is represented by the dynamic program._

_Proof._ Let _D_ be an edge open packing, and set \(U_t=V(D)\cap V(G_t)\) at each node _t_. Every vertex in _V(G<sub>t</sub>_)\\_B<sub>t</sub>_ has no neighbour outside _V(G<sub>t</sub>_), by the separation property of a tree decomposition. Thus, each vertex of _U<sub>t</sub>_\\_B<sub>t</sub>_ has a selected neighbour in _U<sub>t</sub>_. It follows that _G<sub>t</sub>_\[_U<sub>t</sub>_\] is a star forest whose only possible isolated vertex lies in the bag. Observation 5 ensures that at most two vertices are active, and two active vertices form a selected edge.

Assign each boundary component its canonical label. In particular, a boundary edge _xy_ receives label _E_ exactly when it has no attachment in the processed part; otherwise all attachments have the same centre, giving _S<sub>x</sub>_ or _S<sub>y</sub>_. If a singleton boundary vertex _x_ lies in a partial _K_<sub>2</sub> with its other endpoint _v_ outside the bag, label _C_ is sufficient. Indeed, all selected neighbours of _v_ already lie in _V(G<sub>t</sub>_). If _v_ were the centre of a larger global star, that star would therefore already be present in the processed part. Consequently, this _K_<sub>2</sub> either remains a _K_<sub>2</sub> globally or can grow only at _x_. More generally, the unique centre of a global star with at least two edges cannot be forgotten while one of its leaves remains outside<tbc>

