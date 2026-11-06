\begin{tabular}{ccccc}
Search Sequence & Forbidden Pattern & Splay & Greedy & Citation \\
Sequential & (21)-free & _O(n_) & _O(n_) & \[Tar85\] \\
Deque & {(213),(231)}-free & \(O(n\alpha^*(n))\) & \(O(n\alpha(n))\) & \[Pet08, CGJ<sup>+</sup>23\] \\
Preorder & (231)-free & -- & \(O(n2^{\alpha(n)})\) & \[CGJ<sup>+</sup>23\] \\
Postorder & (312)-free & -- & _O(n_) & \[CGJ<sup>+</sup>23\] \\
_k_-Increasing & (_k,...,_2,1)-free & -- & \(O(\mathrm{min}\{nk^2,nk\alpha(n)\})\) & \[CGJ<sup>+</sup>23\] \\
_k_-Recursively

decomposable & avoids all _simple_

(_k_+1)-permutations & -- & _O(n_log_k_)

(_prepr. initial tree_) & \[GG19\] \\
_k_-Permutation

avoiding & \(\pi\)-free & -- & \(O(\mathrm{Ex}(P_\pi\otimes(\bullet),n))\) & \[CGK<sup>+</sup>15b\] \\
\end{tabular}

[CGKMS 2015]
k-permutation avoiding
k-recursively decomposable
k-increasing
[Sleator, Tarjan 1985]
preorder traversal
postorder traversal
deque
sequential

Figure 1: Relation between classes of search sequences. The upper class contains the lower ones.

1: Upper Bounds on Structured Search Sequences

