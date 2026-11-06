Now we need to show that this final point is also close to the exact optimal point to conclude that the point found by the IPM is too. Note that it suffices to show that \(\left[\begin{array}{ c }
x^{(\mathrm{final})} \\
\widetilde{x}^{(\mathrm{final})}
\end{array}\right]\) is close to an optimal point of \(\widetilde{G}\) as any optimal flow for \(\widetilde{G}\) would not use any of the new star edges.

**Lemma 6.7.** _Let_ \(\left[\begin{array}{ c }
x^{(\mathrm{final})} \\
\widetilde{x}^{(\mathrm{final})}
\end{array}\right]\) _be a feasible flow for_ \(\widetilde{G}\) _where_ \(c^\top x^{(\mathrm{final})}+\widetilde{c}^\top\widetilde{x}^{(\mathrm{final})}\le\mathrm{OPT}(\widetilde{G})+\mu n\)_. Then there exists an optimal flow_ \(\left[\begin{array}{ c }
x^\mathrm{OPT} \\
\widetilde{x}^\mathrm{OPT}
\end{array}\right]\) _of_ \(\widetilde{G}\) _with_ \(\widetilde{x}^\mathrm{OPT}=0\) _such that_ \(\|\left[\begin{array}{ c }
x^{(\mathrm{final})} \\
\widetilde{x}^{(\mathrm{final})}
\end{array}\right]-\left[\begin{array}{ c }
x^\mathrm{OPT} \\
\widetilde{x}^\mathrm{OPT}
\end{array}\right]\|_\infty\le\mu n^2\).

_Proof._ \(\left[\begin{array}{ c }
x^{(\mathrm{final})} \\
\widetilde{x}^{(\mathrm{final})}
\end{array}\right]\) is feasible but not optimal. Recall that we can get an optimal flow by repeatedly improving the value of a feasible flow by finding a negative cost cycle in the residual graph induced by this flow, then augmenting the flow by this cycle. Let \(\left[\begin{array}{ c }
x^\mathrm{OPT} \\
\widetilde{x}^\mathrm{OPT}
\end{array}\right]\) be the optimal flow created by augmenting \(\left[\begin{array}{ c }
x^{(\mathrm{final})} \\
\widetilde{x}^{(\mathrm{final})}
\end{array}\right]\) in this way.<br>
Note that our edge costs are integral; thus, each cycle has cost at most -1. Since we have \(c^\top x^{(\mathrm{final})}+\widetilde{c}^\top\widetilde{x}^{(\mathrm{final})}\le\mathrm{OPT}(\widetilde{G})+\mu n\), and each cycle can only use _n_ edges, we have \(\|\left[\begin{array}{ c }
x^{(\mathrm{final})} \\
\widetilde{x}^{(\mathrm{final})}
\end{array}\right]-\left[\begin{array}{ c }
x^\mathrm{OPT} \\
\widetilde{x}^\mathrm{OPT}
\end{array}\right]\|_\infty\le\|\left[\begin{array}{ c }
x^{(\mathrm{final})} \\
\widetilde{x}^{(\mathrm{final})}
\end{array}\right]-\left[\begin{array}{ c }
x^\mathrm{OPT} \\
\widetilde{x}^\mathrm{OPT}
\end{array}\right]\|_1\le\mu n^2\).

## 6.3 Putting Everything Together

In this section, we prove the main result Theorems 1.1 and 1.2.

**Theorem 1.1** (Min-cost Flow, Streaming)**.** _There is a randomized multi-pass streaming algorithm that, given an input graph G_=(_V,E_) _with integer capacities_ \(u\in[1,W]^E\) _and costs_ \(c\in[1,W]^E\)_, vertex demand vector_ \(b\in\mathbb{R}^V\) _and accuracy parameter_ \(\epsilon\in[0,1]\)_, computes w.h.p. a min-cost flow in_ \(\widetilde{O}(n^{1.5}\mathrm{log}(W/\epsilon))\) _space and_ \(\widetilde{O}(\sqrt{n}\mathrm{log}(W/\epsilon))\) _passes over the input. The total time is_ \(\widetilde{O}(mn\mathrm{log}^2(W/\epsilon))\).

_The algorithm returns a randomized_ \(\widetilde{O}(n^{1.5}\mathrm{log}(W/\epsilon))\)_-space data structure that supports edge-queries: For any given edge e_=((_w,v),c<sub>e</sub>,u<sub>e</sub>), the query returns in_ \(\widetilde{O}(\sqrt{n}\mathrm{log}(W/\epsilon))\) _time an estimate <o>f</o><sub>e</sub> of the flow on that edge, with_ \(0\le\overline{f_e}\le u_e\) _and_ \(|\overline{f_e}-f_e|\le\epsilon\) _with high probability._

_Alternatively, we can also assume that during the last pass, the algorithm returns for each given edge e_=((_w,v),c<sub>e</sub>,u<sub>e</sub>_) _the flow <o>f</o><sub>e</sub> on that edge._

_Proof._ We use the interior point method Algorithm 1, specifically Theorem 4.1. This method requires an \(\epsilon\)-centered initial point \((x,s,\mu)\) with query time _T_<sub>0</sub>, and a target \(\mu^{(\mathrm{target})}\).

We use Lemma 6.1 to find an \(\epsilon/W\)-centered initial point, which also gives us a \(T_0=\widetilde{O}(1)\) initial query time. By Lemma 6.2 this constructed \(\epsilon/W\)-centered point uses \(\mu^{(\mathrm{init})}=100m^2W^4\epsilon^{-1}\).

We now run our interior point method on this initial point with target parameter \(\mu^{(\mathrm{target})}=\epsilon/(Wn^2)\). Theorem 4.1 tells us we need \(\widetilde{O}(n^{1.5}\mathrm{log}(W/\epsilon)\) space and \(\widetilde{O}(\sqrt{n}\mathrm{log}(W/\epsilon))\) passes to construct the resulting flow _x_. The total runtime is \(\widetilde{O}(mn\mathrm{log}^2(W/\epsilon))\).

The constructed flow \(x\in\mathbb{R}^E\) is not an optimal min-cost flow, since (i) the cost is slightly too large, (ii) the flow might use the star-edge that were added in the initial point construction.

However, by Lemma 6.4 and accuracy parameter \(\epsilon/W\) we see that for \(\mu^{(\mathrm{target})}=\epsilon/(Wn^2)\) our constructed _x_ is such that there exists an optimal solution _x_<sup>OPT</sup> with \(\|x-x^\mathrm{OPT}\|_\infty\le\epsilon\). In particular, this optimal flow does not route any flow on the star-edges that were added in the initial point construct, so _x_<sup>OPT</sup> is an optimal flow for the original input graph.

Thus _f=x_<sup>OPT</sup> is the optimal flow, and <o>_f_</o>=_x_ is the flow for which we can query edges, and we have \(\|f-\overline{f}\|_\infty\le\epsilon\).

By Theorem 4.1, we use \(\widetilde{O}(n^{1.5}\mathrm{log}(W/\epsilon))\) space with query time on each edge \(\widetilde{O}(\sqrt{n}\mathrm{log}(W/\epsilon))\).

Next, we analyze our algorithm in the context of communication complexity. In this setting, we are only limited by the number of bits sent between the players and not the bits stored, so we can use the following isolation lemma to find an exact flow.

