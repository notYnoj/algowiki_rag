\(max_{L\in\mathcal{L}(G)}\mathbb{T}_A(G,k,L)\) be the _worst-case_ performance of _A_ on (_G,k_). Finally, denote by OPT(_G,k_) the minimum T_<sub>A</sub>(G,k_) over all correct algorithms _A_.

## 3 Lower bounds

In this section, we define and prove several lower bounds for OPT(_G,k_). The first one is a generalization of \[KKZZ18, Theorem 7\] to arbitrary DAGs.

Let _G_ be a DAG on _n_ nodes. If _U_ is a prefix of _G_, then _c(G,U_)=|Sources(_G-U_)|. Further, for each \(k\in[n]\), let \(c(G,k)=max_{U\in P_k}c(G,U)\), where _P<sub>k</sub>_ is the set of all prefixes of _G_ with _k_ nodes.

**Lemma 4.** _For each DAG G on n nodes and_ \(k\in[n]\)_, we have_ \(\text{OPT}(G,k)\ge c(G,k-1)-1\).

_Proof._ Let _U_ be a prefix of _G_ of size _k_-1 such that _c(G,U_)=_c(G,k_-1). Let _S_ be the set of sources of _G-U_. Consider all instances (_G,k,L_) where _U_ consists of the _k_-1 smallest nodes according to _L_. Note that then the _k_-th element of _L_ must be contained in _S_. Solving poset selection on these instances is equivalent to finding the minimum of _S_, which requires exactly |_S_|-1=_c(G,k_-1)-1 comparisons. Solving the general problem is no easier, hence the lower bound follows.

Lemma 4 is, in fact, all we need for our main result. For our forest-specific algorithms (theorems 2 and 3), more sophisticated lower bounds are required.

For a forest _F_ on _n_ nodes and \(k\in[n]\), let \(c^*(F,k)=max_{1\le k^\prime\le k}c(F,k')\). In the following, we show that _c_<sup>∗</sup>(_F,k_-1) is an (asymptotic) lower bound for OPT(_F,k_). Note that while _c_<sup>∗</sup> can be easily defined for general posets, too, it is _not_ in fact a lower bound for general posets.

We need another simple lower bound for our proofs. Let _F_ be a forest on _n_ nodes, and let _U_ be a prefix of _U_. Let _s(F,U_) be the number of _leaves_ in the induced subgraph _F_\[_U_\]. For each \(k\in[n]\), let \(s(F,k)=max_{U\in P_k}s(F,U)\), where _P<sub>k</sub>_ is the set of all prefixes of _F_ with _k_ nodes.

**Lemma 5.** _For each forest F on n nodes and each_ \(k\in[n]\)_, we have_ \(\text{OPT}(F,k)\ge s(F,k)-1\).

_Proof._ Let _U_ be a prefix of _F_, and let _S_ be the set of leaves in _F_\[_U_\]. Consider all instances (_F,k,L_) where the smallest _k_ elements are in _U_. Then the _k_-th smallest element is precisely the maximum element of _S_. Solving poset selection on these instances is thus equivalent to finding the maximum of _S_, which requires |_S_|-1 comparisons.

**Observation 6.** _For each forest F, the function s(F,k_) _is nondecreasing in k._

**Theorem 7.** _For each forest F on n nodes and_ \(k\in[n]\)_, we have_ \(\text{OPT}(F,k)\ge\frac{1}{2}c^*(F,k-1)-1\).

_Proof._ Let _U_ be a prefix of size at most _k_-1 such that _c(F,U_)=_c_<sup>∗</sup>(_F,k_-1). It suffices to show that \(\text{OPT}(F,k)\ge\frac{1}{2}c(F,U)-1\).

If |_U_|=_k_-1, we are done by lemma 4. Otherwise, let _X_ be a prefix of _F_ of size _k_-1 such that \(U\subseteq X\). Let _S_ be the set of roots of _F_\\_U_, so |_S_|=_c(F,U_).

Observe that every vertex in _S_\\_X_ is also a root of _F_\\_X_. Hence, \(|S\backslash X|\le c(F,X)\le c(F,k-1)\le\text{OPT}(F,k)+1\) by lemma 4.

