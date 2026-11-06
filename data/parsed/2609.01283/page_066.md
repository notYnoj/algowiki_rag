If _S_ is independent in \(M^{\vee k}\), we have shown that _P<sub>S</sub>_:=det(_U<sub>R,S</sub>_) is a non-zero polynomial for some _R_. The degree of _P<sub>S</sub>_ is at most \(s\le kr\) (each variable appears with degree at most 1). By the Schwartz-Zippel lemma, under a uniformly random assignment from F to the variables:

\(Pr[P_S=0]\le\frac{deg(P_S)}{|\mathbb{F}|}\le\frac{kr}{|\mathbb{F}|}.\)

This proves the first claim as F is of size poly(_kr_). To establish the second claim, note that any set \(S\subseteq E\) which is dependent in \(M^{\vee k}\) yields the identically zero polynomial for all choices of _R_. So, such sets remain deterministically dependent under any field assignment. \(\square\)

## A.4 Extension of Perfect \(\alpha\)-factor Sensitivity Oracle to Maximum \(\alpha\)-factor

We extend the sensitivity oracle results of the (perfect) \(\alpha\)-factor (Theorems 7.8 and 8.13) to the (maximum) \(\alpha\)-factor, achieving near-identical bounds. Using the terminology from \[GS21a\], the (maximum) \(\alpha\)-factor treats \(\alpha(v)\) as an upper bound on the desired degree of _v_, and the objective is to maximize the total number of edges picked. In contrast, the (perfect) \(\alpha\)-factor treats \(\alpha(v)\) as the exact required degree for _v_, and the oracle strictly answers its existence.

Given a graph _G_=(_V,E_), the function \(\alpha\), edge costs \(c:E\rightarrow[-W,W]\), a precomputed min-cost (maximum) \(\alpha\)-factor _M_ of _G_, and a parameter _f\>_0, we first define the _deficiency def(v_) for any vertex \(v\in V\) as the difference between \(\alpha(v)\) and the number of edges incident to _v_ in _M_. Let \(\delta_M(v)\) denote the set of edges incident to _v_ in _M_. Hence, \(def(v)=\alpha(v)-|\delta_M(v)|\). By definition, \(def(v)\ge 0\).

We now construct an auxiliary undirected graph G from _G_ by adding three dummy vertices _z_<sub>1</sub>_,z_<sub>2</sub>_,z_<sub>3</sub>, along with the following sets of zero-cost edges:

• _E_<sub>_z_<sub>1</sub></sub>: For all \(v\in V\) , add _def(v_)+_f_ parallel edges between _z_<sub>1</sub> and _v_.<tbc>

• _E<sub>triangle</sub>_: Add _f_ parallel edges between each of the pairs (_z_<sub>1</sub>_,z_<sub>2</sub>),(_z_<sub>2</sub>_,z_<sub>3</sub>), and (_z_<sub>3</sub>_,z_<sub>1</sub>).

This yields the graph G=(V,E), where \(\mathcal{V}=V\cup\{z_1,z_2,z_3\}\) and \(\mathcal{E}=E\cup E_{z_1}\cup E_{triangle}\).

We now define a function \(\beta\) over the vertices of G as follows: \(\beta(z_1)=2f+\sum_{v\in V}def(v)\); \(\beta(z_2)=\beta(z_3)=2f\); and \(\beta(v)=\alpha(v)\) for all \(v\in V\) . By construction, G admits a (perfect) \(\beta\)-factor using a subset of the edges of _M_, _E_<sub>_z_<sub>1</sub></sub>, and _E<sub>triangle</sub>_. Furthermore, the cost of the min-cost maximum \(\alpha\)-factor of _G_ is exactly equal to the cost of the min-cost perfect \(\beta\)-factor of G.

For any set of edge updates _U_ in graph _G_, we describe the corresponding updates U to the graph G. For an update to any edge \(e\in G\), we apply the identical update to _e_ in G. We then augment the set U into a parameterized set U_<sup>i</sup>_ for \(i\in[-f,f]\) with the following additional dummy-edge updates:

• If _i\>_0: delete _i_ edges between _z_<sub>2</sub> and _z_<sub>3</sub>; add _i_ zero-cost edges between both (_z_<sub>1</sub>_,z_<sub>3</sub>) and (_z_<sub>1</sub>_,z_<sub>2</sub>).<tbc>

• If \(i\le 0\): add |_i_| zero-cost edges between _z_<sub>2</sub> and _z_<sub>3</sub>; delete |_i_| edges between both (_z_<sub>1</sub>_,z_<sub>3</sub>) and (_z_<sub>1</sub>_,z_<sub>2</sub>).

The following lemma establishes the equivalence between the two factors under these updates:

**Lemma A.3.** _The cardinality of the maximum_ \(\alpha\)_-factor of G+U is equal to_ |_M_|+_i_<sup>∗</sup>_, where i_<sup>∗</sup> _is the maximum possible integer_ \(i\in[-f,f]\) _such that the graph_ G+U_<sup>i</sup> admits a perfect_ \(\beta\)_-factor. Furthermore, the cost of the minimum-cost maximum_ \(\alpha\)_-factor of G+U is equal to the cost of the minimum-cost perfect_ \(\beta\)_-factor of_ G+U_<sup>i<sup>∗</sup></sup>.

