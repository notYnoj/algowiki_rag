<tbc>output array form the contiguous interval

\(\left[\sum_{u=0}^{v-1}c_u,\sum_{u=0}^vc_u\right).\)

Thus, it is unnecessary to compute a separate rank for every input element; it suffices to write each value into its corresponding output interval.

The most basic method for this problem setting is counting sort. It first constructs a histogram _H_\[0_..R_-1\] satisfying _H_\[_v_\]=_c<sub>v</sub>_, and then computes its prefix sums to determine the output interval of each value. For an array \(X[0..\ell-1]\), its prefix-sum array \(Y[0..\ell-1]\) is defined by

\(Y[i]=\sum_{j=0}^iX[j].\)

Although this procedure is straightforward sequentially, histogram updates on a GPU may concentrate additions at the same address, in which case contention among atomic operations can dominate performance. Furthermore, a stable counting sort must determine the local rank of each input element among elements with the same value and combine that rank with a prefix sum to determine its output position. By contrast, the unstable integer-array sorting problem considered here only requires the output interval of each value, allowing the output-generation step to be simplified.

As an early study of counting sort on GPUs, Sun and Ma presented a CUDA implementation of counting sort. Using a 2 GHz AMD Athlon 64 X2 3800+ CPU and an NVIDIA GeForce 9600 GSO GPU, they reported an 8.08-fold speedup over the corresponding CPU implementation for five million integers \[9\]. Faujdar and Ghrera compared sequential counting sort with CUDA-based parallel counting sort under six input conditions. Their sequential implementation ran on a 2.60 GHz Intel Core i5- 3230M, whereas the CUDA implementation ran on a system with a 2.93 GHz Intel Core i3-530 and an NVIDIA GeForce GTX 460; they reported a maximum speedup of 66 for inputs containing from 1,000 to 10,000,000 elements \[10\]. These studies show both that counting sort can be effective on GPUs and that its performance can depend strongly on the input distribution and the value range.

Kolonias et al. designed an integer counting sort for CUDA GPUs whose final output stage avoids synchronization by writing different values to disjoint intervals. They also considered constructing one partial histogram per thread block in shared memory when the range fits in shared memory \[5\]. Our method extends this shared-memory histogram idea through range tiling and differs further in that it directly determines the value at each output position from a local CDF.

Building on the idea of shared-memory partial histograms, we partition the range into small intervals of width _T_, called range tiles, that fit in shared memory, thereby increasing the range sizes that can be handled. For each range tile, we construct a CDF--the cumulative counts within that tile--and load the resulting local CDF into shared memory to determine the value corresponding to each output position.

The output-generation method of Kolonias et al. can be simplified for our problem setting as shown in Algorithm 1. First, a histogram of the input array is computed, and its prefix sums give the output starting position _P_\[_v_\] of each value. Then, for every value _v_, the interval \[_P_\[_v_\]_,P_\[_v_+1\]) is filled with _v_. Because different values are written to disjoint output intervals, the final step requires no synchronization between values.

