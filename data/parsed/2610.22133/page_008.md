## 8 Asteroidal Triples and Friends in (Likely Necessary) Matrix Multiplication Time

{_x,y,z_} if and only if \(\mathbf{G}'\) contains an AT \(\{x',y',z'\}^7\) (see Figure 2a). To achieve this, it suffices to invert all edges in **G** (including those within _X,Y_ , and _Z_ , which consequently become cliques) and add three new vertices _a,b,c_ that are fully connected to \(X\cup Z\), \(Y\cup Z\), and \(X\cup Y\) , respectively. We also add the edges {_a,b_}, {_b,c_}, and {_c,a_}. It is easy to see that \(\mathbf{G}'\) satisfies the claimed property. However, notice that for every triple with \(x\in X\), \(y\in Y\) , and \(z\in Z\) , there is always an _x-y_ path avoiding _N[z_] (and similarly for the other pairs). This means that the reduction relies solely on the fact that an AT {_x,y,z_} is an independent set, as the path condition holds vacuously. The open question was thus whether this path condition which is not exploited in the lower bound could introduce additional computational hardness.

Moving on to the algorithm, we first illustrate Kratsch and Spinrad’s approach. Given a graph **G**=(_V,E_), define for each \(v\in V\) the graph **G**_<sub>v</sub>_:=**G**[_V_\\_N[v_]], obtained by removing the closed neighborhood of _v_. As a first step, Kratsch and Spinrad compute the neighborhood-deleted components, i.e., the connected components of each **G**_<sub>v</sub>_, and then construct a graph \(\tilde{\mathbf{G}}\) as follows:<sup>8</sup>

\(\blacksquare\) 1 for each \(v\in V\) and each connected component _C_ of **G**_<sub>v</sub>_, they introduce a node in \(\tilde{\mathbf{G}}\); and

\(\blacksquare\) 2 for each non-edge {_u,v_} of **G**, they add an edge {_Cu(v),C<sub>v</sub>(u_)} in \(\tilde{\mathbf{G}}\), where _C<sub>x</sub>(y_) now denotes the connected component containing _y_ in **G**_<sub>x</sub>_.

It is not difficult to see that **G** contains an AT if and only if \(\tilde{\mathbf{G}}\) contains a triangle. This allows us to solve the problem by running a triangle detection algorithm on \(\tilde{\mathbf{G}}\). However, due to the number of nodes in \(\tilde{\mathbf{G}}\), we cannot use standard triangle detection; instead, we must resort to sparse triangle detection, which runs in time \(\mathcal{O}(m^{2\omega/(\omega+1)})\), where _m_ is the number of edges [AYZ97]. Since \(\tilde{\mathbf{G}}\) has O(_n_<sup>2</sup>) edges, this running time becomes \(\mathcal{O}(n^{4\omega/(\omega+1)})=\mathcal{O}(n^{2.81})\).<sup>9</sup>

The first key fact we prove is that if \(\tilde{\mathbf{G}}\) contains a triangle {_C_<sub>1</sub>_,C_<sub>2</sub>_,C_<sub>3</sub>} and \(C'_1\) is a connected component containing exactly the same nodes as _C_<sub>1</sub>, then \(\{C'_1,C_2,C_3\}\) is also a triangle (even if _C_<sub>1</sub> and \(C'_1\) come from different graphs **G**_<sub>v</sub>_). Thus, for each distinct connected component across all graphs **G**_<sub>x</sub>_, it suffices to retain only one representative in \(\tilde{\mathbf{G}}\).

<sup>7</sup> It is well known that triangle detection on an _n_-node graph can be reduced to triangle detection on a tripartite 3_n_-node graph: simply create three copies of the vertex set and add edges only between copies of adjacent nodes that reside in different vertex partitions. <sup>8</sup> Technically, the graph \(\tilde{\mathbf{G}}\) we construct is the knotting graph _K_(**G**) of **G**. Knotting graphs were introduced by Gallai [Gal67], who showed that **G** is a comparability graph if and only if _K_(**G**) is bipartite. <sup>9</sup> To be precise, the observation regarding the construction of this graph is due to Lekkerkerker and Boland [LB62], while the use of sparse matrix multiplication was introduced by Köhler [Kö04]. However, Kratsch and Spinrad were the first to achieve an overall subcubic running time, by computing the neighborhood-deleted components subcubically.

N(v)
C
Z
y
Z
Y
X
Y
X
Y
v
N(Z)
N(Y)
a
b
N(X)
X
Z
Z
X
G
G'
= a
= b

**Figure 2.** Visualization of the lower bound construction and a fact that we use in the \(\tilde{\mathcal{O}}(n^\omega)\)-time algorithm for asteroidal triple detection. In (a), dashed gray edges join the auxiliary vertices _a,b,c_.

