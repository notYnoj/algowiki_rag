# Batched Predecessor and Sorting with Size-Priced Information in External Memory

**Abstract**

In the unit-cost comparison model, a black box takes an input two items and outputs the result of the comparison. Problems like sorting and searching have been studied in this model, and it has been generalized to include the concept of priced information, where different pairs of items (say database records) have different comparison costs. These comparison costs can be arbitrary (in which case no algorithm can be close to optimal (Charikar et al. S 2000)), structured (for example, the comparison cost may depend on the length of the databases (Gupta et al. FOCS 2001)), or stochastic (Angelov et al. LATIN 2008). Motivated by the database setting where the cost depends on the sizes of the items, we consider the problems of sorting and batched predecessor where two non-uniform sets of items _A_ and _B_ are given as input.

(1) In the RAM setting, we consider the scenario where both sets have _n_ keys each. The cost to compare two items in _A_ is _a_, to compare an item of _A_ to an item of _B_ is _b_, and to compare two items in _B_ is _c_. We give upper and lower bounds for the case \(a\le b\le c\), the case that serves as a warmup for the generalization to the external-memory model. Notice that the case \(b=1,a=c=\infty\) is the famous "nuts and bolts" problem.

<sup>∗</sup>Stony Brook University, **bender@cs.stonybrook.edu**. This work was supported in part by NSF grants CCF-1725543, CSR-1763680, CCF-1716252, CCF-1617618, CNS- 1938709, and by Sandia National Laboratories. <sup>†</sup>Queens College, CUNY, **mayank.goswami@qc.cuny.edu**. Supported by NSF grants CRII-1755791 and CCF-1910873. <sup>‡</sup>International University of Sarajevo, **dzmedjedovic@ius.edu.ba**. <sup>§</sup>Google Inc., **pabmont@gmail.com**. \(^\unknown\)Aristotle University of Thessaloniki, **tsichlas@csd.auth.gr**.

Michael A. Bender<sup>∗</sup> Mayank Goswami<sup>†</sup> Dzejla Medjedovic<sup>‡</sup> Pablo Montes<sup>§</sup> Kostas Tsichlas<sup>¶</sup>

arXiv:2004.13197v1 [cs.DS] 27 Apr 2020

