<tbc>Proof. Using the bounds from Corollary 6.32 and Proposition 6.40, we get

\(p_v^i\le 2\cdot 2c_3log^{l_4}(n)t_i^{1-\epsilon_1}p_\mathrm{gr}^3\cdot\frac{log^{4l_3+6}(n)}{0.9c_1^3t_ip_\mathrm{gr}^3}\le\frac{5c_3log^{4l_3+l_4+6}(n)}{c_1^3t_i^{\epsilon_1}},\)

as required. □

Let \(p_e^i\) be the probability that an edge \(e\in H_{i.1}[I_{t_{i+1}}]\) does not survive the greedy cover step. That is, the probability that at least one of the vertices in _e_ is in an edge that is used by the greedy cover step.

Proposition 6.42. _For every_ \(e\in H_{i.1}[I_{t_{i+1}}]\),

\(p_e^i\le 4\mathrm{max}_{v\in e}p_v^i.\)

Proof. Let \(e\in H_{i.1}[I_{t_{i+1}}]\). Then by a union bound we have \(p_e^i=\bigcup_{v\in e}p_v^i\le\sum_{v\in e}p_v^i\le 4\mathrm{max}_{v\in e}p_v^i\) as required. □

Corollary 6.43. _For every_ \(e\in H_{i.1}[I_{t_{i+1}}]\),

\(p_e^i<\frac{20c_3log^{4l_3+l_4+6}(n)}{c_1^3t_i^{\epsilon_1}}.\)

We use the bounds from Corollaries 6.41 and 6.43 to look at properties in the graph remaining once the random greedy algorithm has completed. As previously discussed, since a greedy algorithm would not abort, it is clear that the random greedy cover will be able to cover all vertices in _V(H_<sub>_i._1</sub>\[_I<sub>t<sub>i</sub></sub>_\\_I_<sub>_t<sub>i</sub>_+1</sub>\]), and so we obtain a matching \(M_i^c\) covering _V(H_<sub>_i._1</sub>\[_I<sub>t<sub>i</sub></sub>_\\_I_<sub>_t<sub>i</sub>_+1</sub>\]). Let

\(H_{i+1}:=H_{i.1}[V(H_{i.1})\backslash V(M_i^c)].\)

Lemma 6.44. _Let_ \(S\subseteq V(\mathcal{T}[I_{t_{i+1}}])\) _be i-reachable, and let f<sub>S</sub> be a function such that_ \(\frac{\mathrm{max}_{v\in V(H_i[I_{t_{i+1}}])}f_S(v)}{\mathrm{min}_{v\in V(H_i[I_{t_{i+1}}])}f_S(v)}\le log^{500}(n)\)_. With high probability_

\(\sum_{v\in V(H_{i+1}[S])}f_S(v)=(1\pm t_i^{-1.5\epsilon_1})\sum_{v\in V(H_{i.1}[S])}f_S(v)(1-p_v^i),\)

_and in particular the number of vertices which survive the greedy cover process to V(H_<sub>_i_+1</sub>\[_S_\]) _satisfies_

\(|V(H_{i+1}[S])|=(1\pm t_i^{-1.5\epsilon_1})\sum_{v\in V(H_{i.1}[S])}(1-p_v^i).\)

Note that we have \(t_i^{-1.5\epsilon_1}\) where previous similar equations have included \(t_i^{-\epsilon_1}\). The key detail here is that it is of the form \(t_i^{-c\epsilon_1}\) for some _c\>_1 to avoid a blow-up of error terms.

Proof. Let _X<sup>f,S</sup>_ be the total weight removed from _V(H_<sub>_i._1</sub>\[_S_\]) with respect to _f<sub>S</sub>_ as a result of the random greedy cover. Then we have that \(\mathbb{E}(X^{f,S})=\sum_{v\in V(H_{i.1}[S])}f_S(v)p_v^i\). Furthermore, we may write \(X^{f,S}=\sum_jX_j^{f,S}\) where \(X_j^{f,S}\) is the weight removed from _V(H_<sub>_i._1</sub>\[_S_\]) with respect to _f<sub>S</sub>_ as a result of the choice of edge _e<sub>j</sub>_ for vertex _v<sub>j</sub>_ in the random greedy algorithm. Let \(\mathbb{E}'(X_j^{f,S})\) be the conditional expectation of \(X_j^{f,S}\) given that _e_<sub>1</sub>_,...,e_<sub>_j_-1</sub> have been revealed, and let \(Y_j^{f,S}:=\sum_{k\le j}(X_k^{f,S}-\mathbb{E}'(X_k^{f,S}))\). Write \(f_S^\mathrm{max}:=\mathrm{max}_{v\in V(H_{i.1}[S])}f_S(v)\) and

