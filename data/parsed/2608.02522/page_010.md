indexed by some counter _j_=0,1_,...,H_. The coloring of the complete graph obtained at the end of the process, at stage _H_, is the final output. At each stage, the construction invokes the pair of maps _f,g_ with the coordinate-covering property stated in Lemma 3.1, as well as large families of well-separated palettes as provided by Lemma 3.2 to define the next coloring based on the previous one. Our proof follows the same general outline.

In the OpenAI construction as well as in our construction, at each stage _j_ of the process, the vertices of the current complete graph are partitioned into vertex-disjoint blocks of equal size, each of which is associated with its individual palette of colors \(P\subseteq[jt]\) from the palette-family given by Lemma 3.2. The coloring of the complete graph will then be constructed in such a way that edge-colors inside a block avoid the colors in the associated palette _P_ entirely (we say they are _missing_), while the remaining colors may be used (we say they are _active_ on the block). Concretely, inside each block one places a copy of the triangle-free edge-coloring obtained from the preceding stage _j_-1, with colors permuted suitably such that they are all active on the respective block.

Throughout the OpenAI construction (and our construction), one crucially maintains, for each appearing color _c_ in the current edge-coloring, a proper _vertex-coloring_ (with few colors) of the spanning subgraph of color _c_-edges. These vertex-colorings are crucial to define the edge-colors of edges _between_ different blocks. Namely, the color of an edge between two blocks associated with palettes _P_ and _Q_ is defined in a certain way based on the maps _f_ and _g_ applied to the vertex-colors of the endpoints of that edge. This is done in such a way that different edges _uv_ and \(u'v\) between two distinct blocks \(A\unknown u\), \(u'\) and \(B\unknown v\) have the following crucial property: If both _uv_ and \(u'v\) have the same color _c_ that is active on _A_, then _u_ and \(u'\) must have the same _vertex-color_ with respect to the proper vertex-coloring of the color _c_-edges. OpenAI’s proof uses this directly to rule out monochromatic triangles between two blocks. In our proof here, we instead use the same property to rule out monochromatic odd cycles of length 2_r_+3 by reducing them, essentially, to monochromatic odd cycles of length 2_r_+1 in an inductively assumed coloring of a smaller complete graph. To make this work, we need to refine OpenAI’s recursive edge-coloring as described before with a second coordinate based on an inductively assumed edge-coloring without monochromatic odd cycles of length at most 2_r_+1. The latter essentially ensures that monochromatic closed odd walks of length 2_r_+3 in our newly constructed edge-colorings cannot repeat vertex-colors, which is used in deriving the final contradiction.

We now move on to the formal proof of Lemma 3.3, from which Theorem 1.7 can then be deduced by some standard asymptotic estimates.

_Proof of Lemma 3.3._ Throughout this proof, we fix the notation<tbc>

\(m=\lceil 2HlogH\rceil,s=m(m+1)+1,t=s\lceil logH\rceil,M_j=jt(0\le j\le H),\)

<tbc>which is consistent with the statement of this lemma as well as with those of Lemmas 3.1 and 3.2.

Put _q=a<sub>r</sub>(H_+1), and fix an edge-coloring

\(\tau:E(K_{H+1})\longrightarrow[q]\)

with no monochromatic member of O_<sub>r</sub>_. Here, we identify the vertex-set of the complete graph _K_<sub>_H_+1</sub> with [_H_+1].

