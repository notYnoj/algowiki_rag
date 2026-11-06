Sorting Pattern-Avoiding Permutations via 0-1 Matrices Forbidding Product Patterns<sup>∗</sup>

**Abstract**

We consider the problem of comparison-sorting an _n_-permutation _S_ that _avoids_ some _k_- permutation \(\pi\). Chalermsook, Goswami, Kozma, Mehlhorn, and Saranurak [CGK<sup>+</sup>15b] prove that when _S_ is sorted by inserting the elements into the GreedyFuture [DHI<sup>+</sup>09] binary search tree, the running time is linear in the _extremal function_ \(\mathrm{Ex}(P_\pi\otimes(\cdot,\cdot),n)\). This is the maximum number of 1s in an \(n\times n0\)-1 matrix avoiding \(P_\pi\otimes(\cdot,\cdot)\), where \(P_\pi\) is the \(k\times k\) permutation matrix of \(\pi\), and \(P_\pi\otimes(\cdot,\cdot)\) is the \(2k\times 3k\) Kronecker product of \(P_\pi\) and the "hat" pattern \((\cdot,\cdot)\). The same time bound can be achieved by sorting _S_ with Kozma and Saranurak’s SmoothHeap [KS20].

Applying off-the-shelf results on the extremal functions of 0-1 matrices, it was known that

\(\mathrm{Ex}(P_\pi\otimes(\cdot,\cdot),n)=\left\{\begin{array}{ c c } \Omega(n\alpha(n)), & O\big(n\cdot 2^{(\alpha(n))^{3k/2-O(1)}}\big), \\ \Omega(n\alpha(n)), & O\big(n\cdot 2^{(\alpha(n))^{3k/2-O(1)}}\big), \end{array}\right.\)

where \(\alpha(n)\) is the inverse-Ackermann function. In this paper we give _nearly tight_ upper and lower bounds on the density of \(P_\pi\otimes(\cdot,\cdot)\)-free matrices in terms of "_n_", and improve the dependence on "_k_" from doubly exponential to singly exponential.

\(\mathrm{Ex}(P_\pi\otimes(\cdot,\cdot),n)=\left\{\begin{array}{ c c } \Omega\big(n\cdot 2^{\alpha(n)}\big), & \text{for most}\pi, \\ O\big(n\cdot 2^{O(k^2)+(1+o(1))\alpha(n)}\big), & \text{for all}\pi. \end{array}\right.\)

As a consequence, sorting \(\pi\)-free sequences can be performed in \(O(n2^{(1+o(1))\alpha(n)})\) time. For many corollaries of the dynamic optimality conjecture, the best analysis uses forbidden 0-1 matrix theory. Our analysis may be useful in analyzing other classes of access sequences on binary search trees.

## 1 Introduction

The problem of sorting restricted classes of permutations has been studied for decades. Knuth [Knu73] observed that the class of permutations sortable by a stack is precisely the set of (2,3,1)-avoiding permutations; see [Tar72, BGH<sup>+</sup>10, MSS19, HI01, EG17a, EG17b, FP08, AB15, AMR02] and Bóna’s survey [Bón02] for models of restricted sorting devices. In general, an _n_-permutation _S avoids_ a _k_-permutation \(\pi\) if there do not exist indices \(i_1<\cdots<i_k\) for which

\(\forall p,q\in[k].S(i_p)<S(i_q)\Longleftrightarrow\pi(p)<\pi(q).\)

<sup>∗</sup>Supported by NSF grants CCF-1815316 and CCF-2221980 and by the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme under grant agreement No 759557.

Parinya Chalermsook Aalto University

Seth Pettie University of Michigan

Sorrachai Yingchareonthawornchai Aalto University

