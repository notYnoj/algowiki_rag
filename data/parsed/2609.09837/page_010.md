<tbc>and color them _c_. A list coloring is reached by changing only the original vertices. Conversely, if a reachable proper coloring gives _v_ a forbidden color _c_, all its _b_+1 _c_-colored pendent vertices must have changed, which exceeds the budget.

If _C_ is a vertex cover of the source graph, deleting _C_ from the constructed graph leaves a star forest, so \(fvs(H)\le|C|\). For treedepth, put the vertices of _C_ on a chain, put every original vertex outside _C_ below the chain, and put each pendent vertex below its center. This gives \(td(H)\le|C|+2\). See Appendix C.1 for the complete argument.

## 4.2 Swapping and sliding: bandwidth and distance to paths

We use reductions from Equitable Coloring for both the swap and slide variants. For the swap variant, the input graph itself suffices. For the slide variant, connectivity must be ensured without destroying the parameter bound.

**Theorem 5.** _Each of_ Swap-CD _and_ Slide-CD _is_ W[1]_-hard parameterized by q_+bw(_G_) _and by q_+ddp(_G). For the parameter q_+ddp(_G), hardness holds even on graphs with a dominating vertex, and hence on graphs of diameter at most two._

_Proof (sketch)._ Given an Equitable Coloring instance (_G,q_) with _n=aq+r_, initially color the vertices of _G_ so that _r_ colors have multiplicity _a_+1 and all other colors have multiplicity _a_. Every proper target reachable by swaps is an equitable coloring of _G_, since swaps preserve these multiplicities. Conversely, every equitable coloring can be relabeled to have the prescribed multiplicity for each color and, by Lemma 1, can then be reached in at most _n_-1 swaps. This proves the claimed W[1]-hardness of Swap-CD for both parameterizations, without changing the graph.

For the distance-to-disjoint-paths lower bound for both the swap and slide variants, add a universal vertex _z_ of a new, unique color. Arbitrary transpositions still work for swaps and are simulated for slides through the path _u,z,v_. In a proper target, the color of _z_ is unique. Exchanging two color names if necessary yields an equitable coloring of _G_. Removing _z_ recovers _G_, so the parameter increases by at most two.

For the slide variant parameterized by _q_+bw(_G_), attach a chain of _n_ rainbow (_q_+1)-cliques and connect every component of _G_ to a suitable clique. The chain makes the graph connected, while its forced rainbow coloring reserves exactly _n_ copies of each color. A folded bandwidth order places each component connector last and stretches every original distance by a factor of at most two, giving bandwidth at most 2(_q_+2)(bw(_G_)+1). In Appendix C.2 we give the full construction and verify all histogram, reachability, and bandwidth claims.

## 4.3 The four-color lower bound

The preceding reductions bound structural parameters by computable functions of the input parameter. For diameter, we can prove NP-hardness even for a fixed value of the parameter.

