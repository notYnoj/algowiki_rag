**Theorem 3.** _There is a poset selection algorithm using_ \(\mathcal{O}(\mathrm{OPT}(G,k)\cdot\mathrm{loglog}(k/\mathrm{OPT}(G,k)))\) _comparisons for each input_ \((G,k,\prec)\) _when G is a rooted forest where each node of depth less than k has at least one child, and_ \(\mathrm{OPT}(G,k)\le\frac{1}{4}k\).

_Alternatively, the number of comparisons can be bounded by_ O(OPT(_G,k_)logOPT(_G,k_)).

The running time of these two algorithms is O(OPT(_G,k_)+_k_logOPT(_G,k_)).

## 1.1 Technical overview

In this section, we give informal descriptions of our algorithms. We start with some simple approaches, continue with the the soft-heap-based binary-tree selection algorithm of Kaplan, Kozma, Zamir, and Zwick \[KKZZ18\], and then describe our algorithms. In this informal description, we usually focus on _trees_ instead of forests; however, every algorithm for trees can handle forests with simple preprocessing (adding a dummy root).

### Naive selection in trees.

Suppose _G_ is a rooted tree. A simple selection algorithm (cf. \[KKZZ18\]) works as follows: Initialize a priority queue _Q_ (e.g., a binary heap), and insert the root of _G_ into _Q_. Then, repeatedly extract the minimum element from _Q_, and insert all of its children into _Q_. Do this _k_-1 times, and then return the remaining minimum of _Q_. It is easy to see that this extracts, in turn, the smallest element, second-smallest element, and so on, and thus is correct.

What is the running time? Extracting the _k_ smallest elements takes \(\Theta(k\mathrm{log}k)\) time. If _G_ is binary, then we insert two elements for each extracted element, for a total of 2_k_ insertions. Thus, the total running time is \(\Theta(k\mathrm{log}k)\).

If _G_ is not binary, the number of insertions can be much higher. Still, if _Q_ uses an advanced data structure such as a binomial heap \[Vui78\], the total running time is \(\Theta(k\mathrm{log}k+I)\), where _I_ is the number of insertions. It turns out that this is optimal up to the term \(\Theta(k\mathrm{log}k)\), as we show now.

### A basic lower bound for trees.

Fix a tree _G_ and some \(k\in\mathbb{N}_+\). A node set _U_ is called a _prefix_ if it is closed under taking ancestors. Note that the set of smallest _k_ nodes must be a prefix. Consider the prefix _U_ of the _k_-1 smallest nodes, and let _C(G,U_) be the set of children of nodes in _U_ that themselves are not in _U_. Then, finding the _k_-th smallest node is equivalent to finding the _minimum_ of all nodes in _C(G,U_), which takes |_C(G,U_)|-1 comparisons. Let _c(G,k_-1) denote the maximum |_C(G,U_)| over all size-(_k_-1) prefixes. Then \(\mathrm{OPT}(G,k)\ge c(G,k-1)-1\). \[KKZZ18\]

Now consider our naive selection algorithm again. Apart from the _k_-1 smallest elements _U_, the algorithm inserts precisely the nodes _C(G,U_) into _Q_. Thus, we have \(I\le k-1+\mathrm{OPT}(G,k)\), and the running time is O(_k_log_k_+OPT(_G,k_)).

Our goal is to reduce the term _k_log_k_ to _k_. Kaplan, Kozma, Zamir, and Zwick \[KKZZ18\] showed that, for binary trees, this can be done with a simple modification of the algorithm given above, using _soft heaps_.

