## 4.3 Correctness of the algorithm output

Now we prove that Algorithm 1 maintains parity-consistency and potential-separation between all connected nodes. We prove one by one that these invariants hold for the partial potential assignment between each of the main subprocedures FixAndClear (Lemma 8), ExpandBorders (Lemmas 9-11) and TwoColoring (Lemmas 12 and 13). From this we conclude that the invariants are maintained by the update after every insertion (Theorem 14) and the algorithm produces a correct coloring (Corollary 15).

Unless otherwise specified, in this section _G_ and \(\phi\) refer to some state of algorithm Algorithm 1 and the stage of the algorithm will be explicitly mentioned in the context where they occur. Furthermore, we use the following terminology: We call a node _unassigned_ if \(\phi(v)=\perp\), otherwise the node is _assigned_. If it is assigned and has unassigned neighbors we call it an _outer node_.

We start by proving the correctness of the FixAndClear procedure.

\(\blacktriangleright\) **Lemma 8.** _Let G and_ \(G'\) _be two bipartite graphs which differ only in the existence of the edge e between nodes v and w. Let_ \(\phi\) _be a function_ \(V(G)\rightarrow\mathbb{N}\)_. Let all pairs x,y which are connected in G satisfy_ \(x\unknown\leftrightarrow y\) _and_ \(x\sim_\text{par}y\) _with respect to G and_ \(\phi\).

_Then, also in the assignment of potentials_ \(\phi'\) _resulting from FixAndClear(e_) _applied on the graph_ \(G'\) _and_ \(\phi\) _as original state, all connected pairs of assigned nodes satisfy_ \(x\unknown\leftrightarrow y\) _and_ \(x\sim_\text{par}y\) _with respect to_ \(G'\) _and_ \(\phi'\).

**Proof.** Let \(\phi_0\) be the original assignment of potentials, \(\phi_1\) the assignment after fixing the parity and \(\phi_2\) the final assignment after fixing parity and clearing the edit area.

We need the following facts about any pair of nodes _x,y_ that were connected in the original graph _G_:

(1) _If x and y are connected in G, then_ \(d_G(x,y)\equiv d_{G^\prime}(x,y)\) (mod 2), otherwise there would be an odd-length loop in \(G'\), violating bipartiteness.

(2) _If x and y are connected in G, then_ \(\phi_0(x)-\phi_0(y)=\phi_1(x)-\phi_1(y)\). This equality holds because _x_ and _y_ must be in the same component of _G_, so either both are incremented or neither.

(3) _If x and y are connected in G, then_ \(x\sim_\text{par}y\) _in_ \(G'\) _under_ \(\phi_1\). By assumption, as _x_ and _y_ are connected, we have \(x\sim_\text{par}y\) in _G_ under \(\phi_0\). It follows, using Items 1 and 2 that

\(d_{G^\prime}(x,y)\equiv d_G(x,y)\equiv\phi_0(x)-\phi_0(y)\equiv\phi_1(x)-\phi_1(y)(mod2),\)

which proves \(x\sim'_\text{par}y\) in \(G'\) under \(\phi_1\).

Now, we prove that both of the relations \(\sim_\text{par}\) and \(\unknown\unknown\) hold in \(G'\) under \(\phi_2\). It suffices to show this for pairs of _x_ and _y_ that are connected to _e_ in \(G'\). Otherwise, their distance and potential has not changed, so \(x\sim_\text{par}y\) and \(x\unknown\leftrightarrow y\) still hold in \(G'\) under \(\phi_2\).

**1.** We first prove that \(x\sim_\text{par}y\) holds in \(G'\) under \(\phi_2\). Let _x_ and _y_ be connected to _e_ in \(G'\), which we have shown to suffice. We prove that \(x\sim_\text{par}y\) in \(G'\) under \(\phi_1\), from which it directly follows that it also still holds for all connected assigned pairs in the cleared assignment \(\phi_2\). We proceed by distinguishing whether _x_ and _y_ are connected:

**a.** If _x_ and _y_ are connected in _G_, then using fact 3 proven above, \(x\sim_\text{par}y\) in \(G'\) under \(\phi_1\) as required.

**b.** Otherwise, _x_ and _y_ are not connected in _G_. Then, they must each be either in _C<sub>v</sub>_ or _C<sub>w</sub>_, since they are connected to _e_. Without loss of generality, let \(x\in C_v\) and \(y\in C_w\). Using fact 3, we have \(x\sim_\text{par}v\) and \(y\sim_\text{par}w\) in \(G'\) under \(\phi_1\). We prove that \(v\sim_\text{par}w\) after parity-fixing by distinguishing two cases:

