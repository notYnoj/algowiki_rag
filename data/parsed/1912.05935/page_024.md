A slight deviation from the general trend is typical only for the values _n_=(10_,...,_49), which is due to the fact that only the fifth block of calculation is used in this range. The algorithm for finding the solution of the fifth block is significantly different from the operation of the algorithms of the first and third blocks.

In the obtained dependence, the linear coefficient (0.781568) is less than one, which leads to the fact that with increasing _n_, the regression line and the diagonal of the quadrant diverge.

In order to clearly explain the reason for this discrepancy instead of the initial time, we consider the average time that is necessary for the location of one queen on one row, i.e. divide the average counting time by _n_. We call such an indicator the reduced time. Obviously, if the reduced time does not change with increasing _n_, then such a solution will be linear (_O(n_)). As can be seen from Figure 8, which shows a plot of the logarithm of the reduced time (_tRow_), increased by 10<sup>6</sup> times, on the logarithm of the size of the solution matrix, in the range of _n_ from 50 to 10<sup>8</sup>, the reduced time decreases with increasing _n_. If the reduced time for _n_=50 is 10.7146⋆10<sup>-6</sup> seconds, then the corresponding time for _n_=10<sup>8</sup> decreases by 21 times and is 0.5084⋆10<sup>-6</sup> seconds. Such behavior of the algorithm, at first glance, seems erroneous, since there are no objective reasons why the algorithm will<tbc>

2.2
2
1.8
1.6
1.4
1.2
1
0.8
0.6
1
2
3
4
5
6
7
8
Decimal logarithm of solution matrix size, log10(n)

Figure 8: Dependance of the average time to place queen on one row on the size of solution matrix. _tRow_ - average time required to place queen on one row.

