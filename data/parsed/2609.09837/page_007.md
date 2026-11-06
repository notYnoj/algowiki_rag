# The Parameterized Complexity of Coloring Discovery

7

representatives. All remaining assigned colors are assigned bijectively to the remaining vertices. Hence the matching cost is attainable and is also a lower bound on every realization.

There are at most (_k_+1)_<sup>k</sup>_ partitions and (2_<sup>k</sup>_+1)_<sup>k</sup>_ maps, and hence 2<sup>O(_k_<sup>2</sup>)</sup> cases in total. The assignment side and the color side of each matching instance have at most _n_ nodes each, so weighted matching takes O(_n_<sup>3</sup>) time. Computing _S_ via vertex cover in the complement graph and solving the resulting assignment problems gives the stated running time. We present the full details in Appendix A.2.

### 3.2 Color swapping

We now fix two colorings \(\alpha,\beta:V(G)\rightarrow[q]\) and ask for the minimum number of swaps that transform \(\alpha\) into \(\beta\). We assume that \(\alpha\) and \(\beta\) have the same color histogram.

(I) Input
(II) Compute Vertex Cover C
(III) Guess Partition P
P2
C
P1
(IV) Build and Solve Assignment Instance
P1
= =4
r
w(P1,g) = 2
0
w(P2,r) = 4
P2
w(P2,g) = 0
g
w(P2,b) = 3
w(P1,b) = 5
0
*
0
b

**Fig.1.** The four stages of the flip algorithm for a fixed vertex cover: the input instance, the computation of _C_, the guessed partition P of _C_ into independent blocks, and the minimum-cost assignment of distinct color names to the blocks. Thick edges show an optimum assignment in the example; the node ∗ is a zero-cost dummy used to balance the two sides.

