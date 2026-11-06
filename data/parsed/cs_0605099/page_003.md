_-- alphabetic code C -- fully describes the tree, as does length vector **l**, the sequence of lengths_ {_l(i_)}.

The dynamic programming approach of Gilbert and Moore \[4\] is adapted to this problem (2):

**Theorem 1** _An algorithm finds the maximum tree weight W<sub>j,k</sub> (and corresponding optimum tree) for items j through k for each value of k-j from_ 0 _to n_-1 _(in order), by computing inductively_

\(W_{j,k}\leftarrow amax_{s\in\{j+1,j+2,\dots,k\}}[W_{j,s-1}+W_{s,k}]\text{\textit{starting with}}W_{j,j}\leftarrow w(j)\) (3)

_for_ \(1\le j<k\le n\) _in O(n_<sup>3</sup>) _time and O(n_<sup>2</sup>) _space._

**Proof** Recall first that maximizing \(a^{L_a(w,\mathbf{l})}=\sum_iw(i)a^{l(i)}\) minimizes _L<sub>a</sub>(w,**l**_), which is why (3) is a maximization operation. One can see that _W_<sub>1_,n_</sub>=_a_<sup>_L<sub>a</sub>(w,**l**_)</sup> inductively by considering a (sub)tree’s two subtrees as independent, rooted trees, one with summation \(W_{1,s-1}=\sum_{i=1}^{s-1}w(i)a^{l(i)-1}\), the other with summation \(W_{s,n}=\sum_{i=s}^nw(i)a^{l(i)-1}\). Then _W_<sub>1_,n_</sub>=_a(W_<sub>1_,s_-1</sub>+_W<sub>s,n</sub>_). Starting with _W<sub>j,j</sub>=w(j_), then, we see that these values can be built up accordingly (since the path length from a leaf to itself is 0, _W<sub>j,j</sub>=a_<sup>0</sup>_w(j_), and there is nothing numerically special about the final tree). Since all subtrees of an optimal tree are optimal -- via a substitution argument, e.g., \[8\] -- the maximization finds an optimal solution. This suggests the dynamic programming algorithm; similarly to \[8\], calculating all optimal subtrees of a size less than that of the (sub)tree in a current step, we can try all possible splitting points using optimal subtrees, yielding the optimal tree.

_O(n_<sup>2</sup>) items are stored -- _O(n_<sup>2</sup>) weights for every possible range and the associated splitting points; these are used to recursively find the implied subtree -- calculated by testing _O(n_) splitting points for each internal node, thus the time and space complexity.

Knuth \[8\] reduced the algorithmic complexity of Gilbert and Moore’s method for (1) by using the fact that the splitting point of an optimal tree of size _n_ must be between the splitting points of the two optimal subtrees of size _n_-1. With (2), this no longer holds. Consider _a_=0.6 with input weights _w_=(8,1,9,6). The splitting point of (8,1,9) is _s_=3(_w(s_)=_w_(3)=9, yielding subtrees with (8,1) and (9)), and the splitting point of (1,9,6) is _s_=4(_w(s_)=6). However, the optimal splitting point of (8,1,9,6) is _s_=2(_w(s_)=1).

Similarly, for (2) with _a\>_1 \[5\], there is a procedure based on the Hu-Tucker algorithm for finding an optimal alphabetic solution. The Hu-Tucker algorithm begins with the input weights arranged as leaves in numerical order (1,2_,...,n_ in a line). It then combines the two items _i_ and _j_ that, of all pairs of items without a leaf separating them, have a minimum weight sum, putting it in<tbc>

