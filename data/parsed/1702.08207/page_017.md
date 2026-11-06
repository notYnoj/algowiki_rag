**Lemma 4.8.** _The running time of procedure_ \(\mathtt{BuildStrategy}(r(T),\omega)\) _is at most_ \(O((cn)^{\gamma L})\)_, for some absolute constant_ \(\gamma=O(1)\)_, for any_ \(\omega\le n\).

_Proof._ The procedure BuildStrategy is run recursively, and is executed once for each node of the tree. The time of each execution is upper-bounded, up to multiplicative factors polynomial in _n_, by the size of the largest of the schedule sets named \(\hat{\mathcal{S}}[u]\), \(u\in V\) , or \(\hat{\mathcal{S}}_i^*\), appearing in the procedure. We further focus only on bounding the size \(|\hat{\mathcal{S}}|\) of the state space of distinct possible schedules in the (_s<sub>v</sub>,t<sub>v</sub>_) representation. The array _s<sub>v</sub>_ has size _L_, with each entry _s<sub>v</sub>_\[_p_\], \(0\le p\le L-1\), taking one of the values \(s_v[p]\in\{0,\frac{1}{\omega cn},\frac{2}{\omega cn},\dots,1\}\), where the size of the set of possible values is \(\omega cn+1\in\mathbb{N}\). Additionally, in some of the auxiliary schedules, the additional array field _s<sub>v</sub>.max\_child\_load_ has length _L_, with each entry _s<sub>v</sub>.max\_child\_load_\[_p_\], \(0\le p\le L-1\), likewise taking one of the values from the set \(\{0,\frac{1}{\omega cn},\frac{2}{\omega cn},\dots,1\}\). Finally, for the time _t<sub>v</sub>_, we have: \(t_v\in\{0,\omega,2\omega,\dots,(L-1)\omega,\perp\}\), where the size of the set of possible values is _L_+1.

Overall, we obtain:

\(|\hat{\mathcal{S}}|\le(L+1)(\omega cn+1)^L(\omega cn+1)^L\le(L+1)\left(cn^2+1\right)^{2L}<(cn)^{L\gamma^\prime},\)

where \(\gamma'>0\) is a suitably chosen absolute constant. Accommodating the earlier omitted multiplicative _O_(poly(_n_)) factors in the running time of the algorithm, we get the claim for some suitably chosen absolute constant \(\gamma>\gamma'\).

## 4.3 Sequence Assignment Algorithm with Small \(\mathtt{COST}^{(\omega,c)}\)

The procedure for computing a sequence assignment _S_ which achieves a small value of \(\mathtt{COST}^{(\omega,c)}\) is given in Algorithm 4.3. This relies on procedure \(\mathtt{BuildStrategy}(r(T),\omega)\) as an essential subroutine, first determining the minimum value of \(\omega=\frac{i}{cn}\), \(i\in\mathbb{N}\), for which BuildStrategy produces a schedule. Since the schedule of a parent node _v_ is based on an insertion of a query to _v_ into the schedules of its children, a standard backtracking procedure allows us to determine the representation \((s_v,t_v)_{v\in V}\) of the schedules of all nodes of the tree.

**Algorithm 4.3** Construction of sequence assignment _S_

1: \(\omega\leftarrow\frac{1}{cn}\)

2: **while** \(\mathtt{BuildStrategy}(r(T),\omega)=\emptyset\) **do**

3: \(\omega\leftarrow\omega+\frac{1}{cn}\)

4: \((s_v,t_v)_{v\in V}\leftarrow\) schedule assignment of duration at most \(L\omega\), satisfying constraints (4.4), (4.5), and (4.6),<br>
 reconstructed by backtracking through the sets \((\hat{\mathcal{S}}[v])_{v\in V}\) computed in the last call<br>
to procedure BuildStrategy(_r(T_), \(\omega\)).

5: **for** \(v\in V\) **do**

6: \(C(v)\leftarrow\emptyset\)

7: **for** \(u\in V(T_v)\) **do**

8: **if** there is no vertex \(z\neq u\) on the path from _v_ to _u_ s.t. \(t_z<\lfloor t_u+w'(u)\rfloor_\omega+\omega\) **then**

9: \(C(v)\leftarrow C(v)\cup\{(\lfloor t_u\rfloor_\omega,\lfloor t_u+w'(u)\rfloor_\omega,u)\}\)

10: \(S(v)\leftarrow\) sequence of vertices (third field) of _C(v_) sorted in non-decreasing<br>
order, with tuples compared by first field, then second field, then third field.

11: **return** \((S(v))_{v\in V}\)

We start by observing in Algorithm 4.3 that if a node _v_ is not queried \((t_v=\perp)\), then all of the children of _v_ belong to the schedules produced by procedure BuildStrategy following condition (4.4), and thus they will also appear in _S(v_). This guarantees the validity of the solution.

