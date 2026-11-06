<tbc>_If T is binary and_ \(x\in T\)_, we denote the left child of x by l(x_) _and the right child of x by r(x). Thus x is a fringe node if_ \(l(x)=r(x)=\emptyset\)_. We denote the sibling of x by_ \(\sigma(x)\).

_For a node_ \(x\in T\)_, we will define the_ depth _of x, to be denoted by d(x), to be_ \(d(\emptyset)=0\) _and_ \(d(x)=1+d(\pi(x))\) _otherwise._

_Given a weighted tree T, the_ cost _of T, to be denoted c(T), will be defined to be_

\(c(T)=\sum_{x\in T}d(x)p(x).\)

One additional property that will be of interest to us is a node that is either the left child of the left child of its grandparent, or the right child of the right child of its grandparent.

**Definition 2** _Let T be a binary tree, and_ \(x\in T\) _not the root node. We will define the_ like-minded child of _x, to be denoted by_ \(\lambda(x)\)_, to be:_

\(\lambda(x)=\left\{\begin{array}{ c c }
l(x), & \text{\textit{if}}x=l(\pi(x)); \\
r(x) & \text{\textit{if}}x=r(\pi(x)).
\end{array}\right.\)

Many algorithms manipulate binary trees via what are known as _rotations_. As an example, if _T_ is of the form shown in Figure 2, where each of _c_, _d_ and _e_<tbc>

22
binary splay treap weighted balanced optimal
20
18
16
14
mean cost
12
10
8
6
4
2
100
1000
10000
100000
1x106
1x107
tree size

Fig. 1: Baseline performance

