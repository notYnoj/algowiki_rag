<tbc>applies a prefix sum to that histogram to obtain the sorted output. Algorithm 2 shows this procedure.

**Algorithm 2** Basic structure of H-P sort

**Require:** Input array _A_\[0_..n_-1\] and range size _R_

**Ensure:** Sorted array _B_\[0_..n_-1\]

1: \(H_1[0..R-1]\leftarrow\) histogram of _A_

2: \(P_1[0..R-1]\leftarrow\) prefix sums of _H_<sub>1</sub>

3: \(H_2[0..n]\leftarrow\) histogram of _P_<sub>1</sub>

4: \(B[0..n-1]\leftarrow\) prefix sums of _H_<sub>2</sub>\[0_..n_-1\]

5: **return** _B_

Algorithm 2 can be interpreted as follows. Because _P_<sub>1</sub>\[_v_\] is the right endpoint of the output interval of value _v_, the positions at which values of _P_<sub>1</sub> occur indicate boundaries at which the value in the output array changes. The array _H_<sub>2</sub> counts these boundary positions, and its prefix sums give the number of boundaries up to each output position _i_. This number is precisely the value that should be written at output position _i_. For example, if values 0, 1, and 2 occur 2, 3, and 1 times, respectively, then _P_<sub>1</sub>=(2,5,6). The boundary positions of _H_<sub>2</sub> are 2, 5, and 6, and the prefix sums of _H_<sub>2</sub>\[0..5\] are (0,0,1,1,1,2), yielding the sorted array. Thus, H-P sort reconstructs output values from CDF boundary information. Eisenstat’s integer-sorting algorithm, on which H-P sort is based, runs in _O_(log<sup>∗</sup>_n_) time on a Sum-CRCW PRAM \[6\]. On a GPU, however, histogram updates for identical values cause atomic contention, so the theoretical parallelism of the PRAM algorithm is not directly reflected in practical performance.

Kozakai et al. implemented H-P sort on a GPU and compared it with CUB \[7\]. For _n_ from 10<sup>6</sup> to 10<sup>7</sup>, _minVal_=0, and _maxVal=n/_50, H-P sort was up to 2.97 times faster than CUB. They also proposed 1-H-P sort, which omits part of H-P sort for inputs without duplicates, and 0-compressed H-P sort, which compresses intervals of absent values in the histogram. They reported that 1-H-P sort was up to 2.01 times faster than CUB for distinct inputs, and that 0-compressed H-P sort was up to 2.73 times faster when the number of distinct values actually present was small \[7\]. An important result of that work is that H-P sort is not merely a theoretical algorithm: it identifies conditions under which H-P sort is competitive with CUB for range-restricted integer sorting on GPUs. At the same time, its performance varies substantially with the input size _n_, the range size _R_, and the number of distinct values that actually occur. In particular, when many threads concurrently add to the same histogram bin, atomic contention increases and the first histogram computation becomes a bottleneck.

RefHP, proposed by Takase et al., refines H-P sort to mitigate this GPU implementation bottleneck \[8\]. RefHP achieved a maximum speedup of 3.45 over the original H-P sort and outperformed CUB even under conditions where H-P sort was slower than CUB. When constructing the CDF, RefHP extends the bin for each value into multiple bins and distributes input elements among these extended bins. If the extension factor is _e_, it allocates _e_ bins for value _v_ and adds the element at input position _i_ to a location such as _ve_+(_i_mod_e_). Consequently, even when a value appears many times, updates are less likely to concentrate on a single bin. A prefix sum is then computed over the extended histogram; by referring to<tbc>

