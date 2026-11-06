_Proof._ We use the familiar idea that feasibility of edge- versus node-disjoint paths are equivalent in maximum degree three instances. If _H_ has a node-disjoint solution in \(G''\), then by planarity, there is an uncrossed edge-disjoint solution in _G_. We obtain an edge-disjoint solution in _G_ by first contracting the new 4 cycles. This cannot create a crossing at the contracted node due to the fact we had a node-disjoint solution. Second, consider one of the nodes _v_ where we applied triangle operation. Regardless of whether a demand transits through the triangle gadget, we obtain an uncrossed edge-disjoint flow by contracting _v_ together with the new degree 2 nodes.

Conversely, suppose that we have an uncrossed edge-disjoint path solution in _G_. At any non-terminal node _v_, if there are two paths using it, since they are non-crossing they can be realized as node-disjoint on the 4-cycle introduced by the reduction. Now consider a terminal node _v_. If it has degree at most 2, then no other path could use edges incident to _v_, so assume it has degree 3. We can convert this to a node-disjoint solution by first letting the terminal _v_ route via the node which subdivided the edge it used in _G_. This allows us to use the edge between the two other subdivided nodes for the transiting demand, thus keeping node disjointness at the gadget.

This completes the proof of the overall reduction.

**Theorem 6.4.** _Suppose that G,H is a planar instance of edge-disjoint paths. We can compute a planar instance_ \(\widehat{G},\widehat{H}\) _of node-disjoint paths such that G,H has an integral uncrossed flow if and only if_ \(\widehat{G},\widehat{H}\) _has (totally) node-disjoint paths for the demands in_ \(\hat{H}\)_. Moreover,_ \(\widehat{G},\widehat{H}\) _can be computed in polytime, and_ \(|V(\widehat{G})|\le c\Delta^3|V(G)|\) _where_ \(\Delta\) _is the maximum degree in G and c is a constant._

## References

