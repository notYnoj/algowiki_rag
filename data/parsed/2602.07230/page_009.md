<tbc>routed backward toward _s_<sup>∗</sup> within the singular digraph. By Lemma 1, the corresponding backward paths, after deleting _s_<sup>∗</sup>, form a tree. Since all arcs of the singular digraph are removed at the end of the iteration, all its vertices except for _s_<sup>∗</sup> have no outgoing arcs afterwards. Consequently, the paths along which the sub-sink _t_<sub>1</sub> (or its sub-sinks) is later moved backward toward _s_<sup>∗</sup> do not intersect any of these vertices.

_Second case._ Otherwise, by the same argument as for _t_<sub>2</sub> in the first case, the backward paths taken by _t_ (or its sub-sinks), after deleting _s_<sup>∗</sup>, form a tree.

In summary, the backward paths along which the demand of a sink _t_ (or its sub-sinks) is moved form, after deleting the super-source _s_<sup>∗</sup>, an arborescence rooted at _t_.

We are now ready to prove the main result of this section, generalizing the classical result of Dinitz, Garg, and Goemans \[DGG99\] to the Unsplittable Transshipment Problem.

**Theorem 3.** _Given a b-transshipment x, the Modified DGG Algorithm efficiently computes an unsplittable transshipment such that the flow on each arc a is strictly less than x<sub>a</sub>+d_max.

_Proof._ Lemma 2 implies that the algorithm computes an unsplittable transshipment. Thus, it remains to prove the bound on the flow values. As in the original DGG Algorithm, the flow on a non-singular arc is never increased. Hence, the total demand routed along an arc up to the point at which it becomes singular is less than its initial flow. Subsequently, the arc _a_ may appear repeatedly as a backward arc in nice alternating cycles, during which its flow may be increased multiple times. Observe that _a_ remains singular until it is removed from the network, since no arcs are added during the algorithm and vertex out-degrees never increase. In the following, we argue that the total increase of flow on _a_ is bounded by _d_max.

After the last increase of flow on _a_, let _y_ denote the resulting flow and let _t_ be the first regular (sub-)sink encountered at a vertex _v_ along the unique directed path starting at the head of _a_. If _v_ is the head of _a_, set _a<sub>v</sub>_:=_a_; otherwise, let _a<sub>v</sub>_ be the incoming arc of _v_ on this path. By Invariant (ii), _v_ is the first vertex on this path that contains a sink. Hence, by flow conservation, \(y_a\le y_{a_v}\le d_t\). In particular, the total increase of flow on arc _a_ is strictly less than \(d_t\le d_\mathrm{max}\).

The _congestion_ of a transshipment is defined as the maximum, over all arcs, of the ratio between the flow routed on the arc and its capacity. We assume the standard _balance condition_, that is, the capacity of every arc is at least the maximum demand _d_max. Under this assumption, Theorem 3 immediately implies the following corollary.

**Corollary 4.** _Under the balance condition, the Modified DGG Algorithm yields a_ 2_-approximation algorithm for minimizing congestion in unsplittable transshipment instances._

Instead of working with a super-source _s_<sup>∗</sup> as we did above, one could just as well introduce a super-sink _t_<sup>∗</sup> and then reverse all arc directions.

**Remark 5.** _Reversing all arcs yields a maximum capacity violation of at most_ \(\mathrm{max}_{s\in S^+}b(s)\)_. Thus, the Modified DGG Algorithm computes, in polynomial time, an unsplittable transshipment whose arc capacity violation is bounded by the minimum of the maximum supply_ \(\mathrm{max}_{s\in S^+}b(s)\) _and the maximum demand_ \(\mathrm{max}_{t\in S^-}|b(t)|\).

## 3.3 Further observations

### Arc-wise lower bounds for unsplittable transshipments.

Rohwedder and Svensson (personal communication, 2021) observed that the DGG Algorithm can be adapted to guarantee lower bounds on arc flows for unsplittable flows. By applying the same idea, one obtains an analogous result for the Unsplittable Transshipment Problem.

