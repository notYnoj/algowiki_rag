With this additional specification of the Modified DGG Algorithm, we are now ready to prove Theorem 7.

_Proof of Theorem 7._ We prove the result by analyzing how the bipartite graph _G_ evolves during the execution of the Modified DGG Algorithm. Whenever a sink \(t\in S^-\), or one of its sub-sinks, reaches a source \(s\in S^+\) along its backward path to the super-source _s_<sup>∗</sup>, we add the edge {_s,t_} to _G_.

A source \(s\in S^+\) is called _active_ as long as it has at least one outgoing arc. Similarly, a sink \(t\in S^-\) is called _active_ as long as _t_, or one of its sub-sinks, has not yet reached the super-source _s_<sup>∗</sup>. Note that at any time there is at most one (sub-)sink of _t_ that has not reached the super-source. Indeed, whenever a (sub-)sink is split into two sub-sinks, one of them is immediately moved along a backward path within a singular digraph, whose arcs are then deleted.

We prove that the following invariants are maintained throughout the execution of the Modified DGG Algorithm:

(\*) _G_ is acyclic and every connected component of _G_ contains at most one active source or sink.

After the preliminary phase of the algorithm, some sinks may have reached the super-source _s_<sup>∗</sup> via a source in _S_<sup>+</sup>. These sinks are inactive and have exactly one incident edge in _G_, connecting them to their corresponding source in _S_<sup>+</sup>. All remaining sinks are still active and isolated in _G_. In particular, the invariant (\*) is satisfied at this point.

Throughout the execution of the algorithm, the bipartite graph changes only when a sink _t_, or one of its (sub-)sinks, reaches a source \(s\in S^+\) and is then immediately moved further backward to the super-source. Prior to this step, both _t_ and _s_ are active and therefore belong to distinct connected components of _G_, which are merged by the addition of the edge {_s,t_}. In particular, _G_ is still acyclic. It only remains to show that _s_ or _t_ are inactive after this step such that the new connected component of _G_ formed by edge {_s,t_} contains at most one active source or sink.

If _t_ has become inactive, we are done. Otherwise, _t_ was split into two sub-sinks _t_<sub>1</sub> and _t_<sub>2</sub> in the previous step, and only _t_<sub>2</sub> was moved to the super-sink _s_<sup>∗</sup> via a source \(s\in S^+\). In this case, the demand of _t_<sub>2</sub> was set equal to the flow value _y<sub>a</sub>_ of the unique outgoing arc _a_ of _s_, so that _a_ was deleted and _s_ consequently became inactive.

## Appendix E Routing in a constant number of rounds

### Routing in six rounds when \(d_\mathrm{max}\le c_\mathrm{min}/3\).

As in Section 4.1, construct an auxiliary graph \(D'\) with _q_=2 copies of _D_, each carrying half of the original flow. Applying the Modified DGG Algorithm yields a feasible routing in each copy, since _c<sub>a</sub>/_2+_d_<sub>max</sub>_\<c<sub>a</sub>_. These two copies directly serve as two routing rounds for all non-critically split sinks.

Each critically split sink is labeled by the copy containing its forward path(s). For sinks with the same label, we further distinguish two cases according to how much of its demand is routed along the singular digraph: _Type_ 1, at least half, i.e. \(\ge d_t/2\); and _Type_ 2, less than half, i.e. _\<d<sub>t</sub>/_2. This produces four groups in total (two labels times two types). We route each group in a separate additional round, yielding four extra rounds and six rounds overall.

_Feasibility._ Consider a group labeled by Copy 1 (the case of Copy 2 is symmetric). In its routing round, the singular digraph (lying in Copy 2) contributes at most _d_<sub>max</sub> flow per arc for Type 1 and at most _d_<sub>max</sub>/2 for Type 2, while the forward paths (lying in Copy 1) contribute at most _c<sub>a</sub>/_2+_d_<sub>max</sub>/2 for Type 1 and _c<sub>a</sub>/_2+_d_<sub>max</sub> for Type 2. In either case, the total flow on any arc _a_ is bounded by<tbc>

\(c_a/2+3d_\mathrm{max}/2\le c_a,\)

