<tbc>we may assume that this path is contained in _B<sub>i,j</sub>_). This proves \(D_{x,y}^{i,j}\le D_{x^\prime,y^\prime}^{i-1,j}+d(v_{x^\prime,y^\prime},v_{x,y})=D_{x,y}^{i,j}\le D_{x^\prime,y^\prime}^{i-1,j}+d_{x,y}-d_{x^\prime,y^\prime}\). The inductive assumption yields \(D_{x^\prime,y^\prime}^{i-1,j}=d_{x^\prime,y^\prime}\), and thus \(D_{x,y}^{i,j}\le d_{x,y}\) holds as claimed.

**Proposition 3.13.** _Given a straight-line program_ **G**_<sub>X</sub> of size n generating a string X of length N\>_0_, a straight-line program_ **G**_<sub>Y</sub> of size m generating a string Y of length M\>_0_, and an integer_ \(D\in[1..N+M]\)_, one can in_ \(\widetilde{O}\left(\sqrt{nmD(N+M)}\right)\) _time compute_ \(\delta_D(X,Y)\) _or certify that_ \(\delta_D(X,Y)>D\).

_Proof._ The algorithm uses Corollary 3.9 and Lemma 3.5 with the set of portals **P** defined as in Lemma 3.12. The latter lemma guarantees that the resulting value is \(\delta_D(X,Y)\) provided that \(\delta_D(X,Y)\le D\). Otherwise, the resulting value exceeds _D_, certifying that \(\delta_D(X,Y)>D\).

The number of portals is \(O(D\cdot\frac{N+M}{\tau})\), so the overall running time is \(\widetilde{O}(nm\tau+D\cdot\frac{N+M}{\tau})\). Optimizing \(\tau\in[1..N+M]\), we get \(\widetilde{O}(nm+D+\sqrt{nmD(N+M)})\) time. Since \(D\le N+M\), the second term is dominated by the third one. If the first term dominates, then _nm\>D(N+M_), and thus \(\sqrt{nmD(N+M)}\ge D(N+M)\). However, \(\widetilde{O}(N+M+D^2)=\widetilde{O}(D(N+M))\) time suffices solve the problem for uncompressed strings \[LV88\].

Theorem 3.11 follows through exponential search and the reduction from \(\delta_E\) to \(\delta_D\).

## 3.5 LCS Approximation

In this section we prove Theorem 3.14:

**Theorem 3.14.** _Given a straight-line program_ **G**_<sub>X</sub> of size n generating a string X of length N\>_0_, a straight-line program_ **G**_<sub>Y</sub> of size m generating a string Y of length M\>_0_, and a parameter_ \(\epsilon\in(0,1]\)_, a_ \((1+\epsilon)\)_-approximation of_ LCS(_X,Y_) _can be computed in_ \(\widetilde{O}\left((nm(N+M))^{2/3}\epsilon^{-1/3}\right)\) _time._

The algorithm behind Theorem 3.14 is essentially the same as that of Theorem 3.1, and this is why the running times coincide. The main difference is that the output portals of the box _B<sub>i,j</sub>_ are chosen _adaptively_ while the dynamic-programming algorithm processes _B<sub>i,j</sub>_.

As for LCS approximation, our choice of portals is _adaptive_. For a box \(B_{i,j}\in\mathbf{B}\), let \(\mathbf{P}_{i,j}=\mathbf{P}\cap\mathrm{out}^{B_{i,j}}\). Observe that the value \(D_{x,y}^{i,j}\) for \(v_{x,y}\in B_{i,j}\) depends only on \(\mathbf{P}_{i^\prime,j^\prime}\) with \(i'+j'<i+j\). Hence, except for the grid vertices (all included in **P**), we may select the portals **P**_<sub>i,j</sub>_ based on the values \(D_{x,y}^{i,j}\) for \(v_{x,y}\in\mathrm{out}^{B_{i,j}}\).

For \(v_{x,y}\in B_{i,j}\), let \(\ell_{x,y}=\frac{1}{2}(|X|+|Y|-d_{x,y})=\mathrm{LCS}(X[1..x],Y[1..y])\) and \(L_{x,y}^{i,j}=\frac{1}{2}(|X|+|Y|-D_{x,y}^{i,j})\).

