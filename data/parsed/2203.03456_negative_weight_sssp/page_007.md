**Definition 2.3** \((G_s,w_s,G^B,w^B,G_s^B,w_s^B)\)**.** Given any graph _G_=(_V,E,w_), we let \(G_s=(V\cup\{s\},E\cup\{(s,v)\}_{v\in V},w_s)\) refer to the graph _G_ with a dummy source _s_ added, where there is an edge of weight 0 from _s_ to _v_ for every \(v\in V\) and no edges into _s_. Note that _G<sub>s</sub>_ has a negative-weight cycle if and only if _G_ does and that \(dist_{G_s}(s,v)=min_{u\in V}dist_G(u,v)\).

For any integer _B_, let _G<sup>B</sup>_=(_V,E,w<sup>B</sup>_) denote the graph obtained by adding _B_ to all negative edge weights in _G_, i.e. _w<sup>B</sup>(e_)=_w(e_)+_B_ for all \(e\in E^{neg}(G)\) and _w<sup>B</sup>(e_)=_w(e_) for \(e\in E\backslash E^{neg}(G)\). Note that (_G<sup>B</sup>)<sub>s</sub>_=(_G<sub>s</sub>)<sup>B</sup>_ so we can simply write \(G_s^B=(V\cup\{s\},E\cup\{(s,v)\}_{v\in V},w_s^B)\).

**Definition 2.4** \((\eta_G(v),P_G(v))\)**.** For any graph _G_=(_V,E,w_) and \(s\in V\) such that _s_ can reach all vertices in _V_ , define<tbc>

\(\eta_G(v;s):=\left\{\begin{array}{ c c }
\infty & \text{if}dist_G(s,v)=-\infty \\
min\{|E^{neg}(G)\cap P|:P\text{is a shortest}sv\text{-path in}G\}; & \text{otherwise.}
\end{array}\right.\)

<tbc>Let \(\eta(G;s)=max_{v\in V}\eta_G(v;s)\). When \(dist_G(s,v)\neq-\infty\), let _P<sub>G</sub>(v;s_) be a shortest _sv_-path on _G_ such that

\(|E^{neg}(G)\cap P_G(v)|=\eta_G(v).\) (1)

We omit _s_ when _s_ is the dummy source in _G<sub>s</sub>_ defined in Definition 2.3; i.e. \(\eta_G(v)=\eta_{G_s}(v;s)\), \(\eta(G)=\eta(G_s;s)\), and _P<sub>G</sub>(v_)=_P<sub>G<sub>s</sub></sub>(v;s_). Further, the graph _G_ is omitted if the context is clear.

## 2.1 Price Functions and Equivalence

Our algorithm heavily relies on price functions--an idea with deep roots, traceable to Dreyfus’ 1969 survey \[Dre69\] and Braess’ work \[Bra71, Page 176\], if not earlier--and which also appeared in the well-known _A_<sup>∗</sup> algorithm (referred to as a heuristic function in the AI community).<sup>10</sup>

**Definition 2.5** (Price Function)**.** Consider a graph _G_=(_V,E,w_) and let \(\phi\) be any function: \(V\rightarrow\mathbb{Z}\), where Z is the set of integers. Then, we define \(w_\phi\) to be the weight function \(w_\phi(u,v)=w(u,v)+\phi(u)-\phi(v)\) and we define \(G_\phi=(V,E,w_\phi)\). We will refer to \(\phi\) as a _price_ function on _V_ . Note that \((G_\phi)_\psi=G_{\phi+\psi}\).

**Definition 2.6** (Graph Equivalence)**.** We say that two graphs _G_=(_V,E,w_) and \(G'=(V,E,w')\) are _equivalent_ if **(1)** any shortest path in _G_ is also a shortest path in \(G'\) and vice-versa and **(2)** _G_ contains a negative-weight cycle if and only if \(G'\) does.

**Lemma 2.7** (\[Joh77\])**.** _Consider any graph G_=(_V,E,w_) _and price function_ \(\phi\)_. For any pair_ \(u,v\in V\) _we have_ \(dist_{G_\phi}(u,v)=dist_G(u,v)+\phi(u)-\phi(v)\)_, and for any cycle C we have_ \(w(C)=w_\phi(C)\)_. As a result, G and_ \(G_\phi\) _are equivalent. Finally, if_ \(G'=(V,E,w)\), \(G'=(V,E,w')\) _and_ \(w'=c\cdot w(e)\) _for some positive c, then G and_ \(G'\) _are equivalent._

The overall goal of our algorithm will be to compute a price function \(\phi\) such that all edge weights in \(G_\phi\) are non-negative (assuming no negative-weight cycle); we can then run Dijkstra on \(G_\phi\). The lemma below, originally used by Johnson, will be one of the tools we use.

**Lemma 2.8** (\[Joh77\])**.** _Let G_=(_V,E_) _be a directed graph with no negative-weight cycle and let s be any vertex in G that can reach all vertices in V. Let_ \(\phi(v)=dist_G(s,v)\) _for all_ \(v\in V\)_. Then, all edge weights in_ \(G_\phi\) _are non-negative. (The lemma follows trivially from the fact that_ \(dist(s,v)\le dist(s,u)+w(u,v)\)_.)_

<sup>10</sup>We thank Donald E. Knuth for the historical note regarding price functions.

