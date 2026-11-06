**Lemma 14.** _Let_ \(X\subseteq V(G)\) _be any shy set of vertices of G. Assume that_ (_u,v_) _is a conflict pair for X. Let X<sub>v</sub>=X_\\{_v}. The neighborhood of the connected component C<sub>v</sub> containing v in G_\\_X<sub>v</sub> is: N(C<sub>v</sub>_)=_R<sub>G</sub>(v,X)._

_Proof._ Set _N(C<sub>v</sub>_) can be seen as the subset of _X<sub>v</sub>_ which contains all vertices \(w\in X\), \(w\neq v\), such that there exists a path from _w_ to _v_ whose internal vertices do not belong to _X_. This corresponds to the definition of reachability (Definition 5).

We define the notion of _brightening_ of a shy set. The result of our algorithm conflict- greedy will be some brightening of the input shy set.

**Definition 17** (Brightening of a shy set)**.** _Let G be a graph and_ \(X\subseteq V(G)\) _be a shy set of G. A subset_ \(X'\subseteq X\) _is a_ brightening _of X if one of the following statements hold:_

• \(X'\) _is a PMC,_<tbc>

• \(X'\) _admits only_ native full components, i.e. _each connected component C of_ \(G\backslash X'\) _which is full for_ \(X'\) _does not contain any vertex removed from X: formally,_ \(C\cap(X\backslash X')=\emptyset\).

We introduce our algorithm conflict-greedy. Its principle is very simple: consider the input shy set _X_. If _X_ does not admit conflicts (Definition 7), then _X_ is a PMC and we return it. Otherwise, we select an arbitrary vertex \(u\in X\) - that we call _protected vertex_ - which is in conflict with another one, and we remove from _X_ all the vertices which are in conflict with the selected _u_. If the obtained set is still shy, we repeat the process, otherwise we return the obtained set. The pseudocode of conflict-greedy is given in Algorithm 1.

conflict-greedy starts in fact by checking whether the given set is a PMC (line 4 of Algorithm 1). If it is, it does not enter in the while loop and returns _X_ which is thus a brightening of itself, by Definition 17. Otherwise, it enters the while loop and the removal process starts (lines 5-7). It consists in removing from _U_ all vertices in conflict with some arbitrarily fixed protected vertex \(u\in U\). When the removal process is achieved, the condition of the while loop is checked: we verify whether the obtained set _U_ is still shy. If no, we return<tbc>

S
a
b
a'
b'
X = S U {a, b}

S
a
b
a'
b'
X = S U {a, b}

(a) An example of shy set _X_ (in red) which is not a PMC and such that any of its proper subset has a full component.

(b) Almost the same graph (an edge was removed between \(a'\) and _S_): here _X_ is still shy but is a PMC superset with \(\Omega=S\cup\{a\}\).

Figure 5: Two graphs with shy sets _X_ but different decision answer to PMC Superset.

