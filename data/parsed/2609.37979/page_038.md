<tbc>obtained by deleting repeating vertices and edges of the walk. Note that for each \((n,c,\ell)\in X\) the path _P_ uses edges of color \((c,\ell)\) at most _n_ times. Further since check(_G,X)\>_0, we obtain

\(\ell(P)\le\sum_{(n,c,\ell)\in X}n\cdot\ell\le B\text{and}c(P)\le\sum_{(n,c,\ell)\in X}n\cdot c=\mathrm{cost}(X).\)

Thus, _P_ is a feasible path of length at most _B_. Further, \(OPT(G)\le\mathrm{cost}(X)\) since _P_ has cost at most cost(_X_).

Next, assume that \(OPT(G)<\infty\) then there is a _s,t_-path _P_<sup>∗</sup> with \(\ell(P^*)\le B\) and _OPT(G_)=_c(P_<sup>∗</sup>). Now, let _X_ be the set that contains \((n,c,\ell)\) if and only if the edge color \((c,\ell)\) is used _n_ times in _P_<sup>∗</sup>. Observe that \(\sum_{(n,c,\ell)\in X}n\cdot\ell=\ell(P^*)\le B\). Further note that \(OPT(G)=c(P^*)=\sum_{(n,c,\ell)\in X}n\cdot\ell=\mathrm{cost}(X)\). Since _P_<sup>∗</sup> is path _s,t_-path and therefore a walk, (3) yields that \(\mathrm{check}(G,X)\ge 1>0\). Thus, _OPT(G_)=cost(_X_) and check(_G,X)\>_0.

The proof of the following lemma was discussed in \[Bök19, Section 1.1\]. The lemma is a generalization of Theorem 1 in \[DGR18\].

**Lemma 8.11.** _Let F be a tree and H,G be two graphs. If_ \(H\equiv_{1\text{-}\mathrm{WL}}G\) _then_ \(\#\mathrm{Hom}(F\rightarrow G)=\#\mathrm{Hom}(F\rightarrow H)\).

**Lemma 8.12.** _The function_ \(\mathrm{check}:\mathcal{G}\times W\rightarrow\mathbb{R}\) _is 1-WL invariant._

_Proof._ Let \(G,H\in\mathcal{G}\) be two graphs with \(G\equiv_{1\text{-}\mathrm{WL}}H\). According to Lemma 8.11, \(\#\mathrm{Hom}(F\rightarrow G)=\#\mathrm{Hom}(F\rightarrow H)\) for all trees _F_. Since every path is a tree, we obtain that check(_G,X_)=check(_H,X_) for all \(X\in W\) that satisfy the length constraint, that is, \(\sum_{(n,c,\ell)\in X}n\cdot\ell\le B\). Note that _G_ and _H_ have the same length constraint since \(G\equiv_{1\text{-}\mathrm{WL}}H\).

_Proof of Theorem 8.8._ According to Lemma 8.10, the triple \((W,\mathrm{check}:\mathcal{G}\times W\rightarrow\mathbb{R},\mathrm{cost}:W\rightarrow\mathbb{R})\) is a witness function of _OPT_. Further, Lemma 8.12 shows that check is 1-WL invariant. Thus, Lemma 8.7 implies that CSP is 1-WL invariant.

**Corollary 8.13.** _There is an algorithm that solves the_ CSP _problem with k prior instances each of size at most n in O(k(n+m_)log_n_) _preprocessing time and O_((_n+m_)log_n_) _query time._

_Proof._ This is a direct consequence of Theorem 8.4 combined with Theorem 8.8.

## 8.4 CST is 2-WL Invariant

Next, we again turn to the Constrained Spanning Tree (CST) problem. Recall that, in Theorem 6.3, we obtained a randomized algorithm in the Isomorphic-Priors model with \(\widetilde{O}(kn^\omega)\) preprocessing time and \(O(n^\omega)\) query time. In the following, we obtain a deterministic algorithm via 2-WL. Write _OPT_ for the optimal value function of CST and G for the set of valid input graphs of CST. We show that _OPT_ is 2-WL invariant for all values.<sup>27</sup> This together with Theorem 8.3 this immediately yields a deterministic algorithm for CST in the Isomorphic-Priors model.

**Theorem 8.14.** _The problem_ CST _is 2-WL invariant._

<sup>27</sup>As before, we say that two input graphs _G_ and _H_ are 2-WL equivalent if _G_ and _H_ have the same budget _B_ value and \(G\equiv_{2\text{-}\mathrm{WL}}H\) for the underlying attributed graphs.

