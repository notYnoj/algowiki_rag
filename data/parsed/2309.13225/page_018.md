<tbc>On the other hand deg(_u)\>_deg(_v_<sub>2</sub>). If deg(_u)\>s_<sub>2</sub>, we obtain a +2 approximation following the previous discussion of Case 2.3.3. Otherwise, if deg(_u)\<s_<sub>2</sub> then the depth 3 **BFS** from _u_ computes \(\hat{\delta}(u,v_3)=3\) and Line 36 updates \(\hat{\delta}(u^*,v_3)=1+\hat{\delta}(u,v_3)=4\). Since deg(_u)\>_deg(_v_<sub>2</sub>), \((u^*,v_3,v_2,v)\subset G_{\ell(u),u^*}\) so **Dijkstra** computes a distance estimate at most,

\(\hat{\delta}(u^*,v)\le\hat{\delta}(u^*,v_3)+3\le 6\)

Then, as \((v,u^*,u)\subset G_{7,u}\), **Dijkstra** computes a distance estimate at most 7, which is a +2 additive approximation. See Figure 4b for an illustration.

In the full proof we give a detailed argument on all possible variations of length 5 paths as well as the modifications necessary to compute a +4 additive approximation on length 4 paths.

## Time Complexity

The time-complexity to compute **boundedMinPlus** to handle paths with at least one vertex in _V_<sub>0</sub> is \(\tilde{O}(\omega(1,1-x,1))\). This computation dominates the **boundedMinPlus** computation in Case 2.3.2 Figure 3 (see Proposition C.3). The time complexity to handle paths with low degree vertices for paths of length at most 5 is

\(\tilde{O}\left(n^{1+2x}+n^{1+\frac{3k-4}{k}x}+n^{2+\frac{x}{k}}\right)\)

where the first term is from running depth 2 **BFS**, the second term is from running depth 3 **BFS** from vertices with degree at most _s_<sub>2</sub>, and the last term is from running **Dijkstra**. If we balance these terms, we get we choose _x_=0.4414248 and _k_=7 to obtain the time complexity \(\tilde{O}(n^{2.07203166})\). The non-dominating terms include time to run **boundedAdaptiveAPASP**on paths of length \[6, 12\] which requires \(\tilde{O}(n^{2.0638})\) by Corollary 5.14 and **DenseAPASP**(G,12) that requires time \(\tilde{O}(n^{35/17})=\tilde{O}(n^{2.0589})\) by Lemma 3.2.

## Algorithm

Algorithm 3 computes a deterministic (2,0)-approximation of APSP on unweighted graphs. Phase 1 (Lines 19-21), uses **boundedMinPlus**on matrix _M<sub>t</sub>_ to estimate distances for paths of length at most _C_ containing at least one vertex of degree \(\ge n^x\). To do so, Line 19 considers log_n_ degree thresholds, each of the form \(t=\frac{n}{2j}\). Within each threshold, a dominating set _C<sub>t</sub>_ is computed (Line 20) and a edge set _E_<sub>2_n/t_</sub> such that the degree of each vertex does not exceed \(\frac{2n}{t}\) . Line 12 of **dominatingSetAPASP** computes a **BFS** within the sub-graph _G<sub>t</sub>_=(_V,E_<sub>2_n/t_</sub>) from each node in the dominating set _C<sub>t</sub>_, keeping only distances up to _C_+1. Then, for each pair of vertices, _u,v_, a bounded (min,+) product is computed in Line 15 of **dominatingSetAPASP** to compute the shortest path between _u,v_ passing through a vertex \(w\in C_t\). We repeat this computation for all _t_,<tbc>

u*
v2
u
u2
u3
v3
v2
v

u*
u
u2
u3
v3
v2
v

(a) Depth 3 **BFS** search from _v_<sub>2</sub>.

(b) Depth 3 **BFS** search from _u_.

Figure 4: Case 2.3.4 and 2.3.5: We use depth 3 **BFS** in Line 31 to obtain more accurate distance estimates. Solid lines denote edges in _G_. Solid arrows denote depth 3 **BFS** executions. Dotted arrows denote edges \(w\times V\) used in executing **Dijkstra** on the graph _G<sub>j,w</sub>_.

