### Bounded Flow Oracle.

We invoke the decision oracle of Theorem 3.5, which has preprocessing time \(O((kn)^\omega)\) and space _O_((_kn_)<sup>2</sup>log_n_). For a query (_s,t,U_), we binary search over \(\lambda\in[0,k]\) and, for each \(\lambda\), test whether the updated Laplacian on \(G^*+U+E_{s,t,\lambda}\) is non-singular. Each test takes \(O(\delta^\omega)=O((fk^2)^\omega)\) time, and the _O_(log_k_) tests yield \(\lambda^*\) in \(O((fk^2)^\omega logk)\) time.

### Nearest Min-Cut Oracle.

The preprocessing is identical to the bounded flow oracle. Given a query (_s,t,U_), we first compute \(\lambda:=\lambda_{G+U}(s,t)\) in \(O((fk^2)^\omega logk)\) time. For each \(w\in V\backslash\{s,t\}\), we invoke the bounded flow oracle on _G+U_+(_w,t_) to test whether \(\lambda_{G+U+(w,t)}(s,t)=\lambda+1\). By Theorem 2.1, the set

\(\big\{w\in V:\lambda_{G+U+(w,t)}(s,t)=\lambda+1\big\}\)

is the source side of the nearest min-cut, and its complement is the sink side. Each of the _n_ auxiliary queries adds a single edge to _U_, preserving the update size \(\delta=O(fk^2)\), and takes \(O((fk^2)^\omega)\) time. The total query time is \(O((fk^2)^\omega\cdot n)\).

### Min-Cost Flow Oracle.

We invoke the weighted oracle of Theorem 3.5, which has preprocessing time \(\widetilde{O}(W(kn)^3)\) and space _O(W(kn_)<sup>3</sup>log_n_). For a query (_s,t,U_), we first compute \(\lambda^*:=min(k,\lambda_{G+U}(s,t))\) using the bounded flow oracle in \(O((fk^2)^\omega logk)\) time. By Theorem 4.1, the minimum cost of an (_s,t_)-flow of value \(\lambda^*\) in _G+U_ equals the minimum weight of a _k_-packing-set in \(M_\text{out},M_\text{in}\) on \(G^*+U+E_{s,t,\lambda^*}\), which the weighted oracle returns in \(\widetilde{O}(W\cdot kn\cdot\delta^\omega)=\widetilde{O}((fk^2)^\omega\cdot kWn)\) time. □

## 4.2 Sensitivity Oracles for (_s,t_)-Max-Flow and (_s,t_)-Min-Cut

We now turn to the special case of the general max-flow problem for a fixed source-sink pair (_s,t_). The oracle of Theorem 4.2 with _k=n_ already solves this problem, but its query time is quite high. We show that much better bounds are achievable for the case of a fixed source-sink pair through a flow-rerouting reduction that lets us use Theorem 4.2 as a black box on an auxiliary graph with capacity bound _k=O(f_).

Let _G_=(_V,E_) be a directed graph with unit edge capacities and costs in \[-_W,W_\], with fixed source _s_ and sink _t_. We precompute a min-cost (_s,t_)-max-flow _h_ once, during preprocessing. For any query set _U_ of updates, we aim to answer the following: how can _h_ be _repaired_ into a valid flow on _G+U_, and by how much does its cost change.

To achieve this, we augment _G_ to a graph G by adding 2_f_ zero-cost parallel (_s,t_)-edges, and saturating the first _f_ of them in the preprocessed flow _h_ (thus, value of flow _h_ (denoted by val(_h_)) in G is equal to \(f+\lambda_G(s,t)\)). These parallel edges act as a buffer: when updates arrive, they absorb or release flow as needed, and the number of saturated parallel (_s,t_) edges in the repaired flow tells us the new max-flow value.

**Lemma 4.3.** _For any update set U of size at most f, if every_ (_s,t_)_-flow of value_ val(_h_) _in_ G+_U saturates a minimum of i parallel_ (_s,t_) _edges, then_ \(\lambda_{G+U}(s,t)=\lambda_G(s,t)+f-i\).

_Proof._ Let \(\beta:=\lambda_{G+U}(s,t)-\lambda_G(s,t)\). If \(\beta\ge 0\), \(\beta\) units of flow can be moved from the parallel edges back into _G+U_, so the new flow saturates \(i=f-\beta\) parallel edges. If \(\beta<0\), the updates cancel \(|\beta|\) units of flow in _G_, which must be redirected onto the parallel edges, giving \(i=f+|\beta|\). In both cases, \(\beta=f-i\). □

### Reducing to an All-Pairs Query

It remains to test, given a candidate value of _i_, whether _h_ can in fact be repaired in G+_U_ using exactly _i_ parallel (_s,t_) edges. We construct an auxiliary<tbc>

