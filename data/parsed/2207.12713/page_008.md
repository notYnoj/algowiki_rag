<tbc>form some operations, such as joining or filtering. The functionality to retrieve values via positions in PosDB is provided by auxiliary entities called readers \[3\]. There are several types of readers, for example, ColumnReader, PartitionReader, SyncReader. ColumnReader retrieves values of a specified attribute locally, PartitionReader retrieves values of a specified partition either locally or remotely. SyncReader is a composite reader that manages several simpler ones to extract the values of several attributes synchronously. Readers, in turn, use access methods \[10\] to provide their functionality.

Thus, PosDB is able to emulate row-based systems by exploiting early materialization. Such emulation was used to experimentally evaluate the implemented external sorting algorithms.

## 4.2 Operator Implementation

External sort is implemented as a separate operator in the Volcano model. There are several external sort operators in PosDB:

1. **Position-based value sort**. In this case, the operator accepts join index as input and has to obtain values since it needs them for sorting.<tbc>

2. **Position-based position sort**. Input is the same, but in this case the operator does not need values, since it sorts positions.<tbc>

3. **Tuple-based**. This is the classic sort, where operator accepts blocks of tuple data and sorts them. Since in PosDB tuple-based representation lacks positions, it is a value sort.

Position-based value sort operator may be beneficial for late materialization (and therefore interesting for further research), since it sorts key-position pairs similar to unclustered (tag) sorting, which is stated \[24\] to be more efficient on SSD if tuples are big enough. However, it is beyond the scope of this paper.

Source Data
Join Index
T1
T2
T3
T1
T2
T3
row1
X11
X21
row1
Y11
Y21
Y31
row1
Z11
Z21
+
1
2
3
row2
X12
X22
row2
Y12
Y22
Y32
row2
Z12
Z22
2
1
2
row3
X13
X23
row3
Y13
Y23
Y33
row3
Z13
Z23
3
3
3
Resulting records
T1
T2
T3
X11
X21
Y22
Y32
Z13
X12
X22
Y21
Y31
Z12
X13
X23
Y23
Y33
Z13

Fig.2: Example of join index and its usage

