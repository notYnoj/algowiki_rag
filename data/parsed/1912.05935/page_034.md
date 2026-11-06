- all black cells that are found on row _i_ and column _j_ are excluded,

- all black cells that are located along the left and right diagonals passing through the cell (_i,j_) are excluded.

a2) on other board:

- all white cells that are found on row _i_ and column _j_ are excluded,

- all white cells that are located along the left and right diagonals passing through the cell (_i,j_) are excluded.

b) If on one of the boards the queen is located on a white cell with indices (_i,j_), then all the actions of items a1) and a2) are performed for cells of the opposite color.

5. Imagine that in a solution matrix of size \(n\times n\), rows can slide right or left relative to each other, in increments of k cells. Moreover, if the previous row was shifted, for example, to the left, then the next row should be shifted to the right, i.e. each next row is shifted in the opposite direction to the previous row. As a result of this construction, we obtain a rectangular matrix of size \(n\times(n+k)\), where in each row _k_ cells from the beginning of the row or from the end will be excluded from consideration. The problem is to find the maximum value of _k_ for an arbitrary value of _n_ for which there is at least _h_ solution n-Queens Problem (_h_=1,2,3,4,5).

Consider a variant of the problem in which the offset of one line with respect to another is a random number ranging from _k_1 to _k_2.

6. The one-dimensional formulation of _n_-Queens Problem. Suppose that on some line _n_ segments are numbered from 1 to _n_. Divide each segment into _n_ cells, and within each segment, number cells from 1 to _n_. We call such cells open. It is required to select one open cell in each segment, taking into account the following constraints:

a) We can select the open cell with number _j_ from the _i_-th segment, if:

\(D1(r)=0;\)<br> \(D2(t)=0;\)

where _r=n+j-i_; _t=j+i_, _D_1 and _D_2 - 1-dimensional control arrays consisting of 2_n_ cells that were previously zeroed.

