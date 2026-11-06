<tbc>insertion operation can largely reuse techniques from incremental construction. Nevertheless, efficient updates for DVQ indices remain challenging. In particular, designing an efficient deletion repair strategy that preserves high index quality remains challenging.

**Limitations.** Based on the analysis in Section 2.2 and 2.3, existing Pareto-frontier-based DVQ indices suffer from inefficient index construction and substantial update overhead.

## 3 OVERVIEW

To overcome the above limitations, we design ACTIVE , as shown in Figure 3. To accelerate index construction, 1) we introduce an _angle-constrained active range computation_ (§4) strategy that avoids comparing each candidate neighbor against all retained neighbors by leveraging angular constraints. To accelerate index updates, 2) we propose a _connectivity-loss-driven adaptive repair_ (§5) strategy that locally repairs the approximate Pareto frontiers of affected nodes according to the severity of their connectivity degradation. Furthermore, we incorporate _asynchronous reverse graph maintenance_ to efficiently locate the affected nodes (§5.2).

<u>_Index Construction_</u>. ACTIVE employs an incremental construction strategy for each object in the dataset. Specifically, when constructing the out-neighbors of node _v_, the candidate set C is obtained by performing greedy Pareto frontier search over the current index. Subsequently, ACTIVE computes the active ranges of nodes in C using the proposed ACAR and selects the top-_R_ unpruned neighbors in lower layers of Pareto-frontiers as the final out-neighbors _N_<sub>out</sub>(_v_). Finally, for each \(v'\in N_\mathrm{out}(v)\), a reverse edge \((v',v)\) is added to guarantee reachability of _v_ during subsequent searches.

<u>_Index Update_</u>. For insertion, ACTIVE adopts the incremental construction approach to add new nodes into the graph index. For deletion, ACTIVE first leverages reverse graph topology to quickly locate the affected nodes. Then, ACTIVE adaptively repairs the affected nodes with three methods, namely historical-Pareto-frontier repair, affected-layer repair, and multi-layer repair, according to the severity of connectivity degradation for each affected node. Finally, ACTIVE computes the active ranges of the candidate neighbors for each affected node and selects the resulting final neighbors.

<u>_Dual-Vector Query_</u>. For a given dual-vector query _q_ and a query preference \(\alpha\), ACTIVE performs the greedy search based on the distance function (i.e., Eq.1) to obtain the top-_k_ approximate nearest neighbors. Specifically, ACTIVE maintains a candidate queue _Q<sub>c</sub>_ and a result queue _Q<sub>r</sub>_, where _Q<sub>c</sub>_ contains the visited but not expanded nodes while _Q<sub>r</sub>_ contains the expanded nodes, both ordered by their distances to the query. At each iteration, the<tbc>

<tbc>first not expanded node \(Q_c^\mathrm{t}\) in _Q<sub>c</sub>_ is selected for expansion, i.e., its out-neighbors whose active ranges contain \(\alpha\) are inserted into _Q<sub>c</sub>_. The expanded node is then inserted into _Q<sub>r</sub>_. During the search, |_Q<sub>r</sub>_| is bounded by _ef_search. The search terminates when \(\mathrm{Dist}(q,Q_c^\mathrm{t})>\mathrm{Dist}(q,Q_r^\mathrm{b})\), where\(Q_r^\mathrm{b}\) is the last node in _Q<sub>r</sub>_.

## 4 ANGLE-CONSTRAINED ACTIVE RANGE COMPUTATION

The workflow reveals that active range (AR) computation is invoked during both index construction and updates. This additional overhead substantially degrades both construction and update efficiency. To reduce this cost, we exploit the visited characteristics of Pareto- frontier-based neighbors and introduce an angle-constrained AR computation algorithm that improves computational efficiency.

### 4.1 Pareto Angle

The existing AR computation algorithm \[61\] computes the active ranges of the candidate set C of a node in a nested-loop manner. The **forward traversal order** of C follows a **two-level sorting scheme**: nodes are first ordered by the layer of the Pareto frontiers in ascending order and then sorted within each layer _PF_ by their distance to _v_ along a given dimension (e.g., \(\delta_x(v,\cdot)\)). Specifically, when processing node _v_, DEG sequentially traverses its out-neighbors (_a,b,c,d,e,f,..._) to compute their active ranges, following a two- level order: from lower to higher Pareto-frontier layers (i.e., layer 1 to _l_), and within each layer in ascending order of \(\delta_x(v,\cdot)\), i.e., from node _a_ to _e_ as illustrated in Figure 4. When traversing node _f_, DEG compares it against all previously retained nodes, i.e., _a-e_. However, this strategy performs redundant comparisons for each candidate neighbor. For _f_, it is unnecessary to compare _f_ with _e_, since _f_ is close to the \(\delta_y(v,\cdot)\) axis while _e_ lies closer to the \(\delta_x(v,\cdot)\) axis, making it highly unlikely that they will be simultaneously retrieved during query processing. Before introducing our AC computation method, we first introduce Pareto Angle.

Definition 1 (Pareto Angle (\(\phi\))). _Given a node v and its out- neighbor c, the Pareto angle_ \(\phi(v,c)\) _is defined in the 2D space induced by_ \((\delta_x(v,c),\delta_y(v,c))\)_. We define_

\(\phi(v,c)=\mathrm{arccos}\left(\frac{(\delta_x(v,c),\delta_y(v,c))\cdot(0,1)}{\sqrt{\delta_x(v,c)^2+\delta_y(v,c)^2}}\right),\) (2)

_where_ \(\phi(v,c)\) _denotes the angle between the vector_ \(\left(\delta_x(v,c),\delta_y(v,c)\right)\) _and the positive_ \(\delta_y(v,\cdot)\)_-axis. The value of_ \(\phi(v,c)\) _lies in_ \([0,\pi/2]\).

**Observation.** We construct Pareto-frontier-based indexes on three real-world datasets, OI, HM, and CM (details in  1), with all edges assigned an active range of \[0,1\]. We perform a search under query \(\alpha=0.1\) and obtain the result queue _Q<sub>r</sub>_ for each query, which contains the _ef<sub>search</sub>_ closest retrieved nodes. We further compute the Pareto angle \(\phi(v,r)\) for each retrieved node \(r\in Q_r\), where _v_ is<tbc>

Query
Construct/Insert
Delete
Pareto Frontier Search
Greedy
$5 CA-Repair
Search
$4 Angle-Constrained AR Computation
Res
Accelerate
Graph Topology
Reverse Topo.
Active Ranges
Distance Pair
[0.3,0.7]
0.1
0.9
[0.1,0.4]
0.6
0.5
$5.2 Async Background Maintenance

8y (v, )
processing
a
f
compare retained pruned
b
h
i
layer2
d
e
layer1
8x (v, )

1.0
OI
0.8
HM
0.6
CM
0.4
Norm. Frequency
0.2
0.0
0.0
0.2
0.4
0.6
0.8
1.0
cos(Φ)

**Figure 3: Workflow of ACTIVE .**

**Figure 4: Illustration of the existing AR computation algorithm \[61\].**

**Figure 5: Distribution of retrieved nodes across different Pareto angles** \(\phi\) **under** \(\alpha=0.1\).

