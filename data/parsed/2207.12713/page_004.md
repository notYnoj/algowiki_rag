<tbc>merged runs. The naive approach, and therefore the asymptotically slowest, is to check all candidates. A more efficient approach here is to use a data structure that speeds up finding the smallest element. For this purpose, a heap or a tournament tree (either loser or winner) are the most common choices.

## 3 Related Work and Motivation

### 3.1 Related Work

Over the years, there has been a lot of research on external sorting. The algorithmic theoretical aspects of external comparison-based sorting are very well understood. That is, in-memory sorting algorithms, run merge algorithms and the appropriate data structures for single-processor environment are known and have not largely changed over time since Knuth’s survey [13]. Most of the current research in non-distributed external sorting is focused on efficient implementation of an algorithm on modern hardware, i.e., implementing sorting that fully utilizes all available hardware capabilities. The two most popular concerns are how to utilize caches efficiently and how to mitigate disk bandwidth limitations. More generally, one can classify the most of the current research papers on external sorting as follows:

– techniques to improve sorting performance by using hardware resources more efficiently, namely:<tbc>

• CPU and caches<tbc>

• HDD/SSD<tbc>

• GPU<tbc>

– novel external sorting algorithms that make heavy use of parallelism;<tbc>

– distributed external sorting algorithms.

In the paper [16] authors describe the AlphaSort algorithm. It was designed with memory hierarchy in mind and therefore exhibits cache-friendly behavior. The Quicksort is used for in-memory sorting since: 1) it has better cache locality and is less CPU-intensive than the replacement-selection, and 2) modern computers have enough RAM to produce sufficiently long runs. Runs are merged using a tournament tree. The authors compare different approaches to storing tuples during sorting and merging. Possible alternatives are: sort tuples itself, sort pointers to tuples, sort pairs of key and pointer, sort pairs of key prefix and pointer. The authors conclude that sorting the tuples itself can be faster if tuples are short enough. Otherwise, sorting the tuple-pointer and key-prefix pairs is most efficient. A parallel version of the algorithm for multiprocessor systems is also presented.

The authors of the study [19] focus on external sort operator in memory- inconsistent environment. They consider real-time or goal-oriented DBMSes where the available memory for a query (or transaction) may change on-the-fly due to other concurrent transactions. It may either be shrunk since some higher priority transaction requires more memory, or increased because some transaction has<tbc>

