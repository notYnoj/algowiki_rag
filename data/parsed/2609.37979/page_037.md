**Definition 8.9** (Homomorphism of attributed Graphs)**.** Let

\(G=(V_G,E_G,\alpha_G^V,\alpha_G^E)\text{and}H=(V_H,E_H,\alpha_H^V,\alpha_H^E)\)

be two graphs, where _V<sub>G</sub>,V<sub>H</sub>_ are vertex sets, _E<sub>G</sub>,E<sub>H</sub>_ are edge sets, and \(\alpha^V,\alpha^E\) assign attributes from alphabets \(\Sigma_V,\Sigma_E\) to the vertices and edges, respectively.

We say that a function \(f:V_H\rightarrow V_G\) is a _homomorphism_ from _H_ to _G_ if:

1. **Adjacency is preserved:** For all \((u,v)\in E_H\) it is true that \((\varphi(u),\varphi(v))\in E_G\).<tbc>

2. **Vertex attributes are preserved:** For all \(u\in H\) it is true that \(\alpha_H^V(u)=\alpha_G^V(f(u))\).<tbc>

3. **Edge attributes are preserved:** For all \((u,v)\in E_H\) it is true that \(\alpha_H^E(u,v)=\alpha_G^E(f(u),f(v))\).

We write \(\#\mathrm{Hom}(H\rightarrow G)\) for the number of homomorphism from _H_ to _G_.

Next, we use homomorphism to define a witness function. Note that each input graph _G_ has a length constraint _B_.

**Definition of a Witness:**

• \(W=\{X|X\subseteq\mathbb{N}_{\ge 1}\times\mathbb{R}_{\ge 0}\times\mathbb{R}_{\ge 0}\}\),<tbc>

• \(\mathrm{cost}(X)=\sum_{(n,c,\ell)\in X}n\cdot c\),<tbc>

• Let _P_ be a graph. We say that _P_ is a _X-colored s,t-path_ if<tbc>

– _P_ is a path with colored start-vertex _s_ and colored end-vertex _t_,<tbc>

– each edge in _P_ is colored with a color \((c,\ell)\), and<tbc>

**–** for each \((n,c,\ell)\in X\) the path _P_ contains exactly _n_ edges of color \((c,\ell)\).<tbc>

<tbc>Let _P<sub>X</sub>_:={_P|P_ is a _X_-colored _s,t_-path} be a set of paths then we define<tbc>

<tbc>\(\mathrm{check}(G,X)=\left\{\begin{array}{ c c }
\sum_{P\in P_X}\#\mathrm{Hom}(P\rightarrow G) & \text{if}\sum_{(n,c,\ell)\in X}n\cdot\ell\le B \\
0 & \text{otherwise}
\end{array}\right.,\)<tbc>

<tbc>where _B_ is length constraint of _G_.

**Lemma 8.10.** _The triple_ \((W,\mathrm{check}:\mathcal{G}\times W\rightarrow\mathbb{R},\mathrm{cost}:W\rightarrow\mathbb{R})\) _is a witness function of OPT._

_Proof._ We start by showing that for all \(X\in W\) with \(\sum_{(n,c,\ell)\in X}n\cdot\ell\le B\) we obtain

\(\mathrm{check}(G,X)=\#\{\text{walks in}G\text{from}s\text{to}t\text{s.t. for all}(n,c,\ell)\in X\text{the color}(c,\ell)\text{is used}n\text{times}\}.\) (3)

Let \(P\in P_X\) be a path. Since _P_ is a _X_-colored _s,t_-path, we obtain that _V(P_)={_v_<sub>1</sub>_,...,v<sub>t</sub>_} and _E(P_)={_e_<sub>1</sub>_,...e_<sub>_t_-1</sub>} with \(\alpha_P^V(v_1)=s\), \(\alpha_P^V(v_t)=t\) and \(\alpha_P^E(e_i)=(c_i,\ell_i)\). Now, \(\#\mathrm{Hom}(P\rightarrow G)\) is equal to the number of walks in _G_ that start at _s_, end at _t_, and where we used an edge of color \((c_i,\ell_i)\) during the _i_th step of the walk. Thus, equation (3) follows since check(_G,X_) computes the sum over all possible _X_-colored _s,t_-paths.

Next, we check that \((W,\mathrm{check}:\mathcal{G}\times W\rightarrow\mathbb{R},\mathrm{cost}:W\rightarrow\mathbb{R})\) is a witness function of _OPT_. For the first property, let \(G\in\mathcal{G}\), \(X\in W\) and assume that check(_G,X)\>_0. By (3), we obtain that there is walk from _s_ to _t_ that uses the colors _X_. This walk induces a path _P_ from _s_ to _t_ that is<tbc>

