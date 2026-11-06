## B. bsort for floating-point values

**Theorem 1.** _Let x be a rational number with a finite fractional representation in an integer base b\>_1_. Then x can be expressed in the form:_

\(x=s\cdot m\cdot b^p\) (1)

_where_ \(s\in\{-1,1\}\) _is the sign,_ \(m\in\mathbb{N}_0\) _the mantissa, and_ \(p\in\mathbb{Z}_0^-\) _the exponent._

_Proof._ Any such number _x_ can be decomposed into its sign \(s\in\{-1,1\}\), its integer part \(a\in\mathbb{N}_0\), and its fractional part \(f\in[0,1)\). The fractional part _f_ consists of a finite sequence of _q_ digits.

We can express _x_ as \(x=s\cdot(a+f)\). Let the integer formed by the _q_ fractional digits be _c_. This is equivalent to \(c=f\cdot b^q\), which implies _f=c/b<sup>q</sup>_.

Substituting this back into the expression for _x_:

\(x=s\cdot\left(a+\frac{c}{b^q}\right)=s\cdot\left(\frac{a\cdot b^q+c}{b^q}\right)=s\cdot(a\cdot b^q+c)\cdot b^{-q}\)

Since \(a,b^q,c\in\mathbb{N}_0\), then \((a\cdot b^q+c)\in\mathbb{N}_0\) by the closure properties of addition and multiplication. Let this integer be \(m=a\cdot b^q+c\).

Furthermore, let _p_=-_q_. Since \(q\in\mathbb{N}_0\), its additive inverse \(p\in\mathbb{Z}_0^-\). Thus, we can write:

\(x=s\cdot m\cdot b^p\)

This completes the proof. \(\blacksquare\)

Examples of Theorem 1:

\(\bullet\) \(112.9_{10}=1\cdot 1129_{10}\cdot 10^{-1}\)<tbc>

\(\bullet\) \(-8.348975_{10}=-1\cdot 8348975_{10}\cdot 10^{-6}\)<tbc>

\(\bullet\) \(111.11_2=1(2^2\cdot 111_2+11_2)2^{-2}=11111_2\cdot 2^{-2}\)<tbc>

\(\bullet\) \(-101.1_2=-1(2^1\cdot 101_2+1_2)2^{-1}=-1\cdot 1011_2\cdot 2^{-1}\)<tbc>

\(\bullet\) \(4789_{10}=1\cdot 4789_{10}\cdot 10^0\)

Sorting floating-point values, represented as described in Theorem 1, is accomplished through a sequential, multi-pass sort on the components _s_, _p_, and _m_, in that order.

1) Sort by sign, _s_: The first pass sorts the entire array on the sign component, which partitions the data into two primary sections: one for all negative numbers and one for all non-negative numbers.<tbc>

2) Sort by exponent, _p_: Next, each of those two sections is sorted independently by the exponent _p_. This creates finer-grained sub-partitions where all elements share the same sign and exponent. To maintain correct numerical order, the sort direction for the exponents of negative numbers must be the inverse of the direction for positive numbers. For example, to sort the final array in ascending order, the exponents of negative numbers must be sorted in descending order.<tbc>

3) Sort by mantissa, _m_: Since all elements within a sub- partition already have the same sign and exponent, ordering them by their mantissa correctly places them in their final sorted position as it is the same as sorting unsigned integers. The sort direction also depends on the sign.

This three-pass procedure correctly sorts the entire array by progressively refining the order of the elements. Formal proofs are provided in Theorems 2 and 3.

**Theorem 2** (Necessity of sort order)**.** _The correctness of the bsortFloat algorithm is dependent on the hierarchical sorting order of sign, then exponent, then mantissa._

_Proof._ We will prove that any hierarchical sorting order other than sign \(\rightarrow\) exponent \(\rightarrow\) mantissa will fail to produce a correctly sorted array for all inputs. The numerical value of a number is determined first by its sign, then by the magnitude dictated by its exponent, and finally refined by its mantissa. Let’s prove this by contradiction by analyzing the two possible ways the required order can be violated.

**Case 1: The sign component (_s_) is not the primary sort key.** Assume the primary sort key is either the exponent (_p_) or the mantissa (_m_). Consider the input array \[_x,y,z_\]=\[-2.0,0.0,0.5\]. Their representations according to Theorem 1 are \(x=-1\cdot 10_2\cdot 2^0\), \(y=1\cdot 0_2\cdot 2^0\) and \(z=1\cdot 1_2\cdot 2^{-1}\). Suppose we aim to sort the array in ascending order.

If the algorithm sorts by mantissa first, it will incorrectly imply that _y\<z\<x_ because _m<sub>y</sub>\<m<sub>z</sub>\<m<sub>x</sub>_ (0<sub>2</sub>_\<_1<sub>2</sub>_\<_10<sub>2</sub>). Because the initial partitioning by mantissa places each element into a singleton partition, the subsequent recursive sorts on each one, will not change their order. The resulting array, \[0.0,0.5,-2.0\], fails to satisfy the ascending sort invariant.

-8
-1
3
-7
2
6
3
m
1000
1111
0011
1001
0010
0110
0011
1000
sort by sign
3
2
6
3
-8
-1
-7
m
0011
0010
0110
0011
1000
1111
1001
0100
k1
6
3
2
3
-1
-8
-7
m
0110
0011
0010
0011
1111
1000
1001
0010
k2
k1
k'2
6
3
2
3
-1
-8
-7
m
0110
0011
0010
0011
1111
1000
1001
0001
k2
k3
k1
k'2
k'3
6
3
3
2
-1
-7
-8
m
0110
0011
0011
0010
1111
1001
1000
0000
k2
k3
k1
k'2
k'3
sort positive values
sort negative values

Fig. 2: Tracing of bsort algorithm for signed integers using two’s complement notation.

