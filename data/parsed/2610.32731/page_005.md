<tbc>number of insertions so far and _W_<sub>corrupted</sub>, _W_<sub>deleted</sub> are the total weights of currently corrupted, resp. previously deleted elements.

Note that the corruption invariant involves the weights of corrupted and deleted elements, but only the _number_ of inserted elements. This is crucial for our application and should be interpreted as insertion being always cheap (in terms of both running time and corruption), but deletion being expensive for heavy elements.

Implementing WSHs is quite simple: Use a classical soft heap, and whenever an element gets corrupted that should not, re-insert it. Do this a number of times up to the weight of the element, after which the element is considered corrupted in the WSH.

Our O(_k_+OPT) algorithm for _trees_ uses essentially the same strategy as the algorithm of [KKZZ18], but with a WSH, where the weight of an element is the number of its children plus one. The analysis goes roughly as follows. The running time, including heapification, is linear in the total degree (= weight) of deleted or corrupted elements. The number of inserted elements is O(_k_) due to heapification, and the total weight of deleted elements is bounded by \(c(G,k-1)\le\mathrm{OPT}(G,k)\). Finally, the WSH invariant implies that the total weight of corrupted elements is bounded by the previous two quantities.

## A poset algorithm.

Extending the O(_k_+OPT) WSH-based algorithm to arbitrary posets is not trivial. First, the lower bound needs to adapted, which is fairly simple: _c(G,k_-1) is the maximal number of sources obtained by removing some prefix of size _k_-1 from _G_. It is not hard to see that _c(G,k_-1)-1 is a lower bound on the number of comparisons needed to find the _k_-th smallest element. With this, it is also not hard to obtain a O(_k_log_k_+OPT) algorithm using a binomial heap.

However, to generalize our WSH-based algorithm, we need a different notion of weights. An obvious idea would be to use out-degree as the weight, analogously to how we used degree for trees. Unfortunately, this does not work. For trees, deleting or corrupting a node adds all of its children as "candidates" for the next-largest element. In posets, the set of these candidates depends on which elements we previously removed or corrupted.

The solution is to use a _dynamic_ weight. At any point, the weight of a node _v_ is the number of new candidates added after deleting or corrupting _v_, which are precisely the out-neighbors of<tbc>

k
k
k
- 3
k

Figure 2: An example tree where _c(G,k_-1)=_k_+2 and _c(G,_2_k_-2)=_k_<sup>2</sup>+1. The blue nodes form a prefix of size _k_-1. Adding the _k_-1 nodes in red causes _c(G,_2_k_-2) to rise to _k_<sup>2</sup>+1. The path at the bottom ensures that all nodes could be the _k_-th smallest node.

