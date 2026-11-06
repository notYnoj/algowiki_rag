A Foundation for Proving Splay is Dynamically Optimal<sup>∗</sup>

**Abstract**

Consider the task of performing a sequence of searches in a binary search tree. After each search, we allow an algorithm to arbitrarily restructure the tree. The cost of executing the task is the sum of the time spent searching and the time spent optimizing the searches with restructuring operations. Sleator and Tarjan introduced this notion in 1985, along with an algorithm and a conjecture. The algorithm, Splay, is an elegant procedure for performing adjustments that move searched items to the top of the tree. The conjecture, called dynamic optimality, is that the cost of splaying is always within a constant factor of the optimal algorithm for performing searches. We lay a foundation for proving the dynamic optimality conjecture. Central to our method is approximate monotonicity. Approximately monotone algorithms are those whose cost does not increase by more than a fixed multiple after removing searches from the sequence. As we shall see, Splay is dynamically optimal if and only if it is approximately monotone. This result extends to a weaker form of approximate monotonicity as well as insertion, deletion, and related algorithms. We prove that a lower bound on optimal execution cost is approximately monotone and outline how to adapt this proof from the lower bound to Splay, and how to overcome the remaining barriers to establishing dynamic optimality.

## 1 Context

The binary search tree is the canonical pointer-based data structure for maintaining a sorted collection in fast memory. Its most attractive feature is that the number of comparisons required to verify the presence of an item is logarithmic in the size of the tree, provided that the tree is properly arranged. Without exercising care when adding elements, however, a binary search tree can easily become unbalanced, making search cost proportional to the size of the tree in the worst case. Thus binary search trees require some form of maintenance and restructuring for good performance.

Adel’son-Vel’skii and Landis gave the first method that guarantees efficient searches in the presence of updates [1]. They supplement nodes with bits that provide rough information about how balanced each node’s subtrees are. After an insertion or deletion, a restructuring procedure restores invariants on the balance bits. These invariants ensure that all paths in the tree have length at most logarithmic in the tree’s size. There are many variations of this idea. Perhaps most famous is the red-black tree due to its requiring fewer restructuring operations and a catchy name [32]. Restructuring schemes based on balance bits remain an active topic of research [33]. Many more schemes now exist. Randomized search trees, such as treaps [60], zip trees [66] and others [52] trade worst-case performance guarantees for good expected behavior in order to gain simpler rebalancing procedures and fewer pointer changes. Scapegoat trees [4, 28] defer restructuring

<sup>∗</sup>This paper is an adaptation of the first author’s Ph.D. thesis [45]. We presented an earlier version at SODA [46]. <sup>†</sup>Sunshine; caleb.levy@gmail.com. <sup>‡</sup>Department of Computer Science, Princeton University; Intertrust Technologies; ret@cs.princeton.edu.

Caleb C. Levy<sup>†</sup>

Robert E. Tarjan<sup>‡</sup>

arXiv:1907.06310v3 [cs.DS] 9 May 2022

