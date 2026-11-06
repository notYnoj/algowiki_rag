(2) In the Disk-Access Model (DAM), where transferring elements between disk and internal memory is the main bottleneck, we consider the scenario where elements in _B_ are larger than elements in _A_. The larger items take more I/Os to be brought into memory, consume more space in internal memory, and are required in their entirety for comparisons.

A key observation is that the complexity of sorting depends heavily on the interleaving of the small and large items in the final sorted order. If all large elements come after all small elements in the final sorted order, sorting each type separately and concatenating is optimal. However, if the set of predecessors of _B_ in _A_ has size \(k\checkmark n\), one must solve an associated batched predecessor problem in order to achieve optimality.

We first give output-sensitive lower and upper bounds on the batched predecessor problem, and use these to derive bounds on the complexity of sorting in the two models. Our bounds are tight in most cases, and require novel generalizations of the classical lower bound techniques in external memory to accommodate the non-uniformity of keys.

**Keywords:** Priced information sorting batched predecessor external memory output-sensitive algorithms.

## 1 Introduction

In most published literature on sorting and other comparison-based problems (e.g., searching and selection), the traditional assumption is that a comparison between any two elements costs one unit, and the efficiency of an algorithm depends on the total number of comparisons taken to solve the problem. In this paper, we study a natural extension to sorting, where the cost of a comparison between a pair of elements can vary, and the comparison cost is the function of the elements being compared.

We work in both the the random-access-machine (RAM) and the disk- access-machine (DAM) [1] models (described below). We derive worst-case upper and lower bounds for comparison-based sorting and batched predecessor.

In the RAM model, we assume that comparisons between a pair of keys have an associated cost that depends on the "type" of keys involved. As a toy problem, consider the case when we have keys of two types--_n_ red keys and _n_ blue keys. A comparison between a pair of red keys costs _a_, between a red key and a blue key costs _b_, and between a pair of blue keys costs _c_. Without loss of generality we can assume _a\<c_, which gives rise to three cases to be considered, _a\<b\<c_, _a\<c\<b_, and _b\<a\<c_<tbc>

