**Example:**

Let _asc=true_, \(a=[1.75,1.25,-2.5,-\infty]\) and, for sake of brevity and clarity, let’s assume that 6 bits are used to store a single floating-point value: 1 for the sign bit, 3 for the exponent (so bias is 3), and 2 for the mantissa; then _a_=[001111<sub>2</sub>,001101<sub>2</sub>,110001<sub>2</sub>,111100<sub>2</sub>], and the tracing of _bsortFloat(a,asc_) is shown in Figure 4.

## IV. ANALYSIS

### A. Theoretical analysis

**Theorem 4.** _The bsort algorithm sorts an array of n elements with a word size w in O(nw_) _time._

_Proof._ The algorithm’s execution time is governed by the bitwise partitioning of the input.

\(\bullet\) Per-bit pass: For each bit \(b\in\{0,\dots,w-1\}\), the algorithm performs a single partitioning pass (e.g., _singlePassBSort_). This pass involves a linear scan of the current partition. Each element in the partition is inspected exactly once to check the value of its _b_-th bit, resulting in _O(n<sub>p</sub>_) operations, where _n<sub>p</sub>_ is the number of elements in the current sub-partition.

\(\bullet\) Total work per level: At any depth _d_ of the recursion tree (corresponding to a specific bit), the sum of all elements across all partitions is exactly _n_. Therefore, the total work performed at each level of the recursion is _O(n_).<tbc>

\(\bullet\) Total depth: Since the algorithm recurses on the bit-width of the data, the recursion tree has a maximum depth of _w_.

Summing the work across all _w_ levels:

\(T(n)=\sum_{b=1}^wO(n)=O(nw)\) (2)

As _w_ is constant for a given data type (e.g., _w_=64 for doubles), the runtime asymptotic behavior is linear with respect to the number of elements _n_, though formally expressed as _O(nw_) to account for bit-depth.

**Theorem 5.** _The bsort algorithm operates with O(w_) _auxiliary space_

_Proof._ This is established by two factors:

\(\bullet\) In-place partitioning: The partitioning step (e.g., _singlePassBSort_) utilizes a two-pointer approach to swap elements within the original input array. This requires only a constant amount of auxiliary space, O(1), for temporary swap variables and pointers.<tbc>

\(\bullet\) Recursion depth: The algorithm performs a bitwise decomposition. For a word size of _w_ bits, the recursion tree has a maximum depth of _w_. Each stack frame stores a constant number of variables (pointers and bit masks). Therefore, the stack space consumed by recursive calls is _O(w_).

As the algorithm does not allocate additional data structures proportional to the input size _n_, and the stack depth is bounded by _w_, the total auxiliary space complexity is _O(w_). So, we can consider _bsort_ to be an in-place with respect to _n_ algorithm.

### B. Empirical analysis

Introsort was selected as baseline for comparison given its status as the standard implementation in the C++ STL (std::sort). To evaluate `bsort` against modern state-of-the-art techniques, spreadsort and radix sort (ska\_sort) were included, both of which share a non-comparison-based architecture. While the standard C `qsort` implementation was initially considered, it was excluded from the final results due to consistently underperforming all other evaluated algorithms. This disparity arises primarily because `qsort` utilizes function pointers for comparisons, which inhibits the compiler from performing effective inlining and optimization, even at high optimization levels (`-03`) \[6\].

The case of `qsort` serves as a salient example of the potential divergence between theoretical asymptotic behavior and practical performance; while its asymptotic bounds are well- established, architectural overheads and compiler limitations can significantly hinder its real-world efficiency.

A comparison of algorithms’ properties can be found in  I.

1.75
1.25
-2.5
-0
m
001111
001101
110001
111100
100000
sort by sign
-2.5
-0
1.75
1.25
m
110001
111100
001111
001101
010000
k1
-2.5
-0
1.75
1.25
m
110001
111100
001111
001101
k1
-0
-2.5
1.75
1.25
m
111100
110001
001111
001101
k3
k1
sort by exponent
-0
-2.5
1.75
1.25
m
111100
110001
001111
001101
000010
k3
k1
-0
-2.5
1.25
1.75
m
111100
110001
001101
001111
000001
k3
k1
k5
sort by mantissa

Fig. 4: Tracing of bsort for floating-point values. For clarity, only relevant partition indexes (_k_<sub>1</sub>, _k_<sub>3</sub>, _k_<sub>5</sub>) were illustrated.

