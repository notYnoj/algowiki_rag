The next lemma determines the largest possible decrease in cut value caused by flipping both endpoints of an edge. This bounds the term c_<sub>G</sub>(y_)-c_<sub>G</sub>(T<sub>e</sub>y_) in the correlator’s Laurent exponents.

**Lemma 2.3** (Largest cut decrease)**.** _For every edge e_={_u,v_} _of a simple graph, let d<sub>u</sub> and d<sub>v</sub> denote the degrees of u and v, respectively. Then_

\(R_e=d_u+d_v-2.\) (20)

_Proof._ Only edges incident on exactly one endpoint can change when both endpoints are flipped, so \(R_e\le d_u+d_v-2\). Equality is attained by assigning the same spin to _u,v_ and the opposite spin to every other neighbor of either endpoint. This assignment is consistent even when _u_ and _v_ have common neighbors, since every vertex in \((N(u)\cup N(v))\backslash\{u,v\}\) receives the same spin opposite to _u_ and _v_.

For the anchor edge _e<sub>⋆</sub>_={_r,s_} of _G_=G(_H_), both endpoints are universal and therefore<tbc>

\(R_{e_\star}=2N-4.\) (21)

<tbc>The only assignments attaining _R<sub>e<sub>⋆</sub></sub>_ are<tbc>

\((q_\sigma)_r=(q_\sigma)_s=\sigma,(q_\sigma)_w=-\sigma(w\in W),\sigma\in\{\pm 1\},\) (22)

<tbc>for which \(T_{e_\star} q_\sigma=-\sigma\mathbf{1}\). Since every nonanchor vertex has degree strictly less than _N_-1, _e<sub>⋆</sub>_ uniquely maximizes _R<sub>e</sub>_ among all edges. Using \(c_G(x)\le\mathrm{MC}(G)\), \(c_G(t)\ge 0\), and \(R_e\le R_{e_\star}\), the exponent in (16) satisfies<tbc>

\(c_G(x)-c_G(t)+\left(c_G(y)-c_G(T_ey)\right)\le\mathrm{MC}(G)+R_e\le\mathrm{MC}(G)+2N-4.\)

<tbc>Hence every exponent in (16) is at most<tbc>

\(D_\star=\mathrm{MC}(G)+2N-4.\) (23)

<tbc>Since each summand is bounded independently, attaining the upper bound requires _c<sub>G</sub>(x_)=MC(_G_), _c<sub>G</sub>(t_)=0, and _c<sub>G</sub>(y_)-_c<sub>G</sub>(T<sub>e<sub>⋆</sub></sub>y_)=_R<sub>e<sub>⋆</sub></sub>_. Since _G_=G(_H_) is connected, its only zero-cut assignments are the two constant assignments. Hence at equality, necessarily<tbc>

\(x\in\#\mathrm{MC}(G),t=\tau\mathbf{1},\tau\in\{\pm 1\},y\in\{q_+,q_-\}.\) (24)

<tbc>By Lemma 2.1, each \(x\in\#\mathrm{MC}(G)\) is balanced on _W_ and separates the anchors. Consequently

\(d_{Hamm}(x,q_\sigma)=1+\frac{|W|}{2}=\frac{N}{2},\) (25)

independently of _x_ and \(\sigma\).<br>
At the chosen mixer angle, the coefficient of the highest power present in the Laurent polynomial determines the number of maximum cuts.

**Theorem 2.4** (Extreme-coefficient identity)**.** _Recall D<sub>⋆</sub>_:=MC(_G_)+2_N_-4 _as in Eq._ (23)_. Write_<tbc>

\(H_{e_\star}(z;\beta)=\sum_{k\in\mathbb{Z}}a_k(\beta)z^k.\) (26)

<tbc>_For G_=G(_H), we have_ \(a_k(\beta)=0\) _for every k\>D<sub>⋆</sub>, and the coefficient at D<sub>⋆</sub> is_<tbc>

\(a_{D_\star}(\beta)=-2^{1-N}|\#\mathrm{MC}(G)|c^{N/2}(\mathrm{i}\mathrm{s})^{N/2}\left[c^N+(-\mathrm{i}\mathrm{s})^N\right],\) (27)

