<tbc>The example in Figure 2, shows the segments for _t_=3 and level \(\ell=2\). In this case, if we partition _A_ into 4 equally sized segments, then the segments are:

\((A_1,A_2,\dots,A_6),(A_7,A_8,\dots,A_{11}),(A_{12},A_8,\dots,A_{16}),(A_{17},A_{18},\dots,A_{22}).\)

**Proof of Fact 3.1:** This fact is implicit in the AKS paper \[AKS83\], we prove it explicitly below. Alternatively, we can consider the following equivalent variant of the above algorithm: in Step 2, we do not stop at the end of the \((\ell-1)\)-th iteration, but continue all the way to level _t_-1. At this moment, for each node _v_ in level \(\ell\) of the tree: we group together the labels on all leaf nodes in Subtree(_v_) -- their corresponding _t_-AKS-intervals will form one segment.

It is not hard to show through induction that at the end of the iteration _i_=0 to _t_-1 in Step 2, each node _v_ in level _i_+1 of the _t_-AKS tree receives a set of labels from its parent which correspond to a total of _Y<sub>t</sub>(i_) elements. Therefore, at the end of iteration 0 to _t_-2, for each node _v_ in level _i_+1, its labels correspond to a total of consecutive _Y<sub>t</sub>(i_+1) elements. At the end of the final iteration _i=t_-1, each leaf node’s labels correspond to \(n\cdot 2^{-t}\) consecutive elements.

**Even and odd cherries.** In a binary tree, a _cherry_ is defined to be a parent node and its two children. The _even (or odd, resp.) cherries_ are those whose parents reside at an even (or odd, resp.) _level_.

Given _A_:=_A_<sub>1</sub>||_...||A_<sub>_M(t_)</sub> written as _t_-AKS-intervals, we define EvenCherries(_A_<sub>1</sub>||_...||A_<sub>_M(t_)</sub>) to be a set of _disjoint groups_ of _t_-AKS-intervals. Specifically, EvenCherries(_A_<sub>1</sub>||_...||A_<sub>_M(t_)</sub>) is of the form {_G_<sub>1</sub>_,G_<sub>2</sub>_,...,G<sub>d</sub>_} where _d_ is the number of even cherries in a _t_-AKS-tree, and for \(i\in[d]\), each group _G<sub>i</sub>_ corresponds to a distinct even cherry in a _t_-AKS-tree, i.e., _G<sub>i</sub>_ is one of the following two forms depending on whether the even cherry touches the leaf level:

• either _G<sub>i</sub>_:=_A_<sub>_j_<sub>1</sub></sub>||_...||A_<sub>_j_<sub>6</sub></sub> where _j_<sub>1</sub>_\<j_<sub>2</sub>_\<...\<j_<sub>6</sub>, and moreover, _j_<sub>1</sub>_,...,j_<sub>6</sub> correspond to the labels of an even cherry in the _t_-AKS-tree that does not involve the leaf level;<tbc>

• or _G<sub>i</sub>_:=_A_<sub>_j_<sub>1</sub></sub>||_...||A_<sub>_j_<sub>4</sub></sub> where _j_<sub>1</sub>_\<j_<sub>2</sub>_\<...\<j_<sub>4</sub>. and moreover, _j_<sub>1</sub>_,...,j_<sub>4</sub> correspond to the labels of an even cherry in the _t_-AKS-tree, involving the leaves this time.

The notation OddCherries is similarly defined but replacing "even" with "odd".

\(\epsilon\)**-near-sorter.** Let \(\epsilon\in(0,1)\) be a constant. An array _A_ of length _n_ is said to be \(\epsilon\)-near-sorted, iff the following holds for any \(1\le k\le n\):

1. \(A[1:k+\epsilon n]\) contains at least \((1-\epsilon)k\) of the _k_ smallest elements in _A_;<tbc>

2. \(A[n-k-\epsilon n+1:n]\) contains at least \((1-\epsilon)k\) of the _k_ largest elements in _A_.

In the above, we use the following notations to deal with boundary conditions: for _i\>n_, _A_\[1:_i_\]:=_A_\[1:_n_\]; and for _i\<_1, _A_\[_i:n_\]:=_A_\[1:_n_\].

An \(\epsilon\)-near-sorter (for _n_) is a circuit containing _O(n_) comparators and of constant depth (dependent on \(\epsilon\)) that permutes any input array of length _n_ into one that is \(\epsilon\)-near-sorted. Earlier works have shown how to construct such and \(\epsilon\)-near-sorter using expander graphs \[AKS83\].

## 3.3.2 Nearly Orderly Segmenter Construction

Our nearly orderly segmenter construction is described below:

3. For every node v in level \(\ell\) of the t-AKS-tree: all t-AKS-intervals whose corresponding labels are in Subtree(v) (including L(v)) are grouped together and called one segment, where Subtree(v) means the subtree rooted at v.

