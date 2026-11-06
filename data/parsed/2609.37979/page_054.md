\(\{v^{(i)},e_c^{(j)}\}\in\mathcal{L}(G,k)\) then _v=c_, _i=j_ and either _a=v_ or _b=v_. Thus, \(\{\psi(x),\psi(y)\}=\{\tilde{v}^{(i)},\tilde{e}_\tilde{v}^{(i)}\}\in\mathcal{L}(H,k)\).<tbc>

• Case \(x,y\in V\unknown C\unknown W\) and \(x\in C\) and \(y\in C\): Without loss of generality, we assume \(x=c_v^{(i)}\) and \(y=c_u^{(j)}\) for \(u,v\in V\) and \(i,j\in[k]\). If \(\{c_v^{(i)},c_u^{(j)}\}\in\mathcal{L}(G,k)\) then _u=v_ and either _j=i_+1 or _i=j_+1. Without loss of generality, assume _j=i_+1, now \(\{\psi(x),\psi(y)\}=\{c_\tilde{v}^{(i)},c_\tilde{v}^{(i+1)}\}\in\mathcal{L}(H,k)\).<tbc>

• Case \(x,y\in V\unknown C\unknown W\) and \(x\in E\) and \(y\in E\): Without loss of generality, we assume \(x=e_c^{(i)}\) and \(y=d_{c^\prime}^{(j)}\) for some \(e,d\in E(G),i,j\in[k]\). If \(\{e_c^{(i)},d_{c^\prime}^{(j)}\}\in\mathcal{L}(G,k)\) then _e=d_ and _i=j_ and \(c\neq c'\). Thus, \(\{\psi(x),\psi(y)\}=\{\tilde{e}_c^{(i)},\tilde{e}_{c^\prime}^{(i)}\}\in\mathcal{L}(H,k)\).<tbc>

• Otherwise: In all remaining cases we have \(x,y\in V\unknown C\unknown W\) with \(\{x,y\}\notin E(\mathcal{L}(G,k))\). For example, if \(x,y\in V\) then \(\psi(x)=\tilde{v}^{(i)}\) and \(\psi(x)=\tilde{u}^{(j)}\) for \(v,u\in V\) and \(i,j\in[k]\). Note that \(\{\tilde{v}^{(i)},\tilde{u}^{(j)}\}\notin E(\mathcal{L}(H,k))\).

This shows that \(\psi\) is an isomorphism which proves that lemma.

We extend Lovász’s construction by handling even values of _k_ and conclude a isomorphism- preserving reduction to 3-Coloring.

**Lemma 9.22.** Coloring \(\le_p^\cong 3\)-Coloring.

_Proof._ We first define a helper function \(A:\mathcal{G}\rightarrow\mathcal{G}\) that takes as input an graph _G_ and outputs a graph \(G'\) that is obtained by adding a new vertex _x_ to _V(G_) and connecting _x_ to all vertices in _G_. Observe that _A(G_) is computable in time _O_(|_V(G_)|+|_E(G_)|). Further, note that _A(G_) is (_k_+1)-colorable if and only if _G_ is _k_-colorable. Also note that \(G\cong H\) if and only if \(A(G)\cong A(H)\). Next, we define

\(f:\mathcal{G}\times\mathbb{N}_{\ge 3}\rightarrow\mathcal{G},(G,k)\mapsto\left\{\begin{array}{ c c }
\mathcal{L}(G,k) & \text{if}k\text{is odd} \\
\mathcal{L}(A(G),k+1) & \text{if}k\text{is even}
\end{array}\right..\)

We show that _f_ defines a polynomial time many-one reduction from Coloring to 3-Coloring is isomorphism-preserving. First, observe that _f_ is polynomial time computable due to Lemma 9.19. Next, let _G_ be a graph and _k_ be a number, we show \((G,k)\in\text{Coloring}\) if and only if \(f(G,k)\in 3\)-Coloring. If _k_ is odd then this directly follows from Lemma 9.19. If _k_ is even then _G_ is _k_-colorable if and only if _A(G_) is (_k_+1)-colorable. Now, Lemma 9.19 yields that _A(G_) is (_k_+1)-colorable if and only if L(_A(G),k_+1) is 3-colorable, proving the claim.

Lastly, we show that _f_ is isomorphism-preserving. To this end, let \(k\ge 3\) be an integer and _G,H_ be graphs with \(G\cong H\). If _k_ is odd then Lemma 9.21 implies \(f(G,k)\cong f(H,k)\). If _k_ is even then we obtain \(A(G)\cong A(H)\). Again, Lemma 9.21 yields \(f(G,k)\cong f(H,k)\), proving the lemma.

## 9.4.2 Reduction from 3-Coloring to 3-SAT

We give an isomorphism-preserving reduction from 3-Coloring to 3-SAT.

**Lemma 9.23.** 3-Coloring \(\le_p^\cong 3\)-SAT.

_Proof._ We define a polynomial-time, isomorphism-preserving many-one reduction from 3-Coloring \(\le_p^\cong 3\)-SAT.

