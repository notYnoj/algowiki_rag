**Theorem 6.** _Given a b-transshipment x, the adapted Modified DGG Algorithm efficiently computes an unsplittable transshipment such that the flow on each arc a is greater than x<sub>a</sub>-d_<sub>max</sub>.

As with the original DGG Algorithm, all steps remain the same except the augmentation step when a nice alternating cycle is found. In that case, we augment in the opposite direction: we increase the flow on the forward paths and decrease it on the backward paths.

## Tightness of the Modified DGG Algorithm.

For the SSUF problem, Dinitz, Garg, and Goemans \[DGG99\] show that a capacity violation of _d_<sub>max</sub> is unavoidable in the worst case. Since SSUF is a special case of the unsplittable transshipment problem, this bound is also tight for unsplittable transshipments when each sink is reachable from a single source. The tightness of the bound is less immediate in highly connected instances, where each sink is reachable from many sources, and its demand could, in principle, be split so as to reduce congestion. We show that this intuition is misleading: the bound of _d_<sub>max</sub> remains tight even when every sink is connected by directed paths to an arbitrarily large number of sources. A concrete construction establishing this result is given in Appendix C.

## Bounding the total number of paths.

By definition, an arbitrary unsplittable transshipment may use up to \(|S^+|\cdot|S^-|\) distinct paths. However, the following theorem implies that any unsplittable transshipment produced by the Modified DGG Algorithm uses at most |_S_<sup>+</sup>|+|_S_<sup>-</sup>|-1 paths. We refer to Appendix D for a proof.

**Theorem 7.** _Given an unsplittable transshipment, define a bipartite graph with vertex set_ \(S^+\cup S^-\) _by adding an edge between a source_ \(s\in S^+\) _and a sink_ \(t\in S^-\) _if and only if the transshipment routes flow along an s-t path. Then, the bipartite graph associated with any unsplittable transshipment computed by the Modified DGG Algorithm is acyclic, and thus contains at most_ |_S_<sup>+</sup>|+|_S_<sup>-</sup>|-1 _edges._

## Cost of Confluence.

Lemma 2 implies that the Modified DGG Algorithm returns a sink-wise confluent unsplittable transshipment. This leads to the question of whether such confluence has an inherent cost: are there instances with a feasible (non-confluent) unsplittable transshipment for which every confluent unsplittable transshipment has congestion close to _d_<sub>max</sub>, i.e., the largest possible gap?

The answer is yes, as demonstrated by a family of instances parameterized by _q_, illustrated for _q_=4 in Figure 2. Each sink _t<sup>i</sup>_ with \(i\in\{1,\dots,q\}\) must route its demand through arc _a<sub>i</sub>_. Thus, any unsplittable routing reserves 1-1_/q_ units of capacity on _a<sub>i</sub>_ for sink _t<sup>i</sup>_. If we additionally<tbc>

+1
s4
t4
-1 + 1
q
+1
s3
a4
t3
-1 + 1
q
a3
-1
t5
+1
s2
a2
t2
-1 + 1
q
a1
+1
s1
t1
-1 + 1
q

Figure 2: Family of instances (depicted for _q_=4) with unit arc capacities and _d_<sub>max</sub>=1, admitting a feasible non-confluent unsplittable transshipment, while any confluent unsplittable transshipment has congestion 1-1_/q_, tending to _d_<sub>max</sub> as \(q\rightarrow\infty\).

