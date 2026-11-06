is different than the inequality comparison value has been considered for the constant edge cost version of this problem, e.g., [15], [21]. Approaches for solving this have led to the more germane problem in which, rather than allowing an inequality _and_ an equality comparison in each step, one allows an inequality _or_ an equality comparison in each step. This is known as the _two-way key comparison_ problem. If data are highly irregular such that the most probable item is much more probable than any other and is in [2_,n_-1], then an initial equality comparison to the most probable item would likely improve on the "optimal" \((<,\ge)\) decision tree. For fixed edge costs, the algorithm for solving this is a _O(n_<sup>5</sup>)-time _O(n_<sup>3</sup>)- space dynamic programming algorithm [36]. In this algorithm, instead of just _i_ and _j_, a third variable _d_ represents the number of items missing from the subtree due to equality comparisons above this subtree; this accounts for the increased complexity. This algorithm uses the conjecture that equality comparisons should always be with the most likely (remaining) item. This was not proved for equal edge costs, and, even given its veracity, it is not clear whether this would also be true for unequal edge costs. Nevertheless, no counterexample has been presented, so it is a safe assumption to make, especially since such trees would necessarily perform at least as well as the optimal binary decision tree.

The two-way comparison algorithm has been extended to a large variety of problems, including a problem with nine different branch costs: unequal (ordered) costs for \((=,\neq)\) testing, unequal (ordered) costs for \((\le,>)\) testing, unequal (ordered) costs for \((<,\ge)\) testing, and unequal (ordered) costs for three-way testing [37, Chapter 9]. This algorithm can be easily modified for unordered costs by adding tests for \((\neq,=)\), \((>,\le)\), \((\ge,<)\), and other three way tests. Other modifications can be made in a similar manner to those discussed in this paper. Note that some variants of this problems have complexity reduced from _O(n_<sup>5</sup>) to _O(n_<sup>4</sup>) [3], [36], although

this has not been shown to be true of the more general cases that most accurately represent the behavior of hard-coded search trees.

## V. CONCLUSION

In this paper, we presented methods for finding optimal decision and search trees given the real-world behavior of microprocessors, in which not all queries and decision outcomes have identical temporal costs. This approach most often assumes we can hard code the decision tree based on a known probability distribution and known processor behavior. The simplest method, that of Section II, must be generalized for more complex processor prediction techniques, as well as for other subtler performance considerations and for cases in which equality comparisons are allowed. Due to the growing asymmetry of branch performance in complex processors, this often results in strictly better hard-coded search trees than the "optimal" trees produced using traditional methods.

## REFERENCES

[1] J. Abrahams, " and parse trees for lossless source encoding," _Communications in Information and Systems_, vol. 1, no. 2, pp. 113- 146, Apr. 2001.

[2] D. Altenkamp and K. Mehlhorn, "s: Unequal probabilities, unequal letter costs," _J. ACM_, vol. 27, no. 3, pp. 412-427, July 1980.

[3] R. Anderson, S. Kannan, H. Karloff, and R. E. Ladner, "Thresholds and optimal binary comparison search trees," _J. Algorithms_, vol. 44, no. 2, pp. 338-358, Aug. 2002.

[4] A. Andersson, "A note on searching in a binary search tree," _Softw., Pract. Exper._, vol. 21, no. 10, pp. 1125-1128, Oct. 1991.

[5] "Performance of the ARM9TDMITM and ARM9E-STM cores compared to the ARM7TDMITM core," ARM Limited, available from http://www.arm.com/pdfs/comparison-arm7-arm9-v1.pdf.

[6] P. Bradford, M. Golin, L. Larmore, and W. Rytter, "Optimal prefix-free codes for unequal letter costs: Dynamic programming with the Monge property," _J. Algorithms_, vol. 42, no. 2, pp. 219-223, Feb. 2002.

[7] T. Cover, "Admissibility properties of Gilbert’s encoding for unknown source probabilities," _IEEE Trans. Inf. Theory_, vol. IT-18, no. 1, pp. 216-217, Jan. 1972.

[8] A. Fog, "How to optimize for the Pentium<sup>®</sup> microprocessors," 2004, available from http://www.agner.org/assem/.

p(2) B2 p(1) p(4) B1 B4 p(3) a0 a1 B3 a4 a2 a3 (a) Alphabetic tree (βi = 0) (b) Search tree (αi = 0) (c) Full search tree

Fig. 5. Sample search trees (fixed-length representation)

