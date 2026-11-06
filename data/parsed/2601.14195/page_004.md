extend these to strong inapproximability results for the corresponding optimisation problems of interest. On the positive side, we present polynomial-time algorithms for instances with short preference lists, an approximation algorithm, and exact linear programming models. Finally, we show through experiments that almost-stable matchings and maximum-cardinality matchings that distribute the burden of instability well among agents are very likely to exist.

### 1.3 Structure of the Paper

First, in Section 2, we define crucial concepts of this paper and highlight relevant related works. Then, we start by introducing the minimax almost-stability notion in Section 3. There, we also provide crucial observations about their relationship to other, previously studied, notions, and structural characterisations. In Section 4, we highlight strong intractability results for the computation of minimax almost-stable matchings in various settings. On the positive side, we provide polynomial-time algorithms in Section 5 that compute optimal solutions for instances with preference lists of length at most 2. Furthermore, in Section 6, we investigate the approximability of our optimisation problems of interest. In Section 7, we provide integer programming formulations to solve our problems to optimality, and present experimental results. Finally, we summarise new and known complexity results in  3 and pose open questions in Section 8.

## 2 Background

### 2.1 Formal Definitions

We start by rigorously defining the models that we already introduced informally.

**Definition 2.1** (sri Instance)**.** _Let_ \(I=(A,\succ)\) _be a_ Stable Roommates with Incomplete Lists (sri) instance_, where A_={_a_<sub>1</sub>_,a_<sub>2</sub>_,...,a<sub>n</sub>_} _is a set of_ \(n\in\mathbb{N}\) _agents, and_ \(\succ\) _is a tuple of strict ordinal_ preference rankings \(\succ_i\) _of agents a<sub>i</sub> over an arbitrary subset of A_\\{_a<sub>i</sub>}. a<sub>i</sub>_ prefers _a<sub>j</sub> to a<sub>k</sub> if_ \(a_j\succ_ia_k\)_. We write_ \(a_j\unknown_ia_k\) _if_ \(a_j\succ_ia_k\) _or j=k. a<sub>i</sub> and a<sub>j</sub> are_ acceptable _if a<sub>i</sub> appears in_ \(\succ_j\) _and vice versa. Throughout, we assume that acceptability is symmetric._

_We can equivalently treat an_ sri _instance_ \(I=(A,\succ)\) _as a graph G_=(_A,E): let every agent_ \(a_i\in A\) _be a vertex in the graph and let all acceptable pairs of agents_ {_a<sub>i</sub>,a<sub>j</sub>_} _be in E. We refer to G as the_ acceptability graph _and say that I has_ complete preferences _if G is isomorphic to the complete graph K<sub>n</sub>, and_ incomplete preferences _if not. We also assume that every agent ranks themselves last._

**Definition 2.2** (smi Instance)**.** _Let_ \(I=(A,\succ)\) _be an_ sri _instance and let G be the acceptability graph of I. If G is bipartite, i.e., there exist disjoint sets A_<sub>1</sub> _and A_<sub>2</sub> _such that_ \(A=A_1\dot{\cup}A_2\) _and no agents within A_<sub>1</sub> _or A_<sub>2</sub> _are mutually acceptable, then we refer to I as a_ Stable Marriage with Incomplete Lists (smi) _instance. Furthermore, we say that_ smi _instance I has_ complete preferences _if G is isomorphic to K_<sub>|_A_<sub>1</sub>|,|_A_<sub>2</sub>|</sub>_, and_ incomplete preferences _if not._

We adopt the following notation and assume the following concepts for matchings.

**Definition 2.3** (Matchings)**.** _Let_ \(I=(A,\succ)\) _be an_ sri _(or_ smi_) instance. A_ matching _M of I is a set of unordered pairs of agents such that no agent a<sub>i</sub> is contained in more than one pair. If_ \(\{a_i,a_j\}\in M\)_, then we refer to a<sub>i</sub> as_ matched _and to a<sub>j</sub> as the_ partner _of a<sub>i</sub>, denoted by M(a<sub>i</sub>), and vice versa. If a<sub>i</sub> is not paired with any other agent, we say that a<sub>i</sub> is_ unmatched _and set M(a<sub>i</sub>_)=_a<sub>i</sub>._

_We denote the set of all matchings of I by_ M _and refer to some_ \(M\in\mathcal{M}\) _as a_ maximum- cardinality matching _if, for any_ \(M'\in\mathcal{M}\), \(|M|\ge|M'|\)_. We denote the set of all maximum- cardinality matchings by_ M<sup>+</sup>_. We refer to_ \(M\in\mathcal{M}^+\) _as_ perfect _if every agent is matched, and denote the set of such matchings by_ M_<sup>p</sup>._

