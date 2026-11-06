## A.2 The Parallel Algorithm by Larmore et al. [72]

Here we focus on the first phase on how to construct the _l_-tree in parallel. Larmore et al. observe that we can pick any locally minimal pair instead of the left-most one as in Garsia-Wachs, which does not affect the resulting _l_-tree. Hence, we can in parallel process all possible locally minimal pairs in one round. However, in the worst case the number of rounds is still linear. For example, if _a_<sub>1_..n_</sub> is in increasing order, then only one locally minimal pair can be processed in one round.

To overcome this issue, Larmore et al. further proposed the concept of "valleys". A valley \(\alpha=\mathit{vall}(a_i)\) is the _largest_ contiguous subsegment of _a_ that 1) contains _a<sub>i</sub>_, and 2) contains no item larger than _a<sub>i</sub>_. Hence, _a<sub>i</sub>_’s valley contains the elements from _a<sub>i</sub>_’s subtree in the Cartesian tree of _a_. Larmore et al. showed that several disjoint valleys in the sequence can be processed in parallel. To understand this, let us consider a valley \(\alpha\). Let \(\Delta_\alpha\) be the parent of valley \(\alpha\) in the Cartesian tree. Since \(\alpha\) is maximal, the locally minimal pairs from this range will not interact with the outside elements. Hence, we can consider valley \(\alpha\) as an independent task, and repeatedly find and combine the locally minimal pairs inside \(\alpha\). The only difference is that if the combined element \(x=a_i+a_{i+1}>\Delta_\alpha\), we mark it as _x_<sup>∗</sup> and put it in a separate queue. After the parallel processing of disjoint valleys, we collect all marked elements and insert them into the right place.

In total, there can be at most _n_ overlapping valleys. Larmore et al.’s algorithm uses one special type of valley: the 1-valleys. A 1-valley is defined to be a valley \(\alpha\) such that for any node _v_ in the subtree of \(\alpha\) in the Cartesian tree, if _v_ has two children, at least one of the children is a leaf. We can see that in the sequence the maximal 1-valleys are not overlapping, so we can process them in parallel. They also proved that, in each round if we process all maximal 1-valleys and reinsert them as in the sequential order, the number of maximal 1-valleys in the remaining sequence decreases by at least a half. Thus, the whole algorithm will finish in _O_(log_n_) rounds.

Before we show how to process a 1-valley, we introduce some definitions. Let _p(u_) is the parent of _u_ in the Cartesian tree of \(\alpha\). We define a 1-valley \(\alpha\) to be a regular valley if for _u\<v_ are two leaves in the Cartesian tree of \(\alpha\), then _p(u)\<p(v_). A sorted regular valley is defined as a regular valley with the minimum element in the first one. Larmore et al. showed that a 1-valley can be transformed to a sorted regular valley in _O(m_) work and _O_(log_m_) span, where _m_ is the size of this 1-valley. A set of items _S_ is defined to be lf-closed (short for leaf-father-closed) if for any \(a_i\in S\) and _a<sub>i</sub>_ is a leaf in the Cartesian tree of \(\alpha\), then _p(a<sub>i</sub>_) is also in _S_. The weight of _S_ is defined as the sum of the weights of all items in it. We define _W<sub>k</sub>_ as the minimum weighted lf-closed set with _k_ items in it. Larmore et al. showed that all _W<sub>k</sub>_ can be computed in _O(m_log_m_) work and _O_(log_m_) span.

