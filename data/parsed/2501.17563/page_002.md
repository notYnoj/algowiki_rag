STT may be restructured by rotations (appropriately defined). Dynamic algorithms are described in \[4, 5, 6\].

We study a specific approach to computing STTs, that is based on linear programming (LP). Our text is self-contained and introduces everything that is necessary for understanding our results. Before we proceed, we give important terminology and definitions, followed by a formal statement of the problem we study.

**Definition 1.1** (Basic Definitions and Notations)**.**

1. Node: will always refer to an element of a tree.<tbc>

2. Underlying Topology: The topology over which to search. The topology will be consistently denoted as _U_ (for _Underlying_). We only consider topologies that are trees.<tbc>

(a) We also abuse the notation of _U_ to denote the set of nodes in this tree. Moreover, _n_ will always denote the number of nodes in _U_: \(n\equiv|U|\).<tbc>

(b) For two nodes \(i\neq j\), denote by \((i\unknown\unknown j)\) the (unique) path between them in _U_, excluding _i_ and _j_. Use square parenthesis to include _i_ and _j_: \([i\unknown\unknown j]\) (both), \([i\unknown\unknown j)\) (with _i_), \((i\unknown\unknown j]\) (with _j_).<tbc>

(c) We refer to specific topologies with \(2\le n\le 8\) as _U_<sub>(_n,i_)</sub> where _i_ changes according to the topology. Figure 6 (Section 2) and  7 (Appendix A) show the exact correspondence.<tbc>

3. STT: Search tree on tree. We use this term to avoid confusion with the underlying topology which is also a tree. We consistently use _T_ to denote an STT.<tbc>

(a) An STT _T_ is defined over a topology _U_ recursively as follows: Pick a node \(r\in U\) and set it to be the root of _T_. Each subtree of _r_ in _T_ is an STT which is constructed recursively over a connected components of _U_\\{_r_}. See Figure 1 for an example.<tbc>

(b) Frequencies, denoted by _f_: the relative number of queries of each node, a vector of _n_ non-negative values that sum to 1.<tbc>

(c) _depth(v_): The depth of a node _v_ in a given STT is the number of ancestors on its path to the root of the STT, including itself, _depth(root(T_))=1.<tbc>

(d) _cost(T,f_): the cost of a (static) STT _T_ with respect to frequencies _f_ is the sum of the depths of the nodes weighted by their frequencies: \(cost(T,f)=\sum_{v\in U}f_v\cdot depth(v)\).<tbc>

4. Linear programming (LP) related:<tbc>

(a) Weights, Direction, Objective (function): may be used interchangeably to describe the objective function of the linear program.<tbc>

(b) Vertex: always refers to a vertex of the polytope of the linear program (not to be confused with tree nodes).<tbc>

(c) We say that a point is integer if all of its coordinates are integer, and that a polytope is integer if all of its vertices are integer.<tbc>

(d) We reserve _P_ to denote points in space, and use subscripts such as _P<sub>X</sub>_ to denote the projection of _P_ to a set of coordinates _X_. We use P to denote a collection of points or a polytope. When in need, we use additional capitalized letters to denote points, and their corresponding blackboard-bold font to denote a set of points, for example _S_ and S.<tbc>

