# Alphabetic Coding with Exponential Costs<sup>⋆</sup>

**Abstract**

An alphabetic binary tree formulation applies to problems in which an outcome needs to be determined via alphabetically ordered search prior to the termination of some window of opportunity. Rather than finding a decision tree minimizing \(\sum_{i=1}^nw(i)l(i)\), this variant involves minimizing \(log_a\sum_{i=1}^nw(i)al^{l(i)}\) for a given \(a\in(0,1)\). This note introduces a dynamic programming algorithm that finds the optimal solution in polynomial time and space, and shows that methods traditionally used to improve the speed of optimizations in related problems, such as the Hu-Tucker procedure, fail for this problem. This note thus also introduces two approximation algorithms which can find a suboptimal solution in linear time (for one) or _O(n_log_n_) time (for the other), with associated coding redundancy bounds.

_Key words:_ Approximation algorithms; dynamic programming; information retrieval; Rényi entropy; tree searching

### 1 Introduction

Applications such as searching [8] and coding theory [6] make extensive use of binary trees. We denote the length (number of edges) of a path from the root to node \(i\in\{1,2,\dots,n\}\) of the tree as _l(i_), and the weight (usually probability) of the leaf as _w(i_). Given a set of weights, Huffman’s algorithm [6] finds a tree minimizing cost function

\(\sum_{i=1}^nw(i)l(i)\) (1)

and Hu and Tucker’s algorithm [5] finds an optimal _alphabetic_ tree:

<sup>⋆</sup> Material in this paper was presented at the 2006 International Symposium on Information Theory, Seattle, Washington, USA. _Email address:_ `calbear@ieee.org` (Michael B. Baer).

Michael B. Baer

