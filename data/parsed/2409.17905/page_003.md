One drawback is that it involves some tedious case-by-case analysis. We must stress that this tedious work is unnecessary for proving a lower bound of 2_n-O_(1): if we do not insist in proving that the maximum distance is exactly 2_n_-6, but are happy with the less precise lower bound 2_n-O_(1), our proof technique works much more smoothly, and most of the case-by-case analyses disappear. In contrast, the proof of [2], which works by successive refinements of the lower bound, is relatively easy for a lower bound of \(2n-O(\sqrt{n})\), but would require almost as much work to prove 2_n-O_(1) as 2_n_-6.

For other potential applications, we think that our method is more powerful. Instead of relying on the hyperbolic metric, in which solving the problem consists in positioning _n_ points in space adequately (with 3_n_ degrees of freedom), our approach is akin to constructing our own metric, geared to the problem which we wish to solve, and thus there is much more freedom. This will be formalized in the last section.

### Plan of the paper.

In section 2, we leave the binary tree setting and reformulate the problem in terms of flips and triangulations, essentially as in [2]. In section 3, we present the two far-apart triangulations and study the sphere triangulation formed by their union. In section 4, we define a weight function on triangles, using the max-flow min-cut theorem and a partial order on triangles. In section 5, we analyze the change of weights induced by flips, and conclude the proof of the lower bound. In section 6, we discuss connections between this proof, linear programming, and the original proof, as well as other possible applications of the technique.

## 2 Preliminaries : triangulations and tetrahedra

Rather than dealing with binary trees, it is preferable to study the dual problem on triangulations, which have more symmetry.

### 2.1 Binary trees and triangulations

Consider a binary tree with _n_ internal nodes and (_n_+1) external leaves; move the external leaves to infinity by extending the edges to these leaves into half-lines; add a distinguished half-line from the root to infinity. The<tbc>

