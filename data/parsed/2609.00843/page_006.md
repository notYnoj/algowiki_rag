<tbc>the last extended bin of each value, the original CDF can be recovered. This refinement is characterized by distributing atomic contention in global memory through bin extension.

Unlike the original H-P sort in Algorithm 2, RefHP also provides an implementation that does not construct the second histogram \[8\]. Let _H_<sub>1</sub>\[0_..R_-1\] be the input histogram and let _P_<sub>1</sub>\[0_..R_-1\] be the CDF obtained by computing its prefix sums. For _d\>_0,<tbc>

\(P_1[d]-P_1[d-1]=H_1[d].\)

<tbc>Thus, _P_<sub>1</sub>\[_d]\>P_<sub>1</sub>\[_d_-1\] if and only if value _d_ occurs in the input array. When _d_ occurs, _P_<sub>1</sub>\[_d_-1\] is the number of input elements smaller than _d_, and hence is the starting position of _d_ in the sorted array. The output array _B_ of length _n_ is therefore initialized to zero, and for every value _d\>_0 at which the CDF has a step, RefHP writes<tbc>

\(B[P_1[d-1]]\leftarrow d.\)

<tbc>At this point, each value is stored only at the first position of its output interval, while all other entries remain zero. Finally, the prefix maximum of _B_ is computed:

\(B[i]=max_{0\le j\le i}B[j].\)

This propagates each value up to the position immediately preceding the start of the next value’s interval and yields the sorted array _B_. Thus, the construction and prefix sum of the second histogram in Algorithm 2 are replaced by Algorithm 3.

**Algorithm 3** Output generation in RefHP using CDF step detection and a prefix maximum \[8\]

**Require:** CDF _P_<sub>1</sub>\[0_..R_-1\] and input size _n_

**Ensure:** Sorted array _B_\[0_..n_-1\]

1: \(B[0..n-1]\leftarrow 0\)

2: **for all** \(d\in(1,R)\) **in parallel do**

3: **if** _P_<sub>1</sub>\[_d]\>P_<sub>1</sub>\[_d_-1\] **then**

4: \(B[P_1[d-1]]\leftarrow d\)

5: **end if**

6: **end for**

7: InclusiveMaximumInPlace(_B_)

8: **return** _B_

This procedure is an important improvement for efficiently generating the H-P output on a GPU and corresponds to the counting-sort idea of producing an output interval for every value. Taken together, the counting sort of Kolonias et al., H-P sort, and RefHP can all be viewed as methods that construct a CDF from a histogram in some form and determine output intervals from that CDF.

From our perspective, the important property of H-P sort and RefHP is that the CDF obtained from the first histogram and its prefix sums determines the output array. Accordingly, the central design choice in our method is not to handle one CDF for the entire range, but to construct a local CDF for each range tile and retain only the relevant tile’s local CDF in shared memory during output generation.

