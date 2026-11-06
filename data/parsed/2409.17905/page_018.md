Subcase 2: three positively oriented faces, say (_ijl),(jkl),(kil_) and one negatively oriented face (_kji_). If the area of (_ijk_) is strictly greater than the areas of (_ijl),(jkl),(kil_), then by definition of the weight of triangle (_ijk_), the tetrahedron has weight at most one. (The other cases will be in the full version).

Subcase 3: four positively oriented faces. Then at least two of these faces are huge and satisfy the assumptions of lemma 4, thus have weight 0. The other two having weight at most 1/2, the tetrahedron has weight at most 1.

This completes the proof of the lower bound.

## 6 Comments

We note that the proof can be greatly simplified for the more modest goal of proving the lower bound 2_n-O_(1). Then, in section 4, when defining the weights of the triangles, we can just give weight 0 to all the triangles of _T_ within some fixed neighborhood of the special vertices (degree 4 or 5). The non-flat triangles with two edges of _T_ all have weight 0 in the neighborhood of the special vertices and 1/2 otherwise. The flow problem can be defined by giving capacity 1/2 near the source and 1/4 everywhere else, and the proof that there is no small cut becomes straightforward. The proof of lemma 4 is greatly simplified, and analyzing the tetrahedral constraints is also simpler. The lower bound 2_n-O_(1) also holds for more general graphs, namely any graph which looks like the triangular lattice except for a constant number of local perturbations.

We conjecture that the same technique can be used to characterize the pairs of polygon triangulations which are at maximum distance apart. In fact, in the sphere triangulation formed by their union, it is known that there is no vertex of degree greater than 6. Since the sum of the degrees of the (_n_+2) vertices is 6(_n_+2)-12, there are only a finite number of cases to consider for the degree sequence of the graph. In some cases, it is easy to see that the two triangulations are not at maximum distance apart (for example, if the sphere triangulation has a vertex of degree 3, or two adjacent vertices of degree 4). In the other cases, we conjecture that the graph looks like the triangular lattice (i.e. there is no short cycle separating the graph into two large connected components: the injectivity radius is not too small), and that the same proof will work.

More generally, the approach of using a potential function may be useful<tbc>

