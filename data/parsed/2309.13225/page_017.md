We can now assume that every vertex has degree _\<s_<sub>1</sub>. We now compute depth 3 **BFS** in _G_<sub>2</sub>=(_V,E_<sub>2</sub>) from every vertex with degree at most _s_<sub>2</sub>. One depth 3 **BFS** requires \(s_2s_1^2=n^\frac{3k-4}{k}x\) time (contrast to _n_<sup>3_x_</sup> if naively applying depth 3 **BFS** on the graph _G<sub>x</sub>_). The correctness depends on extensive case analysis.

In Case 2.3.3, suppose \(\mathrm{deg}(u_2),\mathrm{deg}(v_2)\ge s_2\). Suppose \(\mathrm{deg}(v)\ge\mathrm{deg}(u)\). From our earlier discussion, since \(P\subset E_2\), \(\hat{\delta}(u_2^*,v)\le\delta(u,v)+1\). Then, since the path \((v^*,u_2^*,u_2,u)\subset G_{\ell(v),v^*}\), **Dijkstra** computes an estimate,

\(\hat{\delta}(v^*,u)\le\hat{\delta}(v^*,u_2^*)+2\le\delta(u,v)+3\)

Then, as \((u,v^*,v)\subset G_{8,u}\), **Dijkstra** computes a +4 additive approximation.

In Case 2.3.4, suppose \(\mathrm{deg}(u_2)\ge s_2\) but deg(_v_<sub>2</sub>)_\<s_<sub>2</sub>. If \(\mathrm{deg}(v)\ge\mathrm{deg}(u)\), then we can proceed exactly as above, so assume deg(_u)\>_deg(_v_). The depth 3 **BFS** from _v_<sub>2</sub> computes \(\hat{\delta}(v_2,u_2)=3\) and Line 36 updates \(\hat{\delta}(v_2^*,u_2)=1+\hat{\delta}(v_2,u_2)=4\). If \(\mathrm{deg}(v_2)\ge\mathrm{deg}(u)\), then, the path \((v_2^*,u_2,u,u^*)\subset G_{\ell(v_2),v_2^*}\), **Dijkstra** computes a distance estimate at most,

\(\hat{\delta}(v_2^*,u^*)\le\hat{\delta}(v_2^*,u_2)+2\le 6\)

Since deg(_u)\>_deg(_v_), \((u^*,v_2^*,v_2,v)\subset G_{\ell(u),u^*}\), **Dijkstra** computes a distance estimate at most,

\(\hat{\delta}(u^*,v)\le\hat{\delta}(u^*,v_2^*)+2\le 8\)

Then, as \((v,u^*,u)\subset G_{7,u}\), **Dijkstra** computes a distance estimate at most 9, a +4 additive approximation. See Figure 4a for an illustration.

u2
*
*
u
u2
u3
v3
v2
v

u*
*
*
*
u
u2
u3
v3
v2
v

Figure 2: Case 2.3.1: \(\ell(u)=\ell(v)=k\). Solid lines denote edges and dotted lines represent paths. Black dashed arrows denote edges \(w\times V\) in _G<sub>j,w</sub>_.

Figure 3: Case 2.3.2: \(\mathrm{deg}(u)\ge s_6\) and deg(_v_<sub>3</sub>)_\>s_<sub>1</sub>. Solid lines denote edges in _G_. Blue dashed arrows denote distance estimates used in the (min,+) product. Black dashed arrows denote edges \(w\times V\) in _G<sub>j,w</sub>_.

