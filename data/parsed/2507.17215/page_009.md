<tbc>finds that that _x_’s counter is non-zero, it will prune the search and move on to the next interval.

However, if _I<sub>y</sub>_ is inserted before _I<sub>x</sub>_, then we have a problem. This is because now, the path leading upto _x_ does not contain _y_. Therefore, the algorithm will increment its counter by 1, and when queried with _t_, it will return 2 as opposed to 1. To get past this issue, we introduce the idea of _lazy updating_ of counters.

Broadly speaking, the idea is to delay counter updates rather than performing them immediately upon each interval insertion. This is implemented as follows: when an input interval is inserted and a node in the tree is selected to store it, instead of updating the node’s counter right away, we mark the node as grey. For example, both _x_ and _y_ would be marked grey in this step, which we refer to as _Phase-1_.

Next, we proceed to _Phase 2_, where all the intervals are re- inserted in the original order. During this re-insertion, if an interval is to be placed at node _k_, and none of the nodes along the insertion path are grey, we keep _k_ grey. However, if there is any grey node along the path to _k_, we reset _k_’s color to white. In the earlier example, since _x_ lies on the path to _y_ and is grey, _y_ is turned back to white.

In the final phase i.e. _Phase 3_, the intervals are inserted once more, and this time, we update the counters only at the nodes that remain grey. So, in the previous case, we will only update the counter of _x_ and not of _y_. As a result, the algorithm will return 1 as opposed to 2. Full implementation details are provided in the supplementary material.

### 3.4 Putting it All Together

Combining the ways to deal with the in-neighbours and out-neighbours, we present the overall algorithm in algorithm-5. Refer to Appendix for the proof.

Theorem 3.5. _The overall running time of the algorithm is_ \(O(malog\sigma_{max})\)

## 4 \(\exists\forall\forall\) Query and \(\exists\forall\exists\) Query

Given a temporal graph _G_=(_V,E_), we seek to find solutions to the \(\exists,\forall,\forall\) query:

Suppose _u_ solves the query. Then, for \(\tau_1\%\) of _u_’s neighbors _v_, _G_ contains at least one temporal edge _e_=(_u,v,t_), which solves the "\(\exists\exists\forall\)" query, when its threshold is set to \(\tau_2\). This observation leads to the following, very simple algorithm:

(1) First, solve for the \(\exists\exists\forall_{\tau_2}\) query . Let _L_ denote the set of solutions to this query.

(2) For every vertex \(v\in V(G)\), create a dictionary _L<sub>v</sub>_, indexed by the vertices in _N(v_).

(3) For every \(e=(u,v,t)\in L\), if _L<sub>u</sub>[v_]=1, then proceed to the next edge in _L_. Otherwise, set _L<sub>u</sub>[v_]=1.

(4) Finally, compute \(\sum_{v\in N(u)}L_u[v]\).

(5) Finally, for every \(v\in N(u)\), if \(\sum_{v\in N(u)}L_u[v]\ge\tau_1|N(u)|\), then include _u_ in the solution set.

The algorithm for the \(\exists\forall\exists\) is essentially the same, except for the lines (1) and (5). In particular, in line (1), instead of enumerating solutions to the \(\exists\exists\forall\) query for a threshold value equal to \(\tau_2\), the algorithm enumerates edges _e_ which satisfy in-count[_e_] + out- count[_e_] ≥ 1. The additional change needed is to update line (5)<tbc>

<tbc>of the algorithm by replacing \(\tau_1\) with \(\tau\), since there is only one threshold.

[7,16] [7,10] [6,13] [12,16] [7,8] [9,10] [12,14] [15,16] [8,10] [6,13], L2 = {[8,14]]

[7,16] [7,10] [6,13] [12,16] [7,8] [9,10] [12,14] [15,16] [8,10] [6,13], L2 = {[8,14]]

[7,16] [7,10] [6,13] [12,16] [7,8] [9,10] [12,14] [15,16] [8,10] [6,13], L2 = {[8,14]]

**(a) Phase 1: Insert the intervals into the segment tree, update suitable colors but donot update the counters**

**(b) Phase 2: Suppose we rein- sert the intervals of** _L_<sub>1</sub> **in the same order. During the inser- tion of** [8,10]**, we come across the grey node containing the seg- ment** [7,10]**. Hence we recolor the segment** [9,10]**, which is sup- posed to contain** [8,10] **to white. On the contrary, since none of the nodes on the path leading up to segment** [7,10] **were grey, we retain its color during the inser- tion of** [6,13]**.**

**(c) Update the counters of grey nodes only.**

**Figure 4: Insertion into Segment Trees, different phases**

