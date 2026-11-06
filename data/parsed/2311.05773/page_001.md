An Algorithm for Bichromatic Sorting with Polylog Competitive Ratio

**Abstract**

The problem of sorting with priced information was introduced by [Charikar, Fagin, Guruswami, Kleinberg, Raghavan, Sahai (CFGKRS), S 2000]. In this setting, different comparisons have different (potentially infinite) costs. The goal is to find a sorting algorithm with small competitive ratio, defined as the (worst-case) ratio of the algorithm’s cost to the cost of the cheapest proof of the sorted order.

The simple case of bichromatic sorting posed by [CFGKRS] remains open: We are given two sets _A_ and _B_ of total size _N_, and the cost of an _A-A_ comparison or a _B-B_ comparison is higher than an _A-B_ comparison. The goal is to sort \(A\cup B\). An \(\Omega(logN)\) lower bound on competitive ratio follows from unit-cost sorting. Note that this is a generalization of the famous nuts and bolts problem, where _A-A_ and _B-B_ comparisons have infinite cost, and elements of _A_ and _B_ are guaranteed to alternate in the final sorted order.

In this paper we give a randomized algorithm InversionSort with an almost-optimal w.h.p. competitive ratio of _O_(log<sup>3</sup>_N_). This is the first algorithm for bichromatic sorting with a _o(N_) competitive ratio.

## 1 Introduction and main results

In their seminal paper "Query strategies for priced information", Charikar, Fagin, Guruswami, Kleinberg, Raghavan and Sahai [4] [CFGKRS S 2000] study the problem of computing a function _f_ of _n_ inputs, where querying an input has a certain cost associated to it, and one wants to find the cheapest query strategy that computes _f_. The _competitive ratio_ is defined as the (worst case) ratio of the cost of the query strategy to the cost of the cheapest proof of _f_. This work initiated a multitude of papers on priced information, studying problems like learning with attribute costs [9], stochastic boolean function evaluation [5], searching on trees [13, 12], priced information in external memory [3], and others.

The problem of _sorting with priced information_, or even a simple bichromatic version of it (stated by (CFGKRS [4])), remains tantalizingly open. After describing their main results, (CFGKRS [4]) mention in further directions: "_Sorting items when each comparison has a distinct cost appears to be highly non-trivial. Suppose, for example, we construct an instance of this problem by partitioning the items into sets A and B, giving each A-to-B comparison a very low cost, and giving each A-to-A and B-to-B comparison a very high cost. We then obtain a very simple non-uniform cost structure in the spirit of the well-known hard problem of "sorting nuts and bolts""_

<sup>∗</sup>Queens College CUNY, Flushing, New York, USA. Supported by NSF grant CCF-1910873. **mayank.goswami@qc.cuny.edu** <sup>†</sup>IT University of Copenhagen, København S, Denmark. Part of this work done during the second Hawaiian workshop on parallel algorithms and data structures, University of Hawaii at Manoa, Hawaii, USA, NSF Grant CCF-1930579. **rikj@itu.dk**

Mayank Goswami<sup>∗</sup>

Riko Jacob<sup>†</sup>

arXiv:2311.05773v1 [cs.DS] 9 Nov 2023

