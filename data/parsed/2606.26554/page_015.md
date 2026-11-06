We remark that by appropriately setting parameters, we can obtain a low diameter small neighborhood decomposition where exactly one of the diameter and expansion factor is polylogarithmic and both are sub-polynomial. However, for our applications, it suffices to obtain a decomposition where both are sub- polynomial.

## 5 Undirected Multiple Source Shortest Paths

In this section, we present our algorithms for MSSP in undirected graphs.

### 5.1 Undirected Unweighted Multiple Source Shortest Paths

We begin with our algorithm for undirected, unweighted graphs.

**Theorem 5.1.** _Given a_ \((d,\phi)\)_-low diameter small neighborhood decomposition, there is a deterministic algorithm computing Multiple Source Shortest Paths (_MSSP_) on undirected, unweighted graphs in time_

\(O\left(n^2\phi d\mathrm{log}n+\mathsf{T}_\mathrm{BMM}\left(\frac{|S_\mathrm{in}|}{\phi\mathrm{log}n},n,n\right)\phi^2d(\mathrm{log}n)^2\right).\)

Combined with Theorem 1.4, we prove our main result.

**Theorem 1.2.** MSSP _on undirected unweighted graphs is equivalent to_ BMM(|_S_<sub>in</sub>|_,n,n), up to n_<sup>_o_(1)</sup> _factors, for randomized algorithms._<sup>3</sup> _In particular, there is a randomized algorithm computing_ MSSP _on undirected, unweighted graphs in n_<sup>_o_(1)</sup>T<sub>BMM</sub>(|_S_<sub>in</sub>|_,n,n_) _time._

_Proof of Theorem 1.2._ We obtain an (_n_<sup>_o_(1)</sup>_,n_<sup>_o_(1)</sup>)-low diameter small neighborhood decomposition in _n_<sup>2+_o_(1)</sup> time via Theorem 1.4. Applying Theorem 5.1, we compute MSSP in \(n^{o(1)}\cdot\mathsf{T}_\mathrm{BMM}\left(|S_\mathrm{in}|,n,n\right)\) time.

We prove Theorem 5.1 in the remainder of Section 5.1. Consider the following procedure.

