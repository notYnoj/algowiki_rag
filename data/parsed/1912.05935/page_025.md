<tbc>consider it slower for small values of _n_ than for large values. However, there is no error, and this is an objective property of this algorithm. This is due to the fact that this algorithm is a composition of three algorithms that operate at different speeds. Moreover, the number of rows processed by each of these algorithms changes with increasing _n_. It is for this reason that the counting time is increasing in the initial interval of values _n_=(10, 20, 30, 40), since all calculations in this small area are carried out only on the basis of the fifth block of procedures, which works very efficiently, but not as fast as first block of procedures. Thus, taking into account that the counting time required for placing the queen on one row decreases with increasing size of a chessboard, the time complexity of this algorithm can be called decreasing-linear.

**The number of cases when the Back Tracking procedure has never been used**. In all cases of a computational experiment, we tracked the number of cases when the Back Tracking(BT) procedure was used in the process of solving each problem. A cumulative summation was made of all cases of using BT, regardless of on what base level was returned to during the search for a solution. This gave us the opportunity to determine for each sample the share of those solutions in which the BT procedure has never been used. Graph in Figure 9 shows how the share of solutions without the use of the BT procedure changes with increasing _n_. It can be seen that in<tbc>

70
60
50
Zero Back Tracking, %
40
30
20
10
100
1000
10000
100000
1000000
0
1
2
3
4
5
6
7
8
Decimal logarithm of solution matrix size, log10(n)

Figure 9: The share of solutions in the sample in which the BT procedure has never been used.

