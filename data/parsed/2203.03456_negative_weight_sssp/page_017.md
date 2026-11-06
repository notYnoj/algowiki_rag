**Running Time Analysis:** By Corollary 5.2, if _G<sub>in</sub>_ does not contain a negative-weight cycle then the algorithm does not terminate, as desired. We now focus on the case where _G<sub>in</sub>_ does not contain a negative-weight cycle. The running time of the algorithm is dominated by the log(_B_)=_O_(log(_n_)) calls to Scale\(\mathrm{Down}(\bar{G}_{\phi_{i-1}},\Delta:=n,B/2^i)\). Note that all the input graphs \(\bar{G}_{\phi_{i-1}}\) are equivalent to _G<sub>in</sub>_, so they do not contain a negative-weight cycle. By Theorem 3.5, the expected runtime of each call to ScaleDown is \(O(m\mathrm{log}^3(n)\mathrm{log}(\Delta))=O(m\mathrm{log}^4(n))\). So, the expected runtime of SPmain is _O(m_log<sup>5</sup>(_n_)).

## 6 Algorithm for Low-Diameter Decomposition

In this section, we prove Lemma 1.2 which we restate here for convenience. Through this section, we often shorten LowDiamDecomposition(_G,D_) to LDD(_G,D_).

**Lemma 1.2.** _There is an algorithm_ LowDiamDecomposition(_G,D_) _with the following guarantees:_

• _INPUT: an m-edge, n-vertex graph G_=(_V,E,w_) _with non-negative integer edge weight function w and a positive integer D._<tbc>

• _OUTPUT: A set of edges E<sup>rem</sup> with the following guarantees:_<tbc>

– _each SCC of G_\\_E<sup>rem</sup> has weak diameter at most D; that is, if u,v are in the same SCC, then_ \(\mathrm{dist}_G(u,v)\le D\) _and_ \(\mathrm{dist}_G(v,u)\le D\).<tbc>

**–** _For every_ \(e\in E\), \(\mathrm{Pr}[e\in E^{rem}]=O\left(\frac{w(e)\cdot\mathrm{log}^2n}{D}+n^{-10}\right)\)_. These probabilities are not guaranteed to be independent._<sup>17</sup><tbc>

• _RUNNING TIME: The algorithm has running time O(m_log<sup>2</sup>_n+n_log<sup>3</sup>_n)._

We start with some basic definitions.

**Definition 6.1** (balls and boundaries)**.** Given a directed graph _G_=(_V,E_), a vertex \(v\in V\) , and a distance-parameter _R_, we define \(\mathrm{Ball}_\mathrm{G}^\mathrm{out}(v,R)=\{u\in V|\mathrm{dist}(v,u)\le R\}\). We define \(\partial\mathrm{Ball}_\mathrm{G}^\mathrm{out}(v,R)=\{(x,y)\in E|x\in\mathrm{Ball}_\mathrm{G}^\mathrm{out}(v,R)\wedge y\notin\mathrm{Ball}_\mathrm{G}^\mathrm{out}(v,R)\}\). Similarly, we define \(\mathrm{Ball}_\mathrm{G}^\mathrm{in}(v,R)=\{u\in V|\mathrm{dist}(u,v)\le R\}\) and we define \(\partial\mathrm{Ball}_\mathrm{G}^\mathrm{in}(v,R)=\{(x,y)\in E|y\in\mathrm{Ball}_\mathrm{G}^\mathrm{in}(v,R)\wedge x\notin\mathrm{Ball}_\mathrm{G}^\mathrm{in}(v,R)\}\). We often use \(\mathrm{Ball}_\mathrm{G}^*\) to denote that a ball can be either an out-ball or an in-ball, i.e., \(*\in\{in,out\}\).

**Definition 6.2** (Geometric Distribution)**.** Consider a coin whose probability of heads is \(p\in(0,1]\). The geometric distribution Geo(_p_) is the probability distribution of the number _X_ of independent coin tosses until obtaining the first heads. We have Pr\[_X=k_\]=_p_(1-_p_)<sup>_k_-1</sup> for every \(k\in\{1,2,3,\dots\}\).

**Remark 6.3.** _In Lemma 1.2 and throughout this section, n always refers to the number of vertices in the main graph G<sub>in</sub>, i.e. graph in which we are trying to compute shortest paths. This is to ensure that "high probability" is defined in terms of the number of vertices in G<sub>in</sub>, rather than in terms of potentially small auxiliary graphs. Note that whenever our shortest path algorithm executes_ LDD(_G,D_) _we always have_ \(|V(G)|\le n\) _(we never add new vertices)._

**The algorithm.** The pseudocode for our low-diameter decomposition algorithm can be found in Algorithm 3. Roughly, in Phase 1 each vertex is marked as either _in-light, out-light_, or _heavy_. In Phase 2 we repeatedly "remove" balls centered at either in-light or out-light vertices: Let _v_ be any in-light vertex (the process is similar for out-light vertices). Consider a ball \(\mathrm{Ball}_\mathrm{G}^\mathrm{in}(v,R_v)\) with radius _R<sub>v</sub>_ selected randomly from the geometric distribution Geo(_p_), with _p_=min{1,80log(_n)/D_} (Lines 12 and 13)<sup>18</sup>. We add edges pointing into this ball (i.e. edges in \(\partial\mathrm{Ball}_\mathrm{G}^\mathrm{in}(v,R_v)\)) to _E<sup>boundary</sup>_,<tbc>

<sup>17</sup>The 10 in the exponent suffices for our application but can be replaced by an arbitrarily large constant. <sup>18</sup>Throughout this section, log(_n_) always denotes log<sub>2</sub>(_n_)

