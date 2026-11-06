**Theorem A.2** (Value-Determined Game in the Isomorphic-Priors Model)**.** _There is an algorithm that solves the Value-determined Game problem with k prior instances each having at most n vertices and m edges in O(k(n+m_)log_n_) _preprocessing time and O_((_n+m_)log_n_) _query time._

Similar to solving Energy Game in the Isomorphic-Priors setting, we only need to show that if two games are 1-WL equivalent, then the winning player is the same.

We initialize 1-WL with the vertex types and labels, and use transition probabilities as labels on edges leaving random nodes. All other edges receive a distinguished dummy label. Colors are compared using a common refinement scheme. Strategies may be history-dependent and randomized.

**Theorem A.3.** _Let G and_ \(G'\) _be two instances of Value-determined Games with the same Borel objective W. If_ \(G\equiv_{1\text{-WL}}G'\) _and_ \(\chi_\infty^G(v_0)=\chi_\infty^{G^\prime}(v'_0)\)_, then the winners of G and_ \(G'\) _are the same._

_Proof._ By symmetry, it suffices to show that the value of \(G'\) is at least the value of _G_. Fix an arbitrary strategy \(\sigma\) for Player 1 in _G_. For simplicity, we use _w_ for the label functions of both games.

For every pair of equally colored vertices \(u,u'\), fix a color-preserving bijection \(b_{u,u^\prime}:\mathrm{Succ}(u)\rightarrow\mathrm{Succ}(u')\). At random nodes, additionally require \(\delta(u)(v)=\delta'(u')\big(b_{u,u^\prime}(v)\big)\). Such bijections exist by Neighborhood Preservation, since the refinement also includes transition probabilities as edge labels.

Fix a common infinite random tape, viewed as a sequence \((U_k)_{k\ge 0}\) of independent uniform random variables on \[0,1\], independent of the players’ randomization. At corresponding random nodes \(u,u'\), order the successors of _u_ arbitrarily and order those of \(u'\) according to \(b_{u,u^\prime}\). At step _k_, both games use _U<sub>k</sub>_ to sample from the corresponding cumulative probability intervals. The two transitions then have the correct marginal distributions and lead to successors matched by \(b_{u,u^\prime}\). This random tape is used only for the coupling and is not observed by the players.

We define \(\sigma'\) dynamically by maintaining a simulated "shadow play" in _G_. Let the current finite prefix of a play in \(G'\) be \(\pi'=(v'_0,v'_1,\dots,v'_k)\) and the shadow play in _G_ be \(\pi=(v_0,v_1,\dots,v_k)\). We show by induction on _k_ that \(\chi_\infty^G(v_i)=\chi_\infty^{G^\prime}(v'_i)\) for all \(i\le k\).

_Base case._ For _k_=0, the claim holds by assumption.

_Inductive step._ Assume the claim holds for all \(i\le k\). Since \(v'_k\) and _v<sub>k</sub>_ have the same color, they have the same vertex type.

• If _v<sub>k</sub>_ and \(v'_k\) are Player 1 nodes, we first move the token in _G_: the strategy \(\sigma\) selects a successor _v_<sub>_k_+1</sub> according to \(\sigma(\pi)\). Then we move the token in \(G'\) to \(v'_{k+1}=b_{v_k,v_k^\prime}(v_{k+1})\). By the choice of the bijection, \(\chi_\infty^{G^\prime}(v'_{k+1})=\chi_\infty^G(v_{k+1})\).<tbc>

• If _v<sub>k</sub>_ and \(v'_k\) are Player 2 nodes, we first move the token in \(G'\): Player 2 selects an arbitrary successor \(v'_{k+1}\) of \(v'_k\). We then move the token in _G_ to \(v_{k+1}=b_{v_k,v_k^\prime}^{-1}(v'_{k+1})\). Again, \(\chi_\infty^G(v_{k+1})=\chi_\infty^{G^\prime}(v'_{k+1})\).<tbc>

• If _v<sub>k</sub>_ and \(v'_k\) are random nodes, the arena samples \(v'_{k+1}\sim\delta'(v'_k)\). Upon observing \(v'_{k+1}\), the strategy \(\sigma'\) appends to the shadow play the vertex \(v_{k+1}:=b_{v_k,v_k^\prime}^{-1}(v'_{k+1})\). This implements the coupling above: since \(\delta'(v'_k)(b_{v_k,v_k^\prime}(u))=\delta(v_k)(u)\) for every \(u\in\mathrm{Succ}(v_k)\), the induced shadow transition has distribution \(\delta(v_k)\). Moreover, color preservation gives \(\chi_\infty^G(v_{k+1})=\chi_\infty^{G^\prime}(v'_{k+1})\). Thus \(\sigma'\) reconstructs the shadow move from the observed move in \(G'\), without observing the random tape.

The fixed local bijections give a bijection between finite histories in the two games. Both directions of this correspondence depend only on the histories already observed. Therefore, \(\sigma'\) is a legal history-dependent strategy.

