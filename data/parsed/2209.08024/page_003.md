<tbc>weight _at most half_ of the total weight of T . A centroid tree is built by iteratively finding a centroid and recursing on the components resulting after its removal. See Figure 1 for an example.

The fact that an (unweighted) centroid always exists was already shown in the 19-th century by C. Jordan \[Jor69\]. We sketch the easy, constructive argument that also shows the existence of a weighted centroid: start at an arbitrary vertex of T and, as long as the current vertex is not a centroid, move one edge in the direction of the component with largest weight. It is not hard to see that the procedure succeeds, visiting each vertex at most once.

A straightforward implementation of the above procedure finds an unweighted centroid tree in O(_n_log_n_) time. This running time has been improved to O(_n_) by carefully using data structures \[BFPÖ01, GPV19\]. The run-time guarantees however, do not readily generalize from the unweighted to the weighted setting. Intuitively, the difficulty lies in the fact that in the weighted case, the removal of a centroid vertex may split the tree in a very unbalanced way, leaving up to _n_-1 vertices in one component. Thus, a naive recursive approach will take \(\Theta(n^2)\) time in the worst case.

Most algorithmic applications of STTs, including those mentioned before, rely on centroid trees. It is therefore surprising that nothing appears to be known about how well the centroid tree approximates the optimal STT in either the unweighted or weighted cases. In this paper we prove that the centroid tree is a 2-approximation of the optimal STT, and that the factor 2 is, in general, best possible, both in the unweighted and weighted settings. As our main result, we also show a more precise bound on the approximation ratio of centroid trees, in terms of the maximum degree of the underlying tree T .<sup>3</sup>

Before stating our results, we need a few definitions. Consider an undirected, unrooted tree T given as input, together with a _weight function_ \(w:V(\mathcal{T})\rightarrow\mathbb{R}_{\ge 0}\). For convenience, for any subgraph H of T , we denote \(w(\mathcal{H})=\sum_{x\in V(\mathcal{H})}w(x)\). (To interpret the weights as probabilities, we need the condition _w_(T)=1. It is, however, often convenient to relax this requirement and allow arbitrary non-negative weights, which is the approach we take in this paper.)

A _search tree_ on T is a rooted tree _T_ with vertex set _V_(T) whose root is an arbitrary vertex \(r\in V(\mathcal{T})\). The children of _r_ in _T_ are the roots of search trees built on the connected components of the forest T-_r_. A tree consisting of a single vertex admits only itself as a search tree. (See Figure 1.) It follows from the definition that for all _x_, the subtree _T<sub>x</sub>_ of _T_ rooted at _x_ induces a connected subgraph T\[_V(T<sub>x</sub>_)\] of T , and moreover, _T<sub>x</sub>_ is a search tree on T\[_V(T<sub>x</sub>_)\].

The _cost_ of a search tree _T_ on T is \(\mathtt{cost}_w(T)=\sum_{x\in V(T)}w(x)\cdot\mathtt{depth}_T(x)\), where the depth of the root is taken to be 1. The _optimum cost_ `OPT`(T_,w_) is the minimum of `cost`_<sub>w</sub>(T_) over all search trees _T_ of T .

A vertex \(v\in V(\mathcal{T})\) is a _centroid_ if for all components H of T-_v_, we have \(w(\mathcal{H})\le w(\mathcal{T})/2\). A search tree _T_ of T is a _centroid tree_ if vertex _x_ is a centroid of T\[_V(T<sub>x</sub>_)\] for all \(x\in V(\mathcal{T})\). In general, the centroid tree is not unique, and centroid trees of the same tree can have different costs.<sup>4</sup> We denote by `cent`(T_,w_) the _maximum_ cost of a centroid tree of (T_,w_), with weight function _w_.

We can now state our approximation guarantee for centroid trees.

**Theorem 1.1.** _Let_ T _be a tree,_ \(w:V(\mathcal{T})\rightarrow\mathbb{R}_{\ge 0}\)_, and m=w_(T)_. Then_

\(\mathtt{cent}(\mathcal{T},w)\le 2\cdot\mathtt{OPT}(\mathcal{T},w)-m.\)

We show that this result is optimal, including in the additive term. Moreover, the constant factor 2 cannot be improved even for unweighted instances.

**Theorem 1.2.**<tbc>

_(i) For every_ \(\varepsilon>0\) _there is a sequence of instances_ (T_<sub>n</sub>,w<sub>n</sub>_) _with w<sub>n</sub>_(T_<sub>n</sub>_)=1_, and for every centroid tree C<sub>n</sub> of_ (T_<sub>n</sub>,w<sub>n</sub>_)<tbc>

\(\mathtt{cost}_{w_n}(C_n)\ge 2\cdot\mathtt{OPT}(\mathcal{T}_n,w_n)-1-\varepsilon.\)

<sup>3</sup>In their recent paper on dynamic STTs, Bose, Cardinal, Iacono, Koumoutsos, and Langerman \[BCI<sup>+</sup>20\] remark that the ratio between the costs of the centroid- and optimal trees may be unbounded. In light of our results, this observation is erroneous. It is true, however, that a centroid tree built using the uniform distribution may be far from the optimum w.r.t. a different distribution. <sup>4</sup>Consider, for instance the two different centroid trees of a path on four vertices, with weights (0.2,0.3,0.2,0.3).

