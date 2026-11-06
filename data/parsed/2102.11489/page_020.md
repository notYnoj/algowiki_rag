## 5 Sorting Short Keys on an Oblivious PRAM

Throughout, we assume that the array _A_ to be sorted contains elements that are (key, payload) pairs. A key can be expressed in _k_ bits, and the entire element can fit in _O_(1) memory words.

### 5.1 Slow Sorter and Slow Alignment

**Slow sorter.** We show that there is a slow sorter that sorts an array containing _n_ elements with _k_-bit keys in \(O(2^k\cdot n)\) work and _O_(log_n_) depth.

**Theorem 5.1** (Slow sorter)**.** _Let K_:=2_<sup>k</sup>. There exists a deterministic, oblivious algorithm, henceforth denoted_ **SlowSort**_<sup>K</sup>(A), that can correctly sort any input array A of length n and containing elements with k-bit keys in O(nK_) _total work and O(k_+log_n_) _depth._

_Proof._ Consider the following algorithm:

\(\text{\textbf{SlowSort}}^K(A)\text{\textbf{Input: An array}}A\text{whose length}n\text{is a power of 2. Every element in}A\text{has a}k\text{-bit key chosen from the domain}[0,K-1]\text{.
\textbf{Algorithm:} 1. For each}u\in[0,K-1]\text{in parallel, count the number of occurrences of the key}u\text{in}A\text{, and let}c_u\text{be this count. Using an all-prefix-sum algorithm, compute}s_u:=\sum_{i\in[0,u-1]}c_i\text{for every}u\in[1,K-1]\text{, and define}s_0:=0\text{. 2. Make}K\text{copies of the array}A\text{, denoted}B_0,\dots,B_{K-1}\text{, respectively. In each}B_u\text{, the elements whose keys are not}u\text{are replaced with}filler\text{. 3. For}u\in[0,K-1]\text{: (a) In array}B_u\text{, for the first}s_u\text{filler elements, treat their keys as}-\infty\text{; for every other filler element, treat its the key as}\infty\text{. This can be accomplished by invoking a generalized binary-to-unary conversion algorithm. (b) Invoke oblivious sorting for ternary keys to sort}B_u\text{. In the resulting array denoted}B'_u\text{, the elements whose keys are equal to}u\text{will appear at positions}s_u+1,\dots,s_{u+1}\text{. 4. In parallel, populate the}i\text{-th element in the output array for every}i\in[n]\text{as follows: select the element whose key is within the range}[0,K-1]\text{among the elements}B'_0[i],B'_1[i],\dots,B'_{K-1}[i]\text{. The selection can be accomplished by aggregating over a binary tree whose leaves are}B'_0[i]\text{,}B'_1[i]\text{,}\dots\text{,}B'_{K-1}[i]\text{.}\)

One can easily verify that the above algorithm indeed correctly sorts in the input array. Moreover, its total work is bounded by _O(nK_) and its depth is bounded by _O(k_+log_n_). Specifically, for the depth, the _O(k_) part upper bounds the depth of the first step that computes the all-prefix-sum of _K_ elements as well as the last step where we select among _K_ elements; and the _O_(log_n_) part is an upper bound on the depth of the generalized binary-to-unary computation, as well as the ternary-key sorting.

**Remark 1** (Reverse routing)**.** In the above **SlowSort** algorithm, there is a way to reverse-route elements in the output array back into their original positions in the input. Suppose that during<tbc>

