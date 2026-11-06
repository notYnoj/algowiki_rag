<tbc>The same is true regarding the position-based position sort. Sorting positions is essential for addressing the out-of-order probing problem inherent for column- stores [1].

The focus of this paper is the latter, classic variant of external sorting -- the tuple-based operator. It implements a comparison-based external sorting algorithm on tapes with the Introsort [15] for run generation and polyphase merge [13] for run merging. The algorithm works as follows:

1. Calls `GetNext()` of child operator until all available memory is filled;<tbc>

2. Sorts collected tuples in-memory using `std::sort` implemented as Introsort;<tbc>

3. Using the polyphase merge pattern, selects the abstract tape to which the current run will be flushed;<tbc>

4. Flushes current run to the selected tape;<tbc>

5. Repeats steps 1-4 until input is fully processed;<tbc>

6. Merges runs from the tapes according to the polyphase merge pattern until there is only one run left.

The implemented external sort tuple-based operator sorts pointers to tuples, not tuples themselves. Even though run merging can be efficiently performed in a single pass in many simple queries, multilevel merge may still may be necessary to efficiently execute a complex query plan, e.g. a plan with several sort and hash operations [9]. Taking this into account, it was decided to implement abstract tapes to store runs. Run merging (and distributing over tapes) is performed using polyphase merge, which, however, falls back to ordinary multiway merge when there are more tapes than runs. Abstract tapes can also be used to efficiently reuse disk space during the merge stage, as is done in PostgreSQL.<sup>5</sup>External sort operator completely bypasses PosDB buffer manager and writes generated runs directly to the disk, it is essential [9] for optimized I/O. Introsort was chosen for the in-memory sorting algorithm for the same reasons that make Quicksort superior [16] to the replacement selection, namely:

1. Quicksort results in far fewer cache misses, which is very important for the performance of modern CPUs;<tbc>

2. Quicksort is less CPU intensive;<tbc>

3. With today’s main memory sizes, there is no need for runs to be twice the amount of available memory (this is what made the replacement selection very attractive in the past);<tbc>

4. With Quicksort (or any other in-place sorting algorithm) it is possible to copy each record only once during run generation stage, while replacement selection needs at least two copy operations [9].

For all of these reasons, replacement selection is widely considered obsolete, and PostgreSQL abandoned it in favor of the Quicksort algorithm a few years ago. Also, none of top five solutions in the ACM SIGMOD 2019<sup>6</sup> Programming

<sup>5</sup> See footnote 4. <sup>6</sup> `http://sigmoid19contest.itu.dk/`

