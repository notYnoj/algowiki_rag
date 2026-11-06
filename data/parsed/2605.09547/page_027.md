**Lemma 6.8** (\[DS08b\], or Lemma 7.8 of \[BLL<sup>+</sup>21\])**.** _Let_ \(\Pi=(G,b,c)\) _be an instance for minimum-cost flow problem where G is a directed graph with m edges, the demand vector_ \(b\in\{-W,\dots,W\}^V\)_, the cost vector_ \(c\in\{-W,\dots,W\}^E\) _and the capacity vector_ \(u\in\{0,\dots,W\}^E\).

_Let the perturbed instance_ \(\Pi'=(G,b,c')\) _be such that_ \(c'_e=c_e+z_e\) _where z<sub>e</sub> is a random number from the set_ \(\big\{\frac{1}{4m^2W^2},\dots,\frac{2mW}{4m^2W^2}\big\}\)_. Let_ \(x'\) _be a feasible flow for_ \(\Pi'\) _whose cost is at most_ \(\mathrm{OPT}(\Pi')+\frac{1}{12m^2W^3}\) _where_ \(\mathrm{OPT}(\Pi')\) _is the optimal cost for problem_ \(\Pi'\)_. With probability at least 1/2, there exists an optimal feasible and integral flow x for_ \(\Pi\) _such that_ \(\|x-x'\|_\infty\le 1/3\).

**Theorem 1.2** (Min-cost Flow, Communication)**.** _There is a randomized communication protocol that, given an input graph G_=(_V,E_) _with integer capacities_ \(u\in[1,W]^E\) _and costs_ \(c\in[1,W]^E\)_, vertex demand vector_ \(b\in\mathbb{R}^V\)_, where the edges are split among two parties, computes w.h.p. an exact min-cost flow in_ \(\widetilde{O}(n^{1.5}\mathrm{log}(W))\) _communication. At the end, each party knows the amount of flow on each of their own edges._

_Proof._ Theorem 1.2 follows directly in the same way as Theorem 1.1 while applying Theorem 4.19. For this, we need to show that we can indeed start with \((x^{(\mathrm{init})},s^{(\mathrm{init})},\mu^{(\mathrm{init})})\) for both parties. \(\mu^{(\mathrm{init})}\) is a single predetermined scalar, and for all non-star edges _e_, each party can query \(x_e^{(\mathrm{init})}\) and \(s_e^{(\mathrm{init})}\) for their own edge set, because they are simply _u<sub>e</sub>/_2 and _c<sub>e</sub>_, respectively, which each party knows for their own edge set. The flow on star edges \(e'\) depend on the vertex demands: since there are only _O(n_) vertices each party can add up the demands from their edges and send them to each other using _O(n_) bits of communication to both know the total vertex demands and determine \(x_{e^\prime}^{(\mathrm{init})}\) and \(s_{e^\prime}^{(\mathrm{init})}\).

Then, we can continue with the algorithm (Theorem 4.19) until both parties know the final transcript. Then each party can query the flow on their own edge set via the transcript.

Now, to make the flow unique, we very slightly modify the above algorithm. Before we do anything we first perturb the edge costs _c_ to \(c'\) according to Lemma 6.8. Storing the perturbations takes _O(m_) space, which can be larger than _O(n_<sup>1.5</sup>), but crucially neither player needs to send this information to the other, as each keeps track of its own edges.

Then, after completing the algorithm, consider our final flow \(\left[\begin{array}{ c }
x^{(\mathrm{final})} \\
\widetilde{x}^{(\mathrm{final})}
\end{array}\right]\). Lemma 6.8 guarantees with probability at least 1/2 that there exists an integral min cost flow \(\left[\begin{array}{ c }
x^\mathrm{OPT} \\
\widetilde{x}^\mathrm{OPT}
\end{array}\right]\) with each edge value differing by at most 1/3. Thus, with probability at least 1/2, if whenever we query the flow along an edge we instead round it to the nearest integer, we recover \(\left[\begin{array}{ c }
x^\mathrm{OPT} \\
\widetilde{x}^\mathrm{OPT}
\end{array}\right]\). Moreover, by Lemma 6.7, we know \(\|\widetilde{x}^{(\mathrm{final})}\|_\infty\) can be made less than 1/3, so indeed the rounded \(\left[\begin{array}{ c }
x^{(\mathrm{final})} \\
\widetilde{x}^{(\mathrm{final})}
\end{array}\right]\) is feasible and optimal for _G_.

Finally, we can boost our success probability to high probability by resampling the random edge costs and repeating our algorithm _O_(log_n_) times. We can verify whether each flow is feasible after rounding by comparing the vertex demands, i.e., having both parties exchange the net-flow on each vertex and checking that they add up to demand _b_, which uses _O(n_) space. Then in the end, we choose the flow with the smallest cost among all constructed feasible flows.

## Remark on Bit-complexity

The bit complexity can be bounded via the following lemma from \[BLL<sup>+</sup>21\].

**Lemma 6.9** (\[BLL<sup>+</sup>21, Lemma 4.46\])**.** _Let W be the ratio of largest to smallest entry of_ \(\phi''(x^{(\mathrm{init})})^{1/2}\) _and let_ \(W'\) _be the ratio of largest to smallest entry of_ \(\phi''(x)^{1/2}\) _encountered throughout the algorithm. Then_

\(\mathrm{log}W'=\widetilde{O}(\mathrm{log}W+\mathrm{log}(1/\mu^{(\mathrm{final})})+\mathrm{log}\|c\|_\infty).\)

Observe that by \(\phi''(x)=1/x_e^2-1/(u_e-x_e)^2\) and \(\mu^{(\mathrm{final})}=1/(\epsilon\cdot\mathrm{poly}(n\mathrm{max}(\|c\|_\infty,\|u\|_\infty,\|b\|_\infty)))\), this lemma bounds the smallest value we might obtain for any _x<sub>e</sub>_. If we run the algorithm with some \(\widetilde{O}(\mathrm{log}(W/\epsilon))\) bit-length numbers, then we can guarantee the additive error is small multiplicative error, i.e., we always have a multiplicative approximation of _x_ and \(\phi''(x)\). Since the algorithm supports spectral approximation of \(\mathbf{A}^\top\mathbf{T}^{-1}\Phi''(x)^{-1}\mathbf{A}\), and entry-wise approximation of \(\tau\) and _x_ when defining _g_ (Section 5), the algorithm and<tbc>

