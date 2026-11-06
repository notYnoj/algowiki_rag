Exchanges are costly, often at a ratio of 2:1 or 3:1 to a simple comparison. We have affixed the likelihood of an exchange to each link. Summary statistics give the maximum and average number of exchanges for the entire network. Consider Figure 1(a) which features 3 stages, namely --in that order-- (23), (12), and again (23). The number 3 in the upper left corner gives the _number_ of links for this particular network. The second number, again 3 here, means that there is one input to the network where 3 links are active and swap, the _worst-case scenario_. The third number, 1.5, means that the average number of swaps, taken over all possible inputs, is 1.5. The number 0 in the upper right corner is a degree of _disorder_ meaning that this design results in a fully sorted array which can also be seen by the three x characters in the output. Below the left rectangle, the first row "10.5" signifies that the probability of an exchange at stage 1 is \(0.5=\frac{1}{2}\); the second row "20.666667" signifies that the probability of an exchange at stage 2 is 0.666667≈2/3; finally, the third row "30.333333" signifies that the probability of an exchange at stage 3 is 0.333333≈1/3. In Appendix A, we provide more details on how the statistics in Figure 1(a) was obtained.

The networks presented so far for _N_=3 are distinct and require in both cases three stages, comparisons and exchanges. Both also demonstrate that a full sort network will include all possible length=1 links as these alone can serve to reorder permutations of sorted data when merely one adjacent transposition exists. The symmetry in Figure 1(b) is compelling: it allows for fully bidirectional sorting when then input and output sides reverse. Unfortunately, it (as in Figure 1(a)) also exhibits a link (a.k.a. comparator in [4]) in which swapping occurs more often than not.

When a link exchange occurs more than half the time, we may reverse the swap vs non-swap .67/.33 to .33/.67 by preexchanging its elements. We remove the direct cost of the exchange by reversing the order of input lines to the left of the offending link. But all inputs are unsorted so any non-conditional exchange has no sorting efficacy and may be removed. In Figure 1(a), the offending link is at stage 2, namely (12). Thus, we replace (23) by (13) at stage 1 while keeping (23) at stage 3 unchanged. For Figure 1(b), the offending link is at stage 3, namely (12). Thus, we replace (23) by (13) at stage 1 and (13) by (23) at stage 2.

3
3
1.5
0
3
3
1.5
0
1
X
1
X
2
X
2
X
3
X
3
X
1
0.5
1
0.5
2
0.666667
2
0.333333
3
0.333333
3
0.666667
(a)
(b)

Figure 1: Two sorting networks: (a) corresponds to the comparisons (23), (12), (23), at stages 1, 2, 3, respectively; (b) corresponds to the comparisons (23), (13), (12), at stages 1, 2, 3, respectively.

