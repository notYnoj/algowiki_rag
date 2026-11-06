<tbc>_Proof._ The equations \(\langle u_iu_i^\top,M\rangle=1\) are linear in _M_, and if the coefficient matrices span Sym(R_<sup>g</sup>_) they have at most one solution. The second statement follows from Lemmas 2.1 and 2.2. □

The converse holds whenever \(M_0\succ 0\): a nonzero symmetric matrix orthogonal to every \(u_iu_i^\top\) gives sufficiently small feasible perturbations of both signs. Thus uniqueness is equivalent to the absence of such a perturbation. In particular, \(n\ge\genfrac(){pt}{2}{g+1}{2}\) is necessary. Our constructions achieve equality before any pendant vertices are added.

We will use two small graphs to start the construction. The graph _K_<sub>1</sub> has the unique feasible matrix (1), of rank one. For the triangle _K_<sub>3</sub>, the objective of a Gram matrix of unit vectors _v_<sub>1</sub>_,v_<sub>2</sub>_,v_<sub>3</sub> is

\(\frac{1}{4}\left(9-\|v_1+v_2+v_3\|^2\right).\)

Three unit vectors summing to zero attain the maximum. Taking inner products with each vector shows that all three off-diagonal entries of their Gram matrix are -1/2. Hence the optimum for _K_<sub>3</sub> is unique and has rank two.

The following extension lets us add vertices without changing the optimal rank.

**Lemma 2.4.** _Let_ \(G'\) _be obtained from a graph G by adding a new vertex_ \(\ell\) _and a single edge_ \(v\ell\) _of weight one, where_ \(v\in V(G)\)_. Then_

\(\mathrm{sdp}(G')=\mathrm{sdp}(G)+1,\rho(G')=\rho(G).\)

_If the optimal solution for G is unique, then so is the optimal solution for_ \(G'\).

_Proof._ For any unit-vector representation of \(G'\), the old edges contribute at most sdp(_G_) and the new edge contributes \(\frac{1}{4}\|v_\ell-v_v\|^2\le 1\). Conversely, an optimal representation of _G_ extends by setting \(v_\ell=-v_v\), attaining sdp(_G_)+1 without increasing the rank. Every optimum for \(G'\) must therefore restrict to an optimum for _G_, which proves the equality of optimal ranks. Moreover, equality on the new edge forces \(v_\ell=-v_v\). All correlations involving the new vertex are consequently fixed by the old Gram matrix, proving the assertion about uniqueness. □

## 3. The Kneser graphs

We now construct the optimal representation and show that it is forced by the diagonal equations. Fix \(m\ge 5\), let _G=K(m,_2) and \(n=\genfrac(){pt}{2}{m}{2}\). We write vertices as pairs _e_={_a,b_}, and _A_ for the adjacency matrix. The graph is regular of degree \(d=\genfrac(){pt}{2}{m-2}{2}\), so _L=dI-A_ and the top Laplacian eigenspace is the least adjacency eigenspace.

Let \(N\in\mathbb{R}^{n\times m}\) be the incidence matrix of pairs versus points, _N<sub>e,a</sub>_=1 if \(a\in e\). Then \(N^\top N=(m-2)I+J\), where _J_ is the all-ones matrix, because a point lies in _m_-1 pairs and two distinct points lie in exactly one. Put

\(E=\{Nf:f\in\mathbb{R}^m,\mathbf{1}^\top f=0\}.\)

Since \(N^\top N=(m-2)I\) on \(\mathbf{1}^\perp\), the map \(f\mapsto Nf\) is injective there and dim_E=m_-1.

**Lemma 3.1.** _The Laplacian L of K(m,_2) _has eigenvalue_ 0 _on_ span(**1**)_, eigenvalue d+m_-3 _on E, and eigenvalue d_-1 _on the orthogonal complement of_ \(\mathrm{span}(\mathbf{1})\oplus E\)_. In particular_ \(\lambda_\mathrm{max}(L)=d+m-3\) _and its eigenspace is exactly E._

_Proof._ For _x=Nf_ with \(\mathbf{1}^\top f=0\) we have _x<sub>ab</sub>=f<sub>a</sub>+f<sub>b</sub>_, and

\((Ax)_{ab}=\sum_{\{c,c^\prime\}\cap\{a,b\}=\varnothing}(f_c+f_{c^\prime})\)<br>
\(=(m-3)\sum_{c\notin\{a,b\}}f_c=-(m-3)(f_a+f_b),\)

