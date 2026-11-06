_C_ was connected in _G_. Then it was also a complete connected component in _G_, since components cannot shrink in a sequence of edge and node insertions. The only way that any node \(x\in C\) with \(\phi'(x)=\phi'_\mathrm{max}(C)\) has \(\phi'(x)>\phi(x)\) and \(\phi'(x)>1\) at any intermediate state is by incrementing during FixAndClear. This can only happen if _C_ was not connected in the previous step, since connected nodes are always parity-consistent by Theorem 14. However, we assumed _C_ to be connected in _G_, so \(\phi'_\mathrm{max}(C)\le\phi_\mathrm{max}(C)\). By induction hypothesis, \(\phi_\mathrm{max}(C)\le 1+3\cdot log_2|C|\).

_C_ was disconnected in _G_. The last step must have been an edge insertion. Let _C<sub>v</sub>_ and _C<sub>w</sub>_ be the connected components in _G_ such that \(C_v\cup C_w=C\). If \(\phi'_\mathrm{max}(C)\le\phi_\mathrm{max}(C)=\mathrm{max}(\phi_\mathrm{max}(C_v),\phi_\mathrm{max}(C_w))\), then by induction hypothesis \(\phi'_\mathrm{max}(C)\le 1+3\cdot log_2\mathrm{max}(|C_v|,|C_w|)\le 1+3\cdot log_2|C|\) as required. Otherwise, _C_ has higher peak potential than _C<sub>v</sub>_ and _C<sub>w</sub>_, which can only happen by increment of the potential in case of a conflict in FixAndClear. Without loss of generality, let \(|C_v|\le|C_w|\). Then

\(\phi'_\mathrm{max}(C)\le\mathrm{min}(\phi_\mathrm{max}(C_v),\phi_\mathrm{max}(C_w))+3\)<br> \(\le 1+3log_2\mathrm{min}(|C_v|,|C_w|)+3\)<br> \(\le 1+3(log_2|C_v|+1)\)<br> \(\le 1+3(log_2(2|C_v|))\)<br> \(\le 1+3(log_2|C|).\)

\(\blacktriangleleft\)

\(\blacktriangleright\) **Lemma 17.** _Whenever the color c(v_) _of a node v is changed by the algorithm, this node has distance bounded by_ \(D\le\frac{3}{2}log_2n+1\) _to the inserted node or to the inserted edge, including both endpoints._

**Proof.** For a node insertion, this is immediately true, since only the coloring of the inserted node is changed. Let us consider an edge insertion. The new coloring is obtained as \(c(v)=\mathrm{mod}(\phi(v),3)\) from the potential assignment \(\phi\) at the end of the update. All nodes that are being cleared and reassigned have distance less than _D_ to both endpoints of the inserted edge. The only time a potential value is changed at a node that has distance at least _D_ to the insertion is in the parity fixing step of FixAndClear. However, this does not change the coloring, since \(\phi(v)+3\equiv\phi(v)(mod3)\). Thus, all nodes that change their coloring have distance less than _D_ to the endpoints of the inserted edge. This distance _D_ is computed as \(D=\frac{1}{2}(\mathrm{max}_{v\in V}\phi'(v)+1)\), where \(\phi'\) refers to the intermediate potential assignment before clearing the edit-area. Using the bound on \(\phi'_\mathrm{max}\) from Lemma 16, we have \(D\le\frac{3}{2}log_2n+1\) as required. \(\blacktriangleleft\)

**Theorem 1.** _There exists a dynamic graph algorithm which maintains a 3-coloring with a locality of O_(log_n_) _in the dynamic-LOCAL model for input sequences of node and edge insertions where the resulting graph is bipartite at every step._

**Proof.** Follows directly from Corollary 15 (correctness of the coloring) and Lemma 17 (bound on the edit radius) with Algorithm 1, and the definition of dynamic-LOCAL. \(\blacktriangleleft\)

**Corollary 2.** _In the dynamic-LOCAL model, the locality of computing a proper_ 3_-coloring of a bipartite graph is_ \(\Theta(logn)\).

