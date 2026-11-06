implement the split/join operations in the preferred paths of Tango trees) whereas the (properly implemented) Tango tree of [16] is oblivious to the parameter.

Consider any fixed access sequence \(X=(X_1,\dots,X_m)\in S^m\). W.l.o.g. assume _n_=|_S_| is a power of 2, and we associate each key in _S_ with an integer in [_n_]. In this section, we will consider a fixed parameter _k_ that is an integer in [1,log_n_].

\(\blacktriangleright\) **Definition 28** (perfect binary tree and subtrees)**.** _Let_ T _denote the perfect binary tree on_ [_n]._<sup>13</sup> _For each key_ \(x\in[n]\)_, define h<sub>x</sub> to be the depth of the node x in_ T _(root has depth_ 1_). Divide the tree_ T _into_ log_n/k levels such that the subtrees on each level have height k. For each key_ \(x\in[n]\)_, consider the path from the root to the node x, and we denote the subtrees encountered along this path as_ \(\mathcal{T}_1^{(x)},\cdots,\mathcal{T}_{\lceil h_x/k\rceil}^{(x)}\).

Note that each tree \(\mathcal{T}_\ell^{(x)}\) has height _k_.

\(\blacktriangleright\) **Definition 29** (preferred child and preferred path [15])**.** _At any time i, for any node x in_ T _, we define its preferred child to be the left (or right) child if the last access to a node within x’s subtree was in the left (or right) subtree of x. Each subtree of_ T _can be decomposed into disjoint sets of preferred paths by recursively following the preferred child._

\(\blacktriangleright\) **Definition 30** (number of changed preferred children)**.** _At any time i, and for any_ \(\ell\in[\lceil h_{X_i}/k\rceil]\)_, define_ \(a_\ell^{(X_i)}\) _to be the number of nodes in_ \(\mathcal{T}_\ell^{(X_i)}\) _whose preferred child changes during access of X<sub>i</sub>. Define_ \(a^{(X_i)}=\sum_{\ell=1}^{\lceil h_{X_i}/k\rceil} a_\ell^{(X_i)}\) _to be the number of all nodes in the whole tree whose preferred child changes during access of X<sub>i</sub>._

By the definition of the alternation bound in Definition 13, we directly have the following lemma.

\(\blacktriangleright\) **Lemma 31** (alternation bound)**.** Alt\(_\mathcal{T}(X)=\sum_{i=1}^ma^{(X_i)}\).

Similar to the original tango tree in [15], we maintain each preferred path as an auxiliary tree. Since we define a preferred path to be a path _within a subtree_, in the auxiliary tree we store the depth of a node _with respect to that subtree_ instead of its depth with respect to the whole tree T . We use the following result from [15]:

\(\blacktriangleright\) **Lemma 32** (auxiliary tree, Section 3.2 of [15])**.** _The auxiliary tree data structure is an augmented BST that stores a preferred path and supports "search", "cut by depth", and "join" operations. Each operation takes O_(log_p_+1) _time, where p is the total number of nodes in the preferred path._

**Algorithm.**

Now we are ready to describe our algorithm. Our data structure is an augmented BST that consists of all the auxiliary trees of all the preferred paths.

When accessing _X<sub>i</sub>_, the algorithm follows the BST until it reaches _X<sub>i</sub>_. Whenever a preferred child is changed, we use the "cut by depth", and "join" operations to change the auxiliary trees accordingly.

<sup>13</sup> Since each node of T uniquely stores a key in [_n_], with an abuse of notation, we will use _x_ to denote both a key in [_n_] and a node in the tree T.

