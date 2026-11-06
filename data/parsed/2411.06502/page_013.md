**Figure 4** To compute \(\mathrm{sim}(\mathbf{F},\mathbf{F}')\) for the two depicted trees **T** and \(\mathbf{T}'\) under Assumption B, we can use the same visualization approach as before. Specifically, we overlay two tree alignment graphs corresponding to the concatenated left and right subtrees, tracing two paths that, whenever they intersect at two spine nodes, provide the possibility to map them. These graphs correspond to \(L_1L_2\cdots L_m\) vs. \(L'_1L'_2\cdots L'_{m^\prime}\) and \(\mathrm{rev}(R_1R_2\cdots R_m)\) vs. \(\mathrm{rev}(R'_1R'_2\cdots R'_{m^\prime})\), shown in blue and teal, respectively. Given the similarity values \(\mathrm{sim}(\mathrm{sub}(v),\mathrm{sub}(v'))\) for all \((v,v')\in(\mathbf{F}\times\mathbf{F}')\backslash(\mathbf{S}\times\mathbf{S}')\), we can construct these trees.

In Spine Edit Distance (SED), instead of computing only \(\mathrm{sim}(\mathbf{F},\mathbf{F}')\), we also need to determine \(\mathrm{sim}(\mathrm{sub}(s),\mathrm{sub}(s'))\) for all \((s,s')\in(\mathbf{S}\times\mathbf{S}')\). Fortunately, by employing a similar divide-and-conquer approach as used for caterpillars, computing \(\mathrm{sim}(\mathbf{F},\mathbf{F}')\) naturally leads to obtaining these values as well.

When designing such a divide-and-conquer scheme, the subproblems must be indexed by rectangles whose edges align with coordinates corresponding to spine nodes. This ensures that no diagonal edges in the tree alignment graphs "jump over" the sides of the rectangle, allowing for a "clean" partitioning into subproblems.

As with caterpillar trees, removing Assumption B would introduce a third path between the two existing ones.

F
F'
S1
S'
L1
R1
L'
R'
S2
S'
L2
R2
L'
R'
S
S'
S'
m'
1
Lm-1
Rm-1
L'
R'
m'
1
S'
S'
m'
S
m'
Lm
Rm
L'
R'
m'

