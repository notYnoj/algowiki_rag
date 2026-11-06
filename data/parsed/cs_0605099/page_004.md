the place of either node, both of which are now (ordered) children. In the original Hu-Tucker algorithm, this item is given weight _w(i_)+_w(j_), whereas for (2) with _a\>_1 it is given weight _aw(i_)+_aw(j_). The algorithm then finds the minimum weighted pair among those pairs of distinct items (uncombined input leaves and combined items) without any _uncombined_ leaf between them, placing the resulting node in the place of either original node. Continuing on, we obtain a tree that is not necessarily alphabetical, but which has the same lengths as an alphabetic tree which can be easily reconstructed, (optimally) solving the problem (for _a\>_1).

However, consider again _a_=0.6, this time for weights (8,1,9,6,2). The Hu- Tucker-like algorithm first combines 6 and 2, then 8 and 1, then the first combined node with 9, and finally the remaining two nodes, resulting in a tree with lengths \(l'=(2,2,2,3,3)\) and \(L_a(w,l')\approx-4.121\). However, a tree with lengths \(l''=(1,3,3,3,3)\), having \(L_a(w,l'')\approx-4.232\), shows that the Hu-Tucker-like solution is nonoptimal.

**Result 1** _Knuth’s method for speeding up dynamic programming fails for a\<_1_, as does using the Hu-Tucker-like method optimal for a\>_1.

## 3 Approximation Algorithms and Bounds

In this section, we add the assertion \(\sum_{i=1}^nw(i)=1\) to our problem, which can be considered an optimization of (2) with constraints:

1. The Kraft inequality of binary trees, \(\sum_{i=1}^n2^{-l(i)}\le 1\);<tbc>

2. The integer constraint, \(l(i)\in\mathbb{Z}\);<tbc>

3. The alphabetic constraint.<tbc>

<tbc>The first and second of these are necessary and sufficient for the lengths to correspond to a binary tree. Relaxing the second and third allows for a numerical solution which can bound the performance of the optimal solution. The numerical solution, _l_<sup>†</sup>, shown by Campbell \[2,3\], results in the Shannon-like

\(l^\mathrm{s}(i)\unknown\lceil l^\dagger\rceil=\left[-\frac{1}{1+\mathrm{log}_2a}\mathrm{log}_2w(i)+\mathrm{log}_2\left(\sum_{j=1}^nw(j)^\frac{1}{1+\mathrm{log}_2a}\right)\right]\)

a valid (but not necessarily optimal) solution to the problem with only the alphabetic constraint relaxed, that is, the Huffman-like problem.

The approximation algorithm in Fig. 3 has a linear-time variant patterned after that in \[11\] -- relying on **_l_**<sup>s</sup> -- and a _O(n_log_n_)-time variant patterned after \[9\] -- instead using **_l_**<sup>h</sup>, those lengths obtained from solving the optimal<tbc>

