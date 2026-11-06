## Search trees on trees.

We mostly follow the terminology of Bose et al. \[BCI<sup>+</sup>20\].

**Definition 1** (Search tree on tree (STT))**.** Given an unrooted tree _S_, a search tree on _S_ is a rooted tree _T_ with _V(T_)=_V(S_), where the subtrees _T<sub>x</sub>_ of _T_ are search trees on the connected components of _S_\\root(_T_), for all children _x_ of root(_T_).

Note that in STTs the ordering of children is irrelevant. See Figure 1 for illustration. The following observation is a direct consequence of the definition.

**Observation 1.** _If T is a search tree on S, then S_\[_V(T<sub>x</sub>_)\] _is a subtree of S for all_ \(x\in V(S)\)_. Furthermore, T<sub>x</sub> is a search tree on S_\[_V(T<sub>x</sub>_)\].

The rotation operation in STTs (see e.g. \[CLP18\]) generalizes BST rotations, see Figure 2.

**Definition 2** (Rotation in STTs)**.** Consider a node _x_ with parent _p_ in a search tree _T_ on _S_. A _rotation of the edge_ {_x,p_}, alternatively called _a rotation at node x_ results in a tree \(T'\) obtained from tree _T_ as follows:

(i) _x_ and _p_ swap places,<tbc>

(ii) if _x_ has a child _y_ whose subtree _T<sub>y</sub>_ contains a node adjacent to _p_ in _S_, then _y_ becomes the child of _p_,<tbc>

(iii) all other children of _x_ and _p_ preserve their parent.

The following observation is immediate.

**Observation 2.** _If T is a search tree on S, then the tree_ \(T'\) _obtained from T by an arbitrary rotation is a search tree on S._

## Steiner-closed STT.

Bose et al. introduced an important property of STTs that also plays an essential role in our results. We review this concept next.

**Definition 3** (Steiner-closed set \[BCI<sup>+</sup>20\])**.** A set of nodes \(A\subseteq V(S)\) is Steiner-closed, if every node in `ch`(_A_)\\_A_ is connected to exactly two nodes of `ch`(_A_).

Observe that for all \(A\subseteq V(S)\), the nodes in `ch`(_A_)\\_A_ are connected to _at least two_ nodes of `ch`(_A_). Therefore, if _A_ is not Steiner-closed, then there is a node \(q\in\mathtt{ch}(A)\backslash A\) that is connected to _at least three_ nodes of `ch`(_A_). See Figure 3 for illustration. The following observation is immediate.

p
X
B1
X
O
O
P
A1
Ak
B1
Bt
A1
Bt
C
X
P
B1
Bt
C
C
A1
Ak
Ak

Figure 2.: Rotation of the edge {_p,x_} in an STT _T_ (_left_), and the underlying tree _S_ (_right_). Triangles and diamonds represent subtrees of _T_ and _S_, respectively. Dots indicate an arbitrary number of subtrees that are affected in the same way by the rotation. One more rotation of the edge {_p,x_} reverses the operation.

