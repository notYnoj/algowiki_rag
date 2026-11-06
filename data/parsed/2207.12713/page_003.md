<tbc>algorithm can be either comparison-based or partition-based. Algorithms of the partition-based class distribute input tuples into buckets using several pivot values (selected by the algorithm) while ensuring the following properties:

- each bucket covers some data range,<tbc>

- all data ranges do not overlap,<tbc>

**-** a union of all data ranges covers the whole range.

Then the algorithm sorts the contents of individual buckets and in doing so it is ensured that each bucket fits into memory. The result is an ordered sequence of buckets, each containing a sorted range.

The partition-based sorting algorithm has two degrees of freedom: the algorithm that sorts the buckets in memory and pivot selection.

Comparison-based algorithms generate sorted runs (i.e., in this case, data ranges intersect) and then merge them into one long run. They consist of two stages: run generation and run merging. These stages can be either completely independent and consecutive, or alternate (known as oscillating sort [13]). Consequently, there are two approaches to run generation:

1. Read tuples from disk for as long as there is enough available memory; sort these tuples using some internal sorting algorithm;<tbc>

2. The algorithm maintains a data structure in memory with a priority queue interface. On each iteration the lowest value from the data structure is retrieved and moved to a buffer or written to the disk. Then algorithm inserts the next value from the input data into the data structure. If the next value is smaller than the last retrieved, it should be marked as belonging to the next run. When the data structure contains only such marked values, the current run is treated as completed. After this, the new one is started. This method is known as the replacement selection [13]. The tournament tree [13] can be used to implement this method.

The second approach was more popular in the past. On average, it generates runs that are twice the size of available memory, which can be useful in a memory-constrained environment. Nowadays, available RAM sizes have grown significantly and the Quicksort became more popular.

In the past, tapes were used instead of disks for persistent storage. Of course, there can be more runs than tapes. Different algorithms exist to merge runs and distribute them over tapes, e.g. multiway merge, polyphase merge, cascade merge, etc. These algorithms are called merge patterns. Disks are the ubiquitous storage type nowadays, but the concept of tape as an abstraction can still be useful in order to save disk space by reusing input tapes as output tapes. This technique is still used in industrial systems.<sup>4</sup>

In addition to the merge pattern, comparison-based sorting algorithms differ in the algorithm for selecting the smallest value among the first elements of the

<sup>4</sup> `https://github.com/postgres/postgres/blob/REL\_14\_STABLE/src/backend/ utils/sort/tuplesort.c`

