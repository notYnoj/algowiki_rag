<tbc>_v_ that have no other in-neighbors in the WSH (see fig. 3). This weight may increase over time (but can never decrease). Accordingly, the WSH implements another operation that allows increasing the weight of an element. There are some further complications that we omit here. In the end, we obtain an algorithm with O(_k_+OPT) comparisons (theorem 1).

## An almost-optimal algorithm for trees.

\[KKZZ18\] gave an optimal algorithm for the case where the input tree _G_ is a union of _m_ directed paths, each of length at least _k_. In this case, the optimum OPT(_G,k_) is \(\mathcal{O}(mlog\frac{k}{m})\), which can be much smaller than _k_.

The algorithm proceeds in \(\mathcal{O}(log\frac{k}{m})\) steps, each of which identifies and deletes \(\approx\frac{1}{2}k\) of the smallest _k_-1 elements. Each step takes O(_m_) time. Doing this \(\mathcal{O}(log\frac{k}{m})\) times reduces _k_ to O(_m_), after which a simple O(_k+m_) algorithm is applied (the latter is based on the binary-tree algorithm).

A single step works by partitioning each path into _blocks_ of size \(\approx\frac{1}{2}\frac{k}{m}\), and running the O(_k+m_) algorithm with \(k\leftarrow m\) on _representatives_ of these blocks, identifying the smallest _m_ block representatives, corresponding to \(\frac{1}{2}k\) elements. Due to the error introduced by lumping together elements into blocks, these elements are not necessarily the smallest. However, it can be shown that all these elements are among the _k_-1 smallest, which means they can be removed.

Inspired by this, we give a faster algorithm for arbitrary trees (and forests). Suppose we know the quantity _c(G,k_-1) in advance. Set _m=c(G,k_-1), and partition each induced path of length _\>m_ in _G_ into blocks of size _m_.

Now start running our O(_k_+OPT) algorithm on _G_, with two main changes. First, ignore all nodes in a block but the lowest (i.e., when encountering a block, jump ahead to its lowest node). Second, recall that the original algorithm performs _k_-1 iterations (each deleting a node from the WSH, then inserting new nodes). Instead, here we continue iterating until we have deleted a constant fraction of the _k_ smallest nodes. Importantly, for this we not only consider nodes deleted from the WSH, but also all nodes in the same block of these nodes, that we "jumped over" earlier.

It can be shown that this runs in O(_m_) time. Finding _m≈c(G,k_-1) can be done with a simple exponential search. Doing this \(\mathcal{O}(log\frac{k}{m})\) times reduces _k_ to _m_, and we can use our O(_k_+OPT) algorithm to actually select the _k_-th smallest element. The total running time is \(\mathcal{O}(mlog\frac{k}{m}+\text{OPT})\). Since \(m\le\mathcal{O}(\text{OPT})\), theorem 2 follows.

