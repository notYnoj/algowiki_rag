Conditions (4.3) and (4.4) provide us with necessary conditions which must be satisfied by any consistent aligned schedule assignment.

In order to lower-bound the duration of the consistent aligned schedule assignment with minimum cost, we perform an exhaustive bottom-up evaluation of aligned schedules which satisfy the constraints of (4.4), and a slightly weaker form of the constraints of (4.3). These weaker constraints are introduced to reduce the running time of the algorithm. Instead of considering individual slots of a schedule which may be empty or full, \(\sigma_v[i]\in\{0,1\}\), we consider the load of each box in the same schedule, defined as the proportion of occupied slots within the box. Formally, for the _p_-th box, \(0\le p<L\), the _load s<sub>v</sub>_\[_p_\] is given as:

\(s_v[p]=\frac{1}{\omega cn}\sum_{i=p\cdot\omega cn}^{(p+1)\omega cn-1}\sigma_v[i],s_v[p]\in\left\{0,\frac{1}{\omega cn},\frac{2}{\omega cn},\dots,1\right\},\)

where we recall that \(\omega cn\) is an integer by the choice of \(\omega\). We will call a box with load _s<sub>v</sub>_\[_p_\]=0 an _empty box_, a box with load _s<sub>v</sub>_\[_p_\]=1 a _full box_, and a box with load 0_\<s<sub>v</sub>_\[_p_\]_\<_1 a _partially full box_ in the schedule of _v_.

By summing over all slots within each box, we obtain the following corollary directly from Observation 4.3.

**Corollary 4.5.** _Assume that the tuple_ \((s_v,t_v)_{v\in V}\) _corresponds to a consistent schedule. Let_ \(v\in V\) _be an arbitrarily chosen node with set of children_ {_v_<sub>1</sub>_,...,v<sub>l</sub>_} _and completion time_ \(t_{end}^v\) _of the query to v given as in Observation 4.3. Let a<sub>p</sub> be the contribution to the load of the p-th box of the query job for vertex v, i.e._<tbc>

\(a_p=\left\{\begin{array}{ c c }
\frac{1}{\omega}|[t_v,t_{end}^v]\cap[p\omega,(p+1)\omega]| & \text{\textit{if}}t_v\neq\perp, \\
0 & \text{\textit{if}}t_v=\perp.
\end{array}\right.\)

<tbc>_Then, for any box_ \([p\omega,(p+1)\omega]\), \(0\le p<L\)_, we have:_

\(s_v[p]=a_p+\sum_{j=1}^ls_{v_j}[p]\in[0,1],\text{\textit{when}}t_{end}^v\ge(p+1)\omega,s_v[p]\ge a_p,\text{\textit{when}}p\omega<t_{end}^v<(p+1)\omega,s_v[p]=0,\text{\textit{when}}t_{end}^v\le p\omega.\right\}\) (4.5)

_Moreover, for any box_ \([p\omega,(p+1)\omega]\), \(0\le p<L\)_, we have:_

\(\text{\textit{For all}}1\le j\le l\text{\textit{, the following bound holds:}}s_{v_j}[p]+a_p\le 1.\) (4.6)

We remark that the statement of Corollary 4.5 treats specially one box, namely the one which contains strictly within it the time moment \(t_{end}^v\). For this box, we are unable to make a precise statement about _s<sub>v</sub>_\[_p_\] based on the description of the schedules of its children, and content ourselves with a (potentially) weak lower bound \(s_v[p]\ge a_p=\frac{1}{\omega}(t_{end}^v-p\omega)\). This is the direct reason for the slackness in our subsequent estimation, which loses \(\omega\) time per down query. However, we note that by the definition of aligned schedule, a query to a heavy vertex will never begin or end strictly inside a box, and will not lead to the appearance of this issue. We remark that condition (4.6) additionally stipulates that within any box, it must be possible to schedule the contribution of the query to _v_ and the contribution of any child _v<sub>j</sub>_ to the load of the box in a non-overlapping way. We now show that the shortest schedule assignments satisfying the set of constraints (4.4), (4.5), and (4.6) can be found in _n_<sup>_O_(log_n_)</sup> time. This is<tbc>

