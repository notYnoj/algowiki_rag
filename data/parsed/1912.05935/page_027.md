<tbc>shape, consider the distribution of completion time for compositions that all have the same size. For this, as an example, we selected from the original sample with size one million, all the compositions whose size is equal to 800. There were 998 such compositions in the sample. Figure 11 shows a completion time histogram for this sub-sample. It can be seen from the figure that the distribution mainly consists of six separate histograms, with decreasing sizes. The reason why the completion time of 998 compositions, in each of which 800 queens where randomly distributed, "clustered" in 6 groups, is the use of the Back Tracking procedure. The first histogram in the figure, with the maximum sample size, is those completion solutions where the BT procedure has never been used. This is a group of the fastest solutions. The second histogram, which is significantly smaller in size than the first, is those solutions in which the BT procedure was used only once. Therefore, the solution time in this group is slightly longer than in the first. Accordingly, in the third group, the BT procedure was used twice, in the fourth - three times, etc., i.e. Solutions in which the BT procedure was used repeatedly were performed over a longer time. Such solutions form the long right tail of the desired distribution.

**False Negative solutions**. If we divide all possible compositions for an arbitrary value of _n_ into positive and negative, then among the positive compositions there are those that this algorithm can classify as negative. This<tbc>

160
Composition Size = 800 Sample Size = 998 Chess board: 1000 x 1000
140
120
100
80
Absolute Frequency
60
40
20
0
0.02
0.03
0.04
0.05
0.06
0.07
0.08
0.09
0.1
0.11
0.12
Composition Completion Time, sec

Figure 11: Completion time histogram for compositions with same size. (_n_=1000; compositions size=800; sample size = 998).

