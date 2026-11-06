\(-\phi_m(-log_2\phi_m+2-\lceil-log_2\phi_m\rceil)\)<br> \(+\sum_{i:\phi_i>0}\phi_i(-log_2\phi_i+2)\)<br> \(=-\sum_{i:\phi_i>0}\phi_ilog_2\phi_i+2\)<br> \(-\phi_1(-log_2\phi_1+2-\lceil-log_2\phi_1\rceil)\)<br> \(-\phi_m(-log_2\phi_m+2-\lceil-log_2\phi_m\rceil)\)<br> \(=H(\phi)+2-\phi_1(2-log_2\phi_1-\lceil-log_2\phi_1\rceil)\)<br> \(-\phi_m(2-log_2\phi_m-\lceil-log_2\phi_m\rceil).\) (26)

We now eliminate the _m_-1 leaves associated with the _additional null_ probabilities in \(\nu\), proceeding similarly to [4], [5]. First, observe that the leaves associated with the probabilities \(\nu_i\) appear, from left to right, in the same order as the probabilities \(\nu_i\) (this is due to the fact that the tree represents an alphabetic code). Moreover, observe that the binary tree of the code \(C'\) is full by construction, i.e., each node has exactly zero or two children. When we prune a leaf _x_ associated with an additional null probability, we bring up one level the whole sub-tree _T_ whose root _r_ is the sibling of _x_. The tree _T_ contains either the leaf associated with a probability in \(\nu\) that immediately follows the additional null probability associated with _x_, or it contains the leaf associated to a probability in \(\nu\) that immediately precedes _x_. Hence, if _x_ is the "left" child of _a_, its pruning causes a bump up of one level of the leaf that follows _x_, and if _x_ is the "right" child of _a_, it causes a bump up of one level of the leaf that precedes _x_. Figure 2 explains the procedure pictorially.

Hence, the elimination of each leaf _x_ associated with an additional null probability in \(\nu\) bumps up one level at least

one leaf among the two leaves that precede and follow _x_. In total, we bump up leaves whose total probability is at least

\(\sum_{i=1}^{m-1}min(\phi_i,\phi_{i+1}).\) (27)

We recall that the construction of the alphabetic code with average cost (26) requires linear time. Similarly, the elimination of the _m_-1 leaves associated with the additional _null_ probabilities in \(\nu\) requires linear time too, since it can be implemented through a simple tree visit.

Thus, from (26) and (27) we conclude that the new alphabetic code has a cost upper bounded by

\(H(\phi)+2-\phi_1\left(2-log_2\phi_1-\lceil-log_2\phi_1\rceil\right)\)<br> \(-\phi_m\left(2-log_2\phi_m-\lceil-log_2\phi_m\rceil\right)-\sum_{i=1}^{m-1}min(\phi_i,\phi_{i+1}).\)

Let us now consider the case where \(\phi_1\) and \(\phi_m\) can be zero.

**Theorem 4.** _For any non-dyadic probability distribution_ \(\phi=(\phi_1,\dots,\phi_m)\) _on the symbols_ \(s_1\prec\cdots\prec s_m\)_, we can construct in linear time an alphabetic code C with_

\(\mathbb{E}[C]\le H(\phi)+2-\phi_\ell\left(2-log_2\phi_\ell-\lceil-log_2\phi_\ell\rceil\right)\)<br> \(-\phi_k\left(2-log_2\phi_k-\lceil-log_2\phi_k\rceil\right)\)<br> \(-\sum_{i=\ell}^{k-1}min(\phi_i,\phi_{i+1})+\phi_\ell+\phi_k\)<br> \(=H(\phi)+2-\phi_\ell\left(1-log_2\phi_\ell-\lceil-log_2\phi_\ell\rceil\right)\)<br> \(-\phi_k\left(1-log_2\phi_k-\lceil-log_2\phi_k\rceil\right)-\sum_{i=\ell}^{k-1}min(\phi_i,\phi_{i+1}),\) (28)

_where_ \(\ell=argmin_i\{\phi_i>0\}\) _and_ \(k=argmax_i\{\phi_i>0\}\).

_Proof._ Let \(\phi'=(\phi_\ell,\dots,\phi_k)\) be the probability distribution obtained by considering only the elements of \(\phi\) between \(\phi_\ell\) and \(\phi_k\). From Theorem 3, we know that we can construct in linear time an alphabetic code \(C'\) for \(\phi'\) with

\(\mathbb{E}[C']\le H(\phi')+2-\phi_\ell\left(2-log_2\phi_\ell-\lceil-log_2\phi_\ell\rceil\right)\)<br> \(-\phi_k\left(2-log_2\phi_k-\lceil-log_2\phi_k\rceil\right)-\sum_{i=\ell}^{k-1}min(\phi_i,\phi_{i+1}).\) (29)

We need to address four cases:

1) \(\ell=1\) and _k=m_: in this case \(\phi=\phi'\) and the result follows from Theorem 3.<tbc>

2) \(\ell>1\) and _k\<m_: then \(\phi=(0,\dots,0,\phi_\ell,\dots,\phi_k,0,\dots,0)\) and we have to create the leaves to allocate the symbols \(s_1,\dots,s_{\ell-1}\) and _s_<sub>_k_+1</sub>_,...,s<sub>n</sub>_. To do so, we let the leaves associated to \(s_\ell\) and _s<sub>k</sub>_ descend by one level and we insert the subtrees _T_ and \(T'\) with leaves \(s_1,\dots,s_{\ell-1}\) and _s_<sub>_k_+1</sub>_,...,s<sub>n</sub>_, respectively, as shown in Figure 3.<tbc>

a
r
T
T
a
r
T
T

Figure 2. The figure shows the two cases discussed above: the elimination of _x_ bumps up of one level the leaf that precedes it (above), and the leaf that follows it (below).

