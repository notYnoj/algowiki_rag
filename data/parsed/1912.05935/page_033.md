3. Change some conditions in the initial formulation of the _n_-Queens Problem. When the queen is placed in position (_i,j_) on a chessboard of size \(n\times n\):<br>
a) Exclude all cells in row _i_.<br>
b) If index _j_ is an even number, then<tbc>

<tbc>b1) exclude cells in even rows of column _j_,<tbc>

<tbc>b2) exclude cells in even lines intersecting with the left and right diagonals passing through the cell (_i,j_).<br>
c) If index _j_ is an odd number, then points b1) and b2) are satisfied for cells located on odd rows.

3.1 It is known [7], that the list of values of all solutions of the nQueens Problem, for _n_=(8, 9, 10, 11, 12, 13, 14, 15, 16), respectively, is (92, 352, 724, 2680, 14200, 73712, 365596 , 2279184, 14772512). How will the number of all solutions change if, in the statement of the problem, the standard condition for diagonal exceptions is changed to paragraph b) or paragraph c)?

3.2 It is known [6], that if we determine the frequency of participation of various cells of the solution matrix in the formation of a list of all solutions, we can find that there are harmonious relationships between all cells in the form of vertical and horizontal symmetries of the corresponding frequencies. This means that, if we assume that _k\<n/_2, then the frequency of the cells of the _k_-th row will be identical to the frequencies of the cells of the row _n-k_+1. Similarly, the frequency of the cells of the _k_-th column will be identical to the frequencies of the cells of the column _n-k_+1. Question: How will these harmonious relations change in the context of the task?

4. All cells of a chessboard are divided into two classes by their color. It is believed that one color is white, the other is black. Consider two chessboards and place one of them on the other so that the edges coincide completely. As a result, we get a "sandwich" of two chessboards in which the arrangement of white and black cells coincide. The task is to find h mutually orthogonal solutions that are located on the first or second board (_h_=3,4,5_,..._), observing the following conditions:<br>
a) If in one of the boards the queen is located on a black cell with indices (_i,j_), then:

a1) on this board:<tbc>

