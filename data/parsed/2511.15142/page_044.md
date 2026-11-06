edges (_x_<sub>_j_-1</sub>_,y<sub>j</sub>_) corresponding to M<sub>2</sub> for \(1\le j\le k\). If \(Y\Delta P\notin\mathcal{I}_2\), then there is an alternate matching \(M'\) from vertices in _P_\\_Y_ to _Y_\\_P_. Consider the multiset union of edges \(M\cup M'\cup 2N\). Similar to the argument in parts (1) and (2a) above, we find a cycle (say) _C_<sub>1</sub> containing the edge (_y<sub>t</sub>,x_<sub>0</sub>) such that \(\ell(C_1)\le\ell(C)\) and |_C_<sub>1</sub>|_\<|C_|. Deleting the edge (_y<sub>t</sub>,x_<sub>0</sub>) gives a path _P_<sub>1</sub> that contradicts the minimality of _P_.

Lemma E.9 allows us to compare lengths of minimal paths using only comparisons of matroid intersections:

\(\ell(P_1)-\ell(P_2)=w(Y\triangle P_1)-w(Y\triangle P_2),\)

when _P_<sub>1</sub> and _P_<sub>2</sub> are minimal paths or cycles. In order to optimize over minimal paths, we modify the Bellman-Ford algorithm in the natural way.

### Modified Bellman-Ford Algorithm.

Let \(p_y^{(t)}\) denote the minimal path in P(_y,t_). We compute it recursively:

• **Initialization:** For each \(y\in Y\) ,<tbc>

<tbc>\(p_y^{(1)}=min_{x\in X_1}(x\rightarrow y).\)<tbc>

• **Update:** For \(t\ge 1\),<tbc>

<tbc>\(p_y^{(t+1)}=min\left\{p_y^{(t)},p_z^{(t)}\rightarrow x\rightarrow y\right\},\)<tbc>

<tbc>where \((z,x)\in Y\times(E\backslash Y)\) satisfies:<tbc>

1. (_z,x_) and (_x,y_) are arcs in _H_, and<tbc>

2. \(Y\triangle p_z^{(t)}+x-y\in\mathcal{I}_1\cap\mathcal{I}_2\).<tbc>

• **Shortest Augmenting path:** After computing paths \(p_y^{(t)}\) for all \(y\in Y\) and _t_=|_Y_|, we extract a minimal shortest path _P_ from _X_<sub>1</sub> to _X_<sub>2</sub> such that \(Y\triangle P\in\mathcal{I}_1\cap\mathcal{I}_2\), and update \(Y\leftarrow Y\triangle P\).

_Proof of Theorem E.4._ Let _Y<sub>t</sub>_ be the extreme common independent set of size exactly _t_ starting with \(Y_0=\emptyset\). Use the modified Bellman-Ford Algorithm to find the shortest augmenting path _P<sub>t</sub>_ in the exchange graph _H_(M<sub>1</sub>,M<sub>2</sub>_,Y<sub>t</sub>_)). Using Lemma E.8 part (i), the exchange graph has no negative cycles. The shortest path computation takes _O(n_<sup>3</sup>) comparison queries and time (see section E.4). After every update, we know that \(Y_{t+1}:=Y_t\Delta P_t\) is an extreme set using Lemma E.8 part (ii). We continue for _n_ steps as long as there is a directed path from _X_<sub>1</sub> to _X_<sub>2</sub> in the exchange graph. Using Lemma E.7, we know that the maximum cardinality intersection is reached when an augmenting path is not present anymore. Finally, we can compare the weights of all the extreme sets obtained to output the minimum weight common intersection _O(n_<sup>4</sup>) comparisons and _O(n_<sup>4</sup>) time.

## E.4 Shortest paths

Finally, when the combinatorial objects of interest are _s-t_ walks, we show that the Bellman-Ford shortest path algorithm can be used to find the shortest _s-t_ walk (which will be a path) using _O(n_<sup>3</sup>) many _s-t_ walk comparisons.

**Theorem E.10** (_s-t_ walks)**.** _There is an algorithm that finds the minimum-length s-t path in a graph G (or a negative cycle, if one exists) using O(n_<sup>3</sup>) _s-t walk comparisons and O(n_<sup>3</sup>) _time._

