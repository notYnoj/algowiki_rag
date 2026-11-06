## 1.2 Pattern-avoidance and the Dynamic Optimality Conjecture

The original _dynamic optimality conjecture_ \[ST85\] states that the (online) Splay BST is _O_(1)- competitive with the optimum offline BST, for any sequence with length \(\Omega(n)\). Today dynamic optimality usually refers to the conjecture that _there exists_ an _O_(1)-competitive BST, with Greedy / GreedyFuture \[Luc88, Mun00, DHI<sup>+</sup>09\] and Splay being the foremost candidates.

It is an open problem to prove _o_(log_n_)-competitiveness for Splay or Greedy, though some _corollaries_ of dynamic optimality have been proved \[ST85, Tar85, Col00, CMSS00, IL16, CGJ<sup>+</sup>23, LT19\]. Many corollaries of dynamic optimality can be characterized by forbidden patterns. For example, the optimum BST executes all of these sequences in linear time.<sup>3</sup>

**Sequential.** The sequential access sequence _S_=(1,2_,...,n_) avoids (2,1).

**Deque.** In a deletion-only deque sequence, _S(i_) is either the minimum or maximum of {_S(i),S(i_+1)_,...,S(n_)}. Deque sequences avoid {(213),(312)}. (In a deque, the accessed elements are also typically deleted from the tree \[Sun92, Pet08\].)

**Preorder and Postorder.** Let _R_ be any BST over {1_,...,n_} and _S_ be a preorder (or postorder) traversal of _R_. Then _S_ avoids (231) (or (312)). (The _Traversal Conjecture_ of Sleator and Tarjan \[ST85\] concerned preorder sequences. If the accessed elements in a preorder sequence are moved to the root and _deleted_, yielding two trees, this corresponds with Lucas’s definition of _Split_-sequences \[Luc91\].)

_k_**-Increasing.** _S_ can be decomposed into (_k_-1) increasing subsequences, or equivalently, _S_ avoids (_k,...,_2,1).

_k_**-Recursively Decomposable.** A permutation _S_ is _k_-recursively decomposable if (i) the 1s of the corresponding permutation matrix _A<sub>S</sub>_ can be partitioned into _k_ non-overlapping rectangles, and (ii) those rectangles are themselves _k_-recursively decomposable, where in the base case, any \(1\times 1\) matrix is _k_-recursively decomposable. These sequences avoid all _simple_ (_k_+1)- permutations.<sup>4</sup>

Figure 1 shows the relationship between the classes of permutations, and  1 gives some known upper bounds on the performance of Splay and Greedy. In particular, our new upper bound on \(\mathrm{Ex}(P_\pi\otimes(\bullet,n)\) improves on the bounds for _k_-recursively decomposable sequences (when preprocessing is not allowed), and _k_-permutation avoiding sequences.

## 1.3 Organization

In Section 2 we review forbidden 0-1 matrix terminology, and some key results. In Section 3 we prove Theorem 1.3, establishing the \(n2^{(1+o(1))\alpha(n)}\) upper bound on \(P\otimes(\bullet,)\)-type matrices. In Section 4 we prove Theorem 4.5’s \(\Omega(n2^{\alpha(n)})\) lower bound on _W_-free matrices. Section 5 presents some additional upper bounds, on \(I_k\otimes(\bullet,)\)-free matrices (Theorem 1.5) and matrices avoiding _W_ and its reflection. We conclude with some open problems in Section 6.

<sup>3</sup>Note that the problem we study in this paper is not on this list. There is no published proof yet to the effect that "accessing a \(\pi\)-avoiding _S_ in \(O_\pi(n)\) time" is a corollary of dynamic optimality. The \(O_\pi(n)\)-height decision-tree implied by Fredman \[Fre76\] is not obviously implementable as a dynamic binary search tree. <sup>4</sup>A (_k_+1)-permutation \(\pi\) is _simple_ if there is no interval \(I\subset\{1,\dots,k+1\}\) with \(|I|\in[2,k]\) such that \(\pi(I)=^\mathrm{def}\{\pi(j)|j\in I\}=I\).

