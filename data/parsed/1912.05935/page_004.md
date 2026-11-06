<tbc>the control vector _D_2 (cell 10 in the figure). The projections of all cells of the solution matrix lying on the same left diagonal fall into the same cell of the left control vector _D_1, respectively, the projections of all cells of the solution matrix lying on the same right diagonal fall into the same cell of the right control vector _D_2. Thus, these two control vectors _D_1 and _D_2, allow full control of all diagonal inhibitions for any cell of the solution matrix.

It is important to note that the idea of using diagonal projections onto cells of control vectors to determine whether a cell of a solution matrix with coordinates (_i,j_) is free or busy was also later implemented by Richards [4]. This publication provides one of the fastest recursive search algorithms for all solutions, based on operations with a bit mask. An important difference is that this algorithm is designed for the sequential search of all solutions, starting from the first row of the solution matrix - down, or from the last row of the matrix - up. The algorithm we proposed is based on the condition that the choice of the number of each row for the location of the queen must be arbitrary. For the considered algorithm, this is of fundamental importance. Note that the above figure 1, we built by analogy with what is published in this paper.

A program to check whether a given solution of the _n_-Queens problem is correct, or whether a given composition of _k_ queens is true, is as follows.

1. To control diagonal constraints, we must create two arrays _D_1(1:_n_2) and _D_2(1:_n_2), where _n_2=2∗_n_, and array _B_(1:_n_) to control the oc<tbc>

D1
D2
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24

Figure 1: Demo example of the diagonal projections of the matrix cells to the corresponding cells of the control arrays _D_1 and _D_2. (_n_=8)

