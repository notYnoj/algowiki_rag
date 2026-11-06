Given a vertex _u_ and a pair \(v,v'\) of _u_’s neighbors, let \(\mathsf{vote}_u(v,v')\) be _u_’s vote for _v_ versus \(v'\). So \(\mathsf{vote}_u(v,v')\) is 1 if _u_ prefers _v_ to \(v'\), it is -1 if _u_ prefers \(v'\) to _v_, otherwise it is 0 (i.e., \(v=v'\)).

For a point **_x_** in the matching polytope of _G_, first make **_x_** perfect in \(\tilde{G}\) by setting \(x_{(u,u)}=1-\sum_{e\in\delta(u)}x_e\) for each \(u\in A\cup B\). The following definition will be useful:<tbc>

\(\mathsf{vote}_u(v,x)=\sum_{v^\prime\in A\cup B}x_{(u,v^\prime)}\cdot\mathsf{vote}_u(v,v')=\sum_{v^\prime:v^\prime\prec_uv}x_{(u,v^\prime)}-\sum_{v^\prime:v^\prime\succ_uv}x_{(u,v^\prime)},\)

<tbc>where \(\{v':v'\prec_uv\}\) consists of all neighbors of _u_ that are ranked worse than _v_ in _u_’s preference list and the set \(\{v':v'\succ_uv\}\) consists of all those that are ranked better; the vertex _u_ is a member of the former set. For any \((a,b)\in E\), its weight wt_<sub>x</sub>(a,b_) is equal to vote_<sub>a</sub>(b,**x**_)+vote_<sub>b</sub>(a,**x**_). Thus

\(\mathsf{wt}_x(a,b)=\left(\sum_{b^\prime:b^\prime\prec_ab}x_{(a,b^\prime)}-\sum_{b^\prime:b^\prime\succ_ab}x_{(a,b^\prime)}\right)+\left(\sum_{a^\prime:a^\prime\prec_ba}x_{(a^\prime,b)}-\sum_{a^\prime:a^\prime\succ_ba}x_{(a^\prime,b)}\right).\) (1)

For any \(u\in A\cup B\), the weight of the self-loop (_u,u_) is \(\mathsf{wt}_x(u,u)=\mathsf{vote}_u(u,x)=-\sum_{e\in\delta(u)}x_e\), where \(\delta(u)\) is the set of edges incident to _u_ in _G_. A fractional matching **_x_** is popular if and only if every perfect fractional matching in \(\tilde{G}\) with edge weights given by wt_<sub>x</sub>_ has weight at most 0. Note that, when **_x_** is the incidence vector of a matching _M_, we have wt_<sub>x</sub>_=wt_<sub>M</sub>_. Section 4 discusses popular fractional matchings in more detail.

The popular fractional matching polytope L_<sub>G</sub>_ is the smallest convex set that contains all popular fractional matchings in _G_. We can formulate L_<sub>G</sub>_ as follows. Let \(\tilde{E}\) be the edge set of \(\tilde{G}\) and let \(\tilde{\delta}(u)=\delta(u)\cup\{(u,u)\}\) for all vertices _u_.

\(\mathsf{wt}_x(N)=\sum_{e\in N}\mathsf{wt}_x(e)\le 0\forall\text{perfect matchings}N\text{in}\tilde{G},\)<br>
\(\sum_{e\in\tilde{\delta}(u)}x_e=1\forall u\in A\cup B\text{and}x_e\ge 0\forall e\in\tilde{E}.\)

The above formulation of L_<sub>G</sub>_ in the original space involves exponentially many constraints. The following compact extended formulation E_<sub>G</sub>_ of L_<sub>G</sub>_ follows from \[31\] (and was explicitly spelt out in \[30\]).

\(\sum_{u\in A\cup B}\alpha_u=0\) (2) \(\sum_{e\in\tilde{\delta}(u)}x_e=1\forall u\in A\cup B\) (5)

\(\alpha_a+\alpha_b\ge\mathsf{wt}_x(a,b)\forall(a,b)\in E\) (3) \(x_e\ge 0\forall e\in\tilde{E}.\) (6)

\(\alpha_u\ge\mathsf{wt}_x(u,u)\forall u\in A\cup B\) (4)

_Remark._ As observed in \[27\], setting \(\alpha_u=0\) for all _u_ makes the above formulation a description of the stable matching polytope that is equivalent to Rothblum’s formulation \[39\].

The LP that gives rise to the above formulation minimizes \(\sum_u\alpha_u\) subject to constraints (3)-(6). This LP is _self-dual_ (it is the same as its dual); this property was used in \[27\] to show the half-integrality of the polytope L_<sub>G</sub>_. Interestingly, in the special case when _G_ admits a perfect stable matching, i.e., when all vertices are matched in some (equivalently, every \[17\]) stable matching, it was shown in \[27\] that L_<sub>G</sub>_ is integral. This result will be used in Section 3.

The above formulation allows us to extend the notion of _witness_ to popular fractional matchings.

**Definition 2.** _If_ \((x,\alpha)\) _satisfies constraints_ (2)-(6) _then_ \(\alpha\) _is called a witness of **x**’s popularity._

Hence, for any **_x_** in the matching polytope of _G_ (this is given by constraints (5)-(6)), \(\alpha\) is a witness of **_x_**’s popularity if constraints (2)-(4) are satisfied. For example, consider the half-integral matching **_x_** in the<tbc>

