_Proof._ Given the previous result, we simply apply **HittingSet** or **rHittingSet** on the subsets \(N(v)\cup\{v\}\) for all \(v\in V_s\). Since \(|V_s|\le n\), note that our previous result is also correct for all collections F of at most _n_ subsets as we can augment F with _n_-|F| subsets and any hitting set of the augmented collection is also a hitting set for the original collection.

**Lemma 2.6.** _Let G be a graph on n vertices. Given degree thresholds s_<sub>1</sub>_\>s_<sub>2</sub>_\>...\>s_<sub>_k_-1</sub>_, there is a deterministic algorithm **Decompose** and a randomized algorithm **rDecompose** that outputs edge sets_ \(\{E_i\}_{i=1}^k\)_, edge set E_<sup>∗</sup>_, and vertex sets_ \(\{D_i\}_{i=1}^k\) _satisfying,_

1. \(E_i=\{(u,v)\in E\text{\textit{s.t.}}min(deg(u),deg(v))<s_{i-1}\}\) _is the set E_<sub>_s<sub>i</sub>_-1</sub>.<tbc>

2. _D<sub>i</sub> dominates_ \(V_{s_i}=\{v\in V\text{\textit{s.t.}}deg(v)\ge s_i\}\) _and_ \(|D_i|=\tilde{O}\left(\frac{n}{s_i}\right)\)_. For convenience, V<sub>s<sub>i</sub></sub> may also be denoted V<sub>i</sub>._<tbc>

3. \(D_1\subset D_2\subset\dots\subset D_k=V\) _and_ \(E_k\subset E_{k-1}\subset\dots\subset E_1=E\).<tbc>

_4._ \(E^*=\bigcup_{i=1}^kE_i^*\) _where each_ \(E_i^*\subset E\) _has for every_ \(v\in V_i\)_, at least one edge_ \((v,w)\in E_i^*\) _for_ \(w\in D_i\).

_Furthermore, **Decompose** runs in_ \(\tilde{O}(kn^2)\) _time and **rDecompose** runs in_ \(\tilde{O}(kn)\) _time. Note that **rDecompose** satisfies the above conditions with high probability._

_For a given vertex_ \(v\in V\)_, define the_ **level of** _v, denoted_ \(\ell(v)\)_, as the integer i such that_ \(s_i\le deg(v)<s_{i-1}\)_. For a given edge_ \(e\in E\)_, define the_ **level of** _e, denoted_ \(\ell(e)\)_, as the integer i such that_ \(e\in E_i\backslash E_{i+1}\).

We first discuss the deterministic algorithm **Decompose**.

_Proof._ By Lemma 2.5, we can compute each _D<sub>i</sub>_ with **dominate** in \(\tilde{O}(ns_i)=\tilde{O}(n^2)\) time, so that overall we can compute all _D<sub>i</sub>_ in \(\tilde{O}(kn^2)\) time. Furthermore, we can ensure \(D_1\subset D_2\subset\dots\subset D_k=V\) by augmenting the _D<sub>i</sub>_ as necessary. Of course, when constructing _D<sub>i</sub>_, we can easily construct \(E_i^*\) by choosing the appropriate edges when we add a vertex to _v_ to _D<sub>i</sub>_. Finally, we can construct _E<sub>i</sub>_ in _O(m_) time by examining each edge for the degrees of its endpoints.

Next, we discuss the randomized algorithm **rDecompose**.

_Proof._ Using the randomized construction **rDominate**, we can likewise choose \(p_i=\frac{clogn}{s_i}\) for large enough _c_ to ensure correctness by the union bound.

**Lemma 6.1.** _Let G be a weighted, undirected graph on n vertices. For a given edge e incident to vertex v, let_ rank_<sub>v</sub>(e_) _be the order of e among all edges incident to v when ranked in increasing order of weight. For example, if e is the lightest edge incident to v,_ rank_<sub>v</sub>(e_)=1_. For a neighbor_ \(w\in N(v)\)_, we also denote_ rank_<sub>v</sub>(w_)=rank_<sub>v</sub>(v,w_) _to be the rank of the edge_ (_v,w)._

_Given thresholds s_<sub>1</sub>_\>s_<sub>2</sub>_\>...\>s_<sub>_k_-1</sub>_, there is an algorithm **WeightedDecompose** that outputs edge sets_ \(\{E_i\}_{i=1}^k\)_, edge set E_<sup>∗</sup>_, and vertex sets_ \(\{D_i\}_{i=1}^k\) _satisfying,_

1. \(E_i=\{(u,v)\in E\text{\textit{s.t.}}min(rank_u(u,v),rank_v(u,v))<s_{i-1}\}\).<tbc>

2. _D<sub>i</sub> dominates_ \(V_{s_i}=\{v\in V\text{\textit{s.t.}}deg(v)\ge s_i\}\) _and_ \(|D_i|=\tilde{O}\left(\frac{n}{s_i}\right)\)<tbc>

_3._ \(E^*=\bigcup_{i=1}^kE_i^*\) _where each_ \(E_i^*\subset E\) _has for every_ \(v\in V_{s_i}\) _at least one edge_ \((v,w)\in E_i^*\) _where_ \(w\in D_i\) _and_ rank_<sub>v</sub>(v,w)\<s<sub>i</sub>._

_Furthermore, **WeightedDecompose** runs in_ \(\tilde{O}(kn^2)\)_-time._

_We define the level of a vertex and edge analogously as in the unweighted case. For a given vertex_ \(v\in V\)_, define the_ **level of** _v, denoted_ \(\ell(v)\)_, as the integer i such that_ \(s_i\le deg(v)<s_{i-1}\)_. For a given edge_ \(e\in E\)_, define the_ **level of** _e, denoted_ \(\ell(e)\)_, as the integer i such that_ \(e\in E_i\backslash E_{i+1}\).

