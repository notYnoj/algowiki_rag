where we have used |_L<sub>B</sub>(P<sub>w,x</sub>_)|_\>|L<sub>B</sub>(P<sub>y,w</sub>_)| as \(\ell(y)\in L_B(P_{w,x})\backslash L_B(P_{y,w})\). Then, in the _k_-th iteration, let _w_ be the closest vertex to _v_ such that \(\mathrm{deg}(w)\ge s_{k-1}\) so that,

\(\hat{\delta}(u,v)\le\hat{\delta}_{k-1}(u,w^*)+1+\delta(w,v)\le\delta(u,v)+2|L_B(P_{w,u})|\le\delta(u,v)+\beta\)

as \(L_B(P_{w,u})=\{k_0+3,\dots,k-2\}\cup\{\mathrm{min}(\ell(u_{\beta/2+1}),\ell(v_{\beta/2+1}))\}\) has size \(\frac{\beta}{2}\) .

To conclude, if _P_ has length less than \(\beta\), then \(P\subset E_{k_0+3}\), so we obtain a \(\beta\) approximation by Lemma A.3.

Finally, we claim that all the estimates produced by Algorithm 15 are feasible.

**Lemma E.9.** _Suppose error event E does not occur. Then, Algorithm 15 obtains an approximation such that_ \(\delta(u,v)\le\hat{\delta}(u,v)\) _for all_ \(u,v\in V\) .

_Proof._ We analyze each instance where the distance estimates are updated. In Phase 0, we initialize the distance estimates to the adjacency matrix. In Phase 1, we compute length 2 paths in a sub-graph \(G_{k_0+1}\subset G\). Next, the distance estimates are updated in Phase 2 in computing \(\text{\textbf{Dijkstra}}(G_{j,w},w,\hat{\delta})\) for all \(w\in D_j\). Note that this is identical to Algorithm **DenseAPASP**, and produces feasible distance estimates.

Line 36 does not violate feasibility as if \(u\in q(w,D_j)\) then \((u,w)\in E\) so that,

\(\hat{\delta}(w,v)\ge 1+\hat{\delta}(u,v)\ge 1+\delta(u,v)\ge\delta(w,v)\)

by the triangle inequality, where we have also used that the previous estimates were feasible.

Finally, since \(p(u,D_i)\in N(u,r_i)\) and \(C(u,i)\subset N(u,r_i)\), the final distance estimates are feasible as for any \(z\in N(u,r_i)\), the updated distance estimate,

\(\hat{\delta}(u,v)=r_i+\hat{\delta}(z,v)\ge r_i+\delta(z,v)\ge\delta(u,v)\)

where in the first inequality we used that the previous estimates are feasible and in the second we used the triangle inequality.

**Proof of Theorem E.1**

To prove the correctness of Algorithm 15, it suffices to prove Lemma E.5. Indeed, whenever _E_ occurs, we compute an exact **APSP** solution, which is obviously correct. If _E_ does not occur, Lemma E.9 guarantees that each estimate is feasible, and is produced by some path in _G_.

_Proof._ Let _u,v_ be a pair of vertices with shortest path _P_ length at most \(\beta+1\). We proceed by case analysis.

**Case 1:** \(P\subset E_{k_0+1}\) Suppose the assumptions of Lemma E.8 are not met, otherwise we obtain an accurate approximation. That is, for some _i_, \(\ell(u_{r_i})\le i+1\). In particular, _u_<sup>∗</sup>=_r(u,D_<sub>_i_+1</sub>) must be in \(N(u,r_i)\cap D_{i+1}\). Then, if \(|N(u,r_i)\cap D_{i+1}|\le 12s_{k-1}\mathrm{log}n\), we obtain a correct estimate by Lemma E.7. Otherwise, since _E(u,i_) does not occur, \(|N(u,i)|\ge s_i\), and we obtain a correct estimate by Lemma E.6.

**Case 2:** \(P\unknown\subset E_{k_0+1}\) We begin with the special case \(\beta=4\), generalizing to \(\beta\ge 6\) later.

