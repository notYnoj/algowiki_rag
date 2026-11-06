balancing the thresholds so that each **BFS** search can be computed efficiently. We repeat for all _t_ large enough such that the dominating set _C<sub>t</sub>_ is small.

Phase 2 handles paths with low degree vertices. Line 24 uses **Decompose** on the remaining sparse graph into _k_=7 degree levels specified in Line 23.

Phase 2.1, computes **BFS** from each vertex in _D_<sub>1</sub> (Lines 26-27) and use a bounded (min,+) product to find approximate distances between each pair of vertices \(V\times D_{k-1}\) that goes through a vertex in _D_<sub>1</sub> in Line 15 of **DominatingSetAPASP**.

In Phase 2.2, a depth 2 **BFS** is computed from each vertex in _G<sub>x</sub>_ (Line 30), as well as depth 3 **BFS** from each vertex of degree at most _s_<sub>2</sub> in the graph _G_<sub>2</sub>=(_V,E_<sub>2</sub>) (Line 31).

**Algorithm 3 2ApproxAPSP**(_G_)

**Input :** Unweighted, undirected Graph _G_=(_V,E_) with _n_ vertices<br>
**Output:** Distance estimate \(\hat{\delta}:U\times V\rightarrow\mathbb{Z}\) such that \(\delta(u,v)\le\hat{\delta}(u,v)\le 2\delta(u,v)\) for all \(u,v\in V\)<br>
Fix parameters \(x\leftarrow 0.45509125\) and \(C\leftarrow 12\)<br>
\(\hat{\delta}(u,v)\leftarrow\left\{\begin{array}{ c c }
1 & (u,v)\in E \\
\infty & \text{o/w}
\end{array}\right.\)<br>
Phase 1: Compute +2 Approximate Distances of High Max Degree Paths<br>
for \(t=2^j\) for \(0\le j\le\lceil(1-x)\mathrm{log}n\rceil\) do<br>
   \(C_t\leftarrow\text{Dominate}\left(G,\frac{n}{t}\right)\) and \(G_t=\left(V,E_\frac{2n}{t}\right)\)<br>
   \(\hat{\delta}\leftarrow\mathrm{min}(\hat{\delta},\text{DominatingSetAPASP}(G_t,V,V,C_t,C+1))\)<br>
Phase 2: Compute Approximate Distances of Low Degree Paths<br>
   \(s_i\leftarrow n^\frac{k-i}{k}x\) for all \(1\le i\le k-1=\frac{C}{2}\)<br>
   (_D_<sub>1</sub>,_D_<sub>2</sub>_,...,D<sub>k</sub>),(E_<sub>1</sub>,_E_<sub>2</sub>_,...,E<sub>k</sub>),E_<sup>∗</sup> \(\leftarrow\text{Decompose}(G_x,(s_1,s_2,\dots,s_{k-1}))\) where \(G_x\leftarrow(V,E_{n^x})\)<br>
Phase 2.1: Computing Approximate Distances of Paths with Vertex in V<sub>s<sub>1</sub></sub><br>
   \(G_{s_1}\leftarrow(V,E_{n^x}\cup E^*)\)<br>
   \(\hat{\delta}\leftarrow\mathrm{min}(\hat{\delta},\text{DominatingSetAPASP}(G_{s_1},V,D_{k-1},D_1,C+2))\)<br>
Phase 2.2: Compute Approximate Distances for \(\delta(u,v)\le 5\)<br>
for \(v\in V\) do<br>
   \(M_{v,2}\leftarrow\text{BFS}(G_x,v,2)\)<br>
   if \(\mathrm{deg}(u)\le s_2\) then \(M_{u,3}\leftarrow\text{BFS}(G_2,u,3)\) where G<sub>2</sub>=(V,E<sub>2</sub>);<br>
   \(\hat{\delta}(v,u)\leftarrow\mathrm{min}(\hat{\delta}(u,v),M_{v,2}(u),M_{v,3}(u))\)<br>
Phase 2.3: Compute Approximate Distances of Low Degree Paths<br>
for \(1\le i\le k\) do<br>
   for \(w\in D_i\) do<br>
   \(\hat{\delta}(w,v)\leftarrow\mathrm{min}(\hat{\delta}(w,v),\mathrm{min}_{u\in q(w,D_i)}1+\hat{\delta}(u,v))\) for all \(v\in V\)<br>
   \(\hat{\delta}\leftarrow\text{Dijkstra}(G_{i,w},w,\hat{\delta})\) where \(G_{i,w}\leftarrow(V,E_i\cup(w\times V)\cup E^*)\)<br>
Phase 3: Compute Approximate Distances of Long Paths<br>
\(\hat{\delta}\leftarrow\mathrm{min}(\hat{\delta},\text{BoundedAdditiveAPASP}(G,6,C),\text{DenseAPASP}(G,C))\)

Phase 2.3 (Lines 26-29), performs **Dijkstra** from each vertex \(w\in D_i\) on the graph \((V,E_i\cup E^*\cup(w\times V))\) with the current estimates \(\hat{\delta}\) equipped as edge weights. Before **Dijkstra** is executed, the distances from a vertex \(w\in D_i\) in the dominating set is updated by examining distances from its constituency (see Definition 2.2).

Finally, Line 31 handles paths of distance between 6 and 12 with a call to **BoundedAdditiveAPASP** and all paths of distance larger than 12 with a call to **DenseAPASP**.

