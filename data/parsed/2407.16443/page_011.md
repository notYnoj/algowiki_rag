Let \(\ell_1=\lceil-log_2\phi_1\rceil\) and \(\ell_2=\lceil-log_2\phi_2\rceil+1\) be the lengths of the codewords associated to symbols _s_<sub>1</sub> and _s_<sub>2</sub>, according to (25). When the level of the codeword associated to _s_<sub>1</sub> exceeds the level of the codeword of _s_<sub>2</sub> by _more each_ of these additional levels, there would have been an internal node having only one child in the tree representation of the code. However, these nodes are removed since the intermediate code \(C'\) constructed through Lemma 2 is full in its tree representation. The elimination of such nodes bumps up the symbol _s_<sub>1</sub>, since the nodes would have been on the path from the lowest common ancestor of _s_<sub>1</sub> and _s_<sub>2</sub> to _s_<sub>1</sub>. Thus, when \(\ell_1-\ell_2-1>0\) we can bump up \(\phi_1\) of at least \(\ell_1-\ell_2-1\) additional levels. This gives the \(-\phi_1max(0,\lceil-log_2\phi_1\rceil-\lceil-log_2\phi_2\rceil-2)\) term of the bound.

A similar reasoning can be made with _s<sub>m</sub>_ and _s_<sub>_m_-1</sub>, where \(\ell_m=\lceil-log_2\phi_m\rceil\) and \(\ell_{m-1}=\lceil-log_2\phi_{m-1}\rceil+1\). Note that such a reasoning cannot be applied to the other pairs of probabilities, since the knowledge of the codeword lengths alone is not sufficient to understand which of the symbols will be bumped up. We have to look at the whole codewords set to have enough information.

The bound (36) can be extended to dyadic probability distributions proceeding as in Corollary 4.1.

## V. ON BINARY SEARCH TREES

In this section, we exploit the results on alphabetic codes we have derived in Section IV to provide new bounds on the average cost of optimal binary search trees. We recall that Knuth’s algorithm \[17\] to construct an optimum binary search tree has quadratic time and space complexity; here we provide a linear-time algorithm and give upper bounds on the cost of the trees our algorithm produces. It is clear that our upper bounds apply to optimal trees as well; we will also see that our bounds improve on the best previous results. Since our algorithms to construct almost-optimal search trees take in input almost-optimal alphabetic trees, in order to get linear time complexity it is essential that we can construct almost- optimal alphabetic trees in linear time as well. This is one of the main reasons why we have stressed this feature of the algorithms presented in Section IV.

We start this section by amending the analysis of the algorithm presented by De Prisco and De Santis \[5\] (actually, our presentation is slightly more general than that of \[5\]).

**Theorem 5.** _Let_ \(\sigma=(\sigma_1,\dots,\sigma_{2n+1})=(p_0,q_1,p_1,\dots,q_n,p_n)\) _be a probability distribution that contains the probabilities q_<sub>1</sub>_,...,q<sub>n</sub> and p_<sub>0</sub>_,...,p<sub>n</sub> for successful and unsuccessful searches, respectively, on an ordered sequence_ \(x_1\prec\cdots\prec x_n\)_. Let C be any alphabetic code for_ \(\sigma\)_, of average length_ E\[_C_\]_. Then, one can construct in linear time a binary search tree T for_ \(\sigma\) _of cost_

\(\mathbb{E}[T]\le\mathbb{E}[C]-\sum_{i=1}^nq_i-\sum_{i=0}^{n-1}min(p_i,p_{i+1}).\) (36)

_Proof._ Let us start from the binary tree _B_ corresponding to the alphabetic code _C_. The tree _B_ has 2_n_+1 leaves,<tbc>

<tbc>that we identify with the ordered sequence of probabilities _p_<sub>0</sub>_,q_<sub>1</sub>_,p_<sub>1</sub>_,...,q<sub>n</sub>,p<sub>n</sub>_. We transform the leaves corresponding to the _q<sub>i</sub>_’s into _internal_ nodes. As in \[5\], we raise each _q<sub>i</sub>_ to the lowest common ancestor of _p_<sub>_i_-1</sub> and _p<sub>i</sub>_, which is at least two levels above _q<sub>i</sub>_. Hence, \(\ell(q_i)\), i.e. the number of nodes from the root to _q<sub>i</sub>_, decreases by at least of one unit, for each _i_. In addition, when we bring up _q<sub>i</sub>_ the whole sub-tree whose root is the sibling of _q<sub>i</sub>_ goes up by at least one level. Hence, at least one between _p_<sub>_i_-1</sub> and _p<sub>i</sub>_ goes up one level. <sup>2</sup> Figure 4 provides an example of the described process.

Therefore, in total we bump up leaves whose total probability is at least

\(\sum_{i=1}^nq_i+\sum_{i=0}^{n-1}min(p_i,p_{i+1}).\) (37)

Let us show that the tree _T_, constructed according to the above procedure, is a correct binary search tree for the distribution \(\sigma=(\sigma_1,\dots,\sigma_{2n+1})=(p_0,q_1,p_1,\dots,q_n,p_n)\).

To that purpose, let us observe that the search property holds in a binary tree if and only if its in-order visit gives the nodes

<sup>2</sup>The analysis of \[5\] is incorrect since it claims that all but only one probability goes up one level. One can see that this is not the case, as also observed by the authors of \[4\] and by \[19\].

P1 P3 Po q1 q2 P2 q3 (a) The initial alphabetic tree q1 Po P1 P3 q2 P2 q3 (b) The tree after transforming q1 into an internal node q2 q1 q3 Po P1 P2 P3 (c) The final binary search tree

Figure 4. Figure (a) shows the initial alphabetic tree; Figure (b) shows the tree after performing the first step; Figure (c) shows the tree after the application of the algorithm.

