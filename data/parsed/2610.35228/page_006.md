**Definition 3.1** (Pseudo-distribution)**.** _Let_ \(r\ge 1\) _be an integer. A level-r pseudo-distribution is a function_ \(\nu:\mathcal{V}_{2r}\rightarrow\mathbb{R}\) _such that_

(_a)_ \(\nu(\emptyset)=1\);<tbc>

(_b)_ \(\nu(T)=0\) _for every_ \(T\in\mathcal{V}_{2r}\) _that contains an edge of G;_<tbc>

_(c)_ _the moment matrix_ \(M_r[\nu]:=(\nu(A\cup B))_{A,B\in\mathcal{V}_r}\) _is positive semidefinite._

_We write_ \(\nu(u):=\nu(\{u\})\) _and_ \(\nu(u,v):=\nu(\{u,v\})\)_, so that_ \(\nu(u,u)=\nu(u)\).

Singleton marginals of a level-_r_ pseudo-distribution lie in \[0,1\] for \(r\ge 1\). For \(r\ge 2\), pairwise marginals also satisfy the bounds below. Adjacent vertices have zero joint marginal at every level \(r\ge 1\).

**Lemma 3.2** (Basic inequalities)**.** _Let_ \(\nu\) _be a level-r pseudo-distribution._

(_a)_ _If_ \(r\ge 1\)_, then_ \(0\le\nu(u)\le 1\) _for every_ \(u\in V\) .<tbc>

_(b)_ _If_ \(r\ge 2\)_, then_ \(0\le\nu(u,v)\le min\{\nu(u),\nu(v)\}\) _for all_ \(u,v\in V\) _, and_ \(\nu(u,v)=0\) _whenever_ \(uv\in E\).

_Proof._ (a) The principal submatrix of \(M_r[\nu]\) indexed by \(\emptyset,\{u\}\) is

\(\left(\begin{array}{ c c }
1 & \nu(u) \\
\nu(u) & \nu(u)
\end{array}\right),\)

by Definition 3.1-(a). It is positive semidefinite, so \(\nu(u)\ge 0\) and \(\nu(u)-\nu(u)^2\ge 0\).

(b) If _u=v_, the claim follows from (a). Let \(u\neq v\), so that \(\{u\},\{u,v\}\in\mathcal{V}_r\). The diagonal entry of \(M_r[\nu]\) at {_u,v_} is \(\nu(u,v)\), so \(\nu(u,v)\ge 0\). Let _x_ be the vector with _x_<sub>{_u_}</sub>:=1, _x_<sub>{_u,v_}</sub>:=-1, and all other entries zero. Then

\(0\le x^\top M_r[\nu]x=\nu(u)-2\nu(u,v)+\nu(u,v)=\nu(u)-\nu(u,v).\)

The first step follows from Definition 3.1-(c), the second step expands the quadratic form, and the third step collects terms. By symmetry, \(\nu(u,v)\le\nu(v)\) also holds. The final assertion follows from Definition 3.1-(b).

Conditioning on the inclusion of a set with positive marginal uses one level per conditioned vertex. The resulting marginals remain feasible and satisfy the usual identities for successive conditioning.

**Lemma 3.3** (Conditioning)**.** _Let_ \(\nu\) _be a level-r pseudo-distribution, and let_ \(S\subseteq V\) _satisfy_ \(|S|\le r-1\) _and_ \(\nu(S)>0\)_. For_ \(T\in\mathcal{V}_{2(r-|S|)}\) _define_

\(\nu_S(T):=\frac{\nu(S\cup T)}{\nu(S)}.\) (8)

_Then_ \(\nu_S\) _is a level-(r_-|_S_|) _pseudo-distribution. Moreover, if_ \(v\in V\backslash S\) _satisfies_ \(\nu_S(v)>0\)_, then_ \(\nu(S\cup\{v\})=\nu(S)\nu_S(v)>0\)_. If in addition_ \(|S|\le r-2\)_, then for every_ \(u\in V\) ,

\(\nu_{S\cup\{v\}}(u)=\frac{\nu_S(u,v)}{\nu_S(v)}.\) (9)

