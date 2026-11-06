Perhaps more surprising is that after unbalancing, the treaps have become easily the most effective method, and their performance is very nearly optimal for all tree sizes. As shown in Figure 5, the approximately 9-10% improvement optimization (relative to either weight-balanced trees or their unbalanced versions) will provide computationally meaningful savings in practice; the 1% difference between the unbalanced treaps and optimal trees is much less interesting.

Of course, given the weak bounds on the number of _possible_ bumps before quiescence, our methods might not be viable in practice after all. Data regarding this (for unbalancing treaps, which appears to be the situation of interest) appears in Figure 6. For each size tree, we show both the mean number of bumps improving a treap of that size, and the maximum number of bumps. As can be seen, both numbers stabilize at _b_≈0.21_n_, where _b_ is the number of bumps. It follows from Proposition 9 that the optimized tree can be found in time _O(n_log(_n_)), a complexity identical to the cost of building the tree in the first place.

Before concluding, we should expand slightly on our earlier remark that our ideas are not a panacea; consider the tree in Figure 7 where the nodes are labeled with their respective probabilities..

1.12 1.1 1.08 size as factor of better option unbalanced treap vs balanced weighted unbalanced treap vs unbalanced weighted unbalanced treap vs optimal 1.06 1.04 1.02 1
100 1000 10000 100000 1x106 1x107 tree size

Fig. 5: Comparative performances

