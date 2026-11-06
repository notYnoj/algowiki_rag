placed is equal to the value of _baseLevel_<sub>3</sub>. Once this condition is met, control is transferred to _Block-_4. If, as a result of the calculations, the search branch is deadlocked, then this search branch is closed and a return is made to the beginning of event 3, from where the calculations are repeated again. For this, the initial values of all control arrays are restored.

## 4.7 Block-4

In this block, data is prepared for the transfer of control to _Block-_5. To this step, after completing the procedure in _Block-_3, the number of free rows (_nRow_) has become even less. Therefore, it is also beneficial to transfer events from a larger array to a smaller array. This approach gives us the opportunity to quickly determine the necessary characteristics for the remaining rows that we need at this stage. Of particular importance is the fact that on the basis of such an array, it is possible to predict the prospectivity of the search branch for many steps forward without having to complete the calculations. The condition is quite simple. If it turns out that among the remaining free rows there is a row in which there is no free position, then the search branch under consideration is closed and control is transferred to one of the lower-level blocks. The preparatory actions carried out here are in many respects similar to what was done in _Block-_2. Based on the original indices of free rows and free columns, a new 2-dimensional array is formed, the zero values of which correspond to free positions in the original solution matrix. In addition, a special array _E_(1: _nRow_, 1: _nRow_) is created in this block, based on which we can determine the number of free positions in the remaining free rows that will be closed if we select the position (_i,j_) to set the queen in solution matrix. Before transferring control to _Block-_5, the following actions are performed:

a) the amount of free positions in all remaining rows is determined

b) the array of free positions, for the considered rows, is ranked in ascending order

c) if all the remaining free rows have free positions (i.e. the minimum value in this ranked list is different from 0), then control is transferred to _Block-_5. If it turns out that in any of the remaining rows there is no free position, then the necessary arrays are restored based on the stored copies, and, depending on the parameters of the task, control is transferred to one of the basic levels.

d) backup copies of all control arrays for this 4th level are formed.

