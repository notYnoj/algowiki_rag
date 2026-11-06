## 4.2 Construction of Noisy Binary Search Trees

Let _k_ be the smallest odd integer that satisfies \(k\ge 32\frac{1-p}{(1-2p)^2}\), and let _c_=250_k_. For the sake of simplicity, we assume that \(m=2cd\cdot 2^h\) where _h_ is a non-negative integer. At the end of this section, we argue that this assumption can be removed.

We start by partitioning the sequence _S_ of _m_ elements into \(2\cdot 2^h\) ordered _groups g_<sub>0</sub>_,g_<sub>1</sub>_,..._ where group _g<sub>i</sub>_ contains the elements in positions \(i\cdot cd+1,\dots,(i+1)cd\). Then, we further partition these \(2\cdot 2^h\) groups into two ordered sets _G_<sub>0</sub> and _G_<sub>1</sub>, where _G_<sub>0</sub> contains the groups _g<sub>i</sub>_ with even _i_, and _G_<sub>1</sub> the groups _g<sub>i</sub>_ with odd _i_. Notice that |_G_<sub>0</sub>|=|_G_<sub>1</sub>|=2_<sup>h</sup>_.

For each \(j\in\{0,1\}\), we define a _noisy binary search tree T<sub>j</sub>_ on _G<sub>j</sub>_. Let \(\eta=2+4\lceil log_7m\rceil\). The tree _T<sub>j</sub>_ is a binary tree of height \(h+\eta\) in which the first _h_+1 levels (i.e., those containing vertices at depths 0 to _h_) are complete and the last \(\eta\) levels consist of 2_<sup>h</sup>_ paths of \(\eta\) vertices, each emanating from a distinct vertex on the (_h_+1)-th level.

We index the leaves of _T<sub>j</sub>_ from 0 to 2_<sup>h</sup>_-1, we use _h(v_) to denote the depth of vertex _v_ in _T<sub>j</sub>_, and we refer to the vertices _v_ at depth \(h(v)\ge h\) as _path-vertices_. We also associate each vertex _v_ of _T<sub>j</sub>_ with one _interval I(v_), i.e., a set of contiguous positions, as follows: for a leaf _v_ with index _i_, _I(v_) consists of the positions in _g_<sub>2_i+j_</sub>, for a non-leaf path-vertex _v_ having _u_ as its only child, we set _I(v_)=_I(u_), and for an internal vertex _v_ having _u_ and _w_ as its left and right children, respectively, we define _I(v_) as the interval containing all the positions between min_I(u_) and max_I(w_) (inclusive).

Moreover, each vertex _v_ of _T<sub>j</sub>_ has a reference to two _shared pointers L(v_) and _R(v_) to positions in \(\{1,\dots,n\}\backslash\bigcup_{g_i\in S_j}g_i\). Intuitively, _L(v_) (resp. _R(v_)) will always point to the positions of _S_ occupied by elements that are _smaller_ (resp. _larger_) than all the elements _s<sub>i</sub>_ with \(i\in I(v)\). For each leaf _v_, _L(v_) initially points to min_I(v_)-_d_-1 while _R(v_) initially points to max_I(v_)+_d_. A non-leaf path-vertex _v_ shares both its pointers with the corresponding pointers of its only child, while a non-path vertex _v_ shares its left pointer _L(v_) with the left pointer of its left child, and its right pointer _R(v_) with the right pointer of its right child. See Figure 1 for an example.

We sometimes allow _L(v_) to point to positions smaller than 1 and _R(v_) to point to positions larger than _m_. We consider all the elements _s<sub>i</sub>_ with \(i\le 0\) (resp. _i\>m_) to be copies of a special \(-\infty\)<tbc>

r
u
L(u)
R(u)
v
h
w
n
- cd
-
go
g1
g2
g3
i*
Gn-1
I(u)
I(w)
I(v)
I(r)

Fig. 1. An example of the noisy tree _T_<sub>0</sub>. On the left side, the shared pointers \(L(\cdot)\) and \(R(\cdot)\) are shown. Notice how _L(r_) (and, in general, all the \(L(\cdot)\) pointers on the leftmost side of the tree) points to the special \(-\infty\) element. Good vertices are shown in black while bad vertices are white. Notice that, since \(i^*\in I(w)\), we have _T_<sup>∗</sup>=_T_<sub>0</sub> and hence all the depicted vertices are either good or bad.

