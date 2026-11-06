**Proof.** If _ijk_ has one edge in _T_, say _jk_, then this edge is far both from the source _i_ and from the sink, hence the dual has capacity 1/4 and \(|w(ijk)|\le 1/4\).

If _ijk_ has no edge in _T_, the weight of _ijk_ is determined by doing a decomposition into three triangles and iterating on each of these triangles until they all have at least one edge in _T_ or have weight 0. Let _ijl_ be the triangle of side _ij_ obtained in this decomposition. If _ijl_ has weight 0, working back up the decomposition, we deduce _w(ijk_)=0. If not, then vertex _l_ is a neighbor either of _i_ or of _j_; say that it is a neighbor of _i_. Thus the edge dual to _il_, being far from both the sink and the source _j_, has capacity 1/4, and \(|w(ijl)|\le 1/4\). Working back up the decomposition, we deduce \(|w(ijk)|\le 1/4\), hence the lemma.

**Lemma 4.** _Large triangles, i.e. such that all three side lengths d(i,j), d(j,k_) _and d(k,i_) _are greater than 10c, have weight 0._

The proof is similar to the proof of the previous lemma and will be in the full version.

## 5.3 Weights of tetrahedra

We will use these lemmas for analyzing the tetrahedral constraints 1.

Case 1: Tetrahedra with 2 faces in _T_: then all the faces are triangles with two or three edges in _T_. Proof by inspection.

Case 2: Tetrahedra with one face in _T_: the weight of the other three faces was defined using flows, precisely so that their contributions cancel. The total weight of the tetrahedron is thus at most 1.

Case 3: Tetrahedra with no face in _T_: this is more difficult. We look at the orientation of the four triangular regions defined by the faces of the tetrahedron.

Subcase 1: two positively oriented and two negatively oriented faces. A positive face must have nonnegative weight, except if it was defined using flows, unoriented and given capacity 1/4. If no face is in that special case, then there are two faces whose weight is between 0 and 1/2 and two faces whose weight is between -1/2 and 0: the total weight of the tetrahedron is thus between -1 and 1. If one of the faces, say _ijk_, is in the special case, then studying the possible positions of the fourth point _l_ of the tetrahedron and using \(c'>3c\) proves that the total weight is at most 1, by arguments similar to the proof of lemma 3. (Proof detailed in full version).

