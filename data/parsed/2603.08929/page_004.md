If the algorithm sorts by exponent first, it will incorrectly imply that _z\<x_ because _p<sub>z</sub>\<p<sub>x</sub>_ (-1_\<_0). The initial partitioning by exponent yields two partitions, in the following relative order: [_z_] and [_x,y_]. Since _z_ is isolated in its own partition, no subsequent recursion on mantissa or sign can correct its position relative to _x_. The final output, [0.5,0.0,-2.0], is also incorrectly sorted.

These cases demonstrate that neither the exponent nor the mantissa maintains global monotonicity across the set of signed numbers. Consequently, the sign bit must serve as the primary sort key; this ensures that the most fundamental numerical boundary (the distinction between negative and non-negative values) is established before the magnitudes of exponents and mantissas are evaluated.

**Case 2: The sign is the primary key, but the exponent (**_p_**) **is not the secondary key.** This implies the sort order must be sign → mantissa → exponent. To test this, we only need to consider numbers of the same sign. Let the input array be [_x,y_]=[0.75,2.0]. Again, suppose we aim to sort the array in ascending order. Their representations are \(x=1\cdot 11_2\cdot 2^{-2}\) and \(y=1\cdot 10_2\cdot 2^0\).

The algorithm first correctly places both into a positive numbers partition. It then proceeds to sort such partition by mantissa. Since _m<sub>y</sub>\<m<sub>x</sub>_ (10<sub>2</sub>_\<_11<sub>2</sub>), the algorithm places _y_ before _x_, resulting in the order [2.0,0.75]. As these elements are now separated in their respective partition, the final sort by exponent will not change their order. The result violates the ascending sort invariant.

The exponent determines a number’s order of magnitude, while the mantissa refines its value within that magnitude. An algorithm must therefore evaluate the exponent before the mantissa.

**Theorem 3** (Sufficiency of sort order)**.** _The bsortFloat algorithm, in conjunction with its sub-procedures, correctly sorts an array of floating-point numbers that adhere to the representation defined in Theorem 1._

_Proof._ The proof is structured in three parts, mirroring the algorithm’s execution flow: (1) the initial sign partition, (2) the recursive sort on the exponent field, and (3) the final sort on the mantissa field.

**1. Correctness of Sign sort:** The logic for partitioning floating-point numbers by sign is identical to the method established for signed integers (Section III-A). As demonstrated in that section, the bitwise order of the sign bit is the inverse of the required numerical order for an ascending sort. A naive ascending pass would incorrectly place non-negative numbers before negative ones.

Therefore, _bsortFloat_ employs the same solution: it inverts the sort direction for the initial pass by calling _singlePassBSort_ with \(\negasc\). This leverages the exact same mechanism to correctly place all negative numbers before all non-negative numbers, establishing the correct primary order.

**2. Correctness of Exponent sort:** We prove by induction that the recursive calls in _bsortF_ correctly sort each same- signed partition by its exponent. Let _w<sub>p</sub>_ be the number of bits<tbc>

<tbc>in the exponent. Let _P<sub>E</sub>(k_) be the inductive hypothesis for the exponent sort:

**Inductive Hypothesis** _P<sub>E</sub>(k_)**:** After processing the _k_ most significant bits of the exponent (for \(1\unknown k\unknown w_p\)), the partition is correctly sorted according to the numerical value represented by those _k_ bits.

**Base Case (**_k_=1**)**:** Let the algorithm process only the most significant bit (_b<sub>k</sub>_). By definition _singlePassBSort_ partitions the array into two sets: _S_<sub>0</sub>={_x|b<sub>k</sub>_=0} and _S_<sub>1</sub>={_x|b<sub>k</sub>_=1}. If the sorting direction is ascending, _S_<sub>0</sub> is placed before _S_<sub>1</sub>, and vice versa if descending. In both cases, the relative order of _S_<sub>0</sub> and _S_<sub>1</sub> satisfies the numerical requirement for that single bit. Thus, the array is correctly partitioned with respect to the _k_=1 bit, and _P<sub>E</sub>_(1) holds

**Inductive Step:** Assume the inductive hypothesis _P<sub>E</sub>(k_) is true for some _k\<w<sub>p</sub>_. This means the partition is correctly sorted based on the lexicographical value of the first _k_ bits of the exponent. All elements that share an identical _k_-bit prefix are now in the same sub-partition.

The algorithm then processes the (_k_+1)-th bit. Consider any one of the sub-partitions created in the previous step. _singlePassBSort_ is called on this sub-partition, dividing it into two smaller groups: a 0-group where the (_k_+1)-th bit is 0, and a 1-group where it is 1.

The procedure places the 0-group before the 1-group (for a standard ascending sort). Let _x_ and _y_ be any element from the 0-group and 1-group, respectively. The (_k_+1)-bit prefix of _x_ is now lexicographically smaller than the prefix of _y_. By placing all such _x_ before all such _y_, the algorithm correctly extends the sorted property to the (_k_+1)-th bit.

This demonstrates that if the array is correctly sorted by _k_ bits, the algorithm will correctly sort it by _k_+1 bits. Thus, if _P<sub>E</sub>(k_) is true, then _P<sub>E</sub>(k_+1) is also true.

**3. Correctness of Mantissa sort:** After the exponent sort, _bsortF_ calls _binaryQuickSort_ on each sub-partition. Within any such sub-partition, all elements have an identical sign and exponent, so their numerical order depends only on their mantissa. Sorting by mantissa is equivalent to sorting unsigned integers, for which _binaryQuickSort_ is correct. The sort direction is chosen based on the sign of the partition, ensuring the final order is correct.

**Conclusion:** Since the array is (1) correctly partitioned by sign, (2) correctly sub-partitioned by exponent, and (3) each resulting sub-partition is correctly sorted by mantissa, the _bsortFloat_ algorithm is correct.

Algorithms 4 and 5 illustrate this sorting procedure. It is important to clarify that in these algorithms _sizeof\_exponent(x_), _sizeof\_mantisa(x_) and _sizeof(x_), return the bit-width of the exponent, mantissa and the actual value of _x_, respectively. Consequently, the relationship between these widths is defined as _size\_of(x_)=_sizeof\_mantisa(x_)+_sizeof\_exponent(x_)+1, where the constant term accounts for the sign bit.

It is assumed that the sign, exponent and mantissa are stored in the order in which they were mentioned (so most<tbc>

