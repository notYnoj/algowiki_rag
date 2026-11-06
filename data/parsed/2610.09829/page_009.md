<tbc>distinct paths \(P_1,P_2\in\mathcal{Q}\) such that \(C=P_1\cup P_2\). With the above family of paths Q at hand, we can simply "guess" the exact subset of these paths forming the non-tree cycles in the solution we are looking for. We remark that although the number of non-tree cycles can be as large as \(\Omega(k^2)\), guessing the paths requires iterating over only 2<sup>O(_k_)</sup> subsets of Q, as opposed to the \(2^{\Omega(k^2)}\) choices needed to guess the exact set of non-tree cycles in the solution.

It remains to handle the tree cycles, which are exactly the nodes of the laminar shortest cycles tree T . We proceed by a bottom-up dynamic programming over T , starting from its leaves, as follows. At a node \(\alpha\) of T , we seek a solution that contains \(\alpha\) and some descendants of \(\alpha\), and we assume that for every strict descendant of \(\alpha\) the corresponding dynamic programming entries have already been computed. We note that the number of nodes in T may not be bounded by a function of _k_, and thus we do not know which descendants to query directly. However, as the number of leaves in T is bounded, so is the number of nodes of degree at least 3, as well as the number of inclusion-maximal paths in T containing only nodes of degree 2. So intuitively, we can guess whether the "closest" descendant of \(\alpha\) in the solution is a leaf, a node of degree at least three, or a node lying on a maximal degree-2 path (and how many solution cycles appear below it).

Once we have the above information (the number of possible guesses is 2<sup>O(_k_)</sup>), we know precisely the descendants that are leaves or nodes of degree at least three, and the unknown ones lie on maximal degree-2 paths. The crucial property, which holds only for packing edge-disjoint cycles, is the following: if a solution exists, then there also exists a solution that satisfies "strict laminarity" in the following sense: for any two distinct shortest cycles \(C,C'\) in the solution, one of the following holds: i) _C_ is embedded strictly inside (modulo the vertices) the region bounded by \(C'\), ii) \(C'\) is embedded strictly inside (modulo the vertices) the region bounded by _C_, or iii) the regions bounded by the curves _C_ and \(C'\) are disjoint (modulo the vertices). In the above, (roughly speaking) the region bounded by a cycle _C_ is always the one not containing the outer face. Now to identify the<tbc>

Po
P1
C1
C2
P2
S
C3
t
C4
C5
P3
Cr
(a) Plane graph G. = P00 P3 is a splittable-node with C (Cr)={C1, C2, C3}, where C1=P00 P1, C2=P10 P2, and C3=P20 P3. C1 and C2 are leaf cycles; C3 is an unsplittable- node with C u(C3)={C4,C5}. The shortest cycles formed by paths P0 and P2, and by paths P1 and P3 are non-tree cycles. (a) Plane graph G. = P00 P3 is a splittable-node with C (Cr)={C1, C2, C3}, where C1=P00 P1, C2=P10 P2, and C3=P20 P3. C1 and C2 are leaf cycles; C3 is an unsplittable- node with C u(C3)={C4,C5}. The shortest cycles formed by paths P0 and P2, and by paths P1 and P3 are non-tree cycles. (b) LSCT T(G) rooted at Cr.

Figure 4: Example of laminar shortest cycles tree construction (Definition 5.4).

