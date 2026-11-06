We show that \(c'\) can be extended to a proper 3-coloring that is defined on all vertices of L(_G,k_). First note that under \(c'\) no two adjacent vertices in \(V'\) have the same color (the only relevant case is between _G<sub>g</sub>_ and _v_<sup>(_i_)</sup> with _f(v_)=_i_ which are non-adjacent by construction).

Let \(v\in V(G)\) then \(\{c_v^{(i)}|\in[k]\}\) induces an odd cycle in L(_G,k_). By construction there are vertices _v_<sup>(_s_)</sup> that are colored _r_ and a vertex _v_<sup>(_i_)</sup> that is colored _g_. Thus, we have three colors available to color the odd cycle \(\{c_v^{(i)}|\in[k]\}\).

Now, let \(e=\{u,v\}\in E(G)\) and \(i\in[k]\) then \(\{e_u^{(i)},e_v^{(i)},e_g^{(i)}\}\) induces a triangle in L(_G,k_). Now, by construction not every node in \(\{e_u^{(i)},e_v^{(i)},e_g^{(i)}\}\) can be adjacent to a vertex that is colored _g_. Otherwise, _f(v_)=_i=f(u_) which is not possible. Thus, we have three colors available to color the triangle \(\{e_u^{(i)},e_v^{(i)},e_g^{(i)}\}\). Meaning that we can extend \(c'\).

The reduction \(\mathcal{L}(\cdot,\cdot)\) is isomorphism-preserving.

**Lemma 9.21.** _Let G and H be two graphs and_ \(k\ge 3\) _be an odd positive integer. If_ \(G\cong H\) _then_ \(\mathcal{L}(G,k)\cong\mathcal{L}(H,k)\).

_Proof._ Let \(\varphi:V(G)\rightarrow V(H)\) be an isomorphism from _G_ to _H_. Write \(V(\mathcal{L}(G,k)):=V\unknown C\unknown W\unknown\{G_g,G_b\}\). For \(v\in V(G)\), we write \(\tilde{v}:=\varphi(v)\). For \(e\in\{u,v\}\), we write \(\tilde{e}:=\{\varphi(u),\varphi(v)\}\in E(H)\). Note that \(v\rightarrow\tilde{v}\) and \(e\rightarrow\tilde{e}\) both define one-to-one mappings between _V(G_) and _V(H_), and between _E(G_) and _E(H_), respectively. We define

\(\psi:V(\mathcal{L}(G,k))\rightarrow V(\mathcal{L}(H,k)),x\mapsto\left\{\begin{array}{ c c }
H_g & \text{if}x=G_g \\
H_b & \text{if}x=G_b \\
\tilde{v}^{(i)} & \text{if}x=v^{(i)} \\
c_\tilde{v}^{(i)} & \text{if}x=c_v^{(i)} \\
\tilde{e}_\tilde{v}^{(i)} & \text{if}x=e_v^{(i)} \\
\tilde{e}_b^{(i)} & \text{if}x=e_b^{(i)}
\end{array}\right..\)

We show that \(\psi\) defines an isomorphism. First, note that \(\psi\) is a bijection. Let us show that \(\{x,y\}\in E(\mathcal{L}(G,k))\) if and only if \(\{\psi(x),\psi(y)\}\in E(\mathcal{L}(H,k))\). By construction we already know that |_E_(L(_G,k_))|=|_E_(L(_H,k_))|, thus it is actually enough to show that \(\{x,y\}\in E(\mathcal{L}(G,k))\) implies \(\{\psi(x),\psi(y)\}\in E(\mathcal{L}(H,k))\).<sup>37</sup>

We consider a case distinction.

• Case _x=G<sub>b</sub>_ or _y=G<sub>b</sub>_: Without loss of generality, we assume _x=G<sub>b</sub>_. If \(\{G_b,y\}\in\mathcal{L}(G,k)\) then either _y=G<sub>g</sub>_ or _y=v_<sup>(_i_)</sup> thus \(\{H_g,\psi(y)\}\in E(\mathcal{L}(H,k))\).<tbc>

• Case (_x=G<sub>g</sub>_ or _y=G<sub>g</sub>_) and \(x\neq G_b\) and \(y\neq G_b\): Without loss of generality, we assume _x=G<sub>g</sub>_. If \(\{G_g,y\}\in\mathcal{L}(G,k)\) then \(y=e_g^{(i)}\) thus \(\{\psi(G_g),\psi(y)\}=\{H_g,\tilde{e}_g^{(i)}\}\in E(\mathcal{L}(H,k))\).<tbc>

• Case \(x,y\in V\unknown C\unknown W\) and \((x\in V\) , \(y\in C\) or \(x\in C\), \(y\in Y\) ): Without loss of generality, we assume _x=v_<sup>(_i_)</sup> and \(y=c_u^{(j)}\) for some \(u,v\in V\) and \(i,j\in[k]\). If \(\{v^{(i)},c_u^{(j)}\}\in\mathcal{L}(G,k)\) then _v=u_ and _i=j_. Thus, \(\{\psi(x),\psi(y)\}=\{\tilde{v}^{(i)},c_\tilde{v}^{(i)}\}\in\mathcal{L}(H,k)\).<tbc>

• Case \(x,y\in V\unknown C\unknown W\) and \((x\in V\) , \(y\in W\) or \(x\in W\), \(y\in V\) ): Without loss of generality, we assume _x=v_<sup>(_i_)</sup> and \(y=e_c^{(j)}\) for some \(v\in V\) , \(e=\{a,b\}\in E(G)\) and \(i,j\in[k]\). If<tbc>

<sup>37</sup>This implies that the mapping \(\psi_E:E(\mathcal{L}(G,k))\rightarrow E(\mathcal{L}(H,k)),\{x,y\}\mapsto\{\psi(x),\psi(y)\}\) is well-defined. Further, \(\psi_E\) is injective since \(\psi\) is. Lastly, |_E_(L(_G,k_))|=|_E_(L(_H,k_))| yields that \(\psi_E\) is a bijection and thus \(\psi\) is an isomorphism.

