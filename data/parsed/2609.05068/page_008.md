## 2 Complexity

We prove that the decision problem associated with DCMCF is strongly NP- hard, even when there are at most three commodities, when all commodities share the same source and the same sink, and when the available path sets _P<sup>k</sup>_ include all possible paths for every commodity \(k\in K\).

This provides a stronger characterization than existing results in the literature. Previous work by [4] proved that the problem is weakly NP-hard, using a reduction from a 2-partition problem with a large number of commodities having distinct sources and destinations. Another form of delay constraints, where delays are proportional to link loads, was considered in [8]. The authors proved the NP-completeness of that variant and provided polynomial approximations under specific assumptions on the paths and graph topologies.

We consider a reduction from the 3-Partition problem [13]. This problem is defined as follows: decide whether a set _I_ of _n_ objects with sizes \(\{w_i\}_{i\in I}\) can be partitioned into _m=n/_3 disjoint subsets (triplets) \(\{T_j\}_{j\in I}\), such that each subset has the same sum _W/m_, where \(W=\sum_{i\in I}w_i\).

To prove the NP-hardness of DCMCF, we build an instance of DCMCF that admits a maximum concurrent flow of value \(\gamma\ge 1\) if and only if the given 3-Partition instance is of _True_ type.

Since scaling all object weights by the same positive factor does not affect the 3-Partition feasibility, we assume without loss of generality that the total weight is \(W=\frac{1}{(2n)^2}\). We also assume that \(w_i\le W/m\) for each object \(i\in I\), as the 3-Partition instance is otherwise trivially infeasible, and that \(m\ge 2\) (or \(n\ge 6\)) -- as the 3-Partition problem involving a single triplet is trivially feasible. Finally, we denote _N_=(2_n_)<sup>2</sup>.

Given such a 3-Partition instance, we construct a DCMCF instance on a directed graph _D_=(_V,A_) as illustrated in Figure 1.

The set of vertices _V_ consists of the following elements:

• A **source** vertex _s_ and a **destination** vertex _t_.<tbc>

