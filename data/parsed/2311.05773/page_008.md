<tbc>not have too much spill-in from their neighbors - we call these subproblems _unaffected_. Inversion search in unaffected subproblems can be charged to their subinstance. What remains is to then show that many subproblems are actually unaffected. In Lemma 18 we show that at any time, with high probability, at least roughly a 1/(log_N_)<sup>2</sup> fraction of all current problems are unaffected. This requires a careful accounting of how the unaffected nodes are distributed in the tree.

### Putting everything together

As mentioned above, a (log_N_)<sup>2</sup> factor appears while accounting (with high probability) for the affected nodes on one snapshot of the backbone. Accounting over the whole tree, including the pivoting, introduces another log_N_ factor corresponding to the depth of the tree.

## 4 InversionSort: Detailed Analysis

**Definition 6** (Stripe)**.** _Let x be an element of an instance_ I _of bichromatic sorting. The the_ stripe _of x consists of all elements y of_ I _where no element of the other color is between x and y._

**Refinement tree as a trace and mean to analyze:** Looking only at the backbone, the algorithm does an interval refinement. If we look back in time, the final backbone is given by the instance, only the choice of the representative of a stripe is arbitrary (everything else is determined by the instance). In contrast, the evolution of the backbone is very much driven by the random choices of the algorithm and leads to a hierarchy of intervals on the backbone. A new inversion and the pivoting steps split one interval of the backbone (not to be confused with a bucket that somehow spans two intervals of the backbone) into three, as detailed in the following definition.

**Definition 7** (Refinement tree)**.** _The root node of the tree has as bounding pivots the artificial smallest red and largest blue element. Every node v of the tree has two pivots b<sub>v</sub> and r<sub>v</sub> of the (final) backbone associated to it with the guarantee that b<sub>v</sub> and r<sub>v</sub> were neighbors on the backbone at some_<tbc>

bv
rv
backbone
y
X

Figure 1: The difference between a subproblem and a subinstance. _b<sub>v</sub>_ and _r<sub>v</sub>_ are on the backbone, and _y\<x_ is the inversion found between them. The stripes in the subinstance (_y,x_) are solid, whereas the stripes in the subproblem (_y,x_) are the union of the solid and shaded stripes.

