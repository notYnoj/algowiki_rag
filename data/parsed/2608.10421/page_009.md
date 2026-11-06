## 4 Optimized Variants

Now that the complexity bounds of directional mergesort are established, we proceed to consider two optimizations that result in directional mergesort<sup>++</sup>.

### 4.1 Adapting to Decreasing Runs

In the base algorithm, the returned Boolean flag tracks if the subarray was purely non-decreasing (`true` iff so) according to the success of skip checks. However, as skip checks only verify if the two halves are already in non-decreasing order, decreasing runs are treated as individual runs of length 1. Thus, we extend the return value to two flags _x_<sub>1</sub> and _x_<sub>2</sub>, where _x_<sub>1</sub> is the standard non-decreasing flag and _x_<sub>2</sub> tracks if the subarray was purely strictly decreasing (`true` iff so). In practice, these flags can be represented with a 2-bit unsigned integer bitmask for simpler implementation.

**Algorithm 2** Directional Mergesort<sup>+1</sup>

function Sort\((A[],\ell,r)\triangleright\) Processing Subarray \(A[\ell..r)\)<br>   if \(r-\ell<2\) then return (`true`, `true`)<br>   if \(r-\ell=2\) then<br>   if \(A[\ell]\le A[\ell+1]\) then return (`true`, `false`)<br>   else return (`false`, `true`)<br>  \(m\leftarrow\lfloor(\ell+r)/2\rfloor\)<br>   \((a_1,a_2)\leftarrow Sort(A,\ell,m)\)<br>  \((b_1,b_2)\leftarrow Sort(A,m,r)\)<br>   if \(a_2\wedge b_2\) then<br>   if A\[m-1\]\>A\[m\] then return (`false`, `true`)<br>  \(\triangleright\) Decreasing Skip Check<br>   if a<sub>2</sub> then Reverse\((A,\ell,m)\triangleright\) Reversing Decreasing Halves<br>   if b<sub>2</sub> then Reverse(A,m,r)<br>   if not\((a_2\wedge b_2)\) then<br>   if \(A[m-1]\le A[m]\) then return (\(a_1\wedge b_1\), `false`)<br>  \(\triangleright\) Standard Skip Check<br>   if \(b_1\vee\neg(b_2\vee a_1)\) then MergeBw\((A,\ell,m,r)\triangleright\) Directional Merging<br>   else MergeFw\((A,\ell,m,r)\)<br>   return (`false`, `false`)<br>   procedure DirectionalMergesort<sup>+1</sup>(A\[],n)<br>   if Sort(A,0,n)=(`false`, `true`) then Reverse(A,0,n)

This variant has two separate base cases. When the subarray has 1 element, it is vacuously both non-decreasing and strictly decreasing, so the procedure returns both as `true`. When the subarray size is 2, one comparison suffices to determine the relationship between the two elements, allowing us to concretely decide if the subarray is non-decreasing or strictly decreasing.

To avoid unnecessary data movement and allow for the maximal extension of decreasing runs, physical reversals are deferred: a purely decreasing subarray is reversed only when its parent subarray is not purely decreasing where the decreasing flag is dropped. To handle the edge case where the entire array is in strictly decreasing order and not corrected during any recursive calls, the outer procedure DirectionalMergesort<sup>+1</sup> intercepts this return value and performs a single top-level reversal to reorient the array in sorted order. Note that stability is maintained by the reversals as they only operate on strictly decreasing subarrays that cannot contain equal elements, ensuring the relative order of equal elements are not inverted.

