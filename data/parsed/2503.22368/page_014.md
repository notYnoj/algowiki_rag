<tbc>it is, in particular, also a maximal common induced subgraph of _G_<sub>1</sub>_,...,G<sub>n</sub>_. By Lemma 1, there exists a maximal clique _K_ in \(G:=\star_{i=1}^nG_i\) of size |_V(K_)|=|_V(H_)|. Hence, \(K\in\mathcal{K}\). Suppose that _K_ is not a maximum clique within K. Hence, there is a clique \(K'\in\mathcal{K}\) of size \(|K'|>|K|\). Again, by Lemma 2, there exists a common subgraph \(H'\) of _G_<sub>1</sub>_,...,G<sub>n</sub>_ of size \(|V(H')|=|V(K')|>|V(K)|\); which contradicts the fact that _H_ is an MVCS of _G_<sub>1</sub>_,...,G<sub>n</sub>_.

By similar arguments, if _K_ is a maximum clique in K but the subgraph _H_ of _G_<sub>1</sub>_,...,G<sub>n</sub>_ induced by the vertex set \(\{p_1(w)|w\in V(K)\}\) in _G_<sub>1</sub> is not maximum, we can find a larger common subgraph \(H'\) of _G_<sub>1</sub>_,...,G<sub>n</sub>_ which results in a clique \(K'\) in _G_ of size \(|V(K')|>|V(K)|\). Hence, \(K'\in\mathcal{K}\) must hold; a contradiction to the choice of _K_.

## C Edge- and vertex-labeled graphs

We are mainly interested in molecular graphs, i.e., simple undirected graphs whose vertices correspond to different atom types and where edges represent pairs of vertices that are connected via a particular type of bond, e.g., hydrogen bonds.

To cover this, we circumvent the explicit construction of such graphs and instead consider a set of vertices _V(G_), a map \(\nu_G:V\rightarrow\mathfrak{V}\) assigning to each vertex \(v\in V(G)\) a symbol \(\nu_G(v)\in\mathfrak{V}\) (the type of atom it represents), and a map \(\varepsilon_G:\genfrac(){pt}{2}{V}{2}\rightarrow\mathfrak{C}\) that assigns to each 2-element subset \(\{u,v\}\in\genfrac(){pt}{2}{V}{2}\) a symbol \(\varepsilon_G(u,v)\in\mathfrak{C}\), which specifies whether _u_ and _v_ are linked by some type of bond or if _u_ and _v_ are not linked at all. In particular, we use the special symbol `E` to specify that \(\varepsilon_G(u,v)\) indicates no bond between _u_ and _v_. We write _G_=

G
H
7
7
5
6
5
6
4
3
4
3
1
2
1
2

**Fig.4.** By way of example, The product contains the clique \(K=\{(1,5),(2,3),(4,4),(5,1),(3,2)\}\subseteq V(G\star H)\). This clique _K_ is inclusion-maximal. To see this, observe that any additional vertex (_x,y_) we may add to _K_ to obtain a larger clique must satisfy \(x,y\notin\{1,2,3,4,5\}\) as neither _G_ nor _H_ contains edges (1,1)_,...,_(5,5). Hence, only \(x,y\in\{6,7\}\) is possible. Since 5 is adjacent to 7 and 3 is adjacent to 6 but 1 is not adjacent to 7 and 6 in _G_ and _H_, it follows that the subgraph induced by \(V(K)\cup\{(x,y)\}\) with \(x,y\in\{6,7\}\) cannot form a clique in _G⋆H_. Since _K_ corresponds to the subgraph induced by {1,2,3,4,5} and since \(G\simeq H\), it follows that _K_ does not correspond to a maximal common subgraph of _G_ and _H_.

