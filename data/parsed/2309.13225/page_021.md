Then, from \(u_2^*\), since \((u_2^*,v_3^*,v_3)\circ P_{v_3,v}\subset G_{\ell(u_2),u_2^*}\), **Dijkstra** computes,

\(\hat{\delta}_{\ell(u_2)}(u_2^*,v)\le\hat{\delta}_{\ell(v_3)}(u_2^*,v_3^*)+1+\delta(v_3,v)\le\delta(u_2,v_3)+3+\delta(v_3,v)\le\delta(u_2,v)+3\)

Finally, in the _k_-th iteration \((v,u_2^*,u_2,u)\subset G_{k,v}\) so **Dijkstra** finds a path of length at most \(\delta(u,v)+4\).

**Case 2.3.2:** \(\ell(P)=1\) **and** \(min(\ell(u),\ell(v))\le k-1\) Recall that _P_=(_u,u_<sub>2</sub>_,u_<sub>3</sub>_,v_<sub>3</sub>_,v_<sub>2</sub>_,v_). For \(\delta(u,v)=4\), note that _u_<sub>3</sub>=_v_<sub>3</sub>.

This case is handled by Phase 2.1. Without loss of generality, assume \(deg(u)\ge deg(v)\) so that \(deg(u)\ge s_{k-1}\). Since \(\ell(P)=1\), there is some vertex _w_ such that \(deg(w)\ge s_1\). Then, let \(w^*=r(w,D_1)\in D_1\) and \(u^*=r(u,D_{k-1})\in D_{k-1}\). Since \(P\subset G_x\),<tbc>

\(B(w^*,u^*)=\hat{\delta}_{s_1}(w^*,u^*)\le\delta(w,u)+2\le C+2\)<br>
\(A(w^*,v)=\hat{\delta}_{s_1}(w^*,v)\le\delta(w,v)+1\le C+1\)

<tbc>Therefore, since both entries are finite, we obtain in the (min,+) product an estimate at most,<tbc>

\(\hat{\delta}(u^*,v)\le\delta(w,u)+\delta(w,v)+3\le\delta(u,v)+3\)

<tbc>Then, in Phase 2.3, when we executing **Dijkstra** from _G<sub>k,v</sub>_, we take the edge (_v,u_<sup>∗</sup>) and (_u_<sup>∗</sup>_,u_) to find,

\(\hat{\delta}(v,u)\le\hat{\delta}(u^*,v)+1\le\delta(u,v)+4\le 2\delta(u,v)\)

**Case 2.3.3:** \(\ell(P)\ge 2\) **and** \(\ell(u_2)=\ell(v_2)=2\) Recall that _P_=(_u,u_<sub>2</sub>_,u_<sub>3</sub>_,v_<sub>3</sub>_,v_<sub>2</sub>_,v_). For \(\delta(u,v)=4\), note that _u_<sub>3</sub>=_v_<sub>3</sub>.

We handle this special case by noting that the number of distinct levels in the path _P_ is small. Without loss of generality, suppose \(\ell(v)\le\ell(u)\). Then, after the 2nd iteration,<tbc>

\(\hat{\delta}_2(u_2^*,v)\le\delta(u_2,v)+1\)

<tbc>as \(P\subset E_2\) and \(E_2\cup E^*\subset G_{2,u_2^*}\). Then, after the \(\ell(v)\)-th iteration, we take the path \((v^*,u_2^*,u_2,u)\) to obtain,

\(\hat{\delta}_{\ell(v)}(v^*,u)\le\hat{\delta}_2(v^*,u_2^*)+2\le\delta(u_2,v)+4\le\delta(u,v)+3\)

In the final iteration, we take the path (_v,u_<sup>∗</sup>_,u_) to obtain a +4 approximation.

**Case 2.3.4:** \(\ell(P)\ge 2\) **and** \(min(\ell(u_2),\ell(v_2))=2,max(\ell(u_2),\ell(v_2))\ge 3\) Recall that _P_=(_u,u_<sub>2</sub>_,u_<sub>3</sub>_,v_<sub>3</sub>_,v_<sub>2</sub>_,v_). For \(\delta(u,v)=4\), note that _u_<sub>3</sub>=_v_<sub>3</sub>.

Without loss of generality, assume \(\ell(u_2)=2\) and \(\ell(v_2)\ge 3\). If \(\ell(v)\le\ell(u)\), then we can proceed in the above case to obtain a +4 approximation. Thus, assume \(\ell(u)<\ell(v)\). We can now break our analysis into two sub-cases. In the remaining cases, we use the Depth 3 BFS search from Line 31 to ensure correctness.

Suppose \(\ell(v_2)\le\ell(u)<\ell(v)\). This case is illustrated in Figure 4a. Since \(\ell(v_2)\ge 3\), we have deg(_v_<sub>2</sub>)_\<s_<sub>2</sub>. Then, **BFS**(_G_<sub>2</sub>_,v_<sub>2</sub>,3) finds _u_<sub>2</sub> so that \(\hat{\delta}(v_2,u_2)=\delta(v_2,u_2)=3\). Then, denote \(v_2^*=r(v_2,D_{\ell(v_2)})\). After Line 36 since \(v_2\in q(v_2^*,D_{\ell(v_2)})\), we obtain \(\hat{\delta}_{\ell(v_2)}(v_2^*,u^*)\le\delta(v_2^*,u)+1\) via the path \((v_2^*,u_2,u,u^*)\). Then in the \(\ell(u)\)-th iteration, since \(\ell(u)<\ell(v)\), we execute **Dijkstra** from _u_<sup>∗</sup> and use the path \((u^*,v_2^*,v_2,v)\) to find \(\hat{\delta}_{\ell(u)}(u^*,v)\le\delta(u,v)+3\). Then, executing **Dijkstra** from _v_ in the _k_-th iteration, we take the path (_v,u_<sup>∗</sup>_,u_) and find an estimate, \(\hat{\delta}(u,v)\le\delta(u,v)+4\).

