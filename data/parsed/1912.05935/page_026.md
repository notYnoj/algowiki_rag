<tbc>the range of values _n_=(7_,...,_100000), the number of solutions in which the BT procedure has never been used exceeds 35%. Moreover, in the range of values _n_=(320_,...,_22500), the number of such cases exceeds 50%. The most effective results were obtained for a chessboard of size \(5000\times 5000\), where in 61.92% of cases of completion from 10000 solutions, a "deterministic solution" of a non-deterministic problem was received, because in this cases BT procedure don’t been used. In the remaining solutions, in 21.87% of cases, the BT procedure was used 1 time, in 9.07% of cases - 2 times, and in 3.77% of cases - 3 times. Together, this accounts for 96.63% of all cases. The fact that after the value _n_=5000, the number of cases of completion without using the BT procedure is gradually decreasing, is associated with the boundary selecting model of _baseLevel.2_ and _baseLevel.3_. We can change these parameters and increase the number of solutions without using the BT procedure. However, this will lead to an increase the counting time, since the share of the fifth block in the algorithm will increase.

**A completion time histogram**. In Figure 10, for _n_=1000, a completion time histogram for sample of one million solutions is presented. The not quite ordinary view of the distribution histogram (which most likely resembles the night silhouette of high-rise buildings) is not associated with an error in the selection of the length or number of intervals. This is a natural property of this algorithm. To understand why the histogram has such a<tbc>

x104
7
Sample Size = 1000000 Chess board: 1000 x 1000
6
5
4
Absolute Frequency
3
2
1
0
0
0.02
0.04
0.06
0.08
0.1
0.12
Composition Completion Time, sec

Figure 10: Completion time histogram for compositions with different size. (_n_=1000; sample size=10<sup>6</sup>).

