_Proof._ Consider an arbitrary \(\Delta_E\)-partial coloring \(\gamma\) of _G_. For an edge \(\{u,v\}\in E\), \(\mathrm{deg}_G(u)\le\Delta_E\) or \(\mathrm{deg}_G(v)\le\Delta_E\). Without loss of generality, let us assume that this holds true for vertex _u_. Therefore, by the definition of partial-coloring, each neighbor of _u_ must be colored properly with respect to _u_ by \(\gamma\), and hence, the edge {_u,v_} is not monochromatic and \(\gamma\) is a proper coloring of _G_.

This lemma tells us that when \(k=\Delta_E\), any valid _k_-partial coloring is in fact a proper coloring. Hence, the subgraph induced by edges realizing the maximum in \(\Delta_E\) forms the core of difficulty for partial coloring--it forces proper coloring behavior.

These graphs thus form the _hard instances_ for _k_-partial _k_-coloring. As we will observe in the following sections (Observations 1 and 2), all our lower bound constructions for centralized and distributed settings are captured by this characterization.

**Some Key Observations**

• For a given graph _G_, it is possible that \(\Delta_{E(G)}<\Delta(G)\). See Fig. 1 for such an example.<tbc>

<tbc>In fact, the following holds: For every graph _G_, \(\mathcal{K}(G)\le\Delta_{E(G)}\le\Delta(G)\) where K(_G_) is the degeneracy of the graph _G_. While the inequality \(\Delta_{E(G)}\le\Delta(G)\) follows immediately from the definitions, here is a simple argument that \(\mathcal{K}(G)\le\Delta_{E(G)}\). Partition _V(G_) into two sets: \(H=\{v\in V(G)|\mathrm{deg}(v)>\Delta_{E(G)})\}\) and _L=V(G_)∖_H_. The set _H_ is an independent set: if \(u,v\in H\) were adjacent, the vertices _u_ and _v_ would be incident to at least \(\Delta_{E(G)}+1\) edges, contradicting the definition of \(\Delta_E\). Now, order the vertices so that all vertices of _H_ appear first (in an arbitrary order), followed by all vertices of _L_ (also in an arbitrary order). In this ordering, each vertex has at most \(\Delta_{E(G)}\) neighbors appearing later, and thus \(\mathcal{K}(G)\le\Delta_{E(G)}\).<tbc>

<tbc>Therefore, the problems of _k_-partial (_k_+1)-coloring and _k_-partial _k_-coloring are generalizations of proper \((\Delta_E+1)\)-coloring and proper \(\Delta_E\)-coloring, respectively. These in turn are non-trivial generalizations<sup>1</sup> of proper \((\Delta+1)\)-coloring and proper \(\Delta\)-coloring.<tbc>

• The _k_-partial (_k_+1)-coloring algorithm of \[9\] implicitly provides an algorithm for \((\Delta_E+1)\)- coloring in \(O(\mathrm{log}^2\Delta_E\cdot\mathrm{log}n)\) rounds by adapting the Ghaffari-Kuhn rounding framework \[16\]. Our results show that reducing even one color from the palette makes the problem "hard" in the classical model as well as in the LOCAL model.

## 6 Classical Complexity

This section is dedicated to proving the following theorem.

**Theorem 1.** _For every fixed integer_ \(k\ge 3\)_, the problem of deciding whether an input graph G is k-partially k-colorable is NP-complete._

We prove Theorem 1 by reduction from the decision problem of proper _k_-colorability of an input graph. It was shown to be NP-complete for every constant \(k\ge 3\) \[12\]. Given an input graph _G_ of proper _k_-colorability, we transform _G_ into \(G'\) by replacing each edge \(\{u,v\}\in E(G)\) with the _edge gadget e_<sub>{_u,v_}</sub> which we define as follows.

<sup>1</sup>A problem \(\Pi\) is a _generalization_ of a problem \(\Pi'\) if every instance of \(\Pi'\) can be expressed as an instance of \(\Pi\) such that any algorithm for \(\Pi\) also solves \(\Pi'\) with the same complexity.

