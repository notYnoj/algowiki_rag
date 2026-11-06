\(w_{i,j}=\left\{\begin{array}{ c c }
0 & X[i]=Y[j] \\
1 & X[i]\neq Y[j].
\end{array}\right.\)

From well-known concentration bounds, for all but a small "tail" fraction of \(x\in\{1,\dots,n\}\), the numbers of 0’s and 1’s in (_x_-1) in binary do not differ by too much more than \(\sqrt{log_2n}\). Therefore, if the total sum of the sequence is \(\varepsilon n\) and \(\varepsilon\) is not too small for the tail to become significant, the total unevenness is roughly bounded by \(\varepsilon n\sqrt{log_2n}\).

## 2.2 Setup and Notation (a Fairly Standard Reduction to Shortest/Longest Path on a 2D Grid)

We reduce ED to a somewhat more general problem of finding the shortest path on a 2D grid<sup>6</sup> with diagonal short-cuts (Definition 5.1 or Fig. 1), where the weight of going from \(\langle\langle u,v\rangle\rangle\) to \(\langle\langle u,v+1\rangle\rangle\) or \(\langle\langle u+1,v\rangle\rangle\) is always 1 (corresponding to insertion or deletion), and the weight of a _short-cut edge_ from \(\langle\langle u,v\rangle\rangle\) to \(\langle\langle u+1,v+1\rangle\rangle\) is either 0 (corresponding to a match) or 1 (corresponding to a substitution). The goal is to find the length (sum of weights) of the shortest path from \(\langle\langle 0,0\rangle\rangle\) to \(\langle\langle n,n\rangle\rangle\). This shortest path problem corresponds to the standard DP algorithm for ED.

Similarly, we reduce LCS to a somewhat more general problem of finding the longest path on a 2D grid with diagonal short-cuts (Definition 5.2), where the weight of going from \(\langle\langle u,v\rangle\rangle\) to \(\langle\langle u,v+1\rangle\rangle\) or \(\langle\langle u+1,v\rangle\rangle\) is always 0, and the weight of a _short-cut edge_ from \(\langle\langle u,v\rangle\rangle\) to \(\langle\langle u+1,v+1\rangle\rangle\) is either 0 (no match) or 1 (match). The goal is to find the length of the longest path from \(\langle\langle 0,0\rangle\rangle\) to \(\langle\langle n,n\rangle\rangle\). This longest path problem corresponds to the standard DP algorithm for LCS.

We now use a 45\(^\circ\)-rotated 2<sup>-polylog_n_</sup>"system (see Fig. 2) to describe 2D grids with the transformation \(\langle\langle u,v\rangle\rangle\rightarrow\langle u+v,v-u+n\rangle\) (Definition 5.3). We use \(\langle x,y\rangle\) when referring to the rotated coordinated system and refer to the x- and y-coordinates defined with respect to the first and second entries of \(\langle x,y\rangle\). In this notation, we are looking for the shortest/longest path from \(\langle 0,n\rangle\) to \(\langle 2n,n\rangle\). We use _column_ to refer to a subset \(\langle x,\cdot\rangle\) of the vertices, and _row_ for \(\langle\cdot,y\rangle\). It is easy to see that any \(\langle 0,n\rangle\)-to-\(\langle 2n,n\rangle\) path visits exactly one vertex of each column. A path _p_ in this notation can be given as a function \(p:\{0,\dots.2n\}\rightarrow\{0,\dots.2n\}\) mapping each x-coordinate to the corresponding y-coordinate. Importantly, such a rotation transform ensures that adjacent vertices the path visits differ in their rows by at most 1 (i.e., \(|p(i)-p(i-1)|\le 1\)), which will be crucial to bounding the curvature of a path.

<sup>6</sup>Do not confuse our 2D grid graphs with the very-closely-related but not identical _alignment graph_ \[CGMW21, CKW23, GK25\], which is not rotated.

t
1
1

Figure 1: Edit distance as a shortest path on 2D grid (standard)

