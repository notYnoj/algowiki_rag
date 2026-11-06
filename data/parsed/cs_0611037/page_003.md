<tbc>Sample representations are shown in Fig. 2 and Fig. 3, the former being labeled with the values of _b<sub>j</sub>(i_). Again, to emphasize the total cost in this pictorial representation, edges are portrayed with depth proportional to their cost. The cost (and thus depth) of leaf 3 in Fig. 2 is, for example,

\(\sum_jc_{b_j(3)}=c_{b_1(3)}+c_{b_2(3)}+c_{b_3(3)}\)<br>
\(=c_1+c_1+c_0=1+1+3=5.\)

I gives the context for this branching problem among other binary tree optimization problems. These other problems are referred to as in the survey paper \[18\]. In most problem formulations, edge cost is fixed, and, where it is not fixed, edges generally have costs according to their order, i.e., a left edge has cost _c_<sub>0</sub> and a right edge has cost _c_<sub>1</sub>. Relaxing this edge-order constraint in the unequal-cost alphabetic problem results in the branching problem we are now considering. Relaxing the alphabetic constraint from either the original alphabetic problem or the branching problem leads to Karp’s nonalphabetic problem; since output items in Karp’s problem need not be in a given (e.g., alphabetical) order, the tree optimal for the ordered-edge nonalphabetic problem is also optimal for the unordered-edge nonalphabetic problem.

Thus the cost _T_<sup>Karp</sup> for the optimal tree under Karp’s formulation -- also called the _lopsided tree problem_ -- is a lower bound on the cost of the optimal branch tree, whereas the cost _T_<sup>ltai</sup> for the optimal tree under Itai’s (alphabetic) formulation is an upper bound on the cost of the optimal branch tree. This enables the use of bounds in \[19\] -- including the lower bound originally formulated in \[20\] -- for the branching problem. Specifically, if _b_<sup>opt</sup> is the optimal branching function and _T_<sup>opt</sup>=_T<sub>p,c</sub>(b_<sup>opt</sup>) the associated cost for the optimal tree, then

\(\frac{H(p)}{d}_{\le^{\left[20\right]}}T^\mathrm{Karp}\le T^\mathrm{opt}\le T^\mathrm{ltai}_{\le^{\left[19\right]}}\frac{H(p)+1}{d}+\mathrm{max}\left\{c_0,c_1\right\}\)

where _H_ is the entropy function \(H(p)=-\sum_ip(i)\mathrm{log}_2p(i)\) and _d_ satisfies 2<sup>-_dc_<sub>0</sub></sup>+2<sup>-_dc_<sub>1</sub></sup>=1. If \(\rho=c_0/c_1\) and _x_ is the sole positive root of \(x^\rho+x-1=0\), then \(d=-c_1^{-1}\mathrm{log}_2x\).<tbc>

<tbc>Thus, for example, when _c_=(31),<tbc>

\(x=\sqrt{\frac{1}{2}+\sqrt{\frac{31}{108}}}-\sqrt{\frac{3}{2}+\sqrt{\frac{31}{108}}}\)

<tbc>so _d_=log<sub>2</sub>_x_<sup>-1</sup>≈0.5515 and

\(T^\mathrm{opt}\in[(1.813\dots)H(p),(1.813\dots)H(p)+4.813\dots].\)

When _c_=(21), \(x=1/\phi\) so \(d=\mathrm{log}_2\phi\), where \(\phi\) is the golden ratio, \(\phi=(\sqrt{5}+1)/2\). These bounds can be used to estimate optimal performance and determine whether or not to use a decision tree when it is one of multiple implementation choices.

The key to constructing an optimizing algorithm is to note that any optimal branching tree must have all its subtrees optimal; otherwise one could substitute an optimal subtree for a suboptimal subtree, resulting in a strict improvement in the result. The branching problem is thus, to use the terminology of \[26\], _subtree optimal_. Each tree (and subtree) can be defined by its _splitting points_. A splitting point _s_ for the root of the tree means that all items (grades) after _s_ and including _s_ will be in the right subtree while all items before _s_ will be in the left subtree, as per the convention in \[7\], \[10\], \[21\]. Since there are _n_-1 possible splitting points for the root, if we know all potential optimal subtrees for all possible ranges, the splitting point can be found through sequential search of the possible combinations. The optimal tree is thus found through dynamic programming, and this algorithm has _O(n_<sup>3</sup>) time complexity and _O(n_<sup>2</sup>) space complexity, in a similar manner to \[21\].

The dynamic programming algorithm is relatively straightforward. Each possible optimal subtree for items _i_ through _j_ has an associated cost, _c(i,j_) and an associated probability _p(i,j_); at the end, _p_(1_,n_)=1 and _c_(1_,n_) is the expected cost (run time) of the optimal tree.

The base case and recurrence relation we use are similar to those of \[12\]. Given unequal branch costs _c_<sub>0</sub> and _c_<sub>1</sub> and probability mass function \(p(\cdot)\) for 1 through _n_,

\(c(i,i)=0\)<br>
\(c'(i,j)=\mathrm{min}_{s\in(i,j]}\{c_0p(i,s-1)+c_1p(s,j)+\)<br>
\(c(i,s-1)+c(s,j)\}\)<br>
\(c''(i,j)=\mathrm{min}_{s\in(i,j]}\{c_1p(i,s-1)+c_0p(s,j)+\)<br>
\(c(i,s-1)+c(s,j)\}\) (1)

\begin{tabular}{ccc}
Given & _p_=(_p_(1)_p_(2)_...p(n_)), _p(i)\>_0, \\
 & \(\sum_ip(i)=1\); & \\
 & \(c_0,c_1\in\mathbb{R}_+\) such that \(c_0\ge c_1\). & \\
find & _B_, a full binary tree; & \\
 & _b_, an assignment of costs to edges of _B_ such that each nonleaf is connected to its children by edges, one with cost _c_<sub>0</sub>, and the other with cost _c_<sub>1</sub>. & \\
minimizing & \(T_{p,c}(b)\unknown\sum_{i=1}^np(i)\sum_{j=1}^{l(i)}c_{b_j(i)}\) & \\
where & the _j_th edge along the path from root to _i_th leaf is assigned cost _c_<sub>_b<sub>j</sub>(i_)</sub>; & \\
 & the number of edges on the path from root to _i_th leaf is _l(i_). & \\
\end{tabular}

\begin{tabular}{cccc}
 & \multicolumn{3}{c}{_edge cost/order restriction_} \\
_alphabetic?_ & Constant cost & Ordered & Unrestricted \\
**Yes** & Hu-Tucker \[8\]-\[10\], \[21\] & Itai \[12\], \[13\] & branching problem (static) \\
**No** & Huffman \[22\] & \multicolumn{2}{c}{Karp \[23\]-\[25\]} \\
\end{tabular}

TABLE I

TYPES OF DECISION TREE PROBLEMS

