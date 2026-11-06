length at most

\(O\left(\frac{m^2n}{(\varepsilon-3\lambda mr-2\lambda m)r}log\left(\frac{m^2n^2}{l}\right)\right)=\widetilde{O}\left(\frac{\lambda m^3n}{(\varepsilon-2\lambda m)^2}\right)\)

which recovers our stated bound.

To interpret the bound in Theorem 7, consider the case in which the routing game is a _large game_ - in which _n_ is substantially larger than the number of edges _m_, and in which no player has a large influence on the latency of any single edge. In our context, this means the Lipschitz parameter \(\lambda\) of the cost function _c<sub>e</sub>_ is small. Since the range of the cost is normalized to lie between 0 and 1, it is reasonable to assume that \(\lambda=O(1/n)\). Given such a largeness assumption, the result of Theorem 7 gives a coordination protocol that coordinates a (_m/n_)-approximate equilibrium flow with a coordination complexity of \(\widetilde{O}(m^3/\varepsilon^2)\) for any constant \(\varepsilon\).

**Remark 2.** _Another application for this coordination technique is the general allocation problem when the players have_ gross substitutes _preferences. In this problem, there are n players and m types of goods, and each type of good has a supply of s. A coordinator who knows the preferences of the players can first simulate m simultaneous ascending price auctions, one for each type of good. The analysis of [KC82] shows that the prices and the allocation in the auctions converge to_ Walrasian equilibrium: _each buyer is simultaneously able to buy his most preferred bundle of goods under the set of prices. We could then have a similar coordination protocol: compress an approximate version of the ascending auctions dynamics using_ ApproxCount_, and broadcast a message that allows each player to reconstruct the price trajectory in the auctions, which can then coordinate a high-welfare allocation._

