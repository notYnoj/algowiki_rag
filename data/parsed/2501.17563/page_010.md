<tbc>that is strictly better than any of the STTs that span the false facet, whose value is strictly better than the value of each of the STTs that span this facet, and this is why we work with \(\mathbb{P}'\) rather than P. Observe that a false facet may hide many vertices, but every normal can reveal at most one new vertex when we solve the LP in its direction.<sup>5</sup> We can theoretically find all the hidden vertices by iteratively refining the search, such that whenever a new vertex is found, we compute the new facets and solve the LP in the direction of the corresponding new normal vectors. We can repeat this until all the facets are determined to be true facets. Note that in the first iteration, every facet is due to STT vertices, hence there are multiple optimal STTs for the normal of a facet (exactly those that span the facet). This explains why in Section 2.1 our analysis determines multiple optimal STTs (revisit Figure 2), and more specifically, each point in the facet satisfies the equality \(D\cdot w=30\) where _D_ is the LP depths-vector and _w_=\[3,2,0,2,3,3,10\] is the normal, which tells us in advance that the optimal LP value for the points induced by STTs is 30. Note also that for \(n\ge 3\), multiple normals may result in the same new vertex, as illustrated in Figure 5.

**Definition 2.4** (Primary Directions)**.** We refer to each normal to a facet of the STT induced polytope as a _primary direction_.

Armed with the normals method, all that remains is to enumerate all the STTs, compute their depths-vectors as our _N_ vertices, convert from vertices to facets, enumerate the facets and for each solve the LP and check if the optimum is strictly better than was expected. This is not trivial, and is computationally demanding, therefore we were only able to run it for topologies of size \(n\le 8\). We exhausted all possible topologies up to this size, and detail the high-level results in the caption of Figure 6. See  1 and  6 for the detailed results. The computation was done in _Sage_, and in particular we used sage to enumerate the facets of the polytope defined as the convex hull<tbc>

<sup>5</sup>Assuming "general position", that is, no set of unknown vertices spans a face that is parallel to a false facet. Otherwise, a deterministic solver will still only find one vertex, but randomization may allow finding more.

5.00
z=2.47
-0.06
-0.06
-0.05
x=2.47
y=2.48

5.00
z=2.47
-0.06
-0.06
-0.05
x=2.47
y=2.48

(a) Without \[0.5,0.5,0.5\]

(b) With \[0.5,0.5,0.5\]

Figure 5: A 3-dimensional illustration of how the _Normals Method_ described in Section 2.2 may find a single vertex for multiple false facets. The figures were produced with _Sage_. (a) 7 Facets of the lower envelope of the convex hull of a set of 9 integer vertices _A_={(4,0,0),(0,4,0),(0,0,4),(0,1,2),(0,2,1),(1,0,2),(1,2,0),(2,0,1),(2,1,0)}. (b) By adding to _A_ an extra vertex (0.5,0.5,0.5), 4 of the facets turn out to be false, while every vertex remains a vertex. In both figures, each facet has its own (arbitrary) color. The vertices in this example are not related to STTs, since the smallest "authentic" example is 7-dimensional.

