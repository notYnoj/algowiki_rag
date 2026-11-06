<tbc>of the STTs. For more on the code, see Appendix B. Due to the computational complexity of converting vertices to facets, we were unable to finish an iterative scan for all the possible vertices. To clarify, we were able to fully scan all the primary directions for each topology, and determine new non-integer vertices in seven of them. However, we did not have enough resources to compute the new facets when taking into account the newly found vertices for the topologies with 8 nodes. This failed even when only 2 new vertices were found. We were only able to run this second phase on the topology with 7 nodes, and for it we determined that no additional new vertices exist. (The second phase had 6385 normals, compared to 6364 primary directions.)

In general, many of the vertices, and the primary directions, may be symmetric. Symmetries arise due to automorphisms of the topology. If \(\pi:U\rightarrow U\) is an automorphism, then we can define an automorphism on the (_X,Z,D_)-space by mapping indices according to \(\pi\). For example, it maps \(D_i\rightarrow D_{\pi(i)}\) and \(X_{ij}\rightarrow X_{\pi(i),\pi(j)}\). Since the "names" of the nodes are arbitrary, it is clear why a vertex _P_ translates by \(\pi\) to another vertex \(P'\), and we say that _P_ and \(P'\) are _symmetric_ to each other. Note that _P_ and \(P'\) have the same coordinate values, permuted by \(\pi\). There are additional cases where primary directions can look symmetric, see Remark 3.16.

We follow with some additional information on the topology _U_<sub>(7,3)</sub> used in the proof of Theorem 2.2. Its LP has a total of 39 false facets which correspond to 9 non-integer vertices. By the automorphism symmetry of the topology it is natural that these numbers are divisible by 3. There are 7 normals, such that one of them has 3 symmetric copies and each of the other six has 6 copies. These normals are (the first was used in Theorem 2.2): _w_=(3,2,0,2,3,3,10),(14,6,0,10,32,5,7),(16,6,0,11,34,4,8),(39,11,0,6,21,4,8),(18,6,0,10,36,5,7),(18,5,0,3,6,4,5),(9,4,0,7,22,4,5). Information about other trees is summarized in  1.

We conclude our findings with an interesting remark.

\begin{tabular}{cccccccc}
Topology & \multirow{2}{*}{STTs} & Primary & False & Frac & Frac Vs & _D_-space & _XZD_-space \\
_U_<sub>(_n,i_)</sub> & & Directions & Facets & Vs & Classes & denom. & denom. \\
(3,0) & 5 & 9 & 0 & . & . & {1} & {1} \* \\
(4,0) & 14 & 32 & 0 & . & . & {1} & {1} \* \\
(4,1) & 16 & 32 & 0 & . & . & {1} & {1} \* \\
(5,0) & 42 & 145 & 0 & . & . & {1} & {1, 2, 3} \* \\
(5,1) & 51 & 152 & 0 & . & . & {1} & {1} \* \\
(5,2) & 65 & 161 & 0 & . & . & {1} & {1} \* \\
(7,3) & 662 & 6364 & 39 & 9 & 2 & {1, 2} & {1, 2} \\
(8,4) & 2416 & 48291 & 362 & 65 & 38 & {1, 2} & {1, 2, 3} \\
(8,5) & 2952 & 56376 & 120 & 2 & 1 & {1, 2} & {1, 2, 3} \\
(8,6) & 2802 & 56724 & 10 & 2 & 1 & {1, 2} & {1, 2, 3, 4} \\
(8,11) & 3988 & 54201 & 78 & 18 & 4 & {1, 2} & {1, 2} \\
(8,12) & 3332 & 56404 & 528 & 60 & 24 & {1, 2} & {1, 2, 3} \\
(8,13) & 4076 & 65733 & 946 & 28 & 4 & {1, 2} & {1, 2} \\
\end{tabular}

1: Summary of all tree topologies up to \(n\le 5\) nodes and those with non-STT _D_-space vertices up to \(n\le 8\) (for more topologies, see  6). Following, _italicized_ refer to column titles. _Frac, Vs_ and _denoms_. are short for fractional, vertices and denominators. _Topology U_<sub>(_n,i_)</sub> correspond to Figure 6. All columns are with respect to _D_- space except for the last. Out of all _Primary Directions_ (Definition 2.4) only few determine _False Facets_, which reveal _Frac Vs_. These vertices all happen to be half-integer (_D-space denom._ of 1 and 2). _Frac Vs Classes_ is the number of equivalence classes of non-STT vertices by automorphic symmetries. _XZD-space denom._ lists denominators of coordinates in vertices of the LP polytope. We were able to enumerate all the vertices for topologies marked with ∗. For the rest, we sampled random vertices by solving the LP in random _XZD_-directions. Lists without ∗ may be incomplete: For example, every extension of _U_<sub>(5,0)</sub> should have third-integer vertices by Theorem 3.12, yet _U_<sub>(7,3)</sub> (allegedly) does not.

