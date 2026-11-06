\(\text{\textbf{Algorithm.
1. For each segment}}i\in[p]\text{in parallel:
(a) Call}\mathsf{key}_i^*:=\text{\textbf{FindDominant}}(A_i,K,|A_i|)\text{;
(b) Count the number of occurrences of}\mathsf{key}_i^*\text{in}A_i\text{to decide if}A_i\text{is}(1-\eta)\text{-uniform.
(c) If}A_i\text{is}(1-\eta)\text{-uniform, mark the following elements as "\textit{misplaced}": 1) all elements whose key differ from}\mathsf{key}_i^*\text{; and 2) exactly}\lceil\eta m\rceil\text{number of elements with the dominant key}\mathsf{key}_i^*\text{.
Else, mark all elements in}A_i\text{as "\textit{misplaced}".
2. All elements in}A\text{calculate which segment it falls in -- note that all elements can learn its position within}A\text{through an all-prefix-sum calculation, and the segment number can be calculated from the element’s position within}A\text{.
Call oblivious compaction to move all elements in}A\text{marked with "\textit{misplaced}" to the front of the array, and all other elements to the end; all elements carry their segment number in the process. Let the outcome be called}X\text{.
3. Call \textbf{SlowAlign}}^{K,K^2}(X[1:3n/K^2])\text{on the first}3n/K^2\text{elements of}X\text{, where the first}2k\text{-bits of each element’s segment number is used as the idx field in the \textbf{SlowAlign} algorithm.
4. Invoke the reverse routing algorithm of the compactor in Step 2 on the outcome of the previous step, and let}Y\text{be the outcome.
5. We will now divide}Y\text{into}K^2\text{super-segments instead where each super-segment is composed of}K\text{original segments. Write}Y:=Y_1||Y_2||\dots||Y_{K^2}\text{as the concatenation of}K^2\text{equally sized super-segments. For each}i\in[K^2]\text{: check if}Y_i\text{has multiple keys; if so, label the super-segment as "\textit{multi-key}".
6. Invoke an oblivious compaction algorithm to move all the super-segments marked "\textit{multi-key}" to the front of the array (here the compaction algorithm treats each super-segment as an element). Let the outcome be}Z\text{.
7. Now, for each of the beginning}K\text{super-segments of}Z\text{in parallel (where each super-segment is}n/K^2\text{in size), use \textbf{SlowSort}}^K\text{to sort within each super-segment.
8. Finally, reverse route the outcome of the previous step by reversing the decisions made in Step 6, and output the result.}\mathsf{key}_i^*\mathsf{key}_i^*\mathsf{key}_i^*\)

**Remark 2.** In the above algorithm, Steps 1b and 1c can be performed obliviously as follows:

• The counting in Step 1b can be performed by aggregating over a binary-tree of depth _O_(log_n_).<tbc>

• If the segment _A<sub>i</sub>_ is not \((1-\eta)\)-uniform: all elements in _A<sub>i</sub>_ label itself as "\textit{misplaced}" (else all elements in _A<sub>i</sub>_ pretend to write a label for obliviousness).<tbc>

• Else, every element whose key differs from the dominate key \(\mathsf{key}_i^*\) marks itself "\textit{misplaced}"; moreover, using a generalized binary-to-unary conversion algorithm, the first \(\lceil\eta m\rceil\) elements with the dominant key \(\mathsf{key}_i^*\) label itself as "\textit{misplaced}". All remaining elements pretend to write a label for obliviousness.

**Correctness.** We will now argue correctness of the above algorithm, i.e., that the result is fully sorted as long as the input array is (2<sup>-8_k_</sup>,2<sup>3_k_</sup>)-orderly. Since there are at most _K_ distinct keys, it<tbc>