Now consider a sorted regular valley \(\alpha\) with length _m_. Our goal is to generate a sequence of forests \(forest_{0..m^\prime-1}(m'<m)\) so that each of them corresponds to a subset of subtrees in the _l_-tree. Here _forest_<sub>0</sub> is empty. The last forest _forest_<sub>_m_-1</sub>, if \(m=m'\), corresponds to the _l_-tree if we merge all elements in this valley. However, this process may not end here--as mentioned above, we will stop if the<tbc>

<tbc>weights of subtrees exceed \(\Delta_\alpha\). Hence, we can have our final state \(forest_{m^\prime-1}\) with \(m'<m\). To compute _forest<sub>i</sub>_, we will enumerate all _forest<sub>j</sub>_ for _j\<i_, and find the best (minimum) transition from them. Here a transition means to build an additional level in the _l_-tree, and the cost _w(j,i)=W_<sub>2_i-j_</sub>. Larmore et al. showed that the cost function _w_ is convex, so computing _forest<sub>i</sub>_ is exactly a convex GLWS problem. If we use Alg. 1 to solve this convex GLWS problem, since each decision _best[i_]=_j_ will add another level to the trees in _forest<sub>i</sub>_ from _forest<sub>j</sub>_, the effective depth is upper bounded by the overall _l_-tree height _h_. Hence, the work and span for each 1-valley subproblem is _O(m_log_m_) work and _O(h_log<sup>2</sup>_m_) span, where _m_ is the subproblem size. Since the total size of 1-valleys in a recursive round is _O(n_), the work and span for one round are _O(n_log_n_) work and _O(h_log<sup>2</sup>_n_), respectively. Multiplying this by _O_(log_n_), the number of recursive rounds, gives the cost bounds in Thm. 5.1.

## A.3 Proof of Lemma 5.1

Here we provide the proof of Lemma 5.1. We first show the following lemma.

Lemma A.1. _Let the weight of a subtree in an OAT as the total weight of all leaves in this subtree. In an OAT, the subtree weight grows by at least twice for every three levels._

_Proof._ Here we denote _p(v_) as the parent node of _v_ in the output OAT _T_ and _w(v_) as the sum of the leaf weights in the subtree of node _v_. We will show for any node _a_ in the OAT, the great-grandfather of _a_ (if exists) must have weight no less than 2_w(a_). In the optimal alphabetic tree _T_, let node _b_ be _a_’s sibling and node _c_ be _a_’s parent. WLOG we assume node _a_ is the left child of node _c_. Then, let _d_ be _c_’s sibling, _e_ as _c_’s parent, and _f_ as _e_’s parent. Now the lemma is equivalent to \(w(f)\ge 2w(a)\).

We consider the first case when _c_ is _e_’s left child (case 1 in Fig. 8). In this case, we must have \(w(d)\ge w(a)\), since otherwise a right rotation will decrement the total cost of the tree by _w(d_)-_w(a_), violating that _T_ is an OAT. Hence, \(w(f)\ge w(e)\ge w(d)+w(a)\ge 2w(a)\) in this case.

The second case is when _c_ is _e_’s right child. There are two subcases. First, if _e_ is _f_’s right child (case 2(a) in Fig. 8), then _c_, _e_, and _f_ form another case 1. Hence, we have \(w(f)\ge 2w(c)\ge 2w(a)\). Second, if _e_ is _f_’s left child (see _T_<sub>4</sub> in case 2(b) in Fig. 8). We can double-rotate and get another valid alphabetic tree _T_<sub>5</sub>. As _T_<sub>4</sub> is the optimal alphabetic tree, we must have \(2w(d)+3w(a)+3w(b)+w(g)\le 2(w(d)+w(a)+w(b)+w(g))\), which leads to \(w(g)\ge w(a)+w(b)\). So \(w(f)=w(d)+w(a)+w(b)+w(g)\ge w(a)+w(g)\ge 2w(a)\).

From all three cases above, we show \(w(f)\ge 2w(a)\), which proves the lemma that the weight doubles for every three steps up the OAT. \(\sqcap\sqcup\)

T1
T2
f
T3
T4
f
T5
e
e
e
g
C
d
a
d
C
d
C
a
b
b
d
d
a
b
g
a
b
a
b
Case 1
Case 2(a)
Case 2(b)

**Figure 8:** Illustrations for analyzing the OAT Height. The three cases are used in the proof of Lemma A.1.

