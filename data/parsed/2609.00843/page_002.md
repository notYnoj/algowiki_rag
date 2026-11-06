<tbc>each value in the output array. If stability is not required, individual input elements need not be moved to their respective ranks. A correct sorted output can instead be obtained by determining the contiguous interval occupied by each value and writing that value throughout the interval. We denote the number of input elements by _n_ and the size of the known integer range [_minVal,maxVal_) by _R=maxVal-minVal_. The problem considered in this paper is to sort _n_ integers from this range into nondecreasing order without preserving the relative order of equal values.

Previous work on range-restricted integer sorting on GPUs includes the counting sort of Kolonias et al. [5], a GPU implementation of H-P sort based on Eisenstat’s algorithm [6, 7], and Ref-H-P sort (hereafter RefHP), which refines H-P sort for GPU execution [8]. These methods share the property that a histogram and its prefix sums provide information about the output position or output interval of each value. We focus on this common structure, in which output intervals are determined from a histogram and prefix sums. We then propose and evaluate Range-Tiled CDF sort (RT-CDF), which partitions the possible integer range into multiple small intervals, called range tiles, that fit in shared memory, and constructs a histogram and a cumulative distribution function (CDF) for each tile.

In this paper, the term CDF denotes the cumulative-count array obtained as the prefix sum of a histogram. It is not a probability distribution normalized to the interval [0,1]; rather, each entry gives the number of input values no greater than the corresponding value. The CDF constructed within a tile, which we call a local CDF, determines the output interval occupied by each value in that tile. Consequently, the output can be generated without rescanning the input array.

The contributions of this work are as follows.

• We develop RT-CDF, which partitions the value range into tiles that fit in shared memory and directly generates the output array from the local CDF of each tile.<tbc>

• We clarify the algorithmic relationship between RT-CDF and a counting-sort implementation based on Kolonias et al., H-P sort, and RefHP, and identify how RT-CDF differs from existing methods that determine output intervals from a CDF.<tbc>

• On an NVIDIA GeForce RTX 4090, we compare RT-CDF with CUB `DeviceRadixSort`, RefHP, and an implementation based on Kolonias et al., and identify the range sizes and input sizes for which RT-CDF is effective, as well as its limitations near _R_=2<sup>18</sup>.

## 2 Background and Motivation

### 2.1 Problem Setting and Counting-Sort-Based Baselines

We consider unstable sorting of arrays whose possible integer values lie in a known range. The input is an array _A_[0_..n_-1] of _n_ integers, all of which belong to a known range [_minVal,maxVal_). Let _R=maxVal-minVal_. For simplicity of notation, we subtract _minVal_ from every element and continue to denote the resulting array by _A_, so that \(0\le A[i]<R\). The output is an array _B_[0_..n_-1] containing the elements of _A_ in nondecreasing order. If value \(v\in[0,R)\) occurs _c<sub>v</sub>_ times, then its positions in the<tbc>

