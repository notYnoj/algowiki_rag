**Proof.** We prove the statement by induction over the sequence of changed individual nodes. The induction hypothesis is that all pairs of nodes that have already been assigned are potential-separated and outer nodes have \(\phi(v)\le k\). As a base case, this is satisfied by assumption if no nodes have been changed.

Next, we prove the induction step of one node being changed. We call \(\phi\) the assignment before, and \(\phi'\) the assignment after the node’s potential has been assigned. Let \(\unknown\unknown\unknown\) and \(\unknown\unknown\unknown'\) mean potential-separation with respect to \(\phi\) and \(\phi'\) respectively. Let _S_ be the set of outer nodes in the original assignment \(\phi\).

We only need to consider the node that changes its assignment (for all unchanged pairs, \(x\unknown\unknown y\) implies \(x\unknown\unknown'y\) directly). By definition of BuildAround(_k_), such a node _x_ is assigned \(\phi'(x)=k-1\). This means that the required condition for outer nodes, \(\phi'(v)\le k\), is maintained even if _x_ becomes an outer node. Note also that by construction _x_ must be adjacent to a node \(y\in S\) which has \(\phi(y)=\phi'(y)=k\).

It suffices to prove that for all nodes \(z\in S\) connected to _x_, we have \(x\unknown\unknown'z\). For any other node _v_ connected to _x_, any shortest path from _x_ to _v_ must pass through an outer node \(z\in S\). This is because _x_ is unassigned in \(\phi\) and _v_ is assigned, so any path between them must transition from unassigned to an assigned outer node. By transitivity of potential-separation as proven by Lemma 7, if \(x\unknown\unknown'z\) it follows that \(x\unknown\unknown'v\) using the induction hypothesis that \(z\unknown\unknown'v\).

To conclude, we prove \(x\unknown\unknown'z\), by distinguishing two cases. They are exhaustive because \(z\in S\), which implies \(\phi(z)\le k\) by assumption.

**Case** \(\phi(z)=k\)**.** Then, \(|\phi'(x)-\phi'(z)|=1\), and \(d_G(x,z)\ge 1\) because \(x\neq z\), so \(x\unknown\unknown'z\).

**Case** \(\phi(z)\le k-1\)**.** We use that _y_ is adjacent to _x_ and has \(\phi'(y)=k\). Note that \(d_G(x,z)\ge d_G(y,z)-1\) because _x_ and _y_ are adjacent. Then,

\(d_G(x,z)\ge d_G(y,z)-1\)<br> \(\ge|\phi'(y)-\phi'(z)|-1\)<br> \(=(k-\phi'(z))-1=k-1-\phi'(z)=|\phi'(x)-\phi'(z)|,\)<br> \(\text{so}x\unknown\unknown'z.\) \(\blacktriangleleft\)

\(\blacktriangleright\) **Lemma 10.** _Let G be bipartite. If all connected pairs x,y of assigned nodes satisfy x∼_<sub>par</sub> _y, then also in the assignment of potentials resulting from BuildAround(k_) _all connected pairs of assigned nodes satisfy x∼_<sub>par</sub> _y._

**Proof.** Every node _x_ that is changed in BuildAround(_k_) has a neighbor _y_ such that \(\phi(x)=\phi(y)-1\) in the resulting assignment by construction. Thus,

\(d_G(x,y)=1\equiv\phi(x)-\phi(y)(mod2)\)

holds, giving _x∼_<sub>par</sub> _y_. Parity-consistency of _x_ with other nodes connected to it follows by transitivity through _y_ (Lemma 6 using bipartiteness of _G_). Parity-consistency of pairs not involving _x_ comes by assumption as their potentials are unchanged. \(\blacktriangleleft\)

\(\blacktriangleright\) **Lemma 11.** _Let G be bipartite. If all connected pairs x,y of assigned nodes satisfy_ \(x\unknown\unknown y\) _and x∼_<sub>par</sub> _y, then also in the assignment of potentials resulting from ExpandBorders all connected pairs of assigned nodes satisfy_ \(x\unknown\unknown y\) _and x∼_<sub>par</sub> _y, and all outer nodes v have_ \(\phi(v)=0\).

