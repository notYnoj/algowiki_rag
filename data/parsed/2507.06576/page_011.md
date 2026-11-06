the set of all 2_w_-diameter decompositions of _G_ such that every vertex in the connected component containing _r_ is within distance strictly less than _k_ from it. More precisely,

\(\mathcal{F}_{2w}^k(G,r)=\{F\in\mathcal{F}_{2w}(G)|rad_F(r)<k\}.\)

We now state a simple Lemma 2, which will be used in the proofs of Theorems 4, 5, and 7.

**Lemma 2.** _Let G be a graph and let x be a SDD(G,_2_w,p_) _for G. If H is a subgraph of G, then the distribution_

\(y_F=\sum_{F^\prime\in\mathcal{F}_{2w}(G)F^\prime\cap E(H)=F}x_{F^\prime}\text{\textit{for each}}F\in\mathcal{F}_{2w}(H),\)

_is a SDD(H,_2_w,p_) _for H._

_Proof._ Fix an edge \(e\in E(H)\). Then<tbc>

\(\sum_{e\in F}y_F=\sum_{e\in F}\sum_{F^\prime\in\mathcal{F}_{2w}(G)F^\prime\cap E(H)=F}x_{F^\prime}=\sum_{F^\prime\in\mathcal{F}_{2w}(G)e\in F^\prime} x_{F^\prime}\le p,\)

<tbc>where the inequality follows from the fact that _x_ is a _SDD(G,_2_w,p_) for _G_. Moreover, since \(y\ge 0\), we verify that _y_ forms a probability distribution:

\(\sum_{F\in\mathcal{F}_{2w}(H)}y_F=\sum_{F\in\mathcal{F}_{2w}(H)}\sum_{F^\prime\in\mathcal{F}_{2w}(G)F^\prime\cap E(H)=F}x_{F^\prime}=\sum_{F^\prime\in\mathcal{F}_{2w}(G)}x_{F^\prime}=1.\)

Thus, _y_ is a _SDD(H,_2_w,p_) for _H_.

**Definition 5** (Projection of a _SDD_)**.** _Let G be a graph and let x be a SDD(G,_2_w,p_) _for G. For a subgraph_ \(H\subseteq G\)_, the projection of x onto H is the distribution_<tbc>

\(x(H)=\big(y_F\big)_{F\in\mathcal{F}_{2w}(H)},\)

<tbc>_where for each_ \(F\in\mathcal{F}_{2w}(H)\),

\(y_F=\sum_{F^\prime\in\mathcal{F}_{2w}(G)F^\prime\cap E(H)=F}x_{F^\prime}.\)

_By Lemma 2, x(H_) _is a SDD(H,_2_w,p_) _for H._

In Theorem 4, we show that if G is closed under the 1-sum operation and is _SDD_(2_w,p_)- acceptable, then for any \(G\in\mathcal{G}\) and \(r\in V(G)\), there exists an _SDD(G,_2_w,p_) over the family of 2_w_-diameter decompositions F<sub>2_w_</sub>(_G_) such that, when sampling a decomposition \(F\in\mathcal{F}_{2w}(G)\) from this distribution, we are guaranteed that \(rad_F(r)\le w-1\), i.e., \(F\in\mathcal{F}_{2w}^w(G,r)\). This condition is directly analogous to the first item of Observation 1.

**Theorem 4.** _Suppose that_ G _is closed under the_ 1_-sum operation and is SDD_(2_w,p_)_- acceptable. Let_ \(G\in\mathcal{G}\) _and let_ \(r\in V(G)\) _be an arbitrary vertex. Then there exists an SDD(G,_2_w,p), i.e., a distribution_ \(y=\{y_F|F\in\mathcal{F}_{2w}(G)\}\)_, such that_

\(\sum_{F\in\mathcal{F}_{2w}^w(G,r)}y_F=1,\)

_meaning that every sampled_ 2_w-diameter decomposition F from this distribution satisfies_ \(rad_F(r)\le w-1\).

