<tbc>size _k_. We want to express the performance of the sorting algorithm, as a function of _S_, _L_, _w_, and _k_.

Sorting with two key lengths helps illustrate a special connection between sorting and batched searching. Consider the following batched searching problem, which we call the _PLE_ (placement of large elements) problem. We have _S_ keys of unit size (short keys), which are given in sorted order. We have _L/w_ (long) keys of size _w_ each, and the objective is to find which short key is the immediate predecessor of each long key. The PLE problem is a lower bound on the sorting problem because it starts off with more information than the original sorting and asks to do less.

Often, the complexity of PLE dominates the complexity of sorting. However, obtaining lower bounds on the PLE presents several challenges. First, for many reasons (we want bounds in terms of _k_, keys have different sizes, and there are many searches happening in batch) standard information-theoretic lower bounds bounding how much information is learned do not immediately apply: different I/Os can "learn" very different amount of information. Second, because of the nonuniformity of the keys, the complexity of PLE turns out to be a minimum of two terms, each optimal for a certain range of values of _w_ (the length of large elements). Each case requires different techniques. Third, we have to take preprocessing into account. PLE is a batched searching problem with a nontrivial preprocessing-query tradeoff [8]. However, in our context it is a subproblem of sorting, and other parts of sorting dictate how much preprocessing is allowed.

## Related Work.

In RAM, algorithms that work with inputs with priced information have been studied before[11, 12, 16, 3].In this setting the results are presented using a competitive analysis framework. Another example of varying comparison costs is the well-known nuts-and-bolts problem [2]. Interleaving-sensitive lower bounds and batched searching in RAM are related to lower bounds for sorting multisets [19] and distribution-sensitive set-partitioning [14].

Aggarwal and Vitter [1] introduced the external-memory (DAM) model. The lower bounds they establish for fundamental comparison-based problems were generalized by Arge, Knudsen, and Larsen [6], and by Erickson [15] to the external algebraic decision tree model. Prominent examples studying lower bounds on batched and predecessor searching are found in [4, 7, 8].

Most previous work that considers variable-length keys does so in the context of B-trees [18, 13, 17, 20, 9].

