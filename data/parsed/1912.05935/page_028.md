is due to the fact that, within the limits set by the search parameters, the algorithm can’t find the right way to complete such compositions. As the experimental results show, the number of such cases does not exceed 0.0001 of sample size, and this error decreases with increasing _n_. In addition, for all values of _n\>_800, there was not a single case of False Negative solution. Even increasing the sample size to one million for a value of _n_=1000 did not lead to the appearance of a False Negative solution. The obtained result allows us to formulate the following rule for solving the posed problem: "Any random composition of _k_ queens that are consistently distributed on an arbitrary chessboard of size \(n\times n\) can be completed in linear time, or it will be decided that this composition is negative, and have not solution. The probability of an error in making such a decision does not exceed the value of 0.0001 from the sample size. With the increasing the size of the chessboard, the likelihood of making erroneous decisions decreases."

## 8 Conclusions

1.An algorithm is described which allows solving in linear time the _n_-Queens Completion problem for an arbitrary composition of k queens, consistently distributed on a chessboard of size \(n\times n\). Moreover, for any composition of _k_ queens (\(1\le k<n\)), a solution is provided, if any, or a decision is made that this composition can’t be completed. The probability of an error in making such a decision does not exceed 0.0001, and this value decreases with increasing size of a chessboard.

2. The operation of this algorithm is based on the use of two important rules:

a) At the solution final stage, from all the remaining free rows, one is selected for which the number of free positions is minimal ( **minimum risk rule**). This minimizes the risks associated with the possibility of excluding the last free positions in some of the remaining rows.

b) From all free positions in the row, the position is selected that causes minimal damage to the free positions in the remaining free rows (**minimum damage rule**). By "minimal damage" is meant the selection of such a position in a row that excludes the least amount of free positions in all remaining free rows.

3. It is established that, the average time required for the queen to be placed on one row decreases with increasing value of _n_. The average time required for the queen to be placed on one row in the case when _n_=10<sup>8</sup> is 21 times less than the corresponding time for the case _n_=50.

