- \(E_g:=\{\{e_g^{(i)},G_g\}|e\in E(G),i\in[k]\}\)<tbc>

**-** \(E_C:=\{\{c_v^{(i)},c_v^{(i+1\mathrm{mod}k)}\}|v\in V(G),i\in[k]\}\cup\{\{v^{(i)},c_v^{(i)}\}|v\in V(G),i\in[k]\}\)<tbc>

\(\text{-}\)<br>
\(E_W=\bigcup_{e\in E(G)e=\{u,v\}}\bigcup_{i=1}^k\big\{\{e_u^{(i)},e_v^{(i)}\},\{e_v^{(i)},e_g^{(i)}\},\{e_g^{(i)},e_u^{(i)}\},\{e_u^{(i)},u^{(i)}\},\{e_v^{(i)},v^{(i)}\}\big\}\)

We show that \(\mathcal{L}(\cdot,\cdot)\) describes a correct polynomial-time many-one reduction.

**Lemma 9.19.** _Given a graph G and an odd integer_ \(k\ge 3\)_, then_ L(_G,k_) _satisfies the following properties:_

• L(_G,k_) _has_ \(O(k\cdot(|V(G)|+|E(G)|))\) _many vertices and edges._<tbc>

• L(_G,k_) _can be constructed in time_ \(O(k\cdot(|V(G)|+|E(G)|))\).<tbc>

• L(_G,k_) _is_ 3_-colorable if and only if G is k-colorable._

_Proof._ Write _n_:=|_V(G_)| and _m_:=|_E(G_)|. It is easy to check that L(_G,k_) has \(O(k\cdot(n+m))\) many vertices and edges and that we can construct L(_G,k_) in time \(O(k\cdot(n+m))\). In the following, we assume that L(_G,k_) is 3-colorable with a function \(\tilde{c}:V(\mathcal{L}(G,k))\rightarrow\{r,g,b\}\) (i.e., the colors red, green, blue). We show that _G_ is _k_-colorable.

Without loss of generality, we assume that the vertex \(G_g\in\mathcal{L}(G,k)\) is colored _g_ and \(G_b\in\mathcal{L}(G,k)\) is colored _b_ (we can do this since _G<sub>g</sub>_ and _G<sub>b</sub>_ are connected). Next, observe that \(\tilde{c}(v^{(i)})\in\{r,g\}\) since each _v_<sup>(_i_)</sup> is connected to _G<sub>b</sub>_. Next, we show the following claim.

**Claim 9.20.** _For every_ \(v\in V(G)\) _there exists an index_ \(i\in[k]\) _such that_ \(\tilde{c}(v^{(i)})=g\).

_Proof._ Assume otherwise, then \(\tilde{c}(v^{(i)})=r\) for all \(i\in[k]\). Since _k_ is odd, we obtain that the vertices \(\{c_v^{(i)}|i\in[k]\}\) induce an odd cycle of size at least 3. Now, each odd cycle of size 3 is 3-colorable but not two colorable. Thus there is an index \(i\in[k]\) with \(\tilde{c}(c^{(i)})=r\). However, this is not possible since _v_<sup>(_i_)</sup> is adjacent to _c_<sup>(_i_)</sup>. Thus, our assumption that \(\tilde{c}(v^{(i)})=r\), for all \(i\in[k]\), is wrong and therefore there exist an \(i\in[k]\) with \(\tilde{c}(v^{(i)})=g\).

Now, Claim 9.20 yields a function \(f:V(G)\rightarrow[k]\) that maps each vertex _v_ to the smallest value \(i\in[k]\) with \(\tilde{c}(v^{(i)})=g\). We show that _f_ is a _k_-coloring for _G_. Assume that _f_ is not a proper 3-coloring then there is an edge \(e=\{u,v\}\in E(G)\) with _f(u_)=_f(v_)=_i_. By construction, we obtain \(\tilde{c}(v^{(i)})=g=\tilde{c}(u^{(i)})\). Further, note that \(\tilde{c}(G_g)=g\). Thus, each vertex in the triangle \(\{e_u^{(i)},e_v^{(i)},e_g^{(i)}\}\) is adjacent to a vertex with color _g_. Hence, we can only use the colors {_r,b_} to color \(\{e_u^{(i)},e_v^{(i)},e_g^{(i)}\}\) which is not possible since the vertices form a triangle in L(_G,k_). Therefore, \(\tilde{c}\) is not a proper 3-coloring which is a contradiction.

Next, let \(f:V(G)\rightarrow[k]\) be a _k_-coloring for _G_. We define the the following mapping on the subset \(V':=\{G_g,G_b\}\cup\{v^{(i)}|v\in V(G),i\in[k]\}\) of vertices of L(_G,k_).

\(c':V'\rightarrow\{r,g,b\},x\mapsto\left\{\begin{array}{ c c }
g & \text{if}x=G_g \\
b & \text{if}x=G_b \\
g & \text{if}x=v^{(i)}\text{and}f(v)=i \\
r & \text{if}x=v^{(i)}\text{and}f(v)\neq i
\end{array}\right.\)