**Lemma 3.15.** _Let_ **B** _be a box decomposition of the graph G<sub>X,Y</sub> for_ \(X,Y\in\Sigma^+\) _and let_ \(\alpha>0\) _be a real number. Suppose that_ **P** _consists of all the grid vertices and, for each box_ \(B_{i,j}\in\mathbf{B}\)_, all vertices_ \(v_{x,y}\in\mathrm{out}^{B_{i,j}}\) _such that:_

• \(v_{x-1,y}\in\mathrm{out}^{B_{i,j}}\) _and_ \(\lfloor\mathrm{log}_{1+\alpha} L_{x,y}^{i,j}\rfloor>\lfloor\mathrm{log}_{1+\alpha} L_{x-1,y}^{i,j}\rfloor\)_, or_<tbc>

• \(v_{x,y-1}\in\mathrm{out}^{B_{i,j}}\) _and_ \(\lfloor\mathrm{log}_{1+\alpha} L_{x,y}^{i,j}\rfloor>\lfloor\mathrm{log}_{1+\alpha} L_{x,y-1}^{i,j}\rfloor\).

_Then, for each vertex_ \(v_{x,y}\in B_{i,j}\)_, we have_ \(L_{x,y}^{i,j}\ge(1+\alpha)^{2-i-j}\ell_{x,y}\).

_Proof._ We proceed by induction on _i+j_. The base case is trivially satisfied due to \(L_{x,y}^{1,1}=\ell_{x,y}\) for \(v_{x,y}\in B_{1,1}\). Thus, we henceforth fix a vertex \(v_{x,y}\in B_{i,j}\) with \((i,j)\neq(1,1)\). By Observation 3.3, there is a shortest path from _v_<sub>0,0</sub> to _v<sub>x,y</sub>_ contained within _G_<sub>_X_\[1_..x_\]_,Y_\[1_..y_\]</sub>. Let \(v_{x^\prime,y^\prime}\) be the first vertex on this path that belong to _B<sub>i,j</sub>_. Observe that \(v_{x^\prime,y^\prime}\in\mathrm{in}^{B_{i,j}}\) and \(\ell_{x,y}=\ell_{x^\prime,y^\prime}+\mathrm{LCS}(X(x'..x],Y(y'..y])\). By symmetry, we may assume without loss of generality that \(v_{x^\prime,y^\prime}\in\mathrm{out}^{B_{i-1,j}}\).

Consider the largest value \(y''\in[1..y']\) such that \(v_{x^\prime,y^{\prime\prime}}\in\mathbf{P}_{i-1,j}\). Since grid vertices are portals, such \(v_{x^\prime,y^{\prime\prime}}\) exits. Moreover, by the choice of the remaining portals, \(L_{x^\prime,y^\prime}^{i-1,j}\le(1+\alpha)L_{x^\prime,y^{\prime\prime}}^{i-1,j}\). Let us construct a portal-respecting (_i,j_) walk to _v<sub>x,y</sub>_ by concatenating a shortest portal-respecting (_i_-1_,j_)-walk to \(v_{x^\prime,y^{\prime\prime}}\) and a shortest path from \(v_{x^\prime,y^{\prime\prime}}\) to _v<sub>x,y</sub>_ (by Observation 3.3, we may assume that this path is contained _B<sub>i,j</sub>_). This proves that \(D_{x,y}^{i,j}\le D_{x^\prime,y^{\prime\prime}}^{i-1,j}+d(v_{x^\prime,y^{\prime\prime}},v_{x,y})\le D_{x^\prime,y^{\prime\prime}}^{i-1,j}+y'-y''+d(v_{x^\prime,y^\prime},v_{x,y})\), i.e., \(L_{x,y}^{i,j}\ge L_{x^\prime,y^{\prime\prime}}^{i-1,j}+\mathrm{LCS}(X(x'..x],Y(y'..y])\ge(1+\alpha)^{-1}L_{x^\prime,y^\prime}^{i-1,j}+\ell_{x,y}-\ell_{x^\prime,y^\prime}\). The inductive assumption further yields \(L_{x^\prime,y^\prime}^{i-1,j}\ge(1+\alpha)^{3-i-j}\ell_{x^\prime,y^\prime}\), and thus \(L_{x,y}^{i,j}\ge(1+\alpha)^{2-i-j}\ell_{x^\prime,y^\prime}+\ell_{x,y}-\ell_{x^\prime,y^\prime}\ge(1+\alpha)^{2-i-j}\ell_{x,y}\) holds as claimed.

