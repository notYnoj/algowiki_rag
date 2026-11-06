algorithm requires sorting the elements in each connected component which requires _O(c<sub>i</sub>_log_c<sub>i</sub>_) comparisons in each component with _c<sub>i</sub>_ elements. Each such comparison takes _O(n_) time to find the path and write down the bases to input to the comparison oracle. Adding everything, we get the _O(n_<sup>2</sup>log_n_) time bound as claimed.

## E.2 Matroid Intersection

We now turn to finding _common independent sets_ \(S\in\mathcal{I}_1\cap\mathcal{I}_2\) between two matroids M<sub>1</sub>=(_U,_I<sub>1</sub>) and M<sub>2</sub>=(_U,_I<sub>2</sub>). Our main result in this case is the following:

**Theorem E.4** (Matroid Intersection)**.** _Let_ M<sub>1</sub>=(_U,_I<sub>1</sub>) _and_ M<sub>2</sub>=(_U,_I<sub>2</sub>) _be two matroids defined on a ground set U containing n elements. Then, there is an algorithm that outputs the minimum- weight set that is in both_ I<sub>1</sub>,I<sub>2</sub> _using O(n_<sup>4</sup>) _comparison queries in O(n_<sup>4</sup>) _time._

To prove this, we show that Edmond’s classical weighted matroid intersection algorithm, as presented in \[Sch03, Section 41.3\], can be implemented using only comparisons of common independent sets. As in the previous section, we first consider the simpler bipartite matching case, where the shortest augmenting paths algorithm constructs extremal matchings via shortest paths in an exchange graph. Our key observation is that these shortest-path steps--e.g., via Bellman-Ford--can themselves be implemented using only comparisons between matchings.

Formally, let _G_=(_V,E_) be a bipartite graph with color classes \(V=L\cup R\). Given an _extremal matching M_ of size _k_ (i.e., a min-cost matching with _k_ edges), we describe a primitive to obtain an extremal matching \(M'\) of size _k_+1.

The _M-exchange graph D_ orients matching edges from _R_ to _L_ and non-matching edges from _L_ to _R_ in _G_. Let \(L'\) and \(R'\) be the unmatched vertices in _L_ and _R_. An _M-augmenting path_ is a directed path in _D_ from a vertex in \(L'\) to one in \(R'\). Define the edge length function \(\ell:E\rightarrow\mathbb{R}\) as: \(\ell(e):=-w(e)\) if \(e\in M\), and _w(e_) otherwise. The following result is standard (see, e.g., Theorem 3.5, Proposition 1 in Section 3.5 of \[Sch90\]).

**Lemma E.5.** _Let M be an extremal matching. Then:_

1. _The exchange graph D has no negative-length cycles._<tbc>

_2._ _If P is a minimum-length M-augmenting path, then_ \(M':=M\triangle P\) _is also extremal._

By iteratively applying Lemma E.5, we construct extremal matchings of increasing size, from size 0 to _n/_2, and return the one with minimum total weight. Moreover, to implement this using only comparisons between matchings, we describe a variant of the Bellman-Ford algorithm. For each \(u\in L\), let \(p_u^{(k)}\) be the shortest _M_-alternating path from \(L'\) to _u_ using at most _k_ matching edges. For matched \(u\in L\), let \(u'\in R\) be its partner. We initialize:

\(p_u^{(1)}=\left\{\begin{array}{ c c }
\emptyset & \text{if}u\in L', \\
s\rightarrow u'\rightarrow u & \text{for}s=argmin_{s\in L^\prime}\ell(s\rightarrow u'\rightarrow u).
\end{array}\right.\)

Moreover, we recursively define \(p_u^{(k+1)}=min_{v\in L}\left(p_u^{(k)},p_v^{(k)}\rightarrow u'\rightarrow u\right)\), where the min operator returns the path with minimum total length \(\ell(p)\), ties broken arbitrarily. Each such path _P_ yields a matching \(M\triangle P\), and satisfies \(\ell(P)=w(M\triangle P)-w(M)\), so comparing path lengths reduces to comparing weights of the resulting matchings.

To reach a free vertex \(t\in R'\), compute: \(p_t=min_{v\in L}\left(p_v^{(n)}\rightarrow t\right)\), which again defines an alternating path. Hence, the full algorithm can be implemented using only comparisons between matchings.

