<tbc>the processed graph. When its centre is forgotten and a leaf remains in the bag, the partial component already has at least two edges and receives label _L_.

At an introduce node, a newly active vertex is pending, is joined to a pending vertex to form a _K_<sub>2</sub>, or is attached to a known centre. These are exactly the listed transitions. At a forget node, a pending vertex cannot occur in the restriction of _D_, because it has no selected neighbour in the processed graph and no neighbour outside it. The other forget transitions preserve the canonical label and count the edge between two active vertices, if present.

At a join node, the two child partial solutions are restrictions of the same global packing and therefore activate the same bag vertices. For a singleton, a leaf with label _L_ in one child has no selected neighbour in the other child and hence meets label _P_ there. Otherwise the labels belong to {_P,C_}, whose merges are all listed. For a boundary edge _xy_, all counted attachments lie at the same endpoint, so its pair labels also combine by a valid merge. Induction now gives a DP computation representing _D_ and counting each of its edges exactly once.

Lemmas 6 and 7 imply that \(\mathrm{DP}[r,\varnothing]=\rho_\mathrm{e}^\circ(G)\).

### 4.4 Running time and reconstruction

Let _b<sub>t</sub>_=|_B<sub>t</sub>_|. A table contains one empty state, 3_b<sub>t</sub>_ singleton states, and \(3\genfrac(){pt}{2}{b_t}{2}\) pair states, hence _O_((_b<sub>t</sub>_+1)<sup>2</sup>) states. Leaf, introduce, and forget nodes can be processed in _O_((_b<sub>t</sub>_+1)<sup>2</sup>) time.

At a join node, states are grouped by their active subset. There is one label for the empty subset, three labels for each singleton subset, and three labels for each two-element subset. Thus, only constantly many label pairs are examined for each active subset, and a join node also takes _O_((_b<sub>t</sub>_+1)<sup>2</sup>) time. The nice decomposition has _O(n_<sup>2</sup>) nodes and \(b_t\le n\), so the total running time is _O(n_<sup>4</sup>).

For a disconnected graph with component orders _n_<sub>1</sub>_,...,n<sub>q</sub>_, the total running time is \(O(\sum_in_i^4)\subseteq O(n^4)\). To reconstruct an optimum packing, store a predecessor transition for every improving DP update and backtrack from the root. This does not change the asymptotic time bound.

**Theorem 8.** _For a chordal graph G on n vertices, the dynamic program computes_ \(\rho_\mathrm{e}^\circ(G)\) _and an optimum edge open packing in O(n_<sup>4</sup>) _time._

## 5 Maximum Edge Open Packing in Convex Bipartite Graphs

Let \(G=(X\cup Y,E)\) be a convex bipartite graph. Isolated vertices do not affect an edge open packing and are deleted first; if no edge remains, the optimum is zero. Let _X_={_x_<sub>1</sub>_,x_<sub>2</sub>_,...,x<sub>p</sub>_} be a convex ordering. For each \(y\in Y\) , write \(N(y)=\{x_{\ell(y)},x_{\ell(y)+1},\dots,x_{r(y)}\}\).

By Observation 1, the components of _G_\[_V(D_)\] for an edge open packing _D_ are stars _K_<sub>1_,t_</sub> with \(t\ge 1\). In particular, _K_<sub>2</sub> is included. Its centre may be chosen in either part; when describing an existing packing, we choose its endpoint in _X_. Since _X_ and _Y_ are independent sets, a collection of vertex-disjoint stars forms an edge open packing exactly when there is no edge between two distinct stars.

### 5.1 Separation properties

For a component _S_ of _G_\[_V(D_)\], define \(x_\mathrm{min}(S)=\mathrm{min}\{i:x_i\in V(S)\cap X\}\). Every component contains an edge, so this minimum is defined. List the components as _S_<sub>1</sub>_,...,S<sub>k</sub>_ in increasing order of _x_<sub>min</sub>; their minima are distinct because their vertex sets are disjoint. A _prefix_ is S_<sub>j</sub>_={_S_<sub>1</sub>_,...,S<sub>j</sub>_} for some \(0\le j\le k\), with \(\mathcal{S}_0=\varnothing\). A component _S<sub>t</sub>_ is _later_ than this prefix if _t\>j_.

**Claim 9.** _If a\<b, every X-vertex of S<sub>a</sub> has index smaller than x_<sub>min</sub>(_S<sub>b</sub>)._

_Proof._ Put _i=x_<sub>min</sub>(_S<sub>b</sub>_). An _X_-centred star contains just one _X_-vertex. Otherwise, if _S<sub>a</sub>_ contained _X_- vertices on both sides of index _i_, convexity would make its _Y_ -centre adjacent to _x<sub>i</sub>_, joining two distinct components. Equality of indices is excluded by vertex-disjointness.

For a prefix S, define \(\alpha(\mathcal{S})=\mathrm{max}\{i:x_i\in V(S)\cap X\text{for some}S\in\mathcal{S}\}\) and \(\beta(\mathcal{S})=\mathrm{max}\{r(y):y\in V(S)\cap Y\text{for some}S\in\mathcal{S}\}\), taking both maxima to be zero for the empty prefix. We always have \(\alpha(\mathcal{S})\le\beta(\mathcal{S})\): each selected _X_-vertex has a selected _Y_ -neighbour whose right endpoint is at least its index.

**Lemma 10.** _Let_ S _be a prefix, and put_ \(\alpha=\alpha(\mathcal{S})\) _and_ \(\beta=\beta(\mathcal{S})\)_. In every later component, each X-vertex x<sub>i</sub> satisfies_ \(i>\beta\)_, and each Y-vertex y satisfies_ \(\ell(y)>\alpha\).

