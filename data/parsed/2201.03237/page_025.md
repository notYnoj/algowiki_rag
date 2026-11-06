<tbc>that dynamic method performs better. Therefore, we adopt the second method in our experiment. Generally speaking, a larger value of _mp_ indicates a larger average out-degree, and the precision of search results is also higher. However, over large out-degree will also lead to the decline of efficiency. Therefore, with the increase of _mp_, the efficiency will firstly increase and then decrease, which is confirmed by our experiment in Figure 8. We only change _mp_ from 0.5 to 0.54 on Sift and Glove, and we can see that the maximum efficiency was achieved around 0.53.

The parameter setting of other algorithms is mainly based on [20], some of which are fine tuned for better performance.

Sift
1000
Glove
2500
TBSG-0.50
TBSG-0.50
TBSG-0.51
TBSG-0.51
TBSG-0.52
TBSG-0.52
2000
TBSG-0.53
800
TBSG-0.53
TBSG-0.54
TBSG-0.54
1500
600
OPS
OPS
1000
400
500
200
0
0
0.960
0.965
0.970
0.975
0.980
0.985
0.990
0.995
1.000
0.90
0.92
0.94
0.96
0.98
1.00
Precision@100
Precision@100

Index Complexity
Search Complexity
1750
Sift
Gist
1500
Glove
O(n)
20
O(n)
1250
O(n)
15
Sift
1000
Glove
Gist
750
O(logo1*2.94)
O(logo1*2.61)
Time(sec)
Time(sec)
10
O(logo1*2.38)
500
250
5
0
0
200000
400000
600000
800000
1000000
1200000
0
200000
400000
600000
800000
1000000
1200000
Number of Points
Number of Points

Figure 8: The result of using _mp_ ranging from 0.5 to 0.54 on Sift and Glove.

Figure 9: The result of index complexity and search complexity on Sift, Gist and Glove.

