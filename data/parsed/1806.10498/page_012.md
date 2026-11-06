<tbc>exceed _k_<sub>0</sub>+1 and \(v'\) is a 1-node. If \(v'\) exists, we recursively call the procedure \(\mathrm{Consolidate}(v,v')\) (respectively \((\mathrm{Consolidate}(v',v))\). There is at most one recursive call of our procedure per tree level. Our procedure shifts _O(k_<sub>0</sub>) nodes by one position to the right and recursively calls itself on some higher tree level; every time when some node in _T_<sup>s</sup> is shifted, we may have to move some leaf \(\varepsilon_i\) of _T_. Hence the total time of \(\mathrm{Consolidate}(u,u')\) is _O(k_<sub>0</sub>log<sup>2</sup>_n_)=_O_(log<sup>3</sup>_n_).

**Lemma 6** _We can implement a binary search tree so that access to an element and an insertion of a new element are supported in O_(log<sup>2</sup>_n_) _time. If an element e<sub>i</sub> was accessed w<sub>i</sub> times over a sequence of W operations, then the depth of the leaf holding e<sub>i</sub> does not exceed_ min(log(_W/w<sub>i</sub>),_log_n_)+_O_(1).

## 7.1 Fast Updates

Now we show how the data structure from Section 6 can be changed to support updates in worst- case time. As in Section 6 the tree _T_<sup>s</sup> is divided into the macro-tree and mini-trees. Each mini-tree contains _O_(log<sup>3</sup>_n_) pseudo-leaves.

A new pseudo-leaf is inserted into a mini-tree; the cost of an insertion is _O_((loglog_n_)<sup>2</sup>) time by Lemma 6. We run an additional background process that maintains the sizes of mini-trees. During each iteration we identify the largest mini-tree _T<sub>l</sub>_ among all subtrees of size at least (7/4)log<sup>3</sup>_n_. We split _T<sub>l</sub>_ into two mini-trees of almost-equal size. We also identify the smallest mini-tree _T<sub>k</sub>_ of size at most (3/4)log<sup>3</sup>_n_; we merge _T<sub>k</sub>_ with one of its direct neighbors (i.e., with the mini-tree immediately to the left or immediately to the right of _T<sub>k</sub>_). If the resulting mini-tree is larger than , then we split it into two almost-equal parts. We will show in Section 8.3 how a mini-tree can be split into two almost-equal parts or merged with another mini-tree in less than _O_(log<sup>2</sup>_n_) time. When we split or merge two mini-trees, we also have to perform _O_(1) updates on the macro-tree. The cost of updates is _O_(log<sup>2</sup>_n_), hence each iteration takes _O_(log<sup>2</sup>_n_(loglog_n_)<sup>2</sup>) time. By Theorem 5 from \[10\], we can organize our background process so that each mini-tree has no more than 2log<sup>3</sup>_n_ and no less than log<sup>3</sup>_n/_2 pseudo-leaves.

**Lemma 7** _We can implement a binary search tree so that access to an element and an insertion of a new element are supported in O_((loglog_n_)<sup>2</sup>) _amortized time. If an element e<sub>i</sub> was accessed w<sub>i</sub> times over a sequence of W operations, then the depth of the leaf holding e<sub>i</sub> does not exceed_ min(log(_W/w<sub>i</sub>),_log_n_)+_O_(1).

We can recursively apply Lemma 7 in the same way as described in Section 6. To obtain the main<tbc>

v
u
u1
u2
u3
u'
u1
u2
u3
u'

Figure 3: Example of procedure \(\mathrm{Consolidate}(u,u')\). Left: nodes _u_ and \(u'\) have one child. Right: node _u_ and its ancestors, up to a node _v_ that has two children, are removed. Children of _u_<sub>1</sub>, _u_<sub>2</sub>, _u_<sub>3</sub> are shifted one position to the right. Only relevant nodes and their children are shown.

