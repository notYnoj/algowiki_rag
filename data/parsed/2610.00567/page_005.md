# Faster Algorithms for Induced Patterns

5

**Definition 6 (Path Decomposition).** _A path decomposition is a tree decomposition in which the underlying tree_ T _is a path. The pathwidth of G, denoted_ pw(_G), is the minimum width over all path decompositions of G._

Finally, we define arithmetic circuits.

**Definition 7 (Arithmetic Circuit).** _An arithmetic circuit over a ring R is a directed acyclic graph whose nodes are of three types: (1) input nodes labeled by variables or constants from R, (2) addition gates labeled_ +_, (3) multiplication gates labeled_ \(\times\).

_Each gate computes a polynomial over R in the natural way. The output gate computes the polynomial defined by the circuit._

_The_ size of a circuit _is the number of gates, and the_ depth _is the length of the longest directed path from an input node to the output gate._

**Definition 8 (Induced Subgraph Polynomial).** _For a k-vertex pattern G and a host H, we define the_ induced subgraph polynomial _as_<tbc>

\(Ind_{G,H}\big((y_v)_{v\in V(H)}\big)=\sum_{S\subseteq V(H)|S|=kH[S]\cong G}\prod_{v\in S}y_v.\)

<tbc>**Definition 9 (Subgraph Polynomial).** _For a k-vertex pattern G and a host H, we define the_ subgraph polynomial _as_

\(Sub_{G,H}\big((y_v)_{v\in V(H)}\big)=\sum_{S\subseteq V(H)|S|=kH[S]\supseteq G}\alpha_S\prod_{v\in S}y_v,\)

_where_ \(H[S]\supseteq G\) _means that H_\[_S_\] _contains a subgraph isomorphic to G, and_ \(\alpha_S\) _denotes the number of such subgraphs in H_\[_S_\].

**Definition 10 (Homomorphism Polynomial).** _For a k-vertex pattern G and a host H, we define the_ homomorphism polynomial _as_<tbc>

\(Hom_{G,H}\big((y_v)_{v\in V(H)}\big)=\sum_\phi\prod_{v\in V(G)}y_{\phi(v)},\)

<tbc>_where_ \(\phi\) _ranges over all homomorphisms from G to H. A_ homomorphism _is a map_ \(\phi:V(G)\rightarrow V(H)\) _such that_

\(\{u,v\}\in E(G)\Longrightarrow\{\phi(u),\phi(v)\}\in E(H).\)

### 3 Small Circuits for Homomorphism Polynomials from Tree Decompositions

We begin by defining a new notion of width for tree decompositions.

