<tbc>also note that Hoàng, Kaminski, Sawada and Sritharan \[6\] gave a \(\widetilde{O}(nm^{k-1})\)- time algorithm for finding _P_<sub>2_k_</sub> in _general graphs_ (They do not give algorithms for finding induced cycles).

## 2 Preliminaries

We begin by defining standard notions of containment in graph theory.

**Definition 1 (Subgraph).** _Let H_=(_V<sub>H</sub>,E<sub>H</sub>_) _and G_=(_V<sub>G</sub>,E<sub>G</sub>_) _be graphs. We say that G is a_ subgraph _of H, denoted by_ \(G\subseteq H\)_, if_

\(V_G\subseteq V_H\text{\textit{and}}E_G\subseteq\{\{u,v\}\in E_H:u,v\in V_G\}.\)

**Definition 2 (Induced Subgraph).** _Let G_=(_V,E_) _be a graph and let_ \(T\subseteq V\)_. The induced subgraph of G on T, denoted G_\[_T_\]_, is the graph whose vertex set is T and whose edge set consists of all edges of G with both endpoints in T._

**Definition 3 (Minor).** _Let H and G be graphs. We say that G is a_ minor _of H (denoted_ \(G\unknown H\)_) if G can be obtained from H by a finite sequence of the operations like vertex deletions, edge deletions and edge contractions._

**Definition 4 (Edge Contraction).** _Let H_=(_V<sub>H</sub>,E<sub>H</sub>_) _be a graph and let_ \(e=\{u,v\}\in E_H\)_. The graph obtained by_ contracting _e, denoted by H/e, is defined as follows._

_Let_<tbc>

\(E'=\{\ell\in E_H:u\in\ell\text{\textit{or}}v\in\ell\}\)

<tbc>_be the set of edges incident to u or v, and let_<tbc>

\(E''=\big\{\{u',w\}:w\in(N_H(u)\cup N_H(v))\backslash\{u,v\}\big\}.\)

<tbc>_where_

\(H/e=(V_{H/e},E_{H/e})\)<br>
\(V_{H/e}=(V_H\backslash\{u,v\})\cup\{u'\}\)<br>
\(E_{H/e}=(E_H\backslash E')\cup E''\)

.

_Here,_ \(u'\) _is a new vertex representing the contraction of u and v._

We now define tree decompositions and path decompositions, which are useful for designing dynamic programming algorithms on graphs.

**Definition 5 (Tree Decomposition).** _A_ tree decomposition _of a graph G_=(_V,E_) _is a pair_ \((\mathcal{T},\{X_t\}_{t\in V(\mathcal{T})})\) _where_ T _is a tree and each node t is assigned a subset_ \(X_t\subseteq V\)_, called a bag, such that: (1)_ \(\bigcup_{t\in V(\mathcal{T})}X_t=V\)_, (2) for every edge_ \(\{u,v\}\in E\)_, there exists t with_ \(\{u,v\}\subseteq X_t\)_, and (3) for every vertex_ \(v\in V\)_, the set_ \(\{t|v\in X_t\}\) _induces a connected subtree of_ T _. The width of a tree decomposition is_ max_<sub>t</sub>|X<sub>t</sub>_|-1_. The treewidth of G, denoted_ tw(_G), is the minimum width over all tree decompositions of G._

