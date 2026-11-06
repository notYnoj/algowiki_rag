**Definition 1.6** (Conversion to STT: Root Rounding)**.** Let _U_ be a tree topology, and let _P_=(_X,Z,D_) be the solution found by the LP for some weights. _STT<sub>U</sub>(P_) is the search tree on _U_ that is computed recursively as follows. If _U_ has a single node, then we have a trivial singleton search tree. Otherwise, find a node _r_ such that: \(\forall v(\neq r)\in U:\sum_{u\in U:r\in[u\unknown v)}X_{uv}\ge\frac{1}{2}\). We clarify that \(r\in[u\unknown v)\) means that _r_ is on the path between _u_ and _v_, and may be _u_ (but not _v_). \[9\] proves that such a node exists. Set _r_ as the root of _STT<sub>U</sub>(P_), and construct its subtrees _STT<sub>H</sub>(P_) for each connected component \(H\subseteq U\backslash\{r\}\) recursively. We refer to this rounding method as _root rounding_ or simply _rooting_.

Intuitively, the choice of the root guarantees that some of the (fractional) depth of each node _v_ is due to nodes that are _r_ or belong to a different connected component than the one of _v_, when _r_ is removed (so we charge _r_ for them). Because of this, setting _r_ to be the root increases the depth of any node \(v\neq r\) by at most \(\frac{1}{2}\) compared to its fractional depth _D<sub>v</sub>_ which we know by the choice of _r_ is at least \(\frac{1}{2}\) for every \(v\neq r\). For a formal proof that such _r_ always exists, see Lemma 3.4 in \[9\]. We emphasize that there may be multiple choices for the root at any given step, so the resulting STT and its approximation ratio may depend on the tie breaking rule.

Property 2 (Theorem 3.1 of \[9\]) implies that when considering integer solutions, there is an optimal solution that is indeed a search tree (in fact, it is a vertex of the LP). Property 3 (Theorem 3.2 of \[9\]) implies that the feasible point corresponding to an optimal STT is a 2-approximation for the LP optimum. Golinsky \[9\] conjectured the following.

**Conjecture 1** (Conjecture 3.1 of \[9\])**.** For any topology and any vector of non-negative weights, there is an optimal STT that induces an optimal solution to the LP in Definition 1.2.

Conjecture 1 implies that all the vertices of the LP are STTs, since by Theorem 3.6 every vertex has some objective for which it is uniquely optimal. In the language of polytopes and extended formulations \[8\], Conjecture 1 states that the LP in Definition 1.2 is an extended formulation of an original polytope of interest. The original polytope is the convex hull of all STTs in _n_ dimensional _D_-space (depth per node), and the LP is (conjectured to be) an extended formulation with additional _X_ and _Z_ variables.

Since we care about Problem 1 and the LP is just a tool, a weaker conjecture is as follows.

**Conjecture 2.** For any topology and any vector of non-negative weights, rounding an optimal solution of the LP in Definition 1.2, according to the root rounding scheme (Definition 1.6) yields an optimal STT.

The work \[9\] verified the conjectures for trees up to \(n\le 4\) nodes, and lists several ideas and failed directions for a general proof. One hope to prove Conjecture 1 would be to show that all the vertices of the LP correspond to STTs, but this is not the case as we show in Theorem 3.7.

**We disprove both conjectures.** In simple words, we show that there exist tree topologies and frequencies such that the value of the best STT for them is strictly larger than the LP optimum, and that the rounding scheme might, and sometimes always, yield a sub-optimal STT. In particular, such optimum of the LP must be a non-integer solution by Property 2.

## 2 Disproving the Conjectures

In this section we disprove Conjectures 1 and 2. We first disprove Conjecture 1 by showing a specific non-integer vertex for a specific topology and frequencies such that this vertex is strictly<tbc>

