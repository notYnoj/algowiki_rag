## 4 Experimental results

It follows from the results of the previous section that we can use our ideas to reduce the expected cost of searching a binary tree, and that doing so can be done in a timely fashion. It is not clear, of course, whether the methods will be effective in practice.

For each of the four basic tree constructions described in Section 2, we bumped nodes with the highest merit until quiescence, so that the tree could not be improved further with our simple method. The results are shown in Figure 4.

Two immediate observations are that the cost remains essentially linear in the logarithm of the tree size, and that the techniques we have proposed are by no means a panacea. They work well for some trees and clearly less well for others. Balanced binary trees, for example, provided the worst performance both before and after the trees are unbalanced.

Beyond that, however, the results are more interesting. Unbalanced splay trees and unbalanced weight-balanced trees perform virtually identically, even though their performance was starkly different before unbalancing. (In actuality, the weight-balanced trees benefited almost not at all from our ideas; the splay trees improved substantially.)

14
binary unbalanced splay unbalanced weighted unbalanced treap unbalanced optimal
12
10
8
mean cost
6
4
2
100
1000
10000
100000
1x106
1x107
tree size

Fig. 4: Algorithm performance after unbalancing the trees

