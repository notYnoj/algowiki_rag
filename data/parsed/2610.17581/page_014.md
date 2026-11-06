where the first inequality is an application of Stirling’s approximation, and the second inequality follows by taking \(n\ge 18\) so that \(2^{n/6}\ge\sqrt{\pi n/3}\). Since the hyperedges are unweighted, we have

\(\mathrm{Pr}[e_i^X=X]=1/|\partial(S_i)|\le 2^{-n/2}.\)

We can bound the probability that hyperedge _X_ is output by any of the _t_ queries with a union bound, yielding \(\mathrm{Pr}[X\in\mathcal{A}_i^X]\le t/2^{n/2}\). Since the distribution of answers on _H<sub>X</sub>_ conditioned on not seeing _X_ is identical to the distribution of answers \(K_n^r\), we get \(\Delta_\text{TV}((\mathcal{A}_t^X|X\notin\mathcal{A}_t^X),\mathcal{A}_t^0)=0\). Finally, we obtain \(\Delta_\text{TV}(\mathcal{A}_t^X,\mathcal{A}_t^0)\le t/2^{n/2}\) by the fact that total variation distance is equal to half of the _L_<sup>1</sup> distance.

We now bound the probability that any algorithm can guess _X_ correctly. Letting \(\mathcal{S}=\{\mathcal{A}_t^0\}\cup\{\mathcal{A}_t^X\}_{X\in\genfrac(){pt}{2}{V}{k}}\), we obtain a coupling of these random variables by Proposition 6. Importantly, this coupling satisfies \(\mathrm{Pr}\left[\mathcal{A}_t^X=\mathcal{A}_t^0\right]\ge 1-2\Delta_\text{TV}(\mathcal{A}_t^X,\mathcal{A}_t^0)\ge 1-2t/2^{n/2}\) for all \(X\in\genfrac(){pt}{2}{V}{k}\). However, \(\mathcal{A}_t^0\) is independent of _X_, and thus the query answers \(\mathcal{A}_t^X\) are independent of _X_ with probability at least 1-2_t/_2<sup>_n/_2</sup>. In this case, we have that \(X|\mathcal{A}_t^X\) is uniformly distributed in \(\genfrac(){pt}{2}{V}{k}\), and so an algorithm can at best guess _X_ with probability \(1/\genfrac(){pt}{2}{n}{k}\). If we roughly bound the probability of correctly guessing _X_ when \(\mathcal{A}_t^X\neq\mathcal{A}_t^0\) by 1, we find that an algorithm can correctly guess _X_ with probability at most

\(\left(1-2t/2^{n/2}\right)\cdot\genfrac(){pt}{2}{n}{k}^{-1}+2t/2^{n/2}\cdot 1\le 1\cdot 2^{-n/2}+2t/2^{n/2}\le\frac{1+2t}{2^{n/2}},\)

completing the proof.

## 5 Lower Bounds on Query Complexity of D_k_S and D_k_SH

In this section, we prove a pair of lower bounds which settle the cut query complexity of exact Densest _k_-Subgraph up to an _O_(log_n_) gap for randomized algorithms on weighted graphs. We prove these results more generally for hypergraphs, yielding a variety of exponential lower bounds on the query complexity of exact Densest _k_-Subhypergraph. Notably, we are able to prove lower bounds against algorithms with access to both cut and edge (and even add) queries, showing that D_k_SH is fundamentally intractable in the query model. Some of the results in this section also imply mild inapproximability, ruling out cut approximation schemes for D_k_S and fully polynomial-time approximation schemes for D_k_SH, even with any queries. In comparison, our strong inapproximability results in Section 4 apply exclusively to algorithms restricted to only cut or only edge queries.

### 5.1 Deterministic Complexity of D_k_S, and D_k_SH with cut queries

We begin by proving a lower bound of \(\genfrac(){pt}{2}{n}{r}\) on the deterministic cut query complexity of D_k_SH on weighted hypergraphs. As a corollary, this result nails down the complexity of deterministic D_k_S on weighted graphs to \(\Theta(n^2)\) queries. For hypergraphs, although Theorem 4.2 unambiguously rules out approximations and thus exact solutions to D_k_SH, our result shows that this problem is hard _even for uniform hypergraphs of arbitrary rank for arbitrary k_, whereas our earlier result relies on the indistinguishability of particular rank-2 and rank-3 hypergraphs.

**Theorem 5.1.** The deterministic cut query complexity of D_k_SH on rank-_r_ hypergraphs is at least \(\genfrac(){pt}{2}{n}{r}\), for any \(r\le k\le n-r\).

Our proof of Theorem 5.1 uses the cut dimension approach. Graur et al. \[18\] originally introduced cut dimension to prove lower bounds on Submodular Function Minimization, before the technique was specialized to graphs by Plevrakis et al. \[33\] to obtain a quadratic lower bound on the query complexity of Max Cut. The key idea is that before any queries, a graph’s<tbc>

