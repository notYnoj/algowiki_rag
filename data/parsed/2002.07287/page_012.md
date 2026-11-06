amount of all numbers in _S_ that are part of R_<sub>i</sub>_.

We create _Q<sub>i</sub>_ only if _S_ contains numbers of a region R_<sub>i</sub>_. Summed over the \(k\le N/\tau\) non empty regions, our structure uses \((\sum_{x=0}^kO(log\#(x,S)))+O(\tau k)=\sum_{x=0}^kO(log\#(x,S))+O(N)=O(N)\) bits.

For a structure _Q<sub>i</sub>_, the array _A<sub>i</sub>_ can be constructed in \(O(k')\) time, where \(k'\) are the number of self-delimiting numbers in \(\mathcal{R}_i\cap S\). Let the numbers inside the _i_th region occupy \(N'\) bits. The rank-select structure can be initialized in \(O(N'/\tau)\) time. Since our smallest possible self-delimiting number uses \(\Omega(1)\) bits and the largest possible uses \(O(\tau)\) bits, the sum of the numbers of region R_<sub>i</sub>_ is within \(N'\) and \(2^{N^\prime}\) and our amount of numbers within \(N'\) bits is within the bounds \(\Omega(N'/\tau)\) (if most self-delimiting numbers are large) and \(O(N')\) (if most self-delimiting numbers are small). In the worst-case, we store \(\Theta(N'/\tau)\) numbers within the \(N'\) bits, and we end up with a construction time that is linear to the amount of numbers in _Q<sub>i</sub>_. Therefore, in total our structure can be constructed in \(O(k+N/\tau)\) time. \(\blacktriangleleft\)

## 4 Preliminaries for Tree Isomorphism

In this paper we use basic graph and tree terminology as given in [41]. By designating a node of a tree as the root, the tree becomes a _rooted_ tree. If the nodes of a tree have labels, the tree is _labeled_, otherwise, the tree is called _unlabeled_. If there is a color associated with each node of the tree, it is called _node-colored_. The _parent_ of a node in a rooted tree is the neighbor of _u_ on the shortest path from _u_ to the root. The root has no parent. The _children_ of a node _u_ are the neighbors of _u_ that are not its parent. A _leaf_ is a node with no children. Two nodes that share the same parent are _siblings_. A _descendant_ of a node is either a child of the node or a child of some descendant of the node. By fixing the order of the children of each node a rooted tree becomes an _ordinal_ tree. The _right sibling_ (_left sibling_) of a node _u_ is the sibling of _u_ that comes after (before) _u_ in the aforementioned order, if it exists. We denote by deg(_v_) the degree of a node _v_, i.e., the number of neighbors of _v_, and by desc(_u_) the number of descendants of a node _u_ in a tree. The _height_ of _u_ is defined as the number of edges between _u_ and the longest path to a descendant leaf. The _depth_ of _u_ is defined as the number of edges on the path between _u_ and the root.

\(\blacktriangleright\) **Definition 7.** _(balanced parenthesis representation of an ordinal tree) A balanced parenthesis representation_ `bpr` _of an ordinal n-node tree T is a sequence of_ 2_n parenthesis and is defined recursively on the root u of T as_

\(\mathtt{bpr}_u=(\mathtt{bpr}_{v_1}\dots\mathtt{bpr}_{v_{deg(u)}})\)

_where v_<sub>1</sub> _is the leftmost child of u and the v_<sub>deg(_u_)</sub> _the rightmost child of u._

For this representation, Munro and Raman [42] showed a succinct data structure (using 2_n+o(n_) bits) that allows constant-time _tree navigation_, which we use. A similar data structure was previously shown by Jacobson [39] who showed a succinct data structure called _level order unary degree sequence_ (LOUDS) that also provides tree navigation.

\(\blacktriangleright\) **Definition 8.** _(tree navigation) Given a node u of an ordinal tree T, tree navigation allows access to_

parent(_u_) _that returns the parent of u, or_ `null` _if u is the root,_

firstChild(_u_) _returns the first child of u if_ \(deg(u)\neq 0\),

leftSibling/rightSibling(_u_) _returns the left / right sibling of u, or_ `null` _if none exists._

