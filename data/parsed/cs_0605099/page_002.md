**Definition 1** _An alphabetic tree is a tree with leaves are in numerical order given inorder tree traversal (i.e.,_ 1,2_,...,n from left to right)._

Three papers independently considered the problem of minimizing

\(L_a(w,\mathbf{l})\unknown log_a\sum_{i=1}^nw(i)a^{l(i)}\) (2)

for _a\>_1 [5, p. 254] [10, p. 485] [7, p. 231] for unconstrained (Huffman- like) minimization, the solution of which is very similar to that of Huffman’s algorithm. One of these further noted that an algorithm similar to Hu and Tucker’s solves the alphabetically constrained version of this problem [5], while another noted that the Huffman-like solution also solves the unconstrained (2) for _a\<_1 [7], in which log_<sub>a</sub>x_ is monotonically decreasing and the objective’s summation term is thus maximized.

A recent paper showed that the _a\<_1 problem describes certain situations of single-shot decision-making [1]. Given a window of time corresponding to a memoryless random variable, if we wish to find the leaf of the binary tree through constant-time edge traversal, this is found in time with probability _a<sup>L<sub>a</sub>(w,**l**)</sup>_ -- which we thus wish to minimize -- for some known _a\<_1. However, solving the alphabetic version of this problem remained unaddressed.

Here we present an _O(n_<sup>3</sup>) algorithm for minimizing (2) that is somewhat similar to Gilbert and Moore’s method for (1) [4]. We then introduce counterexamples on attempts to minimize using faster methods, such the modification of Hu and Tucker’s, which only succeeds for _a\>_1. Finally we present approximation algorithms, related to those for the linear problem, which find suboptimal solutions in _O(n_) and _O(n_log_n_), leading to simple bounds for both these solutions and the optimal ones.

## 2 Optimal Alphabetic Trees

Because the alphabetic tree imposes leaf order, each decision of which child to take, represented by a 0 (for left) or 1 (for right), is equivalent to a question of the form, "Is the output greater than or equal to _s_?" where _s_ is one of the possible symbols, a symbol we call the _splitting point_:

**Definition 2** _The splitting point of an internal node (or the corresponding subtree) is the smallest index among the leaves of the right subtree._

**Definition 3** _Each codeword c(i_) _is the sequence of bits corresponding to the sequence of decisions (path) to arrive at leaf i. The overall set of codewords_<tbc>

