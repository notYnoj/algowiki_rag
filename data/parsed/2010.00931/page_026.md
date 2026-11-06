## 6. Static optimality

As discussed in §1, Splay trees have several powerful adaptive properties, including static optimality. In this section we prove a similar property of our generalized SplayTT algorithm from §5.

**Theorem 3.** _Let S be a tree of size n and let X be a sequence of m searches over the nodes of S. Let_ OPT(_X_) _denote the minimum cost of serving X in a static search tree on S. Then the cost of SplayTT for serving X is_ O(OPT(_X_)+_n_<sup>2</sup>).

Let \(R'\) be an _optimal tree_ for the search sequence _X_, i.e. so that \(\mathtt{cost}_{R^\prime}(X)=\mathtt{OPT}(X)\). By Lemma 1, there is a Steiner-closed search tree _R_ on _S_ with \(\mathtt{cost}_R(X)\le 2\cdot\mathtt{OPT}(X)\). It is important to note that neither _X_, nor \(R',R\) are known to the algorithm, and are only used in the analysis. The initial state of SplayTT is an _arbitrary_ Steiner-closed STT on _S_. Let _T_ denote the state of the search tree before the operation search(_x_). As before, let _T<sub>x</sub>_ denote the subtree of _T_ rooted at _x_, and let us denote its node set _N<sub>x</sub>=V(T<sub>x</sub>_).

We define the _node-potential_ \(\phi(x)=-\mathrm{min}_{y\in N_x}\left\{\mathtt{depth}_R(y)\right\}\) for all \(x\in V(S)\). In words, the node potential is, without the minus sign, the smallest depth (in _R_) of _x_ or a descendant of _x_ (in T). The _total potential_ is \(\phi(T)=d\cdot\sum_{x\in V(T)}\phi(x)\), for a constant _d\>_0 to be chosen later.<sup>3</sup>

We next bound the amortized cost of searching in _T_ by Algorithm 4 in terms of the cost in the optimal tree _R_. Let \(T'\) denote the tree after searching _x_.

**Lemma 16.** _With the above definitions, for some constant c\>_0,

\(\mathtt{depth}_T(x)+\phi(T')-\phi(T)\le c\cdot\mathtt{depth}_R(x).\)

Before proving Lemma 16, we make some easy observations.

**Lemma 17.** _For an arbitrary tree T of size n and_ \(\phi\) _defined as above:_

(_i)_ _The node potential satisfies_ \(-\mathtt{depth}_R(x)\le\phi(x)\le-1\) _for all_ \(x\in V(T)\).<tbc>

(_ii)_ _The total potential satisfies_ \(-dn^2\le\phi(T)\le 0\).<tbc>

_(iii)_ _If x is an ancestor of y in T, then_ \(\phi(x)\ge\phi(y)\).<tbc>

_(iv)_ _For every subtree S_\[_A_\] _of S, there is a unique_ \(x\in A\) _that minimizes_ depth_<sub>R</sub>(x)._<sup>4</sup>

Lemma 16 and Lemma 17(ii) together imply Theorem 3 by a standard amortization argument: since the work performed by SplayTT is at most \(c'\cdot\mathtt{depth}_T(x)\), for some constant \(c'>0\), by scaling \(\phi\) with the same constant, we obtain the upper bound \(cc'\cdot\mathtt{depth}_R(x)\in\mathcal{O}(\mathtt{depth}_R(x))\) on the amortized cost of searching. This telescopes over the sequence of searches, yielding the bound _O_(OPT(_X_)) on cost_<sub>T</sub>(X_), with an additive term _O(n_<sup>2</sup>) due to the final potential.

In the remainder we prove the two lemmas.

<sup>3</sup>The potential function is inspired by a similar one suggested by T. Saranurak for the analysis of classical Splay \[CGK<sup>+</sup>16, §3.2\]. For Splay (i.e. in the BST setting) the corresponding potential function can be seen to be essentially equivalent to the classical "sum-of-logs" potential of Sleator and Tarjan, but this seems not to be the case in the STT setting. <sup>4</sup>This property can be interpreted as saying that _depth in R_ gives a _unique minimum coloring_ (see e.g. \[ES14\]) of the hypergraph formed by nodes and subtrees of _S_.

