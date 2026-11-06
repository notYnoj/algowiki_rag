<tbc>This is because, if this does not hold before the Bellman-Ford phase, then _u_<sub>_j_-1</sub> must be marked (by Invariant A.1)<sup>22</sup>, and _d(u<sub>j</sub>_) will be set to a value of at most _d(u_<sub>_j_-1</sub>)+_w(u_<sub>_j_-1</sub>_,u<sub>j</sub>_) on Line 16. From (11), we can conclude that after iteration _i_ of the Bellman-Ford phase,<tbc>

\(d(u_j)\le d(u_{j-1})+w(u_{j-1},u_j)=\mathrm{dist}(s,u_j).\) (12)

<tbc>Now consider when we finish iteration _i_ of the Dijkstra phase. Since _Q_ is empty and by Invariant A.1, all edges (_u<sub>j</sub>,u_<sub>_j_+1</sub>),(_u_<sub>_j_+1</sub>_,u_<sub>_j_+2</sub>)_,...,(u_<sub>_k_-1</sub>_,u<sub>k</sub>=v_) are inactive (recall that they are all in _E_\\_E<sup>neg</sup>(G_) by definition). Thus,

\(d(v)\le d(u_j)+w(u_j,u_{j+1})+w(u_{j+1},u_{j+2})+\dots+w(u_{k-1},v)=^{(12)}\mathrm{dist}(s,v)\)

It is easy to see that our algorithm always satisfies the invariant \(d(v)\ge\mathrm{dist}(s,v)\). Thus _d(v_)=dist(_s,v_) as claimed.

Invariant A.4 below is needed for proving Lemma A.5.

**Invariant A.4.** _The following always holds during the Dijkstra Phase: For any marked vertex v and any_ \(x\in Q\), \(d(v)\le d(x)\).

_Proof._ The invariant trivially holds when the Dijkstra phase begins (Line 4) because there is no marked vertex (the Bellman-Ford phase unmarks all vertices). The invariant can be affected when **(i)** a new vertex _v_ is marked (Line 6), **(ii)** a new vertex is added to _Q_ (Line 9), or **(iii)** _d(x_) decreases for \(x\in Q\) (Line 10).

For **(i)**, marking _v_ on Line 6 does not violate the invariant because, by definition, _v_ has the lowest _d(v_) among vertices in _Q_. For **(ii)** (Line 9), note that _d(x)\>d(v_) by the if-condition on Line 8 (since \(w(v,x)\ge 0\)). Moreover, since \(v\in Q\), we can conclude by induction that \(d(u)\le d(v)\) for every marked _u_; thus, \(d(u)\le d(v)<d(x)\) and so adding _x_ to _Q_ on Line 9 does not violate the invariant. Similarly, for **(iii)** (Line 10), the new value of _d(x_) is such that \(d(x)\ge d(v)\) (since \(w(v,x)\ge 0\)) and we can conclude by induction that \(d(u)\le d(v)\) for every marked _u_; so, decreasing _d(x_) on Line 10 does not violate the invariant.

**Lemma A.5.** _When a vertex x is added to Q on Line 9, it is not marked._

_Proof._ Suppose for contradiction that there is a vertex _x_ that is marked when it is added to _Q_ on Line 9. This leads to the following contradiction: **(i)** _d(v)\<d(x_) (due to the if-condition on Line 8; note that \(w(v,x)\ge 0\)). **(ii)** \(d(x)\le d(v)\) (by Invariant A.4, where _x_ is marked and \(v\in Q\)).

Now we conclude the runtime analysis. Observe that if there are _N_ vertices added to _Q_ during the entire execution of the algorithm, then the algorithm’s runtime is _O(N_log_n_): each vertex extracted from _Q_ contributes _O_(log_n_) time in the Dijkstra phase and _O_(1) time in the Bellman- Ford phase; here, we use the fact that every vertex has constant out-degree. It thus suffices to bound _N_, the number of vertices added to _Q_.

Lemma A.5 implies that every vertex is added to _Q_ at most once in each iteration of the Dijkstra phase. It is clear from the pseudocode that every vertex is also added to _Q_ at most once in each iteration of the Bellman-Ford phase. Lemma A.3 implies that a vertex _v_ can be added to _Q_ only in iterations \(0,1,\dots,\eta(v)\) of Dijkstra and Bellman-Ford phases; thus, a vertex _v_ can be added to _Q_ at most \(2\eta(v)+2\) times, and the number of vertices added to _Q_ overall is \(N\le 2\sum_{v\in V}\eta(v)+2n\). This implies the claimed runtime of \(O(\mathrm{log}(n)\cdot(\sum_{v\in V}\eta(v)+n))\).

<sup>22</sup>Note that _Q_ is empty after the Dijkstra phase; so, for every active (_x,y_), vertex _x_ must be marked after the Dijkstra phase.

