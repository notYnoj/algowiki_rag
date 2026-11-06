<tbc>those that do not have a solution. The number of such False Negative solutions is insignificant, and their share is mainly less than 0.0001 of sample size. As _n_ increases, the share of False Negative solutions decreases. For all values of _n\>_800, in this series of experiments, there was not a single case of False Negative solutions. However, it is obvious that if the sample size is increased many times, the possibility of the appearance of a False Negative solution is not excluded, although the probability of such an event will be a very small number.

## The time complexity of the algorithm.

Figure 7 shows a graph of changes in the average completion time of random compositions for different _n_. The decimal logarithm of _n_ is plotted along the abscissa axis, and the logarithm, increased by 1000 times, of the average counting time, is plotted along the ordinate axis. For clarity, the figure also shows the dotted line of the diagonal of this quadrant. It can be seen that the solution time increases linearly with an increasing _n_. Over the entire range of _n_ values from 50 to 10<sup>8</sup>, the experimental values of the counting time form a straight line, which is described with a fairly high accuracy (R=0.9998) by the linear regression equation

\(log(1000*t)=-0.628927+0.781568*log(n)\)

8
7
Decimal logarithm of completion time, log(t*1000)
6
5
4
3
2
1
log(1000*t)= 0.628927 + 0.781568*log(n)
0
1
2
3
4
5
6
7
8
Decimal logarithm of solution matrix size, log(n)

Figure 7: Dependence of the average completion time (_t_) of an arbitrary composition on the size (_n_) of solution matrix.

