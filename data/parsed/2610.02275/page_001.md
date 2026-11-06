Maximum Edge Open Packing on AT-Free, Chordal, and Convex Bipartite Graphs

**Abstract**

An edge open packing is a set of edges whose endpoints induce a disjoint union of stars. We study the problem of finding a maximum edge open packing in AT-free, chordal, and convex bipartite graphs. For AT-free graphs, we use the oriented star-conflict graph _A<sub>G</sub>_, introduced by Das and Santra, for which \(\rho_\mathrm{e}^o(G)=\alpha(A_G)\), and prove that _A<sub>G</sub>_ is AT-free whenever _G_ is AT-free. Consequently, a known maximum independent set algorithm for AT-free graphs yields an _O(n_<sup>2</sup>+_m_<sup>4</sup>)-time algorithm for Maximum Edge Open Packing, where _n_ and _m_ denote the numbers of vertices and edges of _G_, respectively. For chordal graphs, we develop an _O(n_<sup>4</sup>)-time dynamic programming algorithm over a nice tree decomposition derived from a clique tree, exploiting the structural fact that the endpoint set of an edge open packing intersects every clique in at most two vertices. Finally, for convex bipartite graphs, we obtain an _O(n_<sup>4</sup>)-time dynamic programming algorithm based on two boundary indices that separate consecutive star components. This result extends the previously known algorithm for biconvex bipartite graphs and, in particular, provides an improved explicit running-time bound for that class.

**Keywords:** Edge open packing; Induced matching; AT-free graphs; Chordal graphs; Convex bipartite graphs; Maximum independent set; Dynamic programming

## 1 Introduction

An induced matching selects edges whose endpoints induce a matching. It is a standard model for choosing mutually isolated interactions and has been studied extensively in graph algorithms [7, 17, 11]. Edge open packing, introduced by Chelladurai et al. [9], allows several selected edges to share a common centre while retaining separation between different components. For example, all _t_ edges of a star _K_<sub>1_,t_</sub> form an edge open packing, whereas an induced matching contains at most one of them.

One motivation comes from channel assignment under a secondary-interference model in packet radio networks [9, 8]. In this model, two selected links conflict when a third link joins their endpoints. A maximum edge open packing is therefore a largest feasible set of links for one channel, and the colour classes of an injective edge colouring are edge open packings. The model permits several links with a shared star centre. More abstractly, it describes the selection of mutually isolated groups of interactions, each organised around one hub.

Formally, let _G_=(_V,E_) be a graph. Two distinct edges have a _common edge_ if an edge other than those two joins an endpoint of one to an endpoint of the other. An _edge open packing_ is a set \(D\subseteq E\) in which no two distinct edges have a common edge. Its maximum cardinality is the _edge open packing number_, denoted by \(\rho_\mathrm{e}^o(G)\), and the optimisation problem of finding such a set is called Maximum Edge Open Packing. If _V(D_) denotes the endpoints of the edges in _D_, then _D_ is an edge open packing precisely when the connected components of _G[V(D_)] are stars, including single edges. Thus, the problem extends induced matching by permitting larger star components.

Brešar and Samadi [5] proved that the decision version is NP-complete on restricted classes including planar graphs of maximum degree four and Eulerian bipartite graphs, and gave a linear-time algorithm for trees. Structural work relates edge open packing to induced matching, diameter, minimum degree,

<sup>∗</sup>gkd@iitg.ac.in <sup>†</sup>kamal.7.2013@gmail.com, kamal.santra@iitg.ac.in

Gautam K. Das<sup>∗</sup><sup>1</sup> and Kamal Santra <sup>†</sup><sup>1</sup>

<sup>1</sup>Department of Mathematics, Indian Institute of Technology Guwahati, Guwahati, 781039, Assam, India

arXiv:2610.02275v1 [cs.DM] 1 Oct 2026

