<tbc>**Definitions, notation and preliminaries**

In this section we introduce some fundamental notation, definitions and results that will be required throughout. We write \[_n_\] to be the set of integers from 1 to _n_, that is \[_n_\]:={1,2_,...,n_}, and \[_i,n_\]:={_i,i_+1_,...,n_} to be the set of integers from _i_ to _n_ for any \(i\le n\). In an abuse of notation, we also use \[_a,b_\] in the continuous sense such that \([a,b]:=\{c\in\mathbb{R}:a\le c\le b\}\), but the meaning should be clear from context.

A _k-uniform hypergraph H_:=_H(V,E_) consists of a vertex set _V(H_) and an edge set _E(H_) whose elements are _k_-subsets of _V(H_). We shall often abbreviate _k_-uniform hypergraph to _k-graph_, and may use ‘graph’ when referring to a hypergraph. For an edge _e_={_v_<sub>1</sub>_,...,v<sub>k</sub>_}, we may sometimes write _e=v_<sub>1</sub>_...v<sub>k</sub>_. Additionally we associate _H_ to its edge set rather than its vertex set, and so may write \(e\in H\) or \(|H|\) in place of \(e\in E(H)\) and \(|E(H)|\) respectively. For a hypergraph _H_ and \(U\subset V(H)\), the subhypergraph of _H induced_ by _U_, _H_\[_U_\], is the subhypergraph of _H_ with vertex set _V(H_\[_U_\])=_U_ and edge set consisting of all edges between the vertices of _U_ in _H_. In an abuse of notation, we may sometimes induce a subhypergraph on an edge set, or collection of edges rather than a set of vertices. In this case, it should be read as the subhypergraph induced by the vertices contained in the given collection.

A _matching M_ in a hypergraph _H_ is a collection of disjoint edges in _H_. That is, \(M\subseteq E(H)\) such that \(e\cap f=\emptyset\) for all distinct \(e,f\in M\). A matching _M_ is a _perfect matching_ if \(\bigcup_{e\in M}e=V(H)\). An _almost-perfect matching_ is a matching such that all but a _o_(1) proportion of the vertices are covered. We often use \(V(M):=\bigcup_{e\in M}e\) for a matching _M_, or more generally for any collection of edges, or structures that are themselves collections of vertices.

For a set _S_ and \(l\in\mathbb{N}\), we write \(\genfrac(){pt}{2}{S}{l}\) to be the collection of all _l_-sets from _S_. Additionally we write \(\genfrac(){pt}{2}{S}{\le l}:=\bigcup_{i\le l}\genfrac(){pt}{2}{S}{l}\).

The _degree_, _d<sub>T</sub>(H_) or _d_<sub>{_v_<sub>1</sub>_,...,v<sub>t</sub>_}</sub>(_H_), of a set of vertices _T_={_v_<sub>1</sub>_,...,v<sub>t</sub>_} in a hypergraph _H_ is the number of edges that contain _T_ as a subset. When we refer to the _vertex degree_ we are considering sets _T_={_v_} only of size one and write _d<sub>v</sub>(H_), the _pair degree_ refers to sets of size two, and the _codegree_ of a _k_-graph refers to the degree of sets of size _k_-1. The minimum _t_-degree, \(\delta_t(H):=min\{d_T(H):T\subseteq V(H),|T|=t\}\), of _H_ is the minimum of _d<sub>T</sub>(H_) over every subset of vertices _T_ in _H_ of size _t_.

**2.1. Bachmann-Landau Notation**

In this section we formally define little-_o_, big-_O_, \(\omega\), \(\Omega\) and \(\Theta\) notation, collectively known as Bachmann-Landau notation, which are used throughout in the discussion of asymptotic results.

