## 5 Conclusion and future work

The techniques that we have described appear to lead to clear and measurable improvements in access times for binary trees, but only scratch the surface of potential applications. Some obvious candidates for future work:

### Non-binary trees

There is no reason to restrict our ideas to binary trees; any data structure where a similar measure of merit can be computed locally should be amenable to similar treatment.

### Unbalancing restrictions

It is possible to apply additional constraints when selecting a node to bump. As an example, if we begin with a binary tree where the maximum node depth is _d_, we could require that no node can be bumped if it pushes another node below depth _d_. This would lead to guaranteed performance improvements with no impact on worst-case performance. We could also obviously limit the maximum depth of a post-bump node in some less restrictive way. Since it is possible to compute and maintain _d(<o>x</o>_) for each node _x_, the impact on computational expense should be minimal.<sup>3</sup>

### Termination before quiescence

Alternatively, one could limit the number of bumps to be a sublinear function of tree size in some way, although this may be difficult without significantly impacting performance. Figure 8, for example, shows performance both for optimized treaps and for treaps where at most 1000 bumps were permitted before the optimization was stopped. As can be seen, allowing our methods to proceed until quiescence provides significant improvement without changing the overall complexity of constructing the tree. Of course, we have no _guarantee_ that the number of bumps will be linear in tree size, and we could obviously limit the number of bumps to (say) 50% of the number of nodes in the tree. Given the "maximum" curve in Figure 6, doing so would not impact any of the results we have presented.

### Multiple bumps

One can imagine situations where bumping a node once degrades overall performance, but bumping it twice provides an improvement. In general, updating the merits after a single bump involves recomputing values for 5 nodes; updating the merits after a bump of _l_ levels will involve recomputing values for 2_l_+3 nodes.

It follows that as long as the depth of the tree is bounded at some fixed multiple of log(_n_), we can consider not just single bumps but bumps of any number of levels and only add a factor of log(_n_) to the worst-case running time. Of course, given that we are producing trees with search costs within 1% of optimal, the additional complexity of such considerations may not be warranted.

Testing all of these ideas should be straightforward.

<sup>3</sup> But not zero. It is possible that a rotation pushes a node lower in the search tree, disallowing a future bump that would otherwise have been permitted. This may then require extending the heap of best future bumps.

