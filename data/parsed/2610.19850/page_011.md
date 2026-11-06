• _Vertices u and v are_ visible despite _U if_ \(v\in R_G(u,U)\) _- equivalently_ \(u\in R_G(v,U)\) _as G is undirected. Another formulation we will use for this statement is either (i) u sees v despite U or (ii) u and v_ see each other _despite U._<tbc>

• _Conversely, vertices u and v are_ in conflict _for U if_ \(v\notin R_G(u,U)\)_. Another possible formulation used is that_ (_u,v_) _is a_ conflict pair _for U._<tbc>

• _Vertex u is_ enlightened _for U if it is not involved in any conflict pair: R<sub>G</sub>(u,U_)=_U._<tbc>

• _Set U satisfies the_ reachability property _if, for any pair_ \(x,y\in U\)_, x and y are visible despite U._

Naturally, by considering a subset \(U'\subseteq U\) where _U_ has the reachability property, we preserve the property as the graph \(G\backslash U'\) is less restricted than _G_\\_U_ in terms of connectivity. More concretely, two reachable vertices \(x,y\in U'\) in _G_\\_U_ are still reachable in \(G\backslash U'\). Trivially, the empty set and singletons always have the reachability property.

**Observation 2.** _Given a set U that satisfies the reachability property, any subset of U also satisfies it._

## 2.2.2 Minimal separators

As we will see it further, PMCs of a graph are closely related to its minimal separators. We begin with a clear presentation on the different shades of separators.

**Definition 8** (Minimal separators and set \(\Delta_G\))**.** _Consider a graph G, two vertices_ \(a,b\in V(G)\) _and some set_ \(S\subseteq V(G)\backslash\{a,b\}\)_. We say that:_

• _S is an_ (_a,b_)-separator _if vertices a and b belong to two different connected components in G_\\_S._<tbc>

• _S is a_ minimal (_a,b)-separator if it is an_ (_a,b)-separator and no proper subset of S is an_ (_a,b)-separator._<tbc>

• _S is a_ minimal separator _of G if we can identify two vertices_ \(a,b\in V(G)\) _such that S is a minimal_ (_a,b)-separator._<tbc>

y
X
C G(a,U)
a
u
v

y
X
u
v

(a) Graph _G_, set _U_={_u,v,x,y_}. We have \(a\in R_G^+(v,U)\) and \(x\in R_G(v,U)\unknown R_G^+(v,U)\) via _C<sub>G</sub>(a,U_). Moreover, \(u\in R_G(v,U)\) via direct edge and \(y\in R_G(v,U)\) via the connected component on top of the figure.

(b) Graph torso(_G,U_). Vertices _u_ and _x_ are connected neither by a direct edge nor via a path whose all internal vertices belong to <o>_U_</o>.

Figure 1: Illustration of the notions of torso and reachability.

