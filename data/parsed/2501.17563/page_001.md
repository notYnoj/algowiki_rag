Search Trees on Trees via LP

**Abstract**

We consider the problem of computing optimal search trees on trees (STTs). STTs generalize binary search trees (BSTs) in which we search nodes in a path (linear order) to search trees that facilitate search over general tree topologies. Golinsky [9] proposed a linear programming (LP) relaxation of the problem of computing an optimal static STT over a given tree topology. He used this LP formulation to compute an STT that is a 2-approximation to an optimal STT, and conjectured that it is, in fact, an extended formulation of the convex-hull of all depths-vectors of STTs, and thus always gives an optimal solution. In this work we study this LP approach further. We show that the conjecture is false and that Golinsky’s LP does not always give an optimal solution. To show this we use what we call the _normals method_. We use this method to enumerate over vertices of Golinsky’s polytope for all tree topologies of no more than 8 nodes. We give a lower bound on the integrality gap of the LP and on the approximation ratio of Golinsky’s rounding method. We further enumerate several research directions that can lead to the resolution of the question whether one can compute an optimal STT in polynomial time.

## 1 Preliminaries, Definitions and Known Results

We consider the problem of search trees on trees (STTs) which we now describe briefly. For a broader context and additional references, see the works of [4, 5, 6, 9].

The problem of STTs is as follows. We are given a tree topology, and have to construct a search tree (STT) for it where we can search for nodes in response to requests. To answer a request, we make queries on the STT as follows. We start at the root, and query an oracle that tells us whether we found the searched node, or to which direction in the tree (a connected component), with respect to the query, we should proceed. Loosely speaking, the underlying tree and its search tree may have completely different structures, since it is usually beneficial to query a vertex which is not adjacent to _v_ following a query to _v_. But both are trees over the same set of nodes. The cost of a query is the number of oracle queries until the specified node is found.

We focus on the static setting, where the STT is fixed. In this case, we assume that we know the query distribution, _f_ (for frequencies), of the nodes in advance. We want to construct an optimal _static_ search tree for _f_. There is also the dynamic setting which we do not consider here, where the

<sup>∗</sup>Tel Aviv University, yanivsadeh@tau.ac.il. Partially supported by the Israel Science Foundation grant no. 1156/23 and the Blavatnik Family Foundation. <sup>†</sup>Tel Aviv University, haimk@tau.ac.il. Partially supported by the Israel Science Foundation grant no. 1156/23 and the Blavatnik Family Foundation. <sup>‡</sup>Tel Aviv University, zwick@tau.ac.il

Yaniv Sadeh<sup>∗</sup>

Haim Kaplan<sup>†</sup>

Uri Zwick<sup>‡</sup>

August 4, 2025

arXiv:2501.17563v2 [cs.DS] 1 Aug 2025

