Now, in the 5-th iteration in Phase 2, when we execute Dijkstra from _u_, we have an edge (_u,y_<sup>∗</sup>) with weight at most \(\delta(u,y)+3\), an edge \((y^*,y)\in E\) and the remaining edges in _E_<sub>5</sub>=_E<sub>k</sub>_, so that,

\(\hat{\delta}(u,v)\le\hat{\delta}_{i^*}(u,y^*)+1+\delta(y,v)\le\delta(u,y)+\delta(y,v)+4\le\delta(u,v)+4\)

**General Case:** \(\beta\ge 6\)

We now present the proof of Theorem 5.6.

_Proof._ (Correctness) Let \(u,v\in V\) be a pair of vertices and _P_ be a shortest path between _u,v_. Let \(\mathrm{deg}(P)=\mathrm{max}_{v\in P}\mathrm{deg}(v)\) be the maximum degree of any vertex on _P_.

Note by the definition of \(k\leftarrow\frac{3\beta-2}{2}\) and \(\beta\) is an even integer,

\(2\left(\lfloor k/3\rfloor+1\right)=2\left(\left\lfloor\frac{\beta}{2}-\frac{1}{3}\right\rfloor+1\right)\le\beta\)

By Lemma 5.10, we only need to show \(\hat{\delta}(u,v)\le\delta(u,v)+2(\lfloor k/3\rfloor+1)\).

Recall that \(V_s=\{v\in V\text{s.t.}\mathrm{deg}(v)\ge s\}\) from Definition 2.3.

**Case 1:** deg(_P)\<s_<sub>_k_<sub>0</sub></sub> In this case, we have \(P\subset E_{k_0+1}\), and we may follow the proof of **SparseAPASP** by Dor, Halperin, and Zwick \[DHZ00\]. By assumption \(L(P,k)\subset\{k_0+1,k_0+2,\dots,k-1\}\) so that \(|L(P,k)|\le\lfloor k/3\rfloor+1\). From Lemma A.3, it immediately follows that \(\hat{\delta}(u,v)\le 2(\lfloor k/3\rfloor+1)\).

**Case 2:** \(\mathrm{deg}(P)\ge s_{k_0}\) By assumption, there is a vertex \(w\in P\) with \(\mathrm{deg}(w)\ge s_{k_0+3}\). Then, with Lemma 5.11, we have that for all \(x\in P\),

\(\hat{\delta}_{k_0+3}(w^*,x)\le\delta(w,x)+5\)

Then, following the same argument as the inductive step of Lemma A.2, consider any vertex \(w\in P\) such that \(\ell(w)\ge j\) for _j\>k_<sub>0</sub>+3. We claim the following for all _j_,

\(\hat{\delta}_j(w^*,x)\le\delta(w,x)+2(j-(k_0+1))+1\)

where above we have shown the base case for _j=k_<sub>0</sub>+3. We now proceed by induction for _j\>k_<sub>0</sub>+3. Consider an execution of **Dijkstra** from _w_<sup>∗</sup> in _G<sub>j,w</sub>_. For any vertex \(x\in P\), let _y_ be the last vertex on the sub-path _P<sub>w,x</sub>_ with \(\ell(y)\le j-1\).

If no such vertex exists, then \(P_{w,x}\subset E_j\) and we compute an exact distance from _w_<sup>∗</sup> so that \(\hat{\delta}(w^*,x)\le\delta(w,x)+1\).

In particular, \(\mathrm{deg}(y)\ge s_{j-1}\) so let _y_<sup>∗</sup>=_r(y,D_<sub>_j_-1</sub>). We take the edges (_w_<sup>∗</sup>_,y_<sup>∗</sup>), \((y^*,y)\in E^*\), and the remaining edges in _E<sub>j</sub>_. By induction, we have,

\(\hat{\delta}_j(w^*,x)\le\hat{\delta}_{j-1}(w^*,y^*)+1+\delta(y,x)\)<br>
\(\le\delta(w,y)+2((j-1)-(k_0+1))+3+\delta(y,x)\)<br>
\(\le\delta(w,x)+2(j-(k_0+1))+1\)

Then, on the final iteration, let _w_ be the closest vertex to _v_ on _P_ such that \(\mathrm{deg}(w)\ge s_{k-1}\). From _u_, we take the edge (_u,w_<sup>∗</sup>), followed by \((w,w^*)\in E^*\) and the remaining path in _E<sub>k</sub>_, so that,

\(\hat{\delta}(u,v)\le\hat{\delta}_{k-1}(u,w^*)+1+\delta(w,v)\)

