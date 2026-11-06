Figure 3, even if (_G,H,u,d_) is feasible, it may not have an uncrossed feasible multiflow<sup>7</sup>. However several classes do admit uncrossed solutions. We say (_G,H_) is an _uncrossable layout_ if for all _u,d_, if (_G,H,u,d_) has a feasible multiflow, then (_G,H,u,d_) has a feasible uncrossed multiflow. Matsumoto et al. \[22\] give an algorithm that, given a feasible fully-planar (_G+H_ planar) instance, produces a feasible uncrossed flow. Thus fully-planar layouts are uncrossable. It is also well-known that single-source layouts (_H_ is a star) are uncrossable. Another uncrossable layout is given when _G_ is a cycle with parallel edges and _H_ is arbitrary, which we call _ring_ layouts. In Section 3 we introduce _pairwise-planar_ layouts and prove they are uncrossable.

## 2.3 Another View on Crossing: Parallelizations

There are more intuitive ways to think about uncrossed paths that we frequently use.

**Widened Graph:** Suppose we "widen" _G_, making its nodes into small disks and its edges into small channels. A family of pairwise uncrossed paths can have its paths drawn as curves simultaneously, each curve following the node disks and edge channels corresponding to its path, so that the curves are disjoint.

**Parallelizations:** To avoid dealing with the formal topology of widened graphs, we use an equivalent notion based on "separating" the paths at each edge. Consider a family of paths P and for each \(e\in E(G)\) let \(\mathcal{P}_e=\{P\in\mathcal{P}:e\in E(P)\}\). Let \(G'\) be obtained by replacing each _e_ with |P_<sub>e</sub>_| parallel copies of itself. Intuitively, the parallel edges represent the curves within the channel of _e_.

Now, for each \(e\in E(G)\) we decide on some one-to-one mapping \(\phi_e\) from P_<sub>e</sub>_ to the parallel class of _e_ in \(G'\). For each \(P\in\mathcal{P}\), we obtain a path \(P_\phi\) in \(G'\) whose edges are \(\{\phi_e(P):e\in P\}\). This induces a family of edge-disjoint paths \(\mathcal{P}_\phi\) in \(G'\). We call \(\mathcal{P}_\phi\) a _parallelization_ of P. If we (arbitrarily) orient each \(e\in E(G)\), it gives a linear ordering \(\le_e\) of P_<sub>e</sub>_. Different choices for \((\phi_e:e\in E(G))\) yield different parallelizations. The family P is pairwise uncrossed if and only if there is some parallelization that is pairwise uncrossed at every<tbc>

<sup>7</sup>In fact, it is not always possible to find an uncrossed flow with bounded congestion. One may modify the canonical grid instance \[16\] so it has a half-integral routing of demands, but any uncrossed multiflow incurs polynomial congestion.

t2
t2
S1
t1
S1
t1
S2
S2

e
z
e
g
e'
g'
g
Z
Z

Figure 3: Problematic instances for uncrossability. Capacities and demand values are unit. (Left) A congestion instance with a feasible multiflow but no uncrossed multiflow. (Right) The _Keyhole Instance_, a congestion instance with a feasible uncrossed trail-multiflow but no uncrossed path-multiflow.

Figure 4: (Left) An uncrossed parallelization of the uncrossed paths from Figure 2. (Right) Disk-expansion of the node _z_ after uncrossed parallelization.

