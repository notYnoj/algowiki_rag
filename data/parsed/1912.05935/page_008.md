in each of these five blocks.

## 4.3 Beginning of the algorithm

Data is entered and the composition is checked for correctness. At each verification step, the cells of the control arrays are changed. A count of the number of correctly installed queens is kept. If there are no errors in the composition, the solution continues, otherwise an error message is displayed. After verification is complete, copies of the main arrays are created for their reuse at this level. After that, control is transferred to _Block_-1.

## 4.4 Block-1

The beginning of the formation of the search branch. We consider _k_ queens located on a chessboard as a starting position. It is required to continue to complete this composition and place the queens on a chessboard until their total number is equal to _baseLevel_<sub>2</sub>. The algorithm used here is called _randSet_ & _randSet_. This is due to the fact that here we are constantly comparing two random lists of indices, in search of pairs free from the corresponding diagonal restrictions. To do this, the following actions are performed:

a) two lists are formed: a list of free row indices and a list of free column indices;

b) perform random permutation of numbers in each of these lists;

c) in a loop, each consecutive pair of values (_i,j_), where index (_i_) is selected from the list of free row indices and index (_j_) from the list of free column indices, is considered as a potential queen position, and it is checked whether this position in the projection area of diagonal exceptions.

If the rule of diagonal exceptions is not violated, then the position is considered correct, and the queen is placed in this position. After that, the counter for the number of correctly installed queens is incremented, and the corresponding cells of the control arrays are changed. If the position (_i,j_) falls into the zone of diagonal restrictions formed by the queens established earlier, then nothing changes and the transition to consideration of the next pair of values takes place. When the comparison cycle of all pairs is completed, based on the remaining indices, a list of indices of the remaining free rows and free columns is again formed, and this procedure is repeated until the total number of correctly placed queens (_totPos_) is equal to or exceeds the limit value of _baseLevel_<sub>2</sub> . Once this condition is met, control is transferred to _Block_-2. If it turns out that as a result of the search, a<tbc>

