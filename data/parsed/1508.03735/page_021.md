**Algorithm 5** BR-\(\text{Sim}((G,\{(s_i,d_i)\}_{i\in[n]},c),\alpha,r)\)

**Input:** a routing game instance \((G,\{(s_i,d_i)\}_{i\in[n]},c)\), best-response parameter \(\alpha\) and refinement parameter _r_ such that \(\alpha>2\lambda m(r+1)\)

**Initialize:**

\(l=\alpha-2\lambda mr-\lambda m,T=\frac{mn}{l}\)

**for** each edge \(e\in E\)

Let Counter(_e_) be an instantiation of \(\text{ApproxCount}(\cdot,r,(T+1)n)\) (waiting for incoming stream)

**Form the initial flow:**

**for** each player _i_:

Let _f_<sup>(_i_)</sup> be the _s<sub>i</sub>_-_d<sub>i</sub>_ path _P_<sup>(_i_)</sup> with the fewest number of edges, break ties lexicographically

**for** each edge _e_:

**if** \(e\in P^{(i)}\) send "1" to Counter(_e_) **else** send "0" to Counter(_e_)

**Best-responses dynamics:**

**for** _t_=1_,...,T_

**if** each player is playing an \(\alpha\)-best-response w.r.t. the counts \(\{\text{Counter}(e)\}_{e\in E}\): Halt

**for** each player _i_

**if** _i_ is not playing an \(\alpha\)-best-response w.r.t. the flow \(\{\text{Counter}(e)\}_{e\in E}\)

Let \(\widehat{f}^{(i)}\) be the best-response of _i_ w.r.t. \((\text{Counter}(e))_{e\in E}\) (breaking ties lexicographically)

**for** each _e_:

**if** \(e\in f^{(i)}\backslash\widehat{f}^{(i)}\): Send "-1" to Counter(_e_)

**if** \(e\in\widehat{f}^{(i)}\backslash f^{(i)}\): Send "1" to Counter(_e_)

**else** : Send "0" to Counter(_e_)

Let \(f^{(i)}=\widehat{f}^{(i)}\)

**else**:

**for** each _e_: Send "0" to Counter(_e_)

**for** each _e_: Let _U<sub>e</sub>_ be the output of Counter(_e_)

**Output:** \(\{U_e\}_{e\in E}\)

This allows us to bound the cost difference of the same path with respect to two flows _f_ and _g_ -- for any path \(P\subseteq E\)<tbc>

\(|c_P(f)-c_P(g)|\le\lambda mr.\)

<tbc>This implies<tbc>

\(|min_{P^\prime\in\mathcal{A}_i}c_{P^\prime}(f)-min_{P^\prime\in\mathcal{A}_i}c_{P^\prime}(g)|\le\lambda mr.\)

<tbc>Note that \(c_{f^{(i)}}(g)-min_{P^\prime\in\mathcal{A}_i}c_{P^\prime}(g)\le\eta\) by our assumption, then it follows from the last two inequalities that<tbc>

\(c_{f^{(i)}}(f)\le min_{P^\prime\in\mathcal{A}_i}c_{P^\prime}(f)+\eta+\lambda mr,\)

<tbc>so _f_<sup>(_i_)</sup> is a \((\eta+\lambda mr)\)-best-response w.r.t. the flow _f_. Let \(f'_i\) be a deviation of player _i_ and let \(f'=(f'_i,f^{(-i)})\) be the resulting flow. We know that for each edge _e_, \(|f'_e-f_e|\le 1\). It follows that<tbc>

\(min_{P^\prime\in\mathcal{A}_i}c_{P^\prime}(f)\le min_{P^\prime\in\mathcal{A}_i}c_{P^\prime}(f')+\lambda m.\)

