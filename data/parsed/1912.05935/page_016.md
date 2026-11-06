<tbc>tests equal to one million, not a single complete solution was obtained on the basis of the _rand_ & _rand_ model.

b) this algorithm is much slower than the _randSet_ & _randSet_ algorithm. If, for _n_=1000, a composition of size 967 is generated, the average time to obtain one composition will be 0.049679 seconds, which is 36 more than the corresponding value of 0.001372 for the _randSet_ & _randSet_ model. The reason for the differences between two essentially similar methods of random selection is due to the fact that in the _randSet_ & _randSet_ model, in order to speed up the calculations, random selection from the remaining list is not carried out at each step. Instead, a pair of indices is sequentially selected from two lists, whose elements were randomly rearranged. Such selection is not random at the full extent, however, it fits well with the logic of the problem and allows us to quickly count.

To visually demonstrate the operation of the _rand_ & _rand_ algorithm, the following experiment was conducted: for a chessboard of size \(100\times 100\), after each queen placement step, the number of free positions in each of the remaining free rows is determined. Thus, after each step of solving the problem, we received a list of free rows and a corresponding list of the number of free positions in these rows. Based on these results, a graph was<tbc>

0.09
0.08
0.07
0.06
The probability of the event
0.05
0.04
0.03
0.02
0.01
0
5
10
15
20
25
30
35
40
The size of the solution matrix, n

Figure 4: Decreasing the probability of obtaining a complete solution in _randSet_ & _randSet_ model with increasing n.

