## Nice alternating cycles and singular digraphs.

As in the original DGG Algorithm, we attempt to construct an alternating cycle by alternating between _forward_ (arbitrary) and _backward_ (singular) arcs. The last vertex reached on a forward path during an iteration is a junction vertex _w_ with no outgoing arcs. All incoming arcs of _w_ are singular, and, by flow conservation, _w_ necessarily contains one or more sinks. Furthermore, a vertex is called a _funnel vertex_ if it has at most one outgoing arc; otherwise, it is called a _non-funnel vertex_. Note that the head of any singular arc is a funnel vertex, and that backward paths in alternating cycles always terminate upon reaching a non-funnel vertex. We call an alternating cycle _nice_ if it does not contain the super-source _s_<sup>∗</sup>. Nice alternating cycles allow us to augment the flow without changing the supplies at the sources in _S_<sup>+</sup> and thus to proceed exactly as in the original DGG Algorithm.

There are, however, situations in which no nice alternating cycle can be found. This occurs precisely when, starting from a junction vertex _w_, all possible backward paths lead to the super- source _s_<sup>∗</sup>. Equivalently, _s_<sup>∗</sup> is the only non-funnel vertex reachable from _w_ via backward paths. This can be verified by a simple backward depth-first search (DFS) starting at _w_ while ignoring the arc \(a'\) used to reach _w_. If backward DFS finds a non-funnel vertex \(v\neq s^*\), we can continue our search for a nice alternating cycle along a forward path from _v_. Otherwise, if all backward paths lead to _s_<sup>∗</sup>, we refer to the sub-digraph explored by this backward DFS as the _singular digraph rooted at w_.

If a singular digraph rooted at the junction vertex _w_ is found, we select a (sub-)sink _t_ located at _w_ with \(d_t>y_{a^\prime}\). The existence of such a (sub-)sink is guaranteed by Invariant (ii), whose validity is established below. This (sub-)sink _t_ is uniquely chosen whenever a singular digraph is encountered and will later be split into two sub-sinks _t_<sub>1</sub> and _t_<sub>2</sub> with demands \(d_{t_1}:=y_{a^\prime}\) and \(d_{t_2}:=d_t-y_{a^\prime}\), respectively. After all other (sub-)sinks in the singular digraph have been moved to the super-source as described below, the sub-sink _t_<sub>2</sub> is created and routed to the super-source as well. Subsequently, the sub-sink _t_<sub>1</sub> is moved backward along the arc \(a'\), reducing the flow on \(a'\) to zero and thereby removing \(a'\) from the network.

**Lemma 1.** _With the exception of arc_ \(a'\)_, all incoming arcs of vertices in the singular digraph rooted at w belong to the singular digraph. Moreover, every vertex_ \(v\neq s^*\) _in the singular digraph has at most one outgoing arc, and this outgoing arc belongs to the singular digraph._

_Proof._ The first statement follows from the fact that the singular digraph is constructed via a back<tbc>

a'
junction w
a'
junction w
forward path
forward path
non-funnel # s*
continue with forward path
singular digraph
S*

Figure 1: Backward path discovery in the Modified DGG Algorithm starting at junction vertex _w_ with singular arcs depicted in thick: _Left_: a non-funnel vertex \(\neq s^*\) is found along some backward path, allowing to continue the construction of a nice alternating cycle; _Right_: the only non-funnel vertex found on backward paths is _s_<sup>∗</sup>, yielding a singular digraph rooted at junction vertex _w_.

