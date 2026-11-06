PMC. This PMC neighborhood naturally defines a directed PMC-graph, where the vertices are PMCs of _G_ and arcs are given by the ordered pairs of N.

Figure 9: Consider graph _G_ with the PMC \(\Omega'\) in the light orange area. On the left, a first choice for _u_<sup>∗</sup> and _b_<sup>∗</sup> produces a potential neighbor of \(\Omega'\): set _N_\[_u_<sup>∗</sup>\] is drawn with bold orange lines around vertices, the _X_<sup>∗</sup>-close (_b_<sup>∗</sup>_,u_<sup>∗</sup>)-separator _S_<sup>∗</sup> contains the vertices filled with green, and the final set \(\Omega=X^*\cap C_G[b^*,S^*]\) is surrounded in blue. \(\Omega\) is a PMC. On the right, given the same _G_ and \(\Omega'\), a different choice for _u_<sup>∗</sup> and _b_<sup>∗</sup> produces a set \(\tilde{\Omega}\) which is not a PMC. Indeed, the reachability between _x_ and _y_ is not satisfied.

PMC-BFS, whose pseudocode is given in Algorithm 2, consists in a traversal of this PMC-graph. It takes as input a graph _G_ together with a starting set of PMCs \(\widehat{\Pi}\) which is put into the initial queue of the BFS. It returns the set of PMCs visited during the traversal, excluding the initial ones in \(\widehat{\Pi}\).

As a small - but very important - implementation remark, we specify briefly here how we can avoid duplication of PMCs, more concretely how we can check fast whether a given PMC was already visited/stored in the enumeration process. This is a test we execute at line 9 of Algorithm 2 for example. Indeed, computing such a test in exponential time would ruin our efforts to obtain overall output-linear time. We show, given a large set \(\Pi\) of PMCs, how to check whether some PMC \(\Omega\) is included into it or not, in time _n_<sup>_O_(1)</sup>. We actually store our PMCs in a binary tree where edges at depth _i_ represent the addition or the exclusion of vertex _v<sub>i</sub>_ in the PMC. In such data structure, any path from the root to a leaf represents a unique PMC. We can not only verify the presence of a PMC but also add one in a running time _O(n_), depending only on the depth of the tree. Such a data structure is also used in PMC-Traversal, see lines 8, 9, 11, 14 of Algorithm 3. Such a data structure is very common in enumeration algorithms: as an example, it was used to store minimal separators in the polynomial-delay algorithm of Berry _et al._ \[1\] under the name of "SEARCH-INSERT" procedure.

The pseudocode of PMC-Traversal is provided in Algorithm 3. The fourth step of BT-enum is replaced by the launch of PMC-BFS (line 13), where the starting set \(\widehat{\Pi}\) is filled up (line 12) with the PMCs already listed in the first three steps (respectively lines 8, 9, 11).

Ω
b*
u*
Ω'

Ω
u*
x
y
b*
Ω'

(a) Example of a PMC \(\Omega'\) admitting a neighbor \(\Omega\) for a certain choice of _u_<sup>∗</sup> and _b_<sup>∗</sup>.

(b) Another choice of _u_<sup>∗</sup> and _b_<sup>∗</sup> leads to a set \(\tilde{\Omega}\) which is not a PMC: \(y\notin R_G(x,\tilde{\Omega})\).

