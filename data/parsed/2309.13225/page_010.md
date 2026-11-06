<tbc>in _D_ or is itself in _D_. _D_ is known as a dominating set. We compute exact distances from _D_, and then for each pair of vertices, we can take the minimum length path passing through a vertex in _D_. On paths with at least one high degree vertex, this gives a +2 approximation as a vertex in _D_ is adjacent to some vertex in the shortest path _P_. On the other hand, for each pair of vertices whose shortest path contains no high degree vertices, we can compute APSP in time _O(n_<sup>5/2</sup>) by computing **BFS** (or **Dijkstra**) from every vertex on the graph \(G'\subset G\) containing only edges adjacent to low degree vertices.

Dor, Halperin and Zwick extended this idea to consider three degree thresholds _s_<sub>0</sub>=_n_<sup>2/3</sup>_,s_<sub>1</sub>=_n_<sup>1/3</sup>_,s_<sub>2</sub>=0 \[DHZ00\]. These degree thresholds are used to compute the dominating sets \(D_0\subset D_1\subset D_2=V\) according to **Decompose** (Lemma 2.6) where _D<sub>i</sub>_ dominates \(V_i=\{v\in V\text{s.t.}deg(v)\ge s_i\}\) and \(E_i=\{(u,v)\in E\text{s.t.}min(deg(u),deg(v))<s_{i-1}\}\) for _i_=0,1,2 (take _s_<sub>-1</sub>=_n_+1). They use **Dijkstra**(instead of **BFS**) from all vertices at the lowest level, i.e., in _G_<sub>2</sub>=(_V,E_<sub>2</sub>), resulting in a running time of \(\tilde{O}\left(n^{2+1/3}\right)=\tilde{O}\left(n^{7/3}\right)\).

For a (2,0)-approximation, it is enough to have a (1,2)-approximation on paths of length up to 3. Using this crucial observation, Roditty was able to extend the decomposition to 4 levels, and then call a (1,4)-approximation algorithm of \[DHZ00\] for paths of length at least 4. This reduces the running time from \(\tilde{O}\left(n^{7/3}\right)\) to \(\tilde{O}\left(n^{2+1/4}\right)=\tilde{O}\left(n^{9/4}\right)\).

To improve the bound, we instead proceed as follows. We consider shortest paths of length \(\ge C\), and less than _C_ separately where _C_ is some threshold which we later set to _C_=22. We also consider another threshold \(x\in(0,1)\), and define \(V_0=\{v\text{s.t.}deg(v)\ge n^x\}\). We will set _x_ appropriately later.

## High Degree Vertices: Paths of length \(\le C\).

Consider first all shortest paths _P_ with at least one vertex from _V_<sub>0</sub> that is of degree \(\ge n^x\). Moreover, concentrate only on paths of length less than _C_=22. Decompose _G_ into (1-_x_)log_n_ levels with degree thresholds \(t_j=\frac{n}{2^j}\) for \(1\le j\le(1-x)logn\) and compute dominating sets _C<sub>j</sub>_ of size \(\tilde{O}(\frac{n}{t_j})\) and edge sets _F<sub>j</sub>_ of size _O(nt_<sub>_j_-1</sub>). Computing **BFS** on the subgraph (_V,F<sub>j</sub>_) from each vertex of _C<sub>j</sub>_ therefore altogether requires \(\tilde{O}(n^2)\) time. Moreover \(|\cup_jC_j|=\tilde{O}\left(n^{1-x}\right)\). For each pair of vertices, compute the estimate \(\hat{\delta}(u,v)=min_{w\in\cup_jC_j}\delta(w,u)+\delta(w,v)\) with a (min,+) product. Since, we concentrate on paths of length up to a constant _C_, we can compute the above efficiently with the **boundedMinPlus** algorithm (Theorem B.8). For the value _j_ such that \(P\subset F_j\) but \(P\unknown\subset F_{j+1}\), there is some vertex \(w\in P\) such that \(t_j\le deg(w)<t_{j-1}\) and \(w^*\in C_j\) is a neighbor of _w_. Thus, the computed estimate is a +2 approximation, which is also a (2,0)-approximation. Computation of the **boundedMinPlus** requires time \(\tilde{O}\left(\omega(1,1-x,1)\right)\).

## Paths of length \(\ge C\).

For paths of lengths at least _C_=22, we are allowed to obtain estimates with large additive errors, which can be computed efficiently using known results from \[DHZ00\]. We can choose any value of _C_ large enough so that executing the additive approximation of \[DHZ00\] does not affect the overall running time.

**Lemma 3.2.** _(\[DHZ00\]) Let_ \(\beta\ge 2\) _be even. Let G be an undirected, unweighted graph with n vertices and m edges. There is an algorithm computing a_ \(+\beta\)_-approximate APSP solution in time_

\(\tilde{O}(min(n^{2-\frac{2}{\beta+2}}m^\frac{2}{\beta+2},n^{2+\frac{2}{3\beta-2}}))\)

_Denote **SparseAPASP** the algorithm running in time_ \(\tilde{O}(n^{2-\frac{2}{\beta+2}}m^\frac{2}{\beta+2})\) _and **DenseAPASP** the algorithm running in time_ \(\tilde{O}(n^{2+\frac{2}{3\beta-2}})\).

Consider paths _P_ such that at least one vertex on _P_ has degree \(\ge n^x\). We run **DenseAPASP** with a running time of \(\tilde{O}\left(n^{2+2/(3C-2)}\right)=\tilde{O}\left(2.03125\right)\).

