• Compute _x<sub>k</sub>_ from its predecessors using the recurrence<tbc>

<tbc>\(x_k=\oplus_{(u,k)\in E}(x_u\otimes w_{u,k}),\)<tbc>

<tbc>where each predecessor _u_ is either in _B<sub>I</sub>_ (if _u\<i_) or has already been processed in {_i,...,k_-1}. For \(u\in B_I\), _x<sub>u</sub>_ is part of the boundary, and for \(u\in[i,k-1]\) we maintain _x<sub>u</sub>_ in _M_ by induction.<tbc>

• Insert (_k,x<sub>k</sub>_) into _M_.<tbc>

• Remove from _M_ any vertex _u_ that will never be used again as a predecessor of any vertex in _I_ with index _\>k_. Formally, we remove _u_ if there is no \(w\in I\) with _w\>k_ and \((u,w)\in E\). To test this, for each \(u\in M\) we scan the adjacency list of _u_ on the read-only input tape and check whether there exists such a successor in _I_; if not, we delete _u_ from _M_.<tbc>

3. Whenever \(k\in U\), record (or output) the value _x<sub>k</sub>_.

At any time _k_, the set of vertices _u_ that have a successor in _I_ with index _\>k_ is contained in \(\text{Front}(k)\cap(B_I\cup V_I)\), whose size is at most \(\omega\) by definition of frontier width. By construction _M_ never contains any vertex outside this set, so \(|M|\le\omega\) throughout the computation. The algorithm uses only the working buffer _M_ plus a constant amount of scratch space for scanning adjacency lists and indices, so the additional work-tape space beyond the representation of the boundary values is \(O(\omega)\).

Finally, by Lemma 1, recomputing the DP in this way using the true boundary values yields the same _x<sub>v</sub>_ as in the global DP, for all \(v\in U\).

This lemma guarantees that, modulo \(O(\omega)\) workspace, we can compute:

• **Forward costs.** Given values on a left boundary \(B_I\subseteq\text{Front}(i-1)\), we can compute the optimal value to reach any \(v\in F_I^\text{out}\) via paths whose internal vertices lie in _I_.<tbc>

• **Suffix costs.** Given a vertex \(v\in I\) and a sink \(s\in I\) with \(v\le s\), we can similarly run a forward DP on the induced subgraph of _I_ starting from _v_ to compute the optimal value of a path from _v_ to _s_ whose internal vertices lie in _I_. As with the prefix computation, the active set remains a subset of the global frontier, ensuring the \(O(\omega)\) space bound.

In the next section, we will use these local evaluations as building blocks in a recursive, meet-in- the-middle traceback algorithm structured by the recursion tree R. The global-to-local consistency of Lemma 1 will ensure that whenever we seed a local DP with true boundary values, the recomputed predecessors agree with the unique global predecessor map on the relevant vertices.

## 5 Universal Hirschberg Algorithm

We now present the core algorithm and its complexity analysis. The construction generalizes Hirschberg’s divide-and-conquer strategy from grids to arbitrary DP DAGs, achieving space efficiency by trading recomputation for memory. Structurally, the algorithm is a meet-in-the-middle traceback scheme organized along the recursion tree R from Section 4, operating in the offline random-access model of Section 2.

### 5.1 Problem restatement and invariant

Fix a DP DAG \(G=(V,E,S_\text{src},T_\text{sink},\tau)\) satisfying Assumptions 1 and 2, and let \(t\in T_\text{sink}\) be a designated sink. Let _x<sub>t</sub>_ denote its optimal value under the global recurrence.

The traceback algorithm maintains recursive subproblems of the following form.

**Traceback subproblem** (_I,B_left_,s,_val):

• _I_=\[_i,j_\] is an interval in the recursion tree R.<tbc>

• _B_left is a boundary set of vertices with indices _\<i_ or in _S_src (possibly empty at internal levels) with known values \(\{x_u\}_{u\in B_\text{left}}\).<tbc>

• \(s\in V_I\) is a target vertex with \(i\le s\le j\).<tbc>

• \(\text{val}\in\mathcal{S}\) is the optimal value of a path from _some_ \(u\in B_\text{left}\) to _s_ whose internal vertices lie in _I_.<tbc>

