determine the input permutation. To complete the sort a sequence of cyclic exchanges then reorder the data. These are often simplified into a sequence of two-element swaps. At N\>5 the decision tree’s size makes it impractical in production settings. At N=3 all solutions require a tree having height=3, leaves=6. The tree show below is optimal in that the two comparison descents occur with M[0]\<=M[1]\<=M[2] or M[0]\>=M[1]\>=M[2] i.e., termination occurs early with presorted (ascending or descending) elements:

if mem[0] <= mem[1] then

if mem[1] <= mem[2] then return // 0 1 2

else if mem[0] <= mem[2] then return // 0 2 1

else return // 2 0 1

else if mem[1] >= mem[2] then return // 2 1 0

else if mem[0] >= mem[2] then return // 1 2 0

else return // 1 0 2

This network is widely quoted [ref]. In the first two steps we either establish mem[0]\<=mem[1] and mem[1]\<=mem[2] and gain mem[0]\<mem[2] by transitivity (is sorted). Otherwise, at the first ELSE mem[1] has largest rank; we need merely disambiguate the ranks of nonadjacent mem[0] and mem[2]. The second half follows by symmetry.

For larger N we can establish that mem[i]\<mem[i+1] in N-1 steps but this set of comparisons does not lead to an optimal (balanced) decision tree. In the code seen above exchanges complete the sort. For the respective six leaves, these are the exchanges { nil; (1,2); (1,2),(0,1); (0,2); (0,1),(1,2); (0,1); }.

By contrast, compare-exchange sorting networks order an array by performing a fused compare and conditional-exchange operation. They are ideally suited to sorting arrays of integers of fixed small size (N = 1..25 typical) where the decision making overhead of more general methods (tree traversal using comparison and bifurcation) will diminish or even negate any reduction in total machine comparisons. An integer compare is typically a single machine instruction. While compact and efficient, a general methodology for the creation of optimal fixed compare-exchange networks remains elusive.

Worst, lack of suitable metrics may lead to sub-optimal networks. Below are two simple networks for N=3. At (a) we recode based on the above algorithm. At (b) we apply Batcher’s even-odd construction for an odd number of elements, applying central symmetry (of inversion) to the right and left halves.

\begin{tabular}{cc}
\multicolumn{2}{c}{\<|unk|\> 1.67} \\
\multicolumn{2}{c}{\<|unk|\> 1.5 | 1.33} \\
\multicolumn{2}{c}{\<|unk|\> 3/1.5 3/1.5} \\
\end{tabular}

