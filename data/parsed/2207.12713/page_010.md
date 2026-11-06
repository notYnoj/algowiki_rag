<tbc>Contest (in which external sorting was one of the challenges) used it. Among them, two solutions implemented some kind of radix sort for in-memory sorting, other two implemented Quicksort with various optimizations and Leyenda implemented a hybrid approach. Despite the fact that the Radix sort is the most efficient sorting algorithm for some specific data types (e.g. integers), it is difficult to implement it as a general-purpose algorithm for sorting arbitrary data.

During the run merging stage, it is necessary to select the smallest element among the frontmost tuples of runs being merged. It can be done using various approaches, and we implemented and experimentally evaluated three, namely: 1) naive, 2) using the tree of losers data structure, and 3) using a binary heap. All disk operations are buffered via basic `std::fstream` buffers.

**Naive.** The naive approach is straightforward and does not use an auxiliary data structure. It simply iterates over first tuples of input runs and selects the smallest ones. The selected tuple is then flushed to the output tape and replaced with the next tuple from its corresponding run.

**Binary heap.** This approach maintains a binary heap in memory to speed up finding the smallest element. First, it constructs the binary heap and fills it with pointers to the first tuples of runs. Second, it removes the root from the heap and flushes tuple pointed to by the root to the output tape. It then reads the next tuple from the run of the previously removed tuple and inserts a pointer to it to the heap.

**Loser tree.** This is the same approach as with a binary heap, but instead of a heap, a loser tree [13] data structure is used.

## 5 Experiments

To evaluate and compare the performance of the implemented algorithms in a DBMS environment, we have performed the following experiments:

1. Comparison with PostgreSQL in order to "validate" the quality and correctness of our implementation;<tbc>

2. Evaluation of the three approaches on the synthetic Star Schema Benchmark [17];<tbc>

3. Evaluation of the three approaches on a real dataset, namely, TripData [23].

Experiments were performed using the following hardware and software configuration:

– Hardware: Intel Core i5-7200U CPU @ 2.50GHz \(\times\) 4, 8 GiB RAM, 240GB KINGSTON SA400S3;<tbc>

– Software: Ubuntu 20.04.4 LTS x86\_64, Kernel 5.13.0-40-generic, gcc 9.4.0, PostgreSQL 12.10.

For the first two experiments, we decided to use a simple query with an `ORDER BY` clause over the `lineorder` table from the Star Schema Benchmark. SSB was

