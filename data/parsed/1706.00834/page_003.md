<tbc>Also, the CH algorithm (and its current extensions (Suehiro et al., 2012; Rajkumar and Agarwal, 2014; Gupta et al., 2016)) cannot be directly applied to problems like BST. The reason is that CH maintains a mean vector of the BSTs which lives in the convex hull of all BSTs with the representation above and this polytope does not have a characterization with polynomially many facets<sup>1</sup>.

In this paper we manage to construct an alternate representation from the offline dynamic programming algorithm for say the BST problem. This gives us a polytope with a polynomial number of facets while the loss is linear in the natural components of the BST problem. This well-behaved polytope will allow us to implement CH efficiently. We also use this representation to implement EH efficiently.

## Paper Outline.

We start with online learning of paths in a directed graph in Section 2 and give an overview on existing algorithms: Expanded Hedge and Component Hedge. In Section 3, We generalize the definition of edge as an ordered pair (_v,u_) of vertices to _multiedge_ which is an ordered pair (_v,U_) where the first element _v_ is a vertex and the second element _U_ is a _subset of the vertices_. Following from this generalization, we extend the definitions of paths, graphs and directed acyclic graphs (DAG) accordingly (see  1; Section 3 contains the formal definitions). These extensions allow us to generalize the existing EH (Section 3.1) and CH (Section 3.2) algorithms from online shortest path problem to learning multipaths. For EH, we introduce the _stochastic product form_ as a concise way of maintaining a distributions over all multipaths. For CH, on the other hand, we maintain the mean vector of a distribution in the _unit-flow polytope_ which has polynomial number of facets. Moreover, we also introduce a new and faster prediction technique for CH for multipaths which directly samples from an appropriate distribution, bypassing the need to create convex combinations. More specifically, we use the maintained mean vector in the unit-flow polytope in the CH algorithm and construct an appropriate distribution in the stochastic product form. In Section 4, we define a general class of combinatorial online<tbc>

1. There is an alternate polytope for BSTs with a polynomial number of facets (called the _associahedron_ (Loday, 2005)) but the average search cost is not linear in terms of the components used for this polytope. CH and its extensions, however, rely heavily on the additivity of the loss over the components. Thus they cannot be applied to the associahedron.

\begin{tabular}{ccc}
**Graph** & \(\Longrightarrow\) & **Multigraph** \\
with the set of vertices _V_ & \multicolumn{2}{c}{with the set of vertices _V_} \\
**Edge** (_v,u_) & \multicolumn{2}{c}{**Multiedge** (_v,U_)} \\
\(u,v\in V\) & \(\Longrightarrow\) & \(v\in V\), \(U\subset V\) \\
 & & \\
**Path** & \(\Longrightarrow\) & **Multipath** \\
**DAG** & \(\Longrightarrow\) & **Multi-DAG** \\
\end{tabular}

