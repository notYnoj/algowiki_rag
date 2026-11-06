# Rotation distance using flows

**Abstract**

Splay trees are a simple and efficient dynamic data structure, invented by Sleator and Tarjan. The basic primitive for transforming a binary tree in this scheme is a rotation. Sleator, Tarjan, and Thurston proved that the maximum rotation distance between trees with _n_ internal nodes is exactly 2_n_-6 for trees with _n_ internal nodes (where _n_ is larger than some constant). The proof of the upper bound is easy but the proof of the lower bound, remarkably, uses sophisticated arguments based on calculating hyperbolic volumes. We give an elementary proof of the same result. The main interest of the paper lies in the method, which is new. It basically relies on a potential function argument, similar to many amortized analyses. However, the potential of a tree is not defined explicitly, but by constructing an instance of a flow problem and using the max-flow min-cut theorem.

### 1 Introduction

Background. Splay trees are a simple and efficient dynamic data structure, invented by Sleator and Tarjan [1]. The basic primitive for transforming a binary tree in this scheme is a _rotation_ (see figure 1). The way in which

\*AUTHOR’S NOTE: Bill Thurston and I composed this extended abstract in 1992. The proof is an outline that was meant to be completed in a subsequent full paper. This work was set aside, and after a time no complete copy of this abstract was known to exist. A copy was recently found, and I am making it available now, for information purposes. -- Claire Mathieu, 25 August 2024

Claire Mathieu

William P. Thurston

1992 <sup>∗</sup>

