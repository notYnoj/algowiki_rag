## 2 A short review of the Dinitz-Garg-Goemans Algorithm for SSUFs

In the following, we summarize the algorithm of Dinitz, Garg, and Goemans [DGG99] (the _DGG Algorithm_) and highlight key ideas underlying its analysis. Subsequently, in Section 3, we present an extended version of the DGG Algorithm for the Unsplittable Transshipment Problem.

### 2.1 Description of the DGG Algorithm

We consider an instance of the SSUF problem on an acyclic digraph _D_=(_V,A_) with a single source _s_, a set of sinks _S_<sup>-</sup> with associated demands _d<sub>t</sub>_ for \(t\in S^-\), and a flow _x_ that satisfies these demands. The DGG Algorithm iteratively modifies the initial flow _x_, and whenever the flow on an arc is reduced to zero during this process, the arc is removed from the network.

In a preliminary phase, starting from the given flow _y_:=_x_, the DGG Algorithm iteratively moves sinks backward toward the source _s_ along flow-carrying arcs whose flow meets or exceeds the sink’s demand, decreasing the flow _y_ on the traversed arcs accordingly. The preliminary phase terminates once every sink has either reached the source _s_ or is located at a vertex with at least two incoming arcs and is regular: A sink is called _regular_ if the flow on each arc entering its current vertex is strictly smaller than the demand of the sink; otherwise, the sink is _irregular_.

Once the preliminary phase ends, the algorithm iteratively augments the current flow _y_ along a carefully chosen alternating cycle and, in each iteration, tries to move the sinks toward the source _s_ according to certain rules.

A key notion for constructing alternating cycles is that of _singular arcs_. At the beginning of an iteration, an arc (_u,v_) is labeled _singular_ if _v_ and all vertices reachable from _v_ have out-degree at most one. An alternating cycle is constructed as follows. Starting from an arbitrary vertex, follow the outgoing arcs until a _junction vertex w_, that is, a vertex with no outgoing arcs, is reached (the _forward path_). Then, beginning with an incoming arc at _w_ that is distinct from the arc used to reach _w_, construct a _backward path_ traversing the incoming singular arcs as far as possible. Upon reaching a vertex with at least two outgoing arcs, resume the construction of a forward path. This alternation of forward and backward paths is repeated until a vertex is revisited, thereby forming an _alternating cycle C_ consisting of alternating forward and backward paths.

The flow _y_ is then augmented along the alternating cycle _C_ as follows. The flow on each forward arc of _C_ is decreased, and the flow on each backward arc of _C_ is increased, by the same positive amount which is the minimum of two values: The first value is the minimum flow along a forward arc of _C_. The second is the minimum of _d<sub>t</sub>-y<sub>a</sub>_ taken over all backward arcs _a_=(_v,w_) of _C_ and over all sinks _t_ at _w_ with _d<sub>t</sub>\>y<sub>a</sub>_. If the minimum is achieved by the flow _y<sub>a</sub>_ on a forward arc _a_, then the augmentation reduces the flow on this arc to zero and the arc is thus deleted. Finally, if possible, sinks are moved backward towards source _s_, preferably along singular arcs carrying exactly their demand, and otherwise along non-singular arcs carrying at least their demand.

The algorithm terminates once all sinks have reached the source _s_, and the resulting unsplittable flow is defined by the collection of paths traced by the sinks during their backward movement.

### 2.2 Analysis of the DGG Algorithm

The correctness and analysis of the DGG Algorithm relies on the following invariants, maintained throughout its execution:

(i) Flow _y_ satisfies all current demands of sinks not yet moved to _s_.<tbc>

