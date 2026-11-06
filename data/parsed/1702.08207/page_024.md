## 6 Proof of Theorem 3.4: A \(O(\sqrt{logn})\)-Approximation Algorithm

We start with some notation. Given a tree _T_=(_V,E,w_) and a fixed value of parameter \(\alpha\), we find a subtree _T_<sup>∗</sup>=(_V_<sup>∗</sup>_,E_<sup>∗</sup>) of the input tree _T_, called an \(\alpha\)_-separating tree_, that satisfies: _r(T_<sup>∗</sup>)=_r(T_) and each connected component of _T_\\_V_<sup>∗</sup> has at most \(\alpha\) vertices. An \(\alpha\)-separating tree _T_<sup>∗</sup> is _minimal_ if the removal of any leaf from _T_<sup>∗</sup> gives an induced tree that is not an \(\alpha\)- separating tree. Then, for a target node \(x\in V\) , we introduce a recursive strategy R that takes the following steps:

1. R first applies strategy A<sup>∗</sup> restricted to tree _T_<sup>∗</sup> to locate the node \(x'\) of _T_<sup>∗</sup> which is closest to the target _x_.<tbc>

2. Then, R queries \(x'\), which either completes the search in case when \(x'\) is the target or provides a neighbor \(x''\) of \(x'\) that is closer to the target than \(x'\).<tbc>

3. If \(x'\) is not the target, then the strategy calls itself recursively on the subtree \(T_{x^{\prime\prime}}\) of \(T\backslash\{x'\}\) containing _x_. The latter strategy for \(T_{x^{\prime\prime}}\) is denoted by \(\mathcal{R}_{x^{\prime\prime}}\). (Note that \(T_{x^{\prime\prime}}\) is a connected component in _T_\\_V_<sup>∗</sup>.)

Such a search strategy R obtained from A<sup>∗</sup> and strategies \(\mathcal{R}_{r(T^\prime)}\) (constructed recursively) for subtrees \(T'\) in _T_\\_V_<sup>∗</sup> is called a \((\mathcal{A}^*,\{\mathcal{R}_{r(T^\prime)}\big|T'\in\mathcal{C}(T\backslash V^*)\})\)_-strategy_, where C(_T_\\_V_<sup>∗</sup>) is the set of connected components (subtrees) in _T_\\_V_<sup>∗</sup>.

The following bound on the cost of the strategy R follows directly from the construction:

**Lemma 6.1.** _For a_ \((\mathcal{A}^*,\{\mathcal{R}_{r(T^\prime)}\big|T'\in\mathcal{C}(T\backslash V^*)\})\)_-strategy_ R _for T it holds_

\(\mathtt{COST}_\mathcal{R}(T)\le\mathtt{COST}_{\mathcal{A}^*}(T^*)+max_{x^\prime\in V^*}w(x')+max_{T^\prime\in\mathcal{C}(T\backslash V^*)}\mathtt{COST}_{\mathcal{R}_{r(T^\prime)}}(T').\)

We now formally describe and analyze the aforementioned contractions of subpaths in a tree. A maximal path with more than one node in a tree _T_ that consists only of vertices that have degree two in _T_ is called a _long chain in T_. For each long chain _P_, contract it into a single node _v<sub>P</sub>_ with weight \(min_{u\in V(P)}w(u)\), obtaining a tree \(\xi(T)\). In what follows, the tree \(\xi(T)\) is called a _chain-contraction of T_.

Our first step is a remark that, at the cost of losing a multiplicative constant in the final approximation ratio, we may restrict ourselves to trees that have no long chains. This is due to the following observation.

**Lemma 6.2.** _Let T be a tree. Given a p-approximate search strategy for_ \(\xi(T)\)_, a_ (_p_+1)_- approximate search strategy for T can be computed in polynomial time._

_Proof._ Let \(\mathcal{A}'\) be a search strategy for \(\xi(T)\). We obtain a search strategy A for _T_ in two stages. In the first stage we ‘mimic’ the behavior of \(\mathcal{A}'\): (i) if \(\mathcal{A}'\) queries a node _v_ that also belongs to _T_, then A also queries _v_; (ii) if \(\mathcal{A}'\) queries a node _v<sub>P</sub>_ that corresponds to some long chain _P_ in _T_, then A queries, in _T_, a node with minimum weight in _P_. Note that after the first stage, the search strategy either located the target or determined that the target belongs to a subpath \(P'\) of some long chain _P_ of _T_. Moreover, the total cost of all queries performed in the first stage is at most \(\mathtt{COST}_{\mathcal{A}^\prime}(\xi(T))\).

Then, in the second stage we compute (in _O(n_<sup>2</sup>)-time) an optimal search strategy \(\mathcal{A}_{P^\prime}\) for \(P'\) \[6\]. Due to the monotonicity of the cost over taking subgraphs, \(\mathtt{COST}_{\mathcal{A}_{P^\prime}}(P')=\mathtt{OPT}(P')\le\mathtt{OPT}(T)\).

Both stages provide us with a search strategy for _T_ with cost at most \(\mathtt{COST}_{\mathcal{A}^\prime}(\xi(T))+\mathtt{OPT}(T)\). Since, \(\mathtt{OPT}(\xi(T))\le\mathtt{OPT}(T)\) and \(\mathtt{COST}_{\mathcal{A}^\prime}(\xi(T))\le p\cdot\mathtt{OPT}(\xi(T))\), the lemma follows.

