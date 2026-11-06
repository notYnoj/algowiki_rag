### 1.2 Organization of the Paper

The aim of Section 2 is to give the necessary notation and a formal statement of the problem (Sections 2.1 and 2.2) and to provide two different but equivalent problem formulations that will be more convenient for our analysis. As opposed to the classical problem formulation in which a strategy is seen as a _decision tree_, Section 2.3 restates the problem in such a way that with each vertex _v_ of the input tree we associate a sequence of vertices that need to be iteratively queried when _v_ is the root of the current subtree that contains the target node. In Section 2.4 we extend this approach by associating with each vertex a sequence of not only vertices to be queried but also time points of the queries.

The latter problem formulation is suitable for a dynamic programming algorithm provided in Section 3.1. In this section we introduce an auxiliary, slightly modified measure of the cost of a search strategy. First we provide a quasi-polynomial time dynamic programming scheme that provides an arbitrarily good approximation of the output search strategy with respect to this modified cost (the analysis is deferred to Section 4), and then we prove that the new measure is sufficiently close to the original one (the analysis is deferred to Section 5). These two facts provide the quasi-polynomial time scheme for the tree search problem, achieving a \((1+\varepsilon)\)-approximation with a computation time of \(n^{O(\mathrm{log}n/\varepsilon^2)}\), for any \(0<\varepsilon<1\).

In Section 3.2 we observe how to use the above algorithm to derive a polynomial-time \(O(\sqrt{\mathrm{log}n})\)-approximation algorithm for the tree search problem. This is done by a divide and conquer approach: a sufficiently small subtree _T_<sup>∗</sup> of the input tree _T_ is first computed so that the quasi-polynomial time algorithm runs in polynomial (in the size of _T_) time for _T_<sup>∗</sup>. This decomposes the problem: having a search strategy for _T_<sup>∗</sup>, the search strategies for _T-T_<sup>∗</sup> are computed recursively. Details of the approach are provided in Section 6.

## 2 Preliminaries

### 2.1 Notation and Query Model

We now recall the problem of searching of an unknown target node _x_ by performing queries on the vertices of a given node-weighted rooted tree _T_=(_V,E,w_) with weight function \(w:V\rightarrow\mathbb{R}_+\). Each _query_ selects one vertex _v_ of _T_ and after _w(v_) time units receives an answer: either the query returns _true_, meaning that _x=v_, or it returns a neighbor _u_ of _v_ which lies closer to the target _x_ than _v_. Since we assume that the queried graph _T_ is a tree, such a neighbor _u_ is unique and is equivalently described as the unique neighbor of _v_ belonging to the same connected component of _T_\\{_v_} as _x_.

All trees we consider are rooted. Given a tree _T_, the root is denoted by _r(T_). For a node \(v\in V\) , we denote by _T<sub>v</sub>_ the subtree of _T_ rooted at _v_. For any subset \(V'\subseteq V\) (respectively, \(E'\subseteq E\)) we denote by \(T[V']\) (resp., \(T[E']\)) the minimal subtree of _T_ containing all nodes from \(V'\) (resp., all edges from \(E'\)). For \(v\in V\) , _N(v_) is the set of neighbors of _v_ in _T_.

For \(U\subseteq V\) and a target node \(x\notin U\), there exists a unique maximal subtree of _T_\\_U_ that contains _x_; we will denote this subtree by \(T\langle U,x\rangle\).

We denote |_V_|=_n_. We will assume w.l.o.g. that the maximum weight of a vertex is normalized to 1. (This normalization is immediately obtained by a proportional scaling of all units of cost.) We will also assume w.l.o.g. that the weight function satisfies the following _star condition_:

\(\text{for all}v\in V,w(v)\le\sum_{u\in N(v)}w(u).\)

Observe that if this condition is not fulfilled, i.e., for some vertex _v_ will have \(w(v)>\sum_{u\in N(v)}w(u)\),<tbc>

