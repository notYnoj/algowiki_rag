**Definition 3.4.** _Let u,v be vertices in a graph G and P a path between u,v. Let_ (_D_<sub>1</sub>_,...,D<sub>k</sub>),_ (_E_<sub>1</sub>_,...,E<sub>k</sub>_) _be the outputs of a call to **Decompose** with degree thresholds s_<sub>1</sub>_,...,s_<sub>_k_-1</sub>_. If there is an edge_ \((a,b)\in P\) _such that_ \((a,b)\notin E_{\ell(u)}\)_, the_ **blocking vertex** _of P from u, denoted b(u,P), is the closest vertex to v that is an endpoint to such an edge. If no such edge exists, then b(u,P_)=_v._

_Then, the_ **blocking vertices of** _P is the set B(P_)={_x_<sub>0</sub>_,x_<sub>1</sub>_,...,x<sub>t</sub>_} _defined in the following manner:_

1. _x_<sub>0</sub>=_u_<tbc>

2. _x_<sub>1</sub>=_v_<tbc>

_3._ \(x_i=b\left(x_{i-1},P_{x_{i-1},x_{i-2}}\right)\) _where P_<sub>_x_<sub>_i_-1</sub>_,x_<sub>_i_-2</sub></sub> _is the sub-path of P between x_<sub>_i_-1</sub>_,x_<sub>_i_-2</sub>.

_For any_ \(j\ge\ell(v)\), **blocking levels of** _P_ **at level** _j is the set_ \(L_B(P,j)=\{\ell(x_i)\text{\textit{s.t.}}x_i\in B(P)\text{\textit{and}}\ell(x_i)<j\}\)_. Denote_ \(L_B(P)=L_B(P,\ell(v))\).

We prove that the number of blocking levels directly determines the additive error accumulated on a given path.

**Lemma 3.5.** _Let u,v be vertices in a graph G and P be a shortest path between u,v. Let B(P_) _be the blocking vertices of P. Then, the distance estimate_ \(\hat{\delta}\) _satisfies_<tbc>

\(\hat{\delta}(v^*,u)\le\delta(v,u)+2|L_B(P)|+1\)

<tbc>_For any level_ \(j\ge\ell(v)\)_, if_ \(v\in D_j\),

\(\hat{\delta}(v,u)\le\hat{\delta}_j(v,u)\le\delta(v,u)+2|L_B(P,j)|\)

The proof is deferred to Appendix A.1.

If \(P\subset F_5\) then we obtain a +6 additive approximation as a Corollary to Lemma 3.5 as \(|L_B(P)|\le 3\). Thus, suppose \(P\subset F_j\) but \(P\unknown\subset F_{j+1}\) for some \(j\le 4\).

For any vertex \(w\in V_7\) and _w_<sup>∗</sup>=_r(w,C_<sub>7</sub>), the graph _G_<sub>7_,w_<sup>∗</sup></sub> contains edge sets \(F_7\cup(w^*\times V)\cup\left(\bigcup_{j=1}^4C_j\times C_6\right)\). For \(v\in V\) , let _z_ denote the first vertex on _P<sub>w,v</sub>_ such that the sub-path \(P_{z,v}\subset F_7\) and \(y\in P_{w,v}\) be the vertex of maximum degree. See Figure 1. Then \(\ell(z)\le 6\), and \(\ell(y)\le 6\). Suppose \(\ell(z)=6\) (other cases are only easier). Let _y_<sup>∗</sup>=_r(y,C<sub>j</sub>_) where \(j\le 6\) and _z_<sup>∗</sup>=_r(z,C_<sub>6</sub>).

W*
y*
Z*
u
W
y
Z
v
l(u) = 8
l(w) = 7
l(y) 4
l(z) = 6
l(v) = 8

Figure 1: Solid lines denote edges and dotted lines represent paths. Blue dashed arrows denote distance estimates used in the (min,+) product. Black dashed arrows denote edges \(w\times V\) used in _G<sub>j,w</sub>_.

