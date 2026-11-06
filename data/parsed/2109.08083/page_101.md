<tbc>which by (6.14) gives

\(f_v(E_{G[V(G)\backslash V(M)]}(v,S_1,S_2,S_3))=\sum_{e\in E_G(v,S_1,S_2,S_3)}f_v(e)\prod_{u\in e\backslash\{v\}}(1-d_{w,G}(u))\)<br>
\(\pm\Delta^{-\epsilon}\big(\sum_{u\in V(G)}q^{(1)}(u)d_{w,G}(u)+\sum_{\bar{v}\in\genfrac(){pt}{2}{V(G)}{2}}q^{(2)}(\bar{v})\prod_{u\in\bar{v}}d_{w,G}(u)\)<br>
\(+\sum_{\bar{v}\in\genfrac(){pt}{2}{V(G)}{3}}q^{(3)}(\bar{v})\prod_{u\in\bar{v}}d_{w,G}(u)\big).\)

Noting that \(q^{(l)}(\bar{v})\prod_{u\in\bar{v}}d_{w,G}(u)\) is only non-zero for _O_(|_E<sub>G</sub>(v,S_<sub>1</sub>_,S_<sub>2</sub>_,S_<sub>3</sub>)|) ele ments \(\bar{v}\in\genfrac(){pt}{2}{V(G)}{l}\) for every \(l\in[3]\) and that \(d_{w,G}(u)\le 1\) for every \(u\in V(G)\) completes the proof. □

## 6.3.1.3. _Number of zero-sum configurations._

We wish to run counts on specific types of zero-sum configuration for the weight shuffle. Now, just as with degree- type properties, where we were interested in counting the number of edges relating in some way to specific subsets of the vertex set, we shall wish to do the same for zero-sum configurations containing some fixed edge _e_. Define

\(f_{Z_{i,e,G}^\pm(\alpha,\beta,\gamma)}^{(l)}(\bar{v}):=\left\{\begin{array}{ c c }
\sum_{z\in Z_{i,e,G}^\pm(\alpha,\beta,\gamma)}\unknown_{\{\bar{v}\subseteq z\}} & \text{for}\bar{v}\cap e=\emptyset, \\
0 & \text{otherwise,}
\end{array}\right.\)

for \(l\in[12]\), so that \(f_{Z_{i,e,G}^\pm(\alpha,\beta,\gamma)}^{(l)}(\bar{v})\) considers all \(z\in Z_{i,e,G}^\pm(\alpha,\beta,\gamma)\) which contain \(\bar{v}\in\genfrac(){pt}{2}{V(G)}{l}\) and _e_, where \(\bar{v}\) is disjoint from _e_. Note that a zero-sum configuration contains 12 vertices other than those in the given edge _e_ so, given a matching _M_ such that \(e\cap V(M)=\emptyset\), counting the number of zero-sum configurations from \(Z_{i,e,G}^\pm(\alpha,\beta,\gamma)\) remaining in _G_\\_V(M_) is an inclusion-exclusion sum over 12 different tuples. Following the strategy used in Section 6.3.1.2 to get counts for degree-type properties, and assuming that (6.1) is satisfied for all twelve functions, we obtain that

\(|Z_{i,e,G[V(G)\backslash V(M)]}^\pm(\alpha,\beta,\gamma)|=\sum_{z\in Z_{i,e,G}^\pm(\alpha,\beta,\gamma)}\prod_{u\in z\backslash e}(1-d_{w,G}(u))\)<br>
\(\pm O\left(\Delta^{-\epsilon}|Z_{i,e,G}^\pm(\alpha,\beta,\gamma)|max_{u\in\bigcup Z_{i,e,G}^\pm(\alpha,\beta,\gamma)}d_{w,G}(u)\right).\)

**6.3.2. Reachability.** Recall from Section 6.2, just above Theorem 6.12, the notion of open and closed permissible pairs and tuples, a restriction of open and closed valid pairs and tuples. A key aspect of our strategy and the vortex of nested subgraphs to reach _L_<sup>∗</sup> relies on, at step _i_, being able to obtain a matching that ensures that every vertex outside _I_<sub>_t<sub>i</sub>_+1</sub> has been matched. In the process of doing this we shall also inevitably match some vertices from within _I_<sub>_t<sub>i</sub>_+1</sub>. However, having reached (_H_<sub>1<sup>∗</sup></sub>_,w_<sub>1<sup>∗</sup></sub>), in any subgraph of _H_<sub>1<sup>∗</sup></sub>\[_I<sub>t<sub>i</sub></sub>_\] (for some _i_), in order to match all vertices outside _I_<sub>_t<sub>i</sub>_+1</sub>, given that T\[_I<sub>t<sub>i</sub></sub>_\] has depth _j_, it follows that we do not need to use any vertices inside _K_<sub>_j_+1</sub>. In particular, any edge that uses vertices inside _K_<sub>_j_+1</sub> will not be covering any vertices outside _I_<sub>_t<sub>i</sub>_+1</sub>. Since we are trying to preserve vertices closer to the centre of T for as long as possible, it would be a waste to remove an edge containing a vertex inside _K_<sub>_j_+1</sub> at a step in the process

