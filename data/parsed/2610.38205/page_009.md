The preceding lemma applies only to pairs at one particular distance. Applying this separately to up to \(\Theta(n^2)\) distinct distances is too expensive. We therefore group distances into geometrically increasing scales. For \(0<\varepsilon<1\), define the distance scales \(r_\ell=d_{min}(1+\varepsilon)^\ell\) for \(\ell=0,\dots,\lceil log_{1+\varepsilon}(\Delta)\rceil\), where \(d_{min}=min_{p\neq q}d(p,q)\). We now round each pairwise distance in _P_ down to the nearest scale \(r_\ell\), that is, we assign each distance \(x\in[d_{min},d_{max}]\) to the largest scale \(r_\ell\) satisfying \(r_\ell\le x\). Consequently, there are only \(O(log_{1+\varepsilon}(\Delta))=O(log(\Delta)/\varepsilon)\) distinct distances, and each new distance differs from its original distance by no more than a factor of \((1+\varepsilon)\). Let \(\rho(x)\) denote the rounded distance for a distance _x_.

We now define the verification procedure used throughout this paper.

**Lemma 2.5** (Batched verification)**.** _Given P, a directed graph G_=(_P,E),_ \(\alpha\ge 1\)_, and_ \(0<\varepsilon\le 1\)_, there is a procedure,_ \(VerifyNav(G,\alpha,\varepsilon)\)_, which runs in_

\(O\left(n^\omega\left(1+log_{1+\varepsilon}\Delta\right)\right)\)

_time and returns a set_ N(_G_) _of source-target pairs that_

1. _Includes all_ (_s,t_) _pairs where no edge_ \((s,v)\in E\) _satisfies_ \(d(v,t)<\frac{1}{\alpha}d(s,t)\)<tbc>

_2._ _Excludes all_ (_s,t_) _pairs where some edge_ \((s,v)\in E\) _satisfies_ \(d(v,t)<\frac{1}{\alpha(1+\varepsilon)}d(s,t)\)

_Equivalently, if_ \(\mathcal{U}_\beta(G)\) _denotes the set of unsatisfied_ \(\beta\)_-navigability constraints, then_

\(\mathcal{U}_\alpha(G)\subseteq\mathcal{N}(G)\subseteq\mathcal{U}_{\alpha(1+\varepsilon)}(G).\)

_Proof._ Recall from Lemma 2.4 that we can identify in \(O(n^\omega)\) time the exact set of (_s,t_) pairs where an edge \((s,v)\in E\) satisfies _d(v,t)\<r_.

We execute this procedure on the distance scales \(r^\ell/\alpha\) for \(\ell=0,\dots,\lceil log_{1+\varepsilon}(\Delta)\rceil\). Thus, we compute, for each distance scale \(r^\ell\), the set of all (_s,t_) pairs where some \((s,v)\in E\) satisfies \(d(v,t)<r^\ell/\alpha\). Now take any (_s,t_) pair. Recall that its rounded distance \(\rho(d(s,t))\) matches some distance scale \(r^\ell\). For that \(r^\ell\), consult whether some \((s,v)\in E\) satisfies \(d(v,t)<r^\ell/\alpha\). If not, return (_s,t_). We claim that doing this over all (_s,t_) pairs returns all pairs whose \(\alpha\)-navigability constraint is not satisfied and no pairs whose \(\alpha(1+\varepsilon)\)-navigability constraint is satisfied.

First, suppose some (_s,t_) pair’s \(\alpha\)-navigability constraint is not satisfied. That is, no (_s,v_) edge satisfies \(d(v,t)<\frac{1}{\alpha}d(s,t)\). Since \(\rho(d(s,t))\le d(s,t)\), it must also hold that no (_s,v_) edge satisfies the even stronger condition of \(d(v,t)<\frac{1}{\alpha}\rho(d(s,t))\). Thus, (_s,t_) is returned.

Second, suppose some (_s,t_) pair’s \(\alpha(1+\varepsilon)\)-navigability constraint is satisfied. That is, there is some edge, \((s,v^*)\in E\), where \(d(v^*,t)<\frac{1}{\alpha(1+\varepsilon)}d(s,t)\). Since rounded distances are less than a \((1+\varepsilon)\) factor off from true distances, it follows that \(\rho(d(s,t))\ge\frac{1}{1+\varepsilon}d(s,t)\). Substituting \(d(s,t)\le(1+\varepsilon)\rho(d(s,t))\) yields that \(d(v^*,t)<\frac{(1+\varepsilon)}{\alpha(1+\varepsilon)}\rho(d(s,t))\le\frac{1}{\alpha}\rho(d(s,t))\). Thus, (_s,t_) is not returned.

Thus, we have shown that the set of returned source-target pairs satisfies the properties listed in the above lemma. Finally, the entire procedure takes _O(n_<sup>2</sup>) time to check whether to return each pair, as well as \(O(log_{1+\varepsilon}(\Delta))=O(log(\Delta)/\varepsilon)\) calls to the procedure from Lemma 2.4, taking \(O(n^\omega log(\Delta)/\varepsilon)\) time total.

## 3 Fast Resource Augmented Sparsest \(\alpha\)-Navigable Graphs

In this section, we prove our main positive result. Recall from Section 2.3 that for each source point \(s\in P\), choosing the outgoing neighbors of _s_ is exactly a set cover problem: each possible edge (_s,v_)<tbc>

