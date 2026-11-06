**Definition 3** (Inverse edges)**.** For a weakly-connected digraph with positive edge weights (_G,_**w**) and a tree edge \(e\in E(T)\), by \(\mathrm{Inv}(G,\mathbf{w},e)=\{b\in B:T-e+b\text{is acyclic}\}\) we denote the set of all _inverse_ edges of _e_ in _G_.

For a tree edge set \(S\subseteq E(T)\), by \(\mathrm{Inv}(G,\mathbf{w},S)=\bigcup_{e\in S}\mathrm{Inv}(G,\mathbf{w},e)\) we denote the union of all inverse edges among all edges in _S_. We shorten the notation to just Inv(_e_) and Inv(_S_).

We start by observing basic properties of inverse edges that follow from their definition.

**Observation 1.** _Let_ \(b\in B\) _be a blocked edge that goes from u to v. Then T contains a directed path P from v to u. Moreover, for a tree edge e, an edge_ \(b\in\mathrm{Inv}(e)\) _iff e lies on P._

_Proof._ Since _b_ is a _blocked_ edge, the subgraph _T+b_ contains a directed cycle _C_, and _b_ lies on it (because _T_ is acyclic). Then there is a path _P_ in _T_ from _v_ to _u_.

Since _T_ is a tree, _C_ is the only cycle in _T+b_. Hence for each _e_ on _P_, we have that _T-e+b_ is acyclic. Conversely, if \(e\notin P\), then \(P\subseteq T-e+b\) and therefore the subgraph still contains _C_.

We also note that if \(X\subseteq G\) is acyclic and _S_ is the set of all tree edges of _G_ outside _E(X_), then _X_ can contain only blocked edges from the set Inv(_S_).

**Observation 2.** _If_ \(X\subseteq G\) _is acyclic and S=E(T_)\\_E(X), then_ \(X\subseteq T+A-S+\mathrm{Inv}(S)\).

_Proof._ Assume the contrary. Then _X_ contains some blocked edge \(b\notin\mathrm{Inv}(S)\). Suppose that _b_ goes from _u_ to _v_. By Observation 1, we know that _T_ contains a directed path _P_ from _v_ to _u_. Together with _b_, this path yields a cycle _C_ in _T+b_. Since \(b\notin\mathrm{Inv}(s)\) for every \(s\in S\), the same observation guarantees that \(S\cap P=\emptyset\) and hence \(P\subseteq T-S\subseteq X\). Therefore, _X_ still contains _C_ which contradicts its acyclicity.

Finally, we observe that blocked and inverse edges have to follow specific directions derived from a cut of _T_ (see Figure 1 (b)).

**Observation 3.** _Let_ \(e\in E(T)\) _and let X,Y be the vertex sets of two weakly-connected components of T-e labeled so that e goes from X to Y in G. Then_

1. _For each_ \(b\in B\)_, b does not go from X to Y in G;_<tbc>

_2._ _For each_ \(b\in\mathrm{Inv}(e)\)_, b goes from Y to X in G._<tbc>



e
X
Y

(a)

(b)

Figure 1: (a) An instance with six tree edges (thick black), four allowed edges (green) and four blocked edges (red). (b) Inv(_e_) is the set of all edges that start in _X_ (vertices reachable from _e_ in _T_) and end in _Y_ (vertices _e_ is reachable from in _T_).

