### Preprocessing Phase.

We are given a database S={_G_<sub>1</sub>_,G_<sub>2</sub>_,...,G<sub>k</sub>_} of _k_ attributed graphs, referred to as _prior graphs_.<sup>21</sup> We assume every graph in S has exactly _n_ vertices and _m_ edges, and that all global problem parameters are fixed across all instances. Each \(G_i\in\mathcal{S}\) is provided alongside its exact solution, denoted by _OPT(G<sub>i</sub>_). For decision problems (e.g., Negative Triangle), \(OPT(G_i)\in\{\text{YES,NO}\}\). For optimization problems (e.g., Constrained Shortest Path), _OPT(G<sub>i</sub>_) defaults to the optimal objective _value_. Note, however, that if the database equips _G<sub>i</sub>_ with an explicit _optimal solution_ (e.g., the actual optimal path or vertex set), all our algorithms are capable of reconstructing and outputting the exact optimal solution for the query graph as well.

The goal of the preprocessing phase is to compute a data structure over S to accelerate future queries. Generally, we consider polynomial preprocessing time as acceptable.

### Query Phase.

Upon receiving a query graph _H_, the algorithm must satisfy the following correctness guarantees. If _H_ is isomorphic to some prior graph \(G_i\in\mathcal{S}\), the algorithm must output the correct solution _OPT(H_)=_OPT(G<sub>i</sub>_). Otherwise, if _H_ is not isomorphic to any graph in S, the algorithm must either (i) output the correct solution _OPT(H_), or (ii) correctly declare that \(H\unknown\cong G_i\) for all \(G_i\in\mathcal{S}\).

We say an algorithm is correct _with high probability_ (w.h.p.) if it answers the query correctly with probability at least 1-1_/N<sup>c</sup>_ for any arbitrarily large constant \(c\ge 1\), where _N_ denotes the input size (of a single query). This probability is taken over the internal randomness of the algorithm. Throughout, our algorithms are analyzed under the standard _oblivious adversary_ model; that is, we assume the sequence of queries is generated independently of the algorithm’s internal random choices (see, e.g., \[NY15\] and \[KL14, Definition 3.4\]).

**Definition 5.3.** We say that a problem \(\Pi\) is _polynomial-time solvable inside the Isomorphic-Priors model_ if it can be solved in polynomial preprocessing time and polynomial query time.

## 5.3 Our Focused Approach: Invariant Representations

All our algorithms employ essentially the same unified design framework called _invariant representation_. In the following, we give an abstract description in its most basic form. Let G be the space of all valid input graphs for a computational problem \(\Pi\). Algorithms in this framework compute a function \(f:\mathcal{G}\rightarrow\mathcal{X}\), for some X called the _feature space_, that satisfies the following.

1. **Permutation Invariance:** For every \(G,H\in\mathcal{G}\), if \(G\cong H\), then _f(G_)=_f(H_).<tbc>

2. **Solution-Preserving:** For every \(G,H\in\mathcal{G}\), if _f(G_)=_f(H_), then \(OPT_\Pi(G)=OPT_\Pi(H)\).

We say that _G_ and _H_ are _f-equivalent_ if _f(G_)=_f(H_). We call such an _f_ an _Invariant and Solution-Preserving Signature for_ \(\Pi\). It is easy to see that Invariant and Solution-Preserving Signatures that are efficiently computable suffice to solve problems in our setting. For the next theorem, we assume that X={0,1}<sup>∗</sup> (which can always be achieved by encoding objects from X using binary strings).

**Theorem 5.4.** _Let_ \(\Pi\) _be a graph optimization or decision problem and let_ \(f:\mathcal{G}\rightarrow\{0,1\}^*\) _be an Invariant and Solution-Preserving Signature for_ \(\Pi\)_. Also let T(n_) _denote the time required to evaluate f on inputs of size at most n._

_Then there is an algorithm that solves_ \(\Pi\) _with k prior instances each of size at most n in_ \(O(k\cdot T(n))\) _preprocessing time and O(T(n_)) _query time._

<sup>21</sup>For simplicity, we focus on defining the model for graphs, though this framework naturally extends to every combinatorial object equipped with a well-defined notion of isomorphism.

