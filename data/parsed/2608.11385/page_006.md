Let input graph _H_=(_V,E_) have _n_ vertices and maximum degree \(\Delta\). Define the odd integer

\(L=2(\Delta+2)+1.\) (8)

For each \(v\in V(H)\), introduce disjoint vertex sets _A<sub>v</sub>_={_a_<sub>_v,_1</sub>_,...,a<sub>v,L</sub>_} and _B<sub>v</sub>_, each of size _L_, and add all edges of the complete bipartite graph between them. For each \(\{u,w\}\in E(H)\) and each \(j\in[L]\), add the synchronous edge {_a<sub>u,j</sub>,a<sub>w,j</sub>_} connecting the corresponding vertices in _A<sub>u</sub>_ and _A<sub>w</sub>_. (Synchronous edges are not added for vertices in the _B<sub>v</sub>_.) Finally add two anchor vertices _r,s_, the edge _e<sub>⋆</sub>_={_r,s_}, and join each anchor to every vertex in

\(W=\bigcup_{v\in V(H)}(A_v\cup B_v).\) (9)

Denote the resulting graph by _G_=G(_H_). It is unweighted, simple, and connected, with

\(N:=|V(G)|=2nL+2\) (10)

vertices. The number of edges is

\(|E(G)|=nL^2+L|E(H)|+4nL+1.\) (11)

gadget for v1
gadget for v2
Av1
Bv1
Av2
Bv2
L matching edges
v1
r
S
KL,L
KL,L
universal anchors
Av3
Bv3
v2
v3
L matching edges
L matching edges
Side 1: {v1}
Side 2: {v2, v3}
KL,L
gadget for v3
(a) Original instance H = K3
(b) Encoded graph G with three KL,L variable gadgets, L-edge matchings, and universal anchors r, s

Figure 1: The balanced counting gadget for the source instance _K_<sub>3</sub> (triangle graph). Blue and red indicate the two labels of one source maximum cut and its corresponding lift. Every _K<sub>L,L</sub>_ variable gadget is cut completely, so each _A<sub>v</sub>_ and _B<sub>v</sub>_ lie on opposite sides; the synchronous matchings among the _A_-parts reproduce the three source edges. The separated anchors _r_ and _s_ are adjacent to one another and each is joined to every vertex in _W_. Each part _A<sub>v</sub>,B<sub>v</sub>_ in panel (b) contains _L_ vertices; only representative vertices and edges are shown. For _H=K_<sub>3</sub>, the constructed graph G(_H_) has _L_=9, _N_=56, and maximum cut counts |#MC(_G_)|=2|#MC(_H_)|=12.

