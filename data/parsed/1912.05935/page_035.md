b) After a such selection, will be closed the segment _i_ and cells with number _j_ in all remaining free segments. Also, it is necessary to close the corresponding cells in the control arrays:

\(D1(r)=1;\)<br>
\(D2(t)=1;\)

In this formulation, the task is completely identical to the original one. Of interest are the formulations of this problem with other constraint conditions. For example, if instead of the formulas: _r=n+j-i_ and _t=j+i_, other relations will be considered that functionally connect the indices _r_ and _t_ with the indices (_i,j_) of the solution matrix.

## 7. The formulation of the task on the basis of an urn with balls (identical to the previous task).

Suppose there are _n_ urns numbered from 1 to _n_, and in each urn there are _n_ balls, also numbered from 1 to _n_. It is required to select one ball from each urn, given the following restrictions:

a) We can select a ball with number _j_ from the _i_-th urn, if:

\(D1(r)=0;\)<br>
\(D2(t)=0;\)

where _r=n+j-i_; _t=j+i_, _D_1 and _D_2 - 1-dimensional control arrays consisting of 2_n_ cells that were previously zeroed.

b) After a such selection, will be closed the urn _i_ and balls with number _j_ in all remaining free urns. Also, it is necessary to close the corresponding cells in the control arrays:

\(D1(r)=1;\)<br>
\(D2(t)=1;\)

In this formulation, the task is completely identical to the original one. As in the previous case, the formulation of this problem with other constraint conditions is of interest.

## 8. The game.

Consider a chessboard of size \(n\times n\). We will return the color to the queens, let some queens have white color, others black. We also return the alternating white and black color to the cells of the chessboard, based on the fact that in solution matrix the cell with the index

