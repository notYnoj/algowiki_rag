1. _x∼_par _y_ 2. \(x\unknown\unknown y\) _for all connected nodes x,y in G with respect to the current state of the algorithm given by a graph G and potential assignment_ \(\phi\).

**Proof.** We prove the statement by induction over the insertion sequence. For an empty sequence the statement is trivially true. Now let _G_ be the graph before an insertion and \(G'\) be the graph after the insertion. We prove that, if the conditions hold for all connected nodes before the update, then the conditions also hold for all connected nodes after the update. Distinguish between edge and node insertions:

On EdgeInsertion(_e_), we compose Lemma 8 (using bipartiteness, using \(\phi(v)\ge 0\) which is always maintained, using induction hypothesis that _x∼_par _y_ and \(x\unknown\unknown y\) for all connected _x,y_) with Lemma 11 (using bipartiteness) and with Lemma 12 and Lemma 13 (using bipartiteness).

The composition gives that all connected pairs of assigned nodes satisfy _x∼_par _y_ and \(x\unknown\unknown y\) in the new assignment.

It remains to show that all nodes are assigned at the end of the step. Only nodes that are connected to the edge endpoints are cleared. This means that TwoColoring assigns a potential to all remaining unassigned nodes, as all nodes that are unassigned in intermediate steps are reachable from the edge endpoint _v_.

On NodeInsertion(_v_), the relations _x∼_par _y_ and \(x\unknown\unknown y\) are preserved for all nodes \(x,y\neq v\), since their distances and potentials don’t change. Since _v_ is not connected to any other node, this is sufficient.

\(\blacktriangleright\) **Corollary 15.** _The coloring c(v_) _produced by the algorithm on an input sequence as in Theorem 14 is a proper 3-coloring._

**Proof.** By construction, \(c(v)=mod(\phi(v),3)\) at the end of every update step. By Theorem 14 we get that all connected nodes are parity-consistent and potential-separated. Theorem 5 lets us conclude that the coloring _c_ is a proper 3-coloring of _G_. \(\blacktriangleleft\)

## 4.4 Analysis of edit radius

The following is derived from the locality analysis of the 3-coloring algorithm in [2]. The idea is that choosing the component with lower peak potential when a conflict occurs guarantees the balanced growth of components.

\(\blacktriangleright\) **Lemma 16.** _In any state of the algorithm reached by edge and node insertions, for any connected component C, the peak potential_ \(\phi_{max}(C)=max_{v\in C}\phi(v)\)_, is bounded by_ \(\phi_{max}(C)\le 1+3\cdot log_2|C|\)_. This bound holds at all intermediate potential assignments that occur in the algorithm._

**Proof.** Proof by induction on sequence of states.

Base case: any state with \(\phi_{max}(C)\le 1\) for a given connected component _C_, including the initial state and isolated nodes. Then, the condition \(\phi_{max}(C)\le 1+3\cdot log_2|C|\) is trivially satisfied for all components.

Induction step \((G,\phi)\rightarrow(G',\phi')\). Let _C_ be any connected component of \(G'\) with \(\phi'_{max}(C)>1\). Distinguish between the following cases:

