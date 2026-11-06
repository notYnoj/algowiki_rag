from different positions, we can see different things. Below are some of them.

1. Consider the problem of arranging _n_ queens on a rectangular "chess" board of size \(n\times m\). Denote _k=m-n_. Let some solution be obtained, and each of the _n_ rows contains one queen. We exclude the positions where the queens are located from further consideration. Now in each row there is _m_-1 free position. Within the remaining free positions, we again find one solution. As before, we exclude from further consideration the positions where the queens of the second solution are located. Now in each row there are _m_-2 free positions. Obviously, the first and second solutions do not intersect in their positions in any row - they are orthogonal. It is required to determine the maximum number of mutually orthogonal solutions for various values of _k_. If _n_ mutually orthogonal solutions are found for the value _k_=0, then a Queens Latin Square will be constructed.

**Comment**. In the publication Grigoryan [6] showed that for any n-Queens Problem solution, there is a complementary solution that does not intersect with it. This means that for an arbitrary value of _n_, the set of all _n_-Queens Problem solutions is divided into two equal-sized subsets. Any solution from the one subset is a complementary solution to the corresponding solution from the other. The rule is quite simple, if _Q_1 (i) is a solution from the first subset, then the corresponding complementary solution _Q_2(_i_) from the second subset is determined by the formula _Q_2(_i_)=_n_+1-_Q_1(_i_), where _i_=(1_,...,n_). It is this rule that explains the fact that the number of all solutions of the _n_-Queens Problem, for any arbitrary value of _n_, is always an even number.

2. In the initial formulation of the _n_-Queens Problem, after the queen is placed in position (_i,j_), the following actions are performed:

a) exclude all cells of row i and column j

b) all cells that are located on the line of the left and right diagonals passing through the cell (_i,j_) are excluded.

We change condition b) in the statement of the problem. Instead of eliminating cells, we will use cell switching. If the cell located on the line of the left or right diagonals is free, then we will close it; if the cell is closed, then we will open it. This makes it easier to find a solution. However, instead of a square matrix \(n\times n\), we consider a rectangular matrix of size \(n\times(n-k)\). It is required, for a given value of _n_, to find the maximum value of _k_ at which at least _h_ orthogonal solutions can be obtained(h=3,4,5). How will the value of _k_ change with increasing value of _n_?

