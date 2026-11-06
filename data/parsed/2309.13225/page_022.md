Finally, suppose \(\ell(u)<\ell(v_2)\). First, if \(\ell(u)=2=\ell(P)\), then from Lemma A.3 we have that after the second iteration \(\hat{\delta}_2(u^*,v)\le\delta(u,v)+1\) and obtain a +2 approximation in the _k_-th iteration via the path (_v,u_<sup>∗</sup>_,u_). We can therefore assume \(\ell(u)\ge 3\).

Then, we execute a Depth 3 **BFS** from _u_ as illustrated in Figure 4b so that after Line 31 we have _M_<sub>_u,_3</sub>(_v_<sub>3</sub>)=3 (for length 4 paths, we in fact obtain _M_<sub>_u,_3</sub>(_v_<sub>2</sub>)=3). In particular, after Line 36, \(\hat{\delta}(u^*,v_3)\le\delta(u,v_3)+1\) where \(u^*=r(u,D_{\ell(u)})\).

Since \(\ell(u)<\ell(v_2),\ell(v)\), in the \(\ell(u)\)-th iteration, we find _v_ from _u_<sup>∗</sup> via the path (_u_<sup>∗</sup>_,v_<sub>3</sub>_,v_<sub>2</sub>_,v_) so that \(\hat{\delta}_{\ell(u)}(u^*,v)\le\delta(u,v)+1\). Finally, in the _k_-th iteration, from _v_ we take the path (_v,u_<sup>∗</sup>_,u_) to find,

\(\hat{\delta}(u,v)\le\delta(u,v)+2\)

and obtain a +2 approximation.

## Case 2.3.5: \(\ell(P)\ge 2\) and \(min(\ell(u_2),\ell(v_2))\ge 3\)

Recall that _P_=(_u,u_<sub>2</sub>_,u_<sub>3</sub>_,v_<sub>3</sub>_,v_<sub>2</sub>_,v_). For \(\delta(u,v)=4\), note that _u_<sub>3</sub>=_v_<sub>3</sub>.

Without loss of generality, assume \(\ell(u_2)\le\ell(v_2)\). Since _u,u_<sub>2</sub>_,v_<sub>2</sub>_,v_ all have degree at most _s_<sub>2</sub>, we can freely afford Depth 3 **BFS** from any of these vertices in the graph _G_<sub>2</sub>.

Without loss of generality, suppose \(\ell(u)\le\ell(v)\). For length 4 paths, we have computed a \(\hat{\delta}(u,v_2)=3\) after Line 31 so that after \(\ell(u)\)-th iteration, \(\hat{\delta}(u^*,v)\le\delta(u,v)+1\) and we obtain a +2 approximation in the _k_-th iteration via the path (_v,u_<sup>∗</sup>_,u_). Similarly, if \(\ell(u)\le\ell(v_2)\), we obtain a +2 approximation for length 5 paths.

Thus, we have \(\ell(v_2)<\ell(u)\). Then, as in the above case, we compute a Depth 3 **BFS** from _v_<sub>2</sub> so that after the \(\ell(v_2)\)-th iteration, \(\hat{\delta}_{\ell(v_2)}(v_2^*,u)\le\delta(v_2,u)+1\). Then, after the \(\ell(u)\)-th iteration, \(\hat{\delta}_{\ell(u)}(u^*,v)\le\delta(u,v)+3\) and we obtain a +4 approximation in the _k_-th iteration.

## Case 2.4: \(\delta(u,v)=3\)

For length 3 paths, we prove that we find a +2 approximation. Denote the path _P_=(_u,u_<sub>2</sub>_,v_<sub>2</sub>_,v_).

We can assume that the maximum degree vertex of _P_ is either _u_<sub>2</sub>_,v_<sub>2</sub>. Otherwise, let _u_ be the endpoint of maximum degree. We compute \(\hat{\delta}_{\ell(u)}(u^*,v)\le\delta(u,v)+1\) and obtain a +2 approximation in the _k_-th iteration via path (_v,u_<sup>∗</sup>_,u_).

Suppose without loss of generality \(\ell(u)\le\ell(v)\). Then, _M_<sub>_u,_2</sub>(_v_<sub>2</sub>)=2 so that after Line 36,

\(\hat{\delta}(u^*,v_2)\le 3\)

where \(u^*=r(u,D_{\ell(u)})\). Executing **dijkstra** from _u_<sup>∗</sup>, we can take the path (_u_<sup>∗</sup>_,v_<sub>2</sub>_,v_) and obtain \(\hat{\delta}_{\ell(u)}(u^*,v)\le\delta(u,v)+1\). Then, in the _k_-th iteration, we take the path (_v,u_<sup>∗</sup>_,u_) and obtain a +2 approximation.

## Case 2.5: \(\delta(u,v)=2\)

For length 2 paths, we in fact find the exact distance. Since \(P\subset G_x\), in Line 30 we compute depth 2 **BFS** from each vertex, and therefore find \(\hat{\delta}(u,v)=\delta(u,v)=2\).

## Time Complexity

_Proof._ We analyze the time complexity of our algorithm. _x,C_ are parameters that will be optimized.

## Phase 1

Following the same arguments as Phase 1 of the randomized algorithm, we can bound the running time of Phase 1 as,<tbc>

\(\tilde{O}\left(n^{\omega(1,1-x,1)}\right)\)

