## A better algorithm with soft heaps.

A soft heap is a priority queue that performs _all_ operation in O(1), at the cost of _corrupting_ some elements. The soft heap may arbitrarily increase the keys of corrupted elements. This means that `find-min` and `extract-min` may not return the actual minimum; however, they are guaranteed to return some element that is smaller than all _uncorrupted_ elements.

The number of corrupted elements in the soft heap is guaranteed to be at most \(\varepsilon\cdot I\) at all times, where \(\varepsilon\) is a positive constant chosen by the user, and _I_ is the number of insertions so far. Note that, in particular, when inserting _I_ elements and then deleting \((1-\varepsilon)I\) elements, _all_ elements in the soft heap may be corrupted, rendering it useless.

Simply replacing the priority queue in the O(_k_log_k_) algorithm with a soft heap will not immediately yield a correct algorithm. However, \[KKZZ18\] considered the following adjustment. Recall that whenever we extract an element from the priority queue _Q_, we insert all of its children into it. Whenever an element gets _corrupted_, we similarly insert its children into _Q_ (but the element itself remains in _Q_). In the case that _G_ is a binary tree, \[KKZZ18\] showed that with a small enough error parameter \(\varepsilon\), the overall number of corruptions and child insertions is O(_k_). Moreover, the _k_-th smallest element must be one of the O(_k_) elements that were extracted or corrupted. Thus, we can use a linear-time selection algorithm such as median-of-medians \[BFP<sup>+</sup>73\] in the end to find the _k_-th element. The overall running time is O(_k_), which is optimal for binary trees.

Now consider general trees. The first problem is that when corrupting a large-degree vertex, we need to insert all of its children into the soft heap, which breaks the delicate balance of corrupted elements. \[KKZZ18\] solve this with a technique they call _on-the-fly ternarization via heapification_, where parts of the input tree are progressively made ternary, so only three nodes per corruption are inserted. In this way, they can limit the number of corrupted elements to \((1+\delta)k\) for any delta. However, they still need to inspect all children of each extracted or corrupted node. Since there are \(k+(1+\delta)k\) such nodes, the total running time can be bounded by \(\mathcal{O}(k+c(G,(2+\delta)k))\).

This may seem close to optimal. Unfortunately, there exist trees _G_ such that \(c(G,k-1)\le\mathcal{O}(k)\), but \(c(G,2k)\ge\Omega(k^2)\) (see fig. 2).<sup>4</sup> Thus, in terms of OPT, no bound better than O(_k_+OPT<sup>2</sup>) holds. Still, for certain trees with a somewhat uniform structure, this bound can be sufficient. Recently, Sandlund and Zhang \[SZ22\] used this algorithm to select from binomial heaps and Fibonacci heaps, and showed that, in that case, \(c(G,3k)\le\mathcal{O}(c(G,k))\).

## Weighted soft heaps.

To improve the running time of the above algorithm, it is necessary to avoid corrupting elements with many children. To this end, we devise a novel soft heap variant that we call the _weighted soft heap_ (WSH). When inserting an element into a WSH, it is assigned a positive integer _weight_. Assigning a higher weight increases the running time of deleting the element, but also makes it harder for the soft heap to corrupt it.

More precisely, the running time for deleting a weight-_w_ element is O(_w_), while all other operations remain O(1). At any point, we have \(W_\mathrm{corrupted}\le\varepsilon(I+W_\mathrm{deleted})\), where _I_ is the<tbc>

<sup>4</sup>In fact, _c(G,_2_k_) can be arbitrarily large. However, \(c(G,2k)>\omega(k^2)\) can only happen when including nodes of depth larger than _k_ (none of which could be among the _k_ smallest nodes).

