Note that we can also easily use Algorithm 6 in place of `DenseAPASP`, although this will not affect the asymptotic performance of our final algorithm.

**Proof of Theorem 3.3**

We start with the correctness proof, followed by a run time analysis.

**Correctness.**

_Proof._ Consider a vertex pair \(u,v\in V\times V\) . Let \(\delta(u,v)\) denote the length of a shortest path between _u,v_. From Lemma C.2, we have that \(\delta(u,v)\le\hat{\delta}(u,v)\) for all _u,v_. We therefore focus on proving \(\hat{\delta}(u,v)\le 2\delta(u,v)\) for all _u,v_. We can assume \(\delta(u,v)\ge 2\) since 1 edge paths can easily be found by examining the adjacency matrix.

**Case 1:** \(\mathrm{deg}(P)\ge n^x\) Suppose \(\delta(u,v)\ge C\). By the correctness of `DenseAPASP`, we have \(\hat{\delta}(u,v)\le\delta(u,v)+C\le 2\delta(u,v)\). Thus, in the following, assume \(\delta(u,v)\le C\)

The remaining proof is similar to Case 3 of the randomized algorithm.

**Case 2:** deg(_P)\<n<sup>x</sup>_ We now prove the correctness of Algorithm 3 on low-degree paths.

**Case 2.1:** \(\delta(u,v)\ge C\) Correctness immediately follows from `DenseAPASP`. In particular,

\(\hat{\delta}(u,v)\le\delta(u,v)+C\le 2\delta(u,v)\)

**Case 2.2:** \(6\le\delta(u,v)\le C\) Correctness immediately follow from `BoundedAdaptiveAPASP`. In particular,

\(\hat{\delta}(u,v)\le\delta(u,v)+6\le 2\delta(u,v)\)

**Case 2.3:** \(4\le\delta(u,v)\le 5\) Denote the path _P_=(_u,u_<sub>2</sub>_,u_<sub>3</sub>_,v_<sub>3</sub>_,v_<sub>2</sub>_,v_). Note that if \(\delta(u,v)=4\), we in fact have _u_<sub>3</sub>=_v_<sub>3</sub>.

Recall that for any vertex, we define the level of vertex _v_ as \(\ell(v)\) to be the index _i_ where \(s_i\le\mathrm{deg}(v)<s_{i-1}\). For any path _P_, define \(\ell(P)=\mathrm{min}_{v\in P}\ell(v)\) to be the minimum level of any vertex in _P_, or alternatively the level of the maximum degree vertex of _P_. Let \(\hat{\delta}_j\) denote the estimate after executing `Dijkstra` from all \(w\in D_j\). We now proceed by case analysis on the levels of the vertices comprising shortest path _P_.

**Case 2.3.1:** \(\ell(u)=\ell(v)=k\) We show a +4 additive error in this case. Without loss of generality, assume \(\ell(u_2)\le\ell(v_2)\). Then, for length 4 paths when _u_<sub>3</sub>=_v_<sub>3</sub>, we actually have \(P\subset E_{\ell(u_2)}\) so that after the execution of `Dijkstra` at the \(\ell(u_2)\) iteration, \(\hat{\delta}_{\ell(u_2)}(u_2^*,v)\le\delta(u_2,v)+1\) where \(u_2^*=r\left(u_2,D_{\ell(u_2)}\right)\). Then, in the _k_-th iteration, when we execute `Dijkstra` from _v_, we have access to the edges \((v,u_2^*),(u_2^*,u_2),(u_2,u)\) to find a path of length at most \(\delta(u,v)+2\).

Now, suppose we have a length 5 path so that \(u_3\neq v_3\). If \(P\notin E_{\ell(u_2)}\) then \(\ell(u_3),\ell(v_3)<\ell(u_2)\). Then, \(P\subset E_{\ell(v_3)}\) so that from \(v_3^*=r\left(v_3,D_{\ell(v_3)}\right)\) the path \((v_3^*,v_3)\circ P_{v_3,u_2}\circ(u_2,u_2^*)\subset G_{\ell(v_3),v_3^*}\) and `Dijkstra` computes an estimate,

\(\hat{\delta}_{\ell(v_3)}(v_3^*,u_2^*)\le\delta(v_3,u_2)+2\)

