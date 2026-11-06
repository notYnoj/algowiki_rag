can be viewed as a way to apply the powerful techniques for undirected graphs to the more difficult setting of directed graphs. Indeed, the recent interior point method-based flow algorithms [CKL<sup>+</sup>25, VDBCK<sup>+</sup>24] all adopt this strategy to great success: each iteration reduces to a problem on an undirected graph, which is solved quickly by dynamic data structures.

Finally, one limit to the current balancing weights approach is the requirement that the graph is strongly connected. We leave as an open question whether the technique can be extended to general directed graphs. One difficulty in handling cuts with no arcs in one direction is that the arcs in the other direction may have their weights approaching 0, which means that **y**(_v_)-**y**(_u_) becomes arbitrarily large. One possible approach is to employ a "softer" weight function to control the potential differences as the weights tend to 0.

### Acknowledgement

The author thanks Satish Rao for many insightful discussions.

## References

