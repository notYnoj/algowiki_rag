• **Structural reframing of fine-grained hardness:** Many fine-grained reductions to Subset- Sum implicitly target _high-entropy_, near collision-free instances (i.e., _U_≈2_<sup>n</sup>_). IC-SubsetSum makes this structural dependency explicit, showing that hardness in the standard reductions aligns with the regime of near-maximal distinct sums.<tbc>

• **A generic design template for certificate-sensitive algorithms:** By reinterpreting dynamic programming as guided certificate traversal, IC-SubsetSum offers a broadly applicable approach to adaptive enumeration, potentially extending to other NP-complete problems with wide certificate-size variance.

## 2 Introduction

### Worst-Case versus Per-Instance Analysis.

The modern theory of algorithms is dominated by worst-case running-time guarantees. While immensely successful, the paradigm sometimes fails to explain the vast performance variance that practitioners observe between individual inputs of the _same_ size. A complementary research line, initiated by Orponen-Ko-Schöning-Watanabe \[OKSW94\], formalised _Instance Complexity_ (IC): the intrinsic difficulty of a _single_ instance is the bit-length of the shortest "special-case program" that decides it within a time bound _t_.

At first glance, however, IC seems paradoxical: for each among infinitely many possible inputs we would have to synthesise a bespoke decision program _before_ seeing that input, with no _a priori_ structural knowledge. Lacking such a generative recipe, researchers long treated IC as a purely existential benchmark--useful for lower bounds but incompatible with efficient algorithms. IC- SubsetSum challenges this perception by constructing the certificate _online_ and bounding its runtime by a provable function of the certificate length.

### The Subset-Sum Problem.

In the canonical Subset-Sum problem we are given a multiset \(S=\{a_1,\dots,a_n\}\subseteq\mathbb{Z}_{>0}\) and a target \(t\in\mathbb{Z}_{>0}\). The task is to decide whether some submultiset sums to _t_. Subset-Sum is NP-complete and underpins numerous reductions across combinatorics, cryptography, and fine-grained complexity.

### Classical Algorithms.

Two textbook techniques illustrate the gulf between worst-case and per-instance behaviour:

a. _Bellman Dynamic Programming_ takes _O(nt_) time--pseudopolynomially efficient when _t_ is small, but infeasible for large numeric ranges \[Bel57\]. While a small target _t_ naturally constrains _U_, the reverse is not true; our approach remains efficient even for large _t_ provided that _U_ is small due to additive structure.<tbc>

b. _Horowitz-Sahni Meet-in-the-Middle_ enumerates all 2<sup>_n/_2</sup> subset sums of each half of _S_ and intersects the two lists in _O_<sup>∗</sup>(2<sup>_n/_2</sup>) time\[HS74\]. Decades of work have failed to beat the 2<sup>_n/_2</sup> factor in the worst case \[BFN25, Woe08\].

Yet practitioners observe that real-data instances (e.g., knapsack crypto, bin-packing logs) are often much easier: many different subsets _collide_ to the same value, so the number of distinct subset sums \(U=|\Sigma(S)|\) is far smaller than 2_<sup>n</sup>_. This _additive redundancy_--small _U_ due to duplicates, near-arithmetic progressions, or other structure--is exactly what analyses that track only _n_ and _t_ overlook.

