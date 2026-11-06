**Proof.** The statement follows from induction over the iterations. We prove that after an iteration with a given _k_ all outer nodes _v_ have \(\phi(v)\le k-1\), and all connected assigned pairs _x,y_ have _x∼_<sub>par</sub>_y_ and \(x\dashleftrightarrow y\). The desired result follows after the last step where _k_=1, so all outer nodes _v_ have \(\phi(v)=0\).

Initially all connected pairs _x,y_ of assigned nodes satisfy \(x\dashleftrightarrow y\) and _x∼_<sub>par</sub>_y_ by assumption and \(\phi(v)\le\phi_\mathrm{max}\).

Every iteration assigns a potential to all neighbors of outer nodes _v_ with \(\phi(v)=k\), so no such outer nodes remain at the end of the step. Remaining and newly created outer nodes have \(\phi(v)\le k-1\) as required. Using Lemma 9 with \(\phi(v)\le k\) by induction hypothesis, we get that \(x\dashleftrightarrow y\) holds for all connected assigned pairs after the iteration. Using Lemma 10 with the bipartiteness of _G_ and with the induction hypothesis, we get that _x∼_<sub>par</sub>_y_ holds for all connected assigned pairs, concluding the induction step. \(\blacktriangleleft\)

The last step of the algorithm is to complete the coloring by alternating between potential 0 and 1. The next lemmas prove that this maintains the invariants on connected assigned nodes.

\(\blacktriangleright\) **Lemma 12.** _If all connected pairs x,y of assigned nodes satisfy_ \(x\dashleftrightarrow y\) _and for all outer nodes v we have_ \(\phi(v)\le 1\)_, then also in the assignment of potentials resulting from TwoColoring all connected pairs of assigned nodes satisfy_ \(x\dashleftrightarrow y\).

**Proof.** TwoColoring only assigns \(\phi(x)\in\{0,1\}\) and all outer nodes have \(\phi(x)\in\{0,1\}\) by assumption. Thus, if \(x\neq y\), we have \(d_G(x,y)\ge 1\ge|\phi(x)-\phi(y)|\), proving \(x\dashleftrightarrow y\) in the resulting assignment for any pair of changed nodes and outer nodes _x,y_.

For the remaining nodes, the result follows by transitivity (Lemma 7), since any shortest path to a changed node must pass through an outer node. \(\blacktriangleleft\)

\(\blacktriangleright\) **Lemma 13.** _Let G be bipartite. If all connected pairs x,y of assigned nodes satisfy x∼_<sub>par</sub>_y, then also in the assignment of potentials resulting from TwoColoring all connected pairs of assigned nodes satisfy x∼_<sub>par</sub>_y._

**Proof.** First, we prove that the node _v_ that is chosen as reference node in TwoColoring satisfies _v∼_<sub>par</sub>_y_ for all previously assigned nodes _y_. If _v_ is a node with \(\phi(v)\neq\perp\) reachable from _v<sub>r</sub>_, then this holds by assumption. Otherwise _v=v<sub>r</sub>_, then there are no other assigned nodes connected to _v<sub>r</sub>_ and _v∼_<sub>par</sub>_v_ holds by reflexivity.

All remaining nodes _w_ are assigned \(\phi(w)=\mathrm{mod}(\phi(v)+d_G(v,w),2)\). We can easily verify the parity-consistency _w∼_<sub>par</sub>_v_:

\(\phi(w)-\phi(v)\equiv(\phi(v)+d_G(v,w))-\phi(v)(\mathrm{mod}2)\equiv d_G(v,w)(\mathrm{mod}2).\)

Parity-consistency of _w_ with other nodes follows by transitivity through _v_ (Lemma 6 using bipartiteness of _G_). All remaining pairs are unchanged, so parity-consistency comes by assumption. \(\blacktriangleleft\)

We have now proven the correctness of the main subprocedures required for the update on an edge insertion. The following theorem combines the previous results to assert correctness of the dynamic algorithm.

\(\blacktriangleright\) **Theorem 14.** _For any sequence of node and edge insertions starting from an empty graph such that the graph remains bipartite in every step, where after every insertion of an edge e we call EdgeInsertion(e_) _and after every insertion of a node v we call NodeInsertion(v), we have_

