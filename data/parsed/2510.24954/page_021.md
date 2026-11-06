## 4.2 Exact Shortest Paths via \((1+\epsilon)\)-Approximate Distance Shortcuts

In this section, we observe that a near-optimal parallel algorithm for constructing a distance shortcut with length slack (1+_o_(1/log_n_)) would imply a near-optimal parallel algorithm for _exact_ single-source shortest paths with \(\tilde{O}(m)\) work and polylog(_n_) depth.

In the SSSP problem, given a graph _G_ and a vertex _s_, we need to output the exact distance _d(u_) from _s_ to every other vertex _u_ in _G_. For \(\alpha\)-approximate SSSP, we are given a graph _G_ and a vertex _s_, output an approximate distance \(\tilde{d}(u)\) from _s_ to every other vertex _u_ in _G_, such that \(d(u)\le\tilde{d}(u)\le\alpha d(u)\).

The reduction from parallel exact SSSP to distance shortcut construction follows from combining tools from \[KS97\] and \[RHM<sup>+</sup>23b\].

**Theorem 4.4.** _For any_ \(n,m,m',h\)_, suppose there is an algorithm_ A _which takes an O(m)-edge O(n)- vertex directed graph and computes a distance shortcut of hopbound O(h), length slack_ (1+_o_(1/log_n_)) _and size_ \(O(m')\)_. Then, there is an algorithm computing exact SSSP of an m-edges n-vertex directed graph with_ \(\tilde{O}\left(1\right)\) _calls to_ A_, with additional_ \(\tilde{O}\left(m+m'\right)\) _work and_ \(\tilde{O}\left(h\right)\) _depth._

In undirected graphs, there exist distance shortcuts of hopbound _n_<sup>_o_(1)</sup>, length slack (1+1/log<sup>2</sup>_n_) and size _n_<sup>1+_o_(1)</sup> (e.g. \[Coh00, HP19\]). Moreover, \[EN19\] showed how to construct them in _m_<sup>1+_o_(1)</sup> work and _n_<sup>_o_(1)</sup> depth.

If this can be generalized to directed graphs even when the shortcut size is _m_<sup>1+_o_(1)</sup>, then Theorem 4.4 would imply an exact SSSP algorithm with _m_<sup>1+_o_(1)</sup> work and _n_<sup>_o_(1)</sup> depth.

**Corollary 4.5.** _Suppose there is an algorithm that, given O(m)-edge O(n)-vertex directed graph, computes a distance shortcut of hopbound n_<sup>_o_(1)</sup>_, length slack_ (1+_o_(1/log_n_))_, and size m_<sup>1+_o_(1)</sup>_. Then, there is an algorithm for computing exact SSSP in an m-edge n-vertex directed graphs in m_<sup>1+_o_(1)</sup> _work and n_<sup>_o_(1)</sup> _depth._

Indeed, in directed graphs, the state-of-the-art is still far from this goal, because the problem is even harder than reachability shortcut. There exist distance shortcuts of hopbound \(\tilde{O}(n^{1/3})\), length slack \((1+\epsilon)\) and size \(\tilde{O}(n/\epsilon^2)\) \[BW23\], but they require large polynomial time to construct. \[CFR20\] showed a parallel algorithm with \(\tilde{O}(m/\epsilon^2)\) work and _n_<sup>0.5+_o_(1)</sup> depth to construct a distance shortcut of hopbound _n_<sup>1/2+_o_(1)</sup>, length slack \((1+\epsilon)\) and size \(\tilde{O}(n/\epsilon^2)\).

Note that, since Theorem 4.4 is a _work-efficient_ reduction, any improvement to the _n_<sup>1/2+_o_(1)</sup> hopbound of \[CFR20\] would immediately improve the start-of-the-art for parallel exact SSSP problem which currently requires \(\tilde{O}(m)\) work and _n_<sup>1/2+_o_(1)</sup> depth \[CFR20, RHM<sup>+</sup>23b\].

**Proof of Theorem 4.4**

_Proof._ We first present an algorithm for computing (1+_o_(1/log_n_))-approximate SSSP in an _O(m_)-edge, _O(n_)-vertex directed graph with 1 call to A and additional \(\widetilde{O}\left(m+m'\right)\) time and \(\widetilde{O}\left(h\right)\) depth. We then show how to solve exact SSSP of an _m_-edge _n_-vertex graph using \(\widetilde{O}\left(1\right)\) calls to the approximation algorithm with additional \(\widetilde{O}\left(m\right)\) work and \(\widetilde{O}\left(h\right)\) depth. Combining the two reductions finishes the proof.

### Approximate SSSP.

Given a directed _G_ with _O(m_) edges and _O(n_) vertices, we first compute a distance shortcut of size \(O(m')\), denoted by \(G'=(V\cup V',E\cup E')\). We will apply \[KS97, Lemma 3.2\], to \(G'\), which we state as follows.

**Lemma 4.6** (\[KS97, Lemma 3.2\])**.** _Given a directed graph G, a vertex u and parameters_ \(h,\epsilon\)_, there is an algorithm computing a h_-limited \((1+\epsilon)\)-approximate shortest path \(\tilde{d}_h\) _defined as_<tbc>

