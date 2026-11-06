The classical work of \[MS96\] establishes the existence of equilibrium flows and shows that an equilibrium flow minimizes the _potential function_ \(\Psi\) of the routing game, which is defined as

\(\Psi(f)\equiv\sum_{e\in E}\sum_{i=1}^{f_e}c_e(i).\)

Note that in atomic routing games, equilibrium flows are not unique, and so equilibrium selection is important. This motivates the coordination problem we study.

We will rely on the following fact to show that a flow is an approximate equilibrium.

**Fact 1.** _Consider a flow_ \(f\in\mathcal{F}\)_. Suppose a player i could decrease her cost by deviating from path P to path_ \(\widetilde{P}\)_, which gives rise to a new flow_ \(\widetilde{f}\)_, then_

\(c_P(f)-c_\widetilde{P}(\widetilde{f})=\Psi(f)-\Psi(\widetilde{f}).\)

Our goal is to give a coordination protocol that coordinates the players to play an approximate equilibrium flow and has low coordination complexity (scaling with the number of edges |_E_| instead of number of players _n_).<sup>6</sup> A very straightforward procedure to compute an equilibrium flow is the _best-response dynamics_: while the flow _f_ is not a \(\eta\)-equilibrium flow, pick a player _i_ and an arbitrary path deviation that could decrease her cost. In our coordination protocol, the coordinator will first simulate an approximate version of the best-response dynamics, and compress the dynamics into a concise string using the subroutine ApproxCount; then the coordinator will broadcast the string to the players so that each player can simulate the sequence of actions she would have played in the dynamics, and thus determine the action she plays at the end of the dynamics using ExtractCount.

In our approximate best-response dynamics, we will let the players best-respond to the approximate count of players on the edges. We first need to define the a player’s best response with respect to a count vector in R_<sup>m</sup>_.

**Definition 8** (Best-Response with respect to counts)**.** _Given a count vector_ \(f^\bullet\in\mathbb{R}^{|E|}\)_, a path P_<sup>(_i_)</sup> _for player i is an_ \(\varepsilon\)_-best-response with respect to the vector_ \(f^\bullet\) _if_

\(c_{P^{(i)}}(f^\bullet)-\varepsilon\le min_{\widetilde{P}^{(i)}\in\mathcal{A}_i}c_{\widetilde{P}^{(i)}}(f^\bullet).\)

Keep in mind that any feasible flow _f_ is also a count vector. We give the formal description of the coordinator’s encoding function BR-Sim in Algorithm 5.

We will now focus on analyzing the best-response dynamics within BR-Sim. Note that in the analysis we might say "player plays best-response" or "player deviates"; while these sound natural, all these procedures are simulated by the coordinator and the protocol is non-interactive.

**Lemma 14.** _At any moment of the dynamics, let_ \(f\in\mathbb{R}^{|E|}\) _be the flow given by all players’ paths and let_ \(g\in\mathbb{R}^{|E|}\) _be the count vector given by the counters_ \(\{\mathsf{Counter}(e)\}_{e\in E}\)_. Suppose that player i’s path f_<sup>(_i_)</sup> _is an_ \(\eta\)_-best-response with respect to g, then the path f_<sup>(_i_)</sup> _is an_ \((\eta+\lambda mr+\lambda m)\)_-best-response._

_Proof._ By Claim 4, we guarantee that throughout the dynamics, for each \(e\in E\)<tbc>

\(|\mathsf{Counter}(e)-f|\le r.\)

<sup>6</sup>The social objective here is not social welfare -- we want instead to minimize approximation factor of the equilibrium \(\varepsilon\).

