<tbc>selection from column-sorted matrices. Note that this corresponds to poset selection when the poset is a collection of equal-length chains. The same authors \[FJ84\] studied selection from collections of row- and column-sorted matrices, which corresponds to another set of highly structured partial orders. Frederickson \[Fre93\] gave an algorithm for selection from a _binary min-heap_, or, more generally, a _t_-nary min-heap. This corresponds to the case where _G_ is a rooted tree where each inner node has degree _t_.<sup>3</sup>

Kaplan, Kozma, Zamir, and Zwick utilized Chazelle’s _soft heaps_ \[Cha00, KTZ13, Bro21\] to simplify several older results, including the optimal algorithms for column-sorted matrices and _t_-nary heaps. They also gave a simple, though not optimal, algorithm for general trees (see section 1.1). We refer to their paper for several applications of selection in these special cases.

In contrast to this somewhat sparse set of results, the corresponding poset _sorting_ problem has been solved in its full generality with an optimal O(log_e(P_)) comparisons, where _e(P_) denotes the number of linear extensions of _P_ \[Kis68, Fre76, Lin84, KK92, BFT95, CFJ<sup>+</sup>10, vR24, HHI<sup>+</sup>25, vdHRR25, Rut26\].

In this paper, we develop an algorithm for selection with arbitrary posets. For a DAG _G_ and a number \(k\le|V(G)|\), let OPT(_G,k_) denote the minimum number of comparisons that any algorithm needs to solve a worst-case instance \((G,k,\prec)\). Note that here _G_ and _k_ are fixed, but the comparison oracle \(\prec\) is chosen to be worst possible for the given algorithm. Our main result is:

**Theorem 1.** _There is a poset selection algorithm using_ O(_k_+OPT(_G,k_)) _comparisons for each input_ \((G,k,\prec)\).

When _G_ is a rooted forest, the _running time_ of this algorithm is also O(_k_+OPT(_G,k_)). This assumes a simple pointer-representation of _G_, where the degree of each node can be determined in constant time. If _G_ is a general DAG, we cannot bound the running time only in terms of _k_ and OPT(_G,k_), but it is linear in the size of _G_.

Our algorithm is not optimal when \(\mathrm{OPT}(G,k)\checkmark k\). In fact, it can be arbitrarily far from optimal in that case. When _G_ is a forest, we obtain some improved algorithms in the case \(\mathrm{OPT}(G,k)\checkmark k\):

**Theorem 2.** _There is a poset selection algorithm using_ \(\mathcal{O}(\mathrm{OPT}(G,k)\cdot\mathrm{log}(k/\mathrm{OPT}(G,k)))\) _comparisons for each input_ \((G,k,\prec)\) _when G is a rooted forest and_ \(\mathrm{OPT}(G,k)\le\frac{1}{2}k\).

<sup>3</sup>We interpret a rooted tree or forest as a DAG where all edges are directed away from the root. That is, the set of roots of the forest are the minima of the corresponding poset.



Figure 1: Three special cases of the poset selection problem. _Left:_ Zero comparisons are needed for all _k_. _Center:_ \(\Theta(\mathrm{log}n)\) comparisons are needed \[KKZZ18\]. _Right:_ Zero comparisons are need for \(k\le 5\), but \(\Theta(n)\) for \(k\ge 6\).

