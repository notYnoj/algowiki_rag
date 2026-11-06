Therefore, \(c_{f^{(i)}}(f)\le min_{P^\prime\in\mathcal{A}_i}c_{P^\prime}(f')+\eta+\lambda mr+\lambda m\), which guarantees that _f_<sup>(_i_)</sup> is a \((\eta+\lambda mr+\lambda m)\)- best-response.

**Lemma 15.** _Every time a player makes a deviation in the dynamics, the potential function_ \(\Psi\) _decreases by at least_ \((\alpha-2\lambda mr-\lambda m)\).

_Proof._ Let _f_ denote the true flow among the _n_ players. Since the amount the potential function decreases equals the amount that player decreases her cost, we can bound \(c_{f^{(i)}}(f)-c_{\widehat{f}^{(i)}}(f')\), where \(f'=(\widehat{f}^{(i)},f^{(-i)})\). Let _g_ denote the count vector given by the counters \((\text{Counter}(e))_{e\in E}\). Suppose a player _i_ has her path switched from _f_<sup>(_i_)</sup> to \(\widehat{f}^{(i)}\) during the dynamics. Then this means<tbc>

\(min_{P\in\mathcal{A}_i}c_P(g)=c_{\widehat{f}^{(i)}}(g)\le c_{f^{(i)}}(g)-\alpha.\)

<tbc>By the accuracy guarantee of Claim 4,<tbc>

\(|c_P(f)-c_P(g)|\le\lambda mr\text{and}\left|min_{P^\prime\in\mathcal{A}_i}c_{P^\prime}(f)-min_{P^\prime\in\mathcal{A}_i}c_{P^\prime}(g)\right|\le\lambda mr.\)

<tbc>This means<tbc>

\(|c_{f^{(i)}}(g)-c_{f^{(i)}}(f)|\le\lambda mr\text{and}|c_{\widehat{f}^{(i)}}(g)-c_{\widehat{f}^{(i)}}(f)|\le\lambda mr.\)

<tbc>Furthermore, note that \(|f_e-f'_e|\le 1\) for each edge _e_ since they differ by only player _i_’s path, so<tbc>

\(|c_{\widehat{f}^{(i)}}(f')-c_{\widehat{f}^{(i)}}(f)|\le\lambda m.\)

<tbc>Combining all the inequalities above we get

\(c_{f^{(i)}}(f)-c_{\widehat{f}^{(i)}}(f')=(c_{f^{(i)}}(f)-c_{f^{(i)}}(g))+(c_{f^{(i)}}(g)-c_{\widehat{f}^{(i)}}(g))\)<br>
\(+(c_{\widehat{f}^{(i)}}(g)-c_{\widehat{f}^{(i)}}(f))+(c_{\widehat{f}^{(i)}}(f)-c_{\widehat{f}^{(i)}}(f'))\)<br>
\(\ge-\lambda mr+\alpha-\lambda mr-\lambda m=\alpha-2\lambda mr-\lambda m,\)

which also lower bounds the amount that the potential function decreases.

**Lemma 16.** _At the end of the best-response dynamics, the players are playing_ \((\alpha+\lambda mr+\lambda m)\)_-approximate equilibrium flow in the routing game instance._

_Proof._ In each iteration, there is at least one player performing a deviation, which will decrease the potential function by at least \((\alpha-2\lambda mr-\lambda m)=l\).

Note that the initial flow has potential

\(\Psi(f)\equiv\sum_{e\in E}\sum_{i=1}^{f_e}c_e(i)\le nm.\)

This means after at most _T=mn/l_ iterations of the best-response dynamics, every player is playing \(\alpha\)- best-response with respect to the flow given by \((\text{Counter}(e))_{e\in E}\). By Lemma 14, each player is playing a \((\alpha+\lambda mr+\lambda m)\)-best-response w.r.t. to the final flow _f_. Hence, the final flow is an \((\alpha+\lambda mr+\lambda m)\)- equilibrium flow.

