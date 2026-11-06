_t_**-AKS-tree.** An _t_-AKS-tree is binary tree containing a total of _t_+1 levels numbered 0,1_,...,t_, respectively. Henceforth define \(M(t):=3\cdot 2^t-2\). All tree nodes receive either one or two labels from the range \[_M(t_)\]; further, each label is given to exactly one tree node. The labeling scheme satisfies the following constraints:

1. Each leaf receives one label from the range \[_M(t_)\]; and each non-leaf node receives two labels from the same range.<tbc>

2. For each internal node, every label in its right subtree is strictly greater than every label in its left subtree.<tbc>

3. The set of labels assigned to each subtree is a contiguous sub-range \([s,t]\subseteq[M(t)]\); and further, the minimum _s_ and maximum _t_ of the range are assigned to the root of the sub-tree.

One can check that the above set of constraints uniquely define the labeling on the tree nodes. In Figure 2, we give an example of a _t_-AKS-tree where _t_=3.

_t_**-AKS-intervals.** Given an array _A_ of length _n_, we can divide it into _M(t_) intervals called _t_-AKS- intervals, i.e., _A_:=_A_<sub>1</sub>||_A_<sub>2</sub>||_..._||_A_<sub>_M(t_)</sub>, where the length of each interval _A<sub>i</sub>_ depends on which level the label _i_ shows up in the _t_-AKS-tree. At a very high level, the length geometrically decreases by a factor of approximately \(\gamma:=16\) as the label _i_’s level becomes smaller.

We now define the lengths of each _t_-AKS-interval more formally, following the same approach as in the original AKS paper \[AKS83\]. We first define the following numbers for _t_=1,2_,...,_log_n_, and for \(\ell=1,2,\dots,t\):<tbc>

\(X_t(\ell):=\left\lfloor\frac{1}{2\gamma}\cdot n\cdot 2^{-t}\cdot\gamma^{\ell-t}\right\rfloor,Y_t(\ell):=\sum_{j=1}^\ell X_t(j)\)

<tbc>Let \(\ell\in[0,t-1]\) and \(j\in[1,2^\ell]\). Suppose that the _j_-th node at level \(\ell\) in the _t_-AKS-tree have the two labels _i_ and \(i'\). Then, the lengths of the two intervals _A<sub>i</sub>_ and \(A_{i^\prime}\) are defined as follows.

\(|A_i|:=\left\{\begin{array}{ c c }
X_t(\ell+1) & \text{if}j\text{is odd} \\
Y_t(\ell+1) & \text{o.w.}
\end{array}\right.\text{and}|A_{i^\prime}|:=X_t(\ell+1)+Y_t(\ell+1)-|A_i|\)

Finally, in the last level \(\ell=t\) in the _t_-AKS-tree, each node has only one label. Suppose that the _j_-th node’s label is _i_, then the length of the interval _A<sub>i</sub>_ is \(|A_i|:=n\cdot 2^{-t}-Y_t(t)\).

**Fact 3.1** (Group _t_-AKS-intervals into equally sized segments)**.** _As mentioned, assume that n_:=|_A_| _is a power of 2. Fix any non-leaf level_ \(\ell\in\{0,1,\dots,t-1\}\) _in a t-AKS-tree, we can partition A into_ \(2^\ell\) _equally sized segments as follows (where equally sized means that every segment contains the same number of elements):_

1. Initially, for every node _v_ in the _t_-AKS tree, L(_v_) is defined to be the set of the original labels of _v_. Specifically, for every non-leaf node _v_, L(_v_) has two labels, and for every leaf node _v_, L(_v_) has only one label.<tbc>

2. For level _i_=0 to \(\ell-1\), for every node _v_ in level _i_ of the _t_-AKS-tree,<tbc>

(a) let \(S\subseteq\mathcal{L}(v)\) be the subset of node _v_’s labels smaller than every label in L(_v_.LeftChild), and let \(S':=\mathcal{L}(v)\backslash S\).<tbc>

(b) let \(\mathcal{L}(v.\text{LeftChild}):=\mathcal{L}(v.\text{LeftChild})\cup S\);<tbc>

(c) let \(\mathcal{L}(v.\text{RightChild}):=\mathcal{L}(v.\text{RightChild})\cup S'\);<tbc>

