### A better algorithm for _k_-unbounded trees.

An improvement over the above algorithm can be obtained as follows: Instead of choosing _m_ once, let the _i_-th step use \(m\approx c(G_i,\frac{1}{2}k_i)\), where _G<sub>i</sub>_ is the remaining forest, and _k<sub>i</sub>_≈2<sup>-_i_</sup>_k_ is the _current_ value of _k_. The analysis above also works with this choice of _m_.

The total number of comparisons is now \(\mathcal{O}(\sum m_i)\). In the worst case, like when _G_ is a collection of _m_ paths, we have _m<sub>i</sub>=m_ for each _i_, so the total running time is still \(mlog\frac{k}{m}\). However, this is in fact optimal for this particular graph _G_, by an information-theoretic argument \[KKZZ18\]. Observe that the algorithm is also optimal when _m<sub>i</sub>_ is exponentially increasing in _i_.

This begs the question on whether we can use information theory to show optimality for arbitrary _G_. At present, we do not know whether this is possible, but we can prove a better running time for a certain natural class of trees.

Say a tree is _k-unbounded_ if each node of depth less than _k_ has at least one child. That is, each leaf has depth at least _k_. Consider now a prefix _U_ of size \(\frac{1}{2}k\). Removing _U_ from _G_ yields a forest \(G'\) with \(m=c(G,\frac{1}{2}k)\) roots, each of which has at least \(\frac{1}{2}k\) descendants (since _G_ is _k_-unbounded). Solving the instance (_G,k_) is as least as hard as solving \((G',\frac{1}{2}k)\). For the latter, a simple information-theoretic argument (cf. \[KKZZ18, Theorem 12\]) yields a lower bound of \(\Omega(mlog\frac{k}{m})\).

We apply this lower bound to each step of the algorithm, and take the largest of all these lower bounds. A relatively simple calculation then bounds the number of comparisons \(\mathcal{O}(\sum m_i)\) by O(OPTloglog(_k/_OPT)).

Finally, it can be shown that \(OPT\ge\mathcal{O}(logk)\) in all but some degenerate cases (which can be handled separately). Thus, the number of comparisons O(OPTlogOPT).

### Organization of this paper.

We finish the introduction by discussing related work below. In section 2, we fix some notation. Then, we prove lower bounds for poset selection in section 3 and describe our central tool, weighted soft heaps, in section 4. We proceed with our algorithms: A simpler O(_k_+OPT) algorithm for forests in section 5, the general algorithm (theorem 1) in section 6, and the algorithms for forests with \(OPT\checkmark k\) (theorems 2 and 3) in section 7.

## 1.2 Related work

Selection has been studied under constraints that are not posets. Perhaps the most prominent example is the _X+Y_ selection problem. Here, two sets _X_ and _Y_ of reals and a number \(k\le|X|\cdot|Y|\) are given, and the task is to select the _k_-th smallest element in the set \(X+Y=\{x+y|x\in X,y\in Y\}\). An optimal algorithm for _X+Y_ selection was given by Frederickson and Johnson \[FJ82\] and simplified by Kaplan, Kozma, Zamir, and Zwick \[KKZZ18\].

Another restricted selection problem is _slope selection_, where we are given a set of points and need to select the line through two points with _k_-smallest slope. The complexity of this problem is known to be \(\Theta(nlogn)\) \[CSSS89, Mat91\]; compare this to the \(\Theta(n^2)\) available lines.

_Multiple selection_ is a generalization of selection where multiple ranks _k_<sub>1</sub>_,k_<sub>2</sub>_,..._ are given that have to be selected at once. An optimal algorithm for the (unconstrained) multiple selection problem is known \[DM81, Pro95, Pan03, KMMS05\]. To the author’s knowledge,<tbc>

