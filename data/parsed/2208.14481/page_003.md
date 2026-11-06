<tbc>case complexity is within a constant factor of optimal, Mehlhorn points out that in the worst case, the tree produced may be quite far from optimal. Mehlhorn argues that the method should be discarded for that reason.<tbc>

3. **Weight-balanced binary trees** also appear in Mehlhorn’s work [12]. In the construction of the tree or any subtree, the node at the root is the one that most evenly divides the aggregated probabilities of the residual nodes between the left and right subtrees.<br>
If _H_ is the entropy of the frequency distribution of the nodes in the tree, Mehlhorn shows that the cost _C_ of the tree constructed in this fashion is bounded below by _H/_log3≈0.63_H_ and above by<tbc>

<tbc>\(2+H/[1-log(\sqrt{5}-1)]\approx 1.44H,\)<tbc>

<tbc>and that these bounds apply to the optimal tree as well. For \(H\ge 14.5\), the lower bound was subsequently improved by De Prisco and De Santis [15] to<tbc>

<tbc>\(H+HlogH-(H+1)log(H+1)\ge H-logH-1-\frac{1}{H}\approx H-1.\)<tbc>

<tbc>For treaps and weight-balanced trees, it can be shown that the average case performance of the data structure in question is within some constant factor of optimal. (Indeed, for weight-balanced trees, the cost is within a constant factor of optimal in every case.) This is suspected to be the case for splay trees as well, but this "dynamic optimality conjecture" has not been proven. The best result of this general type appears to be due to Lecomte and Weinstein [11], who show that Tango Trees [5] are within a factor of _O_(log(log(_n_))) of optimal.

In today’s world, however, where significant computing resources are devoted to finding objects on the Internet, even a pure constant factor is arguably not good enough. All of the above methods (except Tango Trees) were developed in an environment where it was assumed that tree searches would be approximately as common as insertions.<sup>1</sup> Such an assumption is obviously no longer valid today; I (thankfully!) search the Internet far more frequently than I modify it in a publicly accessible way.

Our goal in this paper is to describe a technique that unbalances binary trees in a way that improves their average-case performance. The technique that we will present can run in time _O(n_), although performance will be better as run time is permitted to increase, and is guaranteed to improve the expected performance of the tree being optimized.

We discuss our basic experimental framework and the baseline corresponding to existing techniques in the next section, and our new ideas are introduced in Section 3. Experimental results are presented in Section 4, and suggestions for future work appear in Section 5.

<sup>1</sup> Donald Knuth, personal communication.

