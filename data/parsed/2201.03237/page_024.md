to prevent over large out-degree. Both the search efficiency and precision are greatly affected by the average out-degree. When the average out-degree is too large, the precision will be higher but the search efficiency may decline. The average out-degree of TBSG is slightly higher than that of HNSW and NSSG, however, with the same precision the efficiency of TBSG is higher than that of HNSW and NSSG, indicating that TBSG can achieve a better trade-off between precision and efficiency.<tbc>

2. The index time of TBSG is very close to that of NSSG, which is the lowest except for KGraph. For large-scaled datasets, it is very necessary to reduce index cost to improve the availability.<tbc>

3. Index size refers to the size of the index stored on the disk. The index size of TBSG is smallest except NSSG.

## 4.3. Parameters

The parameters to build TBSG are as follows: the size of neighbors in KNNG _K_, the maximum of the out-degree _m_, the threshold of _min.prob mp_, the distance between query point and nearest neighbor _r_.

Generally speaking, it is harder to perform ANNS query in the dataset with a larger LID. Therefore, it needs more candidate neighbors and larger out-degree. The value of _K_ increases with LID, ranging from hundreds to thousands. The larger the value of _K_, the more time it takes to build the index, and the more accurate the search result will be. The _m_ is set to prevent the over large out- degree. The value of _m_ is always within one hundred.

There are two most important parameters in TBSG: _r_ and _mp_. The value of _r_ can vary widely between different datasets, or between different nodes in the same dataset. Therefore, we consider two methods to determine the value of _r_: static and dynamic. The static method is that for each node \(v_i\in D\), we select a fixed value _r<sub>i</sub>_. The value of _r<sub>i</sub>_ is equal to the distance between _v<sub>i</sub>_ and its nearest neighbor in _D_. The dynamic method is approximating _r_ as _l_, the meaning of which can be seen in inequation (2). In most experiments, we find<tbc>

