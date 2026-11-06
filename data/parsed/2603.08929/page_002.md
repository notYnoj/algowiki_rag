Function singlePassBSort(a, m, ps, pe, asc) is<br>
   Input : a - The array of numbers to be sorted;<br>
   \(a_i\in a\forall i\in\mathbb{Z}:0\le i<|a|\)<br>
    m - the current mask; \(\exists k\in\mathbb{N}_0:m=2^k\)<br>
    ps,pe - the indices at which the partition<br>
to be sorted starts (inclusive) and ends<br>
   (exclusive);<br>
   \(ps,pe\in\mathbb{Z}:0\le ps\le pe<|a|\)<br>
    asc - boolean indicating whether the<br>
order is ascending<br>
   Output: An index \(k\in[ps,pe]\) such that \(a_i\wedge m=0,a_j\wedge m=m\forall i\in[ps,k),j\in[k,pe]\) if<br>
and only if asc is true, or<br>
   \(a_i\wedge m=m,a_j\wedge m=0\) otherwise<br>
   k:=ps<br>
   for \(i\leftarrow ps\) to pe do<br>
   if \((asc\wedge\neg(a_i\wedge m))\vee(\negasc\wedge(a_i\wedge m))\) then<br>
_swap_<br>
_a<sub>i</sub>,a<sub>k</sub>_<br>
  \(k\leftarrow k+1\)<br>
   end if<br>
   end for<br>
   return k<br>
end

**Algorithm 2:** Binary quicksort for equally-signed integers

Function binaryQuickSort(a, m, ps, pe, asc) is<br>
   Input : Same as singlePassBSort<br>
   Output: The same array a but with the partition<br>
starting at ps and ending at pe (exclusive)<br>
now sorted in ascending or descending<br>
order depending of asc<br>
   k:= singlePassBSort(a,m,ps,pe,asc)<br>
   \(m':=m\gg 1\)<br>
   if \(m'=0\) then<br>
**return**<br>
_a_<br>
   end if<br>
   \(binaryQuickSort(a,m',ps,k,asc)\)<br>
   \(binaryQuickSort(a,m',k,pe,asc)\)<br>
   return a<br>
end

## III. BSORT

The bitwise partitioning mechanism of the standard binary quicksort algorithm is predicated on the lexicographical ordering of unsigned integer representations. Consequently, it is not directly applicable to data types such as signed integers or floating-point numbers, which do not adhere to this ordering principle.

_Proof._ Consider an array _a_ containing two signed integers, _a_=\[_x,y_\], where _x\<_0 and \(y\ge 0\). Let _w_ be the word size in bits. In the standard two’s complement representation, the<tbc>

<tbc>MSB of _x_ is 1, while the MSB of _y_ is 0.

The algorithm’s initial partitioning pass, as defined by _singlePassBSort_, operates on the MSB and partitions the array based on the bitwise AND with the mask \(m=1\checkmark(w-1)\)

1) For element _x_, \(x\wedge m=m\), since its MSB is 1.<tbc>

2) For element _y_, \(y\wedge m=0\), since its MSB is 0.

According to the logic in _singlePassBSort_, for an ascending sort, elements yielding a non-zero result are placed in the second partition (the "greater" partition), while those yielding zero are placed in the first. Therefore, the partitioning step will incorrectly place _x_ after _y_. This violates the monotonicity invariant required for a sorted sequence, proving the algorithm fails for mixed-sign integers.

This same logic extends to floating-point numbers. Under the IEEE-754 standard, the MSB is also a sign bit. A similar bitwise comparison will incorrectly order negative and positive values for the same reason outlined above. Furthermore, the lexicographical order of the remaining bits does not correspond directly to the numerical magnitude of floating- point values, creating additional sorting failures even within partitions of the same sign.

### A. bsort for signed integers

The preceding analysis demonstrates that the initial call to _singlePassBSort_ for signed numbers inverts the relative order of the negative and non-negative partitions. For example, in an ascending sort, this erroneously places all negative numbers after all non-negative numbers. To rectify this, we simply invert the sort direction for the initial pass of the algorithm. Algorithm 3 formalizes this procedure.

Throughout this paper, \(a\gg b\) and \(a\gg b\) denote arithmetic and logical right-shift operations, respectively, e.g., given an 8-bit integer _x_=-128<sub>10</sub>=1000\_0000<sub>2</sub>, then \(x\gg 1=-64_{10}=1100\text{\_}0000_2\) and \(x\gg 1=64_{10}=0100\text{\_}0000_2\). The function _sizeof(x_) returns the bit-width of the operand _x_.

Function bsortSigned(a, asc) is<br>
   Input : a - an array of signed integers<br>
   asc - boolean indicating the sorting order<br>
   Output: The same array a but sorted<br>
   \(m:=1\checkmark(sizeof(a_0)-1)\)<br>
   \(k:=singlePassBSort(a,m,0,|a|,\negasc)\)<br>
   \(m':=m\gg 1\)<br>
   \(binaryQuickSort(a,m',0,k,asc)\)<br>
   \(binaryQuickSort(a,m',k,|a|,asc)\)<br>
   return a<br>
end

**Example for Algorithm 3:**

Let the input data be _a_=\[-8,-1,3,-7,2,6,3\]_,asc=false_, then the tracing of _bsortSigned(a,asc_) is shown in Figure 2.

**Algorithm 1:** bsort sub-procedure to partition an array

**Algorithm 3:** bsort for signed integers

