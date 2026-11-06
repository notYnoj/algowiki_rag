<tbc>The dynamic programming algorithm, given the aforementioned considerations, is relatively straightforward. Each possible optimal subtree for items _i_ through _j_ has an associated cost, _c(i,j_) and an associated probability _p(i,j_); at the end, _p_(1_,n_)=1 and _c_(1_,n_) is the expected cost (run time) of the optimal tree.

The base case and recurrence relation we use are similar to those of \[25\]. Given unequal branch costs _c_<sub>1</sub> and _c_<sub>2</sub> and probability mass function \(p(\cdot)\) for 1 through _n_,

\(c(i,i)=0c'(i,j)=min_{s\in(i,j]}\{c_1p(i,s-1)+c_2p(s,j)+c(i,s-1)+c(s,j)\}c''(i,j)=min_{s\in(i,j]}\{c_2p(i,s-1)+c_1p(s,j)+c(i,s-1)+c(s,j)\}c(i,j)=min\{c'(i,j),c''(i,j)\}\text{(2)}\)

where \(p(i,j)=\sum_{k=i}^jp(i)\) can be calculated on the fly along with _c(i,j_). The last minimization determines which branch condition to use (e.g., \< vs. \(\ge\) or "assume taken" vs. "assume untaken"), while the minimizing value of _s_ is the splitting point for that subtree. The branch condition to use -- i.e., the bias of the branch -- must be coded explicitly or implicitly in the software derived from the tree.

Knuth \[27\] and Itai \[25\] also begin with such an algorithm, then go on to note that the splitting point of an optimal tree for their problems must be between the splitting points of the two (possible) optimal subtrees of size \(n'-1\), and use this fact to reduce complexity. The branching problem considered here, however, lacks this property. Consider _p_=(0.30.20.20.3) and _c_=(31), for which optimal trees split either at 2, as in Fig. 1, or at 4, the mirror image of this tree. In contrast, the two largest subtress, as illustrated in the figure and its mirror image, both have optimal split points at 3. Similarly, applying the less complex Hu-Tucker approach \[17\], \[19\] to this problem fails for _p_=(0.20.150.150.20.3) and _c_=(31).

The optimal tree of Fig. 1 is identical to the optimal tree returned by Itai’s algorithm for order-restricted edges \[25\]. Consider a larger example in which this is not so, the binomial distribution _p_=(1615201561)/128 with _c_=(112). If edge order is restricted as in \[25\], the tree at Fig. 2(a) is optimal, yielding an expected cost of 967/64=15.109375. If we relax the restriction, as in the problem under consideration here, the tree at Fig. 2(b) is optimal, yielding an expected cost of 831/64=12.984375, a 14% improvement.

The _O(n_<sup>3</sup>) complexity used to get this better result is generally not limiting. Although this restricts the range of problems solvable within a given time, most hard-coded search tree problems are small enough to be solved quickly. In addition, this model is not robust enough to model performance for large search trees, where some problems, such as the aforementioned grade-assignment problem, are actually better solved via alternative means when _n_ is large; a division and lookup table might be more suitable, for example, if there are dozens of different grades. This is not only due to the fact that search run time scales as _O_(log_n_), but also because large blocks of software code generally run more slowly due to insufficient instruction caching. If larger problems did need to be solved within this framework, space complexity would likely become an issue before time complexity anyway.

Given no information on \(p(\cdot)\), it is common to assume that _p(i_)=1_/n_. This is justified by noting that, if \(p(\cdot)\) is considered a random vector drawn from the probability simplex according to density _g_ -- as in \[7\] -- the expected cost for a given coding scheme is

\(E_p[T(b)]=E_p\left[\sum_{i=1}^np(i)\sum_{j=1}^{l(i)}c_{b_j(i)}\right]=\sum_{i=1}^nE_p[p(i)]\sum_{j=1}^{l(i)}c_{b_j(i)}\)

and, if _g_ is symmetric on the simplex, _E_\[_p(i_)\]=1_/n_ for any _i_. Since edge costs are not fixed, optimal trees for this uniform distribution need not be complete trees, that is, full trees for which all leaves have depth \(\lfloor log_2n\rfloor\) or \(\lceil log_2n\rceil\). For example, the tree in Fig. 1 is optimal for this uniform distribution with an average cost of 3.75, whereas the complete tree for _n_=4 results in an average cost of 4. This is thus a better approach to use for compilers that code switch (case) statements partially \[13\] or entirely \[34\] as decision trees.

ARM architectures such as those of the ARM7 and ARM9 families use no or static branch prediction \[5\]. Such processors are used for most mobile devices, including cell phones and iPods. Recent Pentium designs and the XScale \[24\] -- which is viewed as the successor to ARM architecture StrongARM -- use dynamic prediction, which we explore in the next section.

## III. MORE ADVANCED MODELS

With dynamic branch prediction, which in more advanced forms includes branch correlation, branches are predicted based on the results of prior instances of the same and<tbc>

\begin{tabular}{cccc}
 & \multicolumn{3}{c}{_Edge cost/order specification_} \\
_Output order restriction_ & **Constant cost** & **Order restricted** & **Order unrestricted** \\
**Alphabetic** & Hu-Tucker \[9\], \[10\], \[19\], \[30\] & Itai \[25\], \[35\] & branching problem \\
**Nonalphabetic** & Huffman \[22\], \[29\], \[38\] & \multicolumn{2}{c}{Karp \[6\], \[11\], \[26\]} \\
\end{tabular}

TABLE I

TYPES OF DECISION TREE PROBLEMS

