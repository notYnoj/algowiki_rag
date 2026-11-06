<tbc>vertices \(U\subseteq V\) , the notation <o>_U_</o> refers to the complementary of _U_ in _V_ : <o>_U_</o>=_V_\\_U_. We say two vertices _u_ and _v_ are adjacent in _G_ if \((u,v)\in E\). For any vertex \(u\in V\) , we denote respectively by \(N(u)=\{v:(u,v)\in E\}\) the _open neighborhood_<sup>4</sup> of _u_ and \(N[u]=N(u)\cup\{u\}\) its _close neighborhood_. These notions are naturally generalized to sets: for any \(U\subseteq V\) , \(N(U)=\{v:(u,v)\in E,u\in U,v\notin U\}\) and \(N[U]=U\cup N(U)\).

A _path P_ from _a_ to _b_ of _G_ is a sequence of vertices (_v_<sub>0</sub>_,v_<sub>1</sub>_,v_<sub>2</sub>_,...,v_<sub>_k_-1</sub>_,v<sub>k</sub>_) such that _a=v_<sub>0</sub>_,b=v<sub>k</sub>_, and \((v_i,v_{i+1})\in E\) for any \(0\le i<k\). Concisely, we say that _P_ is an (_a,b_)-path. A _simple path_ is a path without any repetition of vertices. From now on, the term _path_ will automatically refer to the notion of simple path. A graph _G_ is _connected_ if for any pair of vertices \(a,b\in V\) , \(a\neq b\), there is an (_a,b_)-path in _G_.

A _subgraph_ \(G'\) of _G_ is a graph \(G'=(V',E')\) made up of a subset of vertices/edges of _G_, formally \(V'\subseteq V\) and \(E'\subseteq E\cap(V'\times V')\). For any \(V'\subseteq V\) , we denote \(G[V']=(V',E\cap(V'\times V'))\) the _induced subgraph_ of \(V'\). Its edge set will be written briefly as \(E[V']=E\cap(V'\times V')\). Given a vertex set \(U\subseteq V\) , let _G_\\_U_ denote the graph _G_ deprived of vertices in _U_, formally _G_\\_U=G_\[<o>_U_</o>\]. More generally, given two sets _A_ and _B_ such that \(A\subseteq B\), then _B_\\_A_ denote the set _B_ deprived of elements of _A_.

Finally, we distinguish between the notion of _subset_ which includes equality (symbol \(\subseteq\)) and _proper subset_ which refers necessarily to a smaller set (symbol \(\unknown\)).

## 2.2 Connectivity and separators

### 2.2.1 Connectivity

We introduce now standard notations of connectivity, beginning with connected components.

**Definition 1** (Connected components)**.** _Consider a graph G. Let U be a set of vertices_ \(U\unknown V(G)\) _and let_ \(a\notin U\)_. We denote respectively by:_

• _C<sub>G</sub>(a,U_) _the_ connected component _of G_\\_U which contains a,_<tbc>

• _C<sub>G</sub>_\[_a,U_\] _the corresponding_ close connected component:

\(C_G[a,U]=C_G(a,U)\cup(U\cap N_G(C_G(a,U))).\)

_When G is clear from the context, we will sometimes remove it from subscript and use simply C(a,U_) _and C_\[_a,U_\].

We pursue with the concept of _full component_, which is a common notion related to both minimal separators and PMCs. A full component is simply a connected component which admits the whole removed set in its neighborhood.

**Definition 2** (Full components \[6\])**.** _Consider a graph G and a vertex set_ \(U\subseteq V(G)\)_. We say a connected component C of G_\\_U is a_ full component _for U if the neighborhood of the component in G is exactly U, formally N(C_)=_U._

Said differently, if some connected component _C<sub>G</sub>(a,U_) is a full component for _U_, then \(C_G[a,U]=C_G(a,U)\cup U\). We will see in the remainder that a minimal separator _S_ admits full components, but this is not the case for a PMC.

<sup>4</sup>We will use notation _N<sub>G</sub>(u_) when _G_ is not absolutely clear from the context.

