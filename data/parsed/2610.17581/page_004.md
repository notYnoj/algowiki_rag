Taking this lower bound on rank-_n/_2 hypergraphs with \(\varepsilon=\Theta(1/n)\), we prove unconditionally that D_k_SH does not admit fully polynomial-time approximation schemes for D_k_SH in the query model. Finally, we resolve a conjecture of Chakrabarty and Liao \[11\] regarding the relative power of cut and add queries, as well as the is-edge<sup>?</sup>(_S_) query, which returns if _S_ is a hyperedge in _H_.

_While add queries can simulate cut queries, the reverse is impossible; we suspect an exponential lower bound for such a simulation even allowing is-edge_<sup>?</sup> _queries._

We answer this in the affirmative in Section 6, proving that exponentially-many cut and is-edge<sup>?</sup> queries are required to simulate an add oracle within any multiplicative approximation factor.

## 2 Preliminaries

### 2.1 Definitions

Let _H_=(_V,E_) be a (hyper)graph and denote by \(w(e)\in\mathbb{R}_{\ge 0}\) the weight of edge _e_ (note that if _G_ is unweighted, the weights will be universally 1). For any \(F\subseteq E\), we let _w(F_) denote the sum of weights of all edges in _F_. For a subset of vertices \(S\subseteq V\) , the set of _induced edges_ is the collection of all edges contained entirely within _S_. If _E(S_) is the set of edges induced by _S_, we will denote by _H_\[_S_\]=(_S,E(S_)) the sub(hyper)graph induced by _S_. For a subset of vertices \(S\subseteq V\) , we then define the _density_ of _S_ to be \(\rho(S)=w(E(S))/|S|\). We say that _H_ has _maximum density_ \(\rho^*(H)=max_{S\subseteq V}\rho(S)\), and similarly define its _maximum k-density_ to be \(\rho_{=k}^*(H)=max_{S\subseteq V,|S|=k}\rho(S)\). Thus, the Densest Sub(hyper)graph problem is to find a set _S_ which maximizes the density, and the Densest _k_-Sub(hyper)graph problem is to find a set _S_ maximizing the density over all sets of size _k_.

Given a set of vertices _S_, the boundary of _S_, denoted \(\partial(S)\), is the set of edges with non- empty intersection with _S_ and <o>_S_</o>=_V_\\_S_, or simply the set of edges _crossing S_. The _degree_ of a vertex _v_ is \(deg(v)=w(\partial(\{v\}))\), while the _induced degree_ of _v_ in _S_, denoted deg_<sub>S</sub>(v_), is the degree of _v_ in _H_\[_S_\] (or in \(H[S\cup\{v\}]\) when \(v\notin S\)). For graphs, we let _E(S,T_) denote the edges with endpoints in both _S_ and _T_. For a hypergraph _H_, we define its _volume_ to be the sum of the degrees of all vertices, denoted Vol(_H_). Recall that the _rank_ of _H_ is the maximum cardinality of a hyperedge and _H_ is _r-uniform_ if all hyperedges have size _r_.<sup>3</sup><tbc>

<sup>3</sup>Note that we will assume there are no singleton hyperedges as they cannot be detected by cut or edge queries.

\begin{tabular}{cccc}
 & \multicolumn{2}{c}{Unweighted} & \multicolumn{2}{c}{Weighted} \\
 & Randomized & Deterministic & Randomized & Deterministic \\
\multirow{3}{*}{DSG} & \(\left(\Omega(\frac{n}{logn}),O(\frac{n^2}{logn})\right)\) & \multicolumn{2}{c}{\(\left(\Omega(\frac{n}{logn}),O(n^2)\right)\)} \\
 & (Lemma B.1) & \multicolumn{2}{c}{(Lemma 3.5)} \\
 & \(\Theta(\frac{n^2}{logn})\) & \(\left(\Omega(\frac{n^2}{logn}),O(n^2)\right)\) & \(\Theta(n^2)\) \\
\multirow{2}{*}{D_k_S} & (Lemma 5.4) & (Lemma 5.4) & (Corollary 5.3) \\
\end{tabular}

1: Summary of our results on the exact cut query complexity of densest subgraph problems. The upper bounds hold because unweighted and weighted graphs can be learned deterministically in _O(n_<sup>2</sup>/log_n_) queries \[19\] and _O(n_<sup>2</sup>) queries (folklore, noted in \[35\]), respectively. (_f(n),g(n_)) denotes a lower bound of _f(n_) and an upper bound of _g(n_) applies to the setting.

