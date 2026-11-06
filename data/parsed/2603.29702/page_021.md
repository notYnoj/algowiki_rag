**Definition 5.1** (Edit Distance Grid Graph)**.** The Edit Distance Grid Graph is a grid graph with diagonal shortcuts that can be used to compute ED(_X,Y_), and is defined as follows:

**Vertices** The grid points of \([0,n_X]\times[0,n_Y]\). The vertex at the intersection of the _x_-th column and the _y_-th row is \(\langle\langle x,y\rangle\rangle\);

**Edges** The set of edges includes standard grid edges and diagonal shortcut edges:

• Standard grid edges from \(\langle\langle u,v\rangle\rangle\) to \(\langle\langle u,v+1\rangle\rangle\) or \(\langle\langle u+1,v\rangle\rangle\), always with weight 1 (corresponding to insertion or deletion);<tbc>

• Diagonal shortcut edges from \(\langle\langle u,v\rangle\rangle\) to \(\langle\langle u+1,v+1\rangle\rangle\), whose weight is 0 if _X_\[_u_\]=_Y_\[_v_\] (match) and 1 otherwise (substitution).

**Objective** ED(_X,Y_) is the length (sum of weights) of the shortest (0,0)-(_n<sub>X</sub>,n<sub>Y</sub>_) path.

Given two strings _X,Y_ of length _n<sub>X</sub>_ and _n<sub>Y</sub>_, we define an edge-weighted graph, corresponding to the profit of moving between states in the standard quadratic-time DP algorithm for LCS:

**Definition 5.2** (LCS Grid Graph)**.** The LCS Grid Graph is a grid graph with diagonal shortcuts that can be used to compute LCS(_X,Y_), and is defined as follows:

**Vertices** The grid points of \([0,n_X]\times[0,n_Y]\). The vertex at the intersection of the _x_-th column and the _y_-th row is \(\langle\langle x,y\rangle\rangle\);

**Edges** The set of edges includes standard grid edges and diagonal shortcut edges:

• Standard grid edges from \(\langle\langle u,v\rangle\rangle\) to \(\langle\langle u,v+1\rangle\rangle\) or \(\langle\langle u+1,v\rangle\rangle\), always with weight 0 (corresponding to no match between the two characters);<tbc>

• Diagonal shortcut edges from \(\langle\langle u,v\rangle\rangle\) to \(\langle\langle u+1,v+1\rangle\rangle\), whose weight is 1 if _X_\[_u_\]=_Y_\[_v_\] (match) and 0 otherwise (no match).

**Objective** LCS(_X,Y_) is the length (sum of weights) of the longest (0,0)-(_n<sub>X</sub>,n<sub>Y</sub>_) path.

## 5.1.2 Rotated Grid Graph: \(\langle\langle u,v\rangle\rangle\rightarrow\langle u+v,v-u+n_X\rangle\)

To describe our algorithm, we will rotate the grids by 45 degrees and obtain graphs where for any fixed path, each column (corresponding to a diagonal in the original grid) is visited exactly once.

**Definition 5.3** (Rotated Edit Distance Grid Graph)**.** We use \(\langle\langle x,y\rangle\rangle\) to denote a vertex in the (original) Edit Distance Grid Graph at the intersection of column _x_ and row _y_ and \(\langle x,y\rangle\) to denote a vertex in the Rotated Edit Distance Grid Graph at the intersection of column _x_ and row _y_. The description of the new graph on the rotated grid is as follows:

**Vertices** The vertex for \(\langle\langle u,v\rangle\rangle\) in the original grid corresponds to \(\langle u+v,v-u+n_X\rangle\) on the new grid;

**Edges** We start with the same set of edges as in the original graph. Then, we divide each shortcut edge with weight \(w(\in\{0,1\})\) from \(\langle u,v\rangle\) to \(\langle u+2,v\rangle\) into two edges, one from \(\langle u,v\rangle\) to \(\langle u+1,v\rangle\) with weight 0 and the other from \(\langle u+1,v\rangle\) to \(\langle u+2,v\rangle\) with weight _w_.

**Objective** The length of the shortest \(\langle 0,n_X\rangle\)-\(\langle n_X+n_Y,n_Y\rangle\) path equals ED(_X,Y_).

