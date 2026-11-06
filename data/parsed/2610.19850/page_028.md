Thanks to Theorem 6 and Theorem 7, we obtain a complete characterization of PMC supersets.

**Corollary 2.** _Let_ \(X\subseteq V(G)\) _be a shy set. Set X is a PMC superset if and only if there exists a triplet_ (_a,b,S_) _satisfying the following properties:_

• _a and b are two distinct vertices and in particular_ \(a\in X\),<tbc>

• _S is the X-close_ (_a,b)-separator,_<tbc>

• _S is X-shy with regards to C<sub>G</sub>(a,S)._

_Moreover, given such triplet_ (_a,b,S), one can compute a PMC_ \(\Omega\subseteq X\) _thanks to_ conflict- greedy _in O(n_<sup>3</sup>).

### 3.4 A polynomial-time algorithm for PMC superset

The characterization of PMC supersets established in Corollary 2 provides us with a way to check whether some shy set _X_ is a PMC superset. Indeed, it suffices to determine the existence (or not) of a triplet (_a,b,S_) satisfying the properties listed in Corollary 2. It becomes rapidly clear that answering the latter question can be achieved in time polynomial in _n_. One can simply enumerate all possible pairs \(a,b\in V(G)\) and then compute the unique _X_-close (_a,b_)-separator _S_. The last check consists in looking at the shyness of _S_, which is a simple connectivity property. All in all, we obtain a polynomial-time complexity for PMC Superset.

**Theorem 2.** _There is an algorithm deciding_ PMC Superset _in time O(n_<sup>3</sup>_m). Furthermore, for a yes-instance, it produces a solution PMC._

_Proof._ We begin with the research of a triplet (_a,b,S_). First, we enumerate all pairs of vertices \((a,b)\in X\times V(G)\) and check whether \((a,b)\notin E(G)\) and _X_\\{_a_} is an (_a,b_)-separator. If these conditions are not satisfied, we move on to another pair. Otherwise, we compute the _X_-close (_a,b_)-separator _S_. By Definition 12, constructing the _X_-close (_a,b_)-separator consists first in determining set _A=C<sub>G</sub>(a,X_\\{_a_}): it can be achieved with a BFS starting at _a_ in graph _G_\\(_X_\\{_a_}). Second, we compute _S_=S_<sub>G</sub>(A,b_) in linear time (Lemma 4). When _S_ is known, we check whether it is _X_-shy with regard to _C=C<sub>G</sub>(a,S_). Concretely, we compute graph _G_\[_C_\\_X_\] with its connected components: for each of them, we look at their neighborhood and verify whether _S_ is included into it. This takes _O(nm_). In summary, checking the presence of a triplet (_a,b,S_) witnessing the presence of PMC inside _X_ can be achieved by enumerating all pairs (_a,b_) and then verifying whether the _X_-close (_a,b_)-separator exists and is _X_-shy. The running time is _O(n_<sup>3</sup>_m_).

If no triplet satisfies the conditions listed in Corollary 2, then we conclude that _X_ is not a PMC superset. But if one works, then we can compute a PMC \(\Omega\subseteq X\) in _O(n_<sup>3</sup>) (Corollary 2) and we answer that _X_ is indeed a PMC superset. The overall running time to decide PMC superset is thus _O(n_<sup>3</sup>_m_).

## 4 Output-linear algorithm for the enumeration of PMCs

This section is dedicated to the description and the analysis of our algorithm PMC-Traversal which enumerates all PMCs of a graph in output-linear time. The previous section will be used as a toolkit to attain this objective.

