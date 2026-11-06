element. The new pendant vertices have traces among \(\emptyset\) and the singletons {_u_} for \(u\in A_0\). Consequently, the total number of traces on _A_ is at most

\(c|A|^\rho+|A|+1\le(c+2)|A|^\rho.\)

Also, \(|V(G')|\le 2n\), \(|U|\ge(\delta/2)|V(G')|\), and \(\mathrm{deg}_{G^\prime}(u)=\mathrm{deg}_G(u)+1\) for every \(u\in U\). We can therefore apply the twin-free case to \(G'\) and _U_ with constants _c_+2, \(\rho\), and \(\delta/2\). This application has the claimed expected running time. Finally, deleting the new pendant vertices cannot increase a symmetric difference, so the returned pairs satisfy the asserted bound in _G_ as well.

We now present the randomized linear-time algorithm computing an sd-degeneracy sequence.

**Theorem 4.** _For every real number_ \(\rho\ge 1\) _and every graph class_ C _of VC density_ \(\rho\)_, there is a randomized algorithm that, given a graph_ \(G\in\mathcal{C}\)_, outputs an sd-degeneracy sequence of G of width_ \(\mathcal{O}_\mathcal{C}(n^{1-\frac{1}{\rho}})\) _in expected time_ \(\mathcal{O}_\mathcal{C}\big(|V(G)|+|E(G)|\big)\).

_Proof._ Let \(c\ge 1\) be such that every graph in C has \((c,\rho)\)-polynomial neighborhood complexity. Write _n_:=|_V(G_)|, _m_:=|_E(G_)|, and \(\alpha:=1-1/\rho\). We build a sequence _G_<sub>1</sub>_,G_<sub>2</sub>_,..._ of induced subgraphs of _G_, with _G_<sub>1</sub>:=_G_. Every _G<sub>i</sub>_ still has \((c,\rho)\)-polynomial neighborhood complexity.

In every iteration _i_ with \(n_i:=|V(G_i)|\ge 3\), let \(U_i\subseteq V(G_i)\) be the set of \(\lceil n_i/2\rceil\) vertices of _G<sub>i</sub>_ with smallest degrees, breaking ties arbitrarily. By Lemma 26, applied to _G<sub>i</sub>_, _U<sub>i</sub>_, and \(\delta=1/2\), in expected time

\(\mathcal{O}_{c,\rho}\left(n_i+\sum_{u\in U_i}\mathrm{deg}_{G_i}(u)\right)\)

we find a set P_<sub>i</sub>_ of \(\Omega_{c,\rho}(n_i)\) disjoint pairs of \(\mathcal{O}_{c,\rho}(n_i^\alpha)\)-near-twins inside _U<sub>i</sub>_. We order every pair of P_<sub>i</sub>_ arbitrarily, append the ordered pairs to the output sequence, and obtain _G_<sub>_i_+1</sub> by deleting the first vertex of every pair. When at most two vertices remain, we append their pair if there are two vertices, and terminate.

**Claim 29.** _The output is an sd-degeneracy sequence of G of width_ \(\mathcal{O}_{c,\rho}(n^\alpha)\).

_Proof of claim._ Consider a pair (_u,v_) from a batch P_<sub>i</sub>_ when it is reached in the output sequence. Earlier pairs of the same batch are vertex-disjoint from (_u,v_), and the graph then present is an induced subgraph of _G<sub>i</sub>_. Hence, its symmetric difference is no larger than it was in _G<sub>i</sub>_, where (_u,v_) is a pair of \(\mathcal{O}_{c,\rho}(n_i^\alpha)\)-near-twins. Since \(n_i\le n\), this is \(\mathcal{O}_{c,\rho}(n^\alpha)\). If the algorithm terminates with two vertices, their symmetric difference is at most 2, and hence at most \(2n^\alpha\). \(\lrcorner\)

**Claim 30.** _The expected running time is_ \(\mathcal{O}_{c,\rho}(n+m)\).

_Proof of claim._ We maintain deg<sub>_G<sub>i</sub>_</sub>(_v_) for every current vertex _v_, initialized in O(_n+m_) time. When vertices are deleted, we update the degrees of their surviving neighbors; all such updates cost O(_n+m_) in total. In iteration _i_, a linear-time selection algorithm applied to these maintained degrees finds the \(\lceil n_i/2\rceil\) vertices of smallest degree in O(_n<sub>i</sub>_) time.

By conditional linearity of expectation, the remaining expected work is bounded by

\(\mathcal{O}_{c,\rho}\left(\sum_in_i+\sum_i\sum_{u\in U_i}\mathrm{deg}_{G_i}(u)\right).\) (1)

