<tbc>is beneficial and considerably speeds up sorting even in the case when disk is expected to be a bottleneck, 2) loser tree provides the best performance.

### 6 Threats to validity

First of all, we would like to note that the behavior of the external sort operator (and specifically, the number of runs to merge) heavily depends on its available amount of memory. Performance of the merge step is determined by the number of performed comparisons, which is directly affected by the number of runs to merge. The less the number of runs to merge, the less noticeable will be the impact of a more efficient minimum element selection algorithm. For example, if the table to be sorted is two times larger than the memory available to the operator, then there will be two (or three) runs and speeding up the selection of minimal value will not bring any benefit.

We have considered a particular case when a DBMS sorts pointers to data values. It is stated [9,16] that sorting \(\langle\)key prefix, pointer\(\rangle\) pairs is generally more efficient and speeds up the comparisons themselves, which leads to an increase in the intensity of disk I/O operations. Thus, total performance gains obtained from a specialized data structure may not be as significant. The same may be true for other advanced record representation and comparison techniques.

Next, in our study we consider SSDs and not HDDs. For a DBMS running on HDD, the ratio of CPU and disk expenses will be different since modern HDDs are much slower than SSDs. Therefore, the obtained speedup of the merge step may be lost to slow disk reads. In this case, reducing the number of comparisons via implementing a specialized data structure may not improve the overall performance that much.

In this paper, we have considered a single-threaded version of external sort. In the case of multi-threaded operator, the validation of our results would require a separate (and extensive) study since: 1) we would need to take into account the behavior of our data structure in case of multiple threads (e.g., cache pollution may happen), 2) disk could become the bottleneck and thus no prospective CPU gains would improve the overall performance.

Finally, we focused on commodity PCs, and modern high-end servers would require a separate study as well.

### 7 Acknowledgements

We would like to thank Anna Smirnova for her help with the preparation of this paper.

### 8 Conclusion

In this paper, we have considered the design of a comparison-based sort and evaluated the choice of the data structure used on the merge step for implementing

