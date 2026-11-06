(1,1) should be white. All cells at the beginning of the game are considered free. One player places white queens, the other blacks. The player places the queen on an arbitrary free cell with indices (_i,j_). Each player can make a move on both white and black cell. White queens make the first move. Let it be a white cell. As a result of this choice, the following cells are closed:

a) all white cells of row _i_;

b) all white cells of column _j_;

c) all white cells that lie on the left and right diagonals passing through the cell (_i,j_).

If the cell (_i,j_) turns out to be black, then all items a), b), c) are satisfied, and accordingly, all the cells in black are closed. Further, Black performs the move, placing the queen on any of the remaining free cells. After that, in a similar way, the cells close, as described above. The time to think about the next move is fixed, and is selected by agreement of the parties. If during the specified time, one of the players does not complete his move, then the game is transferred to the other. The game ends if both players do not have a decision to complete the move. The one who can place more queens on the board wins.

9. The stability of random selection. Consider the _randSet_ & _randSet_ model. As a result of comparing _n_ random pairs of row and column indices, at the first stage of the cycle, the queen can be established on average on \(k\times n\) rows. The value of _k_ can be considered as a constant value equal to 0.6. Its value varies from 0.605701 at _n_=10, and to 0.599777, at _n_=10<sup>6</sup>, and, with an increase in _n_, the dispersion around the average value decreases. What is the reason for such "constancy"? Why, with a random selection of the row index and the position index, on the basis of two lists of randomly rearranged numbers, it is possible to consistently place 60% of queens?

10. Let the size of the chessboard be \(n\times n\). Based on the _randSet_ & _randSet_ procedure, we place the queens on the chessboard until the search branch reaches the dead end. If, for a given value of _n_, repeat this procedure many times, and construct a histogram of the distribution of values of _k_, it turns out that the change of events frequency to the value of the distribution mode differs from the change of events frequency after this value. If, based on the modal value, the histogram is divided into two parts, then the left part will not coincide with the right part. This pattern is characteristic for any value of _n_. Why, after the transition of the length of the composition through the modal value, does the frequency of events take a different form? By event, we mean the formation of a composition until a deadlock state is

