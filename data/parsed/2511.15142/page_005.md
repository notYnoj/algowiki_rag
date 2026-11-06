## 1.1.4 Efficient algorithms for Classical Combinatorial Families

While our general results provide broad query bounds, achieving computational efficiency for classic combinatorial problems often requires tailored approaches. We now turn our focus to several such problems, and show that despite the diversity in these optimization tasks, they admit very efficient algorithms using only comparison queries.

**Graph Cuts.** For the motivating problem of finding min-cuts in (unweighted) simple graphs, we extend the work of \[RSW18\] from the more informative _value oracle_ model and match it in the _comparison oracle_ model:

**Theorem 1.6** (Minimum cut)**.** _There is a randomized algorithm that computes the exact minimum cut of a simple graph G with high probability using_ \(\widetilde{O}(|V|)\) _cut comparison queries and_ \(\widetilde{O}(|V|^2)\) _time._

In addition to finding the minimum cut, we show how to recover the entire edge set of _G deterministically_ using cut comparison queries, except for some degenerate cases, when the task is provably impossible.

**Theorem 1.7** (Graph recovery)**.** _A simple unweighted graph_ \(G\notin\{K_2,\bar{K}_2,K_3,\bar{K}_3\}\) _can be recovered using_ \(O(\mathrm{min}\{(|E|+|V|)\mathrm{log}|V|,|V|^2\})\) _cut comparison queries and in_ \(\widetilde{O}(|V|^2)\) _time._

Finally, we show that cut comparisons suffice to construct sparsifiers for a broad class of graph problems called _heavy subgraph_ problems (which include _densest subgraph_ and _max-cut_) by combining our edge-sampling techniques with the results of \[EHW15\]; see Section 5.4 for details.

The min-cut problem illustrates a _qualitative difference between the value oracle and comparison oracle settings_: in the former, we can evaluate the expression \(1/2(w(\partial u)+w(\partial v)-w(\partial\{u,v\}))\) to learn whether edge (_u,v_) exists (and what its weight is, if the graphs are weighted). In contrast, reconstructing a graph is not straightforward with cut comparisons. (E.g., all non-trivial cuts in _K_<sub>3</sub> have the same value, and the same holds for its complement graph \(\bar{K}_3\), so we cannot distinguish them by comparison queries alone. Moreover, _weighted_ graphs cannot be recovered at all using comparisons, even up to scaling (see Section D.4.2)! Given this, Theorem 1.7 comes as a surprise.

The main idea behind both results is the following: for a vertex _v_ and set \(S\unknown v\), comparing \(w(\partial(S+v))\) and \(w(\partial(S))\) tells us whether more than half of _v_’s incident edges go into _S_. We build on this observation to identify all edges incident to _v_: for a sequence of nested sets \(\emptyset\neq S_0\subseteq S_1\subseteq\dots\subseteq S_{n-1}\neq V\backslash\{v\}\), we ask the above question for each _S<sub>i</sub>_ to find a "tipping point"--a query where the sign of \(w(\partial(S+v))-w(\partial(S))\) changes--whereupon we find an edge. We then refine the process to make edge recovery more efficient, and to perform efficient sampling on _G_ and get a randomized algorithm using only \(\widetilde{O}(n)\) comparison queries; see Section 5.

**Weighted Min-Cut.** These techniques do not extend to weighted graphs. E.g., there are many weighted graphs which cannot be identified using just comparison queries. (E.g., adding tiny-weight edges to a graph changes the graph but not the comparisons.) Also, while our techniques can give _non-adaptive_ algorithms using poly(_n_) comparisons for min-cut/graph recovery in simple graphs, any non-adaptive algorithm _for the weighted case_ must have exponential query complexity in the worst case. (See Section D.4 for a discussion of this and other bottlenecks.) That said, we give the following result for the case where the graph has a small number of distinct vertex degrees. (See Section D.3 for a proof.)

**Theorem 1.8** (Weighted minimum cut)**.** _For a graph G_=(_V,E_) _with unknown integer edge weights in the range_ \[0_,B_\]_, the minimum cut can be found using_ (_nB_)<sup>_O(r_<sup>2</sup>log_B_)</sup> _queries and time, where_<tbc>

