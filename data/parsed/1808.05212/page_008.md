We conclude our discussion by listing Schwiebert’s sorting network which is known to have the minimum number of stages/delay time. Note that the average and maximum number of comparisons is considerably higher.

## 3 Intuition and Extension

To some the lowered statistics seem surprising. Typical reasoning follows: "to sort three, order any two, the third draws a bye. Bye enters and plays to establish an overall winner (WLOG, loser); third step ranks the runner’s up." While accurate when elements are chosen freely, as a memory- based method each element carries a rank implicit in its index. CE sorting ranks all elements, chosen pairs are not isomorphic. In the case of _N_=3 we may disambiguate thus: "Choosing any two at most omits the median, our set is are guaranteed to hold at least the min or max. Choosing and sorting the outermost elements therefore guarantees at least one of max or min landing in its<tbc>

\begin{tabular}{cccccccccc}
Design & \multicolumn{3}{c}{Median only} & \multicolumn{3}{c}{Min/Med/Max} & \multicolumn{3}{c}{Fully sorted} \\
 & \multicolumn{2}{c}{Swaps} & Stages & \multicolumn{2}{c}{Swaps} & Stages & \multicolumn{2}{c}{Swaps} & Stages \\
 & Avg & Max & & Avg & Max & & Avg & Max & \\
old & 9.105 & 19 & 9 & 9.771 & 21 & 9 & 11.56 & 25 & 11 \\
new & 6.99 & 13 & 6 & 7.657 & 14 & 6 & 9.443 & 18 & 8 \\
new/old & 76.8% & 68.4% & 66.7% & 78.4% & 66.7% & 66.7% & 81.7% & 72.0% & 72.7% \\
\end{tabular}

25
25
13.68
0
1
X
2
X
3
X
4
X
5
X
6
X
7
X
8
X
9
X

1: Summarized statistics of the old and the new design for sorting 9-element networks.

Figure 10: Loren Schwiebert’s 25-link sorting network for 9 elements taken from \[4, Figure 51 for _n_=9\] with delay time 7, i.e., 7 stages.

