### Comparison oracle.

A quantum comparison is the oracle

\(O_x|i,j,c,w\rangle=|i,j,c\oplus\mathbf{1}_{\{x_i<x_j\}},w\rangle,i,j\in[n],\) (1)

where _c_ is a response bit, _w_ is workspace, and **1**<sub>{_x<sub>i</sub>\<x<sub>i</sub>_}</sub>=0. This is the standard comparison oracle on permutations \[23, 24\]. A classical comparison queries one pair and receives the bit **1**<sub>{_x<sub>i</sub>\<x<sub>j</sub>_}</sub>. An admissible quantum algorithm in this instance obeys Definition 1, makes at most _q_ calls to (1) on every branch and outputs one label. Its only access to _x_ is through this oracle. A classical algorithm is an adaptive comparison tree with private randomness and at most _q_ comparisons on every branch. Only oracle calls are charged.

_Remark_ 1. A self-address _i=j_ returns no information about _x_. It is allowed for convenience, and no value in this paper depends on it, because every call already acts as the identity on the \(|+\rangle\) eigenspace of the response bit.

**Definition 2.** For \(q\ge 0\), \(n\ge 1\) and \(0\le r\le n\), the quantum value is

\(Q_q(n,r)=sup_Amin_xPr_x^A[x_I\le r],\) (2)

where _A_ ranges over admissible algorithms with budget _q_ and _x_ over strict orders. The classical value _C<sub>q</sub>(n,r_) is defined in the same way over classical algorithms.

## 3.3 Worst case and average case

The worst-case objective can be analyzed through a uniform random order because an algorithm may randomly relabel designs before making comparisons. The same relabeling is used throughout the run, so the comparison answers remain consistent.

**Proposition 1.** _For every admissible algorithm A there is an admissible algorithm_ \(A'\) _with the same budget whose success on every order equals the success of A averaged over a uniformly random order, and whose whole rank law has the same property. Consequently Q<sub>q</sub>(n,r_) _and C<sub>q</sub>(n,r_) _equal the suprema of the uniform-average success._

_Proof._ Let \(A'\) draw a uniform permutation \(\sigma\) of \[_n_\] from private randomness, and let

\(P_\sigma|i,j,c,w\rangle=|\sigma(i),\sigma(j),c,w\rangle.\)

Then \(P_\sigma^{-1}O_xP_\sigma=O_{x\circ\sigma}\), where \((x\circ\sigma)_i=x_{\sigma(i)}\). Let \(A'\) run _A_ with every call _O<sub>x</sub>_ replaced by \(P_\sigma^{-1}O_xP_\sigma\) and output \(\sigma(I)\). On a fixed order _x_, \(A'\) therefore behaves as _A_ on the order \(x\circ\sigma\), which is uniformly distributed, and the rank of \(\sigma(I)\) under _x_ equals the rank of _I_ under \(x\circ\sigma\). The same \(\sigma\) is used for every call and for the output, so every rank event is uniformized at once. The worst-case success of any algorithm is at most its average success, which gives the second statement.

We average the algorithm over relabelings in Proposition 1, as in the symmetrization of semidefinite programs for ordered search \[27\], whereas Childs and Lee average adversary matrices with the automorphism principle \[34\]. A fresh relabeling between calls would not preserve the oracle answers, and it is not used.

