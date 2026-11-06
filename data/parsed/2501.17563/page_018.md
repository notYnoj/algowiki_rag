_Proof._ Consider an STT _T_<sub>1</sub> where _i_ has depth \(k>\frac{1}{f_i}\). Define _T_<sub>2</sub> by promoting _i_ to the root. Each node other than _i_ gains at most one new ancestor (_i_), so we lose a cost of at most \(\sum_{j(\neq i)\in U}f_j=1-f_i\). However, we also save a cost of \((k-1)\cdot f_i\) for _i_. In total: \(cost(T_1)-cost(T_2)\ge(k-1)f_i-(1-f_i)=k\cdot f_i-1>0\). So _T_<sub>1</sub> is sub-optimal.

**Corollary 3.5.** If there is a node _i_ with frequency \(f_i>\frac{1}{2}\), it must be the root of every optimal STT. Therefore, we can focus our efforts on inputs where \(\forall i:f_i\le\frac{1}{2}\).

## 3.2 More Analysis of Integer Vertices

In this section we motivate focusing our interest on the lower envelope of the _D_-space polytope as we discussed in Section 2.2 for the normals method.

**Theorem 3.6.** Let P be the polytope of the LP corresponding to a topology _U_, and let \(P\in\mathbb{P}\) be an integer point. If _P_ is induced by some STT _T_ then _P_ is a vertex on the lower envelope of P. Moreover, if the projection of _P_ to _D_-space is a vertex on the lower envelope of the projection of P, then _P_ is induced by some STT.

Note that Theorem 3.6 is almost an "if and only if" statement, except that the first part of the claim considers the (_X,Z,D_)-polytope while the second part considers the projection to _D_-space.

_Proof._ We distinguish projections to _D_-space from the corresponding objects in the (_X,Z,D_)- polytope by a subscript _D_. Consider the second part of the claim, that _P<sub>D</sub>_ is a vertex on the lower-envelope of P_<sub>D</sub>_, and assume by contradiction that _P_ is not induced by some STT. Then by being a vertex of P_<sub>D</sub>_, there is a direction _w_ for which _P_ is the unique optimum of the LP. Since _P<sub>D</sub>_ is on the lower envelope of P_<sub>D</sub>_, there is such _w_ with non-negative coordinates. This _w_ is a natural objective function to Problem 1, and from Property 2 we deduce that _P_ is not the unique optimum in the direction _w_, a contradiction.

For the first part of the claim, define the weight of each node _i_ as \(w_i=n^{-4\cdot depth_T(i)}\) (recall that _T_ induces _P_). We next show that _P_ is the unique optimal solution for the LP in the direction _w_. This implies that _P_ is a vertex, and since all the weights are positive, that _P_ is on the lower envelope of P.

To show that _P_ is uniquely optimal in the direction _w_, we prove that every optimal solution satisfies \(\forall i:X_{ir}=0\) (this holds for _P_). Then \(X_{ir}=0\Rightarrow Z_{ijr}=0\) (\(\le X_{ir}\)) and we deduce from the ancestry constraint on _r_ and _j_ that \(\forall j:X_{rj}=1\). The argument is concluded by recursively considering the connected components of the topology when _r_ is removed, and eventually after we fix all the variables, the set of optimal solutions turns out to be a single point, _P_.

Consider a feasible solution with _X_ coordinates such that there is some \(i\neq r\) such that _X<sub>ir</sub>\>_0, and let \(\Delta\equiv min\{X_{ir}|X_{ir}>0\}\). We can infer values of the other variables by setting: \(D_i=\sum_jX_{ji}\) and _Z<sub>kij</sub>_=min{_X<sub>ki</sub>,X<sub>kj</sub>_}.<sup>9</sup> We define an alternative feasible solution \(X'\) where \(X'_{ij}=X_{ij}+n\Delta\) for \(j\neq r\), \(X'_{ir}=max\{0,X_{ir}-\Delta\}\) and \(Z'_{kij}=min\{X'_{ki},X'_{kj}\}\). If _j=r_ then \(Z'_{kir}\ge Z_{kir}-\Delta\) (\(Z'_{kir}=Z_{kir}\) if _X<sub>kr</sub>_=0), and if \(r\neq i,j\) then \(Z'_{kij}=Z_{kij}+n\Delta\).

By construction we maintain the non-negativity of \(X'\) (and hence of \(Z'\)). Ancestry constraints are preserved because all the variables increase except for those of the form _X<sub>ir</sub>_ and _Z<sub>kir</sub>_ (\(i\neq r\)). _X<sub>ir</sub>_ and _Z<sub>kir</sub>_ only decrease if _X<sub>ir</sub>\>_0, and can only violate the ancestry constraints over the pair<tbc>

<sup>9</sup>There could be other ways to set _Z_ (smaller) and _D_ (larger), but our choice is feasible. Importantly, we cannot choose smaller values of _D_.

