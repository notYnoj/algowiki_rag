<tbc>node of \(G'\) (rather than needing to consider longer shared subpaths). Using parallelizations helps us simplify subsequent definitions by assuming paths are edge-disjoint. Given a collection of paths, one can compute in polynomial time an uncrossed parallelization or find a crossing pair of paths.

**Disk-Expansion:** After parallelization, we sometimes go a step closer to the widened graph idea by "expanding" a node _v_. We draw a small disk with _v_ at its centre (small enough that its boundary intersects only \(\delta(v)\), and hits each edge once). Where an edge copy intersects the boundary, we place a new node. We terminate the edges at these new nodes. For an uncrossed parallelization, it is then possible to (simultaneously) draw edges in the open interior of the disk between nodes that correspond to consecutive edges of the same path, such that the drawing is planar. An example is shown in Figure 4.

## 2.4 Strongly Uncrossed Multiflows

Consider an uncrossed multiflow. For any \((s,t)\in E(H)\), its support paths have a clockwise ordering about _s_ (and _t_) given by the parallelization. We call the regions of the plane bounded between two consecutive paths _sectors_ for this commodity (defined more formally in Section 5).

The proof of Theorem 1.3 uses that sectors of different commodities are non-crossing as sets - that is, we want that if \(A,B\subseteq\mathbb{R}^2\) are sectors of different commodities, then either \(A\cap B=\emptyset\) or one contains the other. One might think this non-crossing property follows from Theorem 2.2, however Figure 5 shows a counterexample<sup>8</sup>. In the figure, no pair of flow paths cross, but the green _s_<sub>2</sub>_t_<sub>2</sub>-paths "slip between" the blue _s_<sub>1</sub>_t_<sub>1</sub>-paths to move between two distinct sectors. We define _strongly uncrossed_ multiflows by imposing stricter restrictions on the support paths of different commodities at their terminals. Many layout classes admit these strongly uncrossed flows, including fully-planar, single-source, and rings, as well as pairwise-planar.

**Definition 2.3** (Quasicrossing, Strongly Uncrossed)**.** Let _f_ be a multiflow, with a fixed parallelization (so we assume support paths are edge-disjoint). Consider a node _z_ and the clockwise ordering of edges _e_<sub>1</sub>_,...,e<sub>k</sub>_ about _z_. For a commodity _h_, a _type-1_ (_h,z)-interval_ is \[_i,j_\] (where _i\<j_) such that _e<sub>i</sub>,e<sub>j</sub>_ are consecutive edges of a single support path for _h_ that transits through _z_. A _type-2_ (_h,z)-interval_ is \[_i,j_\] (_i\<j_) such that _e<sub>i</sub>,e<sub>j</sub>_ both terminate (different) support paths for _h_ at _z_. Note that two paths cross at _z_ if and only if their corresponding type-1 intervals cross<sup>9</sup>. We say a _quasicrossing_ occurs at _z_ if there exists an (_h,z_)-interval _I_ and an \((h',z)\)-interval \(I'\) that cross where \(h\neq h'\) and at least one of the intervals is type-2. If there are no crossings and no quasicrossings at any node, we say _f_ is _strongly uncrossed_.

<sup>8</sup>The desired non-crossing sector property does hold for uncrossed flows in _leaf instances_, where terminals all have degree 1. Moving each terminal to its own new leaf node is a standard pre-processing operation, but this is not safe for uncrossed flows - it may turn an uncrossable layout into one that is not. For example, ring instances admit uncrossed flows but Figure 3 (left) does not, even though it is obtained by adding leaves to a ring instance. <sup>9</sup>Two intervals \([i,j],[i',j']\) cross if \(i<i'<j<j'\) or \(i'<i<j'<j\).

t1
t1
t2
t2
S2
S2
S1
S1

Figure 5: (Left) An uncrossed multiflow. The blue paths are for (_s_<sub>1</sub>_,t_<sub>1</sub>) and the green paths are for (_s_<sub>2</sub>_,t_<sub>2</sub>). No pair of support paths cross. (Center) A sector from the _s_<sub>1</sub>_t_<sub>1</sub>-flow (blue shaded region) that crosses a sector from the _s_<sub>2</sub>_t_<sub>2</sub>-flow (green shaded region). (Right) The disk-expansion of _s_<sub>1</sub>. The green path separates the blue nodes in the disk. There is a quasicrossing at _s_<sub>1</sub>.

