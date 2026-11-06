### Warm up: \(\beta=4\)

Note _k_=7_,k_<sub>0</sub>=2. Let _z_ be the vertex of maximum degree. Let _w=b(u,P_) be the vertex closest to _v_ such that \(\mathrm{deg}(w)\ge s_{k_0+4}=s_6\). Since \(P=P_{u,w}\cdot P_{w,v}\), the sub-path _P<sub>u,w</sub>_ must contain the vertex _z_. Let \(z^*=r(z,D_{\ell(z)}),w^*=r(w,D_{k_0+4})\). Since \(P\subset E_{\ell(z)}\), we have \(\hat{\delta}_{\ell(z)}(z^*,u)\le\delta(z,u)+1\) and \(\hat{\delta}_{\ell(z)}(z^*,w^*)\le\delta(z,w)+2\). Furthermore, since \(\ell(z)+(k_0+4)+(k_0+5)\le 3k_0+9=2k+1\), in the _k_<sub>0</sub>+5-th iteration,

\(\hat{\delta}(u,v)\le\hat{\delta}_{\ell(z)}(u,z^*)+\hat{\delta}_{\ell(z)}(z^*,w^*)+1+\delta(w,v)\le\delta(u,v)+4\)

as desired.

## Generalization to \(\beta\ge 6\)

Suppose \(\ell(v)\le\ell(u)\). Recall from Lemma A.2 the blocking vertices _B(P_)={_x_<sub>0</sub>_,x_<sub>1</sub>_,...,x<sub>t</sub>_} and levels _L<sub>B</sub>(P_) of path _P_.

Let \(a=\mathrm{min}_{\ell(x_i)\le k_0+5}i\) be the minimum index of an element in the blocking set such that \(\ell(x_i)\le k_0+5\). Since \(k\ge\ell(x_1)>\ell(x_2)>\dots>\ell(x_t)\ge 1\), we can upper bound,

\(a\le k-(k_0+5)=\frac{\beta}{2}-2\)

Since _P_ is not contained in _E_<sub>_k_<sub>0</sub>+1</sub>, we can assume _a_ exists and \(a\ge 1\).

Let \(x_a\in B(P)\) be the corresponding vertex in _B(P_). Since _P_ has an edge not in _E_<sub>_k_<sub>0</sub>+1</sub>, the last blocking vertex of minimum level must have \(\ell(x_t)\le k_0\). Let \(v^*=r\left(v,D_{\ell(v)}\right)\) for any vertex _v_. Since \(P\subset E_{\ell(x_t)}\), we again have \(\hat{\delta}_{\ell(x_t)}(x_t^*,x_a^*)\le\delta(x_t,x_a)+2\) and \(\hat{\delta}_{\ell(x_t)}(x_t^*,x_{a+1}^*)\le\delta(x_t,x_{a+1})+2\).

Consider the \(\ell(x_a)\)-th iteration. The edges \(D_{\ell(x_t)}\times D_{\ell(x_{a+1})}\) are in \(G_{\ell(x_a),x_a}\) as,<tbc>

\(\ell(z)+\ell(x_{a+1})+\ell(x_a)\le k_0+(k_0+4)+(k_0+5)=3k_0+9=3\left(k-\frac{\beta}{2}-3\right)+9=2k+1\)

<tbc>Then, since \(x_t\in P_{x_a,x_{a+1}}\),

\(\hat{\delta}_{\ell(x_a)}(x_a^*,x_{a-1})\le\hat{\delta}_{\ell(x_t)}(x_a^*,x_t^*)+\hat{\delta}_{\ell(x_t)}(x_t^*,x_{a+1}^*)+1+\delta(x_{a+1},x_{a-1})\)<br>
\(\le\delta(x_a,x_t)+\delta(x_t,x_{a+1})+\delta(x_{a+1},x_{a-1})+5\)<br>
\(\le\delta(x_a,x_{a-1})+5\)

Then, following a similar argument to the inductive step of Lemma A.2, we claim the following for all \(1\le j\le a\).

\(\hat{\delta}_{\ell(x_j)}(x_j^*,x_{j-1})\le\delta(x_j,x_{j-1})+2(2+(a-j))+1\)

where we have established the base case _j=a_ above. We now proceed by induction for _j\<a_. Consider an execution of `Dijkstra` from \(x_j^*\) in \(G_{\ell(x_j),x_j^*}\). Let _x_<sub>_j_+1</sub> be the blocking vertex from the previous iteration. We take the edges \((x_j^*,x_{j+1}^*)\), \((x_{j+1}^*,x_{j+1})\in E^*\), and the remaining edges in \(E_{\ell(x_j)}\). By induction, we have,

\(\hat{\delta}_{\ell(x_j)}(x_j^*,x_{j-1})\le\hat{\delta}_{\ell(x_{j+1})}(x_j^*,x_{j+1}^*)+1+\delta(x_{j+1},x_{j-1})\)<br>
\(\le\delta(x_j,x_{j+1})+2(2+(a-(j+1)))+3+\delta(x_{j+1},x_{j-1})\)<br>
\(\le\delta(x_j,x_{j-1})+2(2+(a-j))+1\)

Thus, we have,

\(\hat{\delta}_{\ell(v)}(v^*,u)=\hat{\delta}_{\ell(x_1)}(x_1^*,x_0)\le\delta(v,u)+2(a+1)+1\)

