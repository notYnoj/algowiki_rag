<tbc>tree with the same keys as _Q<sub>i</sub>_ such that \(x_i=\text{root}(Q'_i)\), and _T<sub>i</sub>_ results from substituting \(Q'_i\) for _Q<sub>i</sub>_ in _T_<sub>_i_-1</sub>, where _T_<sub>0</sub>=_T_. (We refer to _T<sub>m</sub>_ as the execution’s _final tree._) The _cost_ of _E_ is \(\sum_{i=1}^m|Q'_i|\). At least one execution for _X_ starting from _T_ has minimum, or _optimum_ cost, and we denote this cost by OPT(_X,T_). Figure 1 shows an instance and a corresponding execution.

An execution’s rooted hull and after-tree for a given request are uniquely determined by the previous after-tree and the request’s transition tree. Thus we shall occasionally denote an execution by its sequence of transition trees. Defining the cost of an execution as the sum of the transition tree sizes captures the notion of paying for restructuring: fewer operations are required to substitute a smaller tree. Each rooted hull contains the access path, which accounts for the cost of searching. We describe instances that include insertions and deletions in Section 5.

Unless otherwise implied, we may assume without loss of generality that every node in the initial tree _T_ has a descendant in _T_ whose key is requested in _X_ \[15, Theorem 43\], in which case every key in _T_ appears in at least one transition tree and \(\text{OPT}(X,T)\ge|T|\). Similarly, \(\text{OPT}(X,T)\ge|X|\) since every execution produces at least one transition tree per request. Furthermore, since an optimal algorithm can reshape the entire initial tree on the first request, \(\text{OPT}(X,T)\le\text{OPT}(X,T')+|T|\) for any pair of valid binary search trees _T_ and \(T'\) for request sequence _X_ with the same keys. Therefore, it makes little difference to optimal executions whether the initial tree is left specified or unspecified, and many authors do not distinguish between OPT(_X,T_) and OPT<sub>min</sub>(_X_)=min_<sub>T</sub>_ for _X_ OPT(_X,T_). However, the initial tree can, potentially, have a significant impact on algorithmic behavior. Thus, we require instances to specify an initial tree. We discuss this further in Section 4.

A binary search tree _algorithm_ A maps each instance to an execution of the instance. We denote the cost of this execution by cost<sub>A</sub>(_X,T_). We say A is _dynamically optimal_ if there is some constant \(c\ge 1\) so that \(\text{cost}_\mathcal{A}(X,T)\le c\text{OPT}(X,T)\) for all request sequences _X_ and all corresponding initial trees _T_. (Other terms include "constant-competitive" and "instance optimal.")

A _rotation_ at left child _x_ with parent _y_ in _T_ replaces the subtree rooted at _y_ with the tree whose root _x_ has right child _y_ such that the right subtree of _x_ before the rotation becomes the left subtree of _y_ afterward and the left subtree of _x_ and right subtree of _y_ are unchanged. Figure 2 depicts this process. We can also identify this rotation with the edge connecting _x_ to _y_ in _T_. Rotation at a right child is symmetric, and rotation at the root is undefined. Rotation preserves symmetric order while changing up to three child pointers in the tree. Sleator and Tarjan originally measured execution cost by counting rotations. (See Appendix A.)

A _splay_ operation begins with a binary search for a key in the tree. Let _x_ be the node returned<tbc>

TO
T 1
T 2
T 3
3
1
2
6
1
6
3
1
6
2
1
2
6
3
Q3
1
3
Q1
2
4
Q2
4
4
4
5
5
5
Q1
1
Q2
2
Q3
6
3
1
6
X= (1, 2, 6)
2
3

Figure 1: Example of an execution for a binary search tree instance. The total cost is eight.

