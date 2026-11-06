<tbc>splay trees evolve during a sequence of transformations is still not well understood, as witnessed by the resistance of the dynamic optimality conjecture to all efforts so far. In an attempt to understand how rotations act on trees, Sleator, Tarjan and Thurston addressed the question of computing the rotation distance between binary trees, i.e. the minimum number of rotations required to transform a given tree into another given tree [2]. They proved that the maximum distance is exactly 2_n_-6 for trees with _n_ internal nodes (where _n_ is larger than some constant). The proof of the upper bound is easy but the proof of the lower bound, remarkably, uses sophisticated arguments based on calculating hyperbolic volumes.

## Results.

In this paper, we give an elementary proof of the same result, using the max-flow min-cut theorem instead of hyperbolic geometry. One advantage of the proof is that we exhibit two "natural trees" which are at maximum distance apart, namely two variants of the "zig-zag" tree. (In the original proof, the two trees are not explicitly defined).

## The proof method.

The main interest of the paper lies in the method, which is new. It basically relies on a potential function argument, similar to many amortized analyses. However, the potential of a tree is not defined explicitly (as is usually the case in an amortized analysis), but by constructing an instance of a flow problem and using the max-flow min-cut theorem. It is also interesting to see an example of a problem where potential functions can be used for proving lower bounds and not only upper bounds.

## Comparing the two methods.

Our proof has the obvious advantage of being purely combinatorial, so that it is essentially self-contained.

C
A
A
B
B
C

Figure 1: Rotating an edge of a binary tree.

