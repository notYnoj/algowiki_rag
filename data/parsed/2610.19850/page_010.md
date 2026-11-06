**Definition 3** (Shy set)**.** _Consider a graph G and a vertex set_ \(U\subseteq V(G)\)_. We say that U is a_ shy set _if there is no connected component of G_\\_U which is a full component for U. Formally, for any connected component C of G_\\_U,_ \(N_G(C)\neq U\).

Observe that if some set _U_ is shy, then naturally any of its superset is also shy, otherwise a full component for the superset would imply necessarily a full component for _U_ in _G_\\_U_. Trivially, _V(G_) is always a shy set.

**Observation 1.** _Given a shy set_ \(U\subseteq V(G)\) _of G, any of its superset_ \(W\supseteq U\) _is also shy._

Another common notion widely used in the context of treewidth is the _torso_.

**Definition 4** (Torso \[25, 27\])**.** _Consider a graph G and some set_ \(U\subseteq V(G)\)_. The graph torso(G,U_) _has vertex set U and its edge set is made up of all edges_ \((u,v)\in U\times U\) _satisfying either_ \((u,v)\in E(G)\) _or there is a_ (_u,v)-path of G whose internal vertices are not in U._

Torsos characterize, given a vertex set _U_, its connectivity outside _U_, _i.e._ either through direct edges between two vertices or through paths outside _U_. For tree decompositions, torsos are used to characterize the connectivity between vertices of the same bag. In this paper, the torso will be a tool manipulated to not only define PMCs but also to introduce their properties.

We extend the notion of neighborhood into a larger (natural) one that we call _reachability_. Again, if we consider some vertex set \(U\subseteq V(G)\), reachability defines, given some vertex \(u\in U\), the set of vertices which can be reached from _u_ using only intermediary vertices outside _U_.

**Definition 5** (Reachability)**.** _Let U be a set of vertices_ \(U\subseteq V(G)\) _and a vertex_ \(u\in U\)_. We define as R<sub>G</sub>(u,U_) _the set of vertices of U which can be reached from u either directly (with an edge) or via intermediary vertices which are outside U._

_Two equivalent and more formal definitions follow._ \(v\in R_G(u,U)\) _if and only if:_

• _either_ \((u,v)\in E(G)\) _or there is a path in G starting from u and arriving at v such that all its internal vertices belong to <o>U</o>=V(G_)\\_U._<tbc>

• \((u,v)\in E(\mathtt{torso}(G,U))\).

Note that in this definition, set _R<sub>G</sub>(u,U_) is a subset of _U_ and can be seen as the neighborhood of _u_ in torso(_G,U_). Nevertheless, we will sometimes need a broader notion of reachability which contains the vertices outside _U_ also.

**Definition 6** (Global reachability)**.** _Let U be a set of vertices_ \(U\subseteq V(G)\) _and some vertex_ \(a\in V(G)\)_. We fix_ \(R_G^+(a,U)\) _the set of vertices of G which can be reached from a either via some direct edge or through some path whose internal vertices belong to <o>U</o>._

Note that there are two changes compared to Definition 5: first vertex _a_ is not necessarily in _U_, second set \(R_G^+(a,U)\) is not a subset of _U_: it also contains vertices of <o>_U_</o> reachable from _a_ via paths outside _U_. In the case \(u\in U\), then \(R_G(u,U)=R_G^+(u,U)\cap U\). All these aspects are illustrated in Figure 1. We can now introduce some vocabulary related to reachability.

**Definition 7** (Reachability property and conflicts)**.** _Let_ \(U\subseteq V(G)\) _be a set of vertices and_ \(u,v\in U\)_. We say that:_

