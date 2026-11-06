<tbc>in the remaining rows, which leads to the fact that in some rows the rate of reduction in the number of free positions is higher than in other rows. In contrast, with random selection of the free row index and free column index, the queen’s positions are evenly distributed over the "area" of the solution matrix, which reduces the "average" rate of reduction in the number of free positions in the remaining rows. Thus, taking into account the capabilities of the _rand_ & _rand_ algorithm, we use it in the program to continue the formation of the solution search branch until reach the _baseLevel_<sub>3</sub>.

It should be noted that even if the selection algorithms (_randSet_ & _randSet_, _rand_ & _rand_) were not so efficient, we would still have to use some other random selection method when developing the algorithm. This is due to the very statement of the n-Queens Completion problem. If we imagine that there is a certain optimal algorithm that solves the problem, then at the input such an algorithm will always receive a random set of row and column indices. Each time it will be a new random set of row and column indices from a huge variety of possibilities. In order to be able to "take in" the algorithm, such a variety of random compositions, the algorithm itself must be built on the basis of random selection. Matching should be like a key to the lock. If we construct the algorithm on this principle, then any consistent composition of _k_ queens will be considered as the initial<tbc>

100
n=100
90
Step=10
Number of free positions in remaining rows
80
70
60
Step=40
50
40
30
Step=60
20
10
Step=70
10
20
30
40
50
60
70
80
90
100
Row index in the solution matrix

Figure 6: Decreasing the number of free positions in the remaining free rows after placing queens, _rand_ & _rand_ model.

