## Definition of a Witness:

To prove Theorem 8.14 we define a witness for _OPT_ and show that this witness is 2-WL invariant.

• \(W=\{X|X\subseteq\mathbb{N}_{\ge 0}\times\mathbb{R}_{\ge 0}\times\mathbb{R}_{\ge 0}\}\),<tbc>

• \(\mathrm{cost}(X)=\sum_{(n,c,d)\in X}n\cdot c\),<tbc>

• Let _T_ be a graph. We say that _T_ is a _X-colored tree_ if<tbc>

– _T_ is a tree where each vertex has the same color,<tbc>

– each edge in _T_ is colored with a color (_c,d_), and<tbc>

**–** for each \((n,c,d)\in X\) the tree _T_ contains exactly _n_ edges of color (_c,d_).<tbc>

<tbc>We define<tbc>

<tbc>\(\mathrm{check}(G,X)=\left|\left\{T:T\text{is a spanning tree of}G\text{and}T\text{is}X\text{-colored and}\sum_{(n,c,d)\in X}n\cdot d\le B\right\}\right|,\)<tbc>

<tbc>where _B_ is the budget associated with the input graph _G_. This means that check(_G,X_)=0, whenever _X_ is outside the budget constraint of _B_

**Lemma 8.15.** _The triple_ \((W,\mathrm{check}:\mathcal{G}\times W\rightarrow\mathbb{R},\mathrm{cost}:W\rightarrow\mathbb{R})\) _is a witness function of OPT._

_Proof._ Let \(G\in\mathcal{G}\) and \(X\in W\) and assume that check(_G,X)\>_0. By the definition of check(_G,X_), we obtain that there is _X_-colored spanning tree _T_ of _G_. For each \((n,c,d)\in X\), the tree _T_ uses edges of color (_c,d_) exactly _n_ times. Further, since check(_G,X)\>_0 we obtain

\(\ell(T)=\sum_{(n,c,d)\in X}n\cdot d\le B\text{and}c(T)=\sum_{(n,c,d)\in X}n\cdot c=\mathrm{cost}(X).\)

Thus, _T_ is a feasible tree of length at most _B_. Additionally, \(OPT(G)\le\mathrm{cost}(X)\) since _T_ has cost cost(_X_).

Next, assume that \(OPT(G)<\infty\). Now, there is a spanning tree _T_<sup>∗</sup> with \(\sum_{(n,c,d)\in X}n\cdot d\le B\) and _OPT(G_)=_c(T_<sup>∗</sup>). Let _X_ be the set that contains (_n,c,d_) if and only if the edge color (_c,d_) is used _n_ times in _T_<sup>∗</sup>. Note that \(OPT(G)=c(T^*)=\sum_{(n,c,d)\in X}n\cdot d=\mathrm{cost}(X)\). Since _T_<sup>∗</sup> is by definition a _X_-colored spanning tree, we obtain that check(_G,X)\>_0. Thus, _OPT_<sub>CST</sub>(_G_)=cost(_X_) and check(_G,X)\>_0.

We prove the following lemma which together with Lemma 8.15 immediately yields Theorem 8.14.

**Lemma 8.16.** _The function_ \(\mathrm{check}:\mathcal{G}\times W\rightarrow\mathbb{R}\) _is 2-WL invariant on_ G.

_Proof (sketch)._ To prove Lemma 8.16 we show that check(_G,X_)=check(_H,X_) for all \(G,H\in\mathcal{G}\) with \(G\equiv_{2\text{-WL}}H\) and \(X\in W\). Without loss of generality we assume that _X_ satisfies \(\sum_{(n,c,d)\in X}n\cdot d\le B\) since otherwise 0=check(_G,X_)=check(_H,X_)=0. We start with the Kirchhoff polynomial (see \[CY00\])

\(\mathrm{Kir}(G):=\sum_T\prod_{e\in T}X_e,\)

where each edge _e_ in _G_ has its own variable _X<sub>e</sub>_ and the sum is over all spanning trees _T_ of _G_. If we substituted each _X<sub>e</sub>_ with a new variable _c(e_), where _c(e_) is the color of the edge _e_, then we get the _Spanning Tree Polynomial P<sub>ST</sub>(G_) from Section 6.2. Formally, we have \(\mathrm{Kir}(G)|_{X_e=c(e)}\equiv P_{ST}(G)\), where Kir(_G_)|<sub>_X<sub>e</sub>=c(e_)</sub> is obtained by substituting _X<sub>e</sub>_ with _c(e_) in Kir(_G_).

