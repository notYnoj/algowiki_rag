instance has complete preferences (with respect to this bipartition) if its acceptability graph is isomorphic to the complete bipartite graph on |_A_<sub>1</sub>|,|_A_<sub>2</sub>| vertices.

Throughout, we define matchings and associated concepts as follows.

**Definition 2.2** (Matchings)**.** _Let_ \(I=(A,\succ)\) _be an_ sri _(or_ smi_) instance. Then a_ matching _M of I is a set consisting of (unordered) disjoint pairs of agents. For any pair_ \(\{a_i,a_j\}\in M\)_, we refer to a<sub>j</sub> as the_ partner_, denoted by M(a<sub>i</sub>), of a<sub>i</sub>, and vice versa. If there exists some a<sub>j</sub> such that_ \(\{a_i,a_j\}\in M\)_, then we refer to a<sub>i</sub> as_ matched _in M. Otherwise, we refer to a<sub>i</sub> as_ unmatched _and denote M(a<sub>i</sub>_)=_a<sub>i</sub>._

_The set of all matchings of I is given by_ M_. A_ maximum-cardinality matching _is a matching M of I such that, for any other_ \(M'\in\mathcal{M}\)_, it is true that_ \(|M|\ge|M'|\)_. The set of all maximum-cardinality matchings is denoted by_ M<sup>+</sup>_. Furthermore, maximum-cardinality matchings are_ perfect _if every agent is matched (to someone other than themselves). The set of perfect matchings (which might be empty) is denoted by_ M_<sup>p</sup>._

We formalise the classical concept of stability below.

**Definition 2.3** (Stability)**.** _Given an_ sri _(or_ smi_) instance_ \(I=(A,\succ)\) _and a matching M of I, a pair of distinct agents_ {_a<sub>i</sub>,a<sub>j</sub>_} _is a_ blocking pair _of M if_ \(a_i\succ_jM(a_j)\) _and_ \(a_j\succ_iM(a_i)\)_. The set of blocking pairs of M is denoted by bp(M). Given an agent a<sub>i</sub> and a matching M, we can restrict the set of blocking pairs to those containing a<sub>i</sub>, the set of which we denote by bp<sub>a<sub>i</sub></sub>(M). Finally, we refer to a<sub>i</sub> as a_ blocking agent _if_ \(bp_{a_i}(M)\neq\emptyset\)_. The set of all blocking agents of a matching M is denoted by ba(M)._

Any matching that has an empty set of blocking pairs is referred to as _stable_. Any other matching is referred to as _unstable_. Furthermore, we refer to an instance that admits at least one stable matching as _solvable_, and as _unsolvable_ otherwise.

We also assume knowledge of the following "almost-stable" matching problem that aims to minimise the number of blocking pairs, first formalised by Abraham et al. \[1\].

In the introduction, we highlighted already that even a solvable instance might not admit a stable matching which is simultaneously a maximum-cardinality matching. Given the practical importance of large matchings, another key almost-stable matching problem is to find a maximum-cardinality matching that minimises the number of blocking pairs it admits \[8\], which we define below.

To establish key computational complexity results in this paper, we will refer to the decision problem (2,2)-e3-sat, which is a restriction of the classical Satisfiability problem (sat), that is known to be NP-complete, see Berman et al. \[5\]. The problem is defined as follows.

MinBP-AlmostStable-sri
Input: sri instance I.
Output: A matching M of I such that |bp(M)| = minM' \in\mathcal{M}|bp(M')|.

MinBP-AlmostStable-Max-smi
Input: smi instance I.
Output: A maximum-cardinality matching M of I such that |bp(M)| = minM' \in\mathcal{M}^+|bp(M')|.

(2,2)-e3-sat
Input: Boolean formula B in CNF, where every clause contains exactly three (distinct) literals, and every variable occurs exactly twice unnegated and twice negated.
Question: Does B admit a satisfying truth assignment?

