(c) Finally, if<tbc>

<tbc>Max-Flow(_p,u<sub>big</sub>)\<_Max-Flow(_p,f(u_)),<tbc>

<tbc>then (_S<sub>p,u<sub>big</sub></sub>,C<sub>p,u<sub>big</sub></sub>,S<sub>u<sub>big</sub>,p</sub>_) separates _u<sub>big</sub>_ and _u_, and with 3.2 and 3.1 providing an optimal minimum cut, concluding the claim.

## Running time

Here, we prove the upper bounds on the preprocessing time, by proving that with high probability, the algorithm terminates after \(\tilde{O}(\alpha(V))\) calls to Max-Flow and \(\tilde{O}(\alpha(V)n)\) time outside of these calls.

At a high level, our aim is to bound the size of each of the sets in the partition in an expansion operation by \(3|V'|/4\), which implies a bound of _O_(log_n_) on the height of the recursion tree. This bound is immediate for the sets {_f_<sup>-1</sup>(_i_)}_<sub>i</sub>_ since they are subsets of cuts _S<sub>u,p</sub>_ of nodes _u_ in _V<sub>small</sub>_ and, by definition, satisfy that \(|S'_{u,p}|\le n'/2\). Therefore, we only need to worry about \(V'_{big}\). However, any node _u_ that is initially in _V<sub>small</sub>_ will end up reassigned to one of the sets {_f_<sup>-1</sup>(_i_)}_<sub>i</sub>_ and not to \(V'_{big}\). Thus, it suffices to argue that \(|V_{small}|\ge|V'|/4\). To this end, we cite a lemma from \[AKT20a\] which shows that for a randomly chosen _p_, at least 1/4 of the nodes \(u\in V'\) satisfy that the side of _u_ is smaller than the side of _p_, and so they will end up in _V<sub>small</sub>_. We provide a more formal proof of this below, starting with a general lemma about tournaments.

**Lemma 3.4** (Lemma 2.4 in \[AKT20a\])**.** _Let Y_=(_V<sub>Y</sub>,E<sub>Y</sub>_) _be a directed graph on n nodes and m edges that contains a tournament on V<sub>Y</sub>. Then Y contains at least n/_2 _nodes with an out-degree at least n/_4.

The following is a corollary of Lemma 3.4 concerning cuts between every pair of nodes, and it is an adaptation of Corollary 2.5 in \[AKT20a\] to vertex-cuts.

**Corollary 3.5.** _Let F_=(_V<sub>F</sub>,E<sub>F</sub>_) _be a graph where each pair of nodes_ \(u,v\in V_F\) _is associated with a cut_ (_S<sub>u,v</sub>,C<sub>u,v</sub>,S<sub>v,u</sub>_) _where_ \(u\in S_{u,v},v\in S_{v,u}\) _(possibly more than one pair of nodes are associated with each cut), and let_ \(V'_F\subseteq V_F\)_. Then there exist_ \(|V'_F|/2\) _nodes_ \(p'\) _in_ \(V'_F\) _such that at least_ \(|V'_F|/4\) _of the other nodes_ \(w\in V'_F\backslash\{p'\}\) _satisfy_ \(|S_{p^\prime,w}\cap V'_F|\ge|S_{w,p^\prime}\cap V'_F|\).

_Proof._ Let \(H_F(V'_F)\) denote the _helper graph_ of _F_ on \(V'_F\), where there is a directed edge from \(u\in V'_F\) to \(v\in V'_F\) iff \(|S_{u,v}\cap V'_F|>|S_{v,u}\cap V'_F|\). By Lemma 3.4, since \(H_F(V'_F)\) contains a tournament on \(V'_F\), Corollary 3.5 holds.

Next, apply Corollary 3.5 on _G_, and let \(H=H_G(V')\) be the helper graph of _G_ on \(V'\) with the reassigned cuts. As a result, with probability at least 1/2, the pivot _p_ is one of the nodes with out-degree at least \(n'/4\). In that case, when the algorithm partitions \(V'\), it must be that \(\mathrm{max}_i|f^{-1}(i)|\le n'/4\), and \(|f^{-1}(\perp)|\le 3n'/4\), that is, the largest set created is of size at most \(3n'/4\). This is because, while the separated parts _S<sub>u,v</sub>_ and _S<sub>v,u</sub>_ for each _uv_-cut do not cover the entire node set as the case in \[AKT20a\], the condition \(|S_{p,v}\cap V'_F|\ge|S_{v,p}\cap V'_F|\) for adding an edge in the tournament still implies that \(|S_{f(v),p}\cap V'_F|\le n'/2\), meaning that _v_ remains in _V<sub>small</sub>_ after the reassignment process in our setting too.

After making _O(n_log_n_) successful pivot choices, the algorithm terminates with the total depth of the recursion tree being at most log<sub>4/3</sub>_n_. Note that in step 5, the algorithm verifies the choice of _p_ and only proceeds with a successful pivot choice. Therefore, it suffices to bound the running time of the algorithm given only successful pivot choices. The probability of having 4log_n_ consecutive failures in a single instance is bounded by (1/2)<sup>4log_n_</sup>=1_/n_<sup>4</sup>, and by applying the union bound over<tbc>

