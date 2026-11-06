<tbc>may be the roots of further subtrees, the result of operating on _T_ with a _right rotation_ is the new tree shown in Figure 3.

Note that the new tree retains the ordering of the original (presumably _c\<b\<d\<a\<e_), and that _c_, _d_ and _e_ remain apparent fringe nodes in the new tree so that if they are in fact the roots of subtrees, those subtrees can remain attached as previously. The rotation here is generally referred to as the _right rotation rooted at a_, where _a_ is the root of the subtree being rotated.

Similarly, we will say that a _left rotation at b_ produces Figure 2 from Figure 3.

**Definition 3** _Let T be a tree, and let_ \(x\in T\) _be a non-root node. By the result of_ bumping _x in T, to be denoted by T<sup>x</sup>, we will mean the result of right rotating T at_ \(\pi(x)\) _if x is the left child of_ \(\pi(x)\)_, and the result of left rotating T at_ \(\pi(x)\) _if x is the right child of_ \(\pi(x)\)_. If r is the root of T, we will take Tr to be T itself._

Thus Figure 3 shows the result of bumping _b_ in Figure 2, and Figure 2 is the result of bumping _a_ in Figure 3.

a
b
e
C
d

b
C
a
d
e

Fig. 2

Fig. 3

