approximation, but study an instance of a problem that cannot be expressed as a linearly separable convex program, which shows that structure of the sort that we use is necessary.

A line of work \[KPRU14, RR14, CKRW14, HHR<sup>+</sup>14, HHRW14, RRUW15\] has studied protocols for implementing outcomes in various settings under the constraint of joint differential privacy \[DMNS06, KPRU14\], which allows _n_ parties to jointly implement some solution while ensuring that no coalition of parties can learn much about the input of any party outside the coalition. Most (but not all) of these algorithms are actually private coordination protocols of the sort we study here, in which the algorithm can be viewed as a coordinator who is constrained to broadcast a private signal. These jointly private algorithms are not constrained to transmit a short signal - and indeed, the private signals can sometimes be verbose. But as we show, problems with low coordination complexity also have good jointly differentially private algorithms, which was one of our original motivations for studying this quantity.

Lykouris, Syrgkanis, and Tardos \[LST15\] show that the existence of a jointly differentially private algorithm for solving an optimization problem implies that the strategic variant of the problem has a low "price of anarchy" for learning agents, even in dynamic settings, in which player types change over time, as long as the game is smooth. Because we show in Section 5 that any problem with a low sensitivity objective and low coordination complexity has a good jointly differentially private algorithm, using the results of \[LST15\], to prove a bound on the price of anarchy in a smooth dynamic game, we show it suffices to bound the coordination complexity of the game.

## 2 Preliminaries

A _coordination problem_ is defined by a set of _n_ agents, a data domain X, an action range A, and a social objective function \(S:\mathcal{X}^n\times\mathcal{A}^n\rightarrow\mathbb{R}\). An _instance_ of a coordination problem consists of a set of _n_ elements from the data domain: \(D=(D^{(1)},\dots,D^{(n)})\in\mathcal{X}^n\). Each agent _i_ has knowledge only of _D_<sup>(_i_)</sup>, his own portion of the problem instance, and the goal is for a centralized _coordinator_ to broadcast a concise message to the agents to allow them to arrive at a solution \(a=(a_1,\dots,a_n)\in\mathcal{A}^n\) that approximately maximizes the objective function _S(D,a_).

A _coordination protocol_ consists of two functions, an _encoding function_ \(\sigma:\mathcal{X}^n\rightarrow\{0,1\}^*\) and a _decoding function_ \(\pi:\mathcal{X}\times\{0,1\}^*\rightarrow\mathcal{A}\). A coordination protocol \((\sigma,\pi)\) proceeds in two stages:

• First the coordinator broadcasts the message \(\sigma(D)\) to all agents using the encoding function.<tbc>

• Then each agent selects an action _a<sub>i</sub>_ on the basis of her own portion of the problem instance and the broadcast message, using the decoding function: \(a_i:=\pi(D^{(i)},\sigma(D))\).

Both functions \(\sigma\) and \(\pi\) may be randomized. The approximation ratio of a protocol is the ratio of the optimal objective value to the expected objective value of the solution induced by the protocol, in the worst case over problem instances.

**Definition 1** (Approximation Ratio)**.** _A coordination protocol_ \((\sigma,\pi)\) _obtains a_ \(\rho\) _approximation to a problem if:_

\(max_{D\in\mathcal{X}^n}\frac{\mathrm{OPT}(D)}{\mathbb{E}_{a_1,\dots,a_n}\left[S(D,a)\right]}\le\rho\)

_where each_ \(a_i=\pi(D^{(i)},\sigma(D))\)_, and the expectation is taken over the randomness of_ \(\sigma\) _and_ \(\pi\).

The coordination complexity of a protocol is the maximum number of bits the encoding function broadcasts, in the worst case over problem instances.

