**Definition 8.1** (\(\ell\)-WL Equivalence)**.** Two (attributed) graphs _G_ and _H_ are \(\ell\)_-WL equivalent_ \((G\equiv_{\ell\text{-}\text{WL}}H)\) if \(\left\{\left\{\chi_\infty^{G,\ell}(\bar{v})|\bar{v}\in(V(G))^\ell\right\}=\left\{\left\{\chi_\infty^{H,\ell}(\bar{w})|\bar{w}\in(V(H))^\ell\right\}\right\}\).

Observe that isomorphic (attributed) graphs _G,H_ are always \(\ell\)-WL equivalent.

Given an (attributed) graph _G_, the coloring \(\chi_\infty^{G,\ell}\) can be computed in time \(O(n^{\ell+1}logn)\) \[IL90\] (more precisely, similar to Theorem 7.9, we compute a coloring equivalent to \(\chi_\infty^{G,\ell}\)). Moreover, similar to Theorem 7.10, we can compute a complete invariant for \(\ell\)-WL equivalence (see, e.g., \[Ott17\]). In turn, this can be used as an Invariant and Solution-Preserving Signature for problems such as Constrained Spanning Tree (see Section 8.4).

**Theorem 8.2.** _Let_ \(\ell\ge 2\)_. There is a deterministic algorithm that, given an attributed graph G, outputs a string_ \(\text{WL}_\ell(G)\in\{0,1\}^*\) _in time_ \(O(|V(G)|^{\ell+1}log|V(G)|)\)_, such that for every two input graphs G,H it holds that_ \(G\equiv_{\ell\text{-}\text{WL}}H\) _if and only if_ \(\text{WL}_\ell(G)=\text{WL}_\ell(H)\).

## 8.2 \(\ell\)-WL Invariant Functions are in the Isomorphic-Priors Model

A function _f_ on (attributed) graphs is called \(\ell\)_-WL invariant_ if _f(G_)=_f(H_) for all (attributed) graphs _G,H_ with \(G\equiv_{\ell\text{-}\text{WL}}H\).<sup>25</sup> We say that an optimization problem \(\Pi\) is \(\ell\)_-WL invariant_ if \(OPT_\Pi\) is \(\ell\)-WL invariant (where \(OPT_\Pi\) denotes the function that maps an (attributed) input graph to the value of an optimum solution). For such problems, we obtain polynomial-time algorithm in the Isomorphic-Priors model using similar arguments as in Section 7.

**Theorem 8.3.** _Let_ \(\ell\ge 2\) _and let_ \(\Pi\) _be an optimization problem that is_ \(\ell\)_-WL invariant._

_Then there is an algorithm that solves_ \(\Pi\) _with k prior instances each of size at most n in_ \(O(kn^{\ell+1}logn)\) _preprocessing time and_ \(O(n^{\ell+1}logn)\) _query time._

_Proof._ Write S:={_G<sub>i</sub>_}<sub>_i_=1_...k_</sub> for the prior instances. We describe the different phases of the algorithm.

**Preprocessing:** For each graph \(G_i\in\mathcal{S}\), we compute a complete invariant \(\text{WL}_\ell(G)\in\{0,1\}^*\) for _G<sub>i</sub>_ using Theorem 8.2 in time \(O(n^{\ell+1}logn)\) time. We insert each string \(\text{WL}_\ell(G_i)\in\{0,1\}^*\) into a binary search tree, where the _i_-th letter determines whether we take the left/right subtree on the _i_-th level. This takes time proportional to the length of the string \(\text{WL}_\ell(G_i)\), i.e., it can be done in time \(O(n^{\ell+1}logn)\). For the corresponding node where the key \(\text{WL}_\ell(G_i)\) is saved, we save \(OPT_\Pi(G_i)\).

Note that, if two graphs \(G_i,G_j\in\mathcal{S}\) have the same complete invariant, they are \(\ell\)-WL equivalent (Theorem 8.2). In particular, since \(\Pi\) is \(\ell\)-WL invariant, we get that \(OPT_\Pi(G_i)=OPT_\Pi(G_j)\), and no conflicting values can be assigned to a single node of the search tree. Overall, processing all _k_ graphs takes \(O(kn^{\ell+1}logn)\) time.

**Query:** Given the query graph _H_, we compute a complete invariant \(\text{WL}_\ell(H)\in\{0,1\}^*\) for _G<sub>i</sub>_ using Theorem 8.2 in time \(O(n^{\ell+1}logn)\) time. Looking up the computed invariant in the binary search tree takes \(O(n^{\ell+1}logn)\) time, allowing us to return \(OPT_\Pi(H)=OPT_\Pi(G_i)\) (which is correct since \(\Pi\) is \(\ell\)-WL invariant). If the string \(\text{WL}_\ell(H)\) is not contained in the search tree, then we can correctly claim that _H_ is not isomorphic to any graph in S because graphs that are not \(\ell\)-WL equivalent are not isomorphic. The total query time is \(O(n^{\ell+1}logn)\).

For 1-WL invariant optimization problems, we obtain the following variant which is proved analogously using Theorem 7.10.

**Theorem 8.4.** _Let_ \(\Pi\) _be an optimization problem that is 1-WL invariant. Then there is an algorithm that solves_ \(\Pi\) _with k prior instances each of size at most n in O(k(n+m_)log_n_) _preprocessing time and O_((_n+m_)log_n_) _query time._

<sup>25</sup>In the literature (see, e.g., \[GGR24\]), the minimal \(\ell\ge 1\) (if it exists) such that _f_ is \(\ell\)-WL invariant is also called the _WL dimension_ of _f_.

