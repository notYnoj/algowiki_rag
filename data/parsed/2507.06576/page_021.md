<tbc>Since<tbc>

\(\sum_{F^\prime\in\mathcal{F}_{2w}(G^{S(L^\prime)})}x_{F^\prime}=\sum_{F^\prime\in\mathcal{F}_{2w}^w(G^{S(L^\prime)})}x_{F^\prime}=1,\)

<tbc>it follows that some \(F'\in\mathcal{F}_{2w}^w(G^{S(L^\prime)})\) with \(x_{F^\prime}>0\) must appear at least twice in the expansion (14).<br>
Concretely, there exist distinct indices \(j_1,j_2\in\{1,\dots,t\}\) such that<tbc>

\(F_{j_1}=F'\cap E(H_{j_1})\in\mathcal{F}_{2w}^w(H_{j_1})\backslash\mathcal{F}_1^{j_1},F_{j_2}=F'\cap E(H_{j_2})\in\mathcal{F}_{2w}^w(H_{j_2})\backslash\mathcal{F}_1^{j_2}.\)

<tbc>The first condition implies that in _H_<sub>_j_<sub>1</sub></sub>\\_F_<sub>_j_<sub>1</sub></sub> there exists a vertex \(v_1\in V(G_1^{j_1})\) such that \(d_{H_{j_1}}(r_1,v_1)\ge w\). As mentioned earlier, we also have \(d_{G^{S(L^\prime)}}(r_1,v_1)\ge w\). Similarly, from the second condition there exists \(v_2\in V(G_1^{j_2})\) with \(d_{G^{S(L^\prime)}}(r_1,v_2)\ge w\). Therefore, in \(G^{S(L^\prime)}\backslash F'\) the vertices _v_<sub>1</sub>_,v_<sub>2</sub>_,r_<sub>1</sub> all lie in the same connected component. Moreover, since _r_<sub>1</sub> is a cut vertex separating _v_<sub>1</sub> and _v_<sub>2</sub>, we have

\(d_{G^{S(L^\prime)}}(v_1,v_2)=d_{G^{S(L^\prime)}}(r_1,v_1)+d_{G^{S(L^\prime)}}(r_1,v_2)\ge 2w.\)

This contradicts the assumption that \(F'\in\mathcal{F}_{2w}^w(G^{S(L^\prime)})\).<br>
Hence, our initial assumption that the optimal value _z_ of LP (9) is positive must be false. Therefore, the optimal value is _z_=0, completing the proof.

We work in the same regime as before, where _w_ is an even integer. For the remainder, set \(k=\frac{w}{2}\) and fix a small constant \(\epsilon>0\). Choose a cactus \(H'\in\mathcal{G}\) and a distinguished vertex \(r'\in V(H')\) such that

\(\mathrm{max}_{y\text{is an}SDD(H^\prime,2w,p,r^\prime)}\left\{\sum_{F\in\mathcal{F}_{2w}^k(H^\prime,r^\prime)}y_F\right\}<R_{(\mathcal{G},2w,p)}^k+\epsilon.\) (15)

Now, considering this extremal pair \((H',r')\), we replace the two paths used in Theorem 6 with copies of \(H'\) attached at the cycle vertices _u_<sub>1</sub> and _u_<sub>2</sub> (via the distinguished vertices \(r'_1,r'_2\) of the copies). In other words, we work with the graph obtained by taking the 1-sum of the cycle and two disjoint copies of \(H'\) at _u_<sub>1</sub> and _u_<sub>2</sub>.

**Theorem 8.** _Let_ G _be the family of cactus graphs. If_ G _is strongly SDD_(2_w,p)-acceptable, then_ \(w\cdot p\ge\frac{8}{7}-\frac{4\epsilon}{7}\) .

_Proof._ Let _H_ be a cycle of length 2_w_. Let \(r,u_1,\tilde{r},u_2\) be four vertices of the cycle in anticlockwise order, such that \(d(r,u_1)=d(u_1,\tilde{r})=d(\tilde{r},u_2)=d(u_2,r)=\frac{w}{2}\) . Let \(H'_1,H'_2\) be two copies of \(H'\) with corresponding distinguished vertices \(r'_1,r'_2\). Set<tbc>

\(G=H^S\big(\{(u_1,(H'_1,r'_1)),(u_2,(H'_2,r'_2))\}\big).\)

<tbc>Then \(G\in\mathcal{G}\). Denote by _P_<sub>_u_<sub>1</sub></sub> the path of length \(\frac{w}{2}\) from _r_ to _u_<sub>1</sub>, by _P<sub>a</sub>_ the path from _u_<sub>1</sub> to \(\tilde{r}\), by _P<sub>b</sub>_ the path from \(\tilde{r}\) to _u_<sub>2</sub>, and by _P_<sub>_u_<sub>2</sub></sub> the path from _u_<sub>2</sub> to _r_. See Figure 7 for an illustration:<tbc>

