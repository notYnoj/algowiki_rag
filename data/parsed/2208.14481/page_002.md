<tbc>finding a tree structure _T_ for which the cost

\(c(T)=\sum_{x\in T}p(x)d(x)\)

is minimized, where _T_ is the set of all nodes in some particular tree and _c(T_) is the expected cost of a single lookup in the tree.

A variety of authors have considered this problem, and two approaches have historically been taken. Some researchers have focused on finding a globally optimal tree, while others have focused on methods that construct approximately optimal trees. As one might expect, the complexity of the approximate methods is lower than their exact counterparts. Knuth [10] provides a reasonable summary with focus on the construction of globally optimal trees, while Nagaraj [14] provides a somewhat broader description.

Finding a globally optimal tree in general takes time _O(n_<sup>2</sup>), prohibitive given the size of modern search trees. There are two possible improvements:

1. Karpinski et.al. [8] have developed an _O(n_<sup>1.6</sup>) algorithm if there is a fixed lower bound on the relative probability of any particular node in the sense that there is some fixed \(\delta\) such that if {_v_<sub>1</sub>_,...,v<sub>n</sub>_} is an ordering of the values in the tree, then the probability that a query is between _v_<sub>_i_-1</sub> and _v_<sub>_i_+1</sub> is always at least \(\delta/n\). This assumption of relative uniformity among the weights of the nodes is unlikely to be valid in practice because of Zipf’s law [18, and Section 2] and the fact that the harmonic sequence \(\sum_{i=1}^n\frac{1}{i}\) diverges. In any event, _n_<sup>1.6</sup> is itself unlikely to be viable for large trees.<tbc>

2. Garsia and Wachs [6] and many successors [7,9,13, and others] have considered _O(n_log_n_) algorithms in the special case where it is known that the element _v_ being searched for is not in fact in the tree in question, and the goal is therefore to find two consecutive existing values _v<sub>i</sub>,v_<sub>_i_+1</sub> with _v<sub>i</sub>\<v\<v_<sub>_i_+1</sub>. It is perhaps not surprising that the complexity is lower in this case, since the placement of the internal nodes is less important if the search must proceed to the fringe of the tree in any case. Once again, however, this work is of limited practical use in a setting where (for example) one is trying to make Internet search more efficient - after all, when is the last time you did a Google search and got no results?

A wide variety of authors have also considered fast (generally _O(n_log_n_)) methods for constructing nearly optimal binary trees. The three most popular ideas appear to be the following:

1. **Splay trees** were introduced by Sleater and Tarjan [17]. The tree is initially constructed randomly, but every query moves its target to the top of the tree, hopefully causing frequent queries to have small depths. Splay trees are intended to be adjusted online as queries are received, as opposed to depending on a knowledge of relative probabilities in advance.<tbc>

2. **Treaps** were developed by Aragon and Seidel [2,16] although the method is hinted at earlier by Mehlhorn [12]. In this approach, the binary tree is constructed by inserting points in probability order. Although the average<tbc>

