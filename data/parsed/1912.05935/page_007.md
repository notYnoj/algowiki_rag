<tbc>the return points. If, as a result of the solution, a deadlock occurs, then, depending on the parameters of the task, we return back to one of these three basic levels. The first base level (_baseLevel_<sub>1</sub>) corresponds to the state when the data verification of the composition is completed. This is the beginning of the program. The values of the following two base levels (_baseLevel_<sub>2</sub> and _baseLevel_<sub>3</sub>) depend on the size of the matrix _n_. The empirical dependence of these basic values on the size of the solution matrix was established on the basis of a large number of computational experiments. For a more accurate representation of this dependence, we divided the entire considered interval from 7 to 10<sup>8</sup> into two parts. Let _u=lg(n_), then<br>
if _n\<_30000

_baseLevel_<sub>2</sub>=_n-round_(12.749568∗_u_3-46.535838∗_u_2+120.011829∗_u_-89.600272)

_baseLevel_<sub>3</sub>=_n-round_(9.717958∗_u_346.144187∗_u_2+101.296409∗_u_50.669273)<br>
else

_baseLevel_<sub>2</sub>=_n-round_(-0.886344∗_u_3+56.136743∗_u_2+146.486415∗_u_+227.967782)

_baseLevel_<sub>3</sub>=_n-round_(14.959815∗_u_3253.661725∗_u_2+1584.713376∗_u_3060.691342)

## 4.2 Block structure

The algorithm is built in the form of a sequence of five event blocks, where each event is associated with the implementation of a certain part of problem solution. The algorithms in each block are different from each other. Only three blocks serve to form the solution, the remaining two blocks are preparatory. The choice of the block number from which the calculations begin depends on the value of _n_ and on the results of comparing the composition size _k_ with the values of _baseLeve_<sub>2</sub> and _baseLevel_<sub>3</sub>. An exception is the interval of values _n_=(7_,...,_99), which can be called a "turbulent zone" due to the peculiarities of the algorithm behavior in this section. For values _n_=(7_,...,_49), regardless of the composition size, after entering and controlling data, the calculations begin from the 4th block. For values _n_=(50_,...,_99), depending on the composition size, calculations begin either from the second block or from the fourth. At each stage of solving the problem, only those positions in the row are considered that don’t fall into the zone of restrictions created by previously established queens. It is these positions that are called free. Let us briefly describe what calculations are performed<tbc>

