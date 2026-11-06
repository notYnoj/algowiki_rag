<tbc>cupancy of the columns of the solution matrix. Set to zero these three arrays.

2. We introduce the counter of the number of correctly installed queens (_totPos_=0). Consistently, in a cycle, starting from the first row, we consider all the queens positions provided. If _Q(i)\>_0, then based on the index of row _i_ and the index of the position of the queen in this row _j=Q(i_), we form the corresponding indices for the control arrays _D_1(_r_) and _D_2(_t_):

\(r=n+ji\)<br>
\(t=j+i\)

3. If all conditions _D_1(_r_)=0, _D_2(_t_)=0, _B(j_)=0 are satisfied, this will mean that the cell (_i,j_) is free and does not fall into projection zone of diagonal restrictions formed by previously established queens. Placing the queen in this position is correct. If at least one of these conditions is not fulfilled, then the choice of such a position will be erroneous, and the solution will be erroneous.

4. If the solution is correct, then we increment the counter of the number of correctly installed queens and close the corresponding cells of the control arrays: (_totPos=totPos_+1, _D_1(_r_)=1, _D_2(_t_)=1, _B(j_)=1). Thus, we close all cells of the column (_j_) and those cells of the solution matrix that are located along the left and right diagonals intersecting in the cell (_i,j_).

5. Repeat the verification procedure for all remaining positions.

Perhaps, this is one of the fastest algorithm for validation the _n_-Queens problem solution. The verification time of 10<sup>6</sup> positions on the desktop-13 is 0.175 seconds. Which corresponds to the time to press the Enter key.

## 4 Algorithm description

The _n_-Queens Completion problem is a classic non-deterministic problem. The main difficulty of its solution is connected with the question of selecting the row index and position index in this row, in conditions when the state space is huge. When searching for all possible solutions, such a problem does not arise, we must consider all valid search branches in the state space, and the order in which they are considered does not matter. However, when an arbitrary composition of _k_ queens needs to be completed, then in this case we need an algorithm for selecting row and column indices that adequately perceives the existing composition and leads to a solution faster than others. In this project, we decided the question of choice on the basis of the follow<tbc>

