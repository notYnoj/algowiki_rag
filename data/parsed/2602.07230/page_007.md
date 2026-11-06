**Algorithm 1** Modified DGG Algorithm

**Input:** Unsplittable transshipment instance (_D,S_<sup>+</sup>_,S_<sup>-</sup>_,b,x_)

**Output:** Unsplittable transshipment defined by path sets \(\{\mathcal{P}_t\}_{t\in S^-}\)

1: Construct corresponding SSUF instance (_D_<sup>∗</sup>_,s_<sup>∗</sup>_,S_<sup>-</sup>_,d,x_); set _y_:=_x_

2: **while** there exists \(a=(v,t)\in A\) with \(y_a\ge d_t\) **do** \(\triangleright\) **Preliminary phase**

3: decrease _y<sub>a</sub>_ by _d<sub>t</sub>_; move _t_ to _v_; delete _a_ if _y<sub>a</sub>_=0

4: **while** some (sub-)sink has not reached _s_<sup>∗</sup> **do** \(\triangleright\) **Iterations**

5: Label singular arcs and funnel vertices

6: **if** a _nice alternating cycle_ is found **then**

7: Augment flow and move (sub-)sinks exactly as in the original DGG Algorithm

8: **else**

9: Move the (sub-)sinks in the singular digraph <sup>1</sup> backward to the super-source

10: Move further (sub-)sinks according to DGG moving rules

<sup>1</sup>(_sub-)sinks in the singular digraph_ refers to all (sub-)sinks other than _t_ located at vertices of the singular digraph, and the sub-sink _t_<sub>2</sub> of _t_.

ward depth-first search. For the second statement, observe that every vertex \(v\neq s^*\) in the singular digraph is a funnel vertex and hence has at most one outgoing arc. Moreover, this outgoing arc lies on the unique path from _v_ to the junction vertex _w_, which is entirely contained in the singular digraph.

In other words, Lemma 1 states that the sub-digraph of the current network induced by all vertices of the singular digraph except _s_<sup>∗</sup> is an in-tree, i.e., a directed tree rooted at _w_ with all arcs oriented toward it. As a consequence of Lemma 1, the flow _y_ on the singular digraph exactly satisfies the demands of all (sub-)sinks located at its vertices, with the sole exception of the uniquely chosen (sub-)sink _t_, for which only the amount \(d_{t_2}:=d_t-y_{a^\prime}\) is satisfied within the singular digraph. Since the singular digraph contains at most one path from each source in _S_<sup>+</sup> to each of its (sub-)sinks, any path decomposition of its flow yields an unsplittable transshipment that satisfies all these demands.

Equivalently, the algorithm decomposes the flow _y_ on the singular digraph into paths, splits each (sub-)sink into as many sub-sinks as there are paths serving it, and then moves each such sub-sink backward along its corresponding path to the super-source _s_<sup>∗</sup>. Finally, all arcs of the singular digraph are removed.

At the end of an iteration, further sinks may move backward towards super-source _s_<sup>∗</sup> exactly as in the original DGG Algorithm. Algorithm 1 gives a summary of the Modified DGG Algorithm.

## 3.2 Analysis of the Modified DGG Algorithm

The correctness of the Modified DGG Algorithm is based on the preservation of the same Invariants (i), (ii), and (iii) as the original DGG Algorithm.

_Proof of Invariant (i)._ If a nice alternating cycle is found in an iteration, the flow is augmented using the same procedure as in the original DGG Algorithm. This augmentation preserves the property that the flow satisfies the demands of all current (sub-)sinks that have not yet reached _s_<sup>∗</sup>. In the remaining iterations, the flow on the singular digraph exactly satisfies the demands of the (sub-)sinks located at its vertices. Consequently, removing the arcs of the singular digraph together with its (sub-)sinks does not violate Invariant (i).

