<tbc>the original input array into logical regions, creating a sorted and an active region. The active region of the array is reprocessed at the end of each round, the size of the active region is reduced by tracking the index where all previous elements are considered sorted (`partition\_ptr`) while leaving the sorted region intact, it contains elements of respective log groups relatively sorted to each other. The decision of whether an element is sorted or not is based on the condition (_A_\[_i_\]_/base_<sup>_r_-1</sup>=0) (refer line 18 of Algorithm 1) satisfied or not, where _r_ is the iteration of rounds, thereby reducing unnecessary the operations on sorted portion of the input.

In Appendix, we provide the pseudocode of SP-LSD algorithm (Algorithm 1) and Algorithm 2 which is a is a helper function that calls Counting Sort as a subroutine for sorting a portion of the array. We also provide there some details required for understanding Algorithms 1 and 2. Further in the Appendix, we demonstrate the SP-LSD algorithm with two examples (one is a bad case example) which will help the readers to understand how SP-LSD works.

### 5 Analysis of the Optimization

We can break down the cost of operations of the algorithm in stages on the basis of rounds, which run from 1 to _R_. The number of rounds is determined by the formula \(\lfloor log_nk\rfloor+1\), where _k_ is the maximum element. We further define \(\alpha\) to be the cost for sorting and \(\beta\) to be the cost for the partition and \(c=\alpha/\beta\). Also, we define _p_ as the proportion of elements partitioned-out after the first effective partitioning step. Then,

- Stage 1 (Round 1): Perform sorting on the mod values of the entire array, no partitioning required.<tbc>

- Stage 2 (Rounds 2 to _R_-1): Perform partitioning and sort the active region iteratively.<tbc>

**-** Stage 3 (Round _R_): Perform sorting on the final active region, no partitioning required.

#### 5.1 The Pruning Crossover

Introducing adaptiveness provides a significant trade-off: SP-LSD incurs structural overheads (partitioning cost) to prune redundant operations (sorting cost). Unlike the deterministic BNRS, SP-LSD’s cost is inherently input-dependent, governed by the shrinkage rate of the active region. To theoretically bound this behavior, we perform a rigorous cost-benefit analysis, distinguishing between fixed full dataset operations and varying active region operations through the defined stages. We evaluate this trade-off under two boundary conditions defined by dataset assumptions:

1. **Skewed Distribution:** Analysis of the Skewed Distribution provides the minimum required skew (_p_) for the viability of performing SP-LSD.<tbc>

2. **Uniform Log Distribution:** Analysis of the Uniform Log Distribution defines the hardware cost limits (_c_) required for the algorithm to win on uniform partitioning.

