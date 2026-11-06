<tbc>be represented as a binary search tree, with an internal node associated to each element _x<sub>i</sub>_ and a leaf associated to each of the _n_+1 gaps \((-\infty,x_1),(x_1,x_2),\dots,(x_{n-1},x_n),(x_n,+\infty)\) among the _x<sub>i</sub>_’s. Let _x_ be an element that we want to seek for in the list. Each internal node represents a comparison operation between _x_ and the content _x<sub>i</sub>_ of the node. The outcome of the comparison can be either \(x\prec x_i\), _x=x<sub>i</sub>_ or \(x\succ x_i\) (see Section 6.2 of \[18\]). Thus, the internal nodes correspond to successful searches, and the leaves to the unsuccessful ones.

The cost of a binary search tree _T_ is defined as the average number of questions needed to identify an arbitrary input element _x_. More precisely, given a probability distribution \(\sigma=(\sigma_1,\dots,\sigma_{2n+1})=(p_0,q_1,p_2,\dots,q_n,p_n)\), where the probabilities of successful searches are _q_<sub>1</sub>_,...,q<sub>n</sub>_, and _p_<sub>0</sub>_,...,p<sub>n</sub>_ are the probabilities of unsuccessful searches, the cost of the binary search tree _T_, for the probability distribution \(\sigma\), is equal to

\(\mathbb{E}[T]=\sum_{i=1}^nq_i\ell(q_i)+\sum_{i=0}^np_i\ell(p_i),\) (1)

where \(\ell(q_i)\) denotes the level of _q<sub>i</sub>_ in the tree, i.e., the number of nodes from the root of _T_ to _q<sub>i</sub>_, whereas \(\ell(p_i)\) is the level of the parent of _p<sub>i</sub>_ in the tree \[18\]. We stipulate that the level of the root of _T_ is equal to 1.

Note that when the probabilities of successful searches, _q_<sub>1</sub>_,...,q<sub>n</sub>_, are all 0’s, the problem of finding an optimal binary search tree for the probability distribution \(\sigma\) is equivalent to the problem of finding an optimal alphabetic code for the probability distribution \(\phi=(p_0,\dots,p_n)\).

## III. OUR CONTRIBUTIONS IN PERSPECTIVE

Alphabetic codes have been extensively studied. In this section, we limit ourselves to discussing the work that is most closely related to our findings. We will present our results in Section IV and Section V.

In their classic paper \[9\], Gilbert and Moore designed a _O(m_<sup>3</sup>) time dynamic programming algorithm for the construction of optimal alphabetic codes (that is, of minimum average length), where _m_ is the number of symbols. Hu and Tucker \[13\] improved Gilbert and Moore’s result by providing an algorithm of time complexity _O(m_log_m_). Subsequent studies have mostly concentrated on the problem of giving linear time algorithms for the construction of almost optimal alphabetic codes and in providing explicit upper bounds on the average length of the constructed codes. It is clear that the derived bounds are upper bounds on the length of optimal alphabetic codes, as well.

Gilbert and Moore \[9\] gave a linear time algorithm to construct an alphabetic code for a set of symbols _S_, with associated probability distribution \(\phi\), whose average length is less than \(H(\phi)+2\). Here, \(H(\phi)=-\sum_{i=1}^m\phi_ilog\phi_i\) is the Shannon entropy of the distribution \(\phi\). Since the average length of any alphabetic code is lower bounded by \(H(\phi)\), one gets that Gilbert and Moore’s codes are at most two bits away from the optimum. We note that Gilbert and Moore’s upper bound cannot be improved, unless one has some additional information on the probability distribution \(\phi\). In fact, one<tbc>

<tbc>can see that the average length of the best alphabetical code for a set of three symbols \(s_1\prec s_2\prec s_3\), with probability distribution \(\phi=(\epsilon,1-2\epsilon,\epsilon)\), is equal to \(2-\epsilon\). On the other hand, \(H(\phi)\) can be arbitrarily small. Remarkably, the average length of the Huffman code for the same \(\phi=(\epsilon,1-2\epsilon,\epsilon)\) is equal to \(1+2\epsilon\), thus there can be a difference of (approximatively) 1 bit between the average length of the best alphabetical code and that of the Huffman code, for the same \(\phi\). The general characterization of the "shape" of worst-case probability distributions for alphabetical codes is given in the paper \[16\].

Horibe \[12\] provided a better upper bound than the \(H(\phi)+2\) bound of Gilbert and Moore, by giving an algorithm to construct alphabetic codes of average length less than

\(H(\phi)+2-(m+2)\phi_{min},\) (2)

where \(\phi_{min}\) is the smallest probability of \(\phi\).

Nakatsu \[25\] claimed a different upper bound on the minimum average length of alphabetical codes. Successively, Sheinwald \[28\] pointed out a gap in the analysis carried out in \[25\].

Yeung \[29\] also improved the \(H(\phi)+2\) bound of Gilbert and Moore, by proving the following upper bound on the average length _L_<sub>min</sub> of optimal binary alphabetic codes:

\(L_{min}\le H(\phi)+2-\phi_1\left(2-log\phi_1-\lceil-log\phi_1\rceil\right)\)<br>
\(-\phi_m\left(2-log\phi_m-\lceil-log\phi_m\rceil\right)\) (3)

\(\le H(\phi)+2-\phi_1-\phi_m,\) (4)

where \(\phi_1\) and \(\phi_m\) are the probabilities of the first and the last symbol of the ordered set of symbols _S_, respectively. In general, the bounds (2) and (3) are not comparable, in the sense that there are probability distributions \(\phi\) for which (2) is better than (3), and probability distributions \(\phi\) for which the opposite holds.

A new upper bound on the average length of optimal alphabetic codes was recently given by Dagan _et al._ \[4\]. Their bound claims that

\(L_{min}\le H(\phi)+2-\left(\phi_1+\phi_m+\sum_{i=1}^{m-1}min(\phi_i,\phi_{i+1})\right)\) (5)

\(=H(\phi)+1-\frac{\phi_1+\phi_m}{2}+\frac{1}{2}\sum_{i=1}^{m-1}|\phi_i-\phi_{i+1}|.\) (6)

While the upper bound (5) is correct, in Remark 1 (which will be given in Section IV) we point out an unresolved issue in the analysis given in \[4\] that leads to (5).

Our results for alphabetic codes consist of a series of improvements to the upper bound (5) of Dagan _et al._ on the average length of optimal alphabetic codes _L_<sub>min</sub>. For instance, we will prove that

\(L_{min}\le H(\phi)+2-\phi_1\left(2-log_2\phi_1-\lceil-log_2\phi_1\rceil\right)\)<br>
\(-\phi_m\left(2-log_2\phi_m-\lceil-log_2\phi_m\rceil\right)\)<br>
\(-\sum_{i=1}^{m-1}min(\phi_i,\phi_{i+1}).\) (7)

