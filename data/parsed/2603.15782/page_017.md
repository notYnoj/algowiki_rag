## 6.2 Solving the maximum \(\mu\)-uniform Q-flow problem

We will reduce the problem to a maximum multicommodity flow problem in a directed weighted graph G and then apply the algorithm of Chen-Graur-Sidford \[8\] for the latter problem. Start with the network \(\mathcal{N}(\varnothing,\varnothing,\mu)\) of Section 5, remove _s,t_, and add:

• for each \(x\in S\), nodes \(x^\ominus,x^\oplus\), an arc \((x^\ominus,x^\oplus)\) of capacity \(\mu\), and infinite-capacity arcs \((x^\oplus,x^+)\) and \((x^-,x^\ominus)\);<tbc>

• for each rectangle \(Q_i=A_i\times B_i\), private nodes _s<sub>i</sub>,t<sub>i</sub>_ and infinite-capacity arcs \((s_i,x^\ominus)\) for \(x\in A_i\) and \((y^\oplus,t_i)\) for \(y\in B_i\).

Note that G has _M=O(mq_) nodes and edges.

Now consider the maximum multicommodity flow problem in G with _q_ terminal pairs \(\{(s_i,t_i)\}_{i=1}^q\). We claim that it is equivalent to the maximum \(\mu\)-uniform Q-flow problem, i.e. there are value- preserving transformations between the problems in each direction. Indeed, use the path lifting and projection from Lemma 12(b) for the vertex and edge gadgets. For a path with endpoints \(a\in A_i,b\in B_i\), prepend \((s_i,a^\ominus,a^\oplus)\) and append \((b^\ominus,b^\oplus,t_i)\). The gadget arcs enforce exactly the vertex and edge loads, and each endpoint gate is used once per incident demand, enforcing the shared bound \(\mu\) across all rectangles and both endpoint roles. Conversely, remove flow cycles and project each simple _s<sub>i</sub>-t<sub>i</sub>_ path. Such a path cannot traverse an endpoint gate internally, since it would revisit the corresponding split vertex; private sources and sinks cannot occur internally either. The resulting paths therefore lie in \(Q_i^\text{paths}\) and satisfy all three load constraints with the same total value.

Next, we apply the algorithm in \[8\] for the approximate multicommodity flow problem. It produces a flow of value at least \((1-\varepsilon')\) of the optimum in \(O(M^{1+o(1)}q/\varepsilon')\) time, assuming that weights are polynomially-bounded integers. (In our case edges with infinite weights can be safely replaced with _Mc_<sub>max</sub>+1 where _c_<sub>max</sub> is the maximum finite weight in G). Cycle removal and endpoint decomposition take _O(M_log(_n+q_)) time per commodity using dynamic trees \[41, Section 6\] and pseudo-decomposition \[40, Lemma 3.7\]. Recording only the endpoint pairs and their weights constructs the demand graph \(D_\nu\) with _O(Mq_) edges in total, without listing path interiors.

We arrive at the following result.

**Theorem 17.** _For a given value_ \(\mu=a/b\) _with polynomially-bounded integers a,b we can in m_<sup>1+_o_(1)</sup>_q_<sup>2+_o_(1)</sup> _time compute a_ \(\mu\)_-uniform_ Q_-flow_ \(\nu\)_, represented implicitly, of value at least_ OPT<sub>Q</sub>/2_, and construct the demand graph_ \(D_\nu\) _with O(mq_<sup>2</sup>) _edges._

**Remark 1.** _Alternatively, an approximate_ \(\mu\)_-uniform_ Q_-flow with desired guarantees could be computed via calls to a minimum-cost flow subroutine using the MWU framework; this was the solution originally proposed by AI. We replaced it with a reduction to the algorithm in \[8\], which is a shorter way to get the desired complexity._

## 6.3 Feedback matrix for a large flow (\(\text{\texttt{val}}(\nu)\ge 2\alpha/\varepsilon\))

Let \(\nu\) be the flow from Theorem 17. In this section we show the following result.

**Lemma 18.** _Suppose that parameters_ \(\gamma,\tau\) _in eq._ (6) _satisfy_ \(\tau\le\xi/2\) _and_ \(\gamma\le min\{1/4,\varepsilon/(2(\varepsilon+\tau))\}\)_. If_ \(\text{\texttt{val}}(\nu)\ge 2\alpha/\varepsilon\) _then_ \(N=-\mathcal{L}(D_\nu)\) _is a valid feedback matrix of the reduced oracle with_ \(\|N\|\le 2\mu\)_. This matrix has O(mq_<sup>2</sup>) _non-zero entries._

_Proof._ Set \(\lambda_e=\sum_{p:e\in p}\nu(p)\). The load and Laplacian calculations in the proof of Lemma 12(b) apply to any path routing with these vertex, edge and endpoint bounds, including \(\nu\). Thus \(N=-\mathcal{L}(D_\nu)\) has the required form and satisfies \(\|N\|\le 2\mu\).

