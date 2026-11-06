## C Reduction from Dynamic DDG to Incremental DDG in the Offline Setting

In this section, we give a simple reduction from the problem of maintaining a DDG on a dynamic graph to maintaining it on an incremental graph. For concreteness, we tailored the reduction to the guarantees of our incremental data structure but it is straight-forward to generalize the reduction further. From the reduction below, combined with Theorem 5.1, we immediately obtain our main Theorem 2.3 as a corollary.

**Theorem C.1.** _Given an offline data structure_ I_, that for any graph H, an r-capped recursive decomposition_ R_<sub>H</sub> of H with roots H_<sub>1</sub>_,H_<sub>2</sub>_,...,H<sub>k</sub>, and any i, maintains the DDGs of all nodes in the tree rooted at H<sub>i</sub>, with preprocessing time_ \(\tilde{O}(r)\)_, handles each edge weight decrease affecting H<sub>i</sub> in worst-case update time_ \(\tilde{O}(\sqrt{r})\) _and has query time_ \(\tilde{O}(1)\).

_Then there exists an_ offline _data structure_ F_, that given dynamic graph G along with an r- capped recursive decomposition_ R _with roots_ \(G_1,G_2,\dots,G_{k^\prime}\)_, for all j maintains the DDGs of all pieces in the tree rooted at G<sub>j</sub> with pre-processing time_ \(\tilde{O}(r)\) _and amortized update time_ \(\tilde{O}(\sqrt{r})\) _and query time_ \(\tilde{O}(1)\).

_If_ I _is fully-persistent, we can turn the update and query time guarantees of_ F _into worst-case guarantees._

We prove the theorem for the root nodes \(G_1,G_2,\dots,G_{k^\prime}\). This is without loss of generality since the children of these nodes form an _r/_2-capped recursive decomposition and the data structure I can be applied to them and so on recursively, all at the cost of an additional \(\tilde{O}(1)\) factor.

In the end of this section, we argue that standard de-amortization techniques can be used to achieve worst-case update and query time. Let us now state additional preliminaries and components required by our dynamic data structure.

### Additional Notation.

We let \(\tau\) be the number of updates that _G_ is undergoing and assume \(\tau\) is a power of 2 and be polynomially bounded in _n_. We denote by _G<sup>t</sup>_=(_V,E,w<sup>t</sup>_) the graph _G after_ the _t<sup>th</sup>_ update is applied, and call each _G<sup>t</sup>_ a _version_ of _G_. In particular, _G_<sup>0</sup> is the initial graph _G_. Further, we define lg_x_=log<sub>2</sub>_x_, \(\lfloor x\rfloor\) to be shorthand for {0,1_,...,x_-1} and \(\lfloor x\rfloor_i\) to be shorthand for \(\lfloor x/2^i\rfloor\cdot 2^i\), i.e. _x_ rounded down to a power of 2_<sup>i</sup>_.

### A Graph Hierarchy.

We define a graph \(G_i^t=(V,E,\overline{w_i^t})\) for every \(0\le i\le\mathrm{lg}\tau\) and time _t_ to have the weight function defined for every \(e\in E\) by \(\overline{w_i^t}(e)=\mathrm{max}_{j\in[2^i]}w^{\lfloor t\rfloor_i+j}(e)\). We make the following straight-forward but nonetheless interesting observations.

**Observation C.2.** _For every_ \(0\le i\le\mathrm{lg}\tau\) _and time t being a multiple of_ 2_<sup>i</sup>, then for any_ \(j\in[2^i]\), \(G_{i+1}^t=G_{i+1}^{t+j}\).

**Observation C.3.** _For every_ \(0\le i<\mathrm{lg}\tau\) _and time t, we have that_ \(G_i^t\) _differs from_ \(G_{i+1}^t\) _by at most_ 2_<sup>i</sup> edge weight decreases. We denote these edge weight decreases by update sequence_ \(\Delta_i^t\).

For convenience, we also define \(\Delta_i^t\) for negative _t_, to simply be the empty set.

