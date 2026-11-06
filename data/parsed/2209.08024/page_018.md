\(\mathcal{T}'[A]\), and store the weight _W(A_). We call a vertex \(v\in V(A)\) that is adjacent to some vertex \(u\in\mathcal{T}'-V(A)\) a _boundary vertex_ of _A_, and maintain a list of boundary vertices for each super-vertex.

Constructing T and _W_ can be done in linear time. Setting up the top trees requires \(\mathcal{O}(\frac{n}{k}\cdot k\mathrm{log}k)=\mathcal{O}(n\mathrm{log}k)\) time.

## Main procedure and recursion.

Below, we describe how to find a centroid and remove it, along with associated virtual vertices. Doing so may split up T (and implicitly T and \(\mathcal{T}'\)) into multiple connected components, on which we recurse. Hence, a recursive step operates on a tree T<sub>r</sub> (a subgraph of T ), a ternarization \(\mathcal{T}'_\mathrm{r}\) of T<sub>r</sub>, and a super-tree T<sub>r</sub> on \(\mathcal{T}'_\mathrm{r}\). Note that only T<sub>r</sub> is explicitly given, whereas T<sub>r</sub> and \(\mathcal{T}'_\mathrm{r}\) are implicit in the super-tree data structure. Our task is to find a centroid _c_ of T<sub>r</sub> and remove it from T<sub>r</sub>, i.e., for each component H of T<sub>r</sub>-_c_, we return a super-tree on a ternarization of H.

## Finding centroids.

We now describe how to find a centroid of \(\mathcal{T}'_\mathrm{r}\) using the super-tree T<sub>r</sub>. Note that, by Lemma 2.5, this is enough to find a centroid of T<sub>r</sub>.

First, we find the centroid _A_<sup>∗</sup> of T<sub>r</sub> with the trivial linear scan described in the introduction.

By Lemma 2.5, a centroid of \(\mathcal{T}'_\mathrm{r}\) must be contained in \(\mathcal{T}'_\mathrm{r}[A^*]\). We now construct a suitable weight function _w_<sup>∗</sup> on _V(A_<sup>∗</sup>) so that we can find a centroid of \(\mathcal{T}'_\mathrm{r}\) within \(\mathcal{T}'_\mathrm{r}[A^*]\). For each \(v\in V(A^*)\), let _C<sub>v</sub>_ be the connected component of \(\mathcal{T}'_\mathrm{r}-(A^*-v)\) that contains _v_. Let \(w^*(v)=w'(C_v)\). Note that \(\mathcal{T}'_\mathrm{r}[A^*]\) and _w_<sup>∗</sup> correspond to the tree and weight function obtained by contracting each _C<sub>v</sub>_ into a single vertex. If _C<sub>v</sub>_={_v_}, i.e., _v_ is not a boundary vertex, then there are no contractions and \(w^*(v)=w'(v)\).

We compute \(w'(C_v)\) for each boundary vertex _v_, and temporarily modify the weight of each _v_ in the top tree on _V(A_<sup>∗</sup>) to match _w_<sup>∗</sup>(_v_). Then, we find a centroid _c_ of \(\mathcal{T}'_\mathrm{r}[A^*]\) w.r.t. _w_<sup>∗</sup>, and undo the weight change.<sup>5</sup>

By Lemma 2.5, a centroid of \(\mathcal{T}'_\mathrm{r}\) must be contained in _C<sub>c</sub>_. We also know a centroid must be contained in _A_<sup>∗</sup>. Thus, by Lemma 2.2, a centroid must be contained in \(C_c\cap A^*=\{c\}\), so _c_ must be a centroid of \((\mathcal{T}'_\mathrm{r},w')\). If _c_ is not virtual, it also is a centroid of (T<sub>r</sub>_,w_). If it is virtual, the linked non-virtual vertex in T<sub>r</sub> is a centroid of (T<sub>r</sub>_,w_).

The running time to find _A_<sup>∗</sup> is O(|_V_(T<sub>r</sub>)|). Computing _w(C<sub>v</sub>_) for each boundary vertex _v_ can be done while traversing T<sub>r</sub>, also in O(|_V_(T<sub>r</sub>)|) time. There are at most \(\mathrm{deg}_{\mathfrak{T}_\mathrm{r}}(A^*)\le|V(\mathfrak{T}_\mathrm{r})|\) boundary vertices, so changing the weights in the top tree takes O(|_V_(T<sub>r</sub>)|log_k_) time.

## Splitting the data structure.

We now remove _c_ and its virtual vertices from \(\mathcal{T}'_\mathrm{r}\) and T<sub>r</sub>. Let _R_ be the set of vertices to be removed. First, we remove each \(v\in R\) from its associated top tree by deleting all of its incident edges. This may split up each of the top trees into multiple new top trees. Each new top tree corresponds to a new super-vertex.

The creation of new super-vertices changes the super-tree, and may even split it up into a super-forest (see Figure 7 for an example). Let _A_ be a super-vertex from which we removed a vertex. For each boundary vertex _u_ of _A_, we find the new top tree that _u_ belongs to. Using this, we can compute all super-edges incident to the new super-vertices (recall that each super-edge corresponds to a normal edge between two boundary vertices in different super-vertices). Finally, we compute the connected components of the new super-forest F<sub>r</sub> using a simple traversal.

Removing a vertex _v_ from the top trees requires \(\mathcal{O}(\mathrm{deg}_{\mathcal{T}_\mathrm{r}^\prime}(v)\mathrm{log}k)\) time. Since each boundary vertex is the endpoint of an edge in T<sub>r</sub>, there are at most O(|_E_(T<sub>r</sub>)|) boundary vertices. The running time of recomputing the super-forest is thus O(|_E_(T<sub>r</sub>)|log_k_+|_V_(F<sub>r</sub>)|).

## Recursion.

After splitting, we recurse on each component of the super-forest that contains more than one (normal) vertex.

<sup>5</sup>Undoing the weight change is necessary, since we re-use the top tree data structures in later steps.

