<tbc>the external sort operator in DBMSes. First, in our review of the related work, we demonstrated that no study has yet touched on the problem of selecting a data structure for run merging in external sort for DBMSes. After that, we posed several related research questions. To answer them, we have implemented three different approaches and experimentally evaluated them using the PosDB query engine. As the result, we have shown that a loser tree is the most efficient method for run merging.

Thus, we have demonstrated that even without complex I/O optimizations, such as disk striping, parallel I/O using `mmap`, elegant read ahead techniques, etc., the algorithm that selects the smallest element at the merge step has a noticeable impact on the performance of external sort. Therefore, it is worthwhile to make an effort to implement an efficient data structure for run merging on modern commodity computers. With the mentioned optimizations applied, the influence of the algorithm will only increase, since I/O operations become more efficient, which means there will be more computational load on the CPU.

## References

