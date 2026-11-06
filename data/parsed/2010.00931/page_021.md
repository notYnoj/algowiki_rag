<tbc>least 3 in ch(_P_). There must be three distinct nodes \(u,v,w\in P\) that are pairwise separated by _y_. W.l.o.g., no other node in _P_ separates either of _u,v,w_ from _y_ (i.e., choose _u,v,w_ such that their distance to _y_ is minimal). Clearly, \(y\in V(T_x)\). Let _z_ be the child of _x_ such that \(y\in V(T_z)\). Then \(\{u,v,w\}\subseteq\delta(T_z)\), so _T_ is not a 2-cut STT.

We have the following corollary of Theorem 2.

**Corollary 1.** _Given two Steiner-closed STTs T and_ \(T'\) _on the same n-node tree S, we can transform T into_ \(T'\) _through a sequence of at most_ 3_n_-5 _rotations, such that all intermediate trees are Steiner-closed. Moreover, starting with a pointer at the root, we can transform T into_ \(T'\) _through a sequence of_ O(_n_) _pointer moves and rotations at the pointer._

## 5. Splay trees on trees

In this section we extend Splay trees, introduced by Sleator and Tarjan [ST85] to the setting of trees on trees. The Splay tree is an adaptive BST, re-arranged via rotations after every search. (Other operations such as insert, delete, split, etc. are also defined, but for the sake of simplicity we only focus on searches.)

A search for an element _x_ proceeds as in a normal BST, following the search path from the root to node _x_. Afterwards, _x_ is rotated to the root in a series of local steps (called by Sleator and Tarjan the ZIG, ZIG-ZIG, and ZIG-ZAG steps), with the entire transformation of the tree called _splaying x_. Intuitively, the effect of splaying, besides bringing _x_ to the root, is to approximately halve the depth of every node on the search path [Sub96, CGK<sup>+</sup>15b].

Splaying can be defined in a number of equivalent ways. A simple view is that _x_ is rotated to the root, with the rotations grouped in consecutive pairs. For each pair, if the parent _p_ and the grandparent _g_ of _x_ are _on the same side of x_ (i.e. both to the right or both to the left), then we _skip ahead_ and rotate at _p_ first, then at _x_ (this is the ZIG-ZIG step). Otherwise, we do both rotations at _x_, without skipping ahead (this is the ZIG-ZAG step). If the search path is of odd length, then the entire process is finished by a simple rotation (a ZIG step). The "skipping ahead" of ZIG-ZIG is crucial for the efficiency of Splay; a simple rotate-to-root strategy is well-known to be inefficient on some examples.

The above description of Splay trees can be easily extended to STTs, with an appropriate generalization of the parent and grandparent being "on the same side of _x_". We now describe this generalization. To splay _x_, we repeatedly apply one of three types of operations (the extensions of ZIG, ZIG-ZIG, and ZIG-ZAG). For reasons that will become clear later, we define splaying more generally, bringing _x_ not necessarily to the root, but to a given point on the search path. We refer to Algorithm 3 and Figure 5 for details.

Observe that splay(_x,y_) includes as special case the operation of splaying _x_ all the way to the root, when called as splay(_x,null_). It is easy to verify that when the underlying tree _S_ is a path, i.e. in the BST case, the defined splaying operation is identical with the classical splaying of Sleator and Tarjan.

The algorithm, as described, is not well-defined for arbitrary STTs. Besides the two cases (Line 8) _p_ separates _x_ and _g_, and (Line 10) _x_ separates _p_ and _g_, there is a third possible case, when none of _x_, _p_, and _g_ separate the other two. (A hypothetical fourth case, where<tbc>

